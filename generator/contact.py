import random
import string
import os.path
import jsonpickle
import getopt
import sys

from model.contact import Contact


# reading options from command line: n - number of contacts to generate, f - filename to save generated data
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default values
n = 2
f = "data/contacts.json"

for o, a in opts:
    # if name of option is n, then convert it value to int and save to n
    if o == "-n":
        n = int(a)
    # if name of option is f, then save it value to f
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # connect letters, numbers and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    return ''.join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

test_data = [
    Contact(
        firstname=random_string('', 7),
        middlename=random_string('', 7),
        lastname=random_string('', 10),
        nickname=random_string('', 7),
        title=random_string('title', 7),
        company=random_string('company', 10),
        address=random_string('address', 15),
        home=random_numbers(7),
        mobile=random_numbers(10),
        work=random_numbers(10),
        fax=random_numbers(10),
        email=random_string('email', 5),
        email2=random_string('email2', 5),
        email3=random_string('email2', 5),
        homepage=random_string('', 10),
        bday=random.randrange(32),
        bmonth=months[random.randrange(12)],
        byear=random_numbers(5),
        aday=random.randrange(32),
        amonth=months[random.randrange(12)],
        ayear=random_numbers(5),
        address2=random_string('address2', 15),
        phone2=random_numbers(10),
        notes=random_string('notes', 20)
    )
    for i in range(n)
]

# combine directory name with ../ and filename from options
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)
# open file in write mode
with open(file, "w") as output:
    # indent - offset in json structure
    jsonpickle.set_encoder_options("json", indent=2)
    # jsonpickle.encode() converts object to json string
    output.write(jsonpickle.encode(test_data))
