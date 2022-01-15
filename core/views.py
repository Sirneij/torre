from django.http import JsonResponse
from django.shortcuts import render

from .models import Person
from .tasks import get_person_and_save


def index(request):
    username = request.GET.get('search')
    if username:
        if Person.objects.filter(username=username).exists():
            person = Person.objects.filter(username=username).first()
        else:
            person = Person.objects.filter(id=get_person_and_save.delay(username))
    else:
        person = Person.objects.filter().first()
    recom: int = 0
    person_skills = {}
    if person:
        if person.skills:
            recom = sum([p['recommendations'] for p in person.skills])

        for skill in person.skills:
            if skill:
                person_skills.setdefault(skill['proficiency'].replace('-', ''), []).append(skill)
        list(person_skills.values())
    context: dict = {
        "person": person,
        "person_skills": person_skills,
        "recom": recom,
    }
    return render(request, "core/index.html", context)
