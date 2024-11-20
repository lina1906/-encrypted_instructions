#125805345
valid_values = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def decode_string(encoded_string: str) -> str:
    """Расшифровывает строку."""
    stack = []
    count = ''
    current_fragment = ''

    for char in encoded_string:
        if char in valid_values:
            count += char
        elif char == '[':
            stack.append((current_fragment, count))
            current_fragment = ''
            count = ''
        elif char == ']':
            previous_fragment, repeat_count = stack.pop()
            current_fragment = previous_fragment + current_fragment * int(repeat_count)
        else:
            current_fragment += char

    return current_fragment


if __name__ == "__main__":
    input_string = input()
    output_string = decode_string(input_string)
    print(output_string)
