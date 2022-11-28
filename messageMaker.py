import random
from base64 import b64decode, b64encode
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
# from Crypto.Random import get_random_bytes
#please install venv, pycrypto "pip3 install pycryptodome",


'''in this case we used pre made messages a Car would communicate, this can be always expanded using machine learning'''
def messageMaker():
    messages= ["Accident Ahead", "Police Reported Ahead", "Ambulance Ahead", "Broken Down Car Ahead", "Pothole Ahead", "Traffic Light Ahead"]
    chosenMessage = random.choice(messages)
    # print (chosenMessage) # uncomment to test to see if it is working
    return (chosenMessage)

def valueGen(encryptedMsg):
    text = encryptedMsg
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    ans = sum(ascii_values)
    return ans

# https://medium.com/quick-code/aes-implementation-in-python-a82f582f51c2

#The class will recieve a key of any length then it will generate a 256bit has from that key.
class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    #  Encrypt method recieves the plaintext and then pads it to add the extra bits it needs. then we generate a random "iv" with 128bits
    #   using the PyCryptodome library we create the AES cipher by using AES.new("ourkey", CBC Mode, and our "iv") ... Explain CBC MODE
    #we then use cipher.encrypt with our new AES system and decode it back from bits to readable characters
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")


    # Decrypt is basically undoin everything encrypt() has done, first go back to bits then take out the iv, which is the 128 bits from encrypted_text
    # a new AES key is generated in CBC mode and the "iv" we have taken out. last but not least we have to go form bits to text and take out the extra 
    # characters by the unpad function. 

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    #The Pad's job is to add extra characters to make it a multiple of 128, since we are using AES with 128bits
    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    # UnPad's job is to recive the plaintext and take out the extra characters
    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]





def main():
    newMessage = messageMaker() # a message has been made 
    key = input("Enter a Key Phrase: ")
    a = AESCipher(key)
    encryptedMsg = a.encrypt(newMessage)
    print("\n\nthis is the encrypted message: ", encryptedMsg)
    encryptedValue = valueGen(encryptedMsg)
    print ("this is the value for this encrypted Message", encryptedValue)
    
    print("\nNow we will decrypt the message")
    DKey = input("Enter the key used before: ")
    b = AESCipher(DKey)
    decryptedMsg = b.decrypt(encryptedMsg)
    print("\n\nHere is the Decrypted Message: ", decryptedMsg)
if __name__ == '__main__': 
    main() 
