import re


def password_complexity(pwd):

    criteria_patterns = {
        "uppercase": r'[A-Z]',
        "lowercase": r'[a-z]',
        "digit": r'[0-9]',
        "special_characters": r'[!@#$%^&*()\-_+=<>?{}[\]|\\`~]'
    }

    meets_criteria = {
        "uppercase": bool(re.search(criteria_patterns["uppercase"], pwd)),
        "lowercase": bool(re.search(criteria_patterns["lowercase"], pwd)),
        "digit": bool(re.search(criteria_patterns["digit"], pwd)),
        "special_characters": bool(re.search(criteria_patterns["special_characters"], pwd))
    }

    if all(meets_criteria.values()):
        feedback = "Complex ('You're good to go')"
    elif meets_criteria["special_characters"] and (meets_criteria["uppercase"] or meets_criteria["lowercase"]):
        feedback = "Moderate ('Good to go but try something else if you'd like to have a stronger password')"
    else:
        feedback = "Simple ('You're not moving forward without changing this password at least to a Moderate level')"

    return feedback


def has_consecutive_special_characters(pwd):

    return bool(re.search(r'([!@#$%^&*()\-_+=<>?{}[\]|\\`~])\1', pwd))


def get_password():
    while True:
        password = input("Enter your password: ")
        complexity = password_complexity(password)
        if has_consecutive_special_characters(password):
            print("Warning: Consecutive special characters detected. This may reduce password strength.")
        print(f"Password Complexity: {complexity}")
        if complexity == "Complex ('You're good to go')":
            break
        elif complexity == "Moderate ('Good to go but try something else if you'd like to have a stronger password')":

            break
        else:

            print("Please enter a stronger password.")


get_password()
