def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shift_amount = shift % 26  
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter the shift value: "))
    
    encrypted = encrypt(message, shift_value)
    print("Encrypted message:", encrypted)
    
    decrypted = decrypt(encrypted, shift_value)
    print("Decrypted message:", decrypted)
