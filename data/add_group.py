import random
import string

from model.group import Group

# constant with test data to debug
constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    # connect letters, numbers, punctuation symbols and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# create 1 empty group and 5 groups with random names
test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("group_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(5)
]
