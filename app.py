from flask import Flask 
from flask_restful import Api
from utils.dbconn import connection

from resources.doctor import DoctorListResource, DoctorResource, DoctorSpecializationResource
from resources.patient import PatientListResource, PatientResource, PatientMobileNumberResource
from resources.pharmacist import PharmacistListResource, PharmacistResource
from resources.receptionist import ReceptionistListResource, ReceptionistResource
from resources.appointment import AppointmentListResource, AppointmentResource, AppointmentsDoctorResource, AppointmentPatientResource, AppointmentRecepResource, AppointmentStatusResource

from resources.user_account import UserAccountRegResource, UserVerResource
from resources.consultant_datetime import ConsultantDateTimeListResource, ConsultantDateTimeResource, ConsultStatusResource
from resources.doctor_consult_details import DoctorConsultDetailsResource
from resources.patient_medical_records import PatientMedicalRecordsResource
from resources.medical_records import MedicalRecordsResource
from resources.symptons_records import SymptomsRecordsResource, SymptomsRecordsMedicalResource
from resources.medicaiton_record import MedicationRecordsListResource, MedicationRecordResource

from resources.predict import PredictResource

app = Flask(__name__)
api = Api(app)


api.add_resource(DoctorListResource, '/doctors')
api.add_resource(DoctorResource, '/doctors/<int:doctor_id>')
api.add_resource(DoctorSpecializationResource, '/doctors/<string:specialization>')

api.add_resource(PatientListResource, '/patients' )
api.add_resource(PatientResource, '/patients/<int:patient_id>' )
api.add_resource(PatientMobileNumberResource, '/patients/<int:mobile_number>')

api.add_resource(PharmacistListResource, '/pharmacists')
api.add_resource(PharmacistResource, '/pharmacists/<int:pharmacist_id>')

api.add_resource(ReceptionistListResource, '/receptionists')
api.add_resource(ReceptionistResource, '/receptionists/<int:receptionist_id>')

api.add_resource(AppointmentListResource, '/appointments/')
api.add_resource(AppointmentResource, '/appointment/<int:appointment_id>')
api.add_resource(AppointmentsDoctorResource, '/appointments/<int:zdoctor_id>')
api.add_resource(AppointmentPatientResource, '/appointments/<int:patient_id>')
api.add_resource(AppointmentRecepResource, '/appointments/<int:appointment_id>/<int:receptionist_id>')
api.add_resource(AppointmentStatusResource, '/appointments/<string:status>')

api.add_resource(UserAccountRegResource, '/userReg')
api.add_resource(UserVerResource, '/userVerification')

api.add_resource(ConsultantDateTimeListResource, '/consultantDateTime')
api.add_resource(ConsultantDateTimeResource, '/consultantDateTime/<int:consult_id>')
api.add_resource(ConsultStatusResource, '/consultantDateTime/<string:status>')

api.add_resource(DoctorConsultDetailsResource, '/doctorConsultDetails/<int:doctor_id>')

api.add_resource(PatientMedicalRecordsResource, '/patientMedicalRecords/<int:patient_id>')

api.add_resource(MedicalRecordsResource, '/medicalRecords/<int:medical_record_id>')

api.add_resource(SymptomsRecordsResource, '/symptomsRecords')
api.add_resource(SymptomsRecordsMedicalResource, '/symptomsRecords/<int:medical_record_id>')

api.add_resource(MedicationRecordsListResource, '/medicationRecords')
api.add_resource(MedicationRecordResource, '/medicationRecords/<int:med_record_id>')

api.add_resource(PredictResource, '/predict')
if __name__ == "__main__":
    # app.run(port=5000, debug=False, host='0.0.0.0')
    try:
        app.run(port=5000, debug=True)
    except e:
        print(str(e))
    finally:
        connection.close()