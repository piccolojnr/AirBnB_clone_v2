#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers.
"""

from fabric.api import env, put, sudo
from os.path import exists, isfile

env.user = "ubuntu"
env.hosts = ["34.203.29.115", "100.25.3.69"]
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Args:
        archive_path (str): Path to the compressed archive.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path) or not isfile(archive_path):
        print("sorry failed")
        return False

    try:
        # Upload archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract archive to /data/web_static/releases/<filename without extension>/
        filename = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(filename.split(".")[0])
        sudo("mkdir -p {}".format(folder_name))
        sudo("tar -xzf /tmp/{} -C {}".format(filename, folder_name))

        # Remove archive from the web server
        sudo("rm /tmp/{}".format(filename))

        # Move contents to final destination
        sudo("mv {}/web_static/* {}/".format(folder_name, folder_name))
        sudo("rm -rf {}/web_static".format(folder_name))

        # Remove existing symbolic link
        sudo("rm -rf /data/web_static/current")

        # Create new symbolic link
        sudo("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print("sorry failed2", e)
        return False
