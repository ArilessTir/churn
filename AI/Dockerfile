FROM python:3.6

RUN mkdir app 

WORKDIR /app

RUN mkdir App && mkdir Data

COPY App App/
COPY Data Data/
COPY requirements.txt ./

RUN pip install -r requirements.txt


CMD ["uvicorn","App.main:app","--host" ,"0.0.0.0" ,"--port", "3001"]