#!/usr/bin/env python3
import connexion
import datetime
import logging

from connexion import NoContent

# Memory-only storage
CATEGORIES = {}
SHOPS = {}


def get_shops(limit, shop_type=None):
    return [shop for shop in SHOPS.values() if not shop_type or shop['shop_type'] == shop_type][:limit]

def get_shop(shop_id):
    shop = SHOPS.get(shop_id)
    return shop or ('Not found', 404)

def put_shop(shop_id, shop):
    exists = shop_id in SHOPS
    shop['id'] = shop_id
    if exists:
        logging.info('Updating shop %s..', shop_id)
        SHOPS[shop_id].update(shop)
    else:
        logging.info('Creating shop %s..', shop_id)
        shop['created'] = datetime.datetime.utcnow()
        SHOPS[shop_id] = shop
    return NoContent, (200 if exists else 201)


def delete_shop(shop_id):
    if shop_id in SHOPS:
        logging.info('Deleting shop %s..', shop_id)
        del SHOPS[shop_id]
        return NoContent, 204
    else:
        return NoContent, 404


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8585, server='gevent')
