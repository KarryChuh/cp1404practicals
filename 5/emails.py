def main():
    email_to_name = {}
    email = input("Enter the email address: ")
    while email != "":
        name = name_in_email(email)
        correct = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if correct not in ("", "y", "yes"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ")
    print("\nStored email and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")
def name_in_email(email):
    """Extracts a name from the given email."""
    email_name = email.split('@')[0]
    parts = email_name.split('.')
    name = " ".join(parts).title()
    return name

main()
