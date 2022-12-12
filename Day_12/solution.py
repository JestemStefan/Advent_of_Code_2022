import timeit


def solution_part_1():
    """
    Solution proposal:
    Count the cost of reaching each point on the map from the source.
    The cost is amount of steps required to reach this point. (Cost of previous node + 1)
    Dijkstra-like?

    Avoid loops. Keep track of visited nodes in each path
    and if node is already in this path then stop checking this path.
    Mark all nodes in this path as visited

    If node was reached by other path with lower cost then current
    path should be marked as visited
    """
    with open("input_data.txt") as file:
        for line in file:
            ...

    return 0


def solution_part_2():
    with open("input_data.txt") as file:
        for line in file:
            ...

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
