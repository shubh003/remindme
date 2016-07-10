from django.conf.urls import url

from .views import TemplateView

urlpatterns = [
    url(r'^templates/', TemplateView.as_view())
]