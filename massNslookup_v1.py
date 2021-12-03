# py -m pip install dnspython

import dns.resolver, dns.reversename

strDomains = """
ya.ru
yawdadad1.ru
2020.kbsh.rzd.ru
"""

strIps = """
8.8.8.8
83.234.113.47
"""

domains = strDomains.split()
ips = strIps.split()

for ip in ips:
    addr = dns.reversename.from_address(ip)
    try:
        A = dns.resolver.resolve(addr, 'PTR')
    except dns.resolver.NXDOMAIN:
        print(ip," XXX")
    except Exception:
        print(ip," неизвестная ошибка")
    else:
        for i in A.response.answer:
            for j in i.items:
                print(ip," ",j)



for domain in domains:
    try:
        A = dns.resolver.resolve(domain, 'A')
    except dns.resolver.NXDOMAIN:
        print(domain," 0.0.0.0")
    except Exception:
        print(domain," неизвестная ошибка")
    else:
        for i in A.response.answer:
            for j in i.items:
#                print(domain," ",j.address)
                print(domain," ",j)