import pytest
from src.brand import Brand


def test_brand_initialization():
    brand = Brand("Amazon", 10)
    assert brand.name == "Amazon"
    assert brand.discount == 10

def test_brand_invalid_name():
    pass

def test_brand_invalid_discount():
    pass

def test_update_discount():
    brand = Brand("Amazon", 10)
    brand.update_discount(15)
    assert brand.discount == 15

def test_update_invalid_discount():
    pass
