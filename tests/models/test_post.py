

import pytest
from blog.factories import PostFactories

@pytest.fixture
def test_create_published():
    return PostFactories(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(test_create_published):
    assert test_create_published.title == 'pytest with factory'


