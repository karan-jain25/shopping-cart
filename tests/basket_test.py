import pytest

from src.basket import Basket
from src.brand import Brand
from src.gift_card import GiftCard


def test_basket_initialization():
    basket = Basket()
    assert basket.gift_cards == []


def test_add_gift_card():
    brand = Brand("Amazon", 10)
    gift_card = GiftCard(brand, 100)
    basket = Basket()
    basket.add_gift_card(gift_card)
    assert len(basket.gift_cards) == 1
    assert basket.gift_cards[0] == gift_card


def test_calculate_total_price():
    amazon = Brand("Amazon", 10)
    google = Brand("Google", 20)
    card1 = GiftCard(amazon, 100)
    card2 = GiftCard(google, 200)
    basket = Basket()
    basket.add_gift_card(card1)
    basket.add_gift_card(card2)
    assert basket.calculate_total_price() == 250  # 90 + 160


def test_get_all_gift_cards():
    amazon = Brand("Amazon", 10)
    card = GiftCard(amazon, 100)
    basket = Basket()
    basket.add_gift_card(card)
    gift_cards = basket.get_all_gift_cards()
    assert gift_cards == [("Amazon", 100, 90)]


def test_update_brand_discount():
    amazon = Brand("Amazon", 10)
    card1 = GiftCard(amazon, 100)
    card2 = GiftCard(amazon, 200)
    basket = Basket()
    basket.add_gift_card(card1)
    basket.add_gift_card(card2)

    # Update the discount
    basket.update_brand_discount(amazon, 20)

    assert card1.discounted_price == 80  # 20% discount applied
    assert card2.discounted_price == 160  # 20% discount applied
    assert basket.calculate_total_price() == 240  # 80 + 160
