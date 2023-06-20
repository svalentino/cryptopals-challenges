import string
from utils import print_result, xor_singlekey, ptype

INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def is_english_text(input, threshold = 60):
    common_letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', ' ']
    common_letter_count = 0

    for char in input.lower():
        if char in common_letters:
            common_letter_count += 1
    
    english_percentage = (common_letter_count / len(input)) * 100

    if english_percentage >= threshold:
        return True
    else:
        return False

def main():
    input_hex = bytes.fromhex(INPUT)

    alphabet = string.printable
    
    for i, ch in enumerate(alphabet):
        ch_byte = bytes(ch, 'utf-8')
        test = xor_singlekey(input_hex, ch_byte)
        test_decoded = test.decode('utf-8')

        if is_english_text(test_decoded, 50):
            print(f"Candidate key   : {ch}")
            print(f"candidate text  : {test_decoded}")

if __name__ == "__main__":
    main()
