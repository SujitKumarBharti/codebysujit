<?php
$number = 5;                         // Number whose factorial is needed
$factorial = 1;                       // Start multiplication with 1

for ($value = 1; $value <= $number; $value++) { // Run from 1 to number
    $factorial = $factorial * $value; // Multiply every value
}

echo $number . '! = ' . $factorial;   // Display factorial
?>