from flasker import app as application


<VirtualHost *>
    ServerName 3.121.195.199

    WSGIDaemonProcess flasker user=user1 group=group1 threads=5
    WSGIScriptAlias / /var/www/flasker/fliskr.wsgi

    <Directory /var/www/flasker>
        WSGIProcessGroup flasker
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
