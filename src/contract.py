import json
from web3 import Web3
from solc import compile_standard
import random
from typing import Optional


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


def create_contract(location: str, month: int, precipitation: float, address: str):

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

    tx_hash = contract.constructor(location, month, precipitation, address).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    weather_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    month_name = get_month(month)
    utterance = (f'Congrats, you just created a new contract that grants you protection for your crops in {location}, '
                 f'starting from {month_name}; average precipitation in this month are {precipitation} mm.\nAs soon as '
                 f'the evaluation period will be over, the index will be evaluated and payments to either you or '
                 f'the investor who subsidized your contract will be sent out automatically.')
    return tx_hash, tx_receipt, weather_contract, all_accounts, utterance


def getavg(contract):
    out = contract.functions.getAvgPrecipitation().call()
    return out


def getBalance(w3, account):
    # w3.eth.getBalance(w3.eth.defaultAccount)
    bal = w3.eth.getBalance(w3.eth.account)
    return bal
