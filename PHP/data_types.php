<?php
$x = 5;
var_dump($x); // prints data type and value
echo "<br>"; // during running in html, this will linebreak but in ide, it just displays br

$x = "Hello world!"; 
$y = 'Hello world!';

var_dump($x); // prints data type, length and value if the variable is a string
echo "<br>";
var_dump($y);

$x = 10.365;
var_dump($x); // float

$x = true;
var_dump($x); // bool

$cars = array("Volvo","BMW","Toyota");
var_dump($cars); //prints data type, length and array contents w/index if the variable is an array

class Car {
    public $color;
    public $model;
    public function __construct($color, $model) {
      $this->color = $color;
      $this->model = $model;
    }
    public function message() {
      return "My car is a " . $this->color . " " . $this->model . "!";
    }
}
  
$myCar = new Car("red", "Volvo");
var_dump($myCar);

$x = "Hello world!";
$x = null;
var_dump($x); // prints null 

$x = 5;
var_dump($x);
// changing data type
$x = "Hello";
var_dump($x);

$x = 5;
$x = (string) $x;
var_dump($x); // change by cast

?>