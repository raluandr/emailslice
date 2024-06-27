import re
from prettytable import PrettyTable

email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_email(email):
    """Validate the email address using regular expressions."""
    return re.match(email_pattern, email) is not None

def email_slicer(email):
    """Slice the email address into username and domain."""
    username, domain = email.split('@')
    return username, domain

def main():
  
    email_input = input("Please enter your email addresses (comma-separated): ")
    email_list = [email.strip() for email in email_input.split(',')]
    table = PrettyTable()
    table.field_names = ["Email Address", "Username", "Domain", "Valid"]
    for email in email_list:
        if validate_email(email):
            try:
                username, domain = email_slicer(email)
                table.add_row([email, username, domain, "Yes"])
            except ValueError:
                table.add_row([email, "", "", "Invalid format"])
        else:
            table.add_row([email, "", "", "Invalid format"])
    
  
    print(table)

if __name__ == "__main__":
    main()
