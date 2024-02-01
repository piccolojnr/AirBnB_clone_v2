#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update

sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# sudo chown -R ubuntu:ubuntu /data/


echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "server {
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By DESKTOP-T9R9R8N;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" | sudo tee /etc/nginx/sites-available/default > /dev/null


sudo service nginx restart
