<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use ccxt\async\abstract\alpaca as Exchange;
use ccxt\ExchangeError;
use ccxt\NotSupported;
use React\Async;

class alpaca extends Exchange {

    public function describe() {
        return $this->deep_extend(parent::describe(), array(
            'id' => 'alpaca',
            'name' => 'Alpaca',
            'countries' => array( 'US' ),
            'rateLimit' => 333, // 3 req per second
            'hostname' => 'alpaca.markets',
            'pro' => true,
            'urls' => array(
                'logo' => 'https://user-images.githubusercontent.com/1294454/187234005-b864db3d-f1e3-447a-aaf9-a9fc7b955d07.jpg',
                'www' => 'https://alpaca.markets',
                'api' => array(
                    'public' => 'https://api.{hostname}/{version}',
                    'private' => 'https://api.{hostname}/{version}',
                    'cryptoPublic' => 'https://data.{hostname}/{version}',
                    'markets' => 'https://api.{hostname}/{version}',
                ),
                'test' => array(
                    'public' => 'https://paper-api.{hostname}/{version}',
                    'private' => 'https://paper-api.{hostname}/{version}',
                    'cryptoPublic' => 'https://data.{hostname}/{version}',
                    'markets' => 'https://api.{hostname}/{version}',
                ),
                'doc' => 'https://alpaca.markets/docs/',
                'fees' => 'https://alpaca.markets/support/what-are-the-fees-associated-with-crypto-trading/',
            ),
            'has' => array(
                'CORS' => false,
                'spot' => true,
                'margin' => false,
                'swap' => false,
                'future' => false,
                'option' => false,
                'cancelAllOrders' => true,
                'cancelOrder' => true,
                'createOrder' => true,
                'fetchBalance' => true,
                'fetchBidsAsks' => false,
                'fetchClosedOrders' => false,
                'fetchCurrencies' => false,
                'fetchDepositAddress' => false,
                'fetchDepositAddressesByNetwork' => false,
                'fetchDeposits' => false,
                'fetchDepositsWithdrawals' => false,
                'fetchFundingHistory' => false,
                'fetchFundingRate' => false,
                'fetchFundingRates' => false,
                'fetchL1OrderBook' => true,
                'fetchL2OrderBook' => false,
                'fetchMarkets' => true,
                'fetchMyTrades' => false,
                'fetchOHLCV' => true,
                'fetchOpenOrder' => false,
                'fetchOpenOrders' => true,
                'fetchOrder' => true,
                'fetchOrderBook' => true,
                'fetchOrders' => false,
                'fetchPositions' => false,
                'fetchStatus' => false,
                'fetchTicker' => false,
                'fetchTickers' => false,
                'fetchTime' => false,
                'fetchTrades' => true,
                'fetchTradingFee' => false,
                'fetchTradingFees' => false,
                'fetchTransactionFees' => false,
                'fetchTransactions' => false,
                'fetchTransfers' => false,
                'fetchWithdrawals' => false,
                'setLeverage' => false,
                'setMarginMode' => false,
                'transfer' => false,
                'withdraw' => false,
            ),
            'api' => array(
                'markets' => array(
                    'get' => array(
                        'assets/public/beta',
                    ),
                ),
                'private' => array(
                    'get' => array(
                        'account',
                        'orders',
                        'orders/{order_id}',
                        'positions',
                        'positions/{symbol}',
                        'account/activities/{activity_type}',
                    ),
                    'post' => array(
                        'orders',
                    ),
                    'delete' => array(
                        'orders',
                        'orders/{order_id}',
                    ),
                ),
                'cryptoPublic' => array(
                    'get' => array(
                        'crypto/latest/orderbooks',
                        'crypto/trades',
                        'crypto/quotes',
                        'crypto/latest/quotes',
                        'crypto/bars',
                        'crypto/snapshots',
                    ),
                ),
            ),
            'timeframes' => array(
                '1m' => '1min',
                '3m' => '3min',
                '5m' => '5min',
                '15m' => '15min',
                '30m' => '30min',
                '1h' => '1H',
                '2h' => '2H',
                '4h' => '4H',
                '6h' => '6H',
                '8h' => '8H',
                '12h' => '12H',
                '1d' => '1D',
                '3d' => '3D',
                '1w' => '1W',
                '1M' => '1M',
            ),
            'precisionMode' => TICK_SIZE,
            'requiredCredentials' => array(
                'apiKey' => true,
                'secret' => true,
            ),
            'fees' => array(
                'trading' => array(
                    'tierBased' => true,
                    'percentage' => true,
                    'maker' => $this->parse_number('0.003'),
                    'taker' => $this->parse_number('0.003'),
                    'tiers' => array(
                        'taker' => array(
                            array( $this->parse_number('0'), $this->parse_number('0.003') ),
                            array( $this->parse_number('500000'), $this->parse_number('0.0028') ),
                            array( $this->parse_number('1000000'), $this->parse_number('0.0025') ),
                            array( $this->parse_number('5000000'), $this->parse_number('0.002') ),
                            array( $this->parse_number('10000000'), $this->parse_number('0.0018') ),
                            array( $this->parse_number('25000000'), $this->parse_number('0.0015') ),
                            array( $this->parse_number('50000000'), $this->parse_number('0.00125') ),
                            array( $this->parse_number('100000000'), $this->parse_number('0.001') ),
                        ),
                        'maker' => array(
                            array( $this->parse_number('0'), $this->parse_number('0.003') ),
                            array( $this->parse_number('500000'), $this->parse_number('0.0028') ),
                            array( $this->parse_number('1000000'), $this->parse_number('0.0025') ),
                            array( $this->parse_number('5000000'), $this->parse_number('0.002') ),
                            array( $this->parse_number('10000000'), $this->parse_number('0.0018') ),
                            array( $this->parse_number('25000000'), $this->parse_number('0.0015') ),
                            array( $this->parse_number('50000000'), $this->parse_number('0.00125') ),
                            array( $this->parse_number('100000000'), $this->parse_number('0.001') ),
                        ),
                    ),
                ),
            ),
            'headers' => array(
                'APCA-PARTNER-ID' => 'ccxt',
            ),
            'options' => array(
                'fetchTradesMethod' => 'cryptoPublicGetCryptoTrades', // or cryptoPublicGetCryptoLatestTrades
                'fetchOHLCVMethod' => 'cryptoPublicGetCryptoBars', // or cryptoPublicGetCryptoLatestBars
                'versions' => array(
                    'public' => 'v2',
                    'private' => 'v2',
                    'cryptoPublic' => 'v1beta2', // crypto beta
                    'markets' => 'v2', // crypto beta
                ),
                'defaultExchange' => 'CBSE',
                'exchanges' => array(
                    'CBSE', // Coinbase
                    'FTX', // FTXUS
                    'GNSS', // Genesis
                    'ERSX', // ErisX
                ),
                'defaultTimeInForce' => 'gtc', // fok, gtc, ioc
                'clientOrderId' => 'ccxt_{id}',
            ),
            'exceptions' => array(
                'exact' => array(
                    'forbidden.' => '\\ccxt\\PermissionDenied', // array("message" => "forbidden.")
                    '40410000' => '\\ccxt\\InvalidOrder', // array( "code" => 40410000, "message" => "order is not found.")
                    '40010001' => '\\ccxt\\BadRequest', // array("code":40010001,"message":"invalid order type for crypto order")
                    '40110000' => '\\ccxt\\PermissionDenied', // array( "code" => 40110000, "message" => "request is not authorized")
                    '40310000' => '\\ccxt\\InsufficientFunds', // array("available":"0","balance":"0","code":40310000,"message":"insufficient balance for USDT (requested => 221.63, available => 0)","symbol":"USDT")
                ),
                'broad' => array(
                    'Invalid format for parameter' => '\\ccxt\\BadRequest', // array("message":"Invalid format for parameter start => error parsing '0' or 2006-01-02 time => parsing time \"0\" as \"2006-01-02\" => cannot parse \"0\" as \"2006\"")
                    'Invalid symbol' => '\\ccxt\\BadSymbol', // array("message":"Invalid symbol(s) => BTC/USDdsda does not match ^[A-Z]+/[A-Z]+$")
                ),
            ),
        ));
    }

