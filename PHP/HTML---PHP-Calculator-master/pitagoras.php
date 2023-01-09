<html>
<head>
	<LINK REL=stylesheet HREF="index.css" TITLE="Consola" MEDIA=screen>
    <meta charset="UTF-8">
    <title>HTML for Dummies</title>
   
    <link href="https://fonts.googleapis.com/css?family=Orbitron:400,800|Press+Start+2P&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Source+Code+Pro:400,900|VT323&display=swap" rel="stylesheet">
</head>
<body>
<?php 
function pitagorize (){
$Adjacent=$_GET["adjacent"];
$Opposite=$_GET["opposite"];
//Hypotenuse
$Hypotenuse1 = (pow($Adjacent,2)) + (pow($Opposite,2));
$Hypotenuse1=sqrt($Hypotenuse1);
return $Hypotenuse1;
}
?>

<?= "Side one: ".$_GET["adjacent"]?>
<br>
<?="Side two: ". $_GET["opposite"]?>
<br> 
<?="Hypotenuse: ". pitagorize();?>
<br><br>

<a href="index.php">Reset</a>
</body>
</html>