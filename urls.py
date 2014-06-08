from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from apps.hearmecode.views import HomeView, AboutView, ClassesView, TestimonialView, WelcomeView

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
    url(r'^class/$', ClassesView.as_view()),
    url(r'^about/$', AboutView.as_view()),
    url(r'^testimonials/$', TestimonialView.as_view()),
)
