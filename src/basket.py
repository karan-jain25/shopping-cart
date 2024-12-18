from src.brand import Brand
from src.gift_card import GiftCard


class Basket:
    def __init__(self):
        """Initialize the basket to hold gift cards."""
        self.gift_cards = []  # List to store GiftCard objects

    def add_gift_card(self, gift_card: GiftCard):
        """Add a gift card to the basket."""
        self.gift_cards.append(gift_card)

    def calculate_total_price(self) -> float:
        """Calculate the total discounted price of all gift cards in the basket."""
        return round(sum(card.discounted_price for card in self.gift_cards), 2)

    def get_all_gift_cards(self):
        """List all gift cards in the basket."""
        return [(card.brand.name, card.face_value, card.discounted_price) for card in self.gift_cards]

    def update_brand_discount(self, brand: Brand, new_discount: float):
        """Update the discount for a brand and recalculate affected gift cards."""
        brand.update_discount(new_discount)
        for card in self.gift_cards:
            if card.brand.name == brand.name:
                card.discounted_price = card.calculate_discounted_price()
