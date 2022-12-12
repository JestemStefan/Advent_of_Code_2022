import re
import timeit
from functools import reduce


class Monkey:
    def __init__(
        self,
        items,
        operation,
        op_value,
        divide_test_value,
        monkey_idx_when_true,
        monkey_idx_when_false,
    ):
        self.items = items
        self.operation = operation
        self.op_value = op_value
        self.divide_test_value = divide_test_value
        self.monkey_idx_when_true = monkey_idx_when_true
        self.monkey_idx_when_false = monkey_idx_when_false
        self.inspection_counter = 0

    def do_what_monkeys_do_part_1(self, item):
        self.inspection_counter += 1
        if self.operation == "+":
            new_value = self._add_to_current_value(item)

        elif self.operation == "*":
            new_value = self._multiply_current_value(item)

        else:
            new_value = self._power_current_value(item)

        new_value //= 3

        target = (
            self.monkey_idx_when_true
            if new_value % self.divide_test_value == 0
            else self.monkey_idx_when_false
        )

        return target, new_value

    def do_what_monkeys_do_part_2(self, item, divider):
        self.inspection_counter += 1
        if self.operation == "+":
            new_value = self._add_to_current_value(item)

        elif self.operation == "*":
            new_value = self._multiply_current_value(item)

        else:
            new_value = self._power_current_value(item)

        reminder = new_value % self.divide_test_value

        new_value %= divider

        target = (
            self.monkey_idx_when_true if reminder == 0 else self.monkey_idx_when_false
        )

        return target, new_value

    def _add_to_current_value(self, item) -> int:
        return item + self.op_value

    def _multiply_current_value(self, item) -> int:
        return item * self.op_value

    def _power_current_value(self, item) -> int:
        return item**self.op_value

    def __str__(self):
        return f"{self.inspection_counter}"


def solution_part_1():
    monkeys = []
    with open("input_data.txt") as file:
        pattern = re.compile(r"\d+")
        for line in file:
            starting_items = [x for x in map(int, re.findall(pattern, file.readline()))]
            *_, operation, op_value = file.readline().split()
            if op_value == "old":
                op_value = 2
                operation = "**"

            op_value = int(op_value)

            divide_test_value = int(file.readline().split()[-1])
            monkey_idx_when_true = int(file.readline().split()[-1])
            monkey_idx_when_false = int(file.readline().split()[-1])
            _empty_line = file.readline()

            monkey = Monkey(
                items=starting_items,
                operation=operation,
                op_value=op_value,
                divide_test_value=divide_test_value,
                monkey_idx_when_true=monkey_idx_when_true,
                monkey_idx_when_false=monkey_idx_when_false,
            )
            monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                target_monkey_idx, new_value = monkey.do_what_monkeys_do_part_1(item)
                monkeys[target_monkey_idx].items.append(new_value)

            monkey.items = []

    sorted_list = sorted(monkeys, key=lambda m: -m.inspection_counter)
    return sorted_list[0].inspection_counter * sorted_list[1].inspection_counter


def solution_part_2():
    monkeys = []
    with open("input_data.txt") as file:
        pattern = re.compile(r"\d+")
        for line in file:
            starting_items = [x for x in map(int, re.findall(pattern, file.readline()))]
            *_, operation, op_value = file.readline().split()
            if op_value == "old":
                op_value = 2
                operation = "**"

            op_value = int(op_value)

            divide_test_value = int(file.readline().split()[-1])
            monkey_idx_when_true = int(file.readline().split()[-1])
            monkey_idx_when_false = int(file.readline().split()[-1])
            _empty_line = file.readline()

            monkey = Monkey(
                items=starting_items,
                operation=operation,
                op_value=op_value,
                divide_test_value=divide_test_value,
                monkey_idx_when_true=monkey_idx_when_true,
                monkey_idx_when_false=monkey_idx_when_false,
            )
            monkeys.append(monkey)

    all_dividers_multiplied = reduce(
        lambda x, y: x * y, [m.divide_test_value for m in monkeys]
    )

    for _ in range(10_000):
        for monkey in monkeys:
            for item in monkey.items:
                target_monkey_idx, new_value = monkey.do_what_monkeys_do_part_2(
                    item, all_dividers_multiplied
                )
                monkeys[target_monkey_idx].items.append(new_value)

            monkey.items = []

    sorted_list = sorted(monkeys, key=lambda m: -m.inspection_counter)
    return sorted_list[0].inspection_counter * sorted_list[1].inspection_counter


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
