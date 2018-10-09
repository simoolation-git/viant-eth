import sys
import web3
import argparse

from web3 import Web3

def main():
    
    parser = argparse.ArgumentParser() 
    parser.add_argument('address', metavar='address', type=str, help="address")
    parser.add_argument('--host', help='host url', required=True)
    args = parser.parse_args()    
    address = args.address
    host = args.host

    w3 = Web3(Web3.HTTPProvider(host))
    
    if(w3.isConnected):

      for block_number in range(0, w3.eth.blockNumber):
        block = w3.eth.getBlock(block_number)

        for tx_index in range(0, len(block.transactions)): 
          if(block.transactions[tx_index].to == address):
            block_hash = block.hash
            print('Block: ' + web3.utils.encoding.add_0x_prefix(web3.utils.encoding.to_hex(block_hash)))

            tx = w3.eth.getTransactionFromBlock(block_number, 0)
            tx_hash = tx.hash
            print('Transaction: ' + web3.utils.encoding.add_0x_prefix(web3.utils.encoding.to_hex(tx_hash)))
			
			print('-----')
    else:
      print('sth went wrong with the web3 connecction! please try another host!')

if __name__ == '__main__':
    main()
