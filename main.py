from morse3 import Morse

txt_to_convert = input('Enter a Prompt: ')
morse_func = True
while morse_func:
    morse = Morse(txt_to_convert)
    prompt = input('encode or decode? Type e for encode and d for decode. ')
    if prompt == 'encode' or prompt == 'e':
        encode_text = morse.stringToMorse()
        print(f'Decoded Text : {encode_text}')
        morse_func = False
    elif prompt == 'decode' or prompt == 'd':
        decode_text = morse.morseToString()
        print(f'Encoded Text : {decode_text}')
        morse_func = False
    else:
        print("Wrong Command! Try again!")