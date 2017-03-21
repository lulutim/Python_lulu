#!/usr/bin/python
# Filename:  AddressBook.py
'''This is a AddressBook'''
import cPickle as p
#import pickle as p
import os

Dic_AB = {}
class Person:
    '''def __init__(self,name,telephone,mobile,address):
            self.name = name
            self.telephone = telephone
            self.mobile = mobile
            self.address = address'''

f = open(r'C:\work\Training\Python\exercise\AddressBook.data','a+')
try:
    Dic_AB = p.load(f)
    print Dic_AB
except EOFError:
    print Dic_AB
    pass
f.close()        

run = True
while (run == True):
    item = raw_input('input a item')
    print item
    ls_item = item.split(',')
    print ls_item
    if ls_item[0] == 'stop':
        run = False
    else:
        while (Dic_AB.has_key(ls_item[0])):
            ls_item[0] = ls_item[0]+'_0'
        person = Person()
        lenth = len(ls_item)
        if lenth ==1:
            person.name = ls_item[0]
        elif lenth == 2:
            person.name = ls_item[0]
            person.telephone = ls_item[1]
        elif lenth ==3:
            person.name = ls_item[0]
            person.telephone = ls_item[1]
            person.mobile =ls_item[2]
        else:
            person.name = ls_item[0]
            person.telephone = ls_item[1]
            person.mobile =ls_item[2]
            person.address =ls_item[3]
        print '***'
        for ab in Dic_AB:
            print ab
        Dic_AB[person.name]= person
f = open(r'C:\work\Training\Python\exercise\AddressBook.data','w+')
p.dump(Dic_AB,f)
f.close()
          
    
    



