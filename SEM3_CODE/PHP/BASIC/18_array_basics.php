<?php
$numbers = [10, 20, 30];                      // Create an array of numbers
echo 'Original array: ';                      // Display a label
print_r($numbers);                            // Display the array

$numbers[] = 40;                              // Add an item to the array
echo 'After adding 40: ';                     // Display a label
print_r($numbers);                            // Display the updated array

unset($numbers[1]);                           // Remove the item at index one
echo 'After removing index one: ';            // Display a label
print_r($numbers);                            // Display the updated array

echo 'First item: ' . $numbers[0] . PHP_EOL;  // Display the first item
echo 'Array length: ' . count($numbers);      // Display the number of items
?>
