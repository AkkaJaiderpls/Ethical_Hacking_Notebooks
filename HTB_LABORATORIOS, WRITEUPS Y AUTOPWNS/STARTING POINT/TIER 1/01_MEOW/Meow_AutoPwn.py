# IMPORTAMOS LIBRERIAS
from os import *
import telnetlib
import signal

host = ""
user = "root"
password = ""

# CERRAR EL PROGRAMA
def ctrl_c(sig, frame):
    print(f"\n\n [!] Saliendo...")
    exit(1)
signal.signal(signal.SIGINT, ctrl_c)

# PROCESO
def process():
    tn = tn.read_until(b"Login: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"ls \n")
    tn.write(b"exit \n")

# EJECUCION
if __name__ == "__main__":
    process()