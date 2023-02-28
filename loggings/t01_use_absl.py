"""
absl.logging を使用する場合、デバッグレベルには切り替わらない
"""
import tensorflow as tf
from absl import logging, app

print(logging.level_warning()) # True
print(logging.level_info())    # False
print(logging.level_debug())   # False

def main(*args, **kwargs):
    logging.info("info")
    print(logging.level_info())  # True:INFOレベルが切り替わっている

    logging.debug("debug")
    print(logging.level_debug()) # False:Debugのレベルは切り替わらない

if __name__ == "__main__":
    app.run(main)
