ports = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}

def lookup(port):
    return ports.get(port, "Unknown")

number = int(input("Enter a port number: "))
print(number, "is", lookup(number))
