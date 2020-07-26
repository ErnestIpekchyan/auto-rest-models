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
        pass

    def test_retrieve_dog(self, client):
        pass

    def test_retrieve_non_existent_dog(self, client):
        pass

    def test_update_dog(self, client):
        pass

    def test_delete_dog(self, client):
        pass

    def test_filter_dogs(self, client):
        pass

    def test_asc_ordering_dogs(self, client):
        pass

    def test_desc_ordering_dogs(self, client):
        pass

    def test_paginate_dogs(self, client):
        pass
