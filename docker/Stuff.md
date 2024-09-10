## Instructions
- [Full LTS Wiki](https://github.com/SCADA-LTS/Scada-LTS/wiki)
- [Setting It up Instructions](https://github.com/SCADA-LTS/Scada-LTS/wiki/Scada-LTS-docker-compose-tutorial)
- I still need to add .gitignore for docker here so don't commit all those files that get created when you run it

## Setup
- In the directory with the `docker-compose.yml`
- `docker-compose up`

#### To connnect to the terminal
- `docker ps` for the name or id of the scadalts container
- `docker exec -it <container_name/id> /bin/bash` to connect to shell

#### To view the different webpages
- [Scada](http://localhost:8080/Scada-LTS/)
  - username: admin
  - password: admin
- [HiveMQ](http://localhost:8081/)
  - username: admin
  - password: hivemq
