import re
import sys
from pathlib import Path

import nbformat

nb_file = Path("work/study_polars2.ipynb")
if not nb_file.exists():
    print(f"{nb_file}がありません")
    sys.exit()

ok_count = 0
ng_count = 0
unexecuted_count = 0
unexecuted_prob = prob = ""

nb = nbformat.read(nb_file, as_version=4)
for cell in nb.cells:
    m = re.match(r"### (`問題 \d+\.\d+\.\d+` \w+)", cell.source)
    if m:
        prob = m.group(1)
    if not cell.source.startswith("# このセルを実行してください"):
        continue
    for output in cell.outputs:
        if "OK" in output.text:
            ok_count += 1
            break
        elif "NG" in output.text:
            ng_count += 1
            break
    else:
        unexecuted_count += 1
        if unexecuted_count == 1:
            unexecuted_prob = prob

print(f"正解　: {ok_count:>3} 件")
print(f"不正解: {ng_count:>3} 件")
print(f"未実行: {unexecuted_count:>3} 件")
if unexecuted_prob:
    print(f"  {unexecuted_prob} から")
