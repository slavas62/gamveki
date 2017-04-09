#!/bin/sh

set -e

echo resolver $(awk 'BEGIN{ORS=" "} /nameserver/{print $2}' /etc/resolv.conf | sed "s/ $/;/g") > /etc/nginx/resolvers.conf
/env/bin/python manage.py migrate --fake-initial --noinput
/usr/bin/supervisord

