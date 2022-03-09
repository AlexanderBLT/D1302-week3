from django.http import Http404
from django.shortcuts import render
from vacanda.models import Vacancy, Specialty, Company


def main_view(request):
    all_skills = set()
    for vacancy in Vacancy.objects.all():
        for skill in vacancy.skills.split(','):
            all_skills.add(skill)

    specialties = []
    for specialty in Specialty.objects.all():
        specialties.append({
                'title': specialty.title,
                'specialties_count': Vacancy.objects.filter(specialty__title=specialty.title).count(),
                'code': specialty.code,
        })

    companies = []
    for company in Company.objects.all():
        companies.append({
                'id': company.id,
                'logo': company.logo,
                'vacancies_count': Vacancy.objects.filter(company__name=company.name).count(),
        })

    return render(request, 'vacanda/main.html', context={
                                                 'skills': all_skills,
                                                 'specialties': specialties,
                                                 'companies': companies,
                                                         })


def all_vacancies_view(request):
    all_vacancies_count = Vacancy.objects.count()
    vacancies_info = []
    for vacancy in Vacancy.objects.all():
        vacancies_info.append({
             'id': vacancy.id,
             'title': vacancy.title,
             'skills': vacancy.skills.replace(',', ' •'),
             'salary_min': vacancy.salary_min,
             'salary_max': vacancy.salary_max,
             'published_at': vacancy.published_at,
        })

    return render(request, 'vacanda/vacancies.html', context={
                                                      'all_vacancies_count': all_vacancies_count,
                                                      'vacancies_info': vacancies_info,
                                                              })


def specialty_view(request, specialty):
    if specialty not in [specialty.code for specialty in Specialty.objects.all()]:
        raise Http404

    specialty_title = Specialty.objects.get(code=specialty).title
    specialty_vacancies_count = Vacancy.objects.filter(specialty__code=specialty).count()
    vacancies_info = []
    for vacancy in Vacancy.objects.filter(specialty__code=specialty):
        vacancies_info.append({
            'id': vacancy.id,
            'title': vacancy.title,
            'skills': vacancy.skills.replace(',', ' •'),
            'salary_min': vacancy.salary_min,
            'salary_max': vacancy.salary_max,
            'published_at': vacancy.published_at,
        })

    return render(request, 'vacanda/specialties.html', context={
                                                        'specialty_title': specialty_title,
                                                        'specialty_vacancies_count': specialty_vacancies_count,
                                                        'vacancies_info': vacancies_info,
                                                                })


def company_view(request, company_id):
    if company_id not in [company.id for company in Company.objects.all()]:
        raise Http404

    chosen_company = Company.objects.get(id=company_id)
    chosen_company_info = {
            'name': chosen_company.name,
            'location': chosen_company.location,
            'logo': chosen_company.logo,
            'description': chosen_company.description,
            'vacancies_count': Vacancy.objects.filter(company__id=company_id).count(),
    }

    vacancies_info = []
    for vacancy in Vacancy.objects.filter(company__id=company_id):
        vacancies_info.append({
            'id': vacancy.id,
            'title': vacancy.title,
            'skills': vacancy.skills.replace(',', ' •'),
            'salary_min': vacancy.salary_min,
            'salary_max': vacancy.salary_max,
            'published_at': vacancy.published_at,
        })

    return render(request, 'vacanda/company.html', context={
                                                    'chosen_company_info': chosen_company_info,
                                                    'vacancies_info': vacancies_info,
                                                            })


def vacancy_view(request, vacancy_id):
    if vacancy_id not in [vacancy.id for vacancy in Vacancy.objects.all()]:
        raise Http404

    chosen_vacancy = Vacancy.objects.get(id=vacancy_id)
    chosen_vacancy_info = {
            'title': chosen_vacancy.title,
            'skills': chosen_vacancy.skills.replace(',', ' •'),
            'salary_min': chosen_vacancy.salary_min,
            'salary_max': chosen_vacancy.salary_max,
            'published_at': chosen_vacancy.published_at,
            'company': chosen_vacancy.company,
            'description': chosen_vacancy.description,
    }

    return render(request, 'vacanda/vacancy.html', context={
                                                    'chosen_vacancy_info': chosen_vacancy_info,
                                                            })
