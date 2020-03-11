
class Appointment:

    def __init__(self, appointment_id, appointment_date, appointment_time, status, patient_id, doctor_id, receptionist_id=None ):
        self.appointment_id = appointment_id,
        self.appointment_date = appointment_date,
        self.appointment_time = appointment_time,
        self.status = status,
        self.patient_id = patient_id,
        self.doctor_id = doctor_id,
        self.receptionist_id = receptionist_id

    @property
    def data(self):
        return {
            'appointment_id': self.appointment_id[0],
            'appointment_date': self.appointment_date[0],
            'appointment_time': self.appointment_time[0],
            'status': self.status[0],
            'patient_id': self.patient_id[0],
            'doctor_id': self.doctor_id[0],
            'receptionist_id': self.receptionist_id[0]
        }