<?php
$number = (int) readline('Enter a number: ');             // Read the number
$isPrime = true;                                          // Assume the number is prime

if ($number < 2) {                                        // Check numbers smaller than two
    $isPrime = false;                                     // Mark the number as not prime
} else {
    for ($divisor = 2; $divisor < $number; $divisor++) {  // Try possible divisors
        if ($number % $divisor == 0) {                    // Check exact divisibility
            $isPrime = false;                             // Mark the number as not prime
            break;                                        // Stop after finding a divisor
        }
    }
}

if ($isPrime) {                                           // Check the final result
    echo 'Prime number';                                  // Display prime result
} else {
    echo 'Not a prime number';                            // Display non-prime result
}
?>
