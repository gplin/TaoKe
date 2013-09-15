# -*- coding:utf-8 -*-
import os
import sqlite3
from django.conf import settings


def getconn():
    conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,"db\TaoKe.db"))
