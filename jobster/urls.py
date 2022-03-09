from django.contrib import admin
from django.urls import path
from jobster.error_handlers import custom_handler400, custom_handler403, custom_handler404, custom_handler500
import vacanda.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vacanda.views.main_view, name='main'),
    path('vacancies/', vacanda.views.all_vacancies_view, name='all_vacancies'),
    path('vacancies/<int:vacancy_id>', vacanda.views.vacancy_view, name='vacancy'),
    path('vacancies/cat/<str:specialty>', vacanda.views.specialty_view, name='specialty'),
    path('companies/<int:company_id>', vacanda.views.company_view, name='company'),
]

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500
