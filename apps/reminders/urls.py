from django.conf.urls import url

from .views import ReminderView, AlertView

urlpatterns = [
    url(r'^reminder/', ReminderView.as_view()),
    url(r'^alerts/', AlertView.as_view())
]