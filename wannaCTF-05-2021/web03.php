<?php
include "flag.php";
//round 1
if (isset($_GET['1']) & isset($_GET['2'])) {
    if ($_GET['1'] !== $_GET['2'] && $_GET['1'] == $_GET['2']) {
        echo "pass round1";
        //round 2
        if (isset($_GET['3']) & isset($_GET['4'])) {
            if ($_GET['3'] !== $_GET['4'] && md5($_GET['1']) == md5($_GET['2'])) {
                echo "pass round2";
                if (isset($_GET['5']) & isset($_GET['6'])) {
                    if ($_GET['5'] !== $_GET['6'] && sha1($_GET['5']) === sha1($_GET['6'])) {
                        echo "echo flag:" . $flag;
                    }
                }
            }
        }
    }
} else {
    highlight_file(__FILE__);
}
