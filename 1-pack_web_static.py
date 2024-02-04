#!/usr/bin/python3
# A fabfile that will generate a .tgz compressed archive
# from the files of web_static dir.
import os.path
from fabric.api import local
from datetime import datetime as Date


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    date_object = Date.utcnow()
    timestamp = \
        "versions/web_static_{}{}{}{}{}{}.tgz".format(date_object.year,
                                                      date_object.month,
                                                      date_object.day,
                                                      date_object.hour,
                                                      date_object.minute,
                                                      date_object.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(timestamp)).failed is True:
        return None
    return timestamp
