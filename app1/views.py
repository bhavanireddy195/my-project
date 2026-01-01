from django.shortcuts import render
from django.db.models import Q
from .models import Profile


def home(request):
    results = None

    if request.method == "POST":
        role = request.POST.get("role", "").strip().lower()
        query = request.POST.get("specialization", "").strip().lower()

        # AI keyword mapping
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

        # Normalize query using AI mapping
        for key, value in AI_MAP.items():
            if key in query:
                query = value
                break

        queryset = Profile.objects.all()

        # Apply role filter ONLY if role exists
        if role:
            queryset = queryset.filter(role__iexact=role)

        # Apply search filter ONLY if query exists
        if query:
            queryset = queryset.filter(
                Q(specialization__icontains=query) |
                Q(details__icontains=query)
            )

        results = queryset

    return render(request, "app1/home.html", {
        "results": results
    })