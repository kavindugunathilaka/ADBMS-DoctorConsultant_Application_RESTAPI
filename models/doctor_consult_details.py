

class Doctor_consult_details:

    def __init__(self, consult_id, doctor_id ):
        self.consult_id = consult_id,
        self.doctor_id = doctor_id

    @property
    def data(self):
        return {
            'consult_id': self.consult_id[0],
            'doctor_id': self.doctor_id[0]
        }