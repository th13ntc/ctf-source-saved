<?php
chdir("/");
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    echo substr_count($cmd, '.') . '</br>';
    echo strlen($cmd) . '</br>';
    if (preg_match("/[3-9`~!@#\$%^&*\-=+,;?'\"\[\]\{\}\\\\]|0|pcntl|highlight_file|var|root|func|contents|eval|count|cmp/i", $cmd) || substr_count($cmd, '.') > 2 || strlen($cmd) > 64) {
        die("ấu nâu !");
    } else {
        echo $cmd . '</br>';
        eval($cmd . ";");
    }
    highlight_file(__FILE__);
} else {
}
