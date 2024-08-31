
class GivenUser:

    def __init__(self, first_name, last_name, email, password, company, street, city,
                 state, zipcode, country, phone, method):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.phone = phone
        self.method = method


given_user = GivenUser(
    first_name='Firsty',
    last_name='Lastoff',
    email='Lastoff@gmail.com',
    password='QWErty12345',
    company='Lastoff & Co',
    street='Sunflower Rd',
    city='Woodville',
    state='Texas',
    zipcode='75979',
    country='United States',
    phone='(555)555-5555',
    method='Best Way'
)
