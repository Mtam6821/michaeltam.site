
<?php

echo '<!DOCTYPE html>
<html><head><title>POST Request Echo</title>
</head><body><h1 align="center">Get Request Echo</h1>
<hr>';
echo "Message body: ";
if (count($_POST) > 0) {
    foreach ($_POST as $key => $value) {
        echo htmlspecialchars($key)." = ".htmlspecialchars($value)."<br>";
    }
}


echo "</body></html>";
?>