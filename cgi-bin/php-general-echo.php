<?php
header("Cache-Control: no-cache\n") ;
header("Content-type: text/html \n\n") ;

echo '<!DOCTYPE html>
<html><head><title>General Request Echo</title>
</head><body><h1 align="center">General Request Echo</h1>
<hr>';

echo "<p><b>HTTP Protocol:</b> ".getenv("SERVER_PROTOCOL")."</p>";
echo "<p><b>HTTP Method:</b> ".getenv("REQUEST_METHOD")."</p>";
echo "<p><b>Query String:</b> ".getenv("QUERY_STRING")."</p>";


echo "<p>Message body: </p>";

if (count($_POST) > 0) {
    foreach ($_POST as $key => $value) {
        echo htmlspecialchars($key)." = ".htmlspecialchars($value)."<br>";
    }
}
?>