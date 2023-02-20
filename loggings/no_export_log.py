""" loggingのレベルを変えることができない
"""

import logging

import tensorflow as tf
from absl import app


logging.basicConfig(
    level=logging.WARNING
)

def main(*args, **kwargs):
    logging.info("aaaa") #出力される


if __name__ == "__main__":
    app.run(main)