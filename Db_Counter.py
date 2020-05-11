
# =============================================================================
# Created By  : Rahul Kashyap
# Created Date: Monday May 11 2020
# =============================================================================
"""Python Script for Calculating Audio decibels"""
# =============================================================================
# Imports
# =============================================================================
import pyaudio
import numpy as np
import numpy


CHUNK = 4096
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

def dbCounter():
	
	for i in range(int(RATE)): 
		data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
		peakSound=np.average(np.abs(data))*2
		decibel = int(20*numpy.log10(peakSound))
		print(str(decibel) + " Db")
		
pass

dbCounter()