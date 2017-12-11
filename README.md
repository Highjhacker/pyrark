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
pip install logzero
```

## Application Example

- [PytharkFlask](https://github.com/Highjhacker/PytharkFlask) - Example of a web application using Flask and Pythark
- [PytharkCLI](https://github.com/Highjhacker/PytharkCLI) - Example of a CLI application using Click and Pythark
## Usage

### Account

```python
from pythark import Account
acc = Account()
print(acc.get_balance("ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9"))

>>> {'success': True, 'balance': '51795878544', 'unconfirmedBalance': '51795878544'}
```

### Block

```python
from pythark import Block
b = Block()
print(b.get_block("570934191207974498"))

>>> {'success': True, 'block': {'id': '570934191207974498', 'version': 0, 'timestamp': 19174464, 'height': 2376065, 'previousBlock': '7483598217382372212', 'numberOfTransactions': 50, 'totalAmount': 15830360775, 'totalFee': 500000000, 'reward': 200000000, 'payloadLength': 1600, 'payloadHash': '04c497e303c9aaa16db51e52b139e87ec19666f7a0e0fb14804ba0dcf0a15932', 'generatorPublicKey': '034682a4c4d2c8c0bc5f966dd422a83d2b433e212ef1f334f82cc3fe4676240933', 'generatorId': 'AdBSvLKPp6pMp5ZDsxkgjFu6KeCokncSMk', 'blockSignature': '304402201eb4097e7de1f2601e82333c040acac6df6458b7d59ec2370904fca42729243b022043d7ee08bf7007c06ec1119d12aa0ffe2895769f05c34fabc39f1c478a882049', 'confirmations': 158928, 'totalForged': '700000000'}}
```

### Delegate

```python
from pythark import Delegate
d = Delegate()
print(d.search_delegates())

>>> {'success': True, 'delegates': [{'username': 'dr10', 'address': 'ANwjGUcVbLXpqbBUWbjUBQWkr4MWVDuJu9', 'publicKey': '031641ff081b93279b669f7771b3fbe48ade13eadb6d5fd85bdd025655e349f008', 'vote': '147614629879279', 'producedblocks': 30607, 'missedblocks': 190}, {'username': 'drusilla', 'address': 'AGzLMjoUiLbccC4YpaDsMRwHaoUwCoorQG', 'publicKey': '038dfc041c7e609f254b2cf38de4b55e02dff9e743497f5cf6b67d49d8e44978ce', 'vote': '0', 'producedblocks': 0, 'missedblocks': 0}]}
```

### Loader

```python
from pythark import Loader
l = Loader()
print(l.get_status())

>>> {'success': True, 'loaded': False, 'now': 2286032, 'blocksCount': 0}
```

### MultiSignature

```python
from pythark import MultiSignature
m = MultiSignature()
print(m.get_pending("02c7455bebeadde04728441e0f57f82f972155c088252bf7c1365eb0dc84fbf5de"))

>>> {'success': True, 'transactions': []}
```

### Peer

```python
from pythark import Peer
p = Peer()
print(p.get_peer("78.229.106.139", 4001))

>>> {'success': True, 'peer': {'ip': '78.229.106.139', 'port': 4001, 'version': '1.0.1', 'errors': 0, 'os': 'linux4.4.0-92-generic', 'height': 2535012, 'status': 'OK', 'delay': 221}}
```

### Signature

```python
from pythark import Signature
s = Signature()
print(s.get_signature_fee())

>>> {'success': True, 'fee': 500000000}
```

### Transaction

```python
from pythark import Transaction
t = Transaction()
print(t.get_transactions(limit=5, orderBy="timestamp"))

