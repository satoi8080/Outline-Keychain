#Outline Flask Interface

## A simple Outline Management API Web Interface


Developed for rapid key and password export and copy & paste for other Shadowsocks clients to access Outline Server

## Instruction
0. Install dependencies from requirements.txt 
pip install -r requirements.txt 

1. Insert your API URL copied from settings in Outline Manager App

2. Into index.html from line 14 and on

3. Run app.py with Python3

4. Access localhost

## Why does it exist
Just uses requests urllib3 to override https verify so that API could be used without any SSL certificates