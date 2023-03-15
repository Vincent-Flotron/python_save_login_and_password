# Write me a python code that encrypt given "login" and "password".
# Then it save them in a file.
# Then it read this file reverse the encryption in order to display the originals "login" and "passwords".
# When saving the login and password in the file, save the key too.
# So when reading the file, you will get back the key to uncrypt the login and password.
# And hide a bit the key by applying it a rot(1) before saving it.
# Then getting back its value after reading it from the file by applying the reverse of rot(1)

from cryptography.fernet import Fernet

# Define the ROT-1 cipher function
def rot1(text):
    return "".join([chr((ord(c) + 1 - 32) % 94 + 32) for c in text])

# Define the inverse ROT-1 cipher function
def inverse_rot1(text):
    return "".join([chr((ord(c) - 1 - 32) % 94 + 32) for c in text])

# Generate a random key for encryption
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Encrypt the login and password
login = "my_username"
password = "my_password"
encrypted_login = fernet.encrypt(login.encode())
encrypted_password = fernet.encrypt(password.encode())

# Apply ROT-1 cipher to the key
encrypted_key = rot1(key.decode()).encode()

# Save the encrypted login, password, and key in a file
with open("login_info.txt", "wb") as file:
    file.write(encrypted_login + b"\n" + encrypted_password + b"\n" + encrypted_key)

# Read the encrypted login, password, and key from the file
with open("login_info.txt", "rb") as file:
    encrypted_data = file.read()

# Split the data into login, password, and key
encrypted_login, encrypted_password, encrypted_key = encrypted_data.split(b"\n")
decrypted_key = inverse_rot1(encrypted_key.decode()).encode()
fernet = Fernet(decrypted_key)

# Decrypt the login and password
decrypted_login = fernet.decrypt(encrypted_login).decode()
decrypted_password = fernet.decrypt(encrypted_password).decode()

# Display the original login and password
print(f"Login: {decrypted_login}")
print(f"Password: {decrypted_password}")



# from cryptography.fernet import Fernet

# def encrypt_login_password(login: str, password: str, file_path: str):
#     # Generate key
#     key = Fernet.generate_key()
#     # Create Fernet object with key
#     f = Fernet(key)
#     # Encrypt login and password
#     login_encrypted = f.encrypt(login.encode())
#     password_encrypted = f.encrypt(password.encode())
#     # Perform rot(1) on key
#     key = bytes([byte + 1 for byte in key])
#     # Write encrypted login, password, and key to file
#     with open(file_path, 'wb') as file:
#         file.write(login_encrypted)
#         file.write(password_encrypted)
#         file.write(key)

# def decrypt_login_password(file_path: str) -> tuple:
#     # Read encrypted login, password, and key from file
#     with open(file_path, 'rb') as file:
#         login_encrypted = file.readline()
#         password_encrypted = file.readline()
#         key = file.readline()
#     # Revert rot(1) on key
#     key = bytes([byte - 1 for byte in key])
#     # Create Fernet object with key
#     f = Fernet(key)
#     # Decrypt login and password
#     login = f.decrypt(login_encrypted).decode()
#     password = f.decrypt(password_encrypted).decode()
#     # Return decrypted login and password as a tuple
#     return login, password

# # Example usage
# file_path = "encrypted_file.txt"
# login = "my_username"
# password = "my_password"

# # Encrypt and save login and password to file
# encrypt_login_password(login, password, file_path)

# # Decrypt login and password from file and print them
# decrypted_login, decrypted_password = decrypt_login_password(file_path)
# print("Decrypted Login: ", decrypted_login)
# print("Decrypted Password: ", decrypted_password)