    public function fetch_markets($params = array ()) {
        return Async\async(function () use ($params) {
            /**
             * retrieves data on all $markets for alpaca
             * @param {array} $params extra parameters specific to the exchange api endpoint
             * @return {[array]} an array of objects representing market data
             */
            $request = array(
                'asset_class' => 'crypto',
                'tradeable' => true,
            );
            $assets = Async\await($this->marketsGetAssetsPublicBeta (array_merge($request, $params)));
            //
            //    array(
            //        {
            //           "id":"a3ba8ac0-166d-460b-b17a-1f035622dd47",
            //           "class":"crypto",
            //           "exchange":"FTXU",
            //           "symbol":"DOGEUSD",
            //           "name":"Dogecoin",
            //           "status":"active",
            //           "tradable":true,
            //           "marginable":false,
            //           "shortable":false,
            //           "easy_to_borrow":false,
            //           "fractionable":true,
            //           "min_order_size":"1",
            //           "min_trade_increment":"1",
            //           "price_increment":"0.0000005"
            //        }
            //    )
            //
            $markets = array();
            for ($i = 0; $i < count($assets); $i++) {
                $asset = $assets[$i];
                $marketId = $this->safe_string($asset, 'symbol');
                $parts = explode('/', $marketId);
                $baseId = $this->safe_string($parts, 0);
                $quoteId = $this->safe_string($parts, 1);
                $base = $this->safe_currency_code($baseId);
                $quote = $this->safe_currency_code($quoteId);
                $symbol = $base . '/' . $quote;
                $status = $this->safe_string($asset, 'status');
                $active = ($status === 'active');
                $minAmount = $this->safe_number($asset, 'min_order_size');
                $amount = $this->safe_number($asset, 'min_trade_increment');
                $price = $this->safe_number($asset, 'price_increment');
                $markets[] = array(
                    'id' => $marketId,
                    'symbol' => $symbol,
                    'base' => $base,
                    'quote' => $quote,
                    'settle' => null,
                    'baseId' => $baseId,
                    'quoteId' => $quoteId,
                    'settleId' => null,
                    'type' => 'spot',
                    'spot' => true,
                    'margin' => null,
                    'swap' => false,
                    'future' => false,
                    'option' => false,
                    'active' => $active,
                    'contract' => false,
                    'linear' => null,
                    'inverse' => null,
                    'contractSize' => null,
                    'expiry' => null,
                    'expiryDatetime' => null,
                    'strike' => null,
                    'optionType' => null,
                    'precision' => array(
                        'amount' => $amount,
                        'price' => $price,
                    ),
                    'limits' => array(
                        'leverage' => array(
                            'min' => null,
                            'max' => null,
                        ),
                        'amount' => array(
                            'min' => $minAmount,
                            'max' => null,
                        ),
                        'price' => array(
                            'min' => null,
                            'max' => null,
                        ),
                        'cost' => array(
                            'min' => null,
                            'max' => null,
                        ),
                    ),
                    'info' => $asset,
                );
            }
            return $markets;
        }) ();
    }

