<?php
if (isset($_GET["url"])) {
    $url = $_GET["url"];
    $parse = parse_url($url);

    if (isset($parse["scheme"]) && !in_array($parse["scheme"], array("file", "gopher"))) {
        if (!isset($parse["port"]) || $parse["port"] != 9000) {
            $path = urldecode(isset($parse["path"])?$parse["path"]:"");
            if (!preg_match("/flag/i", $path)) {
                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, $url);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($ch, CURLOPT_HEADER, false);
                $output = curl_exec($ch);
                curl_close($ch);
                die($output);
            }
        }
    }
    die("dont hack :)");
}
?>
<a href ="?url=https://pastebin.com/raw/jEwTz1cP">Curl flag</a>