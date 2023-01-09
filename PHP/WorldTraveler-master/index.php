<?php


echo "Forgein currency";
  $riel = 2103942;
  $kyat = 19092;
  $krones = 109;
  $lek = 9094;

  echo "\n\nriels $riel";
  echo "\nkyat $kyat";
  echo "\nkrones $krones";
  echo "\nlek $lek";

echo "\n\nExchange rate";

  $riel_exchange = 0.00024;
  $kyat_exchange = 0.00073;
  $krones_exchange = 0.11;
  $lek_exchange = 0.0092;
  
  echo "\n";
  echo "\n".$riel*$riel_exchange." dlrs in riel";;
  echo "\n".$kyat*$kyat_exchange." dlrs in kyat";
   echo "\n".$krones*$krones_exchange." dlrs in krones";
   echo "\n".$lek*$lek_exchange." dlrs in lek";

//calcular final amount
$final_amount= $riel*$riel_exchange;
$final_amount--;
$final_amount+= $kyat*$kyat_exchange;
$final_amount--;
$final_amount += $krones*$krones_exchange;
$final_amount--;
$final_amount += $lek*$lek_exchange;
$final_amount--;

echo "\n\nThe total amount in dollars is ".$final_amount;

//calcular round number
$dollars_only = $final_amount % 1000000000;
$change = $final_amount - $dollars_only;
$rounded_change = $change * 100;
$rounded_change %= 100;
$rounded_change /= 100;

$final_amount = $dollars_only + $rounded_change;

echo "\nRounded change ".$final_amount;




