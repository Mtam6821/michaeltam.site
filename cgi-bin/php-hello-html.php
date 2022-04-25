<?php
echo "Cache-Control: no-cache\n";
echo "Content-type: text/html \n\n";

echo "<html>";
echo "<head>";
echo "<title>Hello, PHP!</title>";
echo "</head>";
echo "<body>";
echo "<h1>Hello, PHP!</h1>";
echo "<p>This page was generated with the PHP programming langauge</p>";

date_default_timezone_set('America/Los_Angeles');
$date = date('l jS \of F Y h:i:s A');
echo "<p>Current Time: $date </p>";

# IP Address is an environment variable when using CGI
$address = getenv('REMOTE_ADDR');
echo "<p>Your IP Address: $address</p>";

echo "</body>";
echo "</html>";
?>