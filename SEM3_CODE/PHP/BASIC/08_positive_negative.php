<?php
$number = (float) readline('Enter a number: ');  // Read the number

if ($number > 0) {                               // Check for a positive number
    echo 'Positive number';                      // Display positive result
} elseif ($number < 0) {                         // Check for a negative number
    echo 'Negative number';                      // Display negative result
} else {
    echo 'Zero';                                 // Display zero result
}
?>
