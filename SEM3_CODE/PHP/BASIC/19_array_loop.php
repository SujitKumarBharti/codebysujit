<?php
$numbers = [5, 10, 15, 20, 25];  // Create an array of numbers
$total = 0;                      // Store the running total

foreach ($numbers as $number) {  // Visit every array item
    echo $number . PHP_EOL;      // Display the current item
    $total = $total + $number;   // Add the current item
}

echo 'Array sum: ' . $total;     // Display the total
?>
