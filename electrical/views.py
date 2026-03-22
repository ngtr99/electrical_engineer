from django.shortcuts import redirect, render, get_object_or_404
from electrical.models import ElectricalData
from electrical.supabase_storage import upload_image_to_supabase


def index(request):
    projects = ElectricalData.objects.all()
    return render(request, "electrical/index.html", {"projects": projects})


def add_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        description = request.POST.get("description")
        picture = request.FILES.get("picture")
        skills = request.POST.get("skills")

        picture_url = None
        if picture:
            picture_url = upload_image_to_supabase(picture)

        ElectricalData.objects.create(
            name=name,
            date=date,
            description=description,
            picture_url=picture_url,
            skills=skills,
        )
        return redirect("index")

    return render(request, "electrical/add_data.html")


def project_detail(request, project_id):
    project = get_object_or_404(ElectricalData, id=project_id)
    return render(request, "electrical/project_detail.html", {"project": project})


def project_edit(request, project_id):
    project = get_object_or_404(ElectricalData, id=project_id)

    if request.method == "POST":
        project.name = request.POST.get("name")
        project.date = request.POST.get("date")
        project.description = request.POST.get("description")
        project.skills = request.POST.get("skills")

        picture = request.FILES.get("picture")
        if picture:
            project.picture_url = upload_image_to_supabase(picture)

        project.save()
        return redirect("project_detail", project_id=project.id)

    return render(request, "electrical/project_edit.html", {"project": project})


def project_delete(request, project_id):
    project = get_object_or_404(ElectricalData, id=project_id)

    if request.method == "POST":
        project.delete()
        return redirect("index")

    return render(request, "electrical/project_delete.html", {"project": project})