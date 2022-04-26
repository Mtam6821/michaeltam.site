<?php

session_start();
session_destroy();

print "<html>";
print "<head>";
print "<title>Perl Session Destroyed</title>";
print "</head>";
print "<body>";
print "<h1>Session Destroyed</h1>";
print "<a href=\"/perl-cgiform.html\">Back to the Perl CGI Form</a><br />";
print "<a href=\"/cgi-bin/perl-sessions-1.pl\">Back to Page 1</a><br />";
print "<a href=\"/cgi-bin/perl-sessions-2.pl\">Back to Page 2</a>";
print "</body>";
print "</html>";

?>
