import os
import datetime


def generate(package_name: str, username: str) -> None:
    path = f"tests/cases/{package_name}"
    create_dir(f"{path}/src/{package_name}")
    create_dir(f"{path}/tests")
    create_file("LICENSE", generate_license(username), path)


def generate_license(username: str) -> str:
    year = datetime.datetime.now().year
    text = "MIT License\n\n"
    text += f"Copyright (c) {year} {username}\n\n"
    text += ("Permission is hereby granted, free of charge, to any person "
             "obtaining a copy\n")
    text += ("of this software and associated documentation files "
             "(the \"Software\"), to deal\n")
    text += ("in the Software without restriction, including without "
             "limitation the rights\n")
    text += ("to use, copy, modify, merge, publish, distribute, "
             "sublicense, and/or sell\n")
    text += ("copies of the Software, and to permit persons to "
             "whom the Software is\n")
    text += "furnished to do so, subject to the following conditions:\n\n"
    text += ("The above copyright notice and this permission notice "
             "shall be included in all\n")
    text += "copies or substantial portions of the Software.\n\n"
    text += ("THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY "
             "OF ANY KIND, EXPRESS OR\n")
    text += ("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF "
             "MERCHANTABILITY,\n")
    text += ("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. "
             "IN NO EVENT SHALL THE\n")
    text += ("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, "
             "DAMAGES OR OTHER\n")
    text += ("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, "
             "TORT OR OTHERWISE, ARISING FROM,\n")
    text += ("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR "
             "OTHER DEALINGS IN THE\n")
    text += "SOFTWARE."
    return text


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


def read_pyproject(file: str) -> dict[str, dict[str, str]]:
    output: dict[str, dict[str, str]] = {}
    if not os.path.isfile(file):
        return output
    lines: list[str] = []
    with open(file, "r") as f:
        lines = f.readlines()
    group = ""
    n = 0
    while n < len(lines):
        group, n = process_pyproject_line(lines, n, output, group)
    return output


def process_pyproject_line(
        file: list[str], n: int, data: dict[str, dict[str, str]], group: str
        ) -> tuple[str, int]:
    line = file[n].strip()
    if not line:
        return group, n + 1
    if (line[0] == "["):
        if line not in data:
            data[line] = {}
        return line, n + 1
    if not group:
        raise ValueError("Element displayed before a group")
    key, value = line.split(" = ")
    data[group][key] = value
    return group, n + 1


def generate_pyproject(file: str, data: dict[str, dict[str, str]]) -> None:
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
