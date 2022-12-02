import timeit


def solution_part_1():
    with open("input_data.txt") as file:
        score = 0
        hands = {
            "A": 1,
            "B": 2,
            "C": 3,
            "X": 1,
            "Y": 2,
            "Z": 3,
        }

        beats = [1, 2, 3]

        for line in file:
            data = line.strip().split()

            opponent_move = hands[data[0]]
            player_move = hands[data[1]]

            opponent_move_idx = opponent_move - 1

            # draw
            if player_move == beats[opponent_move_idx]:
                score += 3

            # lose
            elif player_move == beats[opponent_move_idx - 1]:
                score += 0

            # win
            else:
                score += 6

            score += player_move

        return score


def solution_part_2():
    with open("input_data.txt") as file:
        score = 0
        hands = {
            "A": 1,
            "B": 2,
            "C": 3,
        }
        moves = {
            "X": -1,
            "Y": 0,
            "Z": 1,
        }
        beats = [1, 2, 3]

        for line in file:
            data = line.strip().split()

            opponent_move = hands[data[0]]

            expected_move = data[1]
            opponent_move_idx = beats.index(opponent_move)

            # wrap around the list
            player_move = beats[(opponent_move_idx + moves[expected_move]) % len(beats)]

            # draw
            if player_move == beats[opponent_move_idx]:
                score += 3

            # win
            elif player_move == beats[opponent_move_idx - 1]:
                score += 0

            else:
                score += 6

            score += player_move

        return score


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
