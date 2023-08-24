import re


def starts_with(reg: str, text: str) -> bool:
    search = re.search(f"^{reg}", text)
    return False if search is None else bool(search)


def separate_equal(text: str) -> list[str]:
    return re.split(" = ", text, 1)


def ends_with(reg: str, text: str) -> bool:
    search = re.search(f"{reg}$", text)
    return False if search is None else bool(search)


def clean_end_list(text: str) -> str:
    return re.sub(r",?\s*$", "", text)


def clean_start(text: str) -> str:
    return re.sub(r"^\s*", "", text)


def prepare_list_item(text: str) -> str:
    return re.sub(r"(,?\s*)$", ", ", text, 1)


def is_title(text: str) -> bool:
    search = re.search(r"^\s*\[.+\]\s*$", text)
    return False if search is None else bool(search)


def get_title(text: str) -> str:
    search = re.search(r"\[.+\]", text)
    if search is None:
        raise ValueError
    s, e = search.span()
    return text[s:e]
