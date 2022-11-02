#!/bin/bash

#Start Docker in background
echo '-----------------------------------'
echo '| Starting internal docker damon...'
echo '-----------------------------------'
dockerd &

retval = $ ? 
if $retval == 0;
then 
    echo '-------' 
    echo '| Done' 
    echo '-------' 
    continue 
else;
    echo "Failed to start Docker damon, please check docker logs" 
    break 
fi 


#Start Code Server in background
echo '----------------------------------------------------------------'
echo '| Starting code server in background for container management...'
echo '----------------------------------------------------------------'

exec \
    s6-setuidgid root \
        /app/code-server/bin/code-server 
            --bind-addr 0.0.0.0:8443 \
            --user-data-dir /.config/data \
            --extensions-dir /.config/extensions \
            --disable-telemetry \
            --auth "password" &


retval = $ ? 
if $retval == 0;
then 
    echo '-------' 
    echo '| Done' 
    echo '-------' 
    continue 
else;
    echo "Failed to start code server, please check container logs" 
    break 
fi 

#Start Flask backend
echo '---------------------------'
echo '| Starting SkiffUI damon...'
echo '---------------------------'

export FLASK_APP=/app/public/backend/app.py
flask run &

retval = $ ? 
if $retval == 0;
then 
    echo '-------' 
    echo '| Done' 
    echo '-------' 
    continue 
else;
    echo "Failed to start SkiffUI damon, please check SkiffUI logs" 
    break 
fi 


#Start npm web server in foreground
echo '----------------------------------'
echo '| Starting front end web server...'
echo '----------------------------------'

npm start --host 0.0.0.0 --port 1027 --disable-host-check

retval = $ ? 
 
if $retval == 0;
then 
    echo '-------' 
    echo '| Done' 
    echo '-------' 
    continue 
else;
    echo "Failed to start web server, please check container logs." 
    break 
fi 