from django.core.management import BaseCommand
from vacanda.models import Company, Vacancy, Specialty
import vacanda.data as data


class Command(BaseCommand):

    def handle(self, *args, **options):
        for company in data.companies:
            Company.objects.create(
                                id=company.get('id'),
                                name=company.get('title'),
                                location=company.get('location'),
                                logo=company.get('logo'),
                                description=company.get('description'),
                                employee_count=company.get('employee_count'),
                                )

        for specialty in data.specialties:
            Specialty.objects.create(
                code=specialty.get('code'),
                title=specialty.get('title'),
                                   )

        for vacancy in data.jobs:
            Vacancy.objects.create(
                                   id=vacancy.get('id'),
                                   title=vacancy.get('title'),
                                   specialty=Specialty.objects.get(code=vacancy.get('specialty')),
                                   company=Company.objects.get(id=int(vacancy.get('company'))),
                                   skills=vacancy.get('skills'),
                                   description=vacancy.get('description'),
                                   salary_min=vacancy.get('salary_from'),
                                   salary_max=vacancy.get('salary_to'),
                                   published_at=vacancy.get('posted'),
                                )
