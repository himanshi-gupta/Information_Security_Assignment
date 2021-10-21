'''Program to Decrypt Additive cipher by frequency anaylsis and printing top 10 results'''

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
    '''
    Purpose of the function is to do frequency attack on the cipher text by exploiting the
    frequency of english alphabets
    Input : cipher_text - text to be decrypted
    Output : returns nothing, just print 10 possible plain text
    '''
    freq=dict()
    
    #frequency of english alphabet in decreasing order
    letterFreq='ETAOINSHRDLCUMWFGYPBVKJXQZ'

    #traversing the english alphabets and initialising the count as zero in dictionary
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ':
        freq[i]=0

    #updating the count of alphabets in cipher text in the dictionary
    for i in cipher_text:
        freq[i]+=1

    #sorting the dictionary on basis of frequency of each letter in reverse order
    sorted_freq = sorted(freq, key=freq.get,reverse=True)
    
    count=0
    for i in sorted_freq:
        if count==10:
            break
        '''calculating key by mapping the alphabets in cipher text to english alphabets
        in reverse order'''
        key=ord(i)-ord(letterFreq[count])
        count+=1
        '''printing the plain text by invoking the decrypt function and passing cipher text
        and key calculated'''
        print("\n",count," Plain text : ",decrypt(cipher_text,key))
    
    
def main():
    #Taking cipher text from the user
    cipher_text=input("Enter cipher text : ")
    #invoking the freq_analyse function to print 10 possible plaintext 
    freq_analyse(cipher_text)
    
if __name__=='__main__':
    main()
    
