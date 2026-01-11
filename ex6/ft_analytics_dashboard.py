
print("=== Game Analytics Dashboard ===")
print("\n=== List Comprehension Examples ===")

players = ['alice', 'bob', 'charlie', 'diana']
players_scorers = [2300, 1800, 2150, 2050]
activations = ['active', 'active', 'active', 'not active']

high_scorers_players = [
    player for score, player in zip(players_scorers, players)
    if score > 2000]

scores_doubled = [score * 2 for score in players_scorers]

active_players = [
    player for player, activation in zip(players, activations)
    if activation == "active"]

print(f"High scorers (>2000): {high_scorers_players}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players:{active_players}")

print("\n=== Dict Comprehension Examples ===")
players = {
    'alice': 2300,
    'bob': 1800,
    'charlie': 2150
}
achievements = {
    'alice': ['win', 'kill', 'quest', 'boss', 'treasure'],
    'bob': ['win', 'quest', 'boss'],
    'charlie': ['win', 'kill', 'quest', 'boss', 'treasure', 'level', 'arena']
}

score_categories = {
    'high':   sum(1 for s in players.values() if s >= 1800),
    'medium': sum(1 for s in players.values() if 1800 <= s < 2200),
    'low':    sum(1 for s in players.values() if s <= 1800),
}

achievement_counts = {
    player: len(ach_list)
    for player, ach_list in achievements.items()
}

print(f"Player scores: {players}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts:{achievement_counts}")

print("\n=== Set Comprehension Examples ===")

players_set = {'alice', 'alice', 'bob', 'charlie', 'diana'}
achievements = {
    'first_kill', 'first_kill', 'level_10', 'level_10',
    'boss_slayer'
    }
regions = {'north', 'east', 'central', 1, 4, None}
active_regions = {region for region in regions if isinstance(region, str)}
print(f"Unique players: {players_set}")
print(f"Unique achievements: {achievements}")
print(f"Active regions: {active_regions}")

print("\n=== Combined Analysis ===")

players = ['alice', 'bob', 'charlie', 'diana']
players_scores = [2300, 1800, 2100, 2050]
achievements = [
    'win', 'kill', 'quest', 'boss', 'treasure', 'win',
    'quest', 'boss', 'win', 'kill', 'quest', 'boss',
    'treasure', 'level', 'arena', '8', '9', '10', '11', '12'
    ]
achievements_set = set(achievements)

top_score = max([score for score in players_scores])
top_player = [
    players[i] for i in range(len(players_scores))
    if players_scores[i] == top_score][0]

print(f"Total players: {len(players)}")
print(f"Total unique achievements: {len(achievements_set)}")
print(f"Average score: {sum(players_scores) / len(players_scorers)}")
print(f"Top performer: {top_player} ({top_score} points)")
