import json
from user import User
from datetime import datetime
from Transaction import Transaction
class Bank:
    
    
    def __init__(self,name):
        self.name=name
        self.list_obj_User=[]
        self.list_obj_Transaction=[]

        
        
    import random   
    def random_number(self,start,end):
            return self.random.randint(start,end) 
    

    def signup(self,name, age):
        account_number_Bank=str(self.random_number((len(name)+2)**100,(age+4)**100))
        account_number_Bank2=account_number_Bank[len(account_number_Bank)-7:]
        user = User(account_number_Bank2,name, age)
        print(user.name,"'s account number is :",user.account_number)
        self.list_obj_User.append(user)        
        return user.account_number   



        
        
    def balance_of(self,account):
        balance=0
        if account!="0000":
            for obj in self.list_obj_Transaction:
                if obj.sender==account or obj.receiver==account:
                    if obj.sender==account:
                        balance-=int(obj.amount)
                    else:
                        balance+=int(obj.amount)
                        
                        
            return balance
        else:
            return -1
        

    def get_all_accounts(self):#output :a list of accounts ,accounts  shoud signup before
        list_accounts=[]
        for obj in self.list_obj_User:
            list_accounts+=[obj.account_number]
        return list_accounts
    
    
    def get_time(self):
        current_time = str(datetime.now().strftime("%H:%M:%S"))
        return current_time
        
        
            
        

        
        
    def transaction(self,sender,receiver,amount):
        
        
        
            if sender=="0000":
                
                for obj in self.list_obj_User:
                    
                    if receiver==obj.account_number:
                        time=self.get_time()
                        transaction=Transaction(sender,receiver,amount,time)
                        self.list_obj_Transaction.append(transaction)
                        
                        return True
                
                
                return False

            
            
            
            
            
            else:
                list_accounts=self.get_all_accounts()
                
                if sender in list_accounts and receiver in list_accounts:
                    
                        if self.balance_of(sender)>=amount:
                            time=self.get_time()
                            transaction=Transaction(sender,receiver,amount,time)
                            self.list_obj_Transaction.append(transaction)
                            return True
                        else:
                            return False
                                
                                      
                else:
                    return False

            
        
    
    def history(self,account):
        lst_history=[]
        for obj in self.list_obj.Transaction:
            
            if account==obj.sender or account==obj.receiver:
                
                lst_history.append([obj.sender,obj.receiver,obj.amount,obj.time])
                
        return lst_history
    
    
    def info(self):
        return(self.name,len(self.get_all_accounts()),len(self.list_obj_Transaction))
    
    def transaction_history(self):
        lst=[]
        for obj in self.list_obj_Transaction:
            lst+=[[obj.sender,obj.receiver,obj.amount,obj.time]]
        return lst
            
            
    
    
    def get_user_by_account_number(account_number):
        for obj in self.list_obj_User:
            if obj.account_number==account_number:
                return (obj.account_number,obj.name,obj.age)
                
        
        
        
        
        
    def save(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        list_save_Transaction=[]
        for obj in self.list_obj_Transaction:
            list_save_Transaction+=[[obj.sender,obj.receiver,obj.amount,obj.time]]
            
        with open(file_name_transaction,"w") as file:
            json.dump(list_save_Transaction,file)
            
        dic_save_User={}
        for obj in self.list_obj_User:
            dic_save_User[obj.account_number]=[obj.name,obj.age]
        with open(file_name_accounts,"w") as file:
            json.dump(dic_save_User,file)
            
            
    def load(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        list_load_Transaction=[]
        with open(file_name_transaction,"r") as file:
            list_load_Transaction=json.load(file)
            for lst in list_load_Transaction:
                transaction1=Transaction(lst[0],lst[1],lst[2],lst[3])
                self.list_obj_Transaction+=[transaction1]
            
        dic_load_User={}    
        with open(file_name_accounts,"r") as file:
            dic_load_User=json.load(file)
            for key in dic_load_User:
                user1=User(key,dic_load_User[key][0],dic_load_User[key][1])
                self.list_obj_User.append(user1)
            
                
                