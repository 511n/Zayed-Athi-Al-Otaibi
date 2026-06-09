high_score_board = []

def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Records a player's game results.

    Parameters:
        player (str): Player name.
        *scores: Any number of round scores.
        bonus (int): Optional bonus added to total.
        multiplier (float): Optional multiplier applied at the end.

    Returns:
        (player, rounds, total, status)
    """

    global high_score_board

    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")

    if any(score < 0 for score in scores):
        return (player, 0, 0, "negative score not allowed")

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)

    rank = 1
    for i, (name, score) in enumerate(sorted_board):
        if name == player and score == total:
            rank = i + 1
            break

    status = "high score!" if rank == 1 else f"rank {rank}"

    return (player, rounds, total, status)


# Main Code
print(record_game("Sara", 10, 20, 30))
print(record_game("Ali", 15, 25, bonus=10))
print(record_game("Mona", 40, 20, multiplier=1.5))

print("\nFinal Leaderboard:")
print(sorted(high_score_board, key=lambda x: x[1], reverse=True))