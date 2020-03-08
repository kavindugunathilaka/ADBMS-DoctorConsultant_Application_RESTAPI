

class Symptoms_record:

    def __init__(self, medical_record_id, symptom ):
        self.medical_record_id = medical_record_id,
        self.symptom = symptom

    @property
    def data(self):
        return {
            'medical_record_id': self.medical_record_id[0],
            'symptom': self.symptom[0]
        }