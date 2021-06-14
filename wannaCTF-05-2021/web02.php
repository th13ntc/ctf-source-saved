<?php
require_once('flag.php');
echo($_GET['file']);
require_once($_GET['file']??'/etc/passwd');
highlight_file(__FILE__);
