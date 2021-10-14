<?php
define('BASE', "icons/");

class weapon
{
	private $fileIcon;

	function __construct()
	{
		$this->fileIcon = BASE . "default.png";
	}

	public function GetIcon()
	{
		return file_get_contents($this->fileIcon);
	}

	public function GetMaxDamage()
	{
		return 50;
	}
}

?>