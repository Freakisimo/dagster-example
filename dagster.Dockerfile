
# Dagster libraries to run both dagster-webserver and the dagster-daemon. Does not
# need to have access to any pipeline code.

FROM python:3.10-slim

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive

# Set $DAGSTER_HOME and copy dagster instance and workspace YAML there
# ENV DAGSTER_HOME=/opt/dagster/dagster_home/

ARG DAGSTER_HOME

RUN mkdir -p ${DAGSTER_HOME}

COPY dagster.yaml workspace.yaml requirements_dagster.txt ${DAGSTER_HOME}

RUN pip install -r ${DAGSTER_HOME}requirements_dagster.txt

WORKDIR ${DAGSTER_HOME}