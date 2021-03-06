import pytest
from django.urls import reverse

from partyou.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:contato'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, 'CONTATO')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:contato")}">Contato</a>')


@pytest.mark.parametrize(
    'content', [
        'Brasil, Pernambuco',
        'Recife - Caçote',
        '+55 (81) 9 8888-8888',
        'Segunda - Sexta: 9:00 às 17:00',
        'partyoudesafio@contato.com',
        'Envie-nos sua mensagem a qualquer momento!',
    ]
)
def test_contact_content(resp, content):
    assert_contains(resp, content)
