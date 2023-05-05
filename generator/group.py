import random
import string
import os.path
import json
import getopt
import sys

from model.group import Group


# reading options from command line: n - number of groups to generate, f - filename to save generated data
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values
n = 5
f = "/data/groups.json"

for o, a in opts:
    # if name of option is n, then convert it value to int and save to n
    if o == "-n":
        n = int(a)
    # if name of option is f, then save it value to f
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # connect letters, numbers, punctuation symbols and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# create 1 empty group and 5 groups with random names
test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("group_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(n)
]

# combine directory name with ../ and filename from options
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
# open file in write mode
with open(file, "w") as output:
    # json.dumps() converts object to json string
    # default - function for transform Group object to dictionary
    # indent - offset in json structure
    output.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
