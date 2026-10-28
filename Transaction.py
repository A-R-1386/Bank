class Transaction:
    from datetime import datetime
    def __init__(self,sender,receiver,amount,time):
        self.sender=sender
        self.receiver=receiver
        self.amount=str(amount)
        self.time=time
    