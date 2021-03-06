import pytest
from django.urls import resolve, reverse

from .factories import CheeseFactory, cheese

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse("cheeses:list") == "/cheeses/"


def test_list_resolve():
    assert resolve("/cheeses/").view_name == "cheeses:list"


def test_add_reverse():
    assert reverse("cheeses:add") == "/cheeses/add/"


def test_add_resolve():
    assert resolve("/cheeses/add/").view_name == "cheeses:add"


def test_detail_reverse(cheese):
    assert (
        reverse("cheeses:detail", kwargs={"slug": cheese.slug})
        == f"/cheeses/{cheese.slug}/"
    )


def test_detail_resolve(cheese):
    assert resolve(f"/cheeses/{cheese.slug}/").view_name == "cheeses:detail"
