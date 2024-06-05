from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a new key for encryption and decryption.
    """
    return Fernet.generate_key()

def create_cipher(key):
    """
    Create a new Fernet cipher object using the given key.
    """
    return Fernet(key)

def encrypt_data(cipher, data):
    """
    Encrypt the given data using the given cipher.
    """
    return cipher.encrypt(data)

def decrypt_data(cipher, encrypted_data):
    """
    Decrypt the given encrypted data using the given cipher.
    """
    return cipher.decrypt(encrypted_data)