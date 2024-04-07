#!/usr/bin/python3
"""This Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime


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
