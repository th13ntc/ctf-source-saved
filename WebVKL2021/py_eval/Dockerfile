FROM python:3.8-slim

RUN useradd -m ctf

WORKDIR /ssti

COPY files/ .

ENV PORT 9997
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

RUN chown -R root:ctf /ssti && \
    chmod 777 /ssti /ssti/app.py


USER ctf
CMD ["/usr/local/bin/python", "/ssti/app.py"]

EXPOSE 9997

