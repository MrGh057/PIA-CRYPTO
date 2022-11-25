import base64,getpass, os, vigenere, binascii, sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from nacl.signing import SigningKey
from nacl.exceptions import BadSignatureError
from art import *
import os

def limpiarTermminal():
    input("\n [+] Preisona para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

class usuario:
    def __init__(self): 
        self.keypair = SigningKey.generate()
        self.usuario = str(input('\t> Usuario: '))
        self.passwd = str(getpass.getpass('\t> Contraseña: '))
   
    @staticmethod
    def leer(path:str): 
        with open(path, 'rb') as fl:
            return fl.read()

    @staticmethod
    def guardar(data,path):
        with open(path, 'wb') as fl:
            fl.write(data)

    def generar_llave(self): 
        passwd = self.passwd.encode('utf-8')
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'vmsoxcghoincwp', iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(passwd))
        return key
    
    def encriptar_llave(self,usrdata):
        llave = self.generar_llave()
        Fenc = Fernet(llave)
        encK =  Fenc.encrypt(usrdata)
        return encK

    def desencriptar_llave(self,usrdata):
        llave = self.generar_llave()
        Fdec = Fernet(llave)
        decK = Fdec.decrypt(usrdata)
        return decK
    
    def firmado(self):
        llave = SigningKey(self.keypair._seed)
        firma = llave.sign(self.usuario.encode('utf-8'))
        return firma

    def registro(self):
        if os.path.exists(f"{self.usuario}.key"):
            print("El usuario ya existe, Intente de nuevo...")
            return False
            
        usrkey = f'{self.usuario}.key'
        usrcert = f'{self.usuario}.cer'
        self.guardar( self.encriptar_llave(self.keypair._seed) , usrkey)    
        self.guardar( self.firmado() , usrcert)
    
    def filtro_vigere(self): 
        key_chars = []

        for c in self.passwd:
            if c.isdigit():
                continue
            else:
                key_chars.append(c)

        return ''.join(key_chars)

    def encriptacion_vigere(self, data):
        keyword = self.filtro_vigere()
        cipher = vigenere.encrypt(data,keyword) 
        vigfile = f'result-{self.usuario}.txt'
        self.guardar(base64.decodebytes(cipher.encode('utf-8')), vigfile)

    def desencriptacion_vigere(self):
        keyword = self.filtro_vigere()
        vigfile = f'result-{self.usuario}.txt'
        cipher = base64.encodebytes(self.leer(vigfile)).decode('utf-8')
        plain_msg = vigenere.decrypt(cipher, keyword)
        print(f'\t> Texto encriptado: {plain_msg}')


    def login(self):
        try:
            usrkey =  f'{self.usuario}.key'
            usrcert = f'{self.usuario}.cer'
            
            seed = self.leer(usrkey) 
            firma = self.leer(usrcert) 
            
            decryptedKey = self.desencriptar_llave(seed)
            checker = SigningKey(decryptedKey).verify_key
                                
            try: 
                checker.verify(firma)
                return True
            except BadSignatureError:
                print('\n\t[!] USUARIO O CONTRASEÑA INCORRECTOS...')
                limpiarTermminal()
                menu()
                return False
        except Exception:
            print('\n\t[!] USUARIO O CONTRASEÑA INCORRECTOS...')
            limpiarTermminal()
        
def menu():
    print(text2art("CryptoLab"))
    print("""
    Integrantes:
    [->] Jose Gerardo Mauricio Esquivel
    [->] Pedro Saldaña Vazquez
    [->] Luis Angel Reyes Olvera
    [->] Jose Arturo Sandoval Errisuriz
    [->] Jesus Alejandro García Dorado
    """)
    print("="*80)
    print(
        "\n[1] Iniciar Sesion.\n"
        "[2] Nuevo usuario.\n"
        "[3] Salir."
    )
    op = int(input("\n[>] Ingresa una opcion: "))

    if op == 1 or op == 2:
        usuario_nuevo = usuario()

    if op == 1:
        if usuario_nuevo.login():
            limpiarTermminal()
            usuario_nuevo.menu_login()
        menu()
    elif op == 2:
        usuario_nuevo.registro()
        limpiarTermminal()
        menu()
    elif op == 3:
        sys.exit()
    else:
        limpiarTermminal()
        menu()