__author__ = 'air'

people = {
    'shenyubao': {
        'phone': '18601010377',
        'addr': 'ssss'
    },

    'liuxiong': {
        'phone': '18600099999',
        'addr': 'Foverever'
    },

    'sunxinyu': {
        'phone': '186010111111',
        'addr': 'eeee'
    }
}
labels = {

    'phone': 'phone number',
    'addr': 'address'
}
name = raw_input('Name: ')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people : print "%s's %s is %s." % \
        (name. labels[key].people[name][key])

import httplib

conn = httplib.HTTPConnection("www.python.org")
conn.request("REQUEST","/index.html")
r1 = conn.getresponse()
print r1.status,r1.reason

#测试
