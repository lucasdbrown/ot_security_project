[Full LTS Wiki](https://github.com/SCADA-LTS/Scada-LTS/wiki)
[Setting It up Instructions](https://github.com/SCADA-LTS/Scada-LTS/wiki/Scada-LTS-on-Docker-tutorial)

## Instructions
```bash
docker pull scadalts/scadalts:latest
docker run -p 81:8080 scadalts/scadalts:latest
```
Then run `docker ps` to get the name/id of the container. `docker exec -it <container_name> bash ` to connect to the bash shell.

go to `http://localhost:81/ScadaBR/` to view the webpage (404 right now).

