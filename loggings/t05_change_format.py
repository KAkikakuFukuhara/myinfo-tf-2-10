"""
infoとdebugの違いをつけるためにフォーマッターを使用する.
t04と違いレベルネームがメッセージの前につくのでわかりやすくなった。
Examples:
    W0228 09:22:01.135139 140269898220032 t03_change_level.py:15](WARNING): warning
    I0228 09:22:01.134853 140269898220032 t03_change_level.py:14](INFO   ): info
    I0228 09:22:01.135263 140269898220032 t03_change_level.py:16](DEBUG  ): debug
参考:https://stackoverflow.com/questions/59654893/python-absl-logging-without-timestamp-module-name
"""

import tensorflow as tf

from absl import app, logging
from absl.logging import PythonFormatter, ABSLHandler


def main(*args, **kwargs):
    logging.set_verbosity(logging.DEBUG)
    absl_handler:ABSLHandler = logging.get_absl_handler() # type:ignore
    absl_handler.setFormatter(PythonFormatter("(%(levelname)-8s):%(message)s"))

    logging.warning("warning")
    logging.info("info")
    logging.debug("debug")
    breakpoint()

if __name__ == "__main__":
    app.run(main)