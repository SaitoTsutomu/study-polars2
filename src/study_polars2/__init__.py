"""main"""

import shutil
import sys
from pathlib import Path

from jupyter_core.command import main as jupyter_main


def main() -> None:
    """nbs/study_polars2.ipynbをworkフォルダにコピーしてJupyterを起動する"""
    cwd = Path()
    (cwd / "work").mkdir(exist_ok=True)
    nb = "study_polars2.ipynb"
    if sys.argv[-1] == "--new" or not (cwd / "work" / nb).exists():
        shutil.copyfile(cwd / "nbs" / nb, cwd / "work" / nb)
        shutil.copyfile(cwd / "nbs/index.md", cwd / "work/index.md")
    sys.argv = ["jupyter", "lab", "work"]
    sys.exit(jupyter_main())
