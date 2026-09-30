def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must contain between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Check the rules for numbers
    number_started = False

    for character in s:
        if character.isdigit():

            # The first number cannot be zero
            if not number_started and character == "0":
                return False

            number_started = True

        elif number_started:
            # Letters cannot appear after numbers
            return False

    return True


main()
