<?php
$rows = 5;                                  // Number of pattern rows

for ($row = 1; $row <= $rows; $row++) {      // Run row by row
    for ($star = 1; $star <= $row; $star++) { // Print stars in each row
        echo '*';                            // Display one star
    }
    echo '<br>';                             // Move to next line
}
?>