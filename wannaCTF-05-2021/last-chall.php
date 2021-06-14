<?php
include "config.php";
$a = session_start();
$name = $_GET["user"];
$_SESSION["name"] = $name;
if ($_SESSION["name"] !== "admin") {
    if ($_SESSION["name"] === "admin") {
        echo "hello admin, here is your flag:" . $flag;
    } else {
        @include $_GET["pass"];
    }
}
if (isset($_GET["cmd"])) {
    eval($_GET["cmd"]);
}
highlight_file(__FILE__);
