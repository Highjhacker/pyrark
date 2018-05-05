![Imgur](https://i.imgur.com/ysh3akS.png)

[![HitCount](http://hits.dwyl.io/Highjhacker/pyrark.svg)](http://hits.dwyl.io/Highjhacker/pyrark) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/Highjhacker/pythark.svg?branch=master)](https://travis-ci.org/Highjhacker/pythark)

# Pythark

Ark API Wrapper in Python.

## Built with
- [Python](https://www.python.org/)
- [Requests](http://docs.python-requests.org/en/master/)

## Installation

Pythark uses Arky to create a new transaction, if you want to use this feature 
you will need to install Arky too. 

Since Arky can works with the nano s ledger now, you need to install these dependencies :

```shell
sudo apt-get install python3-dev libusb-1.0-0-dev libudev-dev
```

```shell
pip install pythark
pip install https://github.com/ArkEcosystem/arky/archive/aip11.zip
```

## Application Example

- [PytharkFlask](https://github.com/Highjhacker/PytharkFlask) - Example of a web application using Flask and Pythark
- [PytharkCLI](https://github.com/Highjhacker/PytharkCLI) - Example of a CLI application using Click and Pythark
## Usage

### Network
Since the version 0.1.3, Pythark can now interact with others network than the main one. If you want
to query on the devnet for example, you will need to specify it like this : 

```python
from pythark import Peer
# It's not mandatory to specify the network, by default the main network will be used.
# So : peer = Peer() is still correct.
peer = Peer("dev") # or peer = Peer(network="dev")
print(peer.get_peers())

>>> {'success': True, 'peers': [{'ip': '167.114.29.62', 'port': 4002, 'version': '1.1.0', 'errors': 0, 'os': 'linux4.4.0-79-generic', 'height': 2056284, 'status': 'OK', 'delay': 33}, 
}...
```

You can use this with all the Pythark functions.

The currently available networks are the following : main, dev, dark, kapu.


### Account

```python
from pythark import Account
acc = Account()
print(acc.get_balance("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9"))

>>> {'success': True, 'balance': '51795878544', 'unconfirmedBalance': '51795878544'}

# If you want to query a balance on the devnet
from pythark import Account
acc = Account("dev")
print(acc.get_balance("DMEvkeU7pNnH5eVDz63GVK6A4CThCmdcpk"))

>>> {'success': True, 'balance': '4688266611418', 'unconfirmedBalance': '4688266611418'}
```

### Block

```python
from pythark import Block
b = Block()
print(b.get_block("570934191207974498"))

>>> {'success': True, 'block': {'id': '570934191207974498', 'version': 0, 'timestamp': 19174464, 'height': 2376065, 'previousBlock': '7483598217382372212', 'numberOfTransactions': 50, 'totalAmount': 15830360775, 'totalFee': 500000000, 'reward': 200000000, 'payloadLength': 1600, 'payloadHash': '04c497e303c9aaa16db51e52b139e87ec19666f7a0e0fb14804ba0dcf0a15932', 'generatorPublicKey': '034682a4c4d2c8c0bc5f966dd422a83d2b433e212ef1f334f82cc3fe4676240933', 'generatorId': 'AdBSvLKPp6pMp5ZDsxkgjFu6KeCokncSMk', 'blockSignature': '304402201eb4097e7de1f2601e82333c040acac6df6458b7d59ec2370904fca42729243b022043d7ee08bf7007c06ec1119d12aa0ffe2895769f05c34fabc39f1c478a882049', 'confirmations': 158928, 'totalForged': '700000000'}}

# If you want to query a block on the dev network :

from pythark import Block
b = Block("dev")
print(b.get_block("5927359504701109797"))

>>> {'success': True, 'block': {'id': '5927359504701109797', 'version': 0, 'timestamp': 23094024, 'height': 2076244, 'previousBlock': '17513022799527103654', 'numberOfTransactions': 4, 'totalAmount': 3320058873, 'totalFee': 40000000, 'reward': 200000000, 'payloadLength': 128, 'payloadHash': '5ff2e3c58a2fe4c3d7c5327ab811d039943e9444dab865853070def0d9f60e1c', 'generatorPublicKey': '0284a88da69cc04439633217c6961d2800df0f7dff7f85b9803848ee02d0743f1d', 'generatorId': 'DRkVSeW5e2zh9v7R5msdLc26fo8axFALGT', 'blockSignature': '3045022100f8e7b6bab48264b77c8f398ff6312a72d4f8698de0328a5a2d0840b481cef3ce02202fb011c0b5883117adf2ab729f7db460abd12e44e275de50547a21bd4e82d3a8', 'confirmations': 18, 'totalForged': '240000000'}}
```

### Delegate

```python
from pythark import Delegate
d = Delegate()
print(d.search_delegates("dr"))

>>> {'success': True, 'delegates': [{'username': 'dr10', 'address': 'ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9', 'publicKey': '031641ff081b93279b669f7771b3fbe48ade13eadb6d5fd85bdd025655e349f008', 'vote': '147614629879279', 'producedblocks': 30607, 'missedblocks': 190}, {'username': 'drusilla', 'address': 'AGzLMjoUiLbccC4YpaDsMRwHaoUwCoorQG', 'publicKey': '038dfc041c7e609f254b2cf38de4b55e02dff9e743497f5cf6b67d49d8e44978ce', 'vote': '0', 'producedblocks': 0, 'missedblocks': 0}]}

# If you want to search for a delegate on the dev network :

from pythark import Delegate
d = Delegate("dev")
print(d.search_delegates("d", limit=1))

>>> {'success': True, 'delegates': [{'username': 'arksidious', 'address': 'DJ4z35JF61d8zkA5B9soUAhg9mYHyLJr2C', 'publicKey': '02ec3f1b7d79d022b5a62a5af97218afd751db2210d1729309cd792c7a4fe92b2e', 'vote': '0', 'producedblocks': 10272, 'missedblocks': 42}]}
```

### Loader

```python
from pythark import Loader
l = Loader()
print(l.get_status())

>>> {'success': True, 'loaded': False, 'now': 2286032, 'blocksCount': 0}

# If you want to get the status on the dev network :

from pythark import Loader
l = Loader("dev")
print(l.get_status())

{'success': True, 'loaded': False, 'now': 1952955, 'blocksCount': 0}
```

### MultiSignature

```python
from pythark import MultiSignature
m = MultiSignature()
print(m.get_pending("02c7455bebeadde04728441e0f57f82f972155c088252bf7c1365eb0dc84fbf5de"))

>>> {'success': True, 'transactions': []}

# If you want to get the pending multi sig on the dev network : 

from pythark import MultiSignature
m = MultiSignature("dev")
print(m.get_pending("026f777ed892898a7c834e4cd9ce7b4c33bf90d2c91a9e67ddaa28de6d60d18ab1"))

>>> {'success': True, 'transactions': []}
```

### Peer

```python
from pythark import Peer
p = Peer()
print(p.get_peer("78.229.106.139", 4001))

>>> {'success': True, 'peer': {'ip': '78.229.106.139', 'port': 4001, 'version': '1.0.1', 'errors': 0, 'os': 'linux4.4.0-92-generic', 'height': 2535012, 'status': 'OK', 'delay': 221}}

# If you want to get a peer on the dev network :

from pythark import Peer
p = Peer("dev")
print(p.get_peer("204.10.184.228", 4002))

>>> {'success': True, 'peer': {'ip': '204.10.184.228', 'port': 4002, 'version': '1.1.1', 'errors': 0, 'os': 'linux4.4.0-98-generic', 'height': 2076293, 'status': 'OK', 'delay': 117}}
```

### Signature

```python
from pythark import Signature
s = Signature()
print(s.get_signature_fee())

>>> {'success': True, 'fee': 500000000}

# Get signature fee on the dev network :

from pythark import Signature
s = Signature("dev")
print(s.get_signature_fee())

>>> {'success': True, 'fee': 500000000}
```

### Transaction

```python
from pythark import Transaction
t = Transaction()
print(t.get_transactions(limit=5, orderBy="timestamp"))

>>> {'success': True, 'transactions': [{'id': 'b2ef0adc90e3cf4af5d221350d79c2f2712378e0ef5a71244eecaca4afdc7140', 'blockid': '4195226696324437309', 'type': 0, 'timestamp': -1980252, 'amount': 7350732799999, 'fee': 10000000, 'vendorField': 'Ark', 'senderId': 'AQKk9BwUZjM5fsjYCpreZJ4Ltatrt6ZJBE', 'recipientId': 'AXGVkwNJ3p5ruPJrEGEcwcaSz3THw69Eni', 'senderPublicKey': '0367b6eeef79462803cecff4692f06df379803d055941fb1f0c976097fa054aa03', 'signature': '3044022023eb7496803968e2f0e63d9eb7b0885adc3138ad7582e91ab83eae6a0d0afbcf02207f9d0f3a83179c408b819791dc007e3d5e3f266da81ba57aece6524586be3172', 'asset': {}, 'confirmations': 2533357}, {'id': '44d9d0a3093232b9368a24af90577741df8340b93732db23b90d44f6590d3e42', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AU9BgcsCBDCkzPyY9EZXqiwukYq4Kor4oX', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3045022100ed57f27cabdb01f5398b30e63e3372735ee428e17e95de675c37586b6d1a5c12022062a0040ed189a4adac6c3d105e05180f7c74e8c68ca9912b3c60286c2226f3fa', 'asset': {}, 'confirmations': 2535055}, {'id': '512f1aa00538b24a3ba55d65519d34cea83d753f5b2cebfd7004d5c0eaa7177a', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AeLpRK8rFVtBeyBVqBtdQpWDfLzaiNujKr', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3044022018618cfd5dd1024c0dd7677fdbddcaa6977b57f832eca130583d36480dfa452302202c067556fd93899fb0d18ea28e6f0276a778099cdde3d97d3bb8733dff965a59', 'asset': {}, 'confirmations': 2535055}, {'id': '8bb3997878a6a359f1418cf25f31c84f660e5e6897ebd6d07549ff6a4374a44d', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'ARagsXvdeTHYghaQgJkwbdSkPLZ73qdMkR', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3044022021e056a123b4a6c30e3f30dd68ff56f4cc1a994222cf27ff5b48434947e45f300220424cbc671a54a019cc655d02b2313a324702908a4a05c86bac4ac83029bb01ef', 'asset': {}, 'confirmations': 2535055}, {'id': '30cb724924823c689058c25243d1c213b9cdb8c157eff26ee9c89fc1e705fedd', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AT9xWcPQ8hGYuXZ8aWE57VJFohyX1TTLkH', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3045022100fd0ab0bee79152978d8d5835e2d244fa159e4957f48d602c65e35e2383c0d14a022036380dac439784075befef7f7b14734f9ed782e4be5ac7f2f4c49985b08fdce9', 'asset': {}, 'confirmations': 2535055}], 'count': '340315'}

# Get the transactions on the dev network :

from pythark import Transaction
t = Transaction("dev")
print(t.get_transactions(limit=5, orderBy="timestamp"))

>>> {'success': True, 'transactions': [{'id': 'e40ce11cab82736da1cc91191716f3c1f446ca7b6a9f4f93b7120ef105ba06e8', 'blockid': '13149578060728881902', 'type': 0, 'timestamp': 0, 'amount': 12500000000000000, 'fee': 0, 'senderId': 'DUFeXjJmYt1mWY3auywA1EQSqfCv5kYYfP', 'recipientId': 'DGihocTkwDygiFvmg6aG8jThYTic47GzU9', 'senderPublicKey': '03cb7bca143376721d0e9e3f3ccb0dc2e7e8470c06e630c3cef73f03e309b558ad', 'signature': '3044022016ecdf3039e69514c7d75861b22fc076496b61c07a1fcf793dc4f5c76fa0532b0220579c4c0c9d13720f9db5d9df29ed8ceab0adc266c6c160d612d4894dc5867eb1', 'asset': {}, 'confirmations': 2076306}, {'id': 'eb0146ac79afc228f0474a5ae1c4771970ae7880450b998c401029f522cd8a21', 'blockid': '13149578060728881902', 'type': 2, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'DNL81CT6WNG1PHjobBmLvKwLV3UUscBymB', 'senderPublicKey': '03e5b39a83e6c7c952c5908089d4524bb8dda93acc2b2b953247e43dc4fe9aa3d1', 'signature': '3045022100e3e38811778023e6f17fefd447f179d45ab92c398c7cfb1e34e2f6e1b167c95a022070c36439ecec0fc3c43850070f29515910435d389e059579878d61b5ff2ea337', 'asset': {'delegate': {'username': 'genesis_1', 'publicKey': '03e5b39a83e6c7c952c5908089d4524bb8dda93acc2b2b953247e43dc4fe9aa3d1'}}, 'confirmations': 2076306}, {'id': 'c9c554056b3428951633a7059dd64dfcbd776fef7f4a156ea362b37ee6ce74c7', 'blockid': '13149578060728881902', 'type': 2, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'DG9LYv5rqX67wuGvGVa9is5k1r86LKCVTA', 'senderPublicKey': '031137050d5fed0b5229b150257da2ac9c135efdf4bcb382b0ad0c197d7be458f4', 'signature': '30440220124baaa04491287d0abbf5a167c9b0f5ac95c22b196f42ff3d275cc9a213c2fd02206e6ebada85f67063e642dbcde6b956f8c99c05f4b9c55f1551d3eebba6375043', 'asset': {'delegate': {'username': 'genesis_3', 'publicKey': '031137050d5fed0b5229b150257da2ac9c135efdf4bcb382b0ad0c197d7be458f4'}}, 'confirmations': 2076306}, {'id': 'c82ccaa16be0e3c7ff4a53e2807968b71a0d88115223c3af2eb320f32449ac32', 'blockid': '13149578060728881902', 'type': 2, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'DMSwarrHg5N9ZAZ6nsqPuUjyAU6gdRAM9d', 'senderPublicKey': '037def83d085778d7767a182a179f345207953441089081f5bc13f86d3891308aa', 'signature': '3045022100900cea3c2df393414899c9d74db57d89c9f311c70d08b974d0fd4a98bfae2fc902204a2aa51a1ec71da27c26afc033de6bd2d15978813c120c95e1a4dafca75ce876', 'asset': {'delegate': {'username': 'genesis_4', 'publicKey': '037def83d085778d7767a182a179f345207953441089081f5bc13f86d3891308aa'}}, 'confirmations': 2076306}, {'id': 'ee6a19fff622ab4e6e96d159396de56d6034b4b18a9cf5c99efcf4e61b28e15a', 'blockid': '13149578060728881902', 'type': 2, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'DFcYHfCwhGWcBNy6cp48wy5SfXbQmfBYgT', 'senderPublicKey': '033f28ad2e9b897d46f1e67c7c52070e9ca46b04c0679ebb21fb236719e38aade3', 'signature': '30440220285188d8900cd3cffccf5e1de305b18856451dd04d2ed21165dffe9a7ce4afc1022009457be6bfe536971697105d47ad1f829738a5cacdb27a23c5d1e8a8dddf3ebd', 'asset': {'delegate': {'username': 'genesis_5', 'publicKey': '033f28ad2e9b897d46f1e67c7c52070e9ca46b04c0679ebb21fb236719e38aade3'}}, 'confirmations': 2076306}], 'count': '142386'}
```

### Transport

```python
from pythark import Transport
t = Transport()
print(t.get_status())

>>> {'success': True, 'height': 2535061, 'forgingAllowed': True, 'currentSlot': 2560155, 'header': {'id': '17084042248047495221', 'height': 2535061, 'version': 0, 'totalAmount': 0, 'totalFee': 0, 'reward': 200000000, 'payloadHash': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'payloadLength': 0, 'timestamp': 20481240, 'numberOfTransactions': 0, 'previousBlock': '9903476536476021910', 'generatorPublicKey': '0354319db3f22fb8d4588a09ebbb3e91631cbc2202ba58c69149b75c1a47eb7686', 'blockSignature': '3045022100d7988e19980767d259072d4884f359f95d5ca99bc99d909f70b55b1eadde5921022000b8eb45266a1ad7943d18abe45e5487da680677272a26f7ede78c63a0d545bb'}}

# Get the status on the dev network : 

from pythark import Transport
t = Transport("dev")
print(t.get_status())

>>> {'success': True, 'height': 2076312, 'forgingAllowed': True, 'currentSlot': 2886837, 'header': {'id': '8062806100428564762', 'height': 2076312, 'version': 0, 'totalAmount': 0, 'totalFee': 0, 'reward': 200000000, 'payloadHash': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'payloadLength': 0, 'timestamp': 23094688, 'numberOfTransactions': 0, 'previousBlock': '3568461414597517092', 'generatorPublicKey': '02dc13fcb190bcfbe9e7ecfc6269635ed2c497a75bab471f2b15c1a99897da97b3', 'blockSignature': '304402202168ab17061e91b15193d4acbdcbf73c4a12a5380161b3359f9abfed9dc24f6702201435e6f13da3b46109c1c1621b147939c74fa5b61b348c86202fb0cf87528878'}}
```

Creating a new transaction : 

```python
from pythark import Transport
transport = Transport()
resp = transport.post_transaction(
        "dark", # Network
        "DDvQqwqPXKd5P8dLAroFsnKR5Q3tKUtvnp", # RecipientAddress
        1000000, # Amount
        "firstPassphrase", # First passphrase, mandatory
        "vendorField", # Vendor field, optional
        "secondPassphrase") # Second passphrase, optional
```

## TODOS

- [x] Core code.
- [x] Write documentation.
    - [ ] Basic docs written, need to polish.
- [x] Unit testing.
    - [ ] Check if it can be better.
- [x] Package it.
    - [ ] Seems OK right now, distributed on PyPi, but have to be sure it's OK for everyone on
          X python version and differents OS.
- [x] Travis.
    - [ ] Missing support for python 3.2.
    - [ ] OSX Support ?
    - [ ] Windows support ?
- [ ] Better errors handling for the models methods.
- [x] Sample flask app.
- [x] Sample CLI app.
- [ ] Integrate it to the DiscArk bot.
- [x] Allow to post a new transaction.
- [x] Allow to specify a network to use (so we can query on the devnet, mainnet, ..)
    - [ ] Functionnal but can be better.

## Authors

- Jolan Beer - Highjhacker

## License

pythark is under MIT license. See the [LICENSE file](https://github.com/Highjhacker/pythark/blob/master/LICENSE) for more informations.
