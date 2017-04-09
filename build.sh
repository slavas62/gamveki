#!/bin/sh
set -e

IMAGE=winsent/fires
docker build -t $IMAGE .
