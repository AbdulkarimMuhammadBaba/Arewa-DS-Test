import re
def is_valid_variable(variable):
    if re.search(r"^[a-zA-Z_]\w*$", variable):
        return True
    else:
        return False


print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))
