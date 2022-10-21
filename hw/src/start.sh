docker build -t new_name .
docker run -it --mount type=bind,src=/Users/roman/PycharmProjects/Docker/hw/data,dst=/src/data new_name