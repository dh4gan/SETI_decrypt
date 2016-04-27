**SETI Decrypt**

This repository stores my attempts to decode @DrReneHeller 's SETI-Decrypt Challenge.

The repo contains a copy of the message (`SETI_message.txt`) and some Python code to read and
parse the bitstream.  Feel free to join in!

Things we've learned so far:

Message frequency  452.12919 MHz = 1420.4/pi MHz (1420.4 is the classic "Water Hole" 21 cm atomic hydrogen line)
(Wavelength:  64.1409593572  cm)

There are  1902341  pulses (bits) in the signal (7 * 359 * 2513)

Rearranging into a 359 px by 5299 px image shows a promising structure.
The image can be further subdivided into parts of 359 px * 757 px in size.

Attempts on interpreting the parts:

Part 1
 - calibration frame

Part 2
 - the first natural numbers (little-endian binary)

Part 3
- the first 757 natural prime numbers (little-endian binary)

Part 4
- one sine wave period (-pi <= x <= pi)

Part 5
- rendering of alien life form

Part 6
- transmitter array?

Part 7
- planetary system
- life form inhabits the 4th planet (Earth analog)
- 3rd planet gas giant
- inner 2 might be akin to Venus or Mercury


Assuming that - as indicated by the 4th part - one wave length corresponds to the width of the picture,
and the height of the bipedal figure corresponds to the height of a single part, allows us to calculate
the physical height of the pictured specimen as:

height = 64.1409593572 cm * 757 px / 359 px = 135.2498780874 cm

We might base the calculation on slightly different values, such as a height of 755 px or a width of 360 px, but it
would be safe to say that the message indicates a (typical) height of the alien life forms of around 135 cm.
