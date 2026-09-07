<?php
$text = readline('Enter a string: ');                      // Read the string
$reverseText = '';                                         // Store the reversed string

for ($index = strlen($text) - 1; $index >= 0; $index--) {  // Read from the last character
    $reverseText = $reverseText . $text[$index];           // Add the current character
}

if ($text == $reverseText) {                               // Compare original and reversed strings
    echo 'Palindrome';                                     // Display palindrome result
} else {
    echo 'Not a palindrome';                               // Display non-palindrome result
}
?>
