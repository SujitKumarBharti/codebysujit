<?php
$database = new PDO('sqlite::memory:');                                                                    // Create temporary database
$database->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);                                        // Show errors
$database->exec('CREATE TABLE users (username TEXT, password TEXT)');                                      // Create table

$query = $database->prepare('INSERT INTO users VALUES (?, ?)');                                            // Prepare insert
$query->execute(array('sujit', 'php123'));                                                                 // Add first registered user
$query->execute(array('admin', 'admin123'));                                                               // Add second registered user

$message = '';                                                                                             // Store login result
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] == 'POST') {                           // Check form submitted
    $username = $_POST['username'];                                                                        // Read username
    $password = $_POST['password'];                                                                        // Read password

    $query = $database->prepare('SELECT * FROM users WHERE username = ? AND password = ?');                // Search user
    $query->execute(array($username, $password));                                                          // Run search query
    $user = $query->fetch();                                                                               // Get matching user

    if ($user) {                                                                                           // User found
        $message = 'Welcome, ' . htmlspecialchars($username) . '!';                                        // Success
    } else {
        $message = 'Wrong username or password.';                                                          // Failure
    }
}
?>
<form method="post">
    <label>Username: <input name="username" required></label><br> <!-- Username input -->
    <label>Password: <input type="password" name="password" required></label><br> <!-- Password input -->
    <button type="submit">Login</button> <!-- Submit login form -->
</form>
<?php if ($message != '') { ?>
    <p><?php echo $message; ?></p> <!-- Display login result -->
<?php } ?>
