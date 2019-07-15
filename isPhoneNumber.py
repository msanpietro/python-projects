import re

def isPhoneNumber(text):
     match = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
     if match:
        return True
        # To print the matches use ===> print match.group()
     else:
        return False

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


# To print the matches use ===> print match.group()

