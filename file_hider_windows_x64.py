from cryptography.fernet import Fernet
import os
from pathlib import Path


class File:
    def encrypt(self, file_name):
        # check key is avilerble
        try:
            # opening the key
            with open('encryption.key', 'rb') as file_key:
                key = file_key.read()
        except Exception:
            # key generation
            key = Fernet.generate_key()

            # string the key in a file
            with open('encryption.key', 'wb') as file_key:
                file_key.write(key)
            with open('encryption.key', 'rb') as file_key:
                key = file_key.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(file_name, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt(self, file_name):
        # opening the key
        with open('encryption.key', 'rb') as file_key:
            key = file_key.read()

        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open(file_name, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file_name, 'wb') as dec_file:
            dec_file.write(decrypted)

    def get_file_paths(self, dir_in):
        def scanRecurse(base_dir):
            """
            Scan a directory and return a list of all files
            return: list of files
            """
            for entry in os.scandir(base_dir):
                if entry.is_file():
                    yield entry
                else:
                    yield from scanRecurse(entry.path)

        file_path_list = []
        for item in scanRecurse(dir_in):
            filePath = Path(item)
            file_path_list.append(filePath)

        return file_path_list


def scan():
    hider = File()
    file_paths = hider.get_file_paths('locker')
    return file_paths


def encode(file_paths):
    hider = File()
    for file in file_paths:
        hider.encrypt(file)


def decode(file_paths):
    hider = File()
    for file in file_paths:
        hider.decrypt(file)


while True:
    print("""████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████
Welocome to File Hider
Source credis to @hora_pusa
1. Hide Files
2. Unhide Files
3. exit""")
    command = input("> ")
    if command == "1":
        try:
            os.system("md locker")
        except:
            pass
        print("Put your files in locker folder.")
        input("Press Enter to Hide files.")
        file_paths = scan()
        encode(file_paths)
        os.system("attrib +h +s +r locker")
        os.system("cls")

    elif command == "2":
        os.system("attrib -h -s -r locker")
        input("Press Enter to Unhide files.")
        file_paths = scan()
        decode(file_paths)
        os.system("cls")

    else:
        exit()
