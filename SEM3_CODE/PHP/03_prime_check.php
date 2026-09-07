<?php
$number = 29;                         // Number to check
$isPrime = true;                       // Initially assume it is prime

if ($number < 2) {                     // Numbers below 2 are not prime
    $isPrime = false;                  // Mark number as not prime
}

for ($divisor = 2; $divisor < $number; $divisor++) { // Try every divisor
    if ($number % $divisor == 0) {     // Remainder 0 means exactly divisible
        $isPrime = false;              // Mark number as not prime
        break;                         // Stop checking
    }
}

if ($isPrime == true) {                // Check final result
    echo $number . ' is a prime number.'; // Display prime message
} else {
    echo $number . ' is not a prime number.'; // Display non-prime message
}
?>