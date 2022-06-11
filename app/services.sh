#!/bin/bash

#Start Docker in background
dockerd &

#Start Code Server in background
exec \
    s6-setuidgid root \
        /app/code-server/bin/code-server \
            --bind-addr 0.0.0.0:8443 \
            --user-data-dir /.config/data \
            --extensions-dir /.config/extensions \
            --disable-telemetry \
            --auth "password" &

#Start Flask backend
export FLASK_APP=/app/public/backend/app.py
flask run &

#Start npm web server in foreground
npm start --host 0.0.0.0 --port 1027 --disable-host-check
