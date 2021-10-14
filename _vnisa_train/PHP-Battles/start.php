<?php
require_once 'player.php';
require_once 'monster.php';

if (!(isset($_COOKIE["hero"]) && $_COOKIE["hero"] !== "" && isset($_COOKIE["monster"]) && $_COOKIE["monster"] !== ""))
{
	header("Location: index.php");
	die();
}
$cHero = @base64_decode($_COOKIE["hero"]);
$cMonster = @base64_decode($_COOKIE["monster"]);
$hero = @unserialize($cHero);
$monster = @unserialize($cMonster);

if (isset($_POST["attack"]) && $_POST["attack"] === "Go")
{
	$heroHealth = $hero->GetHealth() - $monster->attack();
	if ($heroHealth <= 0)
	{
		setcookie("hero", base64_encode(serialize($hero)), time() - 1);
		setcookie("monster", base64_encode(serialize($monster)), time() - 1);
		die("Loser mannnnnnn");
	}
	$hero->SetHealth($heroHealth);
	$monsterHealth = $monster->GetHealth() - $hero->attack();
	if ($monsterHealth <= 0)
	{
		setcookie("hero", base64_encode(serialize($hero)), time() - 1);
		setcookie("monster", base64_encode(serialize($monster)), time() - 1);
		die("Winner mannnnnnn");
	}
	$monster->SetHealth($monsterHealth);
	setcookie("hero", base64_encode(serialize($hero)), time() + 2*60*60);
	setcookie("monster", base64_encode(serialize($monster)), time() + 2*60*60);
	header("Location: start.php");
	die();
}
?>
<html>
<body>
	<h2>Hello <?php echo $hero->GetName(); ?>. Let play</h2>
	<p>Your health: <?php echo $hero->GetHealth(); ?></p>
	<?php
	if ($hero->HaveWeapon())
		echo '<p>Weapon: <img src="data:image/png;base64,' . $hero->GetIcon() . '" height=30px width=30px></p>';
	?>
	<hr>
	<p>Monster's name: <?php echo $monster->GetName(); ?>. Monster's health: <?php echo $monster->GetHealth(); ?></p>
	<hr>
	<form action="#" method="POST">
	<input type="submit" name="attack" value="Go">
	</form>
</body>
</html>