import timeit


def solution_part_1():
    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

    return 0


def solution_part_2():
    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

    return 0


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
