<?php
define("GREETING", "Welcome to W3Schools.com!"); // depreciated; only false is default
echo GREETING;
echo "\n";

const MYCAR = "Volvo";
echo MYCAR;
echo "\n";

define("cars", [
    "Alfa Romeo",
    "BMW",
    "Toyota"
  ]);
  echo cars[0];
echo "\n";

function myTest() {
    echo GREETING;
} 
myTest();
echo "\n";

// Learn magic constants at a later date
?>