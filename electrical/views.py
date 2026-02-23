from django.shortcuts import redirect, render
from electrical.models import ElectricalData

# Create your views here.

def index(request):
    projects = ElectricalData.objects.all()
    return render(request, "electrical/index.html", {"projects": projects})

def add_data(request):
    if request.method == "POST":
        # Handle form submission and save data to the database
        name = request.POST.get('name')
        date = request.POST.get('date')
        description = request.POST.get('description')
        picture = request.FILES.get('picture')
        skills = request.POST.get('skills')

        # Create new ElectricalData instance
        ElectricalData.objects.create(
            name=name,
            date=date,
            description=description,
            picture=picture,
            skills=skills
        )
    return render(request, "electrical/add_data.html")

def project_detail(request, project_id):
    project = ElectricalData.objects.get(id=project_id)
    return render(request, "electrical/project_detail.html", {"project": project})

def project_edit(request, project_id):
    project = ElectricalData.objects.get(id=project_id)
    if request.method == "POST":
        # Handle form submission and update data in the database
        project.name = request.POST.get('name')
        project.date = request.POST.get('date')
        project.description = request.POST.get('description')
        if 'picture' in request.FILES:
            project.picture = request.FILES['picture']
        project.skills = request.POST.get('skills')
        project.save()
    return render(request, "electrical/project_edit.html", {"project": project})    

def project_delete(request, project_id):
    project = ElectricalData.objects.get(id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('index')
    return render(request, "electrical/project_delete.html", {"project": project})  


