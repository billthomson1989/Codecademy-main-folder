<?php
  // Change player location
function changeLocation(){	
  global $location;

  echo "Where do you want to go?\n";
  $comand = strtolower(readline(">>"));

  switch ($comand){
    
    case $comand==="bathroom":
      if ($location === "kitchen"){
        echo "You go to: bathroom.\n";
        $location = "bathroom";
      }else {
        echo "You can't go directly to there from $location. Try going somewhere else first.\n";
      }
    break;

    case $comand==="woods":
    if ($location === "kitchen"){
        echo "You follow the winding path, shivering as you make your way deep into the Terror Woods.\n";
        $location = "woods";
      }else {
        echo "You can't go directly to there from $location. Try going somewhere else first.\n";
      }
    break;

    case $comand==="kitchen":
    if ($location === "woods"||$location === "bathroom"){
        echo "You go to: kitchen.\n";
        $location = "kitchen";
      }else {
        echo "You can't go directly to there from $location. Try going somewhere else first.\n";
      }
    break;

    default:
    echo "That doesn't make sense. Are you confused? Try 'look around'.\n";
    break;
  
  }



  
  
  
  
}