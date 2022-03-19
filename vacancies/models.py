from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=16)
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self) -> str:
        return f'{self.title}'


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=16)
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=2048)
    employee_count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name.title()}'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=128)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()
    owner = models.OneToOneField(User, on_delete=models.DO_NOTHING,
                                 null=True, primary_key=False, related_name='owner_of')

    def __str__(self) -> str:
        return f'{self.title} в {self.company} (от {self.salary_min} до {self.salary_max} руб.)'


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=15, validators=[MinLengthValidator(11)])
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self) -> str:
        return f'Отклик {self.user.first_name} {self.user.last_name} на {self.vacancy.title}'

