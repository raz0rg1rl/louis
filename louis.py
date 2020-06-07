#!/usr/share/python
# -----------------------------------------------------
# Louis.py - whois analyser tool
# By raz0rG1rl
# -----------------------------------------------------

import socket, sys

# Request to whois.iana.org
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))
s.send(sys.argv[1]+"\r\n")
response = s.recv(1024).split()
whois = response[19]

# Request to refer whois
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((whois, 43))
s2.send(sys.argv[1]+"\r\n")
whoisResponse = s2.recv(1024)
print(whoisResponse)
