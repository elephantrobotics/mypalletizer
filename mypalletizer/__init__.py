# encoding=utf-8

from __future__ import absolute_import

from mypalletizer.main import MyPalletizer
from mypalletizer.generate import CommandGenerater
from mypalletizer import utils

__all__ = ["MyPalletizer", "CommandGenerater", "utils"]

__version__ = "1.0.0-beta.1"
__author__ = "Zachary zhang"
__email__ = "lijun.zhang@elephantrobotics.com"
__git_url__ = "https://github.com/elephantrobotics/mypalletizer"
__copyright__ = "2021 Shenzhen Elephantrobotics technology company"

PI_PORT = "/dev/ttyAMA0"
PI_BAUD = 1000000
