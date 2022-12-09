import timeit
from string import ascii_letters


def solution_part_1():
    with open("input_data.txt") as file:
        solution = 0
        priority = {char: value + 1 for value, char in enumerate(ascii_letters)}

        for line in file:
            data = line.strip()
            sequence_middle = len(data) // 2
            first_half, second_half = data[:sequence_middle], data[sequence_middle:]

            for c in first_half:
                if c in second_half:
                    solution += priority[c]
                    break

        return solution


def solution_part_2():
    with open("input_data.txt") as file:
        solution = 0
        priority = {char: value + 1 for value, char in enumerate(ascii_letters)}

        for line in file:
            first_elf = line.strip()
            second_elf = file.readline().strip()
            third_elf = file.readline().strip()

            for c in first_elf:
                if c in second_elf and c in third_elf:
                    solution += priority[c]
                    break

        return solution


if __name__ == "__main__":
    times = 1000
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=times)/(times) * 1000} ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=times)/(times) * 1000} ms'
    )
