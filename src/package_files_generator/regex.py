import re


def starts_with(reg: str, text: str) -> bool:
    search = re.search(f"^{reg}", text)
    return False if search is None else bool(search)
