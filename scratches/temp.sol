///declare the version you want to use; the ^ signals that we want that version or any higher until smt is broken

pragma solidity ^0.5.2;

/* can also comment like this, a C style comment, which also works for multiline comments */

// contract to store data points (for temperature) -> put a history of temperatures on the blockchain


contract temperatureReading {
    // STORAGE: remains throughout codes below 
    string private location;                           // need to declare upfront the type this variable will have
    address issuer;
    int public tempCelsius;                            // like C++ or like when you start a SQL database 
    uint public time;                                  // time at which we measure the temperature (like a timestamp?) (u is unsigned)
    
    // CODES start here
    constructor(string memory loc) public {            // loc is the location of which we record the temperature 
        location = loc;                                // this is like location = self.loc; this assignment takes 15 to 20 seconds and costs gas 
        issuer = msg.sender;                            // whoever wrote the contract
        setTemperature(24);
    }
    
    function setTemperature(int degrees) public {      // whatever is not a constructor is a function
        tempCelsius = degrees;                         // now is timestamp of the block just mined; bad source of randomess, people can cheat!
        time = now;                                    // can use it as longas there is no payoff attached, else it is very dangerous!
    }
    
    function getTemperature() public view returns (int) {   //view: does not need to be mined, just "viewed"
        return tempCelsius;
    }
    
    /* function getLocation() public view returns (string memory) {
        require(msg.sender == issuer);                   // i will only tell you my location if the sender is the owner
        // the above can be replaced by a modifier so that we first check whether sender == owner, and if it is the case
        // it returns the locations (recall: _; at the end of the modifier!), else it tells you that the sender is not authorized 
        return location;
    } */ 
    
    modifier onlyBy(address _account)
        {
            require(
                msg.sender == _account,
                "Sender is not authorized."
                );
                /* the following _; is replaced by the actual
                function body when the modifier is used 
                (in this case: location) */
                _;
        }
        
    function veryExclusiveLocation() public view onlyBy(issuer) returns (string memory) {
        return location;
    }
    
    /* STRUCT creates a new type that did not exist before, exactly as you define it (kind of like a named tuple, but mutable) */
    
    /* function demoRollback(int z) public {  // functions can also be "payable" 
        if (z == 0):
        revert();          // will revert any change that has happened pretending it never occurred: error message to the EVM
    }                      // EVM will revert to the last states before this transaction was ever run */ 

    /* the function below can do very ugly things with respect to others' accounts */ 
    /* function () public {  // every contract has a default function without a name, that does not do anything 
        
    } */ 
}
