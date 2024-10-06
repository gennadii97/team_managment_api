from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Person


class TeamTests(APITestCase):

    def setUp(self):
        # creating new team
        self.team = Team.objects.create(name='IT support')

    def test_create_team(self):
        # testing newly created team
        url = reverse('team-list')
        data = {'name': 'IT support'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Team.objects.get(id=response.data['id']).name, 'IT support')

    def test_get_team_list(self):
        # testing of getting list of all teams
        url = reverse('team-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_team(self):
        # testing of getting particular team
        url = reverse('team-detail', args=[self.team.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'IT support')

    def test_update_team(self):
        # testing team data update
        url = reverse('team-detail', args=[self.team.id])
        data = {'name': 'Updated IT support'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.get(id=self.team.id).name, 'Updated IT support')

    def test_delete_team(self):
        # testing of deleting team
        url = reverse('team-detail', args=[self.team.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)


class PersonTests(APITestCase):

    def setUp(self):
        # creating new team and person
        self.team = Team.objects.create(name='IT support')
        self.person = Person.objects.create(
            name='Gena',
            surname='Kozak',
            email='kozak@gmail.com',
            team=self.team
        )

    def test_create_person(self):
        # testing of person creation
        url = reverse('person-list')
        data = {
            'name': 'Gena',
            'surname': 'Kozak',
            'email': 'kozak@gmail.com',
            'team': self.team.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Person.objects.get(id=response.data['id']).name, 'Gena')

    def test_get_person_list(self):
        # testing of getting list of people
        url = reverse('person-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_person(self):
        # testing of getting particular person
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Gena')

    def test_update_person(self):
        # testing of data update for person
        url = reverse('person-detail', args=[self.person.id])
        data = {
            'name': 'Updated Gena',
            'surname': 'NieKozak',
            'email': 'niekozak@gmail.com',
            'team': self.team.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get(id=self.person.id).name, 'Updated Gena')

    def test_delete_person(self):
        # testing of person removal
        url = reverse('person-detail', args=[self.person.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
