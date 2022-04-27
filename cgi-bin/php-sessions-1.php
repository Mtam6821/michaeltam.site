<?php
header("Cache-Control: no-cache\n") ;
header("Content-type: text/html \n\n") ;

$name = "";
if ($_POST["username"] != "" && $_POST["username"] != "destroyed") {
    $name = $_POST["username"];
    header("Set-Cookie: $name\n\n");
}
else if ($_COOKIE["username"] != "" && $_COOKIE["username"] != "destroyed") {
    $name = $_COOKIE["username"];
}
else {
    $name = "No name set";
}


echo "<html>";
echo "<head>";
echo "<title>PHP Sessions</title>";
echo "</head>";
echo "<body>";

echo "<h1>PHP Sessions Page 1</h1>";

echo "<p><b>Name:</b> $name";

echo "<br/><br/>";
echo "<a href=\"/cgi-bin/php-sessions-2.php\">Session Page 2</a><br/>";
echo "<a href=\"/cgi-bin/php-cgiform.php\">PHP CGI Form</a><br />";
echo "<form style=\"margin-top:30px\" action=\"/cgi-bin/php-destroy-session.php\" method=\"get\">";
echo "<button type=\"submit\">Destroy Session</button>";
echo "</form>";

echo "</body>";
echo "</html>";
?>