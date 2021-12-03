#!/usr/bin/env python3

# py -m pip install dnspython

import re
import dns.resolver
import dns.reversename

#^10(\.{1}((25[0-5])|(2[0-4][0-9])|(1?[0-9]?[0-9]))){3}$
#^(([a-zA-Z0-9]{1}[\-a-zA-Z0-9]{0,}[a-zA-Z0-9]{1}\.{1}){1,}rzd\.{0,1})$

SourceData =  """
    ya.ru.
    yawdadad1.ru
    2020.kbsh.rzd.ru
    8.8.8.8
    83.234.113.47
    10.64.5.5
    uu-.ru
"""

def validate_IP(OneDNSQuery):
    #return re.match("^10(\.{1}((25[0-5])|(2[0-4][0-9])|(1?[0-9]?[0-9]))){3}$", OneDNSQuery)                                                #IP RZD
    return re.match("^(((25[0-5])|(2[0-4][0-9])|(1?[0-9]?[0-9]))){1}(\.{1}((25[0-5])|(2[0-4][0-9])|(1?[0-9]?[0-9]))){3}$", OneDNSQuery)     #IP Internet

def validate_DNS(OneDNSQuery):
    #return re.match("^(([a-zA-Z0-9]{1}[\-a-zA-Z0-9]{0,}[a-zA-Z0-9]{1}\.{1}){1,}rzd\.{0,1})$", OneDNSQuery)             #DNS RZD
    return re.match("^(([a-zA-Z0-9]{1}[\-a-zA-Z0-9]{0,}[a-zA-Z0-9]{1}\.{1}){1,}[a-zA-Z]{2,}\.{0,1})$", OneDNSQuery)     #DNS internet

def query_to_DNS(addr, query_type):
    if query_type == "NO":
        print("{r:20s} :  {w:15s}".format(r = addr, w = "!!!Bad address!!!"))
        return "Source bad"
    
    if query_type == "PTR":
        q = dns.reversename.from_address(addr)
    else:
        q = addr

    try:
        result_DNS_query = dns.resolver.resolve(q, query_type)
    except dns.resolver.NXDOMAIN:
        print("{:20s} :  {}".format(addr, 'No this adress in DNS'))
        return("XXX")
    except Exception:
         print("{:20s} :  {}".format(addr, 'Error of query to DNS'))
         return("Error")
    else:
        for i in result_DNS_query.response.answer:
            for j in i.items:
                print("{:20s} :  {}".format(addr, j))
        return("OK")

SplitSourceData = SourceData.split()

for OneDNSQuery in SplitSourceData:
    if validate_IP(OneDNSQuery):
        query_to_DNS(OneDNSQuery, 'PTR')
    elif validate_DNS(OneDNSQuery):
        query_to_DNS(OneDNSQuery, 'A')
    else:
        query_to_DNS(OneDNSQuery, "NO")