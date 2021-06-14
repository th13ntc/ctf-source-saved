<?php
if(isset($_GET['code'])){
    $code = $_GET['code'];
    $code = str_replace("\\","\\\\",$code);
    $code =preg_replace('/"|\'|\$|\@/', "", $code);
    echo strlen($code);
    if (strlen($code)<20){
        if(preg_match("/cat|find|base|printf|tac|awk|strings|sort|txt|ls|nl|head|less|more|tail|grep|dir/is",$code)){
            die("awwww, how bad you are?");
            
        }
        else{
            system("ping -c 1 ".$code);
        }
    }
    else{
        die("no, you are chicken!!!");
    }
}
else{
    highlight_file(__FILE__);
}
