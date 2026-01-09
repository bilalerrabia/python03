import sys

ac = len(sys.argv)
lst =[]
print("=== Player Score Analytics ===")
if ac == 1:
    print("No scores provided. Usage: "
    "python3 ft_score_analytics.py <score1>"
    " <score2> ...")
else:
    for i in range(1, ac):
        try:
            lst.append(int(sys.argv[i]))
        except:
            print("not a number")
            exit(0)

    avrg = sum(lst) / (ac - 1)

    print(f"Scores processed: {lst}")
    print(f"Total players: {ac - 1}")
    print(f"Total score: {sum(lst)}")
    print(f"Average score: {avrg}")
    print(f"High score: {max(lst)}")
    print(f"Low score: {min(lst)}")
    print(f"Score range: {max(lst) - min(lst)}\n")