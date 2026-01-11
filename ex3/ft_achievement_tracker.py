
print("=== Achievement Tracker System ===")
print()

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {
    'level_10', 'treasure_hunter', 'boss_slayer',
    'speed_demon', 'perfectionist'}

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")
print()

print("=== Achievement Analytics ===")

all_achievement = alice.union(bob, charlie)

print(f"All unique achievements: {all_achievement}")
print(f"Total unique achievements: {len(all_achievement)}")
print()
print(f"Common to all players: {bob.intersection(alice, charlie)}")


rare = bob.difference(alice, charlie)
rare = rare.union(alice.difference(bob, charlie))
rare = rare.union(charlie.difference(alice, bob))
print(f"Rare achievements (1 player): {rare}")


print()
common = bob.intersection(alice)
print(f"Alice vs Bob common: {common}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
