<?php
$x = "Hello World!";
echo substr($x, 6, 5); // start at 6 index continue 5 steps after
echo "\n";

$x = "Hello World!";
echo substr($x, 6); // start at 6 up to end (no 2nd args)
echo "\n";

$x = "Hello World!";
echo substr($x, -5, 3); // using negative indexing, get 3 chars starting from 'o' [-5] on the index. the negative index counting starts at -1
echo "\n";

$x = "Hi, how are you?";
echo substr($x, 5, -3); // start from 5, get all chars until -3 is hit
echo "\n";

?>