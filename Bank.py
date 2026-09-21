class Bank:
    def __init__(self,name):
        self.name=name
        self.tran=[]
        
    def check(self,account):
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
    def transaction(self,account1,account2,money):
        if account1=="0000":
            (self.tran).append([account1,account2,money])
            return True
        else:
            if self.check(account1)>=money:
                (self.tran).append([account1,account2,money])
                return True
            else:
                return False
         
    
    def history(self,account):
        lst_history=[]
        for lst in self.tran:
            for char in lst[0:2]:
                if account==char:
                    lst_history.append(lst)
        return lst_history
    


        
        
        