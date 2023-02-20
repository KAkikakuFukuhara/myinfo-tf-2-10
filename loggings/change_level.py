""" logging レベルを変えることができる
"""
import tensorflow as tf
from absl import logging, app

print(logging.level_debug()) # この時点では変わっていない
logging.set_verbosity(logging.DEBUG)
print(logging.level_debug()) # ここで変わる

def main(*args, **kwargs):
    logging.debug("aaaa")

if __name__ == "__main__":
    app.run(main)
