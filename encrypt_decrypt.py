# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:35:28 2020

@author: TejYadav
"""
def encrypt(sentence):
    
    result = []
    
    for letter in sentence:
        
        l = ord(letter) - 200
        result.append(l)
        
    print("This is your encrypted message!")
    for numbers in result:
        print(numbers, end='')
        print('', end='')
        
    print()
    decrypt(result)
    
def decrypt(result):
    
    end_string = ""
    
    for numbers in result:
        
        l = int(numbers)
        l = l + 200
        l = chr(l)
        end_string = end_string + l
        
    print('Your decrypted message is:')
    print(end_string)

def main():
    
    s = input("Input a sentence that your want to encrypt:")
    encrypt(s)
    
if __name__ == '__main__':
    main()