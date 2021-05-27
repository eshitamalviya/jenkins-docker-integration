FROM python:3.9-slim-buster
EXPOSE 8080
ADD snakewatergun.py https://github.com/eshitamalviya/jenkins-docker-integration
CMD ["python","./snakewatergun.py"]
