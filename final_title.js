const Web3 = require("web3");
const quorumjs = require("quorum-js");
const prompt = require('prompt');
var fs = require('fs');

const web3 = new Web3("http://foodchain-node1.etherhost.org:22001")
quorumjs.extend(web3);
var abi = JSON.parse(fs.readFileSync('food3.abi', 'utf-8'));
const contract = new web3.eth.Contract(abi, "0xA4fafbE0ea4823e262b4916EF93CC5A6306A5DBc");

var title = process.argv[2]
contract.getPastEvents("allEvents", {
    fromBlock: 0,
    toBlock: 10000
}).then(function(events){
    events.forEach(function(event){
        if (String(event['returnValues']['title']).includes(title)) {
            console.log(event)
            process.exit()
        }
    })    
}).catch(function(err){console.error(err)});