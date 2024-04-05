#!/usr/bin/env bash
# This script sets up my web servers for the deployment of web_static.

# Update package list and install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch -c /data/web_static/releases/test/index.html

# Create index.html file
html_file="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$html_file" | sudo tee /data/web_static/releases/test/index.html

# Define the symlink path
SYMLINK_PATH="/data/web_static/current"

# Define the target path the symlink should point to
TARGET_PATH="/data/web_static/releases/test/"

# Check if the symlink exists
if [ -L "$SYMLINK_PATH" ]; then
    # If it exists, delete the symlink
    sudo rm "$SYMLINK_PATH"
fi

# Create symlink
sudo ln -s "$TARGET_PATH" "$SYMLINK_PATH"

# Set appropriate permissions
chown -R ubuntu:ubuntu /data/

# Enable the site configuration and restart Nginx
sudo sed -i 's#listen 80 default_server;#&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}#' /etc/nginx/sites-enabled/default
sudo service nginx restart
