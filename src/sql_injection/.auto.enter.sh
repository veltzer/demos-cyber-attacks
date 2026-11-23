# shellcheck shell=bash
site="mysql"
ENV_DB_USER="root"
ENV_DB_PASSWORD=$(pass show "passwords/${site}/${ENV_DB_USER}")
export ENV_DB_USER
export ENV_DB_PASSWORD
ENV_DB_NAME="demodb"
export ENV_DB_NAME
