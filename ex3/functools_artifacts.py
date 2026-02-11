from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "min": min,
        "max": max
    }
    if operation not in ops:
        raise ValueError(f"Unsupported operation: {operation}")
    op_func = ops[operation]
    return reduce(op_func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, "fire"),
        'ice_enchant': partial(base_enchantment, 50, "ice"),
        'lightning_enchant': partial(base_enchantment, 50, "ligtning")
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register(int)
    def _(spell):
        return f"Damage spell casted! Deals {spell} HP damage"

    @cast.register(str)
    def _(spell):
        return f"Enchantment activated: {spell}!"

    def _(spell):
        result = [cast(s) for s in spell]
        return f"Multi cast:\n {"\n".join(result)}"
