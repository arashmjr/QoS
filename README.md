1) first create virtual env
python -m venv venvName

2) put .env file to project

3) install all requirements with command blew
     pip install -r requirements.txt

4) install erlang and docker on your system

5) pull postgres and rabbitmq with docker and run images

6) run command below:
docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -p 15672:15672 rabbitmq:3-management
and then exec inside the container and then login in rabbitmq

6) perform makemigration and migrate 