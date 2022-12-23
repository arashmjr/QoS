# FROM python:3.10.8-alpine

# # create the appropriate directories
# ENV code=/usr/src/app
# # RUN mkdir /code

# WORKDIR /code

# RUN python -m venv venv
# ENV PATH="venv/bin:$PATH"

# RUN pip install --upgrade pip

# # install psycopg2 dependencies
# # RUN apk update \
# #     && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
# #     py3-pillow freetype-dev libpng-dev openblas-dev g++ \
# #     jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev

# COPY requirements.txt /code/
# # RUN pip install -r requirements.txt
# COPY . /code/

# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     apk add --update --no-cache postgresql-client && \
#     apk add --update --no-cache --virtual .tmp-deps \
#     build-base postgresql-dev musl-dev && \
#     /py/bin/pip install -r requirements.txt && \
#     apk del .tmp-deps && \
#     adduser --disabled-password --no-create-home app

# CMD ["gunicorn", "core.wsgi", ":8000"]



# pull official base image
FROM python:3.9.5-alpine


# create the appropriate directories
ENV APP_HOME=/usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
    py3-pillow freetype-dev libpng-dev openblas-dev g++ \
    jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev

RUN mkdir $APP_HOME
# copy entrypoint-prod.sh
COPY ./build/entrypoint.sh $APP_HOME

COPY ./requirements/production.txt .
RUN pip install -r production.txt
WORKDIR $APP_HOME

# copy project
COPY ./src $APP_HOME/src
COPY ./settings $APP_HOME/settings
# COPY ./certs $APP_HOME/certs
COPY ./manage.py $APP_HOME
COPY ./fixtures $APP_HOME/fixtures
COPY ./core $APP_HOME/core
# COPY ./locale $APP_HOME/locale
RUN addgroup -S app && adduser -S app -G app

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

RUN chmod +x $APP_HOME/manage.py
# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
