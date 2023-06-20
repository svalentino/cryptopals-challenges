def print_result(expected, output):
    print('{:<20}: {}'.format("Expected", expected))
    print('{:<20}: {}'.format("Processed", output))

def xor_strings(first, second):
    # expect bytes

    output = bytearray()
    for i in range(0, len(first), 1):
        output.append(first[i] ^ second[i])
    
    return output

def xor_singlekey(input: bytes, key):
    output = bytearray()
    for i in input:
        output.append(i ^ key[0])
    return output

def ptype(obj):
    print(type(obj))

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
    
def brute_force_xor_singlekey(input_hex: bytes, alphabet, threshold = 60):
    candidates = []
    for ch in alphabet:
        ch_byte = bytes(ch, 'utf-8')
        attempt = xor_singlekey(input_hex, ch_byte)

        try:
            attempt_decoded = attempt.decode('utf-8')

            if is_english_text(attempt_decoded, threshold):
                candidates.append((attempt_decoded, ch))
        
        except Exception:
            pass

    return candidates

def xor_repeating_key(input: str, key: str):
    output = bytearray()
    input_bytes = bytes(input, 'utf-8')
    key_bytes = bytes(key, 'utf-8')
    for i, letter in enumerate(input_bytes):
        key_index = i % len(key)
        output.append(letter ^ key_bytes[key_index])
    return output
