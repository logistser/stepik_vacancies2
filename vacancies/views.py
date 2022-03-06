from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all()
        context['companies'] = Company.objects.all()
        context['vacancies'] = Vacancy.objects.all()
        return context


class AllVacanciesView(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class SpecialtyVacanciesView(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['specialty'] = Specialty.objects.get(code=self.args[0])
            context['vacancies'] = Vacancy.objects.filter(specialty__code=self.args[0])
        except Specialty.DoesNotExist:
            raise Http404("Извините, но такой специализации нет на сайте.")
        return context


class CompanyView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['company'] = Company.objects.get(id=int(self.args[0]))
            context['vacancies'] = Vacancy.objects.filter(company__id=int(self.args[0]))
        except Company.DoesNotExist:
            raise Http404("Извините, но вакансий этой компании нет у нас на сайте.")
        return context


class VacancyView(TemplateView):
    template_name = "vacancy.html"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['vacancy'] = Vacancy.objects.get(id=int(self.args[0]))
        except Vacancy.DoesNotExist:
            raise Http404("Извините, но вакансии, к которой вы пытаетесь получить доступ, не существует.")
        return context


def custom_handler404(request, exception):
    return render(request, 'page404.html', context={'exception': exception})


def custom_handler500(request, *args, **argv):
    return render(request, 'page500.html', status=500)
