<?php
echo "Cache-Control: no-cache\n";
echo "Content-type: text/html \n\n";

echo '<!DOCTYPE html>
<html><head><title>Environment Variables</title>
</head><body><h1 align="center">Environment Variables</h1>
<hr>';

$envs = getenv();
foreach ($envs as $name => $val){
    print "<b>$name:</b> $val<br />\n";
}


echo "</body></html>";
?>