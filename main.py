#!/usr/bin/env python
#
# read fid -- cheat use octal dump, cpio (linux only)
# get parameters -- could use python
# window function
# plot
# 

import functions


command=[' ']
data=[]
nmrdict={}

while (command[0]!='exit') and (command[0]!='quit'):

	if command[0]=='re': #read
		try:
			data=functions.readfile(command[1])
			nmrdict['fid']=data

		except Exception as inst:
			print "File missing"
			print type(inst)

	elif command[0]=='rpar': #get params
		try:
			(params,data)=functions.readpar(command[1],nmrdict['fid'])
		except Exception as inst:
			print type(inst)
		else:
			nmrdict['fid']=data
			nmrdict['params']=params
			
	elif command[0]=='wr': #write
		i=0
	
	elif command[0]=='ft':
		data=functions.ft(nmrdict['fid'],params)
		nmrdict['spectrum']=data
		
	elif command[0]=='apk': #phase
		i=0

	elif command[0]=='absd': #baseline
		i=0

	elif command[0]=='clear': #reset all
		i=0 

	elif command[0]=='plot':
		try:
			todo=command[1]
		except:
			print "Specify plot: spectrum or fid"

#		try:
		if 'spectrum' in command[1]:
			functions.plot(nmrdict['spectrum'],command)
		elif 'fid' in command[1]:
			functions.plot(nmrdict['fid'],command)
		
#		except Exception as inst:
#			print type(inst)
		
	elif command[0]=='print':
		print nmrdict.keys()
		
	elif command[0]=='ft': # fourier transform
		i=0
	elif command[0]=='help': #help
		functions.help()

	elif command[0]=='b2a':
		if not 'bruk2ana' in nmrdict:
			try:
				(data,phase)=functions.b2a(nmrdict['fid'],params) #bruker digital to analogue
				nmrdict['fid']=data
				nmrdict['phase']=phase
				nmrdict['bruk2ana']=True
			except Exception as inst:
				print type(inst)
		else:
			print 'You have already converted this data'
			
	elif command!=[' ']:
		print "Command ",command," not recognised"

	command=raw_input('shellnmr $ ')
	command=command.split(' ')
