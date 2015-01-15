__author__ = 'air'
import httplib

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
key = raw_input('request: ')
if key == 'phone': key = 'phone'
if key == 'addr': key = 'addr'

if name in people : print "%s's %s is %s." % \
        (name,labels[key],people[name][key])




