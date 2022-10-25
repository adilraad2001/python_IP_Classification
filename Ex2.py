#!/bin/python3
print("Hello")
import sys 
import time
import socket
#Fonction pour tester la chaine de caractere si ipv4 or not
def checkIp(Ip):
	try:
		if socket.inet_aton(Ip):#en cas de l'adresse ip valid return 1
			return True
	except:
		return False #en cas de l'adresse ip non-valid return 0
FILE=open('iplist.txt','r') #pour l'ouverture de la fichie que nommee iplist en mode de read
ReadFile=FILE.readlines()#read the file comme un list de line
lenght=len(ReadFile);#calculer le nombre de valeur de cette fichie
print("Total size of Fichier ",lenght)
for i in range(len(ReadFile)):
	time.sleep(0.002)#timer pour visualisez le progress bar parce que en cas normal la progress bar va terminer immediatement
	perc=int( 100*( (i+1) / float(lenght)) ) #calculer le pourcentage de chaque repetition de loop
	sys.stdout.write("\rProgress{}%:[{}{}]".format(perc,'#'*perc,'.'*(100-perc))) #affichage de progresse bar sans repitition 100%
	if checkIp(ReadFile[i]): #check if the line is ip adresse or oter things
		SeparateIp=ReadFile[i].split('.')#Split the line until any '.' and make it in new list
		if int(SeparateIp[0])<127:#check the first numbers of each line to find out which class the Ip Adresse belongs to
			F=open('ipA.txt','a')#open new file named ipA en mode de append
			F.write(ReadFile[i])#append the full line after check it is belong to class A or not
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


	else:#if the line isn't ip adress will skip it
		continue;
