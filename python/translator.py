
# Dictionary for Braille to English
import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'cap', '.O...O': 'dec', '.O.OOO': '#', '..OO.O': '.',
    '..O...': ',', '..O.OO': '?', '..OO..': ':', '..O.O.': ';', '....OO': '-',
    '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
    '......': ' '
}

# Dictionary for English to Braille
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'cap': '.....O', 'dec': '.O...O', '#': '.O.OOO', '.': '..OO.O',
    ',': '..O...', '?': '..O.OO', ':': '..OO..', ';': '..O.O.', '-': '....OO',
    '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......'
}

def is_braille(s):
    # check if input is braille
    return all(c in 'O.o.' for c in s)

def translate_to_braille(text):
    braille_output = []
    num_mode = False

    for char in text:
        if char.isdigit():
            if not num_mode:
                braille_output.append(english_to_braille['#'])
                num_mode = True
            braille_output.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                braille_output.append(english_to_braille['cap'])
                braille_output.append(english_to_braille[char.lower()])
            else:
                braille_output.append(english_to_braille[char])
            num_mode = False
        else:
            braille_output.append(english_to_braille[char])
            num_mode = False

    return ''.join(braille_output)

def translate_to_english(braille):
    english_output = []
    num_mode = False
    capital = False

    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        
        if symbol == '.O.OOO':
            num_mode = True
            continue
        
        if symbol == '.....O':
            capital = True
            continue
        
        if num_mode:
            found_digit = False
            for k, v in english_to_braille.items():
                if v == symbol and k.isdigit():
                    english_output.append(k)
                    found_digit = True
                    break
            if not found_digit:
                english_output.append('')
        else:
            letter = braille_to_english.get(symbol, '')
            if capital and letter:
                letter = letter.upper()
                capital = False
            english_output.append(letter)

    return ''.join(english_output)


def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <input>')
        return

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()
