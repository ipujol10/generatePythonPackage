import os
def generate(package_name: str) -> None:
    path = f"tests/cases/{package_name}"
    os.mkdir(f"{path}/src")
    os.mkdir(f"{path}/src/{package_name}")
    os.mkdir(f"{path}/tests")


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
