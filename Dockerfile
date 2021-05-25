FROM python:3.9-slim-buster
ADD snakewatergun.py .
CMD ["python","./snakewatergun.py"]
