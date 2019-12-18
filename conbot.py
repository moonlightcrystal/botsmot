from telethon.network import connection
import os
import socks

# prox = ('http://' + os.getenv('TG_USER') + ':' + os.getenv('TG_PASS') + '@' + os.getenv('TG_PROXY'),)

# prox = (socks.HTTP, 'http://' + os.getenv('TG_USER') + ':' + os.getenv('TG_PASS') + '@' + os.getenv('TG_PROXY'), 2000)

# socks.set_default_proxy(proxy_type, config.PROXY_HOST, config.PROXY_PORT, config.PROXY_USER, config.PROXY_PASSWD) 

# prox = socks.set_default_proxy('HTTP', os.getenv('TG_PROXY'), '20000', os.getenv('TG_USER'), os.getenv('TG_PASS'))

# proxy = {
#     'connection': connection.ConnectionHttp,
#     'proxy': prox
# }

proxy = {
  'connection'  : connection.ConnectionTcpMTProxyRandomizedIntermediate,
  'proxy'      : ('blog.themarfa.live', 443, 'dd828b44917e30834040992766a7ed2bbf')
}

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')