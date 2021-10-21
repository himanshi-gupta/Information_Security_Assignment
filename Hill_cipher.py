
def encrypt_2(plain_text,key):
    result=[]
    for i in range(0,len(plain_text),2):
        for j in range(2):
            result.append(chr((key[j][0]*(ord(plain_text[i])-65)+key[j][1]*(ord(plain_text[i+1])-65))%26+65))
    cipher_text=''.join(result)
    return cipher_text

def encrypt(plain_text,key):
    rem=len(plain_text)%2
    if(rem==1):
        cipher=encrypt_2(plain_text[:-1],key)
        cipher+=chr((key[0][0]*(ord(plain_text[-1])-65))%26+65)
    else:
        cipher=encrypt_2(plain_text,key)
    return cipher
        
def mul_inverse(key):
    for i in range(26):
        if (key*i)%26==1:
            return i
        
def check_inverse(key):
    det=(key[0][0]*key[1][1]-key[1][0]*key[0][1])%26
    if det in (1,3,5,7,9, 11, 15, 17, 19, 21, 23,25):
        return True
    return False

def key_inverse(key,inv):
    key[0][0],key[1][1]=(key[1][1]%26)*inv%26,(key[0][0]%26)*inv%26
    key[0][1],key[1][0]=(-1*key[0][1]%26)*inv%26,(-1*key[1][0]%26)*inv%26
    return key

def decrypt_2(cipher_text,key):
    result=[]
    for i in range(0,len(cipher_text),2):
        for j in range(2):
            result.append(chr((key[j][0]*(ord(cipher_text[i])-65)+key[j][1]*(ord(cipher_text[i+1])-65))%26+65))
    plain_text=''.join(result)
    return plain_text

def decrypt(cipher_text,key):
    plain_text=""
    det=(key[0][0]*key[1][1]-key[1][0]*key[0][1])%26
    inv=mul_inverse(det)
    key_inverse(key,inv)
    rem=len(cipher_text)%2
    if(rem==1):
        plain=decrypt_2(cipher_text[:-1],key)
        plain+=chr((key[0][0]*(ord(plain_text[-1])-65))%26+65)
    else:
        plain=encrypt_2(cipher_text,key)
    return plain

def main():
    while(True):
        print("\n-----MENU------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        ch=input("Enter choice : ")
        if ch=='1':
            plain_text=input("Enter Plain text : ")
            k=[[0 for x in range(2)]for y in range(2)]
            for i in range(2):
                for j in range(2):
                    k[i][j]=int(input("enter ("+str(i)+","+str(j)+") : "))
            if check_inverse(k):
                cipher_text=encrypt(plain_text,k)
                print("\nPlain text : ",plain_text)
                print("Cipher text : ",cipher_text)
            else:
                print("Key is invalid!")
            
        elif ch=='2':
            cipher_text=input("Enter Cipher text : ")
            k=[[0 for x in range(2)]for y in range(2)]
            for i in range(2):
                for j in range(2):
                    k[i][j]=int(input("enter ("+str(i)+","+str(j)+") : "))
            if check_inverse(k):
                plain_text=decrypt(cipher_text,k)
                print("\nCipher text : ",cipher_text)
                print("Plain text : ",plain_text)
            else:
                print("Key is invalid!")
            
            
        elif ch=='3':
            print("Thankyou!")
            return
        else:
            print("Invalid Input!")
           

if __name__=='__main__':
    main()
