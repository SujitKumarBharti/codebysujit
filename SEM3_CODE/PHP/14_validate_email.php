<?php
$email = 'student@example.com';                           // Email to check
$validEmail = filter_var($email, FILTER_VALIDATE_EMAIL);  // Validate email

if ($validEmail) {                                        // Check validation result
    echo 'Valid email address.';                          // Email is correct
} else {
    echo 'Invalid email address.';                        // Email is incorrect
}
?>
