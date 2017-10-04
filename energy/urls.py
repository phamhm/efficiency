from django.conf.urls import url
from .views import EnergyCaptureFormView

urlpatterns = [
    url(r'^$', EnergyCaptureFormView.as_view(), name='energy-capture-list'),

    url(r'^capture/$',
        EnergyCaptureFormView.as_view(),
        name='energy-capture-form'),
]
