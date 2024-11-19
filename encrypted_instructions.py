#125687164

def decode_string(encoded_string: str) -> str:
    """Расшифровывает строку."""
    def recursive_decode(index: int) -> (str, int):
        current_num = 0
        current_str = ""

        while index < len(encoded_string):
            char = encoded_string[index]
            if '0' <= char <= '9':
                current_num = current_num * 10 + int(char)
            elif char == '[':
                decoded_str, new_index = recursive_decode(index + 1)
                current_str += decoded_str * current_num
                current_num = 0
                index = new_index
                continue
            elif char == ']':
                return current_str, index + 1
            else:
                current_str += char

            index += 1

        return current_str, index

    result = recursive_decode(0)[0]
    return result


if __name__ == "__main__":
    input_string = input().strip()
    output_string = decode_string(input_string)
    print(output_string)
