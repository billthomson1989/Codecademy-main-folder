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
<h3>Addition</h3>
<form method = "get">
First number: <br><input type= "number" name= "first"><br><br>
Second number: <br><input type="number" name= "second"><br><br>
<button type="submit" formaction="/addition.php">Add</button><br><br>

<h3>Division</h3>

Numerator: <br><input type= "number" name= "numerator"><br><br>
Denominator:<br> <input type="number" name= "denominator"><br><br>
<button type="submit" formaction="/division.php">Divide</button><br><br>

<h3>Calculate hypotenuse</h3>
Adjacent:<br> <input type= "number" name= "adjacent"><br><br>
Opposite:<br> <input type="number" name= "opposite"><br><br>
<button type="submit" formaction="/pitagoras.php">Pitagorize!</button><br>
</form><br><br>
<a href="index.php">Reset</a>
</body>
</html>