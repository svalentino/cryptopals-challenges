import base64

INPUT = "1c0111001f010100061a024b53535009181c"
INPUT_XOR = "686974207468652062756c6c277320657965"

EXPECTED_OUTPUT = "746865206b696420646f6e277420706c6179"

def xor(first, second):
    # expect bytes

    output = bytearray()
    for i in range(0, len(first), 1):
        output.append(first[i] ^ second[i])
    
    return output

def print_result(expected, output):
    print('{:<20}: {}'.format("Expected", expected))
    print('{:<20}: {}'.format("Processed", output))

def main():
    input_hex = bytes.fromhex(INPUT)
    input_xor_hex = bytes.fromhex(INPUT_XOR)

    xored = xor(input_hex, input_xor_hex)

    print_result(EXPECTED_OUTPUT, xored.hex())

if __name__ == "__main__":
    main()
