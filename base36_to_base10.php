<?php

function base36_to_base10($input){

    $output = 0;
    $len = strlen($input);

    for( $i=$len-1; $i>=0; $i-- ){

        $val = ord($input[$i]);

	if( $val>=48 && $val<=57 )
            $val -= 48;
	else if( $val>=97 && $val<=122 )
            $val -= 87;
	else
            exit("There is invalid character!");

	$output += $val*pow(36,$len-$i-1);

    }

    return $output;

}

echo base36_to_base10("614qa");
echo "\n";
echo base36_to_base10("614z1");
