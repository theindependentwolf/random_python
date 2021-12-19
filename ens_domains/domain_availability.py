"""
Script to check if ens domain names are available

Instructions:

1. Register for an account in https://infura.io/
2. Create an app. Get AppID and Secret
3. Set AppID and Secret as Environment Variables. 
export WEB3_INFURA_PROJECT_ID=<>
export WEB3_INFURA_API_SECRET=<>
4. Install web3.py  
$pip3 install web3
"""

from web3.auto.infura import w3
from ens import ENS

NO_OWNER = '0x0000000000000000000000000000000000000000'

ns = ENS.fromWeb3(w3)
domain_names = ['sdfkjhsdg.eth', 'facebook.eth']

for domain in domain_names:
    owner = ns.owner(domain)
    if owner == NO_OWNER:
        print(domain, 'is available.')
    else:
        print(domain, 'is owned by ', owner)

