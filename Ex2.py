#!/bin/python3
print("Hello")
import sys
import time
import socket

def checkIp(Ip):
	try:
		if socket.inet_aton(Ip):
			return True
	except:
		return False
FILE=open('iplist.txt','r')
ReadFile=FILE.readlines()
lenght=len(ReadFile);
print("Total size of Fichier ",lenght)
for i in range(len(ReadFile)):
	time.sleep(0.002)
	perc=int( 100*( (i+1) / float(lenght)) )
	sys.stdout.write("\rProgress{}%:[{}{}]".format(perc,'#'*perc,'.'*(100-perc)))
	if checkIp(ReadFile[i]):
		SeparateIp=ReadFile[i].split('.')
		if int(SeparateIp[0])<127:
			F=open('ipA.txt','a')
			F.write(ReadFile[i])
		elif int(SeparateIp[0])<191:
			F=open('ipB.txt','a')
			F.write(ReadFile[i])
		elif int(SeparateIp[0])<223:
			F=open('ipC.txt','a')
			F.write(ReadFile[i])
		elif int(SeparateIp[0])<239:
			F=open('ipD.txt','a')
			F.write(ReadFile[i])
		elif int(SeparateIp[0])<255:
			F=open('ipE.txt','a')
			F.write(ReadFile[i])


	else:
		continue;
