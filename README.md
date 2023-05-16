# Password Breach Checker

This Python program checks if a password has been breached using the "Have I Been Pwned" API. It calculates the SHA-1 hash of a password and queries the API to determine if the hash appears in the database of breached passwords.

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## Usage

```shell
$ python main.py [password1] [password2] ...
```

Replace `[password1]`, `[password2]`, etc., with the passwords you want to check for breaches. You can check multiple passwords at once by providing them as separate command-line arguments.
