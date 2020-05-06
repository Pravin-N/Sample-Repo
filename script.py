import requests

r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)


def addition(x, y):
    return int(x) + int(y)


print(addition(2, 5))
