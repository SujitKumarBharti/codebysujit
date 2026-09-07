<?php
$sentence = 'the quick brown fox jumps over the lazy dog'; // Original sentence
$newSentence = preg_replace('/^the/', 'That', $sentence, 1); // Replace first "the"

echo $newSentence;                              // Display changed sentence
?>