<?php
$text = 'Learning PHP is useful';             // Main string
$search = 'PHP';                              // Text to find

if (strpos($text, $search) !== false) {       // Check text position
	echo 'String found.';                      // Search text exists
} else {
	echo 'String not found.';                 // Search text does not exist
}
?>