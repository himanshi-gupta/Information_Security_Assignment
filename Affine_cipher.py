'''Menu Driven Program to implement Encryption and Decryption using Affine Cipher.'''

def check_inverse(key):
    if key in (1,3,5,7,9, 11, 13,15, 17, 19, 21, 23,25):
        return True
    return False

def inverse(key):
    '''
    Purpose of the function is to find the inverse of a key mod 26.
    Input : key - key whose inverse need to be found
    Output : return the inverse of key mod 26
    '''
    #traverse through 0 to 25
    for i in range(26):
        #if i is the inverse of k, (i*key)mod 26 will be 1
        if (key*i)%26==1:
            return i
        
def encrypt(plain_text,key1,key2):
    '''
    Purpose of the function is to return a cipher text given a plain text and 2 keys.
    The uppercase alphabets are encrypted into uppercase alphabets and lowercase to
    lowercase.Other symbols digits and space are kept same.
    
    Input : plain_text - text to be encoded
            key1 - key that is multiplied to ascii of alphabet of plain text
            key2 - key that is added to ascii of alphabet of plain text
    Output : returns a cipher text after applying key1*alphabet+key2
    '''
    cipher_text=""

    #traversing through plain text
    for i in plain_text:

        #if alphabet is uppercase
        if i.isupper():  
            cipher_text+= chr((key1*(ord(i)-65)+key2)%26+65)    

        #if alphabet is lowercase
        elif i.islower():
            cipher_text+= chr((key1*(ord(i)-97)+key2)%26+97)

        #other than uppercase and lowercase
        else:
            cipher_text+=i
    return cipher_text

def decrypt(cipher_text,key1,key2):
    '''
    Purpose of the function is to return a plain text given a cipher text and 2 keys.
    The uppercase alphabets are decrypted into uppercase alphabets and lowercase to
    lowercase.Other symbols digits and space are kept same.
    
    Input : cipher_text - text to be decrypted
            key1 - key whose inverse is multiplied to ascii of alphabet of plain text
            key2 - key that is subtracted from ascii of alphabet of plain text
    Output : returns a cipher text after applying inverse(key1)*alphabet-key2
    '''
    plain_text=""

    #traversing through cipher text
    for i in cipher_text:
        #if alphabet is uppercase
        if (i.isupper()):  
            plain_text+= chr((inverse(key1)*(ord(i)-65-key2))%26+65)      

        #if alphabet is lowercase
        elif i.islower():
            plain_text+= chr((inverse(key1)*(ord(i)-97-key2))%26+97)

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

            #taking ist key from user
            key1=int(input("Enter Ist key : "))

            #taking 2nd key from user
            key2=int(input("Enter IInd key : "))

            if check_inverse(key1):
                #invoking the encrypt function for getting cipher text
                cipher_text=encrypt(plain_text,key1,key2)

                print("\nPlain text : ",plain_text)
                print("Cipher text : ",cipher_text)

            else:
                print("Key is invalid!")
            

        #if user want to decrypt    
        elif ch=='2':
            #taking cipher text from user
            cipher_text=input("Enter Cipher text : ")

            #taking ist key from user
            key1=int(input("Enter Ist key : "))

            #taking 2nd key from user
            key2=int(input("Enter IInd key : "))

            if check_inverse(key1):
                #invoking the decrypt function for getting plain text
                plain_text=decrypt(cipher_text,key1,key2)

                print("\nCipher text : ",cipher_text)
                print("Plain text : ",plain_text)

            else:
                print("Key is invalid!")
            
        #if user want to exit    
        elif ch=='3':
            print("Thankyou!")
            return
        
        #if user enter invalid choice
        else:
            print("Invalid Input!")
           

if __name__=='__main__':
    main()
