import subprocess
from time import sleep
from sys import argv
from sys import exit


def inc_mac(mac):
    arr = [el.rjust(2,'0') for el in mac.split(':')]
    mac = ''.join(arr)
    val = int(mac, 16);
    val += 1
    inc = "%12x" % val
    arr = [inc[2*i:2*i+2] for i in range(len(inc)//2)]
    return ':'.join(arr)


def spoof_mac(interface, mac):
    # verify the interface is existing
    #? subprocess.Popen(['ip','link','show',interface])
    subprocess.call(['ip','link','set','dev',interface,'down'])
    subprocess.call(['ip','link','set','dev',interface,'address',mac])
    subprocess.call(['ip','link','set','dev',interface,'up'])



params = {}
for i in range(len(argv)):
    if argv[i][0] == '-':
        params[argv[i]] = i

if '-t' in params:
    delay = int(argv[params['-t'] +1])
else:
    delay = 15 * 60 # quarter an hour

if '-i' in params:
    interface = argv[params['-i'] +1]
else:
    print('you supplied no interface.\n' +
          'Supply one with the -i switch.\n')
    exit()

if '-m' in params:
    mac = argv[params['-m'] +1]
else:
    print('you supplied no initial mac adress.\n' +
          'Supply one with the -m switch.\n')
    exit()




while True:
    mac = inc_mac(mac)
    print(mac)
    spoof_mac(interface, mac)
    sleep(delay)
