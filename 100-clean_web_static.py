#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import local, sudo, cd, env

env.user = "ubuntu"
env.hosts = ["34.203.29.115", "100.25.3.69"]
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    local_archives = local("ls -t versions/", capture=True).split()

    with cd("/data/web_static/releases"):
        remote_archives = sudo("ls -t .").split()

    number = int(number)
    num_to_keep = max(number, 1)

    # Local clean
    if len(local_archives) > 0:
        local_to_delete = local_archives[num_to_keep:]
        for file in local_to_delete:
            local("rm -f versions/{}".format(file))

    # Remote clean
    if len(remote_archives) > 0:
        remote_to_delete = remote_archives[num_to_keep:]
        for file in remote_to_delete:
            sudo("rm -rf /data/web_static/releases/{}".format(file.strip(".tgz")))
