# bash
cd ~/semaphore/voteresult
sudo docker build -t semaphore/show .
if [ ! "$(docker ps -a | grep result)" ]; then
	sudo docker stop result
fi
sudo docker run --name result -d -p 8884:80 --link redis:redis semaphore/viewresult