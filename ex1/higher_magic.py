def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return f"{result1}, {result2}"
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def power_amplified(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return power_amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(*args, **kwargs):
        result1 = condition(*args, **kwargs)
        result2 = spell(*args, **kwargs)
        if result1:
            return result2
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    def caster(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return caster


# =================================================
def firebal(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def fireball(power):
    return power


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(firebal, heal)
    print(f"Combined spell result: {combined("Dragon")}")
    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(10)}, Amplified: {mega_fireball(10)}")


if __name__ == "__main__":
    main()
