def decimal_to_base_int(decima_value: int, base: int) -> int:
    """
    10進数からbase進数への変換

    Args:
        decima_value (int): 10進数整数
        base (int): 基数

    Returns:
        int: base進数整数
    """
    if decima_value // base:
        return int(
            str(decimal_to_base_int(decima_value // base, base))
            + str(decima_value % base)
        )
    return int(decima_value % base)
