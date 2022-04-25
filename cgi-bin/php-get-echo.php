
<?php
echo "Cache-Control: no-cache\n";
echo "Content-type: text/html \n\n";

echo '<!DOCTYPE html>
<html><head><title>GET Request Echo</title>
</head><body><h1 align="center">Get Request Echo</h1>
<hr>';

$query_str = getenv('QUERY_STRING');

echo "<b>Query String:</b> $query_str<br />\n"; 

if (strlen($query_str) > 0) {
    $pairs = preg_split("/&/", $query_str);
    foreach ($pairs as $pair) {
        $kvpair = preg_split("/=/", $pair);
        list($key, $val) = $kvpair;
        echo "$key = $vale<br/>\n";
    }
}
echo "</body></html>";
?>