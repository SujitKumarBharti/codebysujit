<?php
$text = readline('Enter a string: ');                      // Read the string
$reverseText = '';                                         // Store the reversed string

for ($index = strlen($text) - 1; $index >= 0; $index--) {  // Read from the last character
    $reverseText = $reverseText . $text[$index];           // Add the current character
}

echo 'Reverse: ' . $reverseText;                           // Display the reversed string
?>
