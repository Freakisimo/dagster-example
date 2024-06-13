FROM python:3.10-slim

# Checkout and install dagster libraries needed to run the gRPC server
# exposing your repository to dagster-webserver and dagster-daemon, and to load the DagsterInstancer

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive

ARG DAGSTER_HOME

RUN mkdir -p ${DAGSTER_HOME}

WORKDIR ${DAGSTER_HOME}

# RUN mkdir -p ${DAGSTER_HOME}dags/

# VOLUME "${DAGSTER_HOME}dags/"

COPY dagster.yaml requirements_user_code.txt ${DAGSTER_HOME}

RUN pip install -r ${DAGSTER_HOME}requirements_user_code.txt

# Run dagster gRPC server on port 4000
EXPOSE 4000

# CMD allows this to be overridden from run launchers or executors that want
# CMD ["dagster", "api", "grpc","--module-name","dags","-h", "0.0.0.0", "-p", "4000"]

CMD ["dagster", "code-server", "start","--module-name","dags","-h", "0.0.0.0", "-p", "4000"]