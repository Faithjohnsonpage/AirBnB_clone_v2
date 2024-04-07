#!/usr/bin/python3
"""This Fabric script distributes an archive to your web servers,
using the function do_deploy."""
from fabric.api import run, put, env, local
from datetime import datetime
import os


# Set Fabric environment variables
env.hosts = ['34.207.63.80', '54.208.120.30']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_pack():
    """Create a compressed archive (.tgz) of the web_static folder.
    Returns:
        str: The filename of the created archive if successful, None otherwise
    """
    try:
        local('mkdir -p versions')

        # Generate the current date and time to use in the file name
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Define the name of the archive file
        filename = f'versions/web_static_{timestamp}.tgz'

        local(f'tar -cvzf {filename} web_static')

        return filename
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    # Check if `archive_path` exists
    if not os.path.exists(archive_path):
        return False

    try:
        # upload archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        folder = f'/data/web_static/releases/web_static_{timestamp}'
        run(f'sudo mkdir -p {folder}/')
        # uncompress archive and delete .tgz
        run(f'sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C {folder}/')

        # remove archive
        run(f'sudo rm /tmp/web_static_{timestamp}.tgz')

        # move contents into host web_static
        run(f'sudo mv {folder}/web_static/* {folder}/')

        # remove extraneous web_static dir
        run(f'sudo rm -rf {folder}/web_static')

        # Remove the existing symbolic link
        run('sudo rm -rf /data/web_static/current')
        # Create a new symbolic link
        run(f'sudo ln -s {folder}/ /data/web_static/current')

        return True
    except Exception as e:
        return False


def deploy():
    """Deploy function"""
    file_path = do_pack()
    if file_path is False:
        return False
    return do_deploy(file_path)
