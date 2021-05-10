<?php

if(!isset($_GET["code"])){
    highlight_file(__FILE__);
}
else{

    if (!preg_match('/[a-z0-9~{}]/si',$_GET['code'])) {
	eval($_GET['code']);
    }
    else{
        die("hacker, go away! i will ban you for 1000 years");
    }

}
