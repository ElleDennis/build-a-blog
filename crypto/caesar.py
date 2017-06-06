from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    text = list(text)
    encrypted_text = ""
    for char in text:
        encrypted_char = rotate_character(char, int(rot))
        encrypted_text += encrypted_char
        #print(encrypted_char)
    return encrypted_text

def main():
    get_text = input("Type a message: ")
    print(get_text)
    get_rot = input("Rotate by: \n")
    #print(get_rot)
    print(encrypt(get_text,get_rot))

if __name__ == '__main__': main()
