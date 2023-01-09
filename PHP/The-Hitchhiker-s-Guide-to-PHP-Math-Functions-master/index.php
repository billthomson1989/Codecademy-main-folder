<?php
$initial = '555';

//Find a PHP function to convert this octal string ($initial) to a decimal number.
$a= octdec($initial);
echo $a."\n";

//The value of $a is a number of degrees. Use a PHP function to convert it to radians and store the result in a new variable, $b.

$b = deg2rad($a);
echo $b."\n";

//take the cosine of $b and store it in a new variable, $c.

$c = cos($b);
echo $c."\n";

//round $c to 3 decimal places and store the result in a new variable, $d.

$d = round($c, 3);
echo $d."\n";

//take the natural log of $d and store the result in a new variable, $e.

$e = log($d);
echo $e."\n";

//take the absolute value of $e and store it in $f.

$f = abs($e);
echo $f."\n";

//take the inverse, or arc cosine of $f and store the result in $g.

$g = acos($f);
echo $g."\n";

//$g is a number in radians. Use a PHP function to convert this to a number of degrees and store it as $h.

$h = rad2deg($g);
echo $h."\n";

//floor (round down) $h and store the result in $i.

$i = floor($h);
echo $i."\n";



