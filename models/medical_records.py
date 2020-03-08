

class Medical_records:

    def __init__(self, medical_record_id, age, disease, medication ):
        self.medical_record_id = medical_record_id,
        self.age = age,
        self.disease = disease,
        self.medication = medication,
    @property
    def data(self):
        return {
            'appointment_id': self.appointment_id[0],
            'appointment_date': self.appointment_date[0],
            'appointment_time': self.appointment_time[0],
            'status': self.status[0],
        }