# -*- coding: utf-8 -*-

from pyvows import Vows
from thumbor.vows import http_loader_vows


@Vows.batch
class ReturnContentVows(http_loader_vows.ReturnContentVows):
    pass
