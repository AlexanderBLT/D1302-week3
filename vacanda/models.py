from django.db.models import Model, CharField, IntegerField, DateField, TextField, URLField, ForeignKey, CASCADE


class Company(Model):
    name = CharField(max_length=64)
    location = CharField(max_length=64)
    logo = URLField(default='https://place-hold.it/100x60')
    description = TextField()
    employee_count = IntegerField()

    def __str__(self):
        return '%s %s' % (self.name, self.location)


class Specialty(Model):
    code = CharField(max_length=32)
    title = CharField(max_length=64)
    picture = URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return '%s %s' % (self.code, self.title)


class Vacancy(Model):
    title = CharField(max_length=64)
    specialty = ForeignKey(Specialty, on_delete=CASCADE, related_name='vacancies')
    company = ForeignKey(Company, on_delete=CASCADE, related_name='vacancies')
    skills = TextField()
    description = TextField()
    salary_min = IntegerField()
    salary_max = IntegerField()
    published_at = DateField()

    def __str__(self):
        return '%s' % self.title
