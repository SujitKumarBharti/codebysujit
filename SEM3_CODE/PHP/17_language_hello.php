<?php
$language = '';                              // Store selected language
$message = '';                               // Store greeting message

if (isset($_POST['language'])) {             // Check form submitted
    $language = $_POST['language'];           // Read selected language
    switch ($language) {                     // Select greeting
        case 'english': $message = 'Hello'; break; // English greeting
        case 'hindi': $message = 'Namaste'; break; // Hindi greeting
        case 'french': $message = 'Bonjour'; break; // French greeting
    }
}
?>
<form method="post">
    <select name="language">                 <!-- Language dropdown -->
        <option value="">Choose a language</option> <!-- Default option -->
        <option value="english">English</option> <!-- English option -->
        <option value="hindi">Hindi</option> <!-- Hindi option -->
        <option value="french">French</option> <!-- French option -->
    </select>
    <button type="submit">Show message</button> <!-- Submit form -->
</form>
<?php if ($message != '') { ?>
    <p><?php echo $message; ?></p>            <!-- Display greeting -->
<?php } ?>