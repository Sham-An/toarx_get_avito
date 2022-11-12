#https://python-scripts.com/wxpython-catching-exceptions-from-anywhere
from __future__ import print_function

import logging
import wx

print(wx.version())


def exceptionLogger(func, loggerName=''):
    """
    Простой декоратор, который обнаружит и внесёт в лог любые исключения, которые могут появится
    в корневом логгере.
    """
    assert callable(func)
    mylogger = logging.getLogger(loggerName)

    # врапаем новую функцию вокруг вызванной
    def logger_func(*args, **kw):
        try:
            if not kw:
                return func(*args)
            return func(*args, **kw)
        except Exception:
            mylogger.exception('Exception in %s:', func.__name__)

    logger_func.__name__ = func.__name__
    logger_func.__doc__ = func.__doc__
    if hasattr(func, '__dict__'):
        logger_func.__dict__.update(func.__dict__)
    return logger_func


def exceptionLog2Logger(loggerName):
    """
    декоратор, который обнаружит и внесёт в лог любые исключения, которые могут появится
    в именном (названом) логгере
    """
    import functools
    return functools.partial(exceptionLogger, loggerName=loggerName)


class Panel(wx.Panel):
    """"""

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label="Raise Exception")
        btn.Bind(wx.EVT_BUTTON, self.onExcept)

    @exceptionLog2Logger('testLogger')
    def onExcept(self, event):
        """
        Raise an error
        """
        print(self, event)
        print(isinstance(self, wx.Panel))

        # trigger an exception
        1 / 0


class Frame(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Exceptions")
        panel = Panel(self)
        self.Show()


if __name__ == "__main__":
    # Устанавливаем логгер по умолчанию
    log = logging.getLogger('testLogger')
    log.setLevel(logging.INFO)

    # создаём logging-файловый хендлер/форматер
    log_fh = logging.FileHandler("error.log")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    log_fh.setFormatter(formatter)
    log.addHandler(log_fh)

    app = wx.App(False)
    frame = Frame()
    app.MainLoop()