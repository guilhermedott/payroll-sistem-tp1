from config import (
    HIGH_TAX_LIMIT,
    MEDIUM_TAX_LIMIT,
    HIGH_TAX_RATE,
    MEDIUM_TAX_RATE,
    LOW_TAX_RATE,
)

def apply_tax(total):
    if total > HIGH_TAX_LIMIT:
        return total - (total * HIGH_TAX_RATE)
    elif total > MEDIUM_TAX_LIMIT:
        return total - (total * MEDIUM_TAX_RATE)
    else:
        return total - (total * LOW_TAX_RATE)

def apply_tax_again(total):
    if total > HIGH_TAX_LIMIT:
        return total - (total * HIGH_TAX_RATE)
    elif total > MEDIUM_TAX_LIMIT:
        return total - (total * MEDIUM_TAX_RATE)
    else:
        return total - (total * LOW_TAX_RATE)
