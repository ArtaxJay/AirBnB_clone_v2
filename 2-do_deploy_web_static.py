#!/usr/bin/python3
# A fabfile that will generate a .tgz compressed archive
# from the files of web_static dir.
import os.path
from fabric.api import local
from datetime import datetime as Date
from fabric.api import run
from fabric.api import put
from fabric.api import env


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    date_object = Date.utcnow()
    locate_file = \
        "versions/web_static_{}{}{}{}{}{}.tgz".format(date_object.year,
                                                      date_object.month,
                                                      date_object.day,
                                                      date_object.hour,
                                                      date_object.minute,
                                                      date_object.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(locate_file)).failed is True:
        return None
    return locate_file


# A fabfile that will distribute a compressed archive
# to a remote web server.

# My host servers IPs
env.host_servers = ["3.85.33.232", "54.90.63.56"]


# Define do_deploy function
def do_deploy(archive_path):
    """This func def distributes compressed archive to web servers.

    Args:
        archive_path (str): arg-the archive file path to distribute.
    Returns:
        If locating the file was unsuccesful ret False.
        Else ret True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    locate_file = archive_path.split("/")[-1]
    getfilename = locate_file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(locate_file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(getfilename)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(getfilename)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(locate_file, getfilename)).failed is True:
        return False
    if run("rm /tmp/{}".format(locate_file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, getfilename)).
    failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(getfilename)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(getfilename)).failed is True:
        return False
    return True
