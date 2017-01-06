class Block:
        def __init__(self, skin, rarity, mining_duration, gravity):
                self.skin = skin
                self.rarity = rarity
                self.mining_duration = mining_duration
                self.gravity = gravity

        # Getters
        def get_skin(self):
                return self.skin
        def get_rarity(self):
                return self.rarity
