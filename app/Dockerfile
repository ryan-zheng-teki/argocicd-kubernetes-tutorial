FROM python:3.8.2
ENV FLASK_APP "/test_flask.py"
RUN pip install Flask
ADD test_flask.py test_flask.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]