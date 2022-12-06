import timeit


def marker_lookup(data: list, size: int) -> int:
    for i, char in enumerate(data):
        end_idx = i + size
        partial_data = data[i:end_idx]
        if len(set(partial_data)) == size:
            return end_idx


def solution_part_1():
    marker_size = 4
    with open("input_data.txt") as file:
        data = list(file.readline().strip())
        return marker_lookup(data, marker_size)


def solution_part_2():
    marker_size = 14
    with open("input_data.txt") as file:
        data = list(file.readline().strip())
        return marker_lookup(data, marker_size)


if __name__ == "__main__":
    times = 1
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=times)/(times) * 1000} ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=times)/(times) * 1000} ms'
    )
