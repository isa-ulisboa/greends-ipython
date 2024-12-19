from gpiozero import LEDBoard
from time import sleep
import sys

# Define Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}

def encode_to_leds(leds, word):
    word = word.upper()
    for char in word:
        if char not in MORSE_CODE:
            print(f"Warning: Character '{char}' is not valid Morse code. Skipping.")
            continue

        code = MORSE_CODE[char]
        # turn on
        for i, symbol in enumerate(code):
            if i >= len(leds):
                break
            if symbol == '-' or symbol == '.':
                leds[i].on()
        sleep(1)

        # turn off '.'
        for i, symbol in enumerate(code):
            if i >= len(leds):
                break
            if symbol == '.':
                leds[i].off()
        sleep(1)

        # turn off '-'
        for i, symbol in enumerate(code):
            if i >= len(leds):
                break
            leds[i].off()

        sleep(3)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 LEDboard.py <word>")
        sys.exit(1)

    input_word = sys.argv[1]

    # Initialize LEDBoard with 5 GPIO pins
    leds = LEDBoard(5, 6, 13, 19, 26)


    try:
        encode_to_leds(leds, input_word)
    except KeyboardInterrupt:
        pass
    finally:
        leds.off()
