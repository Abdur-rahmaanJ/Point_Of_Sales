# -*- coding: utf-8 -*-
"""
Here will be all the code related to the Business Logic, Processes and checkings
""" 
import POSView2
import POSModule
import POSView
import sys
#import POSView2

"""
Desc: check if the user entered the word cancel to exit theprogram
Param:
Return:
"""
def CancelProgramCheck(InputStr):
    if InputStr.lower()=="cancel":
        sys.exit(0)

"""
Desc: Tells the customer that there is invalid Operation
Param:
Return:
"""
def InvalidInputOperation():
    POSView.PrintToUser("Invalid Operation")

"""
Desc: Checking on the user input selection to start the appropriate process
Param: string of the user input to check on it
Return:
"""
def ProceedWithUserSelection(UserChoice,newchoice):
    ''' check doc'''
    if UserChoice!="":
        UserChoice_Split=UserChoice.split()
    else:
        UserChoice_Split=["NoCommand"]
    EnteredCommand=UserChoice_Split[0].lower()
    while (len(UserChoice_Split)<=1 and EnteredCommand not in ("quit","report","crm"))  or not IsCommandValid(EnteredCommand) or len(UserChoice_Split)>5:
        InvalidInputOperation()
        UserChoice=POSView.GetUserChoice()
        UserChoice_Split=UserChoice.split()
        if UserChoice=="":
            UserChoice_Split=["NoCommand"]
        EnteredCommand=UserChoice_Split[0].lower()
    #Removing the command
    UserChoice_Split.remove(UserChoice_Split[0])
    newchoice.append(EnteredCommand)
    if EnteredCommand=="sale":
        SaleList=CheckSalesCommand(UserChoice_Split)
        if AddSalesc(SaleList)=="Success":
            return "The Sale successfuly added"
        else:
            return "Sale wasn't added, please try again later"
    elif EnteredCommand=="customer":
        CustomerList=CheckCustomerCommand(UserChoice_Split)
        if CustomerList is None:
            return "CustomerID already exists!"
        else:
            Status=AddCustomerc(CustomerList)
        
        if Status=="Success":
            return "The Customer successfuly added"
        else:
            return "Customer wasn't added, please try again later"
    elif EnteredCommand=="report":
        return "Report"
    elif EnteredCommand=="crm":
        return "CRM"
    elif UserChoice.lower()=="close day":
        CloseSalesDay()
        return "Close of Sales Day is done"
    elif EnteredCommand=="quit":
        return "\nThanks for using POS System\n"
    else:
        return "Wrong Command!"



"""
Desc: Check if the entered command is valid to our list of commands or not
Param: Command entered by user
Return: 0 if invalid command, 1 if valid command
"""
def IsCommandValid(CheckCommand):
    if CheckCommand not in POSModule.GetInputCommands():
        return 0 #yes its invalide command
    else:
        return 1 #Command is valid
        
"""
Desc: Check if the SKU command is valid or not
Param: SKU entered by user
Return: New SKU Data or None
"""
def CheckSKUCommand(UserChoice_Split):
    SKUList =None   
    SKUID=GetIDFromSKUCommand(UserChoice_Split[1])
    SKUName=UserChoice_Split[0]
    if SKUID is None:
        SKUList= None
    else:
        SKUList= [SKUID,SKUName] #return the customer list
    if SKUList is None:         
        return "ERROR"
    else:
        AddCustomerc(SKUList)
        POSView2.PrintToUser("Success") 
        return "Success"

"""
Desc: Get the SKUID from the SKU Command
Param: SKUID part in the SKU Command entered by user
Return: Only the SKUID or None if the ID already exists
"""    
def GetIDFromSKUCommand(SKUID):
    if  len(SKUID) !=9:
        POSView2.PrintToUser("Incorrect ID length, should be 9 characters")        
        return None
      
    SKU=GetArticleByIDc(SKUID)
    if SKU is not None:
        POSView2.PrintToUser("SKU Already Exists")
        return None
    else:
        return SKUID


"""
Desc: Check if the customer command is valid or not
Param: Customer Command entered by user
Return: New Customer Data or None
"""
def CheckCustomerCommand(UserChoice_Split):
    CustomerList =None   
    CustomerID=GetIDFromCustomerCommand(UserChoice_Split[1])
    CustomerName=UserChoice_Split[0]
    if CustomerID is None:
        CustomerList= None
    else:
        CustomerList= [CustomerID,CustomerName] #return the customer list
    if CustomerList is None:         
        return "ERROR"
    else:
        AddCustomerc(CustomerList)
        POSView2.PrintToUser("Success") 
        return "Success"

#"""
#Desc: Check if the customer command is valid or not
#Param: Customer Command entered by user
#Return: New Customer Data or None
#"""
#def CheckCustomerCommand(UserChoice_Split):
#    CustomerID=GetIDFromCustomerCommand(UserChoice_Split[1])
#    CustomerName=UserChoice_Split[0]
#    if CustomerID is None:
#        return None
#    else:
#        return [CustomerID,CustomerName] #return the customer list


