#!/usr/bin/env python
# readfile, readpar
import pylab as pl
import numpy as nm
import math, numbers

def test():
	print 'test'
	return 0
########################################
def readfile(filename):
	data=[]
	try:
		f=open(filename,'r')
		for line in f:
			line=line.strip('\n')
			line=line.split(' ')
			data+=[[int(line[0]),complex(int(line[1]),int(line[2]))]]
	except Exception as inst:
		print type(inst)
	f.close
	return data
########################################
def readpar(filename,data):
#	try:
	params=[]
	f=open(filename,'r')
	for line in f:
		line=line.rstrip('\n')
		params+=[float(line)]
	f.close
	
	for i in range(0,len(data)):
		data[i][0]=float((data[i][0]-1))*(1/float(len(data)))*(1/(float(params[0])/(float(params[1])/2)))
	return params,data
########################################
def plot(data,command):
	try:
		revsimg=command[2]
	except Exception as inst:
		revsimg=''
		
	if data=='':
		print 'dataset empty'
	else:
		time=[]
		realint=[]
		imagint=[]
		for i in range(0,len(data)):
			time+=[data[i][0]]
			realint+=[data[i][1].real]
			imagint+=[data[i][1].imag]
	if revsimg=='im':
		pl.title('Imaginary')
		pl.plot(time,imagint,'b')
	else:
		pl.title('Real')
		pl.plot(time,realint,'b')
	pl.show()
	return (0)
########################################
def help():
	print "\t The following commands are recognised:"
	print "\t \tre FILENAME"
	print "\t \trpar FILENAME"
	print "\t \twr FILENAME"
	print "\t \tprint"
	print "\t \tplot {spectrum|fid} {re|im}"
	print "\t \tb2a"
	print "\t \tapk"
	return(0)
########################################
def b2a(data,params):
	bruker_dsp_table = { #table stolen from NMR glue
    10: { #http://nmrglue.googlecode.com/svn-history/r44/trunk/nmrglue/fileio/bruker.py
        2    : 44.75,
        3    : 33.5,
        4    : 66.625,
        6    : 59.083333333333333,
        8    : 68.5625,
        12   : 60.375,
        16   : 69.53125,
        24   : 61.020833333333333,
        32   : 70.015625,
        48   : 61.34375,
        64   : 70.2578125,
        96   : 61.505208333333333,
        128  : 70.37890625,
        192  : 61.5859375,
        256  : 70.439453125,
        384  : 61.626302083333333,
        512  : 70.4697265625,
        768  : 61.646484375,
        1024 : 70.48486328125,
        1536 : 61.656575520833333,
        2048 : 70.492431640625,
        },
    11: {
        2    : 46.,
        3    : 36.5,
        4    : 48.,
        6    : 50.166666666666667,
        8    : 53.25,
        12   : 69.5,
        16   : 72.25,
        24   : 70.166666666666667,
        32   : 72.75,
        48   : 70.5,
        64   : 73.,
        96   : 70.666666666666667,
        128  : 72.5,
        192  : 71.333333333333333,
        256  : 72.25,
        384  : 71.666666666666667,
        512  : 72.125,
        768  : 71.833333333333333,
        1024 : 72.0625,
        1536 : 71.916666666666667,
        2048 : 72.03125
        },
    12: {
        2    : 46. ,
        3    : 36.5,
        4    : 48.,
        6    : 50.166666666666667,
        8    : 53.25,
        12   : 69.5,
        16   : 71.625,
        24   : 70.166666666666667,
        32   : 72.125,
        48   : 70.5,
        64   : 72.375,
        96   : 70.666666666666667,
        128  : 72.5,
        192  : 71.333333333333333,
        256  : 72.25,
        384  : 71.666666666666667,
        512  : 72.125,
        768  : 71.833333333333333,
        1024 : 72.0625,
        1536 : 71.916666666666667,
        2048 : 72.03125
        },
    13: {
        2    : 2.75, 
        3    : 2.8333333333333333,
        4    : 2.875,
        6    : 2.9166666666666667,
        8    : 2.9375,
        12   : 2.9583333333333333,
        16   : 2.96875,
        24   : 2.9791666666666667,
        32   : 2.984375,
        48   : 2.9895833333333333,
        64   : 2.9921875,
        96   : 2.9947916666666667
        } 
    }
	magic=bruker_dsp_table[params[5]]
	magickey=magic[params[4]]
	chop=int(math.floor(magickey))
	ph=[0,0]
	ph[1]=(magickey-chop)*2*math.pi

	newfid=data[chop:len(data)]	
	newfid.extend(data[0:chop])

	for i in range(0,len(data)):
		newfid[i][0]=float((i))*(1/float(len(data)))*(1/(float(params[0])/(float(params[1])/2)))

	return newfid, ph
########################################
def ft(data,params):
	fid=[]
	for i in range(0,len(data)):
		fid+=[complex(float(data[i][2]),float(data[i][1]))]
	spectrum=nm.fft.fftshift(nm.fft.fft(fid))
	offset=params[2];sw=params[0]
	freq=nm.linspace(params[2]+params[0]/2,params[2]-params[0]/2,len(spectrum))
	ftdata=[]
	for i in range(0,len(freq)):
		ftdata+=[[freq[i], spectrum[i].real, spectrum[i].imag]]
#		print freq[i], nm.real(spectrum[i]), nm.imag(spectrum[i])
	return ftdata
########################################
def apk(data,params,ph):
	
	return phased
########################################
