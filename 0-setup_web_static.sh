#!/usr/bin/env bash
# Will install Nginx if it is not installed already
    apt-get -y update
    apt-get -y install nginx

# Will create some needful dirs/foldersusing variables.
base_var="/data/web_static"
test_var="$base_var/releases/test"
mkdir -p "$test_var" "$base_var/shared"

# Will create a dummy HTML markup for testing
echo '<html>
	<head>
	</head>
	<body>
  	<h1>Test Web Static</h1>
  	<h2>Done by: ArtaxJay</h2>
	<p><i>Lorem ipsum dolor...</i></p>
	</body>
	</html>' > "$test_var/index.html"

# Will create or recreate a symbolic link every time.
to_change_link="$base_var/current"
if [ -L "$to_change_link" ]; then
    rm "$to_change_link"
fi
ln -s "$test_var" "$to_change_link"

# Ownership permission is by user and group.
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content and restart Nginx
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static {
    alias $base_var/current/;
}"
sed -i "/server_name _;/a $nginx_alias" "$nginx_config"
service nginx restart

exit 0
