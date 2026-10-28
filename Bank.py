import json
from user import User
class Bank:
    
    
    def __init__(self,name):
        self.name=name
        self.list_obj=[]
        self.tran=[]
        
        
    import random   
    def random_number(self,start,end):
            return self.random.randint(start,end) 
    

    def signup(self,name, age):
        account_number_Bank=str(self.random_number((len(name)+2)**100,(age+4)**100))
        account_number_Bank2=account_number_Bank[len(account_number_Bank)-7:]
        user = User(account_number_Bank2,name, age)
        print(user.name,"'s account number is :",user.account_number)
        self.list_obj.append(user)        
        return user.account_number   



        
        
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
        

    def get_all_accounts(self):#output :a list of accounts ,accounts  shoud signup before
        list_accounts=[]
        for obj in self.list_obj:
            list_accounts+=[obj.account_number]
        return list_accounts
            
        

        
        
    def transaction(self,sender,receiver,amount):
        
        
        
            if sender=="0000":
                
                for obj in self.list_obj:
                    
                    if receiver==obj.account_number:
                
                        self.tran.append([sender,receiver,amount])
                        return True
                
                
                return False

            
            
            
            
            
            else:
                list_accounts_transaction=self.get_all_accounts()
                
                if sender in list_accounts_transaction and receiver in list_accounts_transaction:
                    
                        if self.balance_of(sender)>=amount:
                            (self.tran).append([sender,receiver,amount])
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
        return(self.name,len(self.get_all_accounts()),len(self.tran))
    
    def transaction_history(self):
        return self.tran
    
    
    def get_user_by_account_number(account_number):
        for obj in self.list_obj:
            if obj.account_number==account_number:
                return (obj.account_number,obj.name,obj.age)
                
        
        
        
        
        
    def save(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        with open(file_name_transaction,"w") as file:
            json.dump(self.tran,file)
            
        dic_save={}
        for obj in self.list_obj:
            dic_save[obj.account_number]=[obj.name,obj.age]
        with open(file_name_accounts,"w") as file:
            json.dump(dic_save,file)
            
            
    def load(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        with open(file_name_transaction,"r") as file:
            self.tran=json.load(file)
            
        dic_load={}    
        with open(file_name_accounts,"r") as file:
            dic_load=json.load(file)
            for key in dic_load:
                user1=User(key,dic_load[key][0],dic_load[key][1])
                self.list_obj.append(user1)
            
                
                