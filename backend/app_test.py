"""Os testes do projeto.
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true
import requests

# BASE_URL = "http://127.0.0.1"
BASE_URL = "http://localhost:5000"
# BASE_URL = "https://python3-flask-uat.herokuapp.com/"


class NewUUID():  # pylint: disable=too-few-public-methods
    """The new uuid created when creating a new book request.
    The NewUUID is used for further tests
    """

    def __init__(self, value):
        self.value = value



def test_show_all_users():
    "Test getting all users"
    response = requests.get('%s/show_all_users' % (BASE_URL))
    assert_true(response.ok)



def test_show_friends():
    "Test mostrando amigos de um usuario"
    payload = {'nome': 'ana'}
    response = requests.post('%s/show_friends' % (BASE_URL), json=payload)

    assert_true(response.status_code == 200)

def test_show_friend_recomendation():
    "Test mostrando recomendacao de amigos"
    payload = {'nome': 'ana'}
    response = requests.post('%s/show_friend_recomendation' % (BASE_URL), json=payload)

    assert_true(response.status_code == 200)

def test_register_new_user():
    "Test adicionando novo usuario"
    payload = {'nome': 'andre', 'amigo': 'jose'}
    response = requests.post('%s/register_new_user' % (BASE_URL), json=payload)

    assert_true(response.status_code == 201)    

