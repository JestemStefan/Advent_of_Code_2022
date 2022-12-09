import timeit
from functools import reduce


def intersect_ray(grid, grid_size, tree, row, column) -> int:
    blocked_directions_count = 0
    # Check outer ring
    if row in [0, grid_size - 1] or column in [0, grid_size - 1]:
        return 1

    for right_ray_idx in range(column + 1, grid_size):
        if grid[row][right_ray_idx] >= tree:
            blocked_directions_count += 1
            break

    # down raycast
    for down_ray_idx in range(row + 1, grid_size):
        if grid[down_ray_idx][column] >= tree:
            blocked_directions_count += 1
            break

    # left raycast
    for left_ray_idx in reversed(range(0, column)):
        if grid[row][left_ray_idx] >= tree:
            blocked_directions_count += 1
            break

    # up raycast
    for up_ray_idx in reversed(range(0, row)):
        if grid[up_ray_idx][column] >= tree:
            blocked_directions_count += 1
            break

    return 0 if blocked_directions_count == 4 else 1


def get_scenic_score(grid, grid_size, tree, row, column) -> int:
    scenic_scores = []

    right_score = 0
    for right_ray_idx in range(column + 1, grid_size):
        right_score += 1
        if grid[row][right_ray_idx] >= tree:
            break
    scenic_scores.append(right_score)

    # down raycast
    down_score = 0
    for down_ray_idx in range(row + 1, grid_size):
        down_score += 1
        if grid[down_ray_idx][column] >= tree:
            break
    scenic_scores.append(down_score)

    # left raycast
    left_score = 0
    for left_ray_idx in reversed(range(0, column)):
        left_score += 1
        if grid[row][left_ray_idx] >= tree:
            break
    scenic_scores.append(left_score)

    # up raycast
    up_score = 0
    for up_ray_idx in reversed(range(0, row)):
        up_score += 1
        if grid[up_ray_idx][column] >= tree:
            break

    scenic_scores.append(up_score)

    return reduce(lambda x, y: x * y, scenic_scores)


def solution_part_1():
    with open("input_data.txt") as file:
        grid = [[t for t in map(int, row.strip())] for row in file]
        grid_size = len(grid)

        return sum(
            intersect_ray(grid, grid_size, tree, row_idx, column_idx)
            for row_idx, row in enumerate(grid)
            for column_idx, tree in enumerate(row)
        )


def solution_part_2():
    with open("input_data.txt") as file:
        grid = [[t for t in map(int, row.strip())] for row in file]
        grid_size = len(grid)

        return max(
            get_scenic_score(grid, grid_size, tree, row_idx, column_idx)
            for row_idx, row in enumerate(grid)
            for column_idx, tree in enumerate(row)
        )


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
