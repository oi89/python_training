from sys import maxsize


class Contact:
    def __init__(self,
                 firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None,
                 address2=None, phone2=None, notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return f"{self.id}: {self.firstname} {self.lastname}"

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
            and (self.firstname == other.firstname or self.firstname is None or other.firstname is None) \
            and (self.lastname == other.lastname or self.lastname is None or other.lastname is None)

    # функция для сортировки списков, возвращает либо id, либо очень большой идентификатор
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
