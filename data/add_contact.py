import random
import string

from model.contact import Contact

# constant with test data to debug
constants = [
    Contact(
        firstname="firstname1",
        middlename="middlename1",
        lastname="lastname1",
        nickname="nickname1",
        title="title1",
        company="company1",
        address="address1",
        home="011",
        mobile="022",
        work="033",
        fax="044",
        email="a@a.ru",
        email2="b@b.com",
        email3="c@c.net",
        homepage="homepage1",
        bday="1",
        bmonth="January",
        byear="1990",
        aday="12",
        amonth="February",
        ayear="2000",
        address2="address2",
        phone2="055",
        notes="notes1"
    )
]


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
    for i in range(2)
]
