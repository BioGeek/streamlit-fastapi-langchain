FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN useradd -m myuser
USER myuser

CMD ["sh", "-c", "streamlit run --server.port $PORT /app/streamlit_app.py"]
