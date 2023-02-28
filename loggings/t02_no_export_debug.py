""" 
logging（通常)ライブラリを使用した場合、デバッグレベルが出力できない
"""

import logging

import tensorflow as tf
from absl import app

logging.basicConfig(
    level=logging.DEBUG
)

def main(*args, **kwargs):
    logging.info("info")   # 出力される
    logging.debug("debug") # 出力されない

if __name__ == "__main__":
    app.run(main)