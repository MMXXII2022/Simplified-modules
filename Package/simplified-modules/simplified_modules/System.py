from sys import exit
from os import system
from time import sleep

def stopScript():
    exit()

def clrScreen():
    system('cls')

def wait(secs:float):
    sleep(secs)

wait(3)
print ("i")