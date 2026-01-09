import sys

argc = len(sys.argv)

print("=== Command Quest ===")
if argc == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argc - 1}")
    ac = 1
    while ac < argc:
        print(f"Argument {ac}: {sys.argv[ac]}")
        ac += 1
    
print(f"Total arguments: {argc}")