<?php

function pickCrazyMushrooms(){
  global $rounds_left, $location;

  if ($location === "woods") {
    echo "You pick some strange mushrooms. They look soo yummy, that you have to eat them inmediatly! They are tasty but you start to feel funny. You realize you don't care about possessions, you have all you need in this wood, you certainly have a lots of crazy mushrooms...you abandoned your quest and loose de game! \n";

    $rounds_left = 1;
  
  } else {
  echo "There are no mushrooms here, did you eat some alredy? \n";
}

}



