import decimal


def round_or_0(value, digits=2):
    try:
        return round(decimal.Decimal(value), digits)
    except Exception:
        return 0
