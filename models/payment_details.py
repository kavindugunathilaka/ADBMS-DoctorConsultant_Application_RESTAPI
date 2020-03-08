

class Payment_details:

    def __init__(self, payment_record_id, amount, status, payment_date, payment_time, receptionist_id, patient_id ):
        self.payment_record_id = payment_record_id,
        self.amount = amount,
        self.status = status,
        self.payment_date = payment_date,
        self.payment_time = payment_time,
        self.receptionist_id = receptionist_id,
        self.patient_id = patient_id

    @property
    def data(self):
        return {
            'payment_record_id': self.payment_record_id[0],
            'amount': self.amount[0],
            'status': self.status[0],
            'payment_date': self.payment_date[0],
            'payment_time': self.payment_time[0],
            'receptionist_id': self.receptionist_id[0],
            'patient_id': self.patient_id[0]
        }