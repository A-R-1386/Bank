
class Bank:
    import json
    
    
    
    def __init__(self,name):
        self.name=name
        self.sign_up=[]
        self.tran=[]
        
        
    import random   
    def random_number(self,start,end):
            return self.random.randint(start,end) 
    
    def signup(self,name,age):
        if age>0:
            if len(name)<age:
                account_number1=self.random_number((len(name)+2)**100,(age+4)**100)
                account_number2=str(account_number1)
                account_number3=account_number2[0:7]
                self.sign_up.append(account_number3)
                print (" account number of",name ,"is : \n ",account_number3)
                return account_number3
            else:
                account_number1=self.random_number((age+2)**100,(len(name)+4)**100)
                account_number2=str(account_number1)
                account_number3=account_number2[0:7]
                self.sign_up.append(account_number3)
                print ("your account number is : \n ",account_number3)
                return account_number3
        else:
            print("your age is incorrect /n the program for you  isn't functioning properly !!")
            
            
            



        
        
    def balance_of(self,account):
        balance=0
        if account!="0000":
            for lst in self.tran:
                for char in lst[0:2]:
                    if char==account:
                        if char==lst[0]:
                            balance-=lst[2]
                        else:
                            balance+=lst[2]
            return balance
        else:
            return -1
        
        
    def transaction(self,sender,receiver,money):
        if sender and receiver in self.sign_up:
            if sender=="0000":
                self.tran.append([sender,receiver,money])
                return True
            else:
                if self.balance_of(sender)>=money:
                    (self.tran).append([sender,receiver,money])
                    return True
                else:
                    return False
        else:
            return False
         
    
    def history(self,account):
        lst_history=[]
        for lst in self.tran:
            if account in lst[0:2]:
                lst_history.append(lst)
        return lst_history
    
    
    def info(self):
        return(self.name,len(self.sign_up),len(self.tran))
    def transaction_history(self):
        return self.tran
    
    def save(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_sign_up=self.name+"_sign_up"+".json"
        
        with open(file_name_transaction,"w") as file:
            json.dump(self.tran,file)
            
        
            
        with open(file_name_sign_up,"w") as file:
            json.dump(self.sign_up,file)
            
            
    def load(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_sign_up=self.name+"_sign_up"+".json"
        
        with open(file_name_transaction,"r") as file:
            self.tran=json.load(file)
            
            
        with open(file_name_sign_up,"r") as file:
            self.sign_up=json.load(file)
        
            
        
            
            
        
    
    
    