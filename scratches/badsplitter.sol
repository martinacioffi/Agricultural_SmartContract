pragma solidity ^0.5.2;

contract BadSplitter {
    
    uint funds;
    address payable sender;
    address payable receiver;
    
    function deposit(address payable other) public payable {
        funds = msg.value;
        sender = msg.sender;
        receiver = other;
    }
    
    function split() public {
        // This can only be called by the recipient
        require(msg.sender == receiver);
        
        // Split the funds
        sender.transfer(funds / 2);
        receiver.transfer(funds / 2);
    }
    
}
