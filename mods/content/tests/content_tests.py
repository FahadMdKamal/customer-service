from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

from ..models.content import Content
from ..serializers import ContentSerializer

client = Client()


class GetAllContentTest(APITestCase):
    """ Test module for Content model """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user("userone", "userone")

    def test_get_all_content(self):
        self.client.force_authenticate(user=self.user)
        # get API response
        response = self.client.get(reverse('convo_content'))
        # get data from db
        content_obj = Content.objects.all()
        serializer = ContentSerializer(content_obj, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_content_creation(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "type_ref": "Button",
            "title": "Test Button",
            "subtitle": "Sub Button",
            "description": "Lorem ipsum Button",
            "default_action": "daction",
            "action_items": {
                "action_item": "ai"
            },
            "left_contents": {
                "lc": "left_content"
            },
            "display_order": "0",
            "content_body": "lorem ipsum content body",
            "content_format": "JSON",
            "template_cache": "sdf",
            "value_cache": "asdf",
        }
        res = self.client.post(reverse('convo_content'), format='json', data=data)
        self.assertEqual(res.status_code, 201)


class GetSingleContentTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user("userone", "userone")
        data = {
            "type_ref": "Button",
            "title": "Test Button",
            "subtitle": "Sub Button",
            "description": "Lorem ipsum Button",
            "default_action": "daction",
            "action_items": {
                "action_item": "ai"
            },
            "left_contents": {
                "lc": "left_content"
            },
            "display_order": "0",
            "content_body": "lorem ipsum content body",
            "content_format": "JSON",
            "template_cache": "sdf",
            "value_cache": "asdf",
        }
        self.new_content = Content.objects.create(**data)

    # def test_get_valid_single_content(self):
    #     self.client.force_authenticate(user=self.user)
    #     response = client.get(reverse('convo_content', args=(self.new_content.pk,)))
    #     coentent = Content.objects.get(pk=self.new_content.pk)
    #     serializer = ContentSerializer(coentent)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_invalid_single_content(self):
    #     response = client.get(reverse('convo_content', kwargs={'pk': 30}))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)