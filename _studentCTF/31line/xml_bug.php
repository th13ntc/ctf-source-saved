<?php
$dom = new \DOMDocument();
$dom
    ->appendChild($dom->createElementNS('some:namespace', 'foo'))
    ->appendChild($dom->createElement('bar'));
echo ($xml = $dom->saveXML());

$xpath = new \DOMXPath($dom);
$xpath->registerNamespace('n', 'some:namespace');
echo count($xpath->query('/n:foo/bar')) . " should be 0\n";
echo count($xpath->query('/n:foo/n:bar')) . " should be 1\n\n";

//

$dom = new \DOMDocument();
$dom->loadXml($xml);
echo ($xml = $dom->saveXML());

$xpath = new \DOMXPath($dom);
$xpath->registerNamespace('n', 'some:namespace');
echo count($xpath->query('/n:foo/bar')) . " should be 0\n";
echo count($xpath->query('/n:foo/n:bar')) . " should be 1\n\n";
