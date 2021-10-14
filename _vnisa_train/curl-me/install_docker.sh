#!/bin/bash

apt-get update
apt-get remove -y docker docker-engine docker.io
apt-get install -y docker.io

systemctl start docker
systemctl enable docker

docker --version
