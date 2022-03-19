from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from vacancies.models import Specialty, Company, Vacancy
        from vacancies.data.data import specialties, companies, jobs

        Specialty.objects.all().delete()
        Company.objects.all().delete()
        Vacancy.objects.all().delete()

        for specialty in specialties:
            _ = Specialty.objects.create(**specialty)

        for company in companies:
            _ = Company.objects.create(
                name=company['title'],
                location=company['location'],
                logo=company['logo'],
                description=company['description'],
                employee_count=int(company['employee_count']),
            )

        for job in jobs:
            _ = Vacancy.objects.create(
                title=job['title'],
                specialty=Specialty.objects.get(code=job['specialty']),
                company=Company.objects.get(id=int(job['company'])),
                skills=job['skills'],
                description=job['description'],
                salary_min=float(job['salary_from']),
                salary_max=float(job['salary_to']),
                published_at=job['posted'],
            )
