from Model import db, Doctor, DoctorSchema, Nurse, NurseSchema, Patient, PatientSchema, Availability, Appointment, AppointmentSchema, AvailabilitySchema, Clinics, ClinicsSchema
from classes.AccountAdapter import AccountAdapter
from classes.AppointmentFacade import AppointmentFacade
from classes.AvailabilityFacade import AvailabilityFacade
from classes.PatientFacade import PatientFacade
from classes.NurseFacade import NurseFacade
from classes.DoctorFacade import DoctorFacade
from classes.ClinicsFacade import ClinicsFacade

# doctor schema
doctors_schema = DoctorSchema(many=True)
doctor_schema = DoctorSchema()
# nurse schema
nurses_schema = NurseSchema(many=True)
nurse_schema = NurseSchema()
# Patient schema
patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()
#availiblility schema
availabilityies_schema = AvailabilitySchema(many=True)
availability_schema = AvailabilitySchema()
#appointment schema
appointments_schema = AppointmentSchema(many=True)
appointment_schema = AppointmentSchema()
#Clinics schema
clinics_schema = ClinicsSchema(many=True)
clinic_schema = ClinicsSchema()




# follow the singleton patter https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class DatabaseFacade():
    instance = None
    db = None
    appointmentFacade = None
    availabilityFacade = None
    patientFacade = None
    nurseFacade = None
    doctorFacade = None

    def __init__(self, db):
        if DatabaseFacade.instance != None:
            raise Exception("DatabaseFacade is a singleton")
        else:
            DatabaseFacade.db = db
            DatabaseFacade.instance = self

    # Singleton pattern for DatabaseFacade
    def getInstance(db):
        if (DatabaseFacade.instance == None):
            DatabaseFacade(db)
            DatabaseFacade.appointmentFacade = AppointmentFacade.getInstance(DatabaseFacade.db)
            DatabaseFacade.availabilityFacade = AvailabilityFacade.getInstance(DatabaseFacade.db)
            DatabaseFacade.patientFacade = PatientFacade.getInstance(DatabaseFacade.db)
            DatabaseFacade.nurseFacade = NurseFacade.getInstance(DatabaseFacade.db)
            DatabaseFacade.doctorFacade = DoctorFacade.getInstance(DatabaseFacade.db)
            DatabaseFacade.clinicsFacade = ClinicsFacade.getInstance(DatabaseFacade.db)
        return DatabaseFacade.instance

    def getAll(self, objectType):
        if objectType == "Appointment":
            return DatabaseFacade.appointmentFacade.getAll()
        elif objectType == "Availability":
            return DatabaseFacade.availabilityFacade.getAll()
        elif objectType == "Patient":
            return DatabaseFacade.patientFacade.getAll()
        elif objectType == "Nurse":
            return DatabaseFacade.nurseFacade.getAll()
        elif objectType == "Doctor":
            return DatabaseFacade.doctorFacade.getAll()
        elif objectType == "Clinics":
            return DatabaseFacade.clinicsFacade.getAll()
        else:
            raise Exception("No type " + objectType + " found")

    def getByIdentifier(self, objectType, identifier):
        if objectType == "Appointment":
            return DatabaseFacade.appointmentFacade.getByIdentifier(identifier)
        elif objectType == "Availability":
            return DatabaseFacade.availabilityFacade.getAvailabilityByIdentifier(identifier)
        elif objectType == "Patient":
            return DatabaseFacade.patientFacade.getPatientsByIdentifier(identifier)
        elif objectType == "Nurse":
            return DatabaseFacade.nurseFacade.getNursesByIdentifier(identifier)
        elif objectType == "Doctor":
            return DatabaseFacade.doctorFacade.getDoctorsByIdentifier(identifier)
        else:
            raise Exception("No type " + objectType + " found")

    def register(self, objectType, json_data):
        if objectType == "Appointment":
            return DatabaseFacade.appointmentFacade.register(json_data)
        elif objectType == "Availability":
            return DatabaseFacade.availabilityFacade.register(json_data)
        elif objectType == "Patient":
            return DatabaseFacade.patientFacade.register(json_data)
        elif objectType == "Nurse":
            return DatabaseFacade.nurseFacade.register(json_data)
        elif objectType == "Doctor":
            return DatabaseFacade.doctorFacade.register(json_data)
        else:
            raise Exception("No type " + objectType + " found")

    def update(self, objectType, json_data):
        if objectType == "Appointment":
            return DatabaseFacade.appointmentFacade.update(json_data)
        elif objectType == "Availability":
            return DatabaseFacade.availabilityFacade.update(json_data)
        elif objectType == "Patient":
            return DatabaseFacade.patientFacade.update(json_data)
        elif objectType == "Nurse":
            return DatabaseFacade.nurseFacade.update(json_data)
        elif objectType == "Doctor":
            return DatabaseFacade.doctorFacade.update(json_data)
        else:
            raise Exception("No type " + objectType + " found")

    def remove(self, objectType, json_data):
        if objectType == "Appointment":
            return DatabaseFacade.appointmentFacade.remove(json_data)
        elif objectType == "Availability":
            return DatabaseFacade.availabilityFacade.remove(json_data)
        elif objectType == "Patient":
            return DatabaseFacade.patientFacade.remove(json_data)
        elif objectType == "Nurse":
            return DatabaseFacade.nurseFacade.remove(json_data)
        elif objectType == "Doctor":
            return DatabaseFacade.doctorFacade.remove(json_data)
        else:
            raise Exception("No type " + objectType + " found")

    def login(self, type, email_, password_):
        if type == "Doctor":
            account = Doctor.query.filter_by(email=email_, password=password_).first()
            account = doctor_schema.dump(account).data
        elif type == "Patient":
            account = Patient.query.filter_by(email=email_, password=password_).first()
            account = patient_schema.dump(account).data
        else:
            account = Nurse.query.filter_by(email=email_, password=password_).first()
            account = nurse_schema.dump(account).data
        return account
