FROM python:3.12.9

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["sh", "-c", "python train.py && uvicorn main:app --host 0.0.0.0 --port 8989 & streamlit run app_streamlit.py --server.port 8501 --server.address 0.0.0.0"]