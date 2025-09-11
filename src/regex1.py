import re

def is_valid_email(email):
    # Regex pattern as defined above
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def valid_chars_check(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if (regex.search(string) == None):
      return True
    else:
        return False

emails = ["simple@example.com","very.common@example.com",
"FirstName.LastName@EasierReading.org","example@s.example",
        "long.email-address-with-hyphens@and.subdomains.example.com",
          "postmaster@[123.123.123.123]","user%example.com@example.org",
          '"john..doe"@example.org',"mailhost!username@example.org"]

for email in emails:
    is_valid = is_valid_email(email)
    print (f"{email:<45}  => {is_valid}" )

string = "Geeks$For$Geeks"
print ("****************")
# calling run function
val = valid_chars_check(string)
print(f"{string:>30} --> {val}")