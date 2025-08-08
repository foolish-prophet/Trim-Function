"""
dictionary of key value pairs where the values have leading or trailing spaces

iterate through the dictionary checking for spaces in the values

return dictionary with values no longer containing spaces before or after

"""

# strip function identical to built in python strip() method for study
def my_strip(mr_string):
    start = 0
    end = len(mr_string) - 1

    while start <= end and mr_string[start].isspace():
        start += 1
    while end >= start and mr_string[end].isspace():
        end -= 1

    return mr_string[start:end + 1]

### below is a function for trimming a dictionary using long form instead of ternary conditional expressions
""" 
def trim_function(my_dict):
    trimmed_dict = {}

    for key, value in my_dict.items():
        # strip keys, in this case, usernames
         # ternary conditional expression - new_key = my_strip(key) if isinstance(key, str) else key
        if isinstance(key, str):
            new_key = my_strip(key)
        else:
            new_key = key

        # strip values, in this case, first names of users
        # ternary conditional expression - new_value = my_strip(value) if isinstance(value, str) else value
        if isinstance(value, str):
           new_value = my_strip(value)
        else:
            new_value = value
        
        trimmed_dict[new_key] = new_value

    return trimmed_dict
"""
##############################################################################################################

# trim function for dictionaries using ternary conditional expressions
def trim_function(my_dict):
    trimmed_dict = {}

    for key, value in my_dict.items():
        new_key = my_strip(key) if isinstance(key, str) else key
        new_value = my_strip(value) if isinstance(value, str) else value
        trimmed_dict[new_key] = new_value

    return trimmed_dict


# get usernames and corresponding first names from user
def get_users():
    user_dict = {}
    num_of_users = int(input("How many users will you have? "))

    for _ in range(num_of_users):
        key = input("Enter username: ")
        value = input("Enter first name of user: ")
        user_dict[key] = value

    return user_dict

def main(): 
    user_info = {"user1" : "   Alexis   ", "user2" : "   Joshua    ",}
    trimmed_dict = trim_function(user_info)
    print(trimmed_dict)

    ### input_users = get_users()
    input_users = trim_function(get_users())
    print(input_users)

if __name__ == "__main__":
    main()