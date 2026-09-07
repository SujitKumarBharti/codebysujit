<?php
$number = (int) readline('Enter a number: ');              // Read the number
$factorial = 1;                                            // Store the factorial result

if ($number < 0) {                                         // Check for a negative number
    echo 'Factorial is not defined for negative numbers';  // Display the error
} else {
    for ($value = 1; $value <= $number; $value++) {        // Visit values up to number
        $factorial = $factorial * $value;                  // Multiply the current value
    }
    echo 'Factorial: ' . $factorial;                       // Display the factorial
}
?>
