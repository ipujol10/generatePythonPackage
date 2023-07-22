import os


def generate(package_name: str) -> None:
    path = f"tests/cases/{package_name}"
    os.mkdir(f"{path}/src")
    os.mkdir(f"{path}/src/{package_name}")
    os.mkdir(f"{path}/tests")


def create_dir(directory_name: str, path: str | None = None) -> None:
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
