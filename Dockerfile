FROM python:3.7

ENV REDIS_SENTINEL=redis-sentinel
ENV REDIS_MASTER=redis-master

RUN set -x && \
    apt-get update && \
    apt-get install -y apt-utils postgresql-client libpq-dev python-psycopg2 libsasl2-dev libldap2-dev libssl-dev

# install python dependencies with pip
# install pybossa from git
# add unprivileged user for running the service
ENV LIBRARY_PATH=/lib:/usr/lib

RUN set -x && git clone --recursive https://github.com/Scifabric/pybossa /opt/pybossa
RUN set -x && cd /opt/pybossa && git checkout tags/v3.1.3
RUN set -x && pip install -U pip setuptools
RUN set -x && cd /opt/pybossa && pip install -r requirements.txt
RUN set -x && pip install uwsgi
RUN set -x && cd /opt/pybossa && rm -rf /opt/pybossa/.git/
RUN set -x && addgroup pybossa
RUN set -x && useradd -g pybossa -s /bin/sh -d /opt/pybossa pybossa
RUN set -x && usermod -p pybossa pybossa

# variables in these files are modified with sed from /entrypoint.sh
ADD alembic.ini /opt/pybossa/
ADD settings_local.py /opt/pybossa/
ADD secrets.json /opt/pybossa/

RUN ln -s /opt/pybossa/pybossa/themes/default/translations /opt/pybossa/pybossa/translations

# TODO: we shouldn't need write permissions on the whole folder
#   Known files written during runtime:
#     - /opt/pybossa/pybossa/themes/default/static/.webassets-cache
#     - /opt/pybossa/alembic.ini and /opt/pybossa/settings_local.py (from entrypoint.sh)
RUN chown -R pybossa:pybossa /opt/pybossa

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# run with unprivileged user
USER pybossa
WORKDIR /opt/pybossa
EXPOSE 8080

# Background worker is also necessary and should be run from another copy of this container
#   python app_context_rqworker.py scheduled_jobs super high medium low email maintenance
CMD ["python", "run.py"]
