def calculate_elo(rating_a, rating_b, score_a, k_factor=32):
    """
    Calculate new Elo ratings for two players after a game.
    
    :param rating_a: Current rating of player A
    :param rating_b: Current rating of player B
    :param score_a: Score of player A (1 for win, 0.5 for draw, 0 for loss)
    :param k_factor: K-factor for Elo calculation (default 32)
    :return: New ratings for player A and B
    """
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    change = k_factor * (score_a - expected_a)
    new_rating_a = rating_a + change
    new_rating_b = rating_b - change
    return new_rating_a, new_rating_b

# Example scenario
player_a_rating = 1500
player_b_rating = 1700

print(f"初始评分: 玩家A = {player_a_rating}, 玩家B = {player_b_rating}")

# 情景1: 玩家B（较强）击败玩家A（较弱）
new_a, new_b = calculate_elo(player_a_rating, player_b_rating, 0)
print(f"B胜A后: 玩家A = {new_a:.2f}, 玩家B = {new_b:.2f}")

# 情景2: 玩家A（较弱）击败玩家B（较强）
new_a, new_b = calculate_elo(player_a_rating, player_b_rating, 1)
print(f"A胜B后: 玩家A = {new_a:.2f}, 玩家B = {new_b:.2f}")

# 情景3: 平局
new_a, new_b = calculate_elo(player_a_rating, player_b_rating, 0.5)
print(f"平局后: 玩家A = {new_a:.2f}, 玩家B = {new_b:.2f}")