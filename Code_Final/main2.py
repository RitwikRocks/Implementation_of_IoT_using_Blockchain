# -*- coding: utf-8 -*-
"""
Created on Mon June 7 17:05:01 2023

@author: Ritwik Ranjan Pathak
"""


import fastapi as _fastapi
import blockchain as _blockchain
import uvicorn
from threading import Timer
import random 
import time
import Humidity as _humidity
text=""
count=0

blockchain = _blockchain.Blockchain()

app = _fastapi.FastAPI()
datarec=[""]

def entry():
    global text
    #getval=str(random.randint(1, 100))
    humidity,temperature=_humidity.execute()
    
    humidity=str(humidity)
    temperature=str(temperature)
    ins="Humidity: "+humidity+" Temperature: "+temperature
    print(ins)
    #insert="Humidity: "+humidity+" Temperature: "+temperatue
    datarec.append(ins)
    blockchain.mine_block(ins)
    thread1 = Timer(interval = 10, function = entry)
    thread1.start()
    global count
    count+=1
    print("count",count)
   
   
    if count%3==0:
        thread1.cancel()
    


# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
    entry()
 
    global count
    count=0
    block = blockchain.mine_block(data=data)
    return block


# endpoint to return the blo

@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    chain = blockchain.chain
    return chain

# endpoint to see if the chain is valid
@app.get("/validate/")
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@app.get("/blockchain/last/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
        
    return blockchain.get_previous_block()

def dict():
    for item in datarec:
        print(item)
        
    return


