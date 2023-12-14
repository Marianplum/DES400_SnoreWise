#pulling python image
FROM python:3.11

#switch working directory
WORKDIR /app

#copy requirements file into image
COPY requirements.txt requirements.txt

#install dependencies and packages in requirements file
RUN pip3 install -r requirements.txt

#copy every content from the local file to the image
COPY . .

#configure the container to run in an executed manner
# ENTRYPOINT [ "python" ]

CMD ["python3", "-m", "flask", "run","--host=0.0.0.0", "--port=9000"]


# docker build -t ___/imagename:tag .
# docker run -d -p 3000:3000 --name sw_con ___/snorewise:0.1 or :latest
# docker images
# docker login
# docker-credential-desktop list
# docker push ____/snorewise:tagname
# docker ps -a