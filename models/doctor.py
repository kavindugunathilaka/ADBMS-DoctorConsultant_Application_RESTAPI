

class Doctor:

    def __init__(self, doctor_id, first_name, last_name, username, mobile_number, email_address,resid_address, specialization, qualification ):
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
            'doctor_id': self.doctor_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'mobile_number': self.mobile_number,
            'email_address': self.email_address,
            'specialization': self.specialization,
            'qualification': self.qualification,
            'resid_address': self.resid_address,
            'username': self.username
        }