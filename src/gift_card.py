from src.brand import Brand


class GiftCard:
    def __init__(self, brand: Brand, face_value: float):
        """Initialize a gift card with a brand and face value."""
        if not isinstance(face_value, (int, float)) or face_value <= 0:
            raise ValueError("Face value must be a positive number.")

        self.brand = brand
        self.face_value = face_value
        self.discounted_price = self.calculate_discounted_price()

    def calculate_discounted_price(self) -> float:
        """Calculate the discounted price based on the brand's discount."""
        return round(self.face_value * (1 - self.brand.discount / 100), 2)
