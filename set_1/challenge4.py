import string
from utils import brute_force_xor_singlekey

INPUT_FILE = "set_1/4.txt"

def main():
    # Define alphabet to use for brute forcing
    alphabet = string.printable

    with open(INPUT_FILE, "r") as f:
        input = f.readlines()

    for i, line in enumerate(input):
        line_hex = bytes.fromhex(line)

        candidates = brute_force_xor_singlekey(line_hex, alphabet, 70)

        if len(candidates) > 0:
            print(f"Candidate line #{i} : {line}")
            for candidate in candidates:
                print(f"Candidate line #{i} : key:  {candidate[1]}")
                print(f"Candidate line #{i} : text: {candidate[0]}")

if __name__ == "__main__":
    main()
