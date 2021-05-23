from ..models import Cheese
import pytest
from .factories import CheeseFactory
pytestmark = pytest.mark.django_db


def test__init__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
