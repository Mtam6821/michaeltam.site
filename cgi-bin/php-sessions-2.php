<?php

$name = "";
if (isset($_SESSION["name"])) {
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
echo "<a href=\"/cgi-bin/php-sessions-1.pl\">Session Page 1</a><br/>";
echo "<a href=\"/cgi-bin/php-cgiform.php\">PHP CGI Form</a><br />";
echo "<form style=\"margin-top:30px\" action=\"/cgi-bin/php-destroy-session.pl\" method=\"get\">";
echo "<button type=\"submit\">Destroy Session</button>";
echo "</form>";

echo "</body>";
echo "</html>";
?>