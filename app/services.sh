#!/bin/bash

#Start Docker in background
echo '-----------------------------------'
echo '| Starting internal docker damon...'
echo '-----------------------------------'
#dockerd &

#Start Code Server in background
echo '----------------------------------------------------------------'
echo '| Starting code server in background for container management...'
echo '----------------------------------------------------------------'

#exec \
#    s6-setuidgid root \
#        /app/code-server/bin/code-server 
#            --bind-addr 0.0.0.0:8443 \
#            --user-data-dir /.config/data \
#            --extensions-dir /.config/extensions \
#            --disable-telemetry \
#            --auth "password" &


#Start Flask backend
echo '---------------------------'
echo '| Starting SkiffUI damon...'
echo '---------------------------'

export FLASK_APP=/app/public/backend/app.py
pythonw -m flask run -h 0.0.0.0 -p 1027 > log.txt 2>&1 &


#Start npm web server in foreground
echo '----------------------------------'
echo '| Starting front end web server...'
echo '----------------------------------'

npm start --host 0.0.0.0 --port 1027 --disable-host-check
