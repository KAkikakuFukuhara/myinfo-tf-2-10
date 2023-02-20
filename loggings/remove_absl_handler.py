""" abslを使わない場合
"""
import logging

import tensorflow as tf
import absl.logging

from absl import app

root_logger:logging.Logger = logging.getLogger()
# ここでabslログを削除できる
root_logger.removeHandler(absl.logging._absl_handler)
absl.logging._warn_preinit_stderr = False

# 自由にレベルを決められる
logging.basicConfig(level=logging.DEBUG)

print(vars(root_logger))

def main(*args, **kwargs):
    logging.info("aaaa")

    logging.debug("aaaa")

if __name__ == "__main__":
    main()
    # app.run(main) # app.run を使うと削除した行為がなかったことにされる