"""
Desc: Get the CustomerID from the Customer Command
Param: CustomerID part in the Customer Command entered by user
Return: Only the customerID or None if the ID already exists
"""
def GetIDFromCustomerCommand(CustomerID):
#    InputMsg="Please Enter Valid Customer ID ONLY: "
#    if "id:" not in CustomerID:
#        POSView.PrintToUser("CustomerID is missing or wasn't written the expected format!")
#        CustomerID=GetUserInput(InputMsg)
    if  len(CustomerID) !=9:
#        POSView2.PrintToUser("Not nine characters!")
        POSView2.PrintToUser("Not nine characters!")        
        return None
#        CustomerID=GetUserInput(InputMsg)        
#    else:
#        CustomerID=CheckForNumberArguments(CustomerID,"The Customer ID was written with more than one ':'",InputMsg,2,":")
        
    Customer=GetCustomerByIDc(CustomerID)
    if Customer is not None:
        POSView2.PrintToUser("Customer Already Exists")
        return None
    else:
        return CustomerID

"""
Desc: check for the sales command is its valid or not
Param: Sales Command entered by user
Return: New Sale Data as a list
"""
def CheckSalesCommand(UserChoice_Split):
    ArticleID=GetSkuFromSaleCommand(UserChoice_Split)
    CustomerID=GetCustomerFromSaleCommand(UserChoice_Split)
    CC=GetCCFromSaleCommand(UserChoice_Split)
    Amount=GetAmountFromSaleCommand(UserChoice_Split)
    return [ArticleID,CustomerID,CC,Amount] #return the sale list


"""
Desc: Get the sale amount from the sale command
Param: Sales Command entered by user
Return: Sale amount
"""
def GetAmountFromSaleCommand(UserChoice_Split):
    Number_of_Arguments=len(UserChoice_Split)
    Amount=0
    InputMsg="Please Enter Valid Amount Number: "
    if Number_of_Arguments==1:
        Amount=int(CheckNumeric(UserChoice_Split[0],InputMsg))
    if Number_of_Arguments!=1:
        POSView.PrintToUser("Sale Amount is wrong!")
        Amount=int(CheckNumeric(GetUserInput(InputMsg),InputMsg))
    return Amount
        

"""
Desc: Get the Article(SKU) from the sale command
Param: Sales Command entered by user
Return: ArticleID or 0 incase it wasn't found
"""
def GetSkuFromSaleCommand(UserChoice_Split):
    for item in UserChoice_Split:
        if "sku:" in item.lower():
            InputMsg="Please Enter Valid Article Number: "
            ArticleID=CheckForNumberArguments(item,"The Article part was written with more than one ':'",InputMsg,2,":")
            ArticleID=CheckArticle(ArticleID,InputMsg)
            UserChoice_Split.remove(item)
            return ArticleID
    return 0 #means we didn't find it
    
"""
Desc: Get the CustomerID from the sale command
Param: Sales Command entered by user
Return: CustomerID or 0 incase it wasn't found
"""
def GetCustomerFromSaleCommand(UserChoice_Split):
    for item in UserChoice_Split:
        if "id:" in item.lower():
            InputMsg="Please Enter Valid Customer ID: "
            CustomerID=CheckForNumberArguments(item,"The Customer part was written with more than one ':'",InputMsg,2,":")
            CustomerID=CheckCustomer(CustomerID,InputMsg)
            UserChoice_Split.remove(item)
            return CustomerID
    return 0 #means we didn't find it
    
"""
Desc: Get the CC from the sale command
Param: Sales Command entered by user
Return: CC or 0 incase it wasn't found
"""
def GetCCFromSaleCommand(UserChoice_Split):
    for item in UserChoice_Split:
        if "cc" in item.lower():
            UserChoice_Split.remove(item)
            return 1
    return 0 #means we didn't find it

"""
Desc: Checks the number of arguments inside the command is right
    for example SKU:11 and not SKU:wew:223
Param: 
    Item: the part to check its number of arguments
    ErrorMsg: The Error message to display to the user if we found a problem
    InputMsg: The input message that the user will react on it to input the write command
    ArgumentNumber: the expected number of argument in the item
    SplitCharacter: the character sperator in the item, like ":"
Return: the second part after the separator
"""
def CheckForNumberArguments(item,ErrorMsg,InputMsg,ArgumentNumber,SplitCharacter):
    SplitLength=len(item.split(SplitCharacter))
    while SplitLength!=ArgumentNumber:
        POSView.PrintToUser(ErrorMsg)
        return GetUserInput(InputMsg)
    return item.split(SplitCharacter)[1]


"""
Desc: Gets the user input with also checking if the user entered cancel to quit the program
Param: Message for the user of what to input
Return: string of the user input
"""
def GetUserInput(InputMsg):
    InputStr=POSView.InputFromUser(InputMsg)
    CancelProgramCheck(InputStr)
    return InputStr


