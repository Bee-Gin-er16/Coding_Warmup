<?php

$x = 5;
$y = "John";
echo "I love " . $x . "!\n";
$x = 5;
$y = 4;
echo "{$x} plus {$y} equals " .($x + $y). " an integer\n";

function myTest() {
    static $x = 0;
    echo (($x < 3) ? $x : "No more loops"). "\n";
    $x++;
}

myTest();
myTest();
myTest();
myTest();

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

?>