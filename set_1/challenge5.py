import string
from utils import xor_repeating_key

INPUT = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

EXPECTED_OUTPUT = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

KEY = "ICE"

def main():
    
    xored = xor_repeating_key(INPUT, KEY, True)
    print(f"Input:    {INPUT}")
    print(f"Xored:    {xored.hex()}")
    print(f"Expected: {EXPECTED_OUTPUT}")

if __name__ == "__main__":
    main()