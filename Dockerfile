FROM python:3.8
WORKDIR /code
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "./bank_bot.py"]