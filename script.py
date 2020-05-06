import requests

r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)


def addition(x, y):
    return int(x) + int(y)


def divide(x, y):
    return x / y


print(addition(2, 5))
