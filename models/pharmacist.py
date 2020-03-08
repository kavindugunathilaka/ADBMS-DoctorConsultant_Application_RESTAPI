


class Pharmacist:

    def __init__(self, pharmacist_id, first_name, last_name, mobile_number, email_address, username ):
        self.pharmacist_id = pharmacist_id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.mobile_number = mobile_number,
        self.email_address = email_address,
        self.username = username

    @property
    def data(self):
        return {
            'pharmacist_id': self.pharmacist_id[0],
            'first_name': self.first_name[0],
            'last_name': self.last_name[0],
            'mobile_number': self.mobile_number[0],
            'email_address': self.email_address[0],
            'username': self.username
        }