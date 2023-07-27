import os


def generate(package_name: str) -> None:
    path = f"tests/cases/{package_name}"
    os.mkdir(f"{path}/src")
    os.mkdir(f"{path}/src/{package_name}")
    os.mkdir(f"{path}/tests")


def create_dir(directory_name: str, path: str | None = None) -> None:
    directory = directory_name if path is None else f"{path}/{directory_name}"
    if not os.path.exists(directory):
        os.mkdir(directory)


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
