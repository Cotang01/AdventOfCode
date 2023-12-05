
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


# hyper-neutrino
def answer_2(file_path: str) -> int:
    with open(file_path) as file:
        content = file.readlines()
    result = 0
    for line in content:
        nums = [ch for ch in line if ch.isdigit()]
        result += int(nums[0] + nums[-1])
    return result
