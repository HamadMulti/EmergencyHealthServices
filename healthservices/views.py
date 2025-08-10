from django.shortcuts import render, redirect
# from .models import Patient
# from django.db.models import Count
from django.http import HttpResponse
from django.contrib import messages
from .models import Patient, AmbulanceDriver, AdminStaff
from django.contrib.auth import logout as django_logout
import re
from .models import Patient  
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, redirect

patient_check = False
driver_check = False
admin_check =False
login_email = ''
Patient_profile_image = ''
driver_profile_image = ''
user_location = ''

def is_strong_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[^A-Za-z0-9]', password)
    )

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        location = request.POST.get('location')

        # Check if email already exists in any model
        if (
            Patient.objects.filter(email=email).exists() or
            AmbulanceDriver.objects.filter(email=email).exists() or
            AdminStaff.objects.filter(email=email).exists()
        ):
            return HttpResponse("<script>alert('Email already exists'); window.location.href = '';</script>")

        if not is_strong_password(password):
            return HttpResponse("<script>alert('Password too weak! Must be 8+ characters and include uppercase, lowercase, digit, and special character.'); window.location.href = '';</script>")

        # Create user in appropriate model
        if role == 'patient':
            Patient.objects.create(username=username, email=email, password=password, location=location)
        elif role == 'ambulance':
            AmbulanceDriver.objects.create(username=username, email=email, password=password, location=location)
        elif role == 'admin':
            AdminStaff.objects.create(username=username, email=email, password=password)

        messages.success(request, "Signup successfully!")
        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    global patient_check,driver_check,admin_check,login_email, user_location
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_email = email

        print(f"jis ne login kiya ha oski email ya ha {login_email}..........")

        # Patient check
        if Patient.objects.filter(email=email, password=password).exists():
            patient = Patient.objects.get(email=email, password=password)
            user_location = patient.location
            patient_check = True
            request.session['user_email'] = patient.email
            request.session['user_role'] = 'patient'
            return redirect('home')

        # Ambulance driver check
        if AmbulanceDriver.objects.filter(email=email, password=password).exists():
            driver = AmbulanceDriver.objects.get(email=email, password=password)
            user_location = driver.location
            driver_check = True
            request.session['user_email'] = driver.email
            request.session['user_role'] = 'ambulance'
            return redirect('driver_home_page')

        # Admin check
        if AdminStaff.objects.filter(email=email, password=password).exists():
            admin = AdminStaff.objects.get(email=email, password=password)
            admin_check = True
            request.session['user_email'] = admin.email
            request.session['user_role'] = 'admin'
            return redirect('admin_home_page')

        messages.error(request, "Invalid email or password")
        return redirect('signin')

    return render(request, 'signin.html')



def logout(request):
    global patient_check,driver_check,admin_check,login_email
    django_logout(request)
    admin_check = False
    driver_check = False
    patient_check = False
    login_email = ''
    return redirect('signin')

def home(request):
    global user_location
    ambulance = AmbulanceDriver.objects.filter(location=user_location)
    return render(request, 'home.html', {'ambulance': ambulance})

def about(request):
    global patient_check,driver_check,admin_check
    print(f" patient_check: {patient_check} -- driver_check: {driver_check} -- admin_check: {admin_check}")
    return render(request, 'about.html', {'patient_check': patient_check,
                                          'driver_check': driver_check,
                                          'admin_check': admin_check})

def services(request):
    global patient_check,driver_check,admin_check
    print(f" patient_check: {patient_check} -- driver_check: {driver_check} -- admin_check: {admin_check}")
    return render(request, 'services.html', {'patient_check': patient_check,
                                          'driver_check': driver_check,
                                          'admin_check': admin_check})

def contact(request):
    global patient_check,driver_check,admin_check
    print(f" patient_check: {patient_check} -- driver_check: {driver_check} -- admin_check: {admin_check}")
    return render(request, 'contact.html', {'patient_check': patient_check,
                                          'driver_check': driver_check,
                                          'admin_check': admin_check})

def driver_home_page(request):
    global user_location
    patients_req = Patient.objects.filter(location=user_location)
    return render(request, 'driver_home_page.html', {'patients_req': patients_req})

