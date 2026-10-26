tools = ["Linux", "Git", "AWS"]
for tool in tools:
    print("Learning", tool)

for i in range(1, 6):
    print("Day", i)

count = 0
while count < 3:
    print("Count is", count)
    count = count + 1

ports = {"ssh": 22, "http": 80, "https": 443}
for name, port in ports.items():
    if port == 443:
        print(name, "is encrypted")
    else:
        print(name, "is not encrypted")
