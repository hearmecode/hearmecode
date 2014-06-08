from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# from apps.hearmecode.models import Member, Faq

class HomeView(TemplateView):

    template_name = 'index.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context

class AboutView(TemplateView):

    template_name = 'about.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context

class ClassesView(TemplateView):

    template_name = 'class.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context

class TestimonialView(TemplateView):

    template_name = 'testimonials.html'

    def get(self, request, **kwargs):

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):

        context = {}

        return context

class WelcomeView(TemplateView):

    ' For the welcome package / starter kit '

    pass