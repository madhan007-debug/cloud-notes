with open("notes.txt", "w") as f:
    f.write("Day 9 started\n")
    f.write("Learning files\n")

with open("notes.txt", "a") as f:
    f.write("Added a line\n")

with open("notes.txt", "r") as f:
    content = f.read()
print(content)

with open("notes.txt") as f:
    for line in f:
        print("Line:", line.strip())
