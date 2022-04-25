<?php
date_default_timezone_set('America/Los_Angeles');
$date = date('l jS \of F Y h:i:s A');

# IP Address is an environment variable when using CGI
$address = getenv("REMOTE_ADDR");

$message = array('title' => 'Hello, PHP!', 'heading' => 'Hello, PHP!', 'message' => 'This page was generated with the PHP programming language', 'time' => $date, 'IP' => $address);
$json = json_encode($message);
echo "$json\n";
?>