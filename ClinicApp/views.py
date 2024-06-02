
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment

# Create your views here.

def home(request):
    return render(request,'ClinicApp/home.html')

def register(request):
    return render(request,'ClinicApp/register.html')


def patient_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact_number = request.POST['contact_number']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']

        patient = Patient(name=name, contact_number=contact_number,age=age, email=email, password=password)
        patient.save()
        return redirect('login')
    
    return render(request, 'ClinicApp/patient_reg.html')

def doctor_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialization']
        email = request.POST['email']
        password = request.POST['password']

        doctor = Doctor(name=name, specialization=specialization, email=email, password=password)
        doctor.save()
        return redirect('login')
    
    return render(request, 'ClinicApp/doc_reg.html')
    


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if the user exists in the Patient model
        patient_query = Patient.objects.filter(email=email, password=password)
        if patient_query.exists():
            patient = patient_query.first()
            request.session['user_id'] = patient.id
            request.session['user_type'] = 'patient'
            return redirect('patient_dashboard')

        # Check if the user exists in the Doctor model
        doctor_query = Doctor.objects.filter(email=email, password=password)
        if doctor_query.exists():
            doctor = doctor_query.first()
            request.session['user_id'] = doctor.id
            request.session['user_type'] = 'doctor'
            return redirect('doctor_dashboard')

        # Invalid credentials
    return render(request, 'ClinicApp/login.html', {'error': 'Invalid email or password.'})
    
def doctor_dashboard(request):
    if 'user_id' in request.session and request.session['user_type'] == 'doctor':
        doctor = Doctor.objects.get(id=request.session['user_id'])
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'ClinicApp/doctor_dashboard.html', {'doctor': doctor, 'appointments': appointments})
       


def patient_dashboard(request):
    if 'user_id' in request.session and request.session['user_type'] == 'patient':
        patient = Patient.objects.get(id=request.session['user_id'])
        appointments = Appointment.objects.filter(patient=patient)
        return render(request, 'ClinicApp/patient_dashboard.html', {'patient': patient, 'appointments': appointments})
    else:
        return redirect('login')
    
def book_appointment(request):
    if request.method == 'POST' and 'user_id' in request.session and request.session['user_type'] == 'patient':
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        patient_id = request.POST['patient_id']  # it will be in hidden input

        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)  # Fetch the patient based on the ID

        appointment = Appointment(doctor=doctor, patient=patient, date=date, time=time)
        appointment.save()

        return redirect('patient_dashboard')
    
    doc_details = Doctor.objects.all()
    d = {'doc_details' : doc_details}
    return render(request,'ClinicApp/book_appoint.html',d)


def doc_pers_details(request):
    doctor = Doctor.objects.get(id=request.session['user_id'])
    d = {'doctor':doctor}
    return render(request,'ClinicApp/doc_pers_details.html',d)

    







