<?php
if(!isset($_GET['cmd'])){
	highlight_file(__FILE__);
}
else{
	$_GET['cmd']=addslashes($_GET['cmd']);
	if(preg_match("/cat|ls|head|\'|\"|less| |nl|echo|more|tail|grep|dir|tac|\>|\<|\=|\*|\&|\,|\`|\@/is",$_GET['cmd'])){
		die("bad linux user");
	}
	else{
		echo shell_exec($_GET['cmd']);
	}
}
