from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from model_mommy import mommy

from .models import Patient

# Create your tests here.


USERNAME = 'Morty'
USER_PASSWORD = 'password'


@freeze_time("2017-11-25")
class PatientTestCase(TestCase):

    def test_calculate_age(self):
        patient = mommy.make(
            Patient,
            date_of_birth=date(1994, 3, 16)
        )
        self.assertEqual(patient.age(), 23)

    def test_invalid_date_of_birth(self):
        patient = mommy.make(
            Patient,
            date_of_birth=date(2017, 11, 26)
        )

        with self.assertRaises(ValidationError) as cm:
            patient.full_clean(validate_unique=False)

        the_exception = cm.exception
        self.assertDictEqual(
            the_exception.message_dict,
            {'date_of_birth': ['Invalid date of birth.']}
        )


class PatientListApiTestCase(TestCase):
    user = None

    def setUp(self):
        self.user = User.objects.create_user(USERNAME, password=USER_PASSWORD)
        self.client.login(username=USERNAME, password=USER_PASSWORD)

    def test_list_patients(self):
        patients = [
            Patient(
                identification='583930209',
                first_name='Marshall',
                last_name='Kane',
                sex=1,
                date_of_birth=date(2007, 7, 22),
                occupation='Student',
                phone_number='14864677',
                address='9920 Lacinia Rd.'
            ),
            Patient(
                identification='614230563',
                first_name='Stacey',
                last_name='Burch',
                sex=2,
                date_of_birth=date(1998, 4, 25),
                occupation='Clerk',
                phone_number='94599126',
                address='Ap #192-5005 Convallis Avenue'
            ),
        ]

        for patient in patients:
            patient.save()

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

        response = self.client.get(reverse('emr:api-datatables-language'))
        response_json = response.json()

        response_keys = list(response_json.keys())
        response_subkeys = list(response_json['paginate'].keys())

        self.assertListEqual(response_keys, expected_keys)
        self.assertListEqual(response_subkeys, expected_subkeys)
