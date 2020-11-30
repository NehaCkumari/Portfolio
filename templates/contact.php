<??php
	$name = $_POST['name'];
	$email = $_POST['email'];
	$subject = $_POST['subject'];
	$message = $_POST['message'];

	//database
	$conn = new mysqli('localhost','root','','webproject');
	if($conn->connect_error){
		die('Connection failed : ' $conn->connect_error);
			
	}else{
		$stmt = $conn->prepare("insert into registration(name,email,subject,message)
			values(?,?,?,?)");
		$stmt->bind_param("ssss",$name,$email,$subject,$message);
		$stmt->execute();
		echo "message sent!";
		$stmt->close();
		$conn->close();

	}

>