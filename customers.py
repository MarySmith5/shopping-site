"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):
        """Readable method to show customer info
        in console."""
        return f'<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}'

    
def read_customers_from_file(filepath):
    """Read customer data and populate dictionary
    of customers.
    Dictionary will be {email: Customer object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first_name,
                last_name,
                email,
                password) = line.strip().split('|')

            customers[email] = Customer(first_name,
                                        last_name,
                                        email,
                                        password)

    return customers



def get_by_email(email):
    """Return a customer, given their email"""
    if customers.get(email) != None:
        return customers[email]
    else:
        return False


customers = read_customers_from_file("customers.txt")

