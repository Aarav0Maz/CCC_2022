def process_tuning_instructions(instructions):
    result = []
    i = 0
    while i < len(instructions):
        # Extracting the string of uppercase letters
        string_sequence = ""
        while i < len(instructions) and instructions[i].isalpha():
            string_sequence += instructions[i]
            i += 1
        # Extracting the sign (+ or -)
        sign = instructions[i]
        i += 1
        # Extracting the positive integer
        turns = ""
        while i < len(instructions) and instructions[i].isdigit():
            turns += instructions[i]
            i += 1
        # Appending the result in a readable format
        action = 'tighten' if sign == '+' else 'loosen'
        result.append(f"{string_sequence} {action} {int(turns)}")

    return result

def main():
    # Reading input
    tuning_instructions = input().strip()

    # Processing instructions
    processed_instructions = process_tuning_instructions(tuning_instructions)

    # Outputting the result on separate lines
    for instruction in processed_instructions:
        print(instruction)

if __name__ == "__main__":
    main()