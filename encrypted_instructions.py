#125793073
valid_values = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def decode_string(encoded_string: str) -> str:
    """Расшифровывает строку."""
    result = ""
    stack = []
    count = ""
    current_fragment = ""

    for char in encoded_string:
        if char in valid_values:
            count += char
        elif char == '[':
            stack.append((current_fragment, count))
            current_fragment = ""
            count = ""
        elif char == ']':
            last, repeat_count = stack.pop()
            current_fragment = last + current_fragment * int(repeat_count)
        else:
            current_fragment += char

    result += current_fragment
    return result


if __name__ == "__main__":
    input_string = input()
    output_string = decode_string(input_string)
    print(output_string)
