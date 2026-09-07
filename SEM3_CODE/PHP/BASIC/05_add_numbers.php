<?php
$firstNumber = (float) readline('Enter first number: ');    // Read the first number
$secondNumber = (float) readline('Enter second number: ');  // Read the second number

$addition = $firstNumber + $secondNumber;                   // Add the numbers
$subtraction = $firstNumber - $secondNumber;                // Subtract the numbers
$multiplication = $firstNumber * $secondNumber;             // Multiply the numbers

echo 'Addition: ' . $addition . PHP_EOL;                    // Display the addition
echo 'Subtraction: ' . $subtraction . PHP_EOL;              // Display the subtraction
echo 'Multiplication: ' . $multiplication . PHP_EOL;        // Display the multiplication

if ($secondNumber != 0) {                                   // Check before dividing
    $division = $firstNumber / $secondNumber;               // Divide the numbers
    echo 'Division: ' . $division;                          // Display the division
} else {
    echo 'Division is not possible by zero';                // Display the error
}
?>
