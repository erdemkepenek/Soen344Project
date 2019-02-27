from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
<<<<<<< HEAD
=======
from resources.registerRoute import UserRegister
from resources.identifyRoute import Login, Logout
from resources.patientRoute import PatientMake, PatientUpdate, PatientCheck, PatientCancel
from resources.nurseRoute import NurseBook, NurseUpdate, NurseCancel, NurseCheckAll
from resources.doctorRoute import DoctorUpdate
#
# from resources.Category import CategoryResource
# from resources.Comment import CommentResource
>>>>>>> de3f8ea627aff3ef7c5cb745267afaa2e810bfce
from resources.Patient import PatientResource
from resources.Doctor import DoctorResource
from resources.Nurse import NurseResource
from resources.Appointment import AppointmentResource
from resources.Availability import AvailabilityResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/Hello')
api.add_resource(PatientResource, '/Patient')
api.add_resource(DoctorResource, '/Doctor')
api.add_resource(NurseResource, '/Nurse')
api.add_resource(AppointmentResource, '/Appointment')
api.add_resource(AvailabilityResource, '/Availability')