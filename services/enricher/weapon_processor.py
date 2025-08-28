from shared.text_processing.text_processor import TextProcessor

class WeaponProcessor:
    def __init__(self, weapon_list_path):
        processor = TextProcessor()
        self.weapon_list = []
        with open(weapon_list_path, encoding='utf-8') as f:
            for weapon in f:
                clean_weapon = processor.process(weapon)
                if clean_weapon:
                    self.weapon_list.append(clean_weapon)

    def find_weapon(self, text):
        weapon_references = []
        for weapon in self.weapon_list:
            if weapon in text:
                print(f"Found weapon: {weapon}")
                weapon_references.append(weapon)
        if weapon_references:
            return weapon_references
        return None