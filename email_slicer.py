email = input("Type your email: ").strip()


def email_slicer(email):
    username = email[:email.index("@")]
    domain = email[email.index("@") + 1:]

    print("Your username is {} and domain is {}".format(username, domain))


if __name__ == '__main__':
    email_slicer(email)
