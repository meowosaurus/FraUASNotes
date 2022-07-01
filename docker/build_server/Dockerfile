FROM ubuntu:22.04

# Update repository and install openjdk 17
RUN apt update
RUN apt install -y openjdk-17-jdk
RUN apt clean

# Copy .jar file from host to container
RUN mkdir /server
WORKDIR /server
ADD server.jar /server

# Run server file 
CMD "java -jar server.jar"
