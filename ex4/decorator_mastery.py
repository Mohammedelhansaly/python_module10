from functools import wraps
from typing import Callable
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attemp = 0
            while attemp < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attemp += 1
                    if attemp < max_attempts:
                        print(f"Spell failed, retrying... (attempt "
                              f"{attemp}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MagaGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        name = name.strip()
        if len(name) < 3:
            return False
        if not all(char.isalpha() or char.isspace() for char in name):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball():
    time.sleep(0.101)
    return "Fireball cast!"


def main():
    print("Testing spell timer...")

    print(fireball())
    print()
    print("Testing MageGuild...")

    magaGuild = MagaGuild()
    print(magaGuild.validate_mage_name("Mohammed"))
    print(magaGuild.validate_mage_name("1nv"))
    print(magaGuild.cast_spell("Lightning", 15))
    print(magaGuild.cast_spell("Fireball", 8))


if __name__ == "__main__":
    main()
