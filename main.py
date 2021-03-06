import time
from cryptography.fernet import Fernet

# SECRET_KEY is generated by calling Fernet.generate_key()
SECRET_KEY = b'3ujbEbhp4rJQ-Jo0vmUT5AZ7YooTSzSzVwKz5UNWaCs='
fernet = Fernet(SECRET_KEY)


def encrypt_file(path):
    with open(path, "rb") as file:
        file_bytes = file.read()
    
    encrypted_file_bytes = fernet.encrypt(file_bytes)

    with open(path, "wb") as file:
        file.write(encrypted_file_bytes)


def decrypt_file(path):
    with open(path, "rb") as file:
        file_bytes = file.read()
    
    decrypted_file_bytes = fernet.decrypt(file_bytes)

    with open(path, "wb") as file:
        file.write(decrypted_file_bytes)


def main():
    pass
    # encrypt_file('./file.txt')
    # decrypt_file('./file.txt')


if __name__ == "__main__":
    main()