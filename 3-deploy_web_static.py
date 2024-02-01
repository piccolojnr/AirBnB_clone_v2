#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers.
"""

from fabric.api import env, local, sudo, put
from datetime import datetime
import os
from os.path import exists, isfile


env.user = "ubuntu"
env.hosts = ["34.203.29.115", "100.25.3.69"]
env.key_filename = "~/.ssh/school"


def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Generate archive name using the current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress web_static contents into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None


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


def deploy():
    """
    Creates and distributes an archive to your web servers.

    Returns:
        True if successful, otherwise False.
    """
    # Call do_pack() to create the archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if not archive_path:
        return False

    # Call do_deploy() using the new archive path
    return do_deploy(archive_path)
