<?php
function greet($name) {                     // Define a greeting function
    $message = 'Hello, ' . $name;           // Create the greeting message
    return $message;                        // Return the message
}

$userName = readline('Enter your name: ');  // Read the user's name
$result = greet($userName);                 // Call the function
echo $result;                               // Display the returned message
?>
