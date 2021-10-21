'''Program to Decrypt Monoalphabetic cipher by frequency anaylsis and printing top 10 results'''

import random

def decrypt(cipher_text,key):
    '''
    Purpose of the function is to decrypt the cipher text after key is known.
    Input : cipher_text - text to be decrypted
            key - key used to decrypt additive cipher
    Output : returns the plain text corresponding to plain text and key
    '''
    plain_text=""
    #traversing through plain text
    for i in cipher_text:
        
        #if alphabet is uppercase
        if (i.isupper()):  
            plain_text+= chr((ord(i)-key+64)%26+65)
            
        #if alphabet is lowercase
        elif i.islower():
            plain_text+= chr((ord(i)+key-96)%26+97)
            
        #other than uppercase and lowercase
        else:
            plain_text+=i 
    return plain_text

def freq_analyse(cipher_text):
    #creating a dictionary for storing frequencies
    freq=dict()
    plain_text=""

    #frequency of english alphabet in decreasing order
    letterFreq='ETAOINSHRDLCUMWFGYPBVKJXQZ'

    #traversing the english alphabets and initialising the count as zero in dictionary
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        freq[i]=0

    #updating the count of alphabets in cipher text in the dictionary
    for i in cipher_text:
        freq[i]+=1

    #sorting the dictionary on basis of frequency of each letter in reverse order
    sorted_freq = sorted(freq,key=freq.get,reverse=True)

    #for loop to print 10 plaintext
    for j in range(10):
        plain_text=""

        #shuffle the distinct alphabets in cipher text
        random.shuffle(sorted_freq)
        count=0

        #traversing the shufffled alphabets array 
        for i in sorted_freq:
            
            #updating the dictionary as per the shuffled array
            freq[i]=letterFreq[count]
            count+=1

        #creating plaintext as per the mapping
        for i in cipher_text:
            plain_text+=freq[i]
        print("\nPaint text ",j+1," : ",plain_text)
        
def main():
    #Taking cipher text from the user
    cipher_text=input("Enter cipher text : ")
    #invoking the freq_analyse function to print 10 possible plaintext 
    freq_analyse(cipher_text)
    
if __name__=='__main__':
    main()
    
