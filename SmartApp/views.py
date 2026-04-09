from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import IncidentReport
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 

from django.contrib.auth.decorators import permission_required

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # 1. Make them 'Staff' so they can access protected parts of the app
            user.is_staff = False 
            user.save()

            # 2. Get the "Content Type" for your model
            content_type = ContentType.objects.get_for_model(IncidentReport)

            # 3. Find the specific permissions for ADD and VIEW
            perm_add = Permission.objects.get(codename='add_incidentreport', content_type=content_type)
            perm_view = Permission.objects.get(codename='view_incidentreport', content_type=content_type)

            # 4. Assign these permissions to the user
            user.user_permissions.add(perm_add, perm_view)

            login(request, user)
            messages.success(request, "Account created! You can now view and report issues.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# 1. Main Dynamic Reporting View (Handles Safety, Waste, etc.)

@never_cache
@permission_required('SmartApp.add_incidentreport', raise_exception=True)
def report_view(request, report_type):
    if request.method == "POST":
        # Capture data from the HTML form
        IncidentReport.objects.create(
            report_type=report_type,
            category=request.POST.get('category'),
            urgency=request.POST.get('urgency', 'Medium'),
            description=request.POST.get('description'),
            evidence=request.FILES.get('evidence'),
            latitude=request.POST.get('latitude') or None,
            longitude=request.POST.get('longitude') or None
        )
        messages.success(request, f"{report_type.capitalize()} report submitted!")
        return redirect(f'/{report_type}/')

    # Load only the reports belonging to this page
    recent = IncidentReport.objects.filter(report_type=report_type).order_by('-created_at')[:5]
    return render(request, f'SmartApp/{report_type}.html', {'recent_reports': recent})

# 2. General Complaint View (Fixed naming and logic)
@never_cache
@permission_required('SmartApp.add_incidentreport', raise_exception=True)
def complaint_view(request):
    if request.method == "POST":
        # Using IncidentReport instead of IssueReport
        IncidentReport.objects.create(
            report_type='other', # Or assign a specific type
            category=request.POST.get('category'),
            description=request.POST.get('description'),
            urgency=request.POST.get('priority', 'Medium'),
            status='Pending'
        )
        messages.success(request, "Complaint submitted successfully!")
        return redirect('complaint')

    return render(request, 'SmartApp/complaint.html')

# 3. Page Views
@never_cache
@permission_required('SmartApp.add_incidentreport')
def home_view(request):
    reports = IncidentReport.objects.all().order_by('-created_at')[:10]
    return render(request, 'SmartApp/home.html', {'reports': reports})

@never_cache
@login_required
def water_view(request):
    return report_view(request, 'water')

@never_cache
@login_required
def waste_view(request):
    return report_view(request, 'waste')

@never_cache
@login_required
def safety_view(request):
    return report_view(request, 'safety')

@never_cache
@login_required
def lost_view(request):
    return report_view(request, 'lost')

@never_cache
@login_required
def air_view(request):
    return report_view(request, 'air')

@never_cache
@login_required
def help_support_view(request):
    return render(request, 'SmartApp/helpsupport.html')

@never_cache
@login_required
def about_view(request):
    return render(request, 'SmartApp/about.html')