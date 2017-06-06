from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    counter = 0
    key_letter = ""
    encrypted_letter = ""
    encrypted_text = ""
    rot_num = ""
    for char in text:
        if not char.isalpha():
            encrypted_text += char
        else:
            #print(counter)
            key_letter = rot[counter % len(rot)]
            counter += 1
            #above 2 lines put out each letter of key according to length of rotation word.
            #the count advances it through the word.
            rot_num = alphabet_position(key_letter)
            #calls function that turns letters of key into numbers to be used as rotation figures.
            encrypted_letter = rotate_character(char, rot_num)
            encrypted_text += encrypted_letter
            #calls function to apply rotation equation to the letters of the text to encrypt them.
            #print(encrypted_text)
    return encrypted_text


def main():
    get_text = input("Type a message: ")
    print(get_text)
    get_encryption_key = input("Encryption key: \n")
    #print(get_encryption_key)
    print(encrypt(get_text, get_encryption_key))

if __name__ == '__main__': main()
