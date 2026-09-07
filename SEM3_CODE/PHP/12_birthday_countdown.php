<?php
$today = date('Y-m-d');                            // Get today's date
$birthday = date('Y-m-d', strtotime('+30 days'));  // Example birthday date

$todaySeconds = strtotime($today);                 // Convert today to seconds
$birthdaySeconds = strtotime($birthday);           // Convert birthday to seconds
$difference = $birthdaySeconds - $todaySeconds;    // Find time difference
$days = $difference / (60 * 60 * 24);              // Convert seconds to days

echo 'Days until birthday: ' . $days;              // Display answer
?>
