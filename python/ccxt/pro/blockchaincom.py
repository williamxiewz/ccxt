# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

import ccxt.async_support
from ccxt.async_support.base.ws.cache import ArrayCache, ArrayCacheBySymbolById, ArrayCacheByTimestamp
from ccxt.base.types import Balances, Int, Order, OrderBook, Str, Ticker, Trade
from ccxt.async_support.base.ws.client import Client
from typing import List
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import NotSupported


class blockchaincom(ccxt.async_support.blockchaincom):

    def describe(self):
        return self.deep_extend(super(blockchaincom, self).describe(), {
            'has': {
                'ws': True,
                'watchBalance': True,
                'watchTicker': True,
                'watchTickers': False,
                'watchTrades': True,
                'watchMyTrades': False,
                'watchOrders': True,
                'watchOrderBook': True,
                'watchOHLCV': True,
            },
            'urls': {
                'api': {
                    'ws': 'wss://ws.blockchain.info/mercury-gateway/v1/ws',
                },
            },
            'options': {
                'ws': {
                    'options': {
                        'headers': {
                            'Origin': 'https://exchange.blockchain.com',
                        },
                    },
                    'noOriginHeader': False,
                },
            },
            'streaming': {
            },
            'exceptions': {
            },
            'timeframes': {
                '1m': '60',
                '5m': '300',
                '15m': '900',
                '1h': '3600',
                '6h': '21600',
                '1d': '86400',
            },
        })

    async def watch_balance(self, params={}) -> Balances:
        """
        watch balance and get the amount of funds available for trading or funds locked in orders
        :see: https://exchange.blockchain.com/api/#balances
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `balance structure <https://docs.ccxt.com/#/?id=balance-structure>`
        """
        await self.authenticate(params)
        messageHash = 'balance'
        url = self.urls['api']['ws']
        subscribe: dict = {
            'action': 'subscribe',
            'channel': 'balances',
        }
        request = self.deep_extend(subscribe, params)
        return await self.watch(url, messageHash, request, messageHash, request)

    def handle_balance(self, client: Client, message):
        #
        #  subscribed
        #     {
        #         "seqnum": 1,
        #         "event": "subscribed",
        #         "channel": "balances",
        #         "local_currency": "USD",
        #         "batching": False
        #     }
        #  snapshot
        #     {
        #         "seqnum": 2,
        #         "event": "snapshot",
        #         "channel": "balances",
        #         "balances": [
        #           {
        #             "currency": "BTC",
        #             "balance": 0.00366963,
        #             "available": 0.00266963,
        #             "balance_local": 38.746779155,
        #             "available_local": 28.188009155,
        #             "rate": 10558.77
        #           },
        #            ...
        #         ],
        #         "total_available_local": 65.477864168,
        #         "total_balance_local": 87.696634168
        #     }
        #
        event = self.safe_string(message, 'event')
        if event == 'subscribed':
            return
        result: dict = {'info': message}
        balances = self.safe_value(message, 'balances', [])
        for i in range(0, len(balances)):
            entry = balances[i]
            currencyId = self.safe_string(entry, 'currency')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_string(entry, 'available')
            account['total'] = self.safe_string(entry, 'balance')
            result[code] = account
        messageHash = 'balance'
        self.balance = self.safe_balance(result)
        client.resolve(self.balance, messageHash)

    async def watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={}) -> List[list]:
        """
        watches historical candlestick data containing the open, high, low, and close price, and the volume of a market.
        :see: https://exchange.blockchain.com/api/#prices
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents. Allows '1m', '5m', '15m', '1h', '6h' '1d'. Can only watch one timeframe per symbol.
        :param int [since]: timestamp in ms of the earliest candle to fetch
        :param int [limit]: the maximum amount of candles to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns int[][]: A list of candles ordered, open, high, low, close, volume
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        interval = self.safe_string(self.timeframes, timeframe, timeframe)
        messageHash = 'ohlcv:' + symbol
        request = {
            'action': 'subscribe',
            'channel': 'prices',
            'symbol': market['id'],
            'granularity': self.parse_number(interval),
        }
        request = self.deep_extend(request, params)
        url = self.urls['api']['ws']
        ohlcv = await self.watch(url, messageHash, request, messageHash, request)
        if self.newUpdates:
            limit = ohlcv.getLimit(symbol, limit)
        return self.filter_by_since_limit(ohlcv, since, limit, 0, True)

    def handle_ohlcv(self, client: Client, message):
        #
        #  subscribed
        #     {
        #         "seqnum": 0,
        #         "event": "subscribed",
        #         "channel": "prices",
        #         "symbol": "BTC-USDT",
        #         "granularity": 60
        #     }
        #
        #  updated
        #     {
        #         "seqnum": 1,
        #         "event": "updated",
        #         "channel": "prices",
        #         "symbol": "BTC-USD",
        #         "price": [1660085580000, 23185.215, 23185.935, 23164.79, 23169.97, 0]
        #     }
        #
        event = self.safe_string(message, 'event')
        if event == 'rejected':
            jsonMessage = self.json(message)
            raise ExchangeError(self.id + ' ' + jsonMessage)
        elif event == 'updated':
            marketId = self.safe_string(message, 'symbol')
            symbol = self.safe_symbol(marketId, None, '-')
            messageHash = 'ohlcv:' + symbol
            request = self.safe_value(client.subscriptions, messageHash)
            timeframeId = self.safe_number(request, 'granularity')
            timeframe = self.find_timeframe(timeframeId)
            ohlcv = self.safe_value(message, 'price', [])
            self.ohlcvs[symbol] = self.safe_value(self.ohlcvs, symbol, {})
            stored = self.safe_value(self.ohlcvs[symbol], timeframe)
            if stored is None:
                limit = self.safe_integer(self.options, 'OHLCVLimit', 1000)
                stored = ArrayCacheByTimestamp(limit)
                self.ohlcvs[symbol][timeframe] = stored
            stored.append(ohlcv)
            client.resolve(stored, messageHash)
        elif event != 'subscribed':
            raise NotSupported(self.id + ' ' + self.json(message))

    async def watch_ticker(self, symbol: str, params={}) -> Ticker:
        """
        watches a price ticker, a statistical calculation with the information calculated over the past 24 hours for a specific market
        :see: https://exchange.blockchain.com/api/#ticker
        :param str symbol: unified symbol of the market to fetch the ticker for
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict: a `ticker structure <https://docs.ccxt.com/#/?id=ticker-structure>`
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        url = self.urls['api']['ws']
        messageHash = 'ticker:' + symbol
        request = {
            'action': 'subscribe',
            'channel': 'ticker',
            'symbol': market['id'],
        }
        request = self.deep_extend(request, params)
        return await self.watch(url, messageHash, request, messageHash)

    def handle_ticker(self, client: Client, message):
        #
        #  subscribed
        #     {
        #         "seqnum": 0,
        #         "event": "subscribed",
        #         "channel": "ticker",
        #         "symbol": "BTC-USD"
        #     }
        #  snapshot
        #     {
        #         "seqnum": 1,
        #         "event": "snapshot",
        #         "channel": "ticker",
        #         "symbol": "BTC-USD",
        #         "price_24h": 23071.4,
        #         "volume_24h": 236.28398636,
        #         "last_trade_price": 23936.4,
        #         "mark_price": 23935.335240262
        #     }
        # update
        #     {
        #         "seqnum": 2,
        #         "event": "updated",
        #         "channel": "ticker",
        #         "symbol": "BTC-USD",
        #         "mark_price": 23935.242443617
        #     }
        #
        event = self.safe_string(message, 'event')
        marketId = self.safe_string(message, 'symbol')
        market = self.safe_market(marketId)
        symbol = market['symbol']
        ticker = None
        if event == 'subscribed':
            return
        elif event == 'snapshot':
            ticker = self.parse_ticker(message, market)
        elif event == 'updated':
            lastTicker = self.safe_value(self.tickers, symbol)
            ticker = self.parse_ws_updated_ticker(message, lastTicker, market)
        messageHash = 'ticker:' + symbol
        self.tickers[symbol] = ticker
        client.resolve(ticker, messageHash)

    def parse_ws_updated_ticker(self, ticker, lastTicker=None, market=None):
        #
        #     {
        #         "seqnum": 2,
        #         "event": "updated",
        #         "channel": "ticker",
        #         "symbol": "BTC-USD",
        #         "mark_price": 23935.242443617
        #     }
        #
        marketId = self.safe_string(ticker, 'symbol')
        symbol = self.safe_symbol(marketId, None, '-')
        last = self.safe_string(ticker, 'mark_price')
        return self.safe_ticker({
            'symbol': symbol,
            'timestamp': None,
            'datetime': None,
            'high': None,
            'low': None,
            'bid': None,
            'bidVolume': None,
            'ask': None,
            'askVolume': None,
            'vwap': None,
            'open': self.safe_string(lastTicker, 'open'),
            'close': None,
            'last': last,
            'previousClose': self.safe_string(lastTicker, 'close'),
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_string(lastTicker, 'baseVolume'),
            'quoteVolume': None,
            'info': self.extend(self.safe_value(lastTicker, 'info', {}), ticker),
        }, market)

    async def watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={}) -> List[Trade]:
        """
        get the list of most recent trades for a particular symbol
        :see: https://exchange.blockchain.com/api/#trades
        :param str symbol: unified symbol of the market to fetch trades for
        :param int [since]: timestamp in ms of the earliest trade to fetch
        :param int [limit]: the maximum amount of    trades to fetch
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `trade structures <https://docs.ccxt.com/#/?id=public-trades>`
        """
        await self.load_markets()
        market = self.market(symbol)
        symbol = market['symbol']
        url = self.urls['api']['ws']
        messageHash = 'trades:' + symbol
        request = {
            'action': 'subscribe',
            'channel': 'trades',
            'symbol': market['id'],
        }
        request = self.deep_extend(request, params)
        trades = await self.watch(url, messageHash, request, messageHash, request)
        return self.filter_by_since_limit(trades, since, limit, 'timestamp', True)

    def handle_trades(self, client: Client, message):
        #
        #  subscribed
        #     {
        #         "seqnum": 0,
        #         "event": "subscribed",
        #         "channel": "trades",
        #         "symbol": "BTC-USDT"
        #     }
        #  updates
        #     {
        #         "seqnum": 1,
        #         "event": "updated",
        #         "channel": "trades",
        #         "symbol": "BTC-USDT",
        #         "timestamp": "2022-08-08T17:23:48.163096Z",
        #         "side": "sell",
        #         "qty": 0.083523,
        #         "price": 23940.67,
        #         "trade_id": "563078810223444"
        #     }
        #
        event = self.safe_string(message, 'event')
        if event != 'updated':
            return
        marketId = self.safe_string(message, 'symbol')
        symbol = self.safe_symbol(marketId)
        market = self.safe_market(marketId)
        messageHash = 'trades:' + symbol
        stored = self.safe_value(self.trades, symbol)
        if stored is None:
            limit = self.safe_integer(self.options, 'tradesLimit', 1000)
            stored = ArrayCache(limit)
            self.trades[symbol] = stored
        parsed = self.parse_ws_trade(message, market)
        stored.append(parsed)
        self.trades[symbol] = stored
        client.resolve(self.trades[symbol], messageHash)

    def parse_ws_trade(self, trade, market=None):
        #
        #     {
        #         "seqnum": 1,
        #         "event": "updated",
        #         "channel": "trades",
        #         "symbol": "BTC-USDT",
        #         "timestamp": "2022-08-08T17:23:48.163096Z",
        #         "side": "sell",
        #         "qty": 0.083523,
        #         "price": 23940.67,
        #         "trade_id": "563078810223444"
        #     }
        #
        marketId = self.safe_string(trade, 'symbol')
        datetime = self.safe_string(trade, 'timestamp')
        return self.safe_trade({
            'id': self.safe_string(trade, 'trade_id'),
            'timestamp': self.parse8601(datetime),
            'datetime': datetime,
            'symbol': self.safe_symbol(marketId, market, '-'),
            'order': None,
            'type': None,
            'side': self.safe_string(trade, 'side'),
            'takerOrMaker': None,
            'price': self.safe_string(trade, 'price'),
            'amount': self.safe_string(trade, 'qty'),
            'cost': None,
            'fee': None,
            'info': trade,
        }, market)

    async def watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={}) -> List[Order]:
        """
        watches information on multiple orders made by the user
        :see: https://exchange.blockchain.com/api/#mass-order-status-request-ordermassstatusrequest
        :param str symbol: unified market symbol of the market orders were made in
        :param int [since]: the earliest time in ms to fetch orders for
        :param int [limit]: the maximum number of order structures to retrieve
        :param dict [params]: extra parameters specific to the exchange API endpoint
        :returns dict[]: a list of `order structures <https://docs.ccxt.com/#/?id=order-structure>`
        """
        await self.load_markets()
        await self.authenticate()
        if symbol is not None:
            market = self.market(symbol)
            symbol = market['symbol']
        url = self.urls['api']['ws']
        message: dict = {
            'action': 'subscribe',
            'channel': 'trading',
        }
        messageHash = 'orders'
        request = self.deep_extend(message, params)
        orders = await self.watch(url, messageHash, request, messageHash)
        if self.newUpdates:
            limit = orders.getLimit(symbol, limit)
        return self.filter_by_symbol_since_limit(orders, symbol, since, limit, True)

    def handle_orders(self, client: Client, message):
        #
        #     {
        #         "seqnum": 1,
        #         "event": "rejected",
        #         "channel": "trading",
        #         "text": "Not subscribed to channel"
        #     }
        #  snapshot
        #     {
        #         "seqnum": 2,
        #         "event": "snapshot",
        #         "channel": "trading",
        #         "orders": [
        #           {
        #             "orderID": "562965341621940",
        #             "gwOrderId": 181011136260,
        #             "clOrdID": "016caf67f7a94508webd",
        #             "symbol": "BTC-USD",
        #             "side": "sell",
        #             "ordType": "limit",
        #             "orderQty": 0.000675,
        #             "leavesQty": 0.000675,
        #             "cumQty": 0,
        #             "avgPx": 0,
        #             "ordStatus": "open",
        #             "timeInForce": "GTC",
        #             "text": "New order",
        #             "execType": "0",
        #             "execID": "21415965325",
        #             "transactTime": "2022-08-08T23:31:00.550795Z",
        #             "msgType": 8,
        #             "lastPx": 0,
        #             "lastShares": 0,
        #             "tradeId": "0",
        #             "fee": 0,
        #             "price": 30000,
        #             "marginOrder": False,
        #             "closePositionOrder": False
        #           }
        #         ],
        #         "positions": []
        #     }
        #  update
        #     {
        #         "seqnum": 3,
        #         "event": "updated",
        #         "channel": "trading",
        #         "orderID": "562965341621940",
        #         "gwOrderId": 181011136260,
        #         "clOrdID": "016caf67f7a94508webd",
        #         "symbol": "BTC-USD",
        #         "side": "sell",
        #         "ordType": "limit",
        #         "orderQty": 0.000675,
        #         "leavesQty": 0.000675,
        #         "cumQty": 0,
        #         "avgPx": 0,
        #         "ordStatus": "cancelled",
        #         "timeInForce": "GTC",
        #         "text": "Canceled by User",
        #         "execType": "4",
        #         "execID": "21416034921",
        #         "transactTime": "2022-08-08T23:33:25.727785Z",
        #         "msgType": 8,
        #         "lastPx": 0,
        #         "lastShares": 0,
        #         "tradeId": "0",
        #         "fee": 0,
        #         "price": 30000,
        #         "marginOrder": False,
        #         "closePositionOrder": False
        #     }
        #
        event = self.safe_string(message, 'event')
        messageHash = 'orders'
        cachedOrders = self.orders
        if cachedOrders is None:
            limit = self.safe_integer(self.options, 'ordersLimit', 1000)
            self.orders = ArrayCacheBySymbolById(limit)
        if event == 'subscribed':
            return
        elif event == 'rejected':
            raise ExchangeError(self.id + ' ' + self.json(message))
        elif event == 'snapshot':
            orders = self.safe_value(message, 'orders', [])
            for i in range(0, len(orders)):
                order = orders[i]
                parsedOrder = self.parse_ws_order(order)
                cachedOrders.append(parsedOrder)
        elif event == 'updated':
            parsedOrder = self.parse_ws_order(message)
            cachedOrders.append(parsedOrder)
        self.orders = cachedOrders
        client.resolve(self.orders, messageHash)

    def parse_ws_order(self, order, market=None):
        #
        #     {
        #         "seqnum": 3,
        #         "event": "updated",
        #         "channel": "trading",
        #         "orderID": "562965341621940",
        #         "gwOrderId": 181011136260,
        #         "clOrdID": "016caf67f7a94508webd",
        #         "symbol": "BTC-USD",
        #         "side": "sell",
        #         "ordType": "limit",
        #         "orderQty": 0.000675,
        #         "leavesQty": 0.000675,
        #         "cumQty": 0,
        #         "avgPx": 0,
        #         "ordStatus": "cancelled",
        #         "timeInForce": "GTC",
        #         "text": "Canceled by User",
        #         "execType": "4",
        #         "execID": "21416034921",
        #         "transactTime": "2022-08-08T23:33:25.727785Z",
        #         "msgType": 8,
        #         "lastPx": 0,
        #         "lastShares": 0,
        #         "tradeId": "0",
        #         "fee": 0,
        #         "price": 30000,
        #         "marginOrder": False,
        #         "closePositionOrder": False
        #     }
        #
        datetime = self.safe_string(order, 'transactTime')
        status = self.safe_string(order, 'ordStatus')
        marketId = self.safe_string(order, 'symbol')
        market = self.safe_market(marketId, market)
        tradeId = self.safe_string(order, 'tradeId')
        trades = []
        if tradeId != '0':
            trades.append({'id': tradeId})
        return self.safe_order({
            'id': self.safe_string(order, 'orderID'),
            'clientOrderId': self.safe_string(order, 'clOrdID'),
            'datetime': datetime,
            'timestamp': self.parse8601(datetime),
            'status': self.parse_ws_order_status(status),
            'symbol': self.safe_symbol(marketId, market),
            'type': self.safe_string(order, 'ordType'),  # limit, market, stop, stopLimit, trailingStop, fillOrKill
            'timeInForce': self.safe_string(order, 'timeInForce'),
            'postOnly': self.safe_string(order, 'execInst') == 'ALO',
            'side': self.safe_string(order, 'side'),
            'price': self.safe_string(order, 'price'),
            'stopPrice': self.safe_string(order, 'stopPx'),
            'cost': None,
            'amount': self.safe_string(order, 'orderQty'),
            'filled': self.safe_string(order, 'cumQty'),
            'remaining': self.safe_string(order, 'leavesQty'),
            'trades': trades,
            'fee': {
                'rate': None,
                'cost': self.safe_number(order, 'fee'),
                'currency': self.safe_string(market, 'quote'),
            },
            'info': order,
            'lastTradeTimestamp': None,
            'average': self.safe_string(order, 'avgPx'),
        }, market)

    def parse_ws_order_status(self, status):
        statuses: dict = {
            'pending': 'open',
            'open': 'open',
            'rejected': 'rejected',
            'cancelled': 'canceled',
            'filled': 'closed',
            'partial': 'open',
            'expired': 'expired',
        }
        return self.safe_string(statuses, status, status)

    async def watch_order_book(self, symbol: str, limit: Int = None, params={}) -> OrderBook:
        """
        watches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :see: https://exchange.blockchain.com/api/#l2-order-book
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int [limit]: the maximum amount of order book entries to return
        :param dictConstructor [params]: extra parameters specific to the exchange API endpoint
        :param str [params.type]: accepts l2 or l3 for level 2 or level 3 order book
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/#/?id=order-book-structure>` indexed by market symbols
        """
        await self.load_markets()
        market = self.market(symbol)
        url = self.urls['api']['ws']
        type = self.safe_string(params, 'type', 'l2')
        params = self.omit(params, 'type')
        messageHash = 'orderbook:' + symbol + ':' + type
        subscribe: dict = {
            'action': 'subscribe',
            'channel': type,
            'symbol': market['id'],
        }
        request = self.deep_extend(subscribe, params)
        orderbook = await self.watch(url, messageHash, request, messageHash)
        return orderbook.limit()

    def handle_order_book(self, client: Client, message):
        #
        #  subscribe
        #     {
        #         "seqnum": 0,
        #         "event": "subscribed",
        #         "channel": "l2",
        #         "symbol": "BTC-USDT",
        #         "batching": False
        #     }
        #  snapshot
        #     {
        #         "seqnum": 1,
        #         "event": "snapshot",
        #         "channel": "l2",
        #         "symbol": "BTC-USDT",
        #         "bids": [
        #           {num: 1, px: 0.01, qty: 22},
        #         ],
        #         "asks": [
        #           {num: 1, px: 23840.26, qty: 0.25},
        #         ],
        #         "timestamp": "2022-08-08T22:03:19.071870Z"
        #     }
        #  update
        #     {
        #         "seqnum": 2,
        #         "event": "updated",
        #         "channel": "l2",
        #         "symbol": "BTC-USDT",
        #         "bids": [],
        #         "asks": [{num: 1, px: 23855.06, qty: 1.04786347}],
        #         "timestamp": "2022-08-08T22:03:19.014680Z"
        #     }
        #
        event = self.safe_string(message, 'event')
        if event == 'subscribed':
            return
        type = self.safe_string(message, 'channel')
        marketId = self.safe_string(message, 'symbol')
        symbol = self.safe_symbol(marketId)
        messageHash = 'orderbook:' + symbol + ':' + type
        datetime = self.safe_string(message, 'timestamp')
        timestamp = self.parse8601(datetime)
        if self.safe_value(self.orderbooks, symbol) is None:
            self.orderbooks[symbol] = self.counted_order_book()
        orderbook = self.orderbooks[symbol]
        if event == 'snapshot':
            snapshot = self.parse_order_book(message, symbol, timestamp, 'bids', 'asks', 'px', 'qty', 'num')
            orderbook.reset(snapshot)
        elif event == 'updated':
            asks = self.safe_list(message, 'asks', [])
            bids = self.safe_list(message, 'bids', [])
            self.handle_deltas(orderbook['asks'], asks)
            self.handle_deltas(orderbook['bids'], bids)
            orderbook['timestamp'] = timestamp
            orderbook['datetime'] = datetime
        else:
            raise NotSupported(self.id + ' watchOrderBook() does not support ' + event + ' yet')
        client.resolve(orderbook, messageHash)

    def handle_delta(self, bookside, delta):
        bookArray = self.parse_bid_ask(delta, 'px', 'qty', 'num')
        bookside.storeArray(bookArray)

    def handle_deltas(self, bookside, deltas):
        for i in range(0, len(deltas)):
            self.handle_delta(bookside, deltas[i])

    def handle_message(self, client: Client, message):
        channel = self.safe_string(message, 'channel')
        handlers: dict = {
            'ticker': self.handle_ticker,
            'trades': self.handle_trades,
            'prices': self.handle_ohlcv,
            'l2': self.handle_order_book,
            'l3': self.handle_order_book,
            'auth': self.handle_authentication_message,
            'balances': self.handle_balance,
            'trading': self.handle_orders,
        }
        handler = self.safe_value(handlers, channel)
        if handler is not None:
            handler(client, message)
            return
        raise NotSupported(self.id + ' received an unsupported message: ' + self.json(message))

    def handle_authentication_message(self, client: Client, message):
        #
        #     {
        #         "seqnum": 0,
        #         "event": "subscribed",
        #         "channel": "auth",
        #         "readOnly": False
        #     }
        #
        event = self.safe_string(message, 'event')
        if event != 'subscribed':
            raise AuthenticationError(self.id + ' received an authentication error: ' + self.json(message))
        future = self.safe_value(client.futures, 'authenticated')
        if future is not None:
            future.resolve(True)

    async def authenticate(self, params={}):
        url = self.urls['api']['ws']
        client = self.client(url)
        messageHash = 'authenticated'
        future = client.future(messageHash)
        isAuthenticated = self.safe_value(client.subscriptions, messageHash)
        if isAuthenticated is None:
            self.check_required_credentials()
            request: dict = {
                'action': 'subscribe',
                'channel': 'auth',
                'token': self.secret,
            }
            return self.watch(url, messageHash, self.extend(request, params), messageHash)
        return await future
