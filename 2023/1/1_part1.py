
def answer(file_path: str) -> int:
    with open(file_path) as file:
        content = file.readlines()
    numbers = []
    for line in content:
        current_digits = []
        for elem in line:
            if elem.isdigit():
                current_digits.append(elem)
        numbers.append(current_digits)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i][0] + numbers[i][-1])
    return sum(numbers)
