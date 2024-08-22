import os
import json

SEALED_DIR = '/sealed'
INPUT_DIR = '/input'
OUTPUT_DIR = '/output'

def process_input(input_file):
    with open(input_file, 'r') as f:
        input = json.load(f)

    data = input.get('data', '')
    words_to_find = ["hello", "world"]

    # You can create a file to securely store intermediate state
    # Gramine will auto encrypt/decrypt anything in SEALED_DIR
    proof_state_file = os.path.join(SEALED_DIR, f'{os.path.basename(input_file)}-helper.txt')

    with open(proof_state_file, 'w') as psf:
        psf.write("")

    for word in words_to_find:
        if word in data:
            with open(proof_state_file, 'a') as psf:
                psf.write(f"found {word}\n")

    with open(proof_state_file, 'r') as psf:
        found_count = sum(1 for _ in psf)

    return {"valid_contribution": found_count == len(words_to_find)}

def generate_proof():
    for filename in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, f"{filename}_result.json")

        result = process_input(input_path)

        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)
