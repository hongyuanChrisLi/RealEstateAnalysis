#!/bin/bash

echo "Starting Docker with password: "
sudo systemctl start docker &
wait $!

if [ $? = 0 ]
then 
	echo "Starting Splash"
	sudo docker run -d -p 8050:8050 scrapinghub/splash &
	SPLASH_PID=`ps -ef | pgrep -f splash`

	python main.py
	
	sudo kill ${SPLASH_PID}
	echo "Splash stopped"
fi

sudo systemctl stop docker
echo "Docker is stopped"