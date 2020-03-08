
class Medication_record:

    def __init__(self, med_record_id, prescription, date_prescribed, medication_issued, doctor_id, patient_id, pharmacist_id ):
        self.med_record_id = med_record_id,
        self.prescription = prescription,
        self.date_prescribed = date_prescribed,
        self.medication_issued = medication_issued,
        self.doctor_id = doctor_id,
        self.patient_id = patient_id,
        self.pharmacist_id =pharmacist_id

    @property
    def data(self):
        return {
            'med_record_id': self.med_record_id[0],
            'prescription': self.prescription[0],
            'date_prescribed': self.date_prescribed[0],
            'medication_issued': self.medication_issued[0],
            'doctor_id': self.doctor_id[0],
            'patient_id': self.patient_id[0],
            'pharmacist_id': self.pharmacist_id[0]
        }