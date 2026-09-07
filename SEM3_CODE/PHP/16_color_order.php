<?php
$colors = array('white', 'green', 'red');     // Create color array

echo 'Original order: ';                      // Print heading
foreach ($colors as $color) {                 // Read colors one by one
	echo $color . ' ';                        // Display color
}

echo '<br>Reverse order: ';                   // Print second heading
for ($index = count($colors) - 1; $index >= 0; $index--) { // Start from last item
	echo $colors[$index] . ' ';               // Display reverse color
}
?>