import json
from web3 import Web3
from solc import compile_standard
import random
from typing import Optional
import pandas as pd


def get_month(num: int) -> Optional[str]:
    d = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
         'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    for m, n in d.items():
        if n == num:
            return m


def create_new_address():
    w3 = Web3(Web3.EthereumTesterProvider())
    n = random.randint(0, len(w3.eth.accounts)-1)
    address = w3.eth.accounts[n]
    return address


def create_contract(location: str, month: int, precipitation: Optional[float], address: str):

    compiled_sol = compile_standard({
        'language': 'Solidity',
        'sources': {
            'contract.sol': {
                'content': '''
                pragma solidity ^ 0.5.2;

    contract WeatherContract {
        string private location;
        address public owner;
        int public mmPrecipitation = 0;
        uint public avgPrecipitation = 0;
        uint public month;

    constructor(string memory _location, uint _month, uint _avgPrecipitation, address _owner) public {
        location = _location;
        month = _month;
        owner = _owner;
        avgPrecipitation = _avgPrecipitation;
        }

    function getStartingMonth() public view returns(uint) {
        return month;
        }

    function setPrecipitation(int _millimeters) public {
        mmPrecipitation = _millimeters;
        }

    function getAvgPrecipitation() public view returns(uint) {
        require(msg.sender == owner);
        return avgPrecipitation;
        }

    function getLocation() public view returns(string memory) {
        require(msg.sender == owner);
        return location;
        }

    function setLocation() public view returns(string memory) {
        require(msg.sender == owner);
        return location;
        }
    }
            '''
            }
        },
        'settings': {
            'outputSelection': {
                '*': {
                    '*': [
                        'metadata', 'evm.bytecode',
                        'evm.bytecode.sourceMap'
                    ]
                }
            }
        }
    })

    w3 = Web3(Web3.EthereumTesterProvider())
    # w3.eth.defaultAccount = w3.eth.accounts[0]
    all_accounts = w3.eth.accounts

    bytecode = compiled_sol['contracts']['contract.sol']['WeatherContract']['evm']['bytecode']['object']
    abi = json.loads(compiled_sol['contracts']['contract.sol']['WeatherContract']['metadata'])['output']['abi']

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor(location, month, int(precipitation), address).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    weather_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    month_name = get_month(month)

    congrats = (f'Congrats, you just created a new contract that grants you protection for your crops in {location}, '
                f'starting from {month_name}; average precipitation for this month are ')

    if precipitation is None or pd.isnull(precipitation):
        precip = 'not available.\n\n'
    else:
        precip = f'{precipitation} mm.\n\n'

    explic = ('As soon as the evaluation period will be over, the index will be evaluated and payments to either you '
              'or the investor who subsidized your contract will be sent out automatically.')
    technical_info = (f'\n\nIn the meanwhile, please note that your address is {tx_receipt.contractAddress}. Store it '
                      f'in a safe location. For this transaction, you used {tx_receipt.gasUsed} gas, and your '
                      f'overall gas consumption amounts to {tx_receipt.cumulativeGasUsed}.')
    greet = '\n\nSee you next time!'
    utterance = congrats + precip + explic + technical_info + greet

    return tx_hash, tx_receipt, weather_contract, all_accounts, utterance


def get_starting_month(contract):
    # NOTE: this has to be called on 'weather_contract'
    out = contract.functions.getStartingMonth().call()
    return out


def get_avg_precipitation(contract):
    out = contract.functions.getAvgPrecipitation().call()
    return out


def get_location(contract):
    out = contract.functions.getLocation().call()
    return out


def get_balance(w3, address):
    bal = w3.eth.getBalance(address)
    return bal
