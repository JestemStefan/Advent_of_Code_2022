import timeit


def solution_part_1():
    cycle = 0
    register_value = 1
    solution = 0
    check_cycles = {20, 60, 100, 140, 180, 220}

    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

            if data[0] == "noop":
                cost = 1
                value = 0

            else:
                cost = 2
                command, value = data[0], int(data[1])

            for _ in range(cost):
                cycle += 1
                if cycle in check_cycles:
                    solution += cycle * register_value

            register_value += value

    return solution


def solution_part_2():
    cycle = 0
    register_value = 1
    display = [list() for _ in range(6)]

    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

            if data[0] == "noop":
                cost = 1
                value = 0

            else:
                cost = 2
                value = int(data[1])

            for _ in range(cost):
                row_id = cycle // 40
                pixel = "#" if abs((cycle % 40) - register_value) <= 1 else " "

                display[row_id].append(pixel)

                cycle += 1

            register_value += value

    for row in display:
        print("".join(row))

    return 0


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
