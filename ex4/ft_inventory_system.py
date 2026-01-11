players = {
    "Alice":
    {
        "sword":
        {
            "type": "weapon",
            "rarity": "rare",
            "quantities": 1,
            "value": 500
        },
        "potion":
        {
            "type": "consumable",
            "rarity": "common",
            "quantities": 5,
            "value": 50
        },
        "shield":
        {
            "type": "armor",
            "rarity": "uncommon",
            "quantities": 1,
            "value": 200
        }
    },
    "Bob":
    {
        "magic_ring":
        {
            "type": "weapon",
            "rarity": "rare",
            "quantities": 1,
            "value": 700
        }
    }
}
print("=== Player Inventory System ===")
print()
print("=== Alice's Inventory ===")

for item in players["Alice"]:
    quantities = players['Alice'][item]['quantities']
    value = players['Alice'][item]['value']
    print(
        f"{item} ({players['Alice'][item]['type']}, "
        f"{players['Alice'][item]['rarity']}): "
        f"{players['Alice'][item]['quantities']}x @ "
        f"{players['Alice'][item]['value']} "
        f"gold each = {quantities * value} gold "
    )
print()
total_value = 0
for item in players["Alice"]:
    quantities = players['Alice'][item]['quantities']
    value = players['Alice'][item]['value']
    total_value += quantities * value
print(f"Inventory value: {total_value} gold")
item_count = 0
for item in players["Alice"]:
    item_count += players['Alice'][item]['quantities']
print(f"Item count: {item_count} items")

print("Categories: ", end="")

sword = players["Alice"]["sword"]["quantities"]
potion = players["Alice"]["potion"]["quantities"]
shield = players["Alice"]["shield"]["quantities"]
print(f"Categories: weapon({sword}), consumable({potion}), armor({shield})")

print("\n=== Transaction: Alice gives Bob 2 potions ===")
print("Transaction successful!")

print()
print("=== Updated Inventories ===")
to_give = 2
players["Alice"]["potion"]["quantities"] -= to_give
alice_potion = players["Alice"].get("potion")
bob_potion = {
    "type": alice_potion["type"],
    "rarity": alice_potion["rarity"],
    "quantities": to_give,
    "value": alice_potion["value"]
}

bob_potion["quantities"] = to_give
players["Bob"]["potion"] = {}

players["Bob"]["potion"].update(bob_potion)
print(f"Alice potions: {players['Alice']['potion']['quantities']}")
print(f"Bob potions: {players['Bob']['potion']['quantities']}")

print("\n=== Inventory Analytics ===")

alice_gold = 0
bob_gold = 0
for item in players["Alice"]:
    quantities = players['Alice'][item]['quantities']
    value = players['Alice'][item]['value']
    alice_gold += quantities * value
for item in players["Bob"]:
    quantities = players["Bob"][item]["quantities"]
    value = players["Bob"][item]["value"]
    bob_gold += quantities * value

alice_item = 0
for item in players["Alice"]:
    alice_item += players['Alice'][item]['quantities']
bob_item = 0
for item in players["Bob"]:
    bob_item += players['Bob'][item]['quantities']

if alice_gold > bob_gold:
    high = "Alice"
    high_gold = alice_gold
else:
    high = "Bob"
    high_gold = bob_gold

if alice_item > bob_item:
    high_item = alice_item
    high_player_items = "Alice"
else:
    high_item = bob_item
    high_player_items = "Bob"


print(f"Most valuable player: {high} ({high_gold} gold)")
print(f"Most items player: {high_player_items} ({high_item} items)")

rarest_items = []

for player in players:
    for item in players[player]:
        if players[player][item]["rarity"] == "rare":
            rarest_items.append(item)

print(f"Rarest items: {', '.join(rarest_items)}")
