import pytest
from django.urls import reverse

from tests.models import Dog


@pytest.mark.django_db
class TestModelApi:
    APP_NAME = 'tests'
    MODEL_NAME = 'dog'

    def setup(self):
        self.dog = Dog.objects.create(name='Charlie', age=5)

    def test_list_dogs(self, client):
        url = reverse(
            'models-list',
            args=[self.APP_NAME, self.MODEL_NAME]
        )
        response = client.get(url)
        assert response.status_code == 200

        result_data = [{'id': 1, 'name': 'Charlie', 'age': 5}]
        assert response.json() == result_data

    def test_create_dog(self, client):
        data = {'name': 'Richard', 'age': 10}
        url = reverse(
            'models-list',
            args=[self.APP_NAME, self.MODEL_NAME]
        )
        response = client.post(url, data=data)
        assert response.status_code == 201
        assert Dog.objects.filter(**data)

    def test_retrieve_dog(self, client):
        url = reverse(
            'models-detail',
            args=[self.APP_NAME, self.MODEL_NAME, self.dog.pk]
        )
        response = client.get(url)
        assert response.status_code == 200

        result_data = {'id': 1, 'name': 'Charlie', 'age': 5}
        assert response.json() == result_data

    def test_retrieve_non_existent_dog(self, client):
        url = reverse(
            'models-detail',
            args=[self.APP_NAME, self.MODEL_NAME, self.dog.pk + 1]
        )
        response = client.get(url)
        assert response.status_code == 404

    def test_update_dog(self, client):
        data = {'name': 'Richard', 'age': 7}
        url = reverse(
            'models-detail',
            args=[self.APP_NAME, self.MODEL_NAME, self.dog.pk]
        )
        response = client.put(url, data=data, content_type='application/json')
        assert response.status_code == 200

        result_data = {'id': 1, 'name': 'Richard', 'age': 7}
        assert response.json() == result_data
        assert Dog.objects.filter(**result_data)

    def test_delete_dog(self, client):
        url = reverse(
            'models-detail',
            args=[self.APP_NAME, self.MODEL_NAME, self.dog.pk]
        )
        response = client.delete(url)
        assert response.status_code == 204
        assert not Dog.objects.filter(pk=self.dog.pk)

    def test_filter_dogs(self, client):
        Dog.objects.create(name='Charlie', age=3)
        Dog.objects.create(name='Charlie', age=5)

        url = reverse(
            'models-list',
            args=[self.APP_NAME, self.MODEL_NAME]
        ) + '?name=Charlie&age=5'
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_asc_ordering_dogs(self, client):
        Dog.objects.create(name='Charlie', age=3)

        url = reverse(
            'models-list',
            args=[self.APP_NAME, self.MODEL_NAME]
        ) + '?ordering=age'
        response = client.get(url)
        assert response.status_code == 200

        result_data = [
            {'id': 2, 'name': 'Charlie', 'age': 3},
            {'id': 1, 'name': 'Charlie', 'age': 5},
        ]
        assert response.json() == result_data

    def test_desc_ordering_dogs(self, client):
        pass

    def test_paginate_dogs(self, client):
        Dog.objects.create(name='Charlie', age=3)
        Dog.objects.create(name='Charlie', age=5)

        url = reverse(
            'models-list',
            args=[self.APP_NAME, self.MODEL_NAME]
        ) + '?limit=2'
        response = client.get(url)
        assert response.status_code == 200
        assert 'results' in response.json()
        assert len(response.json()['results']) == 2
