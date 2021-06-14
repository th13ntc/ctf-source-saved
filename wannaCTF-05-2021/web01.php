<?php
#include "config.php";
class User
{
    private $name;
    private $is_admin = false;

    public function __construct($name)
    {
        $this->name = $name;
    }
    public function __destruct()
    {
        if ($this->is_admin === true) {
            echo "hi admin, here is your flag";
        }
    }
}
class Show_color
{
    public $color;
    public $type;
    public function __construct($type, $color)
    {
        $this->type = $type;
        $this->color = $color;
    }
    public function __destruct()
    {
        call_user_func($this->type->adu, $this->color);
    }
}
class do_nothing
{
    public $why;
    public $i_use_this;
    public function __construct($a, $b)
    {
        $this->why = $a;
        $this->i_use_this = $b;
    }
    public function __get($method)
    {
        if (isset($this->why)) {
            return $this->i_use_this;
        }
        return $method;
    }
}
if (isset($_GET['code'])) {
    unserialize($_GET['code']);
} else {
    highlight_file(__FILE__);
}
