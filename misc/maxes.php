#!/usr/bin/php

<?php
	include('array.php');

	function getMaxes($arr) {
		// Sort array from highest to lowest.
		rsort($arr,SORT_NUMERIC);

		// Check if theres duplicates at the top of the array.
		// (There still may be more dupes in the array, but we've got what we need.)
		while($arr[0] == $arr[1]) {
			// get rid of them.
			array_shift($arr);
		}

		print $arr[0]." + ".$arr[1]."\n";	
		return $arr[0]+$arr[1];
	}	
	
	print	getMaxes($array)."\n";
?>
