import hmac,hashlib
import time
import urllib
import math
import base64


rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};
endpoint_item_array = {
    "endpoint" : "public/ticker"
};

mt = '%f %d' % math.modf(time.time())
print mt
mt_array = mt.split(" ")[:2];
print mt_array
nonce = mt_array[1] + mt_array[0][2:5];
print nonce

uri_array = dict(endpoint_item_array, **rgParams); # Concatenate the two arrays.
print uri_array
e_uri_data = urllib.urlencode(uri_array);
print e_uri_data

hmac_key = '9607b63c314b905378b70e77f0ef057c'
utf8_hmac_key = hmac_key.encode('utf-8');
hmac_data = '/public/ticker/' + chr(0) + e_uri_data + chr(0) + nonce;
print hmac_data
utf8_hmac_data = hmac_data.encode('utf-8');
print utf8_hmac_data

hmh = hmac.new(bytes(utf8_hmac_key), utf8_hmac_data, hashlib.sha512);
hmac_hash_hex_output = hmh.hexdigest();
print hmac_hash_hex_output
utf8_hmac_hash_hex_output = hmac_hash_hex_output.encode('utf-8');
print utf8_hmac_hash_hex_output
utf8_hmac_hash = base64.b64encode(utf8_hmac_hash_hex_output);
print utf8_hmac_hash

api_sign = utf8_hmac_hash;
utf8_api_sign = api_sign.decode('utf-8');
print utf8_api_sign
