FROM continuumio/miniconda3

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port  $PORT --server.address 0.0.0.0