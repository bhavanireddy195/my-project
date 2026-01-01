from django.shortcuts import render
from django.db.models import Q
from .models import Profile


def home(request):
    results = None

    if request.method == "POST":
        role = request.POST.get("role", "").lower()
        query = request.POST.get("specialization", "").lower()

        # AI keyword mapping (heart -> cardio etc.)
        AI_MAP = {
            "heart": "cardio",
            "cardiac": "cardio",
            "brain": "neuro",
            "teeth": "dent",
            "child": "pediatric",
            "kids": "pediatric",
            "coding": "developer",
            "programming": "developer",
            "accounts": "accountant",
            "finance": "accountant",
        }

        for key, value in AI_MAP.items():
            if key in query:
                query = value
                break

        results = Profile.objects.filter(
            role__icontains=role
        ).filter(
            Q(specialization__icontains=query) |
            Q(details__icontains=query)
        )

    return render(request, "app1/home.html", {"results": results})