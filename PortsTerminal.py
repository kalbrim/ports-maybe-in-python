import random

print("erlickk")




while True:
    print("1) see port protocol")
    print("2) exit")

    choice = input("please enter choice: ")

    choice = choice.strip()

    if (choice == "1"):
        d = {'21': 'ftp tcp', '22': 'sftp tcp/udp', '23': 'telnet tcp/udp', '25': 'smtp tcp', '53': 'dns tcp/udp', '69': 'tftp udp', '80': 'http tcp', '88': 'kerberos tcp/udp', '110': 'pop3 tcp', '119': 'nntp tcp', '135': 'rpc/dcom tcp/udp', '137-139': 'netbios tcp', '143': 'imap tcp', '161': 'snmp udp', '162': 'snmptrap tcp/udp', '389': 'ldap tcp/udp', '443': 'https tcp', '445': 'smb tcp', '465/587': 'smtp ssl tls tcp', '514': 'syslog udp', '636': 'smtp tcp', '860': 'iscsi tcp', '989/990': 'ftps tcp', '993': 'imap4 ssl tcp', '995': 'pop3 ssl tcp', '1433': 'ms sql tcp', '1645/1646': 'radius udp', '1701': 'l2tp udp', '1723': 'pptp tcp/udp', '1812/1813': 'radius udp', '3225': 'fcip tcp/udp', '3260': 'iscsi tor tcp', '3389': 'rdp tcp/udp', '3868': 'diameter tcp', '6514': 'syslog tls tcp'}
        port, description = random.choice(list(d.items()))
        print(description)
        answer = input("throw port: ")
        answer = answer.strip()

        if (answer == port):
            print("correct")
        else:
            print("wrong")

    else:
        exit()

