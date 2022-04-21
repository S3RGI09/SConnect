#!/usr/bin/python3


import getpass
import telnetlib
print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor

print("\033[1;31m"+" ____   ____                            _   ")
print("\033[1;31m"+"/ ___| / ___|___  _ __  _ __   ___  ___| |_ ")
print("\033[1;31m"+"\___ \| |   / _ \| '_ \| '_ \ / _ \/ __| __| github.com/S3>
print("\033[1;31m"+" ___) | |__| (_) | | | | | | |  __/ (__| |_ ")
print("\033[1;31m"+"|____/ \____\___/|_| |_|_| |_|\___|\___|\__|  V1.0")
print("\033[1;33m"+"[Info] Script para automatizar la conexion por telnet a un>
print("\033[;36m"+"  ||   Programada por S3RGI09 (Sergio Casero Verdial) ")
print("\033[1;34m"+"---------------------------------------------------------->
print("\033[;35m"+"* IG: s3rgi09__ | GitHub: S3RGI09"+'\033[0;m')

host = input("\033[1;32m"+"[+] IP a la que se quiere conectar: "+'\033[0;m')
host = host
print("Conectando a: " + host)
user = input("Username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(host)
tn.read_until(b"Login: ")
tn.write(user.encode("ascii") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii"))
