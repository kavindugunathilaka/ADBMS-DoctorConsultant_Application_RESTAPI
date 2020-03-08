

class Doctor_patient_consult_details:

    def __init__(self, patient_id, doctor_id ):
        self.patient_id = patient_id ,
        self.doctor_id = doctor_id,

    @property
    def data(self):
        return {
            'patient_id': self.patient_id[0],
            'doctor_id': self.doctor_id[0]
        }