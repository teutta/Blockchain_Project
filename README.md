# Blockchain_Project in Python 

This repository is a blockchain and its clients implementation in Python. 

The blockchain has the following features:

•	Proof of Work Algorithm

•	Resolve conflicts between blockchain’s nodes

•	Transactions with RSA encryption 

•	Adding nodes to the blockchain

• Mining transactions

The blockchain client has the following features:

•	Wallet generation of private and public key using RSA algorithm

•	Transaction generations 

• View transactions 

There are two dashboards: 

• "Blockchain Client" for clients to generate their public and private keys and make transactions 

• "Blockchain Frontend" for mining and adding transactions to the blockchain

# Dependecies

• Python 3.x

• Flask 

• Flask_cors

• Pycryptodome 

• Binascii

• Anaconda



# How to run the code 

1. To start a **blockchain node**,go to **blockchain.py** folder and execute the command : **python blockchain.py -p 1000**,to start Node 1 execute the command **python blockchain.py -p 1001** , and to start **Node 2** execute the command **python blockchain.py -p 1002**

2. To start the blockchain client,go to **blockchain_client.py folder** and execute the command: **python blockchain_client.py -p 8080**, to start client **Alice** execute the command: **python blockchain.py -p 8082** , and to start client **Bob** execute the following command:  **python blockchain.py -p 8081** 

3.You can have access to blockchain frontend and blockchain client dashboards from your browser by going **127.0.0.1:1000** and **127.0.0.1:8080** 