    public function fetch_trades(string $symbol, ?int $since = null, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $since, $limit, $params) {
            /**
             * get the list of most recent $trades for a particular $symbol
             * @param {string} $symbol unified $symbol of the $market to fetch $trades for
             * @param {int|null} $since timestamp in ms of the earliest trade to fetch
             * @param {int|null} $limit the maximum amount of $trades to fetch
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @return {[array]} a list of ~@link https://docs.ccxt.com/en/latest/manual.html?#public-$trades trade structures~
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $id = $market['id'];
            $request = array(
                'symbols' => $id,
            );
            if ($since !== null) {
                $request['start'] = $this->iso8601($since);
            }
            if ($limit !== null) {
                $request['limit'] = $limit;
            }
            $method = $this->safe_string($this->options, 'fetchTradesMethod', 'cryptoPublicGetCryptoTrades');
            $response = Async\await($this->$method (array_merge($request, $params)));
            //
            // {
            //     "next_page_token":null,
            //     "trades":{
            //        "BTC/USD":array(
            //           {
            //              "i":36440704,
            //              "p":22625,
            //              "s":0.0001,
            //              "t":"2022-07-21T11:47:31.073391Z",
            //              "tks":"B"
            //           }
            //        )
            //     }
            // }
            //
            $trades = $this->safe_value($response, 'trades', array());
            $symbolTrades = $this->safe_value($trades, $market['id'], array());
            return $this->parse_trades($symbolTrades, $market, $since, $limit);
        }) ();
    }

    public function fetch_order_book(string $symbol, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $limit, $params) {
            /**
             * fetches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
             * @param {string} $symbol unified $symbol of the $market to fetch the order book for
             * @param {int|null} $limit the maximum amount of order book entries to return
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @return {array} A dictionary of ~@link https://docs.ccxt.com/#/?$id=order-book-structure order book structures~ indexed by $market symbols
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $id = $market['id'];
            $request = array(
                'symbols' => $id,
            );
            $response = Async\await($this->cryptoPublicGetCryptoLatestOrderbooks (array_merge($request, $params)));
            //
            //   {
            //       "orderbooks":{
            //          "BTC/USD":{
            //             "a":array(
            //                array(
            //                   "p":22208,
            //                   "s":0.0051
            //                ),
            //                array(
            //                   "p":22209,
            //                   "s":0.1123
            //                ),
            //                {
            //                   "p":22210,
            //                   "s":0.2465
            //                }
            //             ),
            //             "b":array(
            //                array(
            //                   "p":22203,
            //                   "s":0.395
            //                ),
            //                array(
            //                   "p":22202,
            //                   "s":0.2465
            //                ),
            //                {
            //                   "p":22201,
            //                   "s":0.6455
            //                }
            //             ),
            //             "t":"2022-07-19T13:41:55.13210112Z"
            //          }
            //       }
            //   }
            //
            $orderbooks = $this->safe_value($response, 'orderbooks', array());
            $rawOrderbook = $this->safe_value($orderbooks, $id, array());
            $timestamp = $this->parse8601($this->safe_string($rawOrderbook, 't'));
            return $this->parse_order_book($rawOrderbook, $market['symbol'], $timestamp, 'b', 'a', 'p', 's');
        }) ();
    }

    public function fetch_ohlcv(string $symbol, $timeframe = '1m', ?int $since = null, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $timeframe, $since, $limit, $params) {
            /**
             * fetches historical candlestick data containing the open, high, low, and close price, and the volume of a $market
             * @param {string} $symbol unified $symbol of the $market to fetch OHLCV data for
             * @param {string} $timeframe the length of time each candle represents
             * @param {int|null} $since timestamp in ms of the earliest candle to fetch
             * @param {int|null} $limit the maximum amount of candles to fetch
             * @param {array} $params extra parameters specific to the alpha api endpoint
             * @return {[[int]]} A list of candles ordered, open, high, low, close, volume
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $request = array(
                'symbols' => $market['id'],
                'timeframe' => $this->safe_string($this->timeframes, $timeframe, $timeframe),
            );
            if ($limit !== null) {
                $request['limit'] = $limit;
            }
            if ($since !== null) {
                $request['start'] = $this->yyyymmdd($since);
            }
            $method = $this->safe_string($this->options, 'fetchOHLCVMethod', 'cryptoPublicGetCryptoBars');
            $response = Async\await($this->$method (array_merge($request, $params)));
            //
            //    {
            //        "bars":{
            //           "BTC/USD":array(
            //              array(
            //                 "c":22887,
            //                 "h":22888,
            //                 "l":22873,
            //                 "n":11,
            //                 "o":22883,
            //                 "t":"2022-07-21T05:00:00Z",
            //                 "v":1.1138,
            //                 "vw":22883.0155324116
            //              ),
            //              array(
            //                 "c":22895,
            //                 "h":22895,
            //                 "l":22884,
            //                 "n":6,
            //                 "o":22884,
            //                 "t":"2022-07-21T05:01:00Z",
            //                 "v":0.001,
            //                 "vw":22889.5
            //              }
            //           )
            //        ),
            //        "next_page_token":"QlRDL1VTRHxNfDIwMjItMDctMjFUMDU6MDE6MDAuMDAwMDAwMDAwWg=="
            //     }
            //
            $bars = $this->safe_value($response, 'bars', array());
            $ohlcvs = $this->safe_value($bars, $market['id'], array());
            return $this->parse_ohlcvs($ohlcvs, $market, $timeframe, $since, $limit);
        }) ();
    }

    public function parse_ohlcv($ohlcv, $market = null) {
        //
        //     {
        //        "c":22895,
        //        "h":22895,
        //        "l":22884,
        //        "n":6,
        //        "o":22884,
        //        "t":"2022-07-21T05:01:00Z",
        //        "v":0.001,
        //        "vw":22889.5
        //     }
        //
        $datetime = $this->safe_string($ohlcv, 't');
        $timestamp = $this->parse8601($datetime);
        return array(
            $timestamp, // $timestamp
            $this->safe_number($ohlcv, 'o'), // open
            $this->safe_number($ohlcv, 'h'), // high
            $this->safe_number($ohlcv, 'l'), // low
            $this->safe_number($ohlcv, 'c'), // close
            $this->safe_number($ohlcv, 'v'), // volume
        );
    }

    public function create_order(string $symbol, string $type, string $side, $amount, $price = null, $params = array ()) {
        return Async\async(function () use ($symbol, $type, $side, $amount, $price, $params) {
            /**
             * create a trade $order
             * @param {string} $symbol unified $symbol of the $market to create an $order in
             * @param {string} $type 'market', 'limit' or 'stop_limit'
             * @param {string} $side 'buy' or 'sell'
             * @param {float} $amount how much of currency you want to trade in units of base currency
             * @param {float} $price the $price at which the $order is to be fullfilled, in units of the quote currency, ignored in $market orders
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @param {float} $params->triggerPrice The $price at which a trigger $order is triggered at
             * @return {array} an ~@link https://docs.ccxt.com/#/?$id=$order-structure $order structure~
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $id = $market['id'];
            $request = array(
                'symbol' => $id,
                'qty' => $this->amount_to_precision($symbol, $amount),
                'side' => $side,
                'type' => $type, // $market, limit, stop_limit
            );
            $triggerPrice = $this->safe_string_n($params, array( 'triggerPrice', 'stop_price' ));
            if ($triggerPrice !== null) {
                $newType = null;
                if (mb_strpos($type, 'limit') !== false) {
                    $newType = 'stop_limit';
                } else {
                    throw new NotSupported($this->id . ' createOrder() does not support stop orders for ' . $type . ' orders, only stop_limit orders are supported');
                }
                $request['stop_price'] = $this->price_to_precision($symbol, $triggerPrice);
                $request['type'] = $newType;
            }
            if (mb_strpos($type, 'limit') !== false) {
                $request['limit_price'] = $this->price_to_precision($symbol, $price);
            }
            $defaultTIF = $this->safe_string($this->options, 'defaultTimeInForce');
            $request['time_in_force'] = $this->safe_string($params, 'timeInForce', $defaultTIF);
            $params = $this->omit($params, array( 'timeInForce', 'triggerPrice' ));
            $clientOrderIdprefix = $this->safe_string($this->options, 'clientOrderId');
            $uuid = $this->uuid();
            $parts = explode('-', $uuid);
            $random_id = implode('', $parts);
            $defaultClientId = $this->implode_params($clientOrderIdprefix, array( 'id' => $random_id ));
            $clientOrderId = $this->safe_string($params, 'clientOrderId', $defaultClientId);
            $request['client_order_id'] = $clientOrderId;
            $params = $this->omit($params, array( 'clientOrderId' ));
            $order = Async\await($this->privatePostOrders (array_merge($request, $params)));
            //
            //   {
            //      "id" => "61e69015-8549-4bfd-b9c3-01e75843f47d",
            //      "client_order_id" => "eb9e2aaa-f71a-4f51-b5b4-52a6c565dad4",
            //      "created_at" => "2021-03-16T18:38:01.942282Z",
            //      "updated_at" => "2021-03-16T18:38:01.942282Z",
            //      "submitted_at" => "2021-03-16T18:38:01.937734Z",
            //      "filled_at" => null,
            //      "expired_at" => null,
            //      "canceled_at" => null,
            //      "failed_at" => null,
            //      "replaced_at" => null,
            //      "replaced_by" => null,
            //      "replaces" => null,
            //      "asset_id" => "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
            //      "symbol" => "AAPL",
            //      "asset_class" => "us_equity",
            //      "notional" => "500",
            //      "qty" => null,
            //      "filled_qty" => "0",
            //      "filled_avg_price" => null,
            //      "order_class" => "",
            //      "order_type" => "market",
            //      "type" => "market",
            //      "side" => "buy",
            //      "time_in_force" => "day",
            //      "limit_price" => null,
            //      "stop_price" => null,
            //      "status" => "accepted",
            //      "extended_hours" => false,
            //      "legs" => null,
            //      "trail_percent" => null,
            //      "trail_price" => null,
            //      "hwm" => null
            //   }
            //
            return $this->parse_order($order, $market);
        }) ();
    }

    public function cancel_order(string $id, ?string $symbol = null, $params = array ()) {
        return Async\async(function () use ($id, $symbol, $params) {
            /**
             * cancels an open order
             * @param {string} $id order $id
             * @param {string|null} $symbol unified $symbol of the market the order was made in
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @return {array} An ~@link https://docs.ccxt.com/#/?$id=order-structure order structure~
             */
            $request = array(
                'order_id' => $id,
            );
            $response = Async\await($this->privateDeleteOrdersOrderId (array_merge($request, $params)));
            //
            //   {
            //       "code" => 40410000,
            //       "message" => "order is not found."
            //   }
            //
            return $this->safe_value($response, 'message', array());
        }) ();
    }

    public function fetch_order(string $id, ?string $symbol = null, $params = array ()) {
        return Async\async(function () use ($id, $symbol, $params) {
            /**
             * fetches information on an $order made by the user
             * @param {string|null} $symbol unified $symbol of the $market the $order was made in
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @return {array} An ~@link https://docs.ccxt.com/#/?$id=$order-structure $order structure~
             */
            Async\await($this->load_markets());
            $request = array(
                'order_id' => $id,
            );
            $order = Async\await($this->privateGetOrdersOrderId (array_merge($request, $params)));
            $marketId = $this->safe_string($order, 'symbol');
            $market = $this->safe_market($marketId);
            return $this->parse_order($order, $market);
        }) ();
    }

    public function fetch_open_orders(?string $symbol = null, ?int $since = null, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $since, $limit, $params) {
            /**
             * fetch all unfilled currently open $orders
             * @param {string|null} $symbol unified $market $symbol
             * @param {int|null} $since the earliest time in ms to fetch open $orders for
             * @param {int|null} $limit the maximum number of  open $orders structures to retrieve
             * @param {array} $params extra parameters specific to the alpaca api endpoint
             * @return {[array]} a list of ~@link https://docs.ccxt.com/#/?id=order-structure order structures~
             */
            Async\await($this->load_markets());
            $market = null;
            if ($symbol !== null) {
                $market = $this->market($symbol);
            }
            $orders = Async\await($this->privateGetOrders ($params));
            return $this->parse_orders($orders, $market, $since, $limit);
        }) ();
    }

    public function parse_order($order, $market = null) {
        //
        //    {
        //        "id":"6ecfcc34-4bed-4b53-83ba-c564aa832a81",
        //        "client_order_id":"ccxt_1c6ceab0b5e84727b2f1c0394ba17560",
        //        "created_at":"2022-06-14T13:59:30.224037068Z",
        //        "updated_at":"2022-06-14T13:59:30.224037068Z",
        //        "submitted_at":"2022-06-14T13:59:30.221856828Z",
        //        "filled_at":null,
        //        "expired_at":null,
        //        "canceled_at":null,
        //        "failed_at":null,
        //        "replaced_at":null,
        //        "replaced_by":null,
        //        "replaces":null,
        //        "asset_id":"64bbff51-59d6-4b3c-9351-13ad85e3c752",
        //        "symbol":"BTCUSD",
        //        "asset_class":"crypto",
        //        "notional":null,
        //        "qty":"0.01",
        //        "filled_qty":"0",
        //        "filled_avg_price":null,
        //        "order_class":"",
        //        "order_type":"limit",
        //        "type":"limit",
        //        "side":"buy",
        //        "time_in_force":"day",
        //        "limit_price":"14000",
        //        "stop_price":null,
        //        "status":"accepted",
        //        "extended_hours":false,
        //        "legs":null,
        //        "trail_percent":null,
        //        "trail_price":null,
        //        "hwm":null,
        //        "commission":"0.42",
        //        "source":null
        //    }
        //
        $marketId = $this->safe_string($order, 'symbol');
        $market = $this->safe_market($marketId, $market);
        $symbol = $market['symbol'];
        $alpacaStatus = $this->safe_string($order, 'status');
        $status = $this->parse_order_status($alpacaStatus);
        $feeValue = $this->safe_string($order, 'commission');
        $fee = null;
        if ($feeValue !== null) {
            $fee = array(
                'cost' => $feeValue,
                'currency' => 'USD',
            );
        }
        $orderType = $this->safe_string($order, 'order_type');
        if (mb_strpos($orderType, 'limit') !== false) {
            // might be limit or stop-limit
            $orderType = 'limit';
        }
        $datetime = $this->safe_string($order, 'submitted_at');
        $timestamp = $this->parse8601($datetime);
        return $this->safe_order(array(
            'id' => $this->safe_string($order, 'id'),
            'clientOrderId' => $this->safe_string($order, 'client_order_id'),
            'timestamp' => $timestamp,
            'datetime' => $datetime,
            'lastTradeTimeStamp' => null,
            'status' => $status,
            'symbol' => $symbol,
            'type' => $orderType,
            'timeInForce' => $this->parse_time_in_force($this->safe_string($order, 'time_in_force')),
            'postOnly' => null,
            'side' => $this->safe_string($order, 'side'),
            'price' => $this->safe_number($order, 'limit_price'),
            'stopPrice' => $this->safe_number($order, 'stop_price'),
            'triggerPrice' => $this->safe_number($order, 'stop_price'),
            'cost' => null,
            'average' => $this->safe_number($order, 'filled_avg_price'),
            'amount' => $this->safe_number($order, 'qty'),
            'filled' => $this->safe_number($order, 'filled_qty'),
            'remaining' => null,
            'trades' => null,
            'fee' => $fee,
            'info' => $order,
        ), $market);
    }

    public function parse_order_status($status) {
        $statuses = array(
            'pending_new' => 'open',
            'accepted' => 'open',
            'new' => 'open',
            'partially_filled' => 'open',
            'activated' => 'open',
            'filled' => 'closed',
        );
        return $this->safe_string($statuses, $status, $status);
    }

    public function parse_time_in_force($timeInForce) {
        $timeInForces = array(
            'day' => 'Day',
        );
        return $this->safe_string($timeInForces, $timeInForce, $timeInForce);
    }

    public function parse_trade($trade, $market = null) {
        //
        //   {
        //       "t":"2022-06-14T05:00:00.027869Z",
        //       "x":"CBSE",
        //       "p":"21942.15",
        //       "s":"0.0001",
        //       "tks":"S",
        //       "i":"355681339"
        //   }
        //
        $marketId = $this->safe_string($trade, 'S');
        $symbol = $this->safe_symbol($marketId, $market);
        $datetime = $this->safe_string($trade, 't');
        $timestamp = $this->parse8601($datetime);
        $alpacaSide = $this->safe_string($trade, 'tks');
        $side = null;
        if ($alpacaSide === 'B') {
            $side = 'buy';
        } elseif ($alpacaSide === 'S') {
            $side = 'sell';
        }
        $priceString = $this->safe_string($trade, 'p');
        $amountString = $this->safe_string($trade, 's');
        return $this->safe_trade(array(
            'info' => $trade,
            'id' => $this->safe_string($trade, 'i'),
            'timestamp' => $timestamp,
            'datetime' => $this->iso8601($timestamp),
            'symbol' => $symbol,
            'order' => null,
            'type' => null,
            'side' => $side,
            'takerOrMaker' => 'taker',
            'price' => $priceString,
            'amount' => $amountString,
            'cost' => null,
            'fee' => null,
        ), $market);
    }

    public function sign($path, $api = 'public', $method = 'GET', $params = array (), $headers = null, $body = null) {
        $versions = $this->safe_value($this->options, 'versions');
        $version = $this->safe_string($versions, $api);
        $endpoint = '/' . $this->implode_params($path, $params);
        $url = $this->implode_params($this->urls['api'][$api], array( 'version' => $version ));
        $url = $this->implode_hostname($url);
        $headers = ($headers !== null) ? $headers : array();
        if ($api === 'private') {
            $headers['APCA-API-KEY-ID'] = $this->apiKey;
            $headers['APCA-API-SECRET-KEY'] = $this->secret;
        }
        $query = $this->omit($params, $this->extract_params($path));
        if ($query) {
            if (($method === 'GET') || ($method === 'DELETE')) {
                $endpoint .= '?' . $this->urlencode($query);
            } else {
                $body = $this->json($query);
                $headers['Content-Type'] = 'application/json';
            }
        }
        $url = $url . $endpoint;
        return array( 'url' => $url, 'method' => $method, 'body' => $body, 'headers' => $headers );
    }

    public function handle_errors($code, $reason, $url, $method, $headers, $body, $response, $requestHeaders, $requestBody) {
        if ($response === null) {
            return null; // default error handler
        }
        // {
        //     "code" => 40110000,
        //     "message" => "request is not authorized"
        // }
        $feedback = $this->id . ' ' . $body;
        $errorCode = $this->safe_string($response, 'code');
        if ($code !== null) {
            $this->throw_exactly_matched_exception($this->exceptions['exact'], $errorCode, $feedback);
        }
        $message = $this->safe_value($response, 'message', null);
        if ($message !== null) {
            $this->throw_exactly_matched_exception($this->exceptions['exact'], $message, $feedback);
            $this->throw_broadly_matched_exception($this->exceptions['broad'], $message, $feedback);
            throw new ExchangeError($feedback);
        }
        return null;
    }
}
