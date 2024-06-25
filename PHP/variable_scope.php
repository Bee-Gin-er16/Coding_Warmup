<?php
// change a global variable to 24 by using $GLOBALS
function change() {
    $GLOBALS['x'] = 24; // $GLOBALS[indexofglobal]
  }
  
  // whenever this fxn is run, the local variable wont be deleted and still maintains its value
  function myTest() {
      static $x = 0; // static local variable
      echo (($x < 1) ? 
      $x : "No more loops after ".$x."!"). "\n";
      $x++;
  }
  
  myTest();
  myTest();
  change();
  echo $x. "\n\n"; // outputs 24
?>