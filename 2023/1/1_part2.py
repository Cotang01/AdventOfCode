

def answer(file_path: str) -> int:
    to_digit_forward = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    to_digit_backwards = {
        'eno': '1',
        'owt': '2',
        'eerht': '3',
        'ruof': '4',
        'evif': '5',
        'xis': '6',
        'neves': '7',
        'thgie': '8',
        'enin': '9'
    }

    with open(file_path) as file:
        content = file.readlines()
    numbers_forward = []
    for line in content:
        current_digits = []
        buffer = ''
        for elem in line:
            buffer += elem
            for k, v in to_digit_forward.items():
                if k in buffer:
                    current_digits.append(v)
                    buffer = ''
            if elem.isdigit():
                current_digits.append(elem)
        numbers_forward.append(current_digits)

    numbers_backwards = []
    for line in content:
        current_digits = []
        buffer = []
        for elem in line[::-1]:
            buffer.append(elem)
            for k, v in to_digit_backwards.items():
                if k in ''.join(buffer):
                    current_digits.append(v)
                    buffer = []
            if elem.isdigit():
                current_digits.append(elem)
        numbers_backwards.append(current_digits)
    return sum([int(numbers_forward[i][0] + numbers_backwards[i][0])
                for i in range(len(numbers_forward))])
