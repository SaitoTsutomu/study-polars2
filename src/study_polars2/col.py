"""列名のExprの取得"""

import polars as pl


class Col:
    """colオブジェクトのクラス"""

    def __getattribute__(self, name: str) -> pl.Expr:
        """大文字で始まる列名のExprの取得"""
        if name[0].isupper():
            c = pl.col(name)
            setattr(self, name, c)
            return c
        return super().__getattribute__(name)


col = Col()
