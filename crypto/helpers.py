def alphabet_position(letter):
    """alphabet_position receives single letter string & returns 0-based
        numerical position in alphabet of that letter."""
    alphabetL = "abcdefghijklmnopqrstuvwxyz"
    alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.lower()
    if letter in alphabetL:
        return alphabetL.find(letter)
    if letter in alphabetU:
        return alphabetU.find(letter)

def rotate_character(char, rot):
    """rotate_character receives single string character & an integer
        for rotation (rot) to places right in alphabet."""
    alphabetL = "abcdefghijklmnopqrstuvwxyz"
    alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if char.isalpha() == False:
        #to ignore all non-alpha chars
        return char
    if char.isupper():
        rotated_let_num = alphabet_position(char)
        """Calling the above function"""
        rotated_let_num = (rotated_let_num + int(rot)) % 26
        encrypted_letter_upper = alphabetU[rotated_let_num]
        return encrypted_letter_upper
    else:
        rotated_let_num = alphabet_position(char)
        """Calling the above function"""
        rotated_let_num = (rotated_let_num + int(rot)) % 26
        encrypted_letter = alphabetL[rotated_let_num]
        return encrypted_letter
