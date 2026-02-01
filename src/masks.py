def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    mask_number = card_number.replace(card_number[6:12], "XXXXXX")
    groups = []
    for i in range(0, len(mask_number), 4):
        group = mask_number[i : i + 4]
        groups.append(group)

    result = " ".join(groups)
    return result


mask_card_number = get_mask_card_number("7000792289606361")
print(mask_card_number)


def get_mask_account(mask_account: str) -> str:
    """ "Функция, которая укорачивает и маскирует номер счета"""
    new_mask_account = mask_account[-6:]
    result = new_mask_account.replace(new_mask_account[0:2], "**")
    return result


result_1 = get_mask_account("73654108430135874305")
print(result_1)