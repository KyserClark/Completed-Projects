import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

file = open('myswitches')

for ip in file:
    ip = ip.strip()
    print('Setting up ssh for Switch ' + ip)
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'enable\n')
    tn.write(b'conf t\n')
    tn.write(b'username Kyser privilege 15 password Kyser\n')
    tn.write(b'line vty 0 4\n')
    tn.write(b'login local\n')
    tn.write(b'transport input all\n')
    tn.write(b'exit\n')
    tn.write(b'ip domain-name kyserclark.com\n')
    tn.write(b'cryto key generate rsa\n')
    tn.write(b'1024\n')
    tn.write(b'end\n')
    tn.write(b'wr\n')
