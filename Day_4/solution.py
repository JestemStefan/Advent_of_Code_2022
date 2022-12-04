import timeit


def solution_part_1():
    with open("input_data.txt") as file:
        solution = 0

        for line in file:
            first_range, second_range = line.strip().split(",")
            first_start, first_end = map(int, first_range.split("-"))
            second_start, second_end = map(int, second_range.split("-"))

            if (first_start >= second_start and first_end <= second_end) or (
                second_start >= first_start and second_end <= first_end
            ):
                solution += 1

        return solution


def solution_part_2():
    with open("input_data.txt") as file:
        solution = 0

        for line in file:
            first_range, second_range = line.strip().split(",")
            start_first_range, end_first_range = map(int, first_range.split("-"))
            start_second_range, end_second_range = map(int, second_range.split("-"))

            if (start_first_range <= start_second_range <= end_first_range) or (
                start_second_range <= start_first_range <= end_second_range
            ):
                solution += 1

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
