import pandas as pd
import numpy as np
import matplotlib as plt
df=pd.read_html('https://merolagani.com/LatestMarket.aspx')
df[0].to_csv('stock.csv')
st=pd.read_csv('stock.csv')
#print (st)
st.drop(['Unnamed: 8','Unnamed: 9','Unnamed: 0'], axis=1 , inplace=True)
#print(st.columns)
#print (st)
#st=st.groupby('Symbol')[['LTP','% Change']].sum().reset_index()
print (st)
#NIFRA
nifra=st[st['Symbol']=='NIFRA']
#print(nifra)
print("\r\r")
if ((nifra.iloc[0,3])>0):
    print("\r"+ str((nifra.iloc[0,0]))  +" share have increased by "+str(nifra.iloc[0,3]) +"% and latest LTP is: "+str(nifra.iloc[0,1]))
elif((nifra.iloc[0,3])<0):
    print("\r"+ str((nifra.iloc[0,0]))  +" share have decreased by "+str(nifra.iloc[0,3]) +"% and latest LTP is: "+str(nifra.iloc[0,1]))
elif((nifra.iloc[0,3])==0):
    print("\r"+ str((nifra.iloc[0,0]))  +"share is constant and latest LTP is: "+str(nifra.iloc[0,1]))
#CGH
CGH=st[st['Symbol']=='CGH']
#print(CGH)
print("\r\r")
if ((CGH.iloc[0,3])>0):
    print("\r"+ str((CGH.iloc[0,0]))  +" share have increased by "+str(CGH.iloc[0,3]) +"% and latest LTP is: "+str(CGH.iloc[0,1]))
elif((CGH.iloc[0,3])<0):
    print("\r"+ str((CGH.iloc[0,0]))  +" share have decreased by "+str(CGH.iloc[0,3]) +"% and latest LTP is: "+str(CGH.iloc[0,1]))
elif((CGH.iloc[0,3])==0):
    print("\r"+ str((CGH.iloc[0,0]))  +" share is constant and latest LTP is: "+str(CGH.iloc[0,1]))



