# 「review」タグを付けたセルを抜き出すプログラム
# 「review」タグは、右上のProperty inspectorのAdd Tagで追加・削除可能
import sys
from pathlib import Path

import nbformat

input_ = Path("work/study_polars2.ipynb")
output = Path("work/review.ipynb")

if output.exists() and (len(sys.argv) <= 1 or sys.argv[1] != "--force"):
    print(f"{output}を削除するか --force を付けてください")
    sys.exit()

src = nbformat.read(input_, as_version=4)

comment = "# ここから解答を作成してください\n"
cells = src.cells[1:4]
count = 0
for cell in src.cells:
    if count or ("review" in cell.get("metadata", {}).get("tags", [])):
        if comment in cell.get("source", ""):
            i = cell["source"].index(comment)
            cell["source"] = cell["source"][: i + len(comment)]
        if "outputs" in cell:
            cell["outputs"] = []
        cells.append(cell)
        count = 4 if count <= 0 else count - 1

dst = nbformat.v4.new_notebook(
    cells=cells,
    metadata={
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3",
        },
    },
)
nbformat.write(dst, output)
print(f"{output}を作成しました")
