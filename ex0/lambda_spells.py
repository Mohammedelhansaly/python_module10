def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mages: mages["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spells: "* " + spells + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mages: mages["power"], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': sum(powers) / len(powers) if powers else 0
    }


def main():
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
    ]
    artifact_sorted = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(artifact_sorted)
    print()
    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    spell_transformed = spell_transformer(spells)
    print(' '.join(spell_transformed))


if __name__ == "__main__":
    main()
