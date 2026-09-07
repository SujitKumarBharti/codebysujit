<?php
$text = 'hello php';                     // String to check
$lowerText = strtolower($text);          // Convert string to lowercase

if ($text == $lowerText) {               // Compare original and lowercase
    echo 'String is in lowercase.';      // Same means lowercase
} else {
    echo 'String is not in lowercase.';  // Different means not lowercase
}
?>
