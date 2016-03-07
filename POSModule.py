# -*- coding: utf-8 -*-
"""
Here will be all the code related to ou data, Add, Update, Delete, and Get
""" 

#Dictionary of Articles
Articles={
          "A00000001": ("Book: Lean Analytics"),
          "A00000002": ("Book: Lean Start-Up"),
          "A00000003": ("Book: Data Mining"),
          "A00000004": ("Book: Why Nations Fail"),
          "A00000005": ("Book: Getting to Yes"),
          "A00000006": ("Music: Passion Pit")
          }

#Dictionary of customers
Customers={"C00000001": "Rahul",
           "C00000002": "Xuan",
           "C00000003": "Carlos",
           "C00000004": "Ahmed",
           "C00000005": "Gaille"}

#List of Lists of sales (ArticleID, CustomerID, Cash or Credit (zero or One), Payment)
Sales=[
    ["A00000003","C00000001",0,1000],
    ["A00000006",0,1,2000],
    ["A00000005","C00000001",0,3000],
    ["A00000005","C00000002",1,2000],
    [0,0,1,1000],
    [0,0,0,3000],
        ]
        
#Last30Days
Last30Days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

#Choices of inputs to the console that can be done by the user
InputCommand=["sale","customer","report","crm","close day","quit","close"]


"""
Desc: Returns the input commands of the system that can be used by the user
Param:
Return: Dictionary of input commands
"""
def GetInputCommands():
    '''
    check doc
    '''
    return InputCommand

"""
Desc: Returns the wanted Article if found and if not found return Nothing
Param: Article ID of type Integer
Return: Wanted Article or None
"""
def GetArticleByIDm(ArticleID):
    return GetItemByID(ArticleID,Articles)
    
"""
Desc: Returns the wanted Customer if found and if not found return Nothing
Param: Customer ID of type Integer
Return: Wanted Customer or None
"""
def GetCustomerByIDm(CustomerID):
    return GetItemByID(CustomerID,Customers)


"""
Desc: Returns the wanted generic item if found and if not found return Nothing
Param: Generic Item ID of type Integer
Return: Wanted Item or None
"""
def GetItemByID(ItemID, Items):
    if ItemID in Items:
        return Items[ItemID]
    return None #this will be executed if the if condition is false


"""
Desc: Adds new Sale to the Sales
Param: SaleList
Return: Success string if Operation is done
"""
def AddSalesm(SaleList):
    Sales.append(SaleList)
    return "Success"
    

"""
Desc: Adds new Customer
Param: CustomerList
Return: Success string if Operation is done
"""
def AddCustomerm(CustomerList):
    Customers[CustomerList[0]]=CustomerList[1]
    return "Success"
"""
Desc: Adds new Article
Param: Article List
Return: Success string if Operation is done
"""
def AddSKUm(SKUList):
    Articles[SKUList[0]]=SKUList[1]
    return "Success"
    
"""
Desc: Getting All Customers
Param: 
Return: All Customers
"""
def GetAllCustomersm():
    return Customers


"""
Desc: Getting All Sales
Param: 
Return: All Sales
"""
def GetAllSalesm():
    return Sales
    
"""
Desc: Getting All Articles
Param: 
Return: All Articles
"""
def GetAllArticlesm():
    return Articles
    
"""
Desc: Remove from the last 30 days list based on its index location
Param: 
Return: Success if operation done
"""
def Last30DaysPOP(POPIndex):
    l=Last30Days.pop(POPIndex)
    return "Success"
    
"""
Desc: Remove from the last 30 days list based on its index location
Param: 
Return: Success if operation done
"""
def Last30DaysInsertAtFirstDay(ValueToAdd):
    Last30Days.insert(0,ValueToAdd)
    return "Success"
    
"""
Desc: Get Last 30 Days Sales
Param: 
Return: Last 30 Days Sales
"""
def GetLast3DaysSales():
    return Last30Days
    
