import re
import math
import random
import string

common_passwords = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome"
]


def calculate_entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26

    if re.search(r"[A-Z]", password):
        pool += 26

    if re.search(r"\d", password):
        pool += 10

    if re.search(r"[^A-Za-z0-9]", password):
        pool += 32

    if pool == 0:
        return 0

    return round(len(password) * math.log2(pool), 2)


def analyze_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Increase length to at least 8")

    if len(password) >= 12:
        score += 20

    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"\d", password))
    special = bool(re.search(r"[^A-Za-z0-9]", password))

    if upper:
        score += 15
    else:
        suggestions.append("Add uppercase letters")

    if lower:
        score += 15
    else:
        suggestions.append("Add lowercase letters")

    if digit:
        score += 15
    else:
        suggestions.append("Add numbers")

    if special:
        score += 15
    else:
        suggestions.append("Add special characters")

    if password.lower() in common_passwords:
        score -= 30
        suggestions.append("Avoid common passwords")

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    entropy = calculate_entropy(password)

    return score, strength, entropy, suggestions


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(14))
