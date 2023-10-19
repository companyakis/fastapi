# newer versions of python (. > Python 3.9)

# int list

ages: list[int] = [43, 33, 10, 7]

# tuple, immutable
# name, age, marital status, country

her_info: tuple[str, int, bool, str] = ("gunay", 33, True, "canada")

# item name and price dictionary

item_info: dict[str, float] = {
    "computer": 15250.4,
    "table": 2000.0,
}

# let's create a list containing int and float values

my_list: list[int | float] = [5, 5.1, 8, 12]

print(my_list)

