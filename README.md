1) first create virtual env
python -m venv venvName

2) put .env file to project

3) install all requirements with command blew
     pip install -r requirements.txt

4) install erlang and docker on your system

5) pull postgres and rabbitmq with docker and run images

6) create container for postgres img:
command: docker run -it -d --name DatabaseName -p 5433:5432 -e POSTGRES_PASSWORD=1234 postgres

7) create container for rabbitmq img:
command: docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -p 15672:15672 rabbitmq:3-management
and then exec inside the container and then login in rabbitmq

8) perform makemigration and migrate 

how to deploy project on ubuntu server using postgresql, rabbitmq, nginx and gunicorn:
 step 1:
     - intall docker on ubuntu server
     - intall erlang on ubuntu server
step 2:
     -clone project from origin 

step 3:
     - run command: sudo docker-compose up -d
     # this command run all services in seprated container based on specified attributes in docker-compose and install requirements of project


configuration of postgresql:
     -exec inside of container and create database, user and GRANT it

configuration of settings.py:
     - value of ALLOWED_HOSTS should be >  ALLOWED_HOSTS = ['your_server_domain_or_IP']
     - value of HOST in DATABASES should equal with name of postgres image in docker-compose
     for example if it is db, value of HOST should equal to db 

configure Nginx to pass traffic to the process:
     - Start by creating and opening a new server block in Nginx’s sites-available directory:
     command: sudo nano /etc/nginx/sites-available/example.conf 
     now copy config of below inside it:
     server {
          listen 80 default_server;
          listen [::]:80 default_server;
          server_name 185.130.78.42;

          location / {
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header Host $host;
                    proxy_set_header X-NginX-Proxy true;
                    proxy_pass http://localhost:8000/;
                    proxy_redirect http://localhost:8000/ https://$server_name/;
          }
     }

     -  Now, you can enable the file by linking it to the sites-enabled directory:
     command: sudo ln -s /etc/nginx/sites-available/example.conf /etc/nginx/sites-enabled

     - now restart nginx by "sudo systemctl restart nginx" then
     test nginx by "sudo nginx -t"

commands that pactical for setup nginx and working with containers:
     docker-compose up -d >> for build from project
     docker rm -f $(docker ps -aq) >> for remove all container
     docker ps >> for see running containers
     docker images >> for see images
     docker rmi imageName >> remove image
     docker stop container id >> for stop a container
     docekr rm containerName >> remove container
     sudo docker logs nginx >> to see logs error of container
     sudo nginx -t >> see logs error of syntax of nginx.conf
     sudo tail -n 100 /var/log/nginx/error.log >> to see errorLog of nginx
     docker-compose logs -f >> display logs of services
     sudo systemctl restart nginx
     sudo systemctl status nginx >> if exist error, show us

