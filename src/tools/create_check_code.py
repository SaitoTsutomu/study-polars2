"""下記を実行して何も出力されなければ問題なし

```
uv run src/tools/create_check_code.py &&\
uv run tmp/code_ok.py | grep NG &&\
uv run tmp/code_ng.py | grep OK
```
"""
# ruff: noqa: INP001

import itertools
import re
from collections import defaultdict
from io import IOBase
from pathlib import Path

import nbformat
from more_itertools import last


def proc_prob(  # noqa: C901 PLR0912 PLR0913 PLR0915 PLR0917
    fp_ok: IOBase,
    fp_ng: IOBase,
    count: int,
    prob_source: str,
    cell1: dict,
    cell2: dict,
    cell3: dict,
    cell4: dict,
) -> tuple[str, list[str]]:
    """問題の処理"""
    msg = f"Cell {count}: invalid 問題\n{prob_source}"
    source = cell1["source"]
    metadata = cell1["metadata"]
    if not re.match(r"### `問題 \d+\.\d+\.\d+` ", source):
        raise ValueError(msg)
    if not source.endswith("**解答欄**"):
        raise ValueError(msg)
    if metadata.get("editable", True) or not metadata.get("frozen", True):
        raise ValueError(msg)
    title = source.splitlines()[0]
    fp_ok.write("\nprint('# ==========')\n")
    fp_ng.write("\nprint('# ==========')\n")
    fp_ok.write(f"print('{title}')\n")
    fp_ng.write(f"print('{title}')\n")

    msg = f"Cell {count + 1}: invalid 解答欄\n{prob_source}"
    source = cell2["source"]
    metadata = cell2["metadata"]
    if cell2["cell_type"] != "code":
        raise ValueError(msg)
    last_line = source.strip().splitlines()[-1]
    if "# ここから解答を作成" not in last_line:
        raise ValueError(msg)
    if not metadata.get("editable", True) or metadata.get("frozen", True):
        raise ValueError(msg)
    fp_ok.write(f"{source}\n")
    fp_ng.write(f"{source}\n")

    msg = f"Cell {count + 2}: invalid 解答例\n{prob_source}"
    source = cell3["source"]
    metadata = cell3["metadata"]
    if cell3["cell_type"] != "markdown":
        raise ValueError(msg)
    if not source.startswith("<details><summary>解答例</summary>"):
        raise ValueError(msg)
    if re.match(r"_ans = \w+ = ", source):
        raise ValueError(msg)
    answers = re.findall("```python\n(.*?)```", source, re.DOTALL)  # noqa: RUF039
    if not answers:
        raise ValueError(msg)
    if metadata.get("editable", True) or not metadata.get("frozen", True):
        raise ValueError(msg)

    msg = f"Cell {count + 3}: invalid 検証\n{prob_source}"
    source = cell4["source"]
    metadata = cell4["metadata"]
    if cell4["cell_type"] != "code":
        raise ValueError(msg)
    if not source.startswith("# このセルを実行してください"):
        raise ValueError(msg)
    if (
        metadata.get("editable", True)
        or metadata.get("frozen", True)
        or "source_hidden" not in metadata.get("jupyter", {})
    ):
        raise ValueError(msg)
    for answer in answers:
        fp_ok.write(f"{answer}\n")
        fp_ok.write(f"{source}\n")
        fp_ng.write(f"{source}\n")
    return title, answers


def create_check_code(  # noqa: C901, PLR0912, PLR0914
    nb_path: Path,
    fp_ok: IOBase,
    fp_ng: IOBase,
    func2prob: dict[str, list[str]],
) -> None:
    """チェック用のコード生成"""
    fp_ok.write(
        "import os\nfrom datetime import date\nfrom textwrap import dedent\nimport polars as pl\nimport polars.selectors as cs\nfrom study_polars2.col import col\nos.chdir('tmp')\n"
    )
    fp_ng.write(
        "import os\nfrom datetime import date\nfrom textwrap import dedent\nimport polars as pl\nimport polars.selectors as cs\nfrom study_polars2.col import col\nos.chdir('tmp')\n"
    )
    nb = nbformat.reads(nb_path.read_text(), 4)
    cells = nb["cells"]
    n_cells = len(cells)
    title_n: tuple[int, ...] = ()
    prob_source = ""
    it = iter(cells)
    count = 0
    while count < n_cells:  # noqa: PLR1702
        count += 1
        cell = next(it)
        source = cell["source"]
        if not source:
            msg = f"Cell {count}: empty source"
            raise ValueError(msg)
        cell_type = cell["cell_type"]
        if cell_type == "markdown":
            if m := re.search(r"^skip (\d+)", source):
                n = int(m.group(1))
                print(f"Skip {n} cells at {count}")  # noqa: T201
                count += n
                for _ in range(n):
                    next(it)
                continue
            if source.startswith("### `問題"):
                prob_source = source
                prev = title_n
                title, answers = proc_prob(fp_ok, fp_ng, count, prob_source, cell, next(it), next(it), next(it))
                m2 = re.match(r"### `問題 (\d+)\.(\d+)\.(\d+)` ", title)
                title_n = tuple(map(int, m2.groups())) if m2 else ()
                if prev >= title_n:
                    msg = f"Cell {count}: invalid 問題\n{prev} {title_n}\n{prob_source}"
                    raise ValueError(msg)
                count += 3
                for answer in answers:
                    funcs = itertools.chain(
                        re.findall(r"([a-z]\w+)\(", answer),
                        re.findall(r"\.(bin|cat|dt|list|meta|name|struct|str)\.", answer),
                    )
                    for func in funcs:
                        if func != "print" and title != last(func2prob[func], default=""):
                            func2prob[func].append(title)
            elif source.startswith("<details><summary>解答例</summary>"):
                msg = f"Cell {count}: invalid 解答例\n{prob_source}"
                raise ValueError(msg)
        elif cell_type == "code":
            last_line = source.strip().splitlines()[-1]
            if "# ここから解答を作成" in last_line:
                msg = f"Cell {count}: invalid 解答欄\n{prob_source}"
                raise ValueError(msg)
            if source.startswith("# このセルを実行してください"):
                fp_ok.write(f"{source}\n")
                fp_ng.write(f"{source}\n")


if __name__ == "__main__":
    in_nb = Path("nbs/study_polars2.ipynb")
    out_ok = Path("tmp/code_ok.py")
    out_ng = Path("tmp/code_ng.py")
    func2prob: dict[str, list[str]] = defaultdict(list)
    with out_ok.open("w") as fp_ok, out_ng.open("w") as fp_ng:
        create_check_code(in_nb, fp_ok, fp_ng, func2prob)
    with Path("nbs/index.md").open("w") as fp:
        fp.write("# Index\n\n")
        for key, lst in sorted(func2prob.items()):
            fp.write(f"* `{key}`:\n")
            fp.writelines(f"  * {title[4:]}\n" for title in lst)
