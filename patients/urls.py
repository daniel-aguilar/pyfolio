from django.conf.urls import url

from .views import (Index, PatientCreate, PatientDelete, PatientDetail,
                    PatientList, PatientUpdate)

app_name = 'patients'
urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^patients$', PatientList.as_view(), name="patient-list"),
    url(r'^patients/(?P<pk>\d+)$', PatientDetail.as_view(), name="patient-detail"),
    url(r'^patients/create$', PatientCreate.as_view(), name="patient-create"),
    url(r'^patients/update/(?P<pk>\d+)$', PatientUpdate.as_view(), name="patient-update"),
    url(r'^patients/delete/(?P<pk>\d+)$', PatientDelete.as_view(), name="patient-delete"),
]
