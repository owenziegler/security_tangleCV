import random
import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
#please install venv, pycrypto "pip3 install pycrypto",


'''in this case we used pre made messages a Car would communicate, this can be always expanded using machine learning'''
def messageMaker():
    messages= ["Accident Ahead", "Police Reported Ahead", "Ambulance Ahead", "Broken Down Car Ahead", "Pothole Ahead", "Traffic Light Ahead"]
    chosenMessage = random.choice(messages)
    # print (chosenMessage) # uncomment to test to see if it is working
    return (chosenMessage)


# AES 256 encryption/decryption using pycrypto library
#https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html

 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
# password = input("Enter encryption password: ") pushed to main()
 
 #encrypting password using PBKDF2

def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key
 
 
def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))


'''using diffie hellman method for a Tangle CV, this will verify the number of the Genesis'''
# def verifier():
#     random.seed()
#     #chooses a random number to use for the private key for "a", used 0 to 100 just as an example, for better security choosing a larger range would be better
#     randomPrivKeyA = random.randint(0,100) 
#     #chooses a random number to use for the private key for "b",
#     randomPrivKeyB = random.randint(0,100)

#     #import function from lab5.py


def main():
    newMessage = messageMaker() # a message has been made 
    password = input("Enter encryption password: ") # key to which our encryption will be done with
    encryptedMsg = encrypt(newMessage, password)
    print(encryptedMsg)

if __name__ == '__main__': 
    main() 