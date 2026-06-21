# 「review」タグを付けたセルを抜き出すプログラム
# 「review」タグは、右上のProperty inspectorのAdd Tagで追加・削除可能
import sys
from pathlib import Path

import nbformat

input_ = Path("work/study_polars2.ipynb")
output = Path("work/review.ipynb")

if output.exists() and (len(sys.argv) <= 1 or sys.argv[1] != "--force"):
    print(f"{output}を削除してください")
    sys.exit()

src = nbformat.read(input_, as_version=4)

cells = [cell for cell in src.cells if "review" in cell.get("metadata", {}).get("tags", [])]

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
