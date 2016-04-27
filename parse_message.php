<?php
/**
 * written 27.04.2016 by Daniel Richter (thehivemind@gmail.com, @drhive)
 *
 * script to visualize the message of the SETI Decrypt Challenge
 * and split it into separate parts
 * ( https://twitter.com/DrReneHeller/status/724935476327624704 )
 *
 */

$bitStream = trim(file_get_contents("SETI_message.txt"));

$width = 359;
$height = 757;

$parts = 7;
$outDir = 'output/';

$messageImage = imagecreatetruecolor($width, $height * $parts);
$partialImage = imagecreatetruecolor($width, $height);

for ($part = 0; $part < $parts; $part++) {

    for ($y=0; $y<$height; $y++) {

        for ($x=0; $x<$width; $x++) {

            $streamOffset = ($part * $height + $y) * $width + $x;
            $bitValue = 1 & $bitStream[$streamOffset];

            imagesetpixel($messageImage, $x, $y + $part * $height, $bitValue * 0xFFFFFF);
            imagesetpixel($partialImage, $x, $y, $bitValue * 0xFFFFFF);
        }

    }
    //write each part to a separate file
    imagepng($partialImage, $outDir. 'part' . ($part + 1) . '.png');
}
//write the final image
imagepng($messageImage, $outDir. 'message.png');
