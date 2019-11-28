pragma solidity ^0.5.2;

contract BadSender {
    
    // function to forward funds to splitter contract
    
    function forward(address payable other) public payable {
    address SplitterContract = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c; 
    BadSplitter() splitter = BadSplitter(SplitterContract);
    splitter.deposit.gas(200000).value(msg.value)(other);
    
    }
    
    function() external {
        // THIS IS EVIL
        revert();
        /* instead of sending money directly out of your own wallet to the bad splitter, you are
        sending it to your own address which is the bad sender */ 
    }
}
