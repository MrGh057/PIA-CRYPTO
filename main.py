import base64, time, sys, getpass, os, signal, binascii
import funciones
from nacl.signing import SigningKey
from nacl.exceptions import BadSignatureError
from art import *

print("="*90)
while True:
    funciones.menu()
    p = input("\t\n[?] ¿Desea permanecer dentro? s/n: ")
    if p == "s" or p == "S":
        continue
    else:
        break