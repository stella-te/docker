COPY ./package.json /package.json


docker-compose.yml


docker build -t getting-started .

cd app/
docker compose logs -f

docker compose up -d

    volumes:
      - ./app:/app


docker compose down --volumes

stella-instruction

stella-just-read-the-instruction

docker image history --no-trunc stella-just-read-the-instruction

docker scan --login
docker scan stella-instruction
docker run -d -v /var/run/docker.sock:/var/run/docker.sock

-v /var/run/docker.sock:/var/run/docker.sock

docker run -dp 3000:3000 stella-just-read-the-instruction
docker run -dp 3000:3000 stella-instruction -v /var/run/docker.sock:/var/run/docker.sock




docker exec -it 30aa7c1f4151 mysql -p todos

docker exec -it 30aa7c1f4151 mysql -u root -p
ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY 'secret';

# log
docker logs -f 295628bc30a1
npx nodemon getting-started/app/src/index.js
************************************************************************************************


# password var
_FILE MYSQL_PASSWORD_FILE

const PORT = process.env.PORT
PORT=9999 node server.js

docker run -dp 3000:3000 \
   -w /app -v "$(pwd):/app" \
   --network todo-app \
   -e MYSQL_HOST=mysql \
   -e MYSQL_USER=root \
   -e MYSQL_PASSWORD=secret \
   -e MYSQL_DB=todos \
   node:18-alpine \
   sh -c "yarn install && yarn run dev"



netshoot
dig mysql

docker run -it --network todo-app nicolaka/netshoot

docker exec -it d2dde3691b8a mysql -u root -p


docker network create todo-app

docker run -d \
     --network todo-app --network-alias mysql \
     -v todo-mysql-data:/var/lib/mysql \
     -e MYSQL_ROOT_PASSWORD=secret \
     -e MYSQL_DATABASE=todos \
     mysql:8.0

************************************************************************************************


docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash
pwd ls

docker stop 31c569c106ac

# bind mount
 docker run -dp 3000:3000 \
    -w /app --mount type=bind,src="$(pwd)",target=/app \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"

docker logs -f d2dde3691b8a

nodemon

docker build -t getting-started .

************************************************************************************************


docker ls

docker stop 31c569c106ac

docker kill 69e439fe471e
docker rm -f 69e439fe471e

docker run -dp 3000:3000 --mount type=volume,src=todo-db,target=/etc/todos stella-just-read-the-instruction
type=bind,src=/path/to/data,target=/usr/local/data

docker run -dp 3000:3000 stella-just-read-the-instruction

docker volume create todo-db

docker volume inspect todo-db

************************************************************************************************

docker run -dp 3000:3000 getting-started

8088:80 80:80
docker run -d -p 8088:80 docker/getting-started

docker tag stella01te/stella-instruction stella-instruction

docker push stella01te/stella-just-read-the-instruction

docker run -dp 3000:3000 stella-just-read-the-instruction
