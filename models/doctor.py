

class Doctor:

    def __init__(self, doctor_id, first_name, last_name, mobile_number, email_address, specialization, qualification, resid_address, username ):
        self.doctor_id = doctor_id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.mobile_number = mobile_number,
        self.email_address = email_address,
        self.specialization = specialization,
        self.qualification = qualification,
        self.resid_address = resid_address,
        self.username = username

    @property
    def data(self):
        return {
            'doctor_id': self.doctor_id[0],
            'first_name': self.first_name[0],
            'last_name': self.last_name[0],
            'mobile_number': self.mobile_number[0],
            'email_address': self.email_address[0],
            'specialization': self.specialization[0],
            'qualification': self.qualification[0],
            'resid_address': self.resid_address[0],
            'username': self.username
        }