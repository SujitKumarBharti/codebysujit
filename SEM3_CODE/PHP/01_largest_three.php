<?php
$first = 12;                         // First number
$second = 45;                        // Second number
$third = 23;                         // Third number

if ($first >= $second && $first >= $third) { // Check first number
    $largest = $first;               // First is largest
} elseif ($second >= $first && $second >= $third) { // Check second number
    $largest = $second;              // Second is largest
} else {
    $largest = $third;               // Third is largest
}

echo 'Largest number is: ' . $largest; // Display answer
?>