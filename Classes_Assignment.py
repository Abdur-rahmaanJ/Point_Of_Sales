# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:25:13 2016

@author: rahulmehra
"""

# CUSTOMER CLASS #

class Customer(object):
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    
    @property   
    def Name(self):
        return self.name
        
    @Name.setter
    def Name(self,name):
        self.name.append(name)
        
    @property
    def Cust_ID(self):
        return self.ID
        
    @Cust_ID.setter
    def Cust_ID(self,ID):
        self.ID.append(ID)



# ARTICLE CLASS #
        
class Article(object):
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    
    @property  
    def Name(self):
        return self.name
        
    @Name.setter
    def Name(self,name):
        self.name.append(name)
        
    @property
    def Art_ID(self):
        return self.ID
        
    @Art_ID.setter
    def Art_ID(self,ID):
        self.ID.append(ID)  
        
 
# SALES CLASS #
   
class Sales(object):
    def __init__(self,Cust_ID,Art_ID,Mode_pay,Amount):
        self.Cust_ID = Cust_ID
        self.Art_ID = Art_ID
        self.Mode_pay = Mode_pay #zero by default is cash and one is cc# 
        self.Amount = Amount
    
    @property
    def custID(self):
        return self.Cust_ID
        
    @custID.setter
    def custID(self,ID):
        self.Cust_ID.append(ID)
        
    @property
    def artID(self):
        return self.Art_ID
        
    @artID.setter
    def artID(self,ID):
        self.Art_ID.append(ID) 
    @property    
    def modePay(self):
        if self.Mode_pay == 0:
            return "CC"
        else:
            return "CASH"
        return self.Mode_pay
    
    @modePay.setter    
    def modePay(self,pay):
        self.Mode_pay.append(pay)
    
    @property        
    def Amt(self):
        return self.Amount
        
    
    @Amt.setter
    def Amt(self,Amt):
        self.Amount.append(Amt)
        

            
            