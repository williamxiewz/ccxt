from ccxt.base.types import Entry


class ImplicitAPI:
    public_spot_get_public_time = publicSpotGetPublicTime = Entry('public/time', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_public_currencies = publicSpotGetPublicCurrencies = Entry('public/currencies', ['public', 'spot'], 'GET', {'cost': 6.6667})
    public_spot_get_public_products = publicSpotGetPublicProducts = Entry('public/products', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_public_product = publicSpotGetPublicProduct = Entry('public/product', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_market_ticker = publicSpotGetMarketTicker = Entry('market/ticker', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_market_tickers = publicSpotGetMarketTickers = Entry('market/tickers', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_market_fills = publicSpotGetMarketFills = Entry('market/fills', ['public', 'spot'], 'GET', {'cost': 2})
    public_spot_get_market_fills_history = publicSpotGetMarketFillsHistory = Entry('market/fills-history', ['public', 'spot'], 'GET', {'cost': 2})
    public_spot_get_market_candles = publicSpotGetMarketCandles = Entry('market/candles', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_market_depth = publicSpotGetMarketDepth = Entry('market/depth', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_market_spot_vip_level = publicSpotGetMarketSpotVipLevel = Entry('market/spot-vip-level', ['public', 'spot'], 'GET', {'cost': 2})
    public_mix_get_market_contracts = publicMixGetMarketContracts = Entry('market/contracts', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_depth = publicMixGetMarketDepth = Entry('market/depth', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_ticker = publicMixGetMarketTicker = Entry('market/ticker', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_tickers = publicMixGetMarketTickers = Entry('market/tickers', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_contract_vip_level = publicMixGetMarketContractVipLevel = Entry('market/contract-vip-level', ['public', 'mix'], 'GET', {'cost': 2})
    public_mix_get_market_fills = publicMixGetMarketFills = Entry('market/fills', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_fills_history = publicMixGetMarketFillsHistory = Entry('market/fills-history', ['public', 'mix'], 'GET', {'cost': 2})
    public_mix_get_market_candles = publicMixGetMarketCandles = Entry('market/candles', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_index = publicMixGetMarketIndex = Entry('market/index', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_funding_time = publicMixGetMarketFundingTime = Entry('market/funding-time', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_history_fundrate = publicMixGetMarketHistoryFundRate = Entry('market/history-fundRate', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_current_fundrate = publicMixGetMarketCurrentFundRate = Entry('market/current-fundRate', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_open_interest = publicMixGetMarketOpenInterest = Entry('market/open-interest', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_mark_price = publicMixGetMarketMarkPrice = Entry('market/mark-price', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_symbol_leverage = publicMixGetMarketSymbolLeverage = Entry('market/symbol-leverage', ['public', 'mix'], 'GET', {'cost': 1})
    public_mix_get_market_querypositionlever = publicMixGetMarketQueryPositionLever = Entry('market/queryPositionLever', ['public', 'mix'], 'GET', {'cost': 1})
    public_margin_get_cross_public_interestrateandlimit = publicMarginGetCrossPublicInterestRateAndLimit = Entry('cross/public/interestRateAndLimit', ['public', 'margin'], 'GET', {'cost': 2})
    public_margin_get_isolated_public_interestrateandlimit = publicMarginGetIsolatedPublicInterestRateAndLimit = Entry('isolated/public/interestRateAndLimit', ['public', 'margin'], 'GET', {'cost': 2})
    public_margin_get_cross_public_tierdata = publicMarginGetCrossPublicTierData = Entry('cross/public/tierData', ['public', 'margin'], 'GET', {'cost': 2})
    public_margin_get_isolated_public_tierdata = publicMarginGetIsolatedPublicTierData = Entry('isolated/public/tierData', ['public', 'margin'], 'GET', {'cost': 2})
    public_margin_get_public_currencies = publicMarginGetPublicCurrencies = Entry('public/currencies', ['public', 'margin'], 'GET', {'cost': 1})
    public_margin_get_cross_account_assets = publicMarginGetCrossAccountAssets = Entry('cross/account/assets', ['public', 'margin'], 'GET', {'cost': 2})
    public_margin_get_isolated_account_assets = publicMarginGetIsolatedAccountAssets = Entry('isolated/account/assets', ['public', 'margin'], 'GET', {'cost': 2})
    private_spot_get_wallet_deposit_address = privateSpotGetWalletDepositAddress = Entry('wallet/deposit-address', ['private', 'spot'], 'GET', {'cost': 4})
    private_spot_get_wallet_withdrawal_list = privateSpotGetWalletWithdrawalList = Entry('wallet/withdrawal-list', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_wallet_deposit_list = privateSpotGetWalletDepositList = Entry('wallet/deposit-list', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_account_getinfo = privateSpotGetAccountGetInfo = Entry('account/getInfo', ['private', 'spot'], 'GET', {'cost': 20})
    private_spot_get_account_assets = privateSpotGetAccountAssets = Entry('account/assets', ['private', 'spot'], 'GET', {'cost': 2})
    private_spot_get_account_assets_lite = privateSpotGetAccountAssetsLite = Entry('account/assets-lite', ['private', 'spot'], 'GET', {'cost': 2})
    private_spot_get_account_transferrecords = privateSpotGetAccountTransferRecords = Entry('account/transferRecords', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_post_wallet_transfer = privateSpotPostWalletTransfer = Entry('wallet/transfer', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_wallet_transfer_v2 = privateSpotPostWalletTransferV2 = Entry('wallet/transfer-v2', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_wallet_subtransfer = privateSpotPostWalletSubTransfer = Entry('wallet/subTransfer', ['private', 'spot'], 'POST', {'cost': 10})
    private_spot_post_wallet_withdrawal = privateSpotPostWalletWithdrawal = Entry('wallet/withdrawal', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_wallet_withdrawal_v2 = privateSpotPostWalletWithdrawalV2 = Entry('wallet/withdrawal-v2', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_wallet_withdrawal_inner = privateSpotPostWalletWithdrawalInner = Entry('wallet/withdrawal-inner', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_wallet_withdrawal_inner_v2 = privateSpotPostWalletWithdrawalInnerV2 = Entry('wallet/withdrawal-inner-v2', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_account_sub_account_spot_assets = privateSpotPostAccountSubAccountSpotAssets = Entry('account/sub-account-spot-assets', ['private', 'spot'], 'POST', {'cost': 200})
    private_spot_post_account_bills = privateSpotPostAccountBills = Entry('account/bills', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trade_orders = privateSpotPostTradeOrders = Entry('trade/orders', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trade_batch_orders = privateSpotPostTradeBatchOrders = Entry('trade/batch-orders', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_trade_cancel_order = privateSpotPostTradeCancelOrder = Entry('trade/cancel-order', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trade_cancel_order_v2 = privateSpotPostTradeCancelOrderV2 = Entry('trade/cancel-order-v2', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trade_cancel_symbol_order = privateSpotPostTradeCancelSymbolOrder = Entry('trade/cancel-symbol-order', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trade_cancel_batch_orders = privateSpotPostTradeCancelBatchOrders = Entry('trade/cancel-batch-orders', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_trade_cancel_batch_orders_v2 = privateSpotPostTradeCancelBatchOrdersV2 = Entry('trade/cancel-batch-orders-v2', ['private', 'spot'], 'POST', {'cost': 4})
    private_spot_post_trade_orderinfo = privateSpotPostTradeOrderInfo = Entry('trade/orderInfo', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_trade_open_orders = privateSpotPostTradeOpenOrders = Entry('trade/open-orders', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_trade_history = privateSpotPostTradeHistory = Entry('trade/history', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_trade_fills = privateSpotPostTradeFills = Entry('trade/fills', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_placeplan = privateSpotPostPlanPlacePlan = Entry('plan/placePlan', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_modifyplan = privateSpotPostPlanModifyPlan = Entry('plan/modifyPlan', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_cancelplan = privateSpotPostPlanCancelPlan = Entry('plan/cancelPlan', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_currentplan = privateSpotPostPlanCurrentPlan = Entry('plan/currentPlan', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_historyplan = privateSpotPostPlanHistoryPlan = Entry('plan/historyPlan', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_plan_batchcancelplan = privateSpotPostPlanBatchCancelPlan = Entry('plan/batchCancelPlan', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_ordercurrentlist = privateSpotPostTraceOrderOrderCurrentList = Entry('trace/order/orderCurrentList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_orderhistorylist = privateSpotPostTraceOrderOrderHistoryList = Entry('trace/order/orderHistoryList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_closetrackingorder = privateSpotPostTraceOrderCloseTrackingOrder = Entry('trace/order/closeTrackingOrder', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_updatetpsl = privateSpotPostTraceOrderUpdateTpsl = Entry('trace/order/updateTpsl', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_followerendorder = privateSpotPostTraceOrderFollowerEndOrder = Entry('trace/order/followerEndOrder', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_order_spotinfolist = privateSpotPostTraceOrderSpotInfoList = Entry('trace/order/spotInfoList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_config_gettradersettings = privateSpotPostTraceConfigGetTraderSettings = Entry('trace/config/getTraderSettings', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_config_getfollowersettings = privateSpotPostTraceConfigGetFollowerSettings = Entry('trace/config/getFollowerSettings', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_user_mytraders = privateSpotPostTraceUserMyTraders = Entry('trace/user/myTraders', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_config_setfollowerconfig = privateSpotPostTraceConfigSetFollowerConfig = Entry('trace/config/setFollowerConfig', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_user_myfollowers = privateSpotPostTraceUserMyFollowers = Entry('trace/user/myFollowers', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_config_setproductcode = privateSpotPostTraceConfigSetProductCode = Entry('trace/config/setProductCode', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_user_removetrader = privateSpotPostTraceUserRemoveTrader = Entry('trace/user/removeTrader', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_profit_totalprofitinfo = privateSpotPostTraceProfitTotalProfitInfo = Entry('trace/profit/totalProfitInfo', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_profit_totalprofitlist = privateSpotPostTraceProfitTotalProfitList = Entry('trace/profit/totalProfitList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_profit_profithislist = privateSpotPostTraceProfitProfitHisList = Entry('trace/profit/profitHisList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_profit_profithisdetaillist = privateSpotPostTraceProfitProfitHisDetailList = Entry('trace/profit/profitHisDetailList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_profit_waitprofitdetaillist = privateSpotPostTraceProfitWaitProfitDetailList = Entry('trace/profit/waitProfitDetailList', ['private', 'spot'], 'POST', {'cost': 2})
    private_spot_post_trace_user_gettraderinfo = privateSpotPostTraceUserGetTraderInfo = Entry('trace/user/getTraderInfo', ['private', 'spot'], 'POST', {'cost': 2})
    private_mix_get_account_account = privateMixGetAccountAccount = Entry('account/account', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_account_accounts = privateMixGetAccountAccounts = Entry('account/accounts', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_position_singleposition = privateMixGetPositionSinglePosition = Entry('position/singlePosition', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_position_singleposition_v2 = privateMixGetPositionSinglePositionV2 = Entry('position/singlePosition-v2', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_position_allposition = privateMixGetPositionAllPosition = Entry('position/allPosition', ['private', 'mix'], 'GET', {'cost': 4})
    private_mix_get_position_allposition_v2 = privateMixGetPositionAllPositionV2 = Entry('position/allPosition-v2', ['private', 'mix'], 'GET', {'cost': 4})
    private_mix_get_account_accountbill = privateMixGetAccountAccountBill = Entry('account/accountBill', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_account_accountbusinessbill = privateMixGetAccountAccountBusinessBill = Entry('account/accountBusinessBill', ['private', 'mix'], 'GET', {'cost': 4})
    private_mix_get_order_current = privateMixGetOrderCurrent = Entry('order/current', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_order_margincoincurrent = privateMixGetOrderMarginCoinCurrent = Entry('order/marginCoinCurrent', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_order_history = privateMixGetOrderHistory = Entry('order/history', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_order_historyproducttype = privateMixGetOrderHistoryProductType = Entry('order/historyProductType', ['private', 'mix'], 'GET', {'cost': 4})
    private_mix_get_order_detail = privateMixGetOrderDetail = Entry('order/detail', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_order_fills = privateMixGetOrderFills = Entry('order/fills', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_order_allfills = privateMixGetOrderAllFills = Entry('order/allFills', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_plan_currentplan = privateMixGetPlanCurrentPlan = Entry('plan/currentPlan', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_plan_historyplan = privateMixGetPlanHistoryPlan = Entry('plan/historyPlan', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_currenttrack = privateMixGetTraceCurrentTrack = Entry('trace/currentTrack', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_followerorder = privateMixGetTraceFollowerOrder = Entry('trace/followerOrder', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_followerhistoryorders = privateMixGetTraceFollowerHistoryOrders = Entry('trace/followerHistoryOrders', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_historytrack = privateMixGetTraceHistoryTrack = Entry('trace/historyTrack', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_summary = privateMixGetTraceSummary = Entry('trace/summary', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_trace_profitsettletokenidgroup = privateMixGetTraceProfitSettleTokenIdGroup = Entry('trace/profitSettleTokenIdGroup', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_trace_profitdategrouplist = privateMixGetTraceProfitDateGroupList = Entry('trace/profitDateGroupList', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_trade_profitdatelist = privateMixGetTradeProfitDateList = Entry('trade/profitDateList', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_waitprofitdatelist = privateMixGetTraceWaitProfitDateList = Entry('trace/waitProfitDateList', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_trace_tradersymbols = privateMixGetTraceTraderSymbols = Entry('trace/traderSymbols', ['private', 'mix'], 'GET', {'cost': 1})
    private_mix_get_trace_traderlist = privateMixGetTraceTraderList = Entry('trace/traderList', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_traderdetail = privateMixGetTraceTraderDetail = Entry('trace/traderDetail', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_get_trace_querytraceconfig = privateMixGetTraceQueryTraceConfig = Entry('trace/queryTraceConfig', ['private', 'mix'], 'GET', {'cost': 2})
    private_mix_post_account_sub_account_contract_assets = privateMixPostAccountSubAccountContractAssets = Entry('account/sub-account-contract-assets', ['private', 'mix'], 'POST', {'cost': 200})
    private_mix_post_account_open_count = privateMixPostAccountOpenCount = Entry('account/open-count', ['private', 'mix'], 'POST', {'cost': 1})
    private_mix_post_account_setleverage = privateMixPostAccountSetLeverage = Entry('account/setLeverage', ['private', 'mix'], 'POST', {'cost': 4})
    private_mix_post_account_setmargin = privateMixPostAccountSetMargin = Entry('account/setMargin', ['private', 'mix'], 'POST', {'cost': 4})
    private_mix_post_account_setmarginmode = privateMixPostAccountSetMarginMode = Entry('account/setMarginMode', ['private', 'mix'], 'POST', {'cost': 4})
    private_mix_post_account_setpositionmode = privateMixPostAccountSetPositionMode = Entry('account/setPositionMode', ['private', 'mix'], 'POST', {'cost': 4})
    private_mix_post_order_placeorder = privateMixPostOrderPlaceOrder = Entry('order/placeOrder', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_batch_orders = privateMixPostOrderBatchOrders = Entry('order/batch-orders', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_cancel_order = privateMixPostOrderCancelOrder = Entry('order/cancel-order', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_cancel_batch_orders = privateMixPostOrderCancelBatchOrders = Entry('order/cancel-batch-orders', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_modifyorder = privateMixPostOrderModifyOrder = Entry('order/modifyOrder', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_cancel_symbol_orders = privateMixPostOrderCancelSymbolOrders = Entry('order/cancel-symbol-orders', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_cancel_all_orders = privateMixPostOrderCancelAllOrders = Entry('order/cancel-all-orders', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_order_close_all_positions = privateMixPostOrderCloseAllPositions = Entry('order/close-all-positions', ['private', 'mix'], 'POST', {'cost': 20})
    private_mix_post_plan_placeplan = privateMixPostPlanPlacePlan = Entry('plan/placePlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_modifyplan = privateMixPostPlanModifyPlan = Entry('plan/modifyPlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_modifyplanpreset = privateMixPostPlanModifyPlanPreset = Entry('plan/modifyPlanPreset', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_placetpsl = privateMixPostPlanPlaceTPSL = Entry('plan/placeTPSL', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_placetrailstop = privateMixPostPlanPlaceTrailStop = Entry('plan/placeTrailStop', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_placepositionstpsl = privateMixPostPlanPlacePositionsTPSL = Entry('plan/placePositionsTPSL', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_modifytpslplan = privateMixPostPlanModifyTPSLPlan = Entry('plan/modifyTPSLPlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_cancelplan = privateMixPostPlanCancelPlan = Entry('plan/cancelPlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_cancelsymbolplan = privateMixPostPlanCancelSymbolPlan = Entry('plan/cancelSymbolPlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_plan_cancelallplan = privateMixPostPlanCancelAllPlan = Entry('plan/cancelAllPlan', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_closetrackorder = privateMixPostTraceCloseTrackOrder = Entry('trace/closeTrackOrder', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_modifytpsl = privateMixPostTraceModifyTPSL = Entry('trace/modifyTPSL', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_setupcopysymbols = privateMixPostTraceSetUpCopySymbols = Entry('trace/setUpCopySymbols', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_followersetbatchtraceconfig = privateMixPostTraceFollowerSetBatchTraceConfig = Entry('trace/followerSetBatchTraceConfig', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_followerclosebytrackingno = privateMixPostTraceFollowerCloseByTrackingNo = Entry('trace/followerCloseByTrackingNo', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_followerclosebyall = privateMixPostTraceFollowerCloseByAll = Entry('trace/followerCloseByAll', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_followersettpsl = privateMixPostTraceFollowerSetTpsl = Entry('trace/followerSetTpsl', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_cancelcopytrader = privateMixPostTraceCancelCopyTrader = Entry('trace/cancelCopyTrader', ['private', 'mix'], 'POST', {'cost': 4})
    private_mix_post_trace_traderupdateconfig = privateMixPostTraceTraderUpdateConfig = Entry('trace/traderUpdateConfig', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_mytraderlist = privateMixPostTraceMyTraderList = Entry('trace/myTraderList', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_myfollowerlist = privateMixPostTraceMyFollowerList = Entry('trace/myFollowerList', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_removefollower = privateMixPostTraceRemoveFollower = Entry('trace/removeFollower', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_public_getfollowerconfig = privateMixPostTracePublicGetFollowerConfig = Entry('trace/public/getFollowerConfig', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_report_order_historylist = privateMixPostTraceReportOrderHistoryList = Entry('trace/report/order/historyList', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_report_order_currentlist = privateMixPostTraceReportOrderCurrentList = Entry('trace/report/order/currentList', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_querytradertpslratioconfig = privateMixPostTraceQueryTraderTpslRatioConfig = Entry('trace/queryTraderTpslRatioConfig', ['private', 'mix'], 'POST', {'cost': 2})
    private_mix_post_trace_traderupdatetpslratioconfig = privateMixPostTraceTraderUpdateTpslRatioConfig = Entry('trace/traderUpdateTpslRatioConfig', ['private', 'mix'], 'POST', {'cost': 2})
    private_user_get_fee_query = privateUserGetFeeQuery = Entry('fee/query', ['private', 'user'], 'GET', {'cost': 2})
    private_user_get_sub_virtual_list = privateUserGetSubVirtualList = Entry('sub/virtual-list', ['private', 'user'], 'GET', {'cost': 2})
    private_user_get_sub_virtual_api_list = privateUserGetSubVirtualApiList = Entry('sub/virtual-api-list', ['private', 'user'], 'GET', {'cost': 2})
    private_user_post_sub_virtual_create = privateUserPostSubVirtualCreate = Entry('sub/virtual-create', ['private', 'user'], 'POST', {'cost': 4})
    private_user_post_sub_virtual_modify = privateUserPostSubVirtualModify = Entry('sub/virtual-modify', ['private', 'user'], 'POST', {'cost': 4})
    private_user_post_sub_virtual_api_batch_create = privateUserPostSubVirtualApiBatchCreate = Entry('sub/virtual-api-batch-create', ['private', 'user'], 'POST', {'cost': 20})
    private_user_post_sub_virtual_api_create = privateUserPostSubVirtualApiCreate = Entry('sub/virtual-api-create', ['private', 'user'], 'POST', {'cost': 4})
    private_user_post_sub_virtual_api_modify = privateUserPostSubVirtualApiModify = Entry('sub/virtual-api-modify', ['private', 'user'], 'POST', {'cost': 4})
    private_p2p_get_merchant_merchantlist = privateP2pGetMerchantMerchantList = Entry('merchant/merchantList', ['private', 'p2p'], 'GET', {'cost': 2})
    private_p2p_get_merchant_merchantinfo = privateP2pGetMerchantMerchantInfo = Entry('merchant/merchantInfo', ['private', 'p2p'], 'GET', {'cost': 2})
    private_p2p_get_merchant_advlist = privateP2pGetMerchantAdvList = Entry('merchant/advList', ['private', 'p2p'], 'GET', {'cost': 2})
    private_p2p_get_merchant_orderlist = privateP2pGetMerchantOrderList = Entry('merchant/orderList', ['private', 'p2p'], 'GET', {'cost': 2})
    private_broker_get_account_info = privateBrokerGetAccountInfo = Entry('account/info', ['private', 'broker'], 'GET', {'cost': 2})
    private_broker_get_account_sub_list = privateBrokerGetAccountSubList = Entry('account/sub-list', ['private', 'broker'], 'GET', {'cost': 20})
    private_broker_get_account_sub_email = privateBrokerGetAccountSubEmail = Entry('account/sub-email', ['private', 'broker'], 'GET', {'cost': 20})
    private_broker_get_account_sub_spot_assets = privateBrokerGetAccountSubSpotAssets = Entry('account/sub-spot-assets', ['private', 'broker'], 'GET', {'cost': 2})
    private_broker_get_account_sub_future_assets = privateBrokerGetAccountSubFutureAssets = Entry('account/sub-future-assets', ['private', 'broker'], 'GET', {'cost': 2})
    private_broker_get_account_sub_api_list = privateBrokerGetAccountSubApiList = Entry('account/sub-api-list', ['private', 'broker'], 'GET', {'cost': 2})
    private_broker_post_account_sub_create = privateBrokerPostAccountSubCreate = Entry('account/sub-create', ['private', 'broker'], 'POST', {'cost': 20})
    private_broker_post_account_sub_modify = privateBrokerPostAccountSubModify = Entry('account/sub-modify', ['private', 'broker'], 'POST', {'cost': 20})
    private_broker_post_account_sub_modify_email = privateBrokerPostAccountSubModifyEmail = Entry('account/sub-modify-email', ['private', 'broker'], 'POST', {'cost': 20})
    private_broker_post_account_sub_address = privateBrokerPostAccountSubAddress = Entry('account/sub-address', ['private', 'broker'], 'POST', {'cost': 2})
    private_broker_post_account_sub_withdrawal = privateBrokerPostAccountSubWithdrawal = Entry('account/sub-withdrawal', ['private', 'broker'], 'POST', {'cost': 2})
    private_broker_post_account_sub_auto_transfer = privateBrokerPostAccountSubAutoTransfer = Entry('account/sub-auto-transfer', ['private', 'broker'], 'POST', {'cost': 4})
    private_broker_post_account_sub_api_create = privateBrokerPostAccountSubApiCreate = Entry('account/sub-api-create', ['private', 'broker'], 'POST', {'cost': 2})
    private_broker_post_account_sub_api_modify = privateBrokerPostAccountSubApiModify = Entry('account/sub-api-modify', ['private', 'broker'], 'POST', {'cost': 2})
    private_margin_get_cross_account_riskrate = privateMarginGetCrossAccountRiskRate = Entry('cross/account/riskRate', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_account_maxtransferoutamount = privateMarginGetCrossAccountMaxTransferOutAmount = Entry('cross/account/maxTransferOutAmount', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_account_maxtransferoutamount = privateMarginGetIsolatedAccountMaxTransferOutAmount = Entry('isolated/account/maxTransferOutAmount', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_order_openorders = privateMarginGetIsolatedOrderOpenOrders = Entry('isolated/order/openOrders', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_order_history = privateMarginGetIsolatedOrderHistory = Entry('isolated/order/history', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_order_fills = privateMarginGetIsolatedOrderFills = Entry('isolated/order/fills', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_loan_list = privateMarginGetIsolatedLoanList = Entry('isolated/loan/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_repay_list = privateMarginGetIsolatedRepayList = Entry('isolated/repay/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_interest_list = privateMarginGetIsolatedInterestList = Entry('isolated/interest/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_liquidation_list = privateMarginGetIsolatedLiquidationList = Entry('isolated/liquidation/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_isolated_fin_list = privateMarginGetIsolatedFinList = Entry('isolated/fin/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_order_openorders = privateMarginGetCrossOrderOpenOrders = Entry('cross/order/openOrders', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_order_history = privateMarginGetCrossOrderHistory = Entry('cross/order/history', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_order_fills = privateMarginGetCrossOrderFills = Entry('cross/order/fills', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_loan_list = privateMarginGetCrossLoanList = Entry('cross/loan/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_repay_list = privateMarginGetCrossRepayList = Entry('cross/repay/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_interest_list = privateMarginGetCrossInterestList = Entry('cross/interest/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_liquidation_list = privateMarginGetCrossLiquidationList = Entry('cross/liquidation/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_get_cross_fin_list = privateMarginGetCrossFinList = Entry('cross/fin/list', ['private', 'margin'], 'GET', {'cost': 2})
    private_margin_post_cross_account_borrow = privateMarginPostCrossAccountBorrow = Entry('cross/account/borrow', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_account_borrow = privateMarginPostIsolatedAccountBorrow = Entry('isolated/account/borrow', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_account_repay = privateMarginPostCrossAccountRepay = Entry('cross/account/repay', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_account_repay = privateMarginPostIsolatedAccountRepay = Entry('isolated/account/repay', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_account_riskrate = privateMarginPostIsolatedAccountRiskRate = Entry('isolated/account/riskRate', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_account_maxborrowableamount = privateMarginPostCrossAccountMaxBorrowableAmount = Entry('cross/account/maxBorrowableAmount', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_account_maxborrowableamount = privateMarginPostIsolatedAccountMaxBorrowableAmount = Entry('isolated/account/maxBorrowableAmount', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_order_placeorder = privateMarginPostIsolatedOrderPlaceOrder = Entry('isolated/order/placeOrder', ['private', 'margin'], 'POST', {'cost': 4})
    private_margin_post_isolated_order_batchplaceorder = privateMarginPostIsolatedOrderBatchPlaceOrder = Entry('isolated/order/batchPlaceOrder', ['private', 'margin'], 'POST', {'cost': 4})
    private_margin_post_isolated_order_cancelorder = privateMarginPostIsolatedOrderCancelOrder = Entry('isolated/order/cancelOrder', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_isolated_order_batchcancelorder = privateMarginPostIsolatedOrderBatchCancelOrder = Entry('isolated/order/batchCancelOrder', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_order_placeorder = privateMarginPostCrossOrderPlaceOrder = Entry('cross/order/placeOrder', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_order_batchplaceorder = privateMarginPostCrossOrderBatchPlaceOrder = Entry('cross/order/batchPlaceOrder', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_order_cancelorder = privateMarginPostCrossOrderCancelOrder = Entry('cross/order/cancelOrder', ['private', 'margin'], 'POST', {'cost': 2})
    private_margin_post_cross_order_batchcancelorder = privateMarginPostCrossOrderBatchCancelOrder = Entry('cross/order/batchCancelOrder', ['private', 'margin'], 'POST', {'cost': 2})
