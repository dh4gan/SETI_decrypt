

# Written by David (Ami) Wulf 04/25/16

# I adjusted pieces of python from Dr Duncan Forgan's github to reflect
# what I knew would be a pattern at a pixel width of 359 (I had adjusted 
# my browser width to fit the 359 leading 1s in a single row, and scrolled
# down to see an alien head staring at me)

# Note that the pcolormesh takes a minute and saving the figure to a readable
# .svg format takes longer (not to mention opening it).

# I have a couple theories/thoughts about the resultant image. 
# 1) The large wave pictured and the large alien pictured are to scale and 
#    can give us the answer to question 1
# 2) There seem to be objects scattered at the feet of the large alien before
#    the picture changes to a different scale completely
# 3) The different pieces of the image should be split apart and dealt with
#    separately (3 aliens of different sizes imply at least 3 peices, as well
#    as the wierd first area that I don't see any images in)
# 4) There are some strange half-planet things (transmitting radio dishes?)
#    in there

import numpy as np
import matplotlib.pyplot as plt

# Read the message

print "Reading message bitstream"

f_obj = open('http___goo.gl_AQ78JH.txt', 'r')

rawdata = f_obj.readline()

# parse into an array

datapoints = np.array(list(rawdata),dtype=int)

# Recast array in x by y

print "Recasting bit stream into 2D array"
image3 = datapoints.reshape(359, 5299)
image4 = datapoints.reshape(5299, 359)


print "Plotting ",359, " x ", 5299, " image"
fig2 = plt.figure(2)
fig2.savefig("create_fig.png")
ax2 = fig2.add_subplot(1,10,1)
fig2.savefig("add_subplot.png")
ax2.set_title("The main image: "+str(359)+ " x "+str(5299))
ax2.pcolormesh(image4)
fig2.savefig("largebysmall_2.svg", format='svg', dpi=120)

