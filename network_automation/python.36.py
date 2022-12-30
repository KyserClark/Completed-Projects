import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

file = open('myswitches')

for ip in file:
    ip = ip.strip()
    print("Configuring Switch " + ip)
    tn = telnetlib.Telnet(ip)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")

    for n in range(2, 20):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_Vlan_" + str(n).encode('ascii') + b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
