import re


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
    numbers_backwards = []
    for line in content:
        current_digits_f = []
        buffer_f = ''
        for elem in line:
            buffer_f += elem
            for k, v in to_digit_forward.items():
                if k in buffer_f:
                    current_digits_f.append(v)
                    break
            if elem.isdigit():
                current_digits_f.append(elem)
                break
        current_digits_b = []
        buffer_b = ''
        for elem in line[::-1]:
            buffer_b += elem
            for k, v in to_digit_backwards.items():
                if k in buffer_b:
                    current_digits_b.append(v)
                    break
            if elem.isdigit():
                current_digits_b.append(elem)
                break
        numbers_backwards.append(current_digits_b)
        numbers_forward.append(current_digits_f)
    return sum([int(numbers_forward[i][0] + numbers_backwards[i][0])
                for i in range(len(numbers_forward))])


# hyper-neutrino
def answer_2(file_path: str) -> int:
    with open(file_path) as file:
        content = file.readlines()
    num_words = ['one', 'two', 'three', 'four', 'five',
                 'six', 'seven', 'eight', 'nine']
    valid = '(?=(' + '|'.join(num_words) + '|\\d))'

    def num_converter(n: str):
        nonlocal num_words
        if not n.isdigit():
            return str(num_words.index(n) + 1)
        return n

    res = 0
    for line in content:
        digits = [*map(num_converter, re.findall(valid, line))]
        res += int(digits[0] + digits[-1])
    return res
