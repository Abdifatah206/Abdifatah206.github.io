import re
def check_password(password):
    if len(password) < 8:
        return "weak: too short"
    if not re.search("[A-Z]", password):
        return "weak: add uppercase letter"
    if not re.search("[a-z]", password):
        return "weak: add lowercase letter"
    if not re.search("[0-1]", password):
        return  "weak: add number"
    if not re.search("[!@#$%^&*]", password):
        return "weak: add special character"
    return " Strong"
print(check_password("Shire#123"))
