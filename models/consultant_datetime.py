

class Consultant_datetime:

    def __init__(self, consult_id, consult_date, consult_time, status, receptionist_id ):
        self.consult_id = consult_id,
        self.consult_date = consult_date,
        self.consult_time = consult_time,
        self.status = status,
        self.receptionist_id = receptionist_id
        

    @property
    def data(self):
        return {
            'consult_id' : self.consult_id[0],
            'consult_date' : self.consult_date[0],
            'consult_time' : self.consult_time[0],
            'status' : self.status[0],
            'receptionist_id' : self.receptionist_id[0]
        }