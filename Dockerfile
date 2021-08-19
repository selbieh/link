FROM python:3.8
LABEL Description="link"
WORKDIR /web
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT "/entrypoint.sh"
