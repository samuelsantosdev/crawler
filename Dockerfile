FROM python:3.7-alpine
MAINTAINER Samuel Santos <samuelsantosdev@gmail.com>

#security, we create a user, out of group root to be a main user
RUN addgroup -S infoglobo && adduser -S app -G infoglobo app \
&& mkdir /app && chmod 700 -R /app && chown app:infoglobo -R /app \
&& apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY app /app
COPY docker/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh && chown app:infoglobo /entrypoint.sh \
&& pip install -r /app/requirements.txt && rm /app/requirements.txt

USER app
WORKDIR /app