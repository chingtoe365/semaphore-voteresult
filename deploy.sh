#!/bin/bash
cd semaphore/show && sudo docker build -t semaphore/viewresult .
if [ "$(sudo docker ps -a | grep result)" ]; then
	sudo docker stop result
	sudo docker rm result
fi
sudo docker run --name result -d -p 8884:80 --link redis:redis semaphore/viewresult