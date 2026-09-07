<?php
$limit = (int) readline('Enter the last number: ');  // Read the last number
$total = 0;                                          // Store the running total

for ($number = 1; $number <= $limit; $number++) {    // Visit numbers up to limit
    $total = $total + $number;                       // Add the current number
}

echo 'Sum: ' . $total;                               // Display the total
?>
