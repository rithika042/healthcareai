<?php
// Check if the request is a POST request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the user's email and checklist status from the POST data
    $userEmail = $_POST["email"];
    $status = $_POST["status"];

    // Perform the database update
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "healthcare_db";

    // Create a database connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Update the checklist status for the user and set the 'updated_at' column to the current date and time
    $sql = "UPDATE patient_details SET checklist = ?, updated_at = NOW() WHERE email = ?";
    $stmt = $conn->prepare($sql);

    if ($stmt) {
        $stmt->bind_param("ss", $status, $userEmail);
        if ($stmt->execute()) {
            echo "Checklist updated successfully!";
        } else {
            echo "Failed to update the checklist: " . $stmt->error;
        }
        $stmt->close();
    } else {
        echo "Failed to prepare the SQL statement: " . $conn->error;
    }

    // Close the database connection
    $conn->close();
} else {
    // Handle non-POST requests (if necessary)
    echo "Invalid request method.";
}
?>
