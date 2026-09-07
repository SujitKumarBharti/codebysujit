<?php
function fibonacci($number) {                                // Function calls itself
    if ($number <= 1) {                                      // Stop recursion at 0 or 1
        return $number;                                      // Return current number
    }
    return fibonacci($number - 1) + fibonacci($number - 2);  // Add previous terms
}

$count = 10;                                                 // Number of terms to print
for ($number = 0; $number < $count; $number++) {             // Print each term
    echo fibonacci($number) . ' ';                           // Call recursive function
}
?>
