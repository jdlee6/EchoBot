FROM python:3
WORKDIR <path of repo>
COPY requirements.txt requirements.txt
ENV TOKEN="Insert Discord Bot Token Here"
ENV APIkey="Insert Coinmarketcap API Key Here"
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./main.py"]
