<?php
$x = "Hello World!";
echo ("" .strtoupper($x). "\n"); // upper
echo ("" .strtolower($x). "\n"); // lower
echo str_replace("World", "Dolly", $x); // replace
echo "\n";
echo strrev($x); // reverse strings
echo "\n";
echo trim($x); // remove whitespace on start and ends only
echo "\n";
$y = explode(" ", $x); // split a given string into arrays for every white space
print_r($y); // the only way to print arrays
echo "\n";

?>