# Dagster Example

## Description

This project was created to showcase the capabilities of Dagster technology as an orchestrator to manage pipelines.

## Setup

You need to install Docker and Docker Compose to run this project.

## Instructions

To run this project, simply execute the following command in your terminal:  

``docker-compose --env-file .env  up --no-deps --build`` 

This command pulls the images for each Dockerfile and runs the four services described in the Docker Compose file.

## The Services

This setup includes four services necessary for Dagster to run. The services are:

* docker_postgresql
* docker_user_code
* docker_webserver
* docker_daemon


When al services are running, you can go to http://0.0.0.0:3000/ amd find the webserver UI to interact with the dags created on dagster


Enjoy it!