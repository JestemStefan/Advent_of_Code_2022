import timeit


def solution_part_1():
    with open("input_data.txt") as file:
        list_of_elfs_calories = []
        current_elf_calories = 0

        for line in file:
            data = line.strip()
            if not data:
                list_of_elfs_calories.append(current_elf_calories)
                current_elf_calories = 0
                continue

            current_elf_calories += int(data)

        return max(list_of_elfs_calories)


def solution_part_2():
    with open("input_data.txt") as file:
        list_of_elfs_calories = []
        current_elf_calories = 0

        for line in file:
            data = line.strip()
            if not data:
                list_of_elfs_calories.append(current_elf_calories)
                current_elf_calories = 0
                continue

            current_elf_calories += int(data)

        top_tree = sorted(list_of_elfs_calories)
        top_tree.reverse()
        return sum(top_tree[:3])


if __name__ == "__main__":
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=1000)} ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=1000)} ms'
    )
