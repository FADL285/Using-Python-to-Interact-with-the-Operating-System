import re

# Pattern to return which country start and end with a
pattern = r"^a.*a$"

with open('countries.txt') as countries:
  data = countries.read()
  print(type(data))
  # print(data)
  print(re.findall(pattern, data, re.M|re.I))


def variable_name_validator(variable_name):
  pattern = r"^[a-z][\w\d]*$"
  if re.search(pattern, variable_name, re.I):
    print("Valid")
  else:
    print("Invalid")


variable_name_validator("85_val_68")