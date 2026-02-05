class StoreSystem:
    def __init__(self):
        self.currency = 0
        self.crates = []
        self.inventory = []

    def earn_currency(self, amount):
        self.currency += amount
        print(f"Earned {amount} currency. Total: {self.currency}")

    def buy_crate(self, crate_type):
        prices = {"basic": 100, "premium": 500}
        if self.currency >= prices.get(crate_type, 999999):
            self.currency -= prices[crate_type]
            self.crates.append(crate_type)
            print(f"Bought {crate_type} crate.")
            return True
        print("Not enough currency.")
        return False

    def open_crate(self, crate_type):
        if crate_type in self.crates:
            self.crates.remove(crate_type)
            # Simple loot table
            reward = "Skin_" + str(len(self.inventory))
            self.inventory.append(reward)
            print(f"Opened {crate_type} crate and got: {reward}")
            return reward
        return None

# Easy-to-earn logic: Daily rewards and mission bonuses
class MissionManager:
    @staticmethod
    def get_daily_bonus():
        return 200 # High bonus for easy earning

    @staticmethod
    def get_match_reward(placement, kills):
        return (250 - placement) * 10 + (kills * 50)
