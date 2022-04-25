
<?php
echo "Cache-Control: no-cache\n";
echo "Content-type: text/html \n\n";

echo '<!DOCTYPE html>
<html><head><title>GET Request Echo</title>
</head><body><h1 align="center">Get Request Echo</h1>
<hr>';
echo "Message body: ";
if (count($_POST) > 0) {
    foreach ($_POST as $key => $value) {
        echo htmlspecialchars($key)." is ".htmlspecialchars($value)."<br>";
    }
}


echo "</body></html>";
?>