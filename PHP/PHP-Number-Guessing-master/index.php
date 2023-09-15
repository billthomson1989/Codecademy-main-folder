<?php

$play_count = 0;
$correct_guesses = 0;
$guess_high = 0;
$guess_low = 0

echo "Hello, my friend, to test your phychic abilities, you'll try to guess the number I'm thinking ten times. Then we'll see how powerfull your powers are! I'm going to think of numbers between 1 and 10 (inclusive). Do you think you can guess correctly?\n";

function guessNumber(){
  
  global $play_count, $correct_guesses, $guess_high, $guess_low;

  $play_count++;

  $random_number= rand(1,10);

  echo "\nMake your guess...\n";

  $player_number = intval(readline(">>"));

  echo "Round: $play_count\nMy Number: $random_number\nYour guess: $player_number";

  if ($random_number===$player_number){
    $correct_guesses++
  }else if($random_number<$player_number){
    $guess_high++;
  }else{
    $guess_low++;
  }

}

guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();
guessNumber();

$good_guesses = $correct_guesses/$play_count * 100;

echo "\nAfter $play_count rounds, here are some facts about your guessing:\nYou guessed the number correctly $good_guesses% of the time.\n";

if ($guess_high>$guess_low){
  echo "\nWhen you guessed wrong, you tended to guess high.\n";
}elseif ($guess_high < $guess_low){
  echo "\nWhen you guessed wrong, you tended to guess low.\n"
}

