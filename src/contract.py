import json
from web3 import Web3
from solc import compile_standard


def create_contract(location, month, precipitation, address):

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

    w3.eth.defaultAccount = w3.eth.accounts[0]

    all_accounts = w3.eth.accounts

    bytecode = compiled_sol['contracts']['contract.sol']['WeatherContract']['evm']['bytecode']['object']

    abi = json.loads(compiled_sol['contracts']['contract.sol']['WeatherContract']['metadata'])['output']['abi']

    WeatherContract = w3.eth.contract(abi=abi, bytecode=bytecode)

    #TODO chamge variables with those got from fucntions

    tx_hash = WeatherContract.constructor(location, month, precipitation, address).transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    weathercontract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
    utterance = 'Congrats, you just created a new contracts with... '
    return tx_hash, tx_receipt, weathercontract, all_accounts, utterance


def getavg(contract):
    out = contract.functions.getAvgPrecipitation().call()
    return out

def getBalance(w3, account):
    # w3.eth.getBalance(w3.eth.defaultAccount)
    bal = w3.eth.getBalance(w3.eth.account)
    return bal
