<?php
$text = 'madam';                     // Word to check
$reverseText = strrev($text);        // Reverse the word

if ($text == $reverseText) {         // Compare word and reverse
    echo 'It is a palindrome.';      // Same from both sides
} else {
    echo 'It is not a palindrome.';  // Different from both sides
}
?>
