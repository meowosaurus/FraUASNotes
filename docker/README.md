# FraUASNotes - Docker

## Prerequesites
* Docker -> https://docs.docker.com/get-docker/
* git

## Setup Guide
1. Run `git clone https://github.com/meowosaurus/FraUASNotes`
1. Navigate to `FraUASNotes/docker/` 
1. Edit the `docker-compose.yml` file with an editor such as nano
1. Change the mysql root password, mysql username, mysql user password and mysql user database
1. When using nano, exit with control + X and save the file
1. Create folders for your server and mysql data with `mkdir -p server/src mysql`
1. Copy all server files `cp -R ../server/src/main/ ./server/src/`
1. Navigate to `./server/src/main/resources/`
1. Edit file `application.properties`
1. Change the mysql server address, user password and user database. If you like you could also use the mysql root password
1. Run `docker-compose up -d` and wait 10 seconds

Congratulations, you server is now up and running

## SSL
There is a great guide on medium.com on how to set up SSL with your server: https://medium.com/quick-code/spring-boot-how-to-secure-rest-api-with-https-54ec8f0e4796
