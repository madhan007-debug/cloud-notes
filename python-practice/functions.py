def greet(name):
    return f"Hello, {name}!"

def check_port(port):
    if port == 22:
        return "SSH"
    elif port == 80:
        return "HTTP"
    elif port == 443:
        return "HTTPS"
    else:
        return "Unknown"

print(greet("Cloud learner"))
print(check_port(22))
print(check_port(443))
print(check_port(9999))
