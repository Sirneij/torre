import requests
from celery import shared_task

from .models import Person

BASE_API_URL = "https://torre.bio/api/bios"


@shared_task
def get_person_and_save(username: str):
    p = requests.get(f"{BASE_API_URL}/{username}").json()
    if p:
        person, _ = Person.objects.get_or_create(username=username, id=p.get('person').get('id'))
        person.name = p.get('person').get("name", "No name")
        person.professional_headline = p.get('person').get("professionalHeadline", "")
        person.picture = p.get('person').get("picture", "pictureThumbnail")
        person.bio = p.get('person').get("summaryOfBio", "")
        skills_list = []
        if p["strengths"]:
            for skill in p["strengths"]:
                skills_list.append({"id": skill.get("id"), "name": skill.get('name'), "proficiency": skill.get('proficiency'),'recommendations': skill.get('recommendations')})
        person.skills = skills_list  
        person.save()

        return person.id
    
