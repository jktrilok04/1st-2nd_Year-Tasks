from web3 import Web3

def validity(address):
    if Web3.is_address(address):
        return True

    return False

ethereum_address = "0x21a31Ee1afC51d94C2eFcCAa2092aD1028285549"

if validity(ethereum_address):
    print("Valid Ethereum address")
else:
    print("Invalid Ethereum address")


