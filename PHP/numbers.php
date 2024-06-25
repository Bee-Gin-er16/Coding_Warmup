<?php
$a = 5;
$b = 5.34;
$c = "25";
var_dump($a); // int(5)
var_dump($b); // float(5.34)
var_dump($c); // string(2) "25"
echo "\n";

$x = 5985;
var_dump(is_int($x)); // bool(true)
echo "\n";

$x = 59.85;
var_dump(is_int($x)); // bool(false)
echo "\n";

$x = 10.365;
var_dump(is_float($x)); // bool (true)
echo "\n";

$x = 1.9e411;
var_dump($x); // float (INF)
echo "\n";

$x = acos(8); 
var_dump($x); // float (NAN)
echo "\n";

$x = 5985;
var_dump(is_numeric($x)); // bool (true)
echo "\n";

$x = "5985";
var_dump(is_numeric($x)); // bool (true)
echo "\n";

$x = "59.85" + 100;
var_dump(is_numeric($x)); // bool (true)
echo "\n";

$x = "Hello";
var_dump(is_numeric($x)); // bool (false)
echo "\n";

$x = 23465.768;
$int_cast = (int)$x; // convert float to int
echo $int_cast;
echo "\n";

$x = "23465.768";
$int_cast = (int)$x; // convert string to int
echo $int_cast;
echo "\n";

// casting will just be searched

?>