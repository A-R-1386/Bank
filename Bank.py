
class Bank:
    import json
    from user import User
    
    
    def __init__(self,name):
        self.name=name
        self.dic={}
        self.tran=[]
        
        
    import random   
    def random_number(self,start,end):
            return self.random.randint(start,end) 
    

    def signup(self,name, age):
        from user import User
        user = User(name, age)
        print(user.name,"'s account number is :",user.account_number)
        self.dic[user.account_number]={"name":user.name,"age":user.age}
        
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
        

    def get_accounts(self):#output :a list of accounts ,accounts  shoud signup before
        list_accounts=[]
        for key in self.dic:
            list_accounts+=key
        return list_accounts
            
        

        
        
    def transaction(self,sender,receiver,money):
        
        
        
            if sender=="0000":
                
                for key in self.dic:
                    
                    if receiver==key:
                
                        self.tran.append([sender,receiver,money])
                        return True
                
                
                return False

            
            
            
            
            
            else:
                list_accounts=self.get_accounts()
                
                if sender and receiver in list_accounts:
                    
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
        return(self.name,len(self.dic),len(self.tran))
    def transaction_history(self):
        return self.tran
    
    
    def get_user_by_account_number(account_number2):
        for key in self.dic:
            if key==account_number2:
                return (key,key["name"],key["age"])
                
        
        
        
        
        
    def save(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        with open(file_name_transaction,"w") as file:
            json.dump(self.tran,file)
            
        
            
        with open(file_name_accounts,"w") as file:
            json.dump(self.dic,file)
            
            
    def load(self):
        import json
        file_name_transaction=self.name+"_transaction"+".json"
        file_name_accounts=self.name+"_account"+".json"
        
        with open(file_name_transaction,"r") as file:
            self.tran=json.load(file)
            
            
        with open(file_name_accounts,"r") as file:
            self.dic=json.load(file)