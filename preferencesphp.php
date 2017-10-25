<?php

if (isset($POST['font_size'],
$_POST['font_color'])) {

setcookie('sizes', $_POST['sizes']);
setcookie('color', $_POST['color']);


$msg = '<p> Your settings have been entered. Now see them <a href="#"> in action </a> </p>';
}
?>