import requests
import argparse
import sys
import time

#parser stuff
parser = argparse.ArgumentParser()

parser.add_argument("-wh", type=str, required=True, help="webhook url")
parser.add_argument("-msgamt", type=int, required=True, help="message amt")
parser.add_argument("-cont", type=str, required=True, help="message content")

args = parser.parse_args()



# variables
webhook = args.wh
msgamt = args.msgamt
msgcont = args.cont

# juicy stuff

print("""    
      
                                                                                  
  █████████   █████                         █████████                                                                        
 ███▒▒▒▒▒███ ▒▒███                         ███▒▒▒▒▒███                                                                       
▒███    ▒▒▒  ███████    ██████   ████████ ▒███    ▒▒▒  ████████   ██████   █████████████   █████████████    ██████  ████████ 
▒▒█████████ ▒▒▒███▒    ▒▒▒▒▒███ ▒▒███▒▒███▒▒█████████ ▒▒███▒▒███ ▒▒▒▒▒███ ▒▒███▒▒███▒▒███ ▒▒███▒▒███▒▒███  ███▒▒███▒▒███▒▒███
 ▒▒▒▒▒▒▒▒███  ▒███      ███████  ▒███ ▒▒▒  ▒▒▒▒▒▒▒▒███ ▒███ ▒███  ███████  ▒███ ▒███ ▒███  ▒███ ▒███ ▒███ ▒███████  ▒███ ▒▒▒ 
 ███    ▒███  ▒███ ███ ███▒▒███  ▒███      ███    ▒███ ▒███ ▒███ ███▒▒███  ▒███ ▒███ ▒███  ▒███ ▒███ ▒███ ▒███▒▒▒   ▒███     
▒▒█████████   ▒▒█████ ▒▒████████ █████    ▒▒█████████  ▒███████ ▒▒████████ █████▒███ █████ █████▒███ █████▒▒██████  █████    
 ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒   ▒███▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒     
                                                       ▒███                                                                  
                                                       █████                                                                 
                                                      ▒▒▒▒▒                                                                                       ▀                          ▀                                                       
""")


while True:
    choice = input("are you sure you want to completely DECIMATE and utterly DESTROY this webhook? (y/n)").lower()
    if choice == "y":
        break
    elif choice =="n":
        sys.exit()
    else:
       continue


def spam():

    data = {
        "content": msgcont,
        "attachments": []
    }


    
    for i in range(msgamt):
        response = requests.post(webhook, json=data)
        if response.status_code == 204:
            print(f"[INFO/SENT] Message {i+1} successfully sent.")
            if i == 41:
                # tried to fix rate limiting here but didnt work as i planned lol  
                time.sleep(10)

    
        else:
            print(f"[INFO/ERROR] Message {i+1} not sent. Status code: {response.status_code}")

spam()

