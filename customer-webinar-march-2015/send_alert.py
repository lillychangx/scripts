import os, sys
import time
import hashlib
import hmac, base64
import urllib2, httplib, socket

if len(sys.argv) < 7:
	print "Please provide proper arguments:"
	print "  python %s <device name> <device ip> <metric name> <alert state> <subject> <description>" % (sys.argv[0])
	sys.exit()


# clientTechnology: SEISMICGATEWAY=Vistara Gateway, NCARE=Vistara Gateway"


alertXML = """<Alerts><Alert><deviceName>%s</deviceName><deviceIp>%s</deviceIp><serviceName>%s</serviceName><currentState>%s</currentState><oldState>%s</oldState><subject>%s</subject><description>%s</description><createdTimeString>%s</createdTimeString><ackUrl></ackUrl><clientTechnology>SEISMICGATEWAY</clientTechnology><uniqueId></uniqueId></Alert></Alerts>"""


client_id     = "client_588063"
secret        = "DhhtsnGRfyQvj8bCMzT7vfPhyMkgNcfz"



old_state     = "OK"
current_state = sys.argv[4]
if current_state.lower() == "ok":
	old_state = "Critical"


def httpRequest(url, headers={}, data=None):
    try: 
        http_headers = {
            'Accept'       : 'application/xml'
        }
        http_headers.update(headers)
        req = urllib2.Request(url, data, http_headers)
        return urllib2.urlopen(req)
    except urllib2.HTTPError, emsg:
        raise Exception('httpRequest: HTTPError - ' + str(emsg))
    except urllib2.URLError, emsg:
        raise Exception('httpRequest: URLError - ' + str(emsg))
    except Exception, emsg:
        raise Exception('httpRequest: Exception - ' + str(emsg))

def normalize(data):
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace("\"", "&quot;")
    data = data.replace("'", "") # &#39;
    data = data.replace("\r", "")
    return data


# URL
url = "https://api.vistarait.com/api/%s/alerts" % (client_id)
print "URL: %s" % url




headers = {
	"AuthToken"    : secret,
	"Content-Type" : "application/xml"
}


# Alert Data
alertTime = time.strftime('%F %T', time.gmtime())
alert_data = alertXML % (sys.argv[1], sys.argv[2], sys.argv[3], current_state, old_state, normalize(sys.argv[5]), normalize(sys.argv[6]), alertTime)

print "Alert Content:"
print alert_data


# Post an alert
request = httpRequest(url, headers, alert_data)
response_code = request.getcode()
response_data = request.read()

print "Response Code: ", response_code
print "Response Data: ", response_data