"""
Desc: Check if the item (string) is numeric
Param: Item (string), Message for the user of what to input
Return: Item ID of type string
"""
def CheckNumeric(Item,MessageToUser):
    while not Item.isnumeric():
        POSView.PrintToUser("This is not a number")
        Item=GetUserInput(MessageToUser)
    return Item

"""
Desc: Return the Article that the user wants
Param: 
Return: Article ID that the user wants
"""
def CheckArticle(ArticleID,InputMsg):
    Article=GetArticleByIDc(ArticleID)
    while Article is None:
        POSView.ItemNotFound("Article")
        ArticleID=GetUserInput(InputMsg)
        Article=GetArticleByIDc(ArticleID)
    #print("The Article that was choosed is ", Article[0]," and its price is ",Article[1])
    return ArticleID
    
"""
Desc: Return the Customer that the user wants
Param: 
Return: Customer that the user wants
"""
def CheckCustomer(CustomerID,InputMsg):
    Customer=GetCustomerByIDc(CustomerID)
    while Customer is None:
        POSView.ItemNotFound("Customer")
        CustomerID=GetUserInput(InputMsg)
        Customer=GetCustomerByIDc(CustomerID)
    return CustomerID

"""
Desc: Returns the payment types
Param:
Return: List of payment types.
"""
def GetPaymentTypesc():
    return POSModule.GetPaymentTypesm()

"""
Desc: Returns the input commands of the system that can be used by the user
Param: None
Return: Dictionary of input commands
"""
def GetInputCommand():
    return POSModule.GetInputCommands()
    
"""
Desc: Returns the wanted Article if found and if not found return Nothing
Param: Article ID of type Integer
Return: Wanted Article or None
"""
def GetArticleByIDc(ArticleID):
    return POSModule.GetArticleByIDm(ArticleID)
    
"""
Desc: Returns the wanted Customer if found and if not found return Nothing
Param: Customer ID of type Integer
Return: Wanted Customer or None
"""
def GetCustomerByIDc(CustomerID):
    return POSModule.GetCustomerByIDm(CustomerID)
    
"""
Desc: Adds new Sale to the Sales
Param: SaleList
Return: Success string if Operation is done
"""
def AddSalesc(SaleList):
    return POSModule.AddSalesm(SaleList)
    
"""
Desc: Adds new Customer
Param: CustomerList
Return: Success string if Operation is done
"""
def AddCustomerc(CustomerList):
    return POSModule.AddCustomerm(CustomerList)

"""
Desc: Adds new Article
Param: Article LIst
Return: Success string if Operation is done
"""
def AddSKUc(SKUList):
    return POSModule.AddSKUm(SKUList)

"""
Desc: Getting All Customers
Param: 
Return: All Customers
"""
def GetAllCustomersc():
    return POSModule.GetAllCustomersm()

"""
Desc: Getting All Sales
Param: 
Return: All Sales
"""
def GetAllSalesc():
    return POSModule.GetAllSalesm()
  
"""
Desc: Preparing the Report
Param: 
Return: Report List
"""  
def PrepareReport():
    DaySales=POSModule.GetAllSalesm()
    CashAmount=0
    CreditAmount=0
    for item in DaySales:
        if item[2]==0: #cash
            CashAmount+=item[3]
        else: #Credit
            CreditAmount+=item[3]
    ReportList=[["Cash",CashAmount],["Credit",CreditAmount]]
    return ReportList
    
"""
Desc: Preparing the CRM Report
Param: 
Return: CRM Dictionary
0"""  
def PrepareCRM():
    DaySales=POSModule.GetAllSalesm()
    AllCustomers=POSModule.GetAllCustomersm()
    CRMDictionary={}
    for item in DaySales:
        if item[1]==0:
            if "Anonymous" in CRMDictionary:
                CRMDictionary["Anonymous"]=CRMDictionary["Anonymous"]+item[3]
            else:
                CRMDictionary["Anonymous"]=item[3]
        else:
            CustomerName=AllCustomers[item[1]]
            if CustomerName in CRMDictionary:
                CRMDictionary[CustomerName]=CRMDictionary[CustomerName]+item[3]
            else:
                CRMDictionary[CustomerName]=item[3]
    return CRMDictionary
    
"""
Desc: Close the sales day and update the list of the last 30 days os sales
Param: 
Return:
"""  
def CloseSalesDay():
    DaySales=POSModule.GetAllSalesm()
    SalesAmount=0
    for item in DaySales:
        SalesAmount+=item[3]
    print("ok")
    Last30DaysSales=POSModule.GetLast3DaysSales()
    if len(Last30DaysSales)==30:
        POSModule.Last30DaysPOP(len(Last30DaysSales)-1)
    POSModule.Last30DaysInsertAtFirstDay(SalesAmount)
