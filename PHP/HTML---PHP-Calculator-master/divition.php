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
<?= $_GET["numerator"]." / ". $_GET["denominator"]." = ". $_GET["numerator"]/$_GET["denominator"];?>
<br><br>

<a href="index.php">Reset</a>
</body>
</html>