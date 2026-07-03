import ctypes
import sys

from config.settings import DLL_WINDOWS
from config.settings import DLL_LINUX


class Landmark(ctypes.Structure):

    _fields_ = [

        ("x", ctypes.c_float),

        ("y", ctypes.c_float),

        ("z", ctypes.c_float)

    ]


def obter_nome_biblioteca():

    if sys.platform.startswith("win"):

        return DLL_WINDOWS

    return DLL_LINUX