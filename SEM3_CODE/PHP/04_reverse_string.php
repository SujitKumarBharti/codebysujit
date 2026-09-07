<?php
$input = '';                          // Store text entered by user
$reverse = '';                        // Store reversed text

if ($_SERVER['REQUEST_METHOD'] == 'POST') { // Check form submission
    $input = $_POST['text'];           // Read text from form
    $reverse = strrev($input);         // Reverse the text
}
?>
<form method="post">
    <label>Enter a string: <input name="text" value="<?php echo htmlspecialchars($input); ?>"></label> <!-- Text input -->
    <button type="submit">Reverse</button> <!-- Submit form -->
</form>
<?php if ($reverse != '') { ?>
    <p>Reverse: <?php echo htmlspecialchars($reverse); ?></p> <!-- Display result -->
<?php } ?>