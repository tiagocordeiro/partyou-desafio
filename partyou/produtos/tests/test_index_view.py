from os import path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

# from partyou.django_assertions import assert_contains
from partyou.produtos.models import Product


# def test_app_link_in_home(client):
#     response = client.get('/')
#     assert_contains(response, reverse('produtos:product_list'))


IMAGE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(IMAGE_PATH, '2.jpg')


@pytest.fixture
def produtos(db):
    image = SimpleUploadedFile(
        name='2.jpg', content=open(IMAGE_PATH, 'rb').read(), content_type='image/jpeg')
    produto = Product(
        titulo='Camisa Manga Longa Vermelha',
        preco='190',
        foto=image,
        descricao='está é uma descrição'

    )

    produto.save()
    return [produto]


@pytest.fixture
def resp(client, produtos):
    return client.get(reverse('produtos:product_list'))  # pragma: no cover

#
# def test_status_code(resp):
#     assert 200 == resp.status_code


# @pytest.mark.parametrize(
#     'content', [
#         'Camisa Manga Longa Vermelha',
#         'está é uma descrição',
#         '190',
#     ]
# )
# def test_index_content(resp, content):
#     assert_contains(resp, content)
