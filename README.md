# Introduction 
This project contains all files necessary for setting up a Pybossa instance.

# Getting Started
1. Run `cp .env.tmpl .env` and change the contents of `.env` to your needs. Especially set an postgres password.
2. Install docker and docker-compose, if not already installed: https://docs.docker.com/engine/install/ and https://docs.docker.com/compose/install/. For Ubuntu:
```
curl -fsSL htstps://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker your-user
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
3. [If local development]: Copy over the production database to your local machine:
    1. Log onto the production machine
    2. Run `docker exec [postgres docker container name] pg_dump -U pybossa -F t pybossa | gzip >~/backup/pybossa-$(date +%Y-%m-%d).tar.gz`
    3. Copy the resuling .tar.gz file to your local machine
    4. Start the local database with `docker-compose up -d postgres`
    5. Restore the database with `docker exec -i [postgres docker container name] pg_restore -U pybossa -d pybossa < [.tar.gz file path]`
4. Build and run the composition with `docker-compose up -d`
5. [If local development]: Modify the compose file: Comment out unneeded party from the compose file: nginx-proxy, nginx-proxy-letsencrypt and, if you copied over the production database, db-init.
6. Build and run the composition with `docker-compose up -d`
7. Point your web browser to the machines address. The first registered user will be made admin.

# Trouble Shooting

## Insecure connection error

In this case an error with the nginx proxy might be the source of trouble. For solving it a force-recreate has to be triggered. Docker has not recognized any changes in one of the containers. Hence a recreation of the container and its volume has to be triggered manually by the following command.

```
docker-compose up -d --build --force-recreate
```

## 502 HTTP error

Is triggered when the code includes syntax errors. Check the docker-compose logs for the traceback. When there are no issues check if the pybossa background worker is running. Otherwise it could be the case that this container was started to early. It has to be started after the pybossa container is already running. In this case stop docker-compose and start it again.
