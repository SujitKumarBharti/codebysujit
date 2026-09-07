<?php
$number = (int) readline('Enter a number: ');                        // Read the table number

for ($multiplier = 1; $multiplier <= 10; $multiplier++) {            // Generate multipliers
    $result = $number * $multiplier;                                 // Calculate the table value
    echo $number . ' x ' . $multiplier . ' = ' . $result . PHP_EOL;  // Display the table line
}
?>
