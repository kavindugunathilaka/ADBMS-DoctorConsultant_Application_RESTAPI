

class Patient_medical_records:

    def __init__(self, patient_id, medical_record_id ):
        self.patient_id = patient_id,
        self.medical_record_id = medical_record_id,

    @property
    def data(self):
        return {
            'patient_id': self.medical_record_id[0],
            'medical_record_id': self.patient_id[0]
        }