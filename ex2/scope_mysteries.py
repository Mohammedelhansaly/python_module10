def mage_counter() -> callable:
    count = 0

    def count_clled():
        nonlocal count
        count += 1
        return count
    return count_clled


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def total(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power
    return total


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    count_called = mage_counter()
    print(f"Call 1: {count_called()}")
    print(f"Call 2: {count_called()}")
    print(f"Call 3: {count_called()}")
    print()
    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))


if __name__ == "__main__":
    main()
