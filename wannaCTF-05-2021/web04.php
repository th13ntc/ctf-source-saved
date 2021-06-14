<?php
$file = $_GET['f'];
if (isset($file)) {
    if (file_exists($file)) {
        echo "f*** off ..........";
    } else {
        include $file;
    }
} else {
    highlight_file(__FILE__);
}
