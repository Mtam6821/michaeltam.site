<?php
session_start();
$name = "";
if (isset($POST["username"])) {
    $name = $_SESSION["name"];
}
else {
    $name = "No name set";
}


echo "<html>";
echo "<head>";
echo "<title>Perl Sessions</title>";
echo "</head>";
echo "<body>";

echo "<h1>Perl Sessions Page 2</h1>";

echo "<p><b>Name:</b> $name";

echo "<br/><br/>";
echo "<a href=\"/cgi-bin/php-sessions-1.php\">Session Page 1</a><br/>";
echo "<a href=\"/cgi-bin/php-cgiform.php\">PHP CGI Form</a><br />";
echo "<form style=\"margin-top:30px\" action=\"/cgi-bin/php-destroy-session.php\" method=\"get\">";
echo "<button type=\"submit\">Destroy Session</button>";
echo "</form>";

echo "</body>";
echo "</html>";
?>