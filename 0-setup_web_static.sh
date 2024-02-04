#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

server="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"

sudo apt-get update -y
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -hR ubuntu:ubuntu /data/


echo "<html>
  <head>
  </head> 
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
rm -f "/data/web_static/current"; ln -s "/data/web_static/releases/test/" "/data/web_static/current"

sudo sed -i "29i\ $server" "$file"

sudo service nginx restart
