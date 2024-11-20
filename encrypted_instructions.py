#125846073
VALID_VALUES = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def decode_instructions(encoded_instructions: str) -> str:
    """Расшифровывает инструкцию."""
    stack = []
    multiplier = ''
    decoded_part = ''

    for char in encoded_instructions:
        if char in VALID_VALUES:
            multiplier += char
        elif char == '[':
            stack.append((decoded_part, int(multiplier)))
            decoded_part = ''
            multiplier = ''
        elif char == ']':
            last_part, repeat_multiplier = stack.pop()
            decoded_part = last_part + decoded_part * repeat_multiplier
        else:
            decoded_part += char

    return decoded_part


if __name__ == "__main__":
    input_instructions = input()
    output_instructions = decode_instructions(input_instructions)
    print(output_instructions)
