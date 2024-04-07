#!/usr/bin/python3
"""This Fabric script distributes an archive to your web servers,
using the function do_deploy."""
from fabric.api import run, put, env
from datetime import datetime
import os


# Set Fabric environment variables
env.hosts = ['34.207.63.80', '54.208.120.30']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    # Check if `archive_path` exists
    if not os.path.exists(archive_path):
        return False

    try:
        # upload archive
        put(archive_path, '/tmp/')

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        folder = f"/data/web_static/releases/web_static_{timestamp}"

        # Create target directory if it doesn't exist
        run(f'mkdir -p {folder}')

        # Uncompress archive
        run(f'tar -xzvf /tmp/{archive_path} -C {folder}')
        # Remove uploaded archive
        run(f'rm /tmp/{archive_path}')

        # Remove the existing symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link
        run(f'ln -sf {folder} /data/web_static/current')

        return True
    except Exception as e:
        return False
