from datetime import date

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test.utils import ignore_warnings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from freezegun import freeze_time
from model_bakery import baker

from .models import Patient

# Create your tests here.


USERNAME = 'morty'
USER_PASSWORD = 'password'


@freeze_time('2017-11-25')
class PatientTestCase(TestCase):

    def test_calculate_age(self):
        patient = baker.make(
            Patient,
            date_of_birth=date(1994, 3, 16)
        )
        self.assertEqual(patient.age(), 23)

    def test_invalid_date_of_birth(self):
        patient = baker.make(
            Patient,
            date_of_birth=date(2017, 11, 26)
        )

        with self.assertRaises(ValidationError) as cm:
            patient.full_clean(validate_unique=False)

        the_exception = cm.exception
        self.assertDictEqual(
            the_exception.message_dict,
            {'date_of_birth': [_('Invalid date of birth.')]}
        )


class PatientListApiTestCase(TestCase):
    user = None
    patients = None

    def setUp(self):
        ignore_warnings(message='No directory at', module='whitenoise.base').enable()
        self.user = User.objects.create_user(USERNAME, password=USER_PASSWORD)
        self.client.login(username=USERNAME, password=USER_PASSWORD)

        self.patients = [
            baker.make(
                Patient,
                id=1,
                identification='583930209',
                first_name='Marshall',
                last_name='Kane'
            ),
            baker.make(
                Patient,
                id=2,
                identification='614230563',
                first_name='Stacey',
                last_name='Burch'
            ),
        ]

    def test_list_patients(self):
        expected_json = {
            'data': [
                {
                    'id': 1,
                    'identification': '583930209',
                    'first_name': 'Marshall',
                    'last_name': 'Kane',
                },
                {
                    'id': 2,
                    'identification': '614230563',
                    'first_name': 'Stacey',
                    'last_name': 'Burch',
                },
            ]
        }

        response = self.client.get(reverse('emr:api-patient-list'))
        self.assertDictEqual(response.json(), expected_json)

    def test_datatables_language_file(self):
        expected_keys = [
            'emptyTable',
            'info',
            'infoEmpty',
            'infoFiltered',
            'lengthMenu',
            'loadingRecords',
            'search',
            'zeroRecords',
            'paginate',
        ]

        expected_subkeys = [
            'next',
            'previous',
        ]

        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'es'})
        response = self.client.get(reverse('emr:api-datatables-language'))
        response_json = response.json()

        response_keys = list(response_json.keys())
        response_subkeys = list(response_json['paginate'].keys())

        self.assertListEqual(response_keys, expected_keys)
        self.assertListEqual(response_subkeys, expected_subkeys)
