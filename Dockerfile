FROM python:3.11-alpine
WORKDIR app/
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
CMD python3 fitnise_bot

docker image tag echo_bot polat396/echo_bot
   docker push polat396/echo_bot




   docker run -it -d my_first_bot
  docker ps -a
   docker stop my_first_bot
  docker stop flamboyant_ellis

sudo chmod 666 /var/run/docker.sock