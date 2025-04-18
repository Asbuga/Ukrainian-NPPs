import calendar
from datetime import datetime


def get_date(year: int, quarter: int) -> str:
    """
    Return the last calendar day of a given quarter in 'dd.mm.yyyy' format.

    Parameters:
        year (int): The year (e.g. 2024).
        quarter (int): The quarter number (1 to 4).

    Returns:
        str: A string representing the last date of the quarter in 'dd.mm.yyyy' format.

    Raises:
        ValueError: If the quarter is not in the range 1 to 4.
    """
    if quarter not in range(1, 5):
        raise ValueError("Quarter must be between 1 – 4.")

    month = quarter * 3
    days = calendar.monthrange(year=year, month=month)[1]
    return datetime(year=year, month=month, day=days).strftime("%d.%m.%Y")


def format_label(label: str) -> str:
    """
    Formats a label by replacing underscores with spaces,
    removing extra spaces, and converting the first letters of words to 
    uppercase.

    Args:
        label (str): The input label that needs formatting.

    Returns:
        str: The formatted label.
    """
    # Заміна підкреслень на пробіли, видалення зайвих пробілів та перетворення на title case
    return label.replace("_", " ").replace("  ", " ").strip().title()
    return formatted_label
