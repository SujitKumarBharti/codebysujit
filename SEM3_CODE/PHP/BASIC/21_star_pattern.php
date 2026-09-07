<?php
$size = (int) readline('Enter a size: ');          // Read the number of lines

for ($line = 1; $line <= $size; $line++) {         // Create each pattern line
    $stars = '';                                   // Start with an empty line
    for ($count = 1; $count <= $line; $count++) {  // Add stars one by one
        $stars = $stars . '*';                     // Add one star
    }
    echo $stars . PHP_EOL;                         // Display the pattern line
}
?>
