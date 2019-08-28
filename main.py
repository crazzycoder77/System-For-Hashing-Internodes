# -*- coding: utf-8 -*-
"""
Software named Realative Adaptor for Hashing Intermotes 
famously known as RASHI used to calculate optimum number of gateways required 
to connect a System of IOT Devices
@name RASHIv1.1
@version 1.1
@author Praveen Mishra 
@institue Kalyani Goverment Engineering College IT Depatment
"""
import csv
import pandas as pd

MOTES_FILE = "graph.csv"
GATEWAYS_FILE = "gateway.csv"


class Mote(object):
    
    def __init__(self, mid, x, y, z, mrange, mtype):
        self.id = mid
        self.x = x
        self.y = y
        self.z = z
        self.range = mrange
        self.type = mtype
    
    def dist(self, other):
        a = self.x - other.x
        b = self.y - other.y
        c = self.z - other.z
        return ((a**2 + b**2 + c**2)**0.5)
    
    def __eq__(self, other):
        return (self.type == other.type and self.dist(other) < (self.range + other.range))



class Gateway(object):
    def __init__(self, gid, grange, gfrom , gto):
        self.id = gid
        self.range = grange
        self.start = gfrom
        self.end = gto    
    def __eq__(self, other):
        return (self.start == other.start and self.end == other.end)
        
class Edge(object):
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start= start
        self.end = end
    def __lt__(self, other):
        return (self.weight < other.weight)

def graph(flag):
     motes=[]
     while True:
         mid =           input("Enter id of the mote              : ").strip()
         x =       float(input("Enter x coordinate of the mote    : "))
         y =       float(input("Enter y coordinate of the mote    : "))
         z =       float(input("Enter z coordinate of the mote    : "))
         mrange =  float(input("Enter range of the mote           : "))
         mtype =         input("Enter type of the mote            : ").strip()
         data = [mid, x, y, z, mrange, mtype]
         motes.append(data)
         ch = input("Do you Want to add more motes(Y/N)? ")
         if ch == "N" or ch == "n":
             break
     if not flag:
         myFile = open(MOTES_FILE, 'w', newline='')
     else:
         myFile = open(MOTES_FILE, 'a', newline='')
     writer = csv.writer(myFile)
     with myFile:
        writer.writerows(motes)
         
     print("\n\nWriting complete...\n")
    
def gateways(flag):
     motes=[]
     while True:
         mid =           input("Enter id of the gateway           : ").strip()
         mrange =  float(input("Enter range of the gateway        : "))
         mfrom =         input("Enter type motes supported        : ").strip()
         mto =           input("Enter another mote type supported : ").strip()
         data = [mid, mrange, mfrom, mto]
         motes.append(data)
         ch = input("Want to add more gateways (Y/N)?  :")
         if ch == "N" or ch == "n":
             break
     if not flag:
         myFile = open(GATEWAYS_FILE, 'w', newline='')
     else:
         myFile = open(GATEWAYS_FILE, 'a', newline='')
     writer = csv.writer(myFile)
     with myFile:
        writer.writerows(motes)
         
     print("\n\nWriting complete...\n")
    
def optimal():
    loc = input("Enter Location Where File Is Be Saved : ").strip()
    motes=[]
    gateways=[]
    with open(MOTES_FILE,  newline='') as file:
        reader = csv.reader(file)
        motes = list(map(tuple, reader))
        print(motes)
    

def main():
    while True:
        print("\n\n\n\n0. To Exit Console")
        print("1. To make new graph of motes.")
        print("2. To make new set of gateways.")
        print("3. To append in graph of motes.")
        print("4. To append in set of gateways.")
        print("5. To Calculate required number of gateways with exact location.")
        choice = int(input("Please Enter Your Choice...       : "))
        if choice == 0:
            break;
        elif choice == 1:
            graph(False)
        elif choice == 2:
            gateways(False)
        elif choice == 3:
            graph(True)
        elif choice == 4:
            gateways(True)
        elif choice == 5:
            optimal()
        else:
            print("\n Invalid Option Please try again!!!")    
if __name__ == "__main__":
    main()
   