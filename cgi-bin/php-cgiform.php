<?php
session_start();

if (isset($_POST["username"])) {
  $_SESSION["username"] = $_POST["username"];
  header("Location:php-sessions-1.php");
}
?>

<!doctype html>
<html>

<head>
  <title>CGI Form</title>
</head>

<body>
  <h1 align="center">Session Test</h1>
  <hr>
  <label for="cgi-lang">CGI using PHP</label>
  <form action="/cgi-bin/php-cgiform.php" method="Post" id="form">
    <label>What is your name? <input type="text" name="username" autocomplete="off"></label>
    <br>
    <input type="submit" value="Test Sessioning">
  </form>

  <a href="/" style="display:inline-block;margin-top:20px;">Home</a> 

</body>

</html>
