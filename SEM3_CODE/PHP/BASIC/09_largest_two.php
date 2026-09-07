<?php
$firstNumber = (float) readline('Enter first number: ');    // Read the first number
$secondNumber = (float) readline('Enter second number: ');  // Read the second number

if ($firstNumber >= $secondNumber) {                        // Compare both numbers
    $largest = $firstNumber;                                // Store the first number
} else {
    $largest = $secondNumber;                               // Store the second number
}

echo 'Largest number: ' . $largest;                         // Display the largest number
?>
