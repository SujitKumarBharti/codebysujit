<?php
$number = 5;                         // Number whose factorial is needed
$factorial =1;
for ($value=1;$value<=$number;$value++){
    $factorial=$factorial*$value;
}  
echo 'factorial of '. $number.' is : '. $factorial;      // Start multiplication with 1
?>