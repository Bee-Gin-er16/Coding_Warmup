<?php
echo "Hello\n";
//same as:
echo("Hello\n");

$txt1 = "Learn PHP";
$txt2 = "W3Schools.com";

// text can contain html markup. have not tested this in html yet
echo "<h2>$txt1</h2> \n"; 
echo "<p>Study PHP at $txt2</p> \n";
echo '<h2>' . $txt1 . '</h2>'; // single quote
echo "\n<h2>" . $txt1 . "</h2> \n"; // double quotes make it easier to newline

?>