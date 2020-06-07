#!/usr/share/python
# -----------------------------------------------------
# Louis.py - whois analyser tool
# By raz0rG1rl
# -----------------------------------------------------
# Reminders
# AF_INET = Ipv4
# AF_INET6 = Ipv6
# -----------------------------------------------------

# Import socket module
import socket
# Create instance of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Stabilish connection with socket
s.connect(("200.160.2.3", 43))
# Send message to url
s.send("businesscorp.com.br", 80)
# Size of bytes to receive
response = s.recv(1024)
# Print the response
print(response)
