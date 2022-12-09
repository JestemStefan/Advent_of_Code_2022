import timeit


def solution_part_1():
    with open("input_data.txt") as file:
        stacks = [[] for i in range(9)]

        # For first 7 lines read stack
        for line_idx in range(8):
            data = file.readline()
            stack_idx = 0
            for char_idx in range(1, len(data), 4):
                if box := data[char_idx].strip():
                    stacks[stack_idx].insert(0, box)
                stack_idx += 1

        # skip two empty lines
        file.readline()
        file.readline()

        for line in file:
            box_amount, source, target = [
                int(c) for c in line.strip().split(" ") if c.isdigit()
            ]
            boxes_to_transfer = []
            for _ in range(box_amount):
                boxes_to_transfer.append(stacks[source - 1].pop())

            stacks[target - 1].extend(boxes_to_transfer)

        return "".join(c[-1] for c in stacks if c)


def solution_part_2():
    with open("input_data.txt") as file:
        stacks = [[] for i in range(9)]

        # For first 7 lines read stack
        for line_idx in range(8):
            data = file.readline()
            stack_idx = 0
            for char_idx in range(1, len(data), 4):
                if box := data[char_idx].strip():
                    stacks[stack_idx].insert(0, box)
                stack_idx += 1

        # skip two empty lines
        file.readline()
        file.readline()

        for line in file:
            box_amount, source, target = [
                int(c) for c in line.strip().split(" ") if c.isdigit()
            ]
            boxes_to_transfer = []
            for _ in range(box_amount):
                boxes_to_transfer.append(stacks[source - 1].pop())

            stacks[target - 1].extend(reversed(boxes_to_transfer))

        return "".join(c[-1] for c in stacks if c)


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
