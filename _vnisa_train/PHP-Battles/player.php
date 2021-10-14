<?php
require_once 'weaporn.php';

class player
{
	protected $name;
	protected $maxDamage;
	protected $health;

	function __construct($name)
	{
		$this->name = $name;
		$this->health = 100;
		$this->maxDamage = 10;
	}

	public function GetName()
	{
		return $this->name;
	}

	public function GetHealth()
	{
		return $this->health;
	}

	public function SetHealth($health)
	{
		$this->health = $health;
	}

	public function attack()
	{
		return rand(0, $this->maxDamage);
	}

	public function HaveWeapon()
	{
		return false;
	}
}

class vipPlayer extends player
{
	private $weapon;

	function __construct($name)
	{
		$this->name = $name;
		$this->health = 200;
		$this->weapon = new weapon();
		$this->maxDamage = $this->weapon->GetMaxDamage();
	}

	public function GetIcon()
	{
		return base64_encode($this->weapon->GetIcon());
	}

	public function HaveWeapon()
	{
		return true;
	}
}

?>