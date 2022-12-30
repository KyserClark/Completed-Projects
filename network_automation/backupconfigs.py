import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

file = open('myswitches')

for ip in file:
    ip = ip.strip()
    print('Getting running config from Switch ' + ip)
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'wr\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'show run\n')
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput = open('switch' + ip, 'w')
    saveoutput.write(readoutput.decode('ascii') + '\n')
    saveoutput.close()
