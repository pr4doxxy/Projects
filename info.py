import os
import socket
import platform

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
sistema = platform.system()
versao = platform.release()
import getpass
user = getpass.getuser()


print("Informações da máquina:")
print(f"Usuário: {user}")
print(f"Hostname: {hostname}")
print(f"IP: {ip}")
print(f"Sistema: {sistema} {versao}")
