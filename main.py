from ping3 import ping
import time
from datetime import datetime


print("Start ping tool with IPs from /ip_table.txt \n")
input_loop_delay = input('Enter loop delay in seconds: ')
input_IP_retry = input('Enter number of retrys each IP: ')
input_IP_timeout = input('Enter timeout for each retry in seconds: ')

with open('ip_table.txt') as f:
    IP_table = f.read().splitlines()

    for i, line in enumerate(IP_table):
        global temp_array
        temp_array = IP_table[i].split('.')

    if temp_array[3] == '0':
        print('do full IP range: ' + str(IP_table))
        IP_table.clear()
        for i in range(1, 255):
            IP_table.append(str(temp_array[0]) + "." + str(temp_array[1]) + "." + str(temp_array[2]) + "." + str(i))


def time_now():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

with open('output.txt', 'w') as f:
    f.write('Start ping at: '+ time_now())


def myping(host):
         n = 1
         while n <= int(input_IP_retry):
            n += 1
            resp = ping(host, unit='ms', timeout=int(input_IP_timeout))
            if resp == False or resp == None:
                continue
            else: return round(resp,1)
         else: return False


def ping_loop():

    print("new loop:")

    for client in IP_table:
        ping_result = myping(client)
        if ping_result == False:
            print(client + "-> " + str(ping_result) )
            with open('output.txt', 'a') as f:
                f.write('\n' + str(client) + ' no response at: ' + time_now())
        else: print(client + "-> " + str(ping_result) + "ms ")
    print("")



while True:
    ping_loop()
    time.sleep(int(input_loop_delay))
