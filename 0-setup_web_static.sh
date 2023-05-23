#!/usr/bin/env bash
# Bash script to automate web static

if ! command -v nginx> /dev/null; then
	echo "command not found! installing nginx"
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "a Hello Wonderer"|sudo tee /data/web_static/releases/test/index.html >/dev/null
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# add /hnb_static/ route
if grep -R "hbnb_static" /etc/nginx/sites-available/default;then
	echo "already set">/dev/null;
else
	echo "setting up hbnb_static route">/dev/null;
	sudo sed -i '/^\tlocation \/ {$/a \\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default;
fi
# restart server
sudo service nginx restart
