import requests
import hashlib
import sys

# usage
# $ python main.py hello willowtree newadventure letmegoitsmytime


def make_request(hash_query):
    url = "https://api.pwnedpasswords.com/range/" + hash_query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again"
        )
    return res


def hash_password(passw: str):
    return hashlib.sha1(passw.encode("utf-8")).hexdigest().upper()


def get_breach(bad_passwords, hashed_password):
    for line in bad_passwords:
        parts = line.split(":")
        hash = parts[0]
        count = int(parts[1])
        if hash in hashed_password:
            return (hash, count)


def check_password(password: str):
    hashed_password = hash_password(password)
    res = make_request(hashed_password[:5])
    bad_passwords = res.text.splitlines()
    breach = get_breach(bad_passwords, hashed_password)

    if breach:
        print(f"WARNING: {password} has been breached {breach[1]} times!")
    else:
        print(f"OK: {password} not breached.")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        check_password(arg)
