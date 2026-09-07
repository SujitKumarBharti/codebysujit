<?php
$first_no=100;
$second_no=200;
$third_no=30;
if($first_no>=$second_no && $first_no>=$third_no){
    $largest=$first_no;
}elseif ($second_no>=$first_no && $second_no>=$third_no) {
    $largest=$second_no;
}else {
    $largest=$third_no;
}
echo 'largst no is '.$largest;
?>