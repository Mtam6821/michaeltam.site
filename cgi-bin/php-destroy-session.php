<?php

header("Cache-Control: no-cache\n") ;
header("Content-type: text/html \n\n") ;
header("Set-Cookie: username=destroyed\n");


print "<html>";
print "<head>";
print "<title>PHP Session Destroyed</title>";
print "</head>";
print "<body>";
print "<h1>Session Destroyed</h1>";
print "<a href=\"/php-cgiform.html\">Back to the Perl CGI Form</a><br />";
print "<a href=\"/cgi-bin/php-sessions-1.php\">Back to Page 1</a><br />";
print "<a href=\"/cgi-bin/php-sessions-2.php\">Back to Page 2</a>";
print "</body>";
print "</html>";

?>
