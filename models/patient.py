

class Patient:

    def __init__(self, patient_id, first_name, last_name, age, mobile_number, email_address, guardian_name, guardian_mobile ):
        self.patient_id = patient_id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.mobile_number = mobile_number,
        self.email_address = email_address,
        self.guardian_name = guardian_name,
        self.guardian_name = guardian_mobile

    @property
    def data(self):
        return {
            'patient_id': self.patient_id,
            'first_name': self.first_name ,
            'last_name': self.last_name,
            'age': self.age,
            'mobile_number': self.mobile_number,
            'email_address': self.email_address,
            'guardian_name': self.guardian_name,
            'guardian_mobile': self.guardian_mobile
        }