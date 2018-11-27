from yourapplication import app as application


<VirtualHost *>
    ServerName 35.158.80.91

    WSGIDaemonProcess fliskr user=user1 group=group1 threads=5
    WSGIScriptAlias / /var/www/fliskr/fliskr.wsgi

    <Directory /var/www/fliskr>
        WSGIProcessGroup fliskr
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
