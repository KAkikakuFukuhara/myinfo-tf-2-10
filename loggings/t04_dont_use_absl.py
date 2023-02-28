"""
abslを使わない方法ならフォーマットをいじれる
ただし、absl.app.run を使用すると設定が意味なくなる
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
    logging.info("info")

    logging.debug("debug")

if __name__ == "__main__":
    main()
    app.run(main) # app.run を使うと削除した行為がなかったことにされる
