def final_deposit_amount(*interest, amount=1000):
    result = amount
    for rate in interest:
        result += result * (rate / 100)
    return round(result, 2)