from scapy.all import *
destination=input('Enter the destination : ')
minPort=int(input('enter min Port : '))
maxPort=int(input('enter max Port : '))

ans,unans = sr(IP(dst=destination)/TCP(sport=RandShort(), dport=(minPort,maxPort)),timeout=0.2)
print('\nUnanswerd packets\n')
unans.summary()
print('\n----------------\n')
print('Answerd packets\n')
ans.summary()