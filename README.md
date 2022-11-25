# PIA - Criptografía

## Descripción
Este es el repositorio del PIA de criptografía, el cual consiste en el desarrollo de un sistema criptográfico, en este caso nos declinamos por el uso de Python 3 para el desarrollo de la actividad.

El sistema consiste en llo siguiente:
- Uso de curvas elípticas: En este caso (eDSA25519, Curve25519) nos apoyamos de la librería [PyNaCl](https://pypi.org/project/PyNaCl/), importando el modulo que requerimos, en este caso, el de firmas, de la siguiente forma:
`from nacl.signing import SigningKey`

- Encriptación de llaves: para ello nos apoyamos de la librería Fernet del modulo Cryptography, la cual es implementada para la encriptación y desencriptación de las llaves.
`from cryptography import Fernet`

- Base64: nos apoyamos del cifrado Base64 para las llaves de los usuarios
`import base64`

## USO

**Descarga**
- Linux
`$ git clone https://github.com/MrGh057/PIA_Crypto`

Para windows, basta con con dar descargar el repositorio de manera gráfica

### Requerimientos
Para facilitar la instalación de los modulos, es necesario correr el siguiente onliner en la terminal ya sea CMD, Bash, ZSH, cualquiera que sea la que utilices:
`$ pip install requeriments.txt`

### Ejecución
No requiere de argumentos iniciales, por lo cual la ejecución de este script es de la siguiente manera:
`$ python main.py`
