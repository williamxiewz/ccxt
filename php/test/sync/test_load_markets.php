<?php
namespace ccxt;
use \ccxt\Precise;

// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------
include_once __DIR__ . '/../base/test_market.php';

function test_load_markets($exchange, $skipped_properties) {
    $method = 'loadMarkets';
    $markets = $exchange->load_markets();
    assert(is_array($exchange->markets), '.markets is not an object');
    assert(gettype($exchange->symbols) === 'array' && array_keys($exchange->symbols) === array_keys(array_keys($exchange->symbols)), '.symbols is not an array');
    $symbols_length = count($exchange->symbols);
    $market_keys = is_array($exchange->markets) ? array_keys($exchange->markets) : array();
    $market_keys_length = count($market_keys);
    assert($symbols_length > 0, '.symbols count <= 0 (less than or equal to zero)');
    assert($market_keys_length > 0, '.markets objects keys length <= 0 (less than or equal to zero)');
    assert($symbols_length === $market_keys_length, 'number of .symbols is not equal to the number of .markets');
    $market_values = is_array($markets) ? array_values($markets) : array();
    for ($i = 0; $i < count($market_values); $i++) {
        test_market($exchange, $skipped_properties, $method, $market_values[$i]);
    }
}
