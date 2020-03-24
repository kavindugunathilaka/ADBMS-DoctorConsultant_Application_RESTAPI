

class Medical_records:

    def __init__(self, medical_record_id, disease, specialization ):
        self.medical_record_id = medical_record_id,
        self.disease = disease,
        self.specialization = specialization


    @property
    def data(self):
        return {
            'medical_record_id': self.medical_record_id[0],
            'disease': self.disease[0],
            'specialization': self.specialization[0]
        }