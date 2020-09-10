# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxtpro.base.exchange import Exchange
import ccxt.async_support as ccxt
from ccxtpro.base.cache import ArrayCache


class currencycom(Exchange, ccxt.currencycom):

    def describe(self):
        return self.deep_extend(super(currencycom, self).describe(), {
            'has': {
                'ws': True,
                'watchBalance': True,
                'watchTicker': True,
                'watchTickers': False,  # for now
                'watchTrades': True,
                'watchOrderBook': True,
                # 'watchStatus': True,
                # 'watchHeartbeat': True,
                'watchOHLCV': True,
            },
            'urls': {
                'api': {
                    'ws': 'wss://api-adapter.backend.currency.com/connect',
                },
            },
            'options': {
                'tradesLimit': 1000,
                'OHLCVLimit': 1000,
                # WS timeframes differ from REST timeframes
                'timeframes': {
                    '1m': 'M1',
                    '3m': 'M3',
                    '5m': 'M5',
                    '15m': 'M15',
                    '30m': 'M30',
                    '1h': 'H1',
                    '4h': 'H4',
                    '1d': 'D1',
                    '1w': 'W1',
                },
            },
            'streaming': {
                # okex does not support built-in ws protocol-level ping-pong
                # instead it requires a custom text-based ping-pong
                'ping': self.ping,
                'keepAlive': 20000,
            },
        })

    def ping(self, client):
        # custom ping-pong
        requestId = str(self.request_id())
        return {
            'destination': 'ping',
            'correlationId': requestId,
            'payload': {},
        }

    def handle_pong(self, client, message):
        client.lastPong = self.milliseconds()
        return message

    def handle_balance(self, client, message, subscription):
        #
        #     {
        #         status: 'OK',
        #         correlationId: '1',
        #         payload: {
        #             makerCommission: 0.2,
        #             takerCommission: 0.2,
        #             buyerCommission: 0.2,
        #             sellerCommission: 0.2,
        #             canTrade: True,
        #             canWithdraw: True,
        #             canDeposit: True,
        #             updateTime: 1596742699,
        #             balances: [
        #                 {
        #                     accountId: 5470306579272968,
        #                     collateralCurrency: True,
        #                     asset: 'ETH',
        #                     free: 0,
        #                     locked: 0,
        #                     default: False
        #                 },
        #                 {
        #                     accountId: 5470310874305732,
        #                     collateralCurrency: True,
        #                     asset: 'USD',
        #                     free: 47.82576735,
        #                     locked: 1.187925,
        #                     default: True
        #                 },
        #             ]
        #         }
        #     }
        #
        payload = self.safe_value(message, 'payload')
        balance = self.parse_balance_response(payload)
        self.balance = self.extend(self.balance, balance)
        messageHash = self.safe_string(subscription, 'messageHash')
        client.resolve(self.balance, messageHash)
        if messageHash in client.subscriptions:
            del client.subscriptions[messageHash]

    def handle_ticker(self, client, message, subscription):
        #
        #     {
        #         status: 'OK',
        #         correlationId: '1',
        #         payload: {
        #             tickers: [
        #                 {
        #                     symbol: 'BTC/USD_LEVERAGE',
        #                     priceChange: '484.05',
        #                     priceChangePercent: '4.14',
        #                     weightedAvgPrice: '11682.83',
        #                     prevClosePrice: '11197.70',
        #                     lastPrice: '11682.80',
        #                     lastQty: '0.25',
        #                     bidPrice: '11682.80',
        #                     askPrice: '11682.85',
        #                     openPrice: '11197.70',
        #                     highPrice: '11734.05',
        #                     lowPrice: '11080.95',
        #                     volume: '299.133',
        #                     quoteVolume: '3488040.3465',
        #                     openTime: 1596585600000,
        #                     closeTime: 1596654452674
        #                 }
        #             ]
        #         }
        #     }
        #
        destination = '/api/v1/ticker/24hr'
        payload = self.safe_value(message, 'payload')
        tickers = self.safe_value(payload, 'tickers', [])
        for i in range(0, len(tickers)):
            ticker = self.parse_ticker(tickers[i])
            symbol = ticker['symbol']
            self.tickers[symbol] = ticker
            messageHash = destination + ':' + symbol
            client.resolve(ticker, messageHash)
            if messageHash in client.subscriptions:
                del client.subscriptions[messageHash]

    def handle_trade(self, trade, market=None):
        #
        #     {
        #         price: 11668.55,
        #         size: 0.001,
        #         id: 1600300736,
        #         ts: 1596653426822,
        #         symbol: 'BTC/USD_LEVERAGE',
        #         orderId: '00a02503-0079-54c4-0000-00004020163c',
        #         clientOrderId: '00a02503-0079-54c4-0000-482f0000754f',
        #         buyer: False
        #     }
        #
        symbol = None
        if market is None:
            marketId = self.safe_string(trade, 'symbol')
            market = self.safe_value(self.markets_by_id, marketId)
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'ts')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'size')
        id = self.safe_string_2(trade, 'id')
        orderId = self.safe_string(trade, 'orderId')
        buyer = self.safe_value(trade, 'buyer')
        side = 'buy' if buyer else 'sell'
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'id': id,
            'order': orderId,
            'type': None,
            'takerOrMaker': None,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': price * amount,
            'fee': None,
        }

    def handle_trades(self, client, message, subscription):
        #
        #     {
        #         status: 'OK',
        #         destination: 'internal.trade',
        #         payload: {
        #             price: 11668.55,
        #             size: 0.001,
        #             id: 1600300736,
        #             ts: 1596653426822,
        #             symbol: 'BTC/USD_LEVERAGE',
        #             orderId: '00a02503-0079-54c4-0000-00004020163c',
        #             clientOrderId: '00a02503-0079-54c4-0000-482f0000754f',
        #             buyer: False
        #         }
        #     }
        #
        payload = self.safe_value(message, 'payload')
        parsed = self.handle_trade(payload)
        symbol = parsed['symbol']
        # destination = self.safe_string(message, 'destination')
        destination = 'trades.subscribe'
        messageHash = destination + ':' + symbol
        stored = self.safe_value(self.trades, symbol)
        if stored is None:
            limit = self.safe_integer(self.options, 'tradesLimit', 1000)
            stored = ArrayCache(limit)
            self.trades[symbol] = stored
        stored.append(parsed)
        client.resolve(stored, messageHash)

    def find_timeframe(self, timeframe):
        timeframes = self.safe_value(self.options, 'timeframes')
        keys = list(timeframes.keys())
        for i in range(0, len(keys)):
            key = keys[i]
            if timeframes[key] == timeframe:
                return key
        return None

    def handle_ohlcv(self, client, message):
        #
        #     {
        #         status: 'OK',
        #         destination: 'ohlc.event',
        #         payload: {
        #             interval: 'M1',
        #             symbol: 'BTC/USD_LEVERAGE',
        #             t: 1596650940000,
        #             h: 11670.05,
        #             l: 11658.1,
        #             o: 11668.55,
        #             c: 11666.05
        #         }
        #     }
        #
        # destination = self.safe_string(message, 'destination')
        destination = 'OHLCMarketData.subscribe'
        payload = self.safe_value(message, 'payload', {})
        interval = self.safe_string(payload, 'interval')
        timeframe = self.find_timeframe(interval)
        marketId = self.safe_string(payload, 'symbol')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
            symbol = market['symbol']
            messageHash = destination + ':' + timeframe + ':' + symbol
            result = [
                self.safe_integer(payload, 't'),
                self.safe_float(payload, 'o'),
                self.safe_float(payload, 'h'),
                self.safe_float(payload, 'l'),
                self.safe_float(payload, 'c'),
                None,  # no volume v in OHLCV
            ]
            self.ohlcvs[symbol] = self.safe_value(self.ohlcvs, symbol, {})
            stored = self.safe_value(self.ohlcvs[symbol], timeframe)
            if stored is None:
                limit = self.safe_integer(self.options, 'OHLCVLimit', 1000)
                stored = ArrayCache(limit)
                self.ohlcvs[symbol][timeframe] = stored
            length = len(stored)
            if length and result[0] == stored[length - 1][0]:
                stored[length - 1] = result
            else:
                stored.append(result)
            client.resolve(stored, messageHash)

    def request_id(self):
        reqid = self.sum(self.safe_integer(self.options, 'correlationId', 0), 1)
        self.options['correlationId'] = reqid
        return reqid

    async def watch_public(self, destination, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        messageHash = destination + ':' + symbol
        url = self.urls['api']['ws']
        requestId = str(self.request_id())
        request = self.deep_extend({
            'destination': destination,
            'correlationId': requestId,
            'payload': {
                'symbols': [market['id']],
            },
        }, params)
        subscription = self.extend(request, {
            'messageHash': messageHash,
            'symbol': symbol,
        })
        return await self.watch(url, messageHash, request, messageHash, subscription)

    async def watch_private(self, destination, params={}):
        await self.load_markets()
        messageHash = '/api/v1/account'
        url = self.urls['api']['ws']
        requestId = str(self.request_id())
        payload = {
            'timestamp': self.milliseconds(),
            'apiKey': self.apiKey,
        }
        auth = self.urlencode(self.keysort(payload))
        request = self.deep_extend({
            'destination': destination,
            'correlationId': requestId,
            'payload': payload,
        }, params)
        request['payload']['signature'] = self.hmac(self.encode(auth), self.encode(self.secret))
        subscription = self.extend(request, {
            'messageHash': messageHash,
        })
        return await self.watch(url, messageHash, request, messageHash, subscription)

    async def watch_balance(self, params={}):
        await self.load_markets()
        return await self.watch_private('/api/v1/account', params)

    async def watch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        destination = '/api/v1/ticker/24hr'
        messageHash = destination + ':' + symbol
        url = self.urls['api']['ws']
        requestId = str(self.request_id())
        request = self.deep_extend({
            'destination': destination,
            'correlationId': requestId,
            'payload': {
                'symbol': market['id'],
            },
        }, params)
        subscription = self.extend(request, {
            'messageHash': messageHash,
            'symbol': symbol,
        })
        return await self.watch(url, messageHash, request, messageHash, subscription)

    async def watch_trades(self, symbol, since=None, limit=None, params={}):
        future = self.watch_public('trades.subscribe', symbol, params)
        return await self.after(future, self.filter_by_since_limit, since, limit, 'timestamp', True)

    async def watch_order_book(self, symbol, limit=None, params={}):
        future = self.watch_public('depthMarketData.subscribe', symbol, params)
        return await self.after(future, self.limit_order_book, symbol, limit, params)

    async def watch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        destination = 'OHLCMarketData.subscribe'
        messageHash = destination + ':' + timeframe
        timeframes = self.safe_value(self.options, 'timeframes')
        request = {
            'destination': destination,
            'payload': {
                'intervals': [
                    timeframes[timeframe],
                ],
            },
        }
        future = self.watch_public(messageHash, symbol, self.extend(request, params))
        return await self.after(future, self.filter_by_since_limit, since, limit, 0, True)

    def handle_deltas(self, bookside, deltas):
        prices = list(deltas.keys())
        for i in range(0, len(prices)):
            price = prices[i]
            amount = deltas[price]
            bookside.store(float(price), float(amount))

    def handle_order_book(self, client, message):
        #
        #     {
        #         status: 'OK',
        #         destination: 'marketdepth.event',
        #         payload: {
        #             data: '{"ts":1596235401337,"bid":{"11366.85":0.2500,"11366.1":5.0000,"11365.6":0.5000,"11363.0":2.0000},"ofr":{"11366.9":0.2500,"11367.65":5.0000,"11368.15":0.5000}}',
        #             symbol: 'BTC/USD_LEVERAGE'
        #         }
        #     }
        #
        payload = self.safe_value(message, 'payload', {})
        data = self.safe_value(payload, 'data', {})
        marketId = self.safe_string(payload, 'symbol')
        market = None
        symbol = None
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
                symbol = market['id']
            else:
                symbol = marketId
        # destination = self.safe_string(message, 'destination')
        destination = 'depthMarketData.subscribe'
        messageHash = destination + ':' + symbol
        timestamp = self.safe_integer(data, 'ts')
        orderbook = self.safe_value(self.orderbooks, symbol)
        if orderbook is None:
            orderbook = self.order_book()
        orderbook.reset({
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
        })
        bids = self.safe_value(data, 'bid', {})
        asks = self.safe_value(data, 'ofr', {})
        self.handle_deltas(orderbook['bids'], bids)
        self.handle_deltas(orderbook['asks'], asks)
        self.orderbooks[symbol] = orderbook
        client.resolve(orderbook, messageHash)

    def sign_message(self, client, messageHash, message, params={}):
        # todo: signMessage not implemented yet
        return message

    def handle_message(self, client, message):
        #
        #     {
        #         status: 'OK',
        #         correlationId: '1',
        #         payload: {
        #             tickers: [
        #                 {
        #                     symbol: '1COV',
        #                     priceChange: '-0.29',
        #                     priceChangePercent: '-0.80',
        #                     prevClosePrice: '36.33',
        #                     lastPrice: '36.04',
        #                     openPrice: '36.33',
        #                     highPrice: '36.46',
        #                     lowPrice: '35.88',
        #                     openTime: 1595548800000,
        #                     closeTime: 1595795305401
        #                 }
        #             ]
        #         }
        #     }
        #
        #     {
        #         status: 'OK',
        #         destination: 'marketdepth.event',
        #         payload: {
        #             data: '{"ts":1596235401337,"bid":{"11366.85":0.2500,"11366.1":5.0000,"11365.6":0.5000,"11363.0":2.0000},"ofr":{"11366.9":0.2500,"11367.65":5.0000,"11368.15":0.5000}}',
        #             symbol: 'BTC/USD_LEVERAGE'
        #         }
        #     }
        #
        #     {
        #         status: 'OK',
        #         destination: 'internal.trade',
        #         payload: {
        #             price: 11634.75,
        #             size: 0.001,
        #             id: 1605492357,
        #             ts: 1596263802399,
        #             instrumentId: 45076691096786110,
        #             orderId: '00a02503-0079-54c4-0000-0000401fff51',
        #             clientOrderId: '00a02503-0079-54c4-0000-482b00002f17',
        #             buyer: False
        #         }
        #     }
        #
        requestId = self.safe_string(message, 'correlationId')
        if requestId is not None:
            subscriptionsById = self.index_by(client.subscriptions, 'correlationId')
            status = self.safe_string(message, 'status')
            subscription = self.safe_value(subscriptionsById, requestId)
            if subscription is not None:
                if status == 'OK':
                    destination = self.safe_string(subscription, 'destination')
                    if destination is not None:
                        methods = {
                            '/api/v1/ticker/24hr': self.handle_ticker,
                            '/api/v1/account': self.handle_balance,
                        }
                        method = self.safe_value(methods, destination)
                        if method is None:
                            return message
                        else:
                            return method(client, message, subscription)
        destination = self.safe_string(message, 'destination')
        if destination is not None:
            methods = {
                'marketdepth.event': self.handle_order_book,
                'internal.trade': self.handle_trades,
                'ohlc.event': self.handle_ohlcv,
                'ping': self.handle_pong,
            }
            method = self.safe_value(methods, destination)
            if method is None:
                return message
            else:
                return method(client, message)
