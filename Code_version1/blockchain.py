# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:00:01 2023

@author: Ritwik Ranjan Pathak
"""
import hashlib
class Block:
    def __init__(self,no,nonce,data,hashcode,prev):
        self.no=no
        self.nonce=nonce
        self.data=data
        self.hashcode=hash
        self.prev=prev
        
    def getStringVal():
        return self.no,self.nonce,self.data,self.hash,self.prev
    
    
    
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.prefix="0000"
        
    def addNewBlock(self,data):
        no=len(self.chain)
        nonce=0
        
        if len(self.chain)==0:
            prev="0"
        else:
            prev=self.chain[-1].hashcode
            
        myHash=hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        block=Block(no,nonce,data,myHash,prev)
        
        self.chain.append(block)
        
    def printBlockChain(self):
        chainDict={}
        for no in range(len(self.chain)):
            chainDict[no]=self.chain[no].getStringVal()
        print(chainDict)
        
        
    def mineChain(self):
        brokenLink=self.checkIfBroken()
        if(brokenLink==None):
            pass
        else:
            for block in self.chain[brokenLink.no:]:
                print(block.getStringVal())
                self.mineBlock(block)
                
                
    def mineBlock(self,block):
        nonce=0
        myHash=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
        while myHash[0:4]!=self.prefix:
            myHash=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
            nonce=nonce+1
        else:
            self.chain[block.no].hashcode=myHash
            self.chain[block.no].nonce=nonce
            if(block.no<len(self.chain)-1):
                self.chain[block.no+1].prev=myHash
                
                
    def checkIfBroken(self):
        for no in range(len(self.chain)):
            if(self.chain[no].hashcode[0:4]==self.prefix):
                pass
            else:
                self.chain[no]
            
            
    def changeData(self,no,data,nonce,block):
            self.chain[no].data=data
            self.chain[no].hashcode=hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
            
    def is_chain_valid(self) -> bool:
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            # Check if the previous hash of the current block is the same as the hash of it's previous block
            if block["previous_hash"] != self._hash(previous_block):
                return False

            previous_proof = previous_block["proof"]
            index, data, proof = block["index"], block["data"], block["proof"]
            hash_operation = _hashlib.sha256(
                self._to_digest(
                    new_proof=proof,
                    previous_proof=previous_proof,
                    index=index,
                    data=data,
                )
            ).hexdigest()

            if hash_operation[:4] != "0000":
                return False

            previous_block = block
            block_index += 1

        return True

            
            
        