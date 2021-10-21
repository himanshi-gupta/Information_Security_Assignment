'''Menu Driven Program to implement Encryption and Decryption using Additive Cipher.'''

def encrypt(plain_text,key):
    '''
    Purpose of the function is to return a cipher text given a plain text and key. The uppercase
    alphabets are encrypted into uppercase alphabets and lowercase to lowercase.Other symbols
    digits and space are kept same.
    
    Input : plain_text - text to be encoded
            key - shift
    Output : returns a cipher text after shifting plain text by 'key' shift to right.
    '''
    cipher_text=""
    
    #traversing through plain text
    for i in plain_text:
        
        #if alphabet is uppercase
        if i.isupper():  
            cipher_text+= chr((ord(i)+key-65)%26+65)

        #if alphabet is lowercase
        elif i.islower():
            cipher_text+= chr((ord(i)+key-97)%26+97)

        #other than uppercase and lowercase
        else:
            cipher_text+=i
    return cipher_text

def decrypt(cipher_text,key):
    '''
    Purpose of the function is to return a plain text given a cipher text and key. The uppercase
    alphabets are decrypted into uppercase alphabets and lowercase to lowercase.Other symbols
    digits and space are kept same.
    
    Input : cipher_text - text to be decrypted
            key - shift
    Output : returns a plain text after shifting cipher text by 'key' shift to left.
    '''
    plain_text=""

    #traversing through cipher text
    for i in cipher_text:

        #if alphabet is uppercase
        if (i.isupper()):  
            plain_text+= chr((ord(i)-key-65)%26+65)

        #if alphabet is lowercase
        elif i.islower():
            plain_text+= chr((ord(i)-key-97)%26+97)

        #other than uppercase and lowercase
        else:
            plain_text+=i 
    return plain_text

def main():
    while(True):
        #MENU to be printed
        print("\n-----MENU------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        #taking choice from user
        ch=input("Enter choice : ")

        #if user want to encrypt
        if ch=='1':
            #taking plain text from user
            plain_text=input("Enter Plain text : ")
            
            #taking key from user
            key=int(input("Enter key : "))
            
            #invoking the encrypt function for getting cipher text
            cipher_text=encrypt(plain_text,key)
            
            print("\nPlain text : ",plain_text)
            print("Cipher text : ",cipher_text)

        #if user want to decrypt
        elif ch=='2':
            #taking cipher text from user
            cipher_text=input("Enter Cipher text : ")

            #taking key from user
            key=int(input("Enter key : "))

            #invoking the decrypt function for getting plain text
            plain_text=decrypt(cipher_text,key)
            
            print("\nCipher text : ",cipher_text)
            print("Plain text : ",plain_text)

        #if user want to exit
        elif ch=='3':
            print("Thankyou!")
            return

        #if user enter invalid choice
        else:
            print("Invalid Input!")
           

if __name__=='__main__':
    main()
