# 馃殌 PIA - Criptograf铆a 馃殌

## Descripci贸n
Este es el repositorio del PIA de criptograf铆a, el cual consiste en el desarrollo de un sistema criptogr谩fico, en este caso nos declinamos por el uso de Python 3 para el desarrollo de la actividad.

El sistema consiste en llo siguiente:
- Uso de curvas el铆pticas: En este caso (eDSA25519, Curve25519) nos apoyamos de la librer铆a [PyNaCl](https://pypi.org/project/PyNaCl/), importando el modulo que requerimos, en este caso, el de firmas, de la siguiente forma:
`from nacl.signing import SigningKey`

- Encriptaci贸n de llaves: para ello nos apoyamos de la librer铆a Fernet del modulo Cryptography, la cual es implementada para la encriptaci贸n y desencriptaci贸n de las llaves.
`from cryptography import Fernet`

- Base64: nos apoyamos del cifrado Base64 para las llaves de los usuarios
`import base64`

## USO

**Descarga**
- Linux
`$ git clone https://github.com/MrGh057/PIA_Crypto`

Para windows, basta con con dar descargar el repositorio de manera gr谩fica

### Requerimientos
Para facilitar la instalaci贸n de los modulos, es necesario correr el siguiente onliner en la terminal ya sea CMD, Bash, ZSH, cualquiera que sea la que utilices:
`$ pip install requeriments.txt`

### Ejecuci贸n
No requiere de argumentos iniciales, por lo cual la ejecuci贸n de este script es de la siguiente manera:
`$ python main.py`
