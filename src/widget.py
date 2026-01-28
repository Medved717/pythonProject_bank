def mask_account_card(card_and_account_number: str) -> str:
    """Функция, которая принимает на вход тип и номер карты, а также номер счета, выводит маску."""

    card_name_maestro = "Maestro"
    card_name_master_card = "MasterCard"
    card_name_visa_classic = "Visa Classic"
    card_name_visa_platinum = "Visa Platinum"
    card_name_visa_gold = "Visa Gold"
    card_name_score = "Счет"

    # 1. Условие по Маэстро
    if card_name_maestro in card_and_account_number:

        # Функция по Маэстро
        def get_mask_card_number(card_and_account_number: str) -> str:
            """Функция принимает на вход тип и номер карты, и возвращает ее маску."""

            card_type = card_and_account_number[0:8]
            card_number = card_and_account_number[8::]
            mask_in_number = card_number.replace(card_number[6:12], "XXXXXX")
            groups = []
            for i in range(0, len(mask_in_number), 4):
                group = mask_in_number[i: i + 4]
                groups.append(group)

            number_result = " ".join(groups)
            result = card_type + number_result
            return result

        return get_mask_card_number(card_and_account_number)

    # 2. Условие по Мастеркард
    elif card_name_master_card in card_and_account_number:

        # Функция по Мастеркард
        def get_mask_card_number(card_and_account_number: str) -> str:
            """Функция принимает на вход тип и номер карты, и возвращает ее маску."""

            card_type = card_and_account_number[0:11]
            card_number = card_and_account_number[11::]
            mask_in_number = card_number.replace(card_number[6:12], "XXXXXX")
            groups = []
            for i in range(0, len(mask_in_number), 4):
                group = mask_in_number[i: i + 4]
                groups.append(group)

            number_result = " ".join(groups)
            result = card_type + number_result
            return result

        return get_mask_card_number(card_and_account_number)

    # 3. Условие по Виза классик
    elif card_name_visa_classic in card_and_account_number:

        # Функция по Виза классик
        def get_mask_card_number(card_and_account_number: str) -> str:
            """Функция принимает на вход тип и номер карты, и возвращает ее маску."""

            card_type = card_and_account_number[0:13]
            card_number = card_and_account_number[13::]
            mask_in_number = card_number.replace(card_number[6:12], "XXXXXX")
            groups = []
            for i in range(0, len(mask_in_number), 4):
                group = mask_in_number[i: i + 4]
                groups.append(group)

            number_result = " ".join(groups)
            result = card_type + number_result
            return result

        return get_mask_card_number(card_and_account_number)

    # 4. Условие по Виза платинум
    elif card_name_visa_platinum in card_and_account_number:

        # Функция по Виза платинум
        def get_mask_card_number(card_and_account_number: str) -> str:
            """Функция принимает на вход тип и номер карты, и возвращает ее маску."""

            card_type = card_and_account_number[0:14]
            card_number = card_and_account_number[14::]
            mask_in_number = card_number.replace(card_number[6:12], "XXXXXX")
            groups = []
            for i in range(0, len(mask_in_number), 4):
                group = mask_in_number[i: i + 4]
                groups.append(group)

            number_result = " ".join(groups)
            result = card_type + number_result
            return result

        return get_mask_card_number(card_and_account_number)

    # 5. Условие по Виза голд
    elif card_name_visa_gold in card_and_account_number:

        # Условие по Виза голд
        def get_mask_card_number(card_and_account_number: str) -> str:
            """Функция принимает на вход тип и номер карты, и возвращает ее маску."""

            card_type = card_and_account_number[0:10]
            card_number = card_and_account_number[10::]
            mask_in_number = card_number.replace(card_number[6:12], "XXXXXX")
            groups = []
            for i in range(0, len(mask_in_number), 4):
                group = mask_in_number[i: i + 4]
                groups.append(group)

            number_result = " ".join(groups)
            result = card_type + number_result
            return result

        return get_mask_card_number(card_and_account_number)

    # 6. Условие по маске счета.
    elif card_name_score in card_and_account_number:

        # Функция по маске счета.
        def get_mask_account(card_and_account_number: str) -> str:
            """Функция, которая укорачивает и маскирует номер счета"""

            score = card_and_account_number[0:5]
            new_mask_account = card_and_account_number[-6:]
            score_result = new_mask_account.replace(new_mask_account[0:2], "**")
            result = score + score_result
            return result

        return get_mask_account(card_and_account_number)


mask_card_number = mask_account_card("Счет 73654108430135874305")
print(mask_card_number)


def get_date(dd_mm_yyyy: str) -> str:
    """Функция, которая переводит даты в формат ДД.ММ.ГГГГ."""
    result = ".".join([dd_mm_yyyy[8:10], dd_mm_yyyy[5:7], dd_mm_yyyy[0:4]])
    return result


result_date = get_date("2024-03-11T02:26:18.671407")
print(result_date)
