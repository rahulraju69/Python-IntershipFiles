'''
it is a python file which contains func
pre-defined func:
os,sys,math,collection,rand
os: mkdir-create a file
chdir-to go to a particular file
getcwd-current working dir
rmdir-remove the dir
listdir-to see the list of files & folder in current folder
'''
import os
#os.mkdir("c://Demofolder1")
#print("file created succesfully")
os.chdir("c://Demofolder1") #chmd
print("Current Working folder:",os.getcwd()) #getcwd
print("files and folder:",os.listdir("c://Demofolder1")) #listdir
print("remove dir:",os.rmdir("c://Demofolder1"))


