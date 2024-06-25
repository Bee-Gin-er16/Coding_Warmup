<?php
$x = "John";
echo "Hello $x \n"; // double quotes perform ops for special chars like "/n"

$x = "John";
echo 'Hello $x \n'.$x."\n"; // single quotes write string as is even with "\n". You can put both separately 

echo strlen("Hello world!"); // returns 12
echo "\n"; // to new line in ide but for html live testing, use <br> tag
echo str_word_count("Hello world!"); // returns 2
echo "\n";
echo strpos("Hello world!", "world");

?>