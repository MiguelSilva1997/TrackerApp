FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./auth /auth

CMD ["uvicorn", "auth.main:app", "--host", "0.0.0.0", "--port", "80"]
