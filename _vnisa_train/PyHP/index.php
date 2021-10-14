<?php
define("BASE", "files/");
$kcj = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
?>

<html>
<head>
    <title>PyHP == Python + PHP :))</title>
</head>
<body>
    <a href="?src"></a><p>TẢI MỘT FILE PYTHON LÊN, CHÚNG TÔI SẼ CHẠY HỘ BẠN</p>
    <!-- bốc phét thôi chứ ko có python đâu mà chạy -->
    <hr>
    <form method="POST" action="index.php" enctype="multipart/form-data">
        <input type="file" name="file">
        <br>
        <input type="submit" name="submit" value="Send">
    </form>
</body>
</html>

<?php

if(isset($_GET['src']))
{
    highlight_file(__FILE__);
    die();
}

if(isset($_POST['submit']) && $_POST['submit'] === "Send")
{
    $file = isset($_FILES['file']) ? $_FILES['file'] : [];
    if(is_uploaded_file($file['tmp_name']))
    {
        $fileName = substr(str_shuffle($kcj), 0, 20).".py";
        $path = BASE.$fileName;
        if(file_exists($path))
            die("File exists !!!");

        if($file["size"] > 128)
            die("File is too big !!!");

        if(move_uploaded_file($file['tmp_name'], $path))
        {
            echo "Upload succeed !!!<br>";
            exec("chmod +x $path; $path");
            echo "Executed file !!!<br>";
            die();
        }
    }
    else die("Hack detected !!!");
}
?>