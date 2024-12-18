class Brand:
    def __init__(self, name: str, discount: float):
        """Initialize a single brand with a name and a discount."""
        if not isinstance(name, str):
            raise ValueError("Brand name must be a string.")
        if not isinstance(discount, (int, float)) or discount < 0:
            raise ValueError("Discount must be a non-negative number.")

        self.name = name
        self.discount = discount

    def update_discount(self, new_discount: float):
        """Update the discount percentage for the brand."""
        self.discount = new_discount
