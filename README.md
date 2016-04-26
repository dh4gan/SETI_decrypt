**SETI Decrypt**

This repository stores my attempts to decode @DrReneHeller 's SETI-Decrypt Challenge.

The repo contains a copy of the message (`SETI_message.txt`) and some Python code to read and
parse the bitstream.  Feel free to join in!

Things we've learned so far:

Message frequency  452.12919  MHz = 1420.4/pi MHz (1420.4 is the classic "Water Hole" 21cm atomic hydrogen line)
(Wavelength:  64.1409593572  cm)

There are  1902341  pulses (bits) in the signal (2513 x 757 = 2513 x 359 x7)

1479538  are zeros 
422803  are ones 

First  359  entries are 1
Rearranging into a 2513 x 757 image shows signs of structure

Sine wave in image with  7 wave crests
If this represents the signal, then wavelength =  314  units =  99.9493042617  pi
Bipedal figures in image are approximately  100  pixels in height
in wavelengths:  0.31847133758
This corresponds to a physical height of  20.4270571201  cm!


A subset of the image (7x359) contains what may be a set of representations of numbers...