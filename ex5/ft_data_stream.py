def infinit_fib():
    i1 = 0
    i2 = 1

    while True:
        yield i1
        tmp = i1
        i1 = i2
        i2 = i2 + tmp


def infinit_primes():
    i = 0
    prime = 2
    while True:
        i = 2
        while i < prime:
            if prime % i == 0:
                prime += 1
                i = 2
            i += 1
        yield prime
        prime += 1


def event_generator(n: int):
    print(f"\nProcessing {n} game events...\n")
    lst = [
        "charlie (level 8) leveled up",
        "alice (level 5) killed monster",
        "bob (level 12) found treasure"
    ]

    for i in range(n):
        yield lst[i % len(lst)]


print("=== Game Data Stream Processor ===")

events_count = 1000
events = event_generator(events_count)

total_events = 0
treasure_events = 0
level_up_events = 0
high_level_players = 0

for event in events:
    total_events += 1

    if "found treasure" in event:
        treasure_events += 1

    if "leveled up" in event:
        level_up_events += 1

    if "(level 1" in event or "(level 12" in event:
        high_level_players += 1

    if total_events <= 3:
        print(f"Event {total_events}: Player {event}")

print("\n...\n")


print("=== Stream Analytics ===")
print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")
print("Memory usage: Constant (streaming)")
print("Processing time: constant per event")

print()
print("=== Generator Demonstration ===")

print("Fibonacci sequence (first 10): ", end='')
fibooo = infinit_fib()
for i in range(10):
    print(f"{next(fibooo)}, ", end="")
print()

print("Prime numbers (first 5): ", end='')
prime = infinit_primes()
for i in range(5):
    print(f"{next(prime)}, ", end="")
print()
