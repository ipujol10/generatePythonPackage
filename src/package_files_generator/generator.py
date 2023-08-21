import os


def generate(package_name: str) -> None:
    path = f"tests/cases/{package_name}"
    create_dir(f"{path}/src/{package_name}")
    create_dir(f"{path}/tests")


def create_dir(directory_name: str, path: str | None = None) -> None:
    directory = get_final_path(directory_name, path)
    if not os.path.exists(directory):
        if last_dir := get_last_folder(directory):
            create_dir(last_dir)
        os.mkdir(directory)


def create_file(file: str, content: str | None = None,
                directory: str | None = None) -> None:
    file = get_final_path(file, directory)
    content = "" if content is None else content
    with open(file, "w") as f:
        f.write(content)


def get_last_folder(path: str) -> str:
    separated = path.split("/")
    return "" if len(separated) < 2 else "/".join(separated[:-1])


def get_file_content(file: str, directory: str | None = None) -> list[str]:
    with open(get_final_path(file, directory), "r") as f:
        return [el.strip() for el in f.readlines()]


def get_final_path(primary: str, extra: str | None) -> str:
    if not primary:
        raise ValueError("Primary path cannot be empty")
    return primary if (extra is None or not extra) else f"{extra}/{primary}"


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
