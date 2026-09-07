<?php
$number = 5;                                // How many odd numbers to add
$sum = 0;                                   // Store total sum

for ($value = 1; $value <= ($number * 2); $value += 2) { // Get odd numbers
    $sum = $sum + $value;                    // Add odd number to sum
}

echo 'Sum = ' . $sum;                       // Display answer
?>