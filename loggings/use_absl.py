""" logging.info を使った時
"""
import tensorflow as tf
from absl import logging, app

print(logging.level_info())
print(logging.level_warning())

def main(*args, **kwargs):
    logging.info("aaaa")
    print(logging.level_info()) # 自動でレベルが切り替わっている

    logging.debug("aaaa")
    print(logging.level_debug()) # レベルは切り替わらない

if __name__ == "__main__":
    app.run(main)
