#!/usr/bin/php

<?php
	$MAX_ARRAY_SIZE = 10000;
	$array = [];

	function print_array($array) {
		print "<?php\n";
		print "\$array = [";
		for($c=0;$c<sizeof($array);$c++) {
			print $array[$c];
			if($c < sizeof($array)-1) {
				print ",";
			}
		}
		print "];\n ?>\n";
	}

	list($usec,$sec) = explode(' ',microtime());
	$seed = (float) $sec + ((float) $usec * 10000);
	mt_srand($seed);
	
	for($i=0;$i<$MAX_ARRAY_SIZE;$i++) {
		array_push($array,mt_rand(-1668*($MAX_ARRAY_SIZE/2),2048*$MAX_ARRAY_SIZE));
	}
	print_array($array);
?>
