
import requests
import argparse
import sys
import time


# allow for infinite messages cuz it breaks otherwise
def msgamt_type(val):
    if val == "inf":
        return val
    if val.isdigit():
        return int(val)
    raise argparse.ArgumentTypeError("msgamt must be an integer or 'inf'")


#parser
parser = argparse.ArgumentParser()

parser.add_argument("-wh", type=str, required=True, help="webhook url")
parser.add_argument("-msgamt", type=msgamt_type, required=True, help="message amt")
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
                                                      ▒▒▒▒▒                                                                                                                                                                      

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


    def send(i=None):
        r = requests.post(webhook, json=data)
        if r.status_code == 204:
            print(f"[INFO/SENT] Message {i+1} sent successfully")
            time.sleep(0.5)
        else:
            print(f"[INFO/ERR] Message {i+1} not sent. {r.status_code}")

    if msgamt == "inf":
        i = 0
        while True:
            send(i)
            i += 1

    else:
        for i in range(msgamt):
            send(i)



spam()