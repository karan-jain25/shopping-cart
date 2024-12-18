import pytest

from src.brand import Brand
from src.gift_card import GiftCard


def test_gift_card_initialization():
    brand = Brand("Amazon", 10)
    gift_card = GiftCard(brand, 100)
    assert gift_card.brand == brand
    assert gift_card.face_value == 100
    assert gift_card.discounted_price == 90  # 10% discount applied

def test_invalid_face_value():
    pass

def test_calculate_discounted_price():
    brand = Brand("Google", 20)
    gift_card = GiftCard(brand, 200)
    assert gift_card.calculate_discounted_price() == 160  # 20% discount applied
