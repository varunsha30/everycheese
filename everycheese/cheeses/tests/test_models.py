from ..models import Cheese
import pytest

pytestmark = pytest.mark.django_db


def test__init__():
    cheese = Cheese.objects.create(
        name="New Cheese",
        description="hellow this is test cheese",
        firmness=Cheese.Firmness.HARD,
    )

    assert cheese.__str__() == "New Cheese"
    assert str(cheese) == "New Cheese"
