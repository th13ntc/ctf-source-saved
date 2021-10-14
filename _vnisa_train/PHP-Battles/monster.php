<?php
require_once 'player.php';

class monster extends player
{
	function __construct($name = "AZ-5 RBMK")
	{
		$this->name = $name;
		$this->health = 100;
		$this->maxDamage = 10;
	}
}
?>