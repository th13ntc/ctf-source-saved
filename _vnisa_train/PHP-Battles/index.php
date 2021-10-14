<?php
require_once 'player.php';
require_once 'monster.php';

if (isset($_POST["submit"]) && $_POST["submit"] === "Send")
{
	$name = isset($_POST["name"]) ? $_POST["name"] : "Len Stal Put 'in";
	$hero = new player($name);
	setcookie("hero", base64_encode(serialize($hero)), time() + 2*60*60);
	$monster = new monster();
	setcookie("monster", base64_encode(serialize($monster)), time() + 2*60*60);
	header("Location: start.php");
	die();
}
else
{
	echo '<html>
	<head>
		<title>Pentest this game</title>
	</head>
	<body>
	<form action="#" method="POST">
		<input type="text" name="name" placeholder="Player\'s name">
		<br>
		<input type="submit" name="submit" value="Send">
	</form>
	</body>
</html>';
}
?>
