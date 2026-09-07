<?php
$firstNumber = (float) readline('Enter first number: ');    // Read the first number
$operator = readline('Enter operator (+, -, *, /): ');      // Read the operator
$secondNumber = (float) readline('Enter second number: ');  // Read the second number

if ($operator == '+') {                                     // Check for addition
    $result = $firstNumber + $secondNumber;                 // Add the numbers
} elseif ($operator == '-') {                               // Check for subtraction
    $result = $firstNumber - $secondNumber;                 // Subtract the numbers
} elseif ($operator == '*') {                               // Check for multiplication
    $result = $firstNumber * $secondNumber;                 // Multiply the numbers
} elseif ($operator == '/' && $secondNumber != 0) {         // Check for valid division
    $result = $firstNumber / $secondNumber;                 // Divide the numbers
} else {
    $result = 'Invalid operation';                          // Store an error message
}

echo 'Result: ' . $result;                                  // Display the result
?>
