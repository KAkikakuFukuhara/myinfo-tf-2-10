""" 
debugを出力するための方法
ただし既存のフォーマットではdebugとinfoの違いが分からない
下記の文字列の最初がinfoでもdebugでもIになっている
Examples:
    I0228 09:22:01.134853 140269898220032 t03_change_level.py:14] info
    W0228 09:22:01.135139 140269898220032 t03_change_level.py:15] warning
    I0228 09:22:01.135263 140269898220032 t03_change_level.py:16] debug
"""
import tensorflow as tf
from absl import logging, app

print(logging.level_debug()) # この時点では変わっていない
logging.set_verbosity(logging.DEBUG)
print(logging.level_debug()) # ここで変わる

def main(*args, **kwargs):
    logging.info("info")
    logging.warning("warning")
    logging.debug("debug")

if __name__ == "__main__":
    app.run(main)
