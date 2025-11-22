FROM python:3.10-slim
WORKDIR /app
copy . /app
RUN pip install --no-cache-dir requirementes.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]