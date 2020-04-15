# Outline - Keychain

## A simple Outline Server Access Key Copy and Paste Web Interface

Developed for key and password export and copy & paste for other Shadowsocks clients to access Outline Server

## Instruction
1. Install dependencies from requirements.txt 
`pip3 install -r requirements.txt` 

2. Copy your **Management API URL**s in **settings** of each server in [Outline Manager](https://getoutline.org/en/home)

3. Paste them into **index.html** in each `""` of `value=""` from line 15 and on

4. Run app.py 
`python3 app.py`

5. Access localhost, usually http://127.0.0.1:5000/

## Why does this program exist
Just uses requests and urllib3 to override https verify so that API could be used without any SSL certificates

