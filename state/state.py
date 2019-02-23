import numpy as np
import random
import math, random 
import gym 
import numpy as np 


class State:
    def __init__(self, data1, data2, Bal_stock1, Bal_stock2, open_cash, timestep):
        self.Stock1Price=data1[timestep] #stock 1 open price
        self.Stock2Price=data2[timestep] #stock 2 open price
        self.Stock1Blnc=Bal_stock1 #stock 1 balance
        self.Stock2Blnc=Bal_stock2 #stock 2 balance
        self.open_cash=open_cash #cash balance
        self.fiveday_stock1=self.five_day_window(data1, timestep)
        self.fiveday_stock2=self.five_day_window(data2, timestep)
        #self.volume1=volume1[timestep]
        #self.volume2=volume2[timestep]
        self.portfolio_value=self.portfolio_value()

    def portfolio_value(self):
        pvalue=0
        #print("In portfolio func")
        #print("self.Stock1Price",self.Stock1Price, type(self.Stock1Price))
        #print("self.Stock1Blnc",self.Stock1Blnc[0], type(self.Stock1Blnc))

        v1=self.Stock1Price * float(self.Stock1Blnc)
        v2=self.Stock2Price * float(self.Stock2Blnc)
        v3=float(self.open_cash)
        return (v1+v2+v3)
    
    def next_opening_price(self):
        return [data1[timestep+1], data2[timestep+1]]
    
    def five_day_window(self,data, timestep):
        step = timestep
        if step < 5:
            return data[0]
        
        stock_5days = np.mean(data[step-5:step])
        #print("stock_5days=" + str(stock_5days))
        #print(stock_5days)

        #print(type(stock_5days))

        return stock_5days
    
    def reset(self):
        #self.state = torch.FloatTensor(torch.zeros(8)).cuda()
        self.Stock1Price=151.25 #stock 1 open price Google
        self.Stock2Price=21.845 #stock 2 open price Walmart
        self.Stock1Blnc=34 #stock 1 balance Google
        self.Stock2Blnc=221 #stock 2 balance Walmart
        self.open_cash=10000 #cash balance
        self.fiveday_stock1=151.25
        self.fiveday_stock2=21.845
        self.portfolio_value=10000
        
    def getState(self):
        #print("In get state")
        res=[]
        res.append(self.Stock1Price) #stock 1 open price
        res.append(self.Stock2Price) #stock 2 open price
        res.append(self.Stock1Blnc) #stock 1 balance
        res.append(self.Stock2Blnc) #stock 2 balance
        res.append(self.open_cash) #cash balance
        res.append(self.fiveday_stock1)
        res.append(self.fiveday_stock2)        
        res.append(self.portfolio_value)
        #res.append(self.volume1)
        #res.append(self.volume2)


        
        #print(res)
        res1=np.array([res])
        #print("res array"+np.array([res]))
        return res1