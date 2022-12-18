# FROM python:3.10.8-alpine

# # create the appropriate directories
# ENV APP_HOME=/usr/src/app
# RUN mkdir $APP_HOME

# # install psycopg2 dependencies
# RUN apk update \
#     && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
#     py3-pillow freetype-dev libpng-dev openblas-dev g++ \
#     jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev

# WORKDIR $APP_HOME

# # RUN pip install --upgrade pip
# COPY . $APP_HOME 

# # COPY ./requirements.txt $APP_HOME
# # COPY ./requirements/requirements.txt .
# # COPY ./requirements/requirements.txt $APP_HOME
# # COPY requirements/requirements.txt requirements.txt
# # COPY ./requirements.txt /requirements.txt
# COPY requirements.txt $APP_HOME/requirements.txt


# RUN pip install -r requirements.txt



# # COPY . $APP_HOME

# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "core.wsgi", ":8000"]



FROM python:3.10.8-alpine

# create the appropriate directories
ENV code=/usr/src/app
# RUN mkdir /code

# install psycopg2 dependencies
RUN apk update \
    && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
    py3-pillow freetype-dev libpng-dev openblas-dev g++ \
    jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD ["gunicorn", "core.wsgi", ":8000"]
