#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


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