>>> {'success': True, 'transactions': [{'id': 'b2ef0adc90e3cf4af5d221350d79c2f2712378e0ef5a71244eecaca4afdc7140', 'blockid': '4195226696324437309', 'type': 0, 'timestamp': -1980252, 'amount': 7350732799999, 'fee': 10000000, 'vendorField': 'Ark', 'senderId': 'AQKk9BwUZjM5fsjYCpreZJ4Ltatrt6ZJBE', 'recipientId': 'AXGVkwNJ3p5ruPJrEGEcwcaSz3THw69Eni', 'senderPublicKey': '0367b6eeef79462803cecff4692f06df379803d055941fb1f0c976097fa054aa03', 'signature': '3044022023eb7496803968e2f0e63d9eb7b0885adc3138ad7582e91ab83eae6a0d0afbcf02207f9d0f3a83179c408b819791dc007e3d5e3f266da81ba57aece6524586be3172', 'asset': {}, 'confirmations': 2533357}, {'id': '44d9d0a3093232b9368a24af90577741df8340b93732db23b90d44f6590d3e42', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AU9BgcsCBDCkzPyY9EZXqiwukYq4Kor4oX', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3045022100ed57f27cabdb01f5398b30e63e3372735ee428e17e95de675c37586b6d1a5c12022062a0040ed189a4adac6c3d105e05180f7c74e8c68ca9912b3c60286c2226f3fa', 'asset': {}, 'confirmations': 2535055}, {'id': '512f1aa00538b24a3ba55d65519d34cea83d753f5b2cebfd7004d5c0eaa7177a', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AeLpRK8rFVtBeyBVqBtdQpWDfLzaiNujKr', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3044022018618cfd5dd1024c0dd7677fdbddcaa6977b57f832eca130583d36480dfa452302202c067556fd93899fb0d18ea28e6f0276a778099cdde3d97d3bb8733dff965a59', 'asset': {}, 'confirmations': 2535055}, {'id': '8bb3997878a6a359f1418cf25f31c84f660e5e6897ebd6d07549ff6a4374a44d', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'ARagsXvdeTHYghaQgJkwbdSkPLZ73qdMkR', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3044022021e056a123b4a6c30e3f30dd68ff56f4cc1a994222cf27ff5b48434947e45f300220424cbc671a54a019cc655d02b2313a324702908a4a05c86bac4ac83029bb01ef', 'asset': {}, 'confirmations': 2535055}, {'id': '30cb724924823c689058c25243d1c213b9cdb8c157eff26ee9c89fc1e705fedd', 'blockid': '4366553906931540162', 'type': 0, 'timestamp': 0, 'amount': 0, 'fee': 0, 'senderId': 'AewxfHQobSc49a4radHp74JZCGP8LRe4xA', 'recipientId': 'AT9xWcPQ8hGYuXZ8aWE57VJFohyX1TTLkH', 'senderPublicKey': '0235d486fea0193cbe77e955ab175b8f6eb9eaf784de689beffbd649989f5d6be3', 'signature': '3045022100fd0ab0bee79152978d8d5835e2d244fa159e4957f48d602c65e35e2383c0d14a022036380dac439784075befef7f7b14734f9ed782e4be5ac7f2f4c49985b08fdce9', 'asset': {}, 'confirmations': 2535055}], 'count': '340315'}
```

### Transport

```python
from pythark import Transport
t = Transport()
print(t.get_status())

>>> {'success': True, 'height': 2535061, 'forgingAllowed': True, 'currentSlot': 2560155, 'header': {'id': '17084042248047495221', 'height': 2535061, 'version': 0, 'totalAmount': 0, 'totalFee': 0, 'reward': 200000000, 'payloadHash': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'payloadLength': 0, 'timestamp': 20481240, 'numberOfTransactions': 0, 'previousBlock': '9903476536476021910', 'generatorPublicKey': '0354319db3f22fb8d4588a09ebbb3e91631cbc2202ba58c69149b75c1a47eb7686', 'blockSignature': '3045022100d7988e19980767d259072d4884f359f95d5ca99bc99d909f70b55b1eadde5921022000b8eb45266a1ad7943d18abe45e5487da680677272a26f7ede78c63a0d545bb'}}
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
        "vendorField", # Vendor field, optionnal
        "secondPassphrase") # Second passphrase, optionnal
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
