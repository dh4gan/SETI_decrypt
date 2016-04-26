# Written 26/4/16 by dh4gan
# Test script to read and manipulate SETI_decrypt message

# Message context:
# This is a call for a fun scientific challenge.
# 
# Suppose a telescope on Earth receives a series of pulses from a fixed, unresolved source beyond the solar system. 
# The source is a star about 50 light years from Earth. The pulses are in the form of short/long signals and they are received 
# in a very narrow band around an electromagnetic frequency of 452.12919 MHz. 
# A computer algorithm identifies the artificial nature of the pulses. It turns out the pulses carry a message. 
# The pulses signify binary digits. Suppose further that you were, by whatsoever reason, put in charge of decoding this message.
# 
# If you successfully encrypted the message, you should be able to answer the following questions:
# 
# 1. What is the typical body height of our interstellar counterparts?
# 2. What is their typical lifetime?
# 3. What is the scale of the devices they used to submit their message?
# 4. Since when have they been communicating interstellar?
# 5. What kind of object do they live on?
# 6. How old is their stellar system?
# 
# These are the rules.
# 
# 1. No restrictions on collaborations.
# 2. Open discussion (social networks etc.) of possible solutions strongly encouraged.
# 3. 3 hints to the solutions can be offered as per request.
# 4. Send your solutions to me via e-mail (heller@mps.mpg.de), twitter (@DrReneHeller) or facebook (DrReneHeller). 
# Human-readable format and the format of the message are allowed.
# 5. On 3 June 2016, a list of the successful SETI crackers (in chronological order) will be released.

import numpy as np
import matplotlib.pyplot as plt

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


def is_prime(n):
    if(n<2): return False
    return all(n % i for i in xrange(2, n))

# Read the message

HI_frequency = 1420.4
message_frequency = 452.12919
speed_of_light = 2.9e8
message_wavelength = speed_of_light/(message_frequency*1.0e6)

freq_ratio = HI_frequency/message_frequency

print "Message frequency ",message_frequency, " MHz"
print "Wavelength: ",message_wavelength, " m"
print "HI frequency ", HI_frequency
print "Ratio: ",freq_ratio
print "In units of pi: ", freq_ratio/np.pi


print "Reading message bitstream"

f_obj = open('SETI_message.txt', 'r')

rawdata = f_obj.readline()

# parse into an array, and record where the zeros and ones are

datapoints = np.array(list(rawdata),dtype=int)

zeropoints = np.argwhere(datapoints[:]==0)
onepoints = np.argwhere(datapoints==1)

npulses = len(datapoints)

n_ones = len(onepoints)
n_zeros = len(zeropoints)

print "There are ", npulses, " pulses "
print n_zeros, " are zeros " 
print n_ones, " are ones "

# Find prime factors of the total datastream length

prime1 = largest_prime_factor(npulses)
prime2 = npulses/prime1

print "Prime Factors of total string: ", prime1, prime2
print "Are both factors prime? ", is_prime(prime1), is_prime(prime2)

prime3 = largest_prime_factor(prime2)
prime4 = prime2/prime3
print "Two more prime factors hidden: ",prime3, prime4

# Recast array in x by y

print "Recasting bit stream into 2D array"
image1 = datapoints.reshape(prime2, prime1)
image2 = datapoints.reshape(prime1, prime2)

# Plot them

# print "Plotting first "
# fig1 = plt.figure(1)
# ax1 = fig1.add_subplot(111)
# ax1.pcolor(image1)
# 

print "Plotting ",prime2, " x ", prime1, " image"
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
ax2.set_title("The main image: "+str(prime2)+ " x "+str(prime1))
ax2.pcolor(image2)
fig2.savefig("largebysmall.png")

print "2513 x 757 image shows signs of structure"

# First N numbers are all ones, what is N?

n_firstblock = zeropoints[0]

print "First ", n_firstblock, " entries are 1"
print "Is this equal to the third prime? ", n_firstblock==prime3

ncrest = 7
nwaves = 8

wavelength_in_units = prime2/nwaves
print "Sine wave in image with ",ncrest, "wave crests"
print "If this represents the signal, then wavelength = ", wavelength_in_units, " units = ",wavelength_in_units/np.pi, " pi"

biped_height_in_pixels = 100

print "Bipedal figures in image are approximately ",biped_height_in_pixels, " pixels in height"

biped_height_in_wavelengths = np.float(biped_height_in_pixels)/np.float(wavelength_in_units)
print "in wavelengths: ", biped_height_in_wavelengths
biped_height_in_m = biped_height_in_wavelengths*message_wavelength

print "This corresponds to a physical height of ",biped_height_in_m, " metres"

# # How about every nth element?
# 
# print "selecting every ",prime3, "th element"
# select_by_prime = datapoints[0::prime3]
# 
# nrows = largest_prime_factor(select_by_prime.shape[0])
# ncolumns = select_by_prime.shape[0]/largest_prime_factor(select_by_prime.shape[0])
# 
# print nrows,ncolumns
# 
# image3 = select_by_prime.reshape(ncolumns,nrows)
# image4 = select_by_prime.reshape(nrows,ncolumns)
# 
# fig1 = plt.figure(3)
# ax1 = fig1.add_subplot(111)
# ax1.pcolor(image3)
# 
# 
# fig2 = plt.figure(4)
# ax2 = fig2.add_subplot(111)
# ax2.pcolor(image4)
# 
# print "Showing images"
# plt.show()

# Now do selection of image

subset = image2[0:prime3,0:prime4]

fig2 = plt.figure(4)
ax2 = fig2.add_subplot(111)

ax2.set_title("A subset of the main image: "+str(prime3)+ " x "+str(prime4)+ ": numbers?")
ax2.pcolor(subset)
fig2.savefig("subset.png", format='png')

# Image looks like a set of numbers represented as 