def admin_home_page(request):
    patient_count = 0
    driver_count = 0
    p_count = Patient.objects.all()
    for p in p_count:
        patient_count += 1
    print(f"patients in database are--------------- {patient_count}")  

    d_count = AmbulanceDriver.objects.all()
    for d in d_count:
        driver_count += 1 
    print(f"patients in database are------------------ {driver_count}")  

    global login_email
    admin_page_data = AdminStaff.objects.all()
    all_drivers = AmbulanceDriver.objects.all()


    print(f"Logged-in email: {login_email}")

    # Try fetching the admin profile using the login email
    try:
        admin = AdminStaff.objects.get(email=login_email)
        admin_profile_image = admin  # pass the full admin object
        print(f"Admin image URL: {admin.image.url if admin.image else 'No image'}")
    except AdminStaff.DoesNotExist:
        admin_profile_image = None
        print("Admin not found with that email.")


    months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    patient_entries = [40, 35, 38, 42, 45, 32]
    ambulance_entries = [5, 6, 7, 8, 6, 9]
    discharged_patients = [30, 28, 32, 35, 38, 20]
    patient_deaths = [1, 10, 2, 5, 3, 5]

    patient_register = patient_count
    driver_register = driver_count

    context = {
        'months': months,
        'patient_entries': patient_entries,
        'ambulance_entries': ambulance_entries,
        'discharged_patients': discharged_patients,
        'patient_deaths': patient_deaths,
        'admin_profile_image': admin_profile_image,
        'admin_page_data': admin_page_data,
        'patient_register':int(float(patient_register)),
        'driver_register':int(float(driver_register)),
        'all_drivers': all_drivers,
    }
    return render(request, 'admin_home_page.html', context)


def toggle_driver_status(request, driver_id):
    driver = get_object_or_404(AmbulanceDriver, id=driver_id)
    driver.is_active = not driver.is_active
    driver.save()
    return redirect('admin_home_page')  

def delete_driver(request, driver_id):
    driver = AmbulanceDriver.objects.get(id=driver_id)
    driver.delete()
    return redirect('admin_home_page')

# def edit_driver(request, driver_id):
#     driver = get_object_or_404(AmbulanceDriver, id=driver_id)

#     if request.method == 'POST':
#         driver.username = request.POST.get('username')
#         driver.email = request.POST.get('email')
#         driver.location = request.POST.get('location')
#         driver.save()
#         return redirect('admin_home_page')

#     return render(request, 'edit_driver.html', {'driver': driver})





def profile_image(request):
    global patient_check,driver_check,admin_check,login_email,Patient_profile_image,driver_profile_image
    print(f" patient_check: {patient_check} -- driver_check: {driver_check} -- admin_check: {admin_check}")
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        # Example: save to patient assuming already logged in
        # user_email = request.session.get('user_email')
        if patient_check:
            patient_image = Patient.objects.get(email=login_email)
            patient_image.image = image
            patient_image.save()
            Patient_profile_image = patient_image
            print(f"this is profile image of patient {Patient_profile_image}")
            return redirect('home')
            # return render(request, 'home.html', {'patient_check': patient_check})  

        elif driver_check:
            driver = AmbulanceDriver.objects.get(email=login_email)
            driver.image = image
            driver.save()
            driver_profile_image = driver
            print(f"this is profile image of driver {driver_profile_image}")
            return redirect('driver_home_page')
            # return render(request, 'driver_home_page.html', {'driver_check': driver_check})  
        elif admin_check:
            admin = AdminStaff.objects.get(email=login_email)
            admin.image = image
            admin.save()
            # return render(request, 'admin_home_page.html', {'admin_check': admin_check})  
            return redirect('admin_home_page')

    return render(request, 'profile_image.html', {'patient_check': patient_check,
                                          'driver_check': driver_check,
                                          'admin_check': admin_check})



def accept_request(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        if not patient.is_accepted:
            patient.is_accepted = True
            patient.save()
            return JsonResponse({'status': 'accepted'})
        else:
            return JsonResponse({'status': 'unavailable'})
    except Patient.DoesNotExist:
        return JsonResponse({'status': 'error'})