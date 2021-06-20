FROM python:3.8

RUN addgroup prometheus
RUN adduser --disabled-password --no-create-home --home /app  --gecos '' --ingroup prometheus prometheus

COPY requirements.txt /app/
COPY unifi/ /app/unifi/
COPY unifi-dump.py unifi-exporter.py unifi-dump-devices-json.py /app/

RUN /usr/local/bin/pip3.8 install -r /app/requirements.txt

EXPOSE 9108

CMD ["/usr/local/bin/python",  "/app/unifi-exporter.py"]
