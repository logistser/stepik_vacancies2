from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=16)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self) -> str:
        return f'{self.title}'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=16)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=2048)
    employee_count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name.title()}'


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()

    def __str__(self) -> str:
        return f'{self.title} в {self.company} (от {self.salary_min} до {self.salary_max} руб.)'
