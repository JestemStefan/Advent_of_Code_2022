import timeit


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def solution_part_1():
    with open("input_data.txt") as file:
        visited_locations = set()
        head_pos = Position(0, 0)
        tail_pos = Position(0, 0)

        moves = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, -1),
            "D": (0, 1),
        }

        for line in file:
            data = line.strip().split()
            direction, distance = data[0], int(data[1])

            for _ in range(distance):
                move = moves[direction]
                head_pos.x += move[0]
                head_pos.y += move[1]
                if abs(tail_pos.x - head_pos.x) > 1:
                    tail_pos.x = head_pos.x - move[0]
                    tail_pos.y = head_pos.y

                elif abs(tail_pos.y - head_pos.y) > 1:
                    tail_pos.y = head_pos.y - move[1]
                    tail_pos.x = head_pos.x

                new_tail_pos = Position(tail_pos.x, tail_pos.y)
                visited_locations.add(new_tail_pos)

    return len(visited_locations)


def solution_part_2():
    with open("input_data.txt") as file:
        visited_locations = set()

        knots = [Position(0, 0) for i in range(10)]
        moves = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, -1),
            "D": (0, 1),
        }

        for line in file:
            data = line.strip().split()
            direction, distance = data[0], int(data[1])

            for _ in range(distance):
                move = moves[direction]

                head_pos = knots[0]
                head_pos.x += move[0]
                head_pos.y += move[1]

                for i in range(len(knots) - 1):
                    _head = knots[i]
                    _tail = knots[i + 1]

                    move_h = _head.x - _tail.x
                    move_v = _head.y - _tail.y

                    if abs(move_h) > 1 and abs(move_v) > 1:
                        _tail.x += move_h // 2
                        _tail.y += move_v // 2

                    elif abs(move_h) > 1:
                        _tail.x += move_h // 2
                        _tail.y = _head.y

                    elif abs(move_v) > 1:
                        _tail.y += move_v // 2
                        _tail.x = _head.x

                    visited_locations.add(Position(knots[9].x, knots[9].y))

    return len(visited_locations)


if __name__ == "__main__":
    times = 100
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=times)/(times) * 1000} ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=times)/(times) * 1000} ms'
    )
