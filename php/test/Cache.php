<?php
namespace ccxtpro;
include_once __DIR__ . '/../../vendor/autoload.php';
// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -----------------------------------------------------------------------------

function equals($a, $b) {
    return json_encode($a) === json_encode($b);
}

// ----------------------------------------------------------------------------

$cache = new ArrayCache (3);

$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 1 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 2 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 3 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 4 ));

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'data' => 2 ),
    array( 'symbol' => 'BTC/USDT', 'data' => 3 ),
    array( 'symbol' => 'BTC/USDT', 'data' => 4 ),
)));

$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 5 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 6 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 7 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 8 ));

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'data' => 6 ),
    array( 'symbol' => 'BTC/USDT', 'data' => 7 ),
    array( 'symbol' => 'BTC/USDT', 'data' => 8 ),
)));

$cache->clear ();

$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 1 ));

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'data' => 1 ),
)));

// ----------------------------------------------------------------------------

$cache = new ArrayCache (1);

$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 1 ));
$cache->append (array( 'symbol' => 'BTC/USDT', 'data' => 2 ));

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'data' => 2 ),
)));

// ----------------------------------------------------------------------------

$cache = new ArrayCacheByTimestamp ();

$ohlcv1 = [100, 1, 2, 3];
$ohlcv2 = [200, 5, 6, 7];
$cache->append ($ohlcv1);
$cache->append ($ohlcv2);

assert (equals ($cache, [$ohlcv1, $ohlcv2]));

$modify2 = [200, 10, 11, 12];
$cache->append ($modify2);

assert (equals ($cache, [$ohlcv1, $modify2]));

// ----------------------------------------------------------------------------

$cache = new ArrayCacheBySymbolById ();

$object1 = array( 'symbol' => 'BTC/USDT', 'id' => 'abcdef', 'i' => 1 );
$object2 = array( 'symbol' => 'ETH/USDT', 'id' => 'qwerty', 'i' => 2 );
$object3 = array( 'symbol' => 'BTC/USDT', 'id' => 'abcdef', 'i' => 3 );
$cache->append ($object1);
$cache->append ($object2);
$cache->append ($object3); // should update index 0

assert (equals ($cache, array( $object2, $object3 )));

$cache = new ArrayCacheBySymbolById (5);

for ($i = 1; $i < 11; $i++) {
    $cache->append (array(
        'symbol' => 'BTC/USDT',
        'id' => (string) $i,
        'i' => $i,
    ));
}

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '6', 'i' => 6 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 7 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 8 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '9', 'i' => 9 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '10', 'i' => 10 ),
)));

for ($i = 1; $i < 11; $i++) {
    $cache->append (array(
        'symbol' => 'BTC/USDT',
        'id' => (string) $i,
        'i' => $i + 10,
    ));
}

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '6', 'i' => 16 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 17 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 18 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '9', 'i' => 19 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '10', 'i' => 20 ),
)));

$middle = array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 28 );
$cache->append ($middle);

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '6', 'i' => 16 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 17 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '9', 'i' => 19 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '10', 'i' => 20 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 28 ),
)));

$otherMiddle = array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 27 );
$cache->append ($otherMiddle);

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '6', 'i' => 16 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '9', 'i' => 19 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '10', 'i' => 20 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 28 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 27 ),
)));

for ($i = 30; $i < 33; $i++) {
    $cache->append (array(
        'symbol' => 'BTC/USDT',
        'id' => (string) $i,
        'i' => $i + 10,
    ));
}

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 28 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 27 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '30', 'i' => 40 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '31', 'i' => 41 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '32', 'i' => 42 ) )));

$first = array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 38 );
$cache->append ($first);

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 27 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '30', 'i' => 40 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '31', 'i' => 41 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '32', 'i' => 42 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 38 ),
)));

$another = array( 'symbol' => 'BTC/USDT', 'id' => '30', 'i' => 50 );
$cache->append ($another);

assert (equals ($cache, array(
    array( 'symbol' => 'BTC/USDT', 'id' => '7', 'i' => 27 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '31', 'i' => 41 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '32', 'i' => 42 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '8', 'i' => 38 ),
    array( 'symbol' => 'BTC/USDT', 'id' => '30', 'i' => 50 ),
)));

// ----------------------------------------------------------------------------

// test ArrayCacheBySymbolById limit with $symbol set
$symbol = 'BTC/USDT';
$cache = new ArrayCacheBySymbolById ();
$initialLength = 5;
for ($i = 0; $i < $initialLength; $i++) {
    $cache->append (array(
        'symbol' => $symbol,
        'id' => (string) $i,
        'i' => $i,
    ));
}

$limited = $cache->getLimit ($symbol, null);

assert ($initialLength === $limited);

$appendItemsLength = 3;
for ($i = 0; $i < $appendItemsLength; $i++) {
    $cache->append (array(
        'symbol' => $symbol,
        'id' => (string) $i,
        'i' => $i,
    ));
}
$outsideLimit = 5;
$limited = $cache->getLimit ($symbol, $outsideLimit);

assert ($appendItemsLength === $limited);

$outsideLimit = 2; // if limit < newsUpdate that should be returned
$limited = $cache->getLimit ($symbol, $outsideLimit);

assert ($outsideLimit === $limited);

// ----------------------------------------------------------------------------

// test ArrayCacheBySymbolById limit with $symbol null
$symbol = null;
$cache = new ArrayCacheBySymbolById ();
$initialLength = 5;
for ($i = 0; $i < $initialLength; $i++) {
    $cache->append (array(
        'symbol' => $symbol,
        'id' => (string) $i,
        'i' => $i,
    ));
}

$limited = $cache->getLimit ($symbol, null);

assert ($initialLength === $limited);

$appendItemsLength = 3;
for ($i = 0; $i < $appendItemsLength; $i++) {
    $cache->append (array(
        'symbol' => $symbol,
        'id' => (string) $i,
        'i' => $i,
    ));
}
$outsideLimit = 5;
$limited = $cache->getLimit ($symbol, $outsideLimit);

assert ($appendItemsLength === $limited);

$outsideLimit = 2; // if limit < newsUpdate that should be returned
$limited = $cache->getLimit ($symbol, $outsideLimit);

assert ($outsideLimit === $limited);

// ----------------------------------------------------------------------------
// test testLimitArrayCacheByTimestamp limit

$cache = new ArrayCacheByTimestamp ();

$initialLength = 5;
for ($i = 0; $i < $initialLength; $i++) {
    $cache->append (array(
        $i * 10,
        $i * 10,
        $i * 10,
        $i * 10
    ));
}

$limited = $cache->getLimit (null, null);

assert ($initialLength === $limited);

$appendItemsLength = 3;
for ($i = 0; $i < $appendItemsLength; $i++) {
    $cache->append (array(
        $i * 4,
        $i * 4,
        $i * 4,
        $i * 4
    ));
}
$outsideLimit = 5;
$limited = $cache->getLimit (null, $outsideLimit);

assert ($appendItemsLength === $limited);

$outsideLimit = 2; // if limit < newsUpdate that should be returned
$limited = $cache->getLimit (null, $outsideLimit);

assert ($outsideLimit === $limited);
