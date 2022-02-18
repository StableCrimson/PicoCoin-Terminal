# Preface

This project started with a simple question: **"This 'blockchain' thing is really important to crypto. How does blockchain work?"** After watching a phenomenal explanation of the concept and execution on YouTube, I decided to give it a shot. So I wrote a simple blockchain in Python. "Cool," I thought. "What if I could make transactions myself, instead of hard-coding the debug ones?" So I added that. "What if I could view the previous transactions?" So I added that. "What if it was a menu-driven program that had user management, authentication, key generation/verificiation, and balance tracking?" So I added that. This project outgrew it's scope within a matter of hours. It was built with one intention, and each new feature I dreamt up had to be adapted more and more to work with my increasingly archaic code. So it's time for a complete rewrite. Start from scratch with a whole host of new QoL and security features in mind. This commit marks the transition from an ad-hoc crypto wallet that's the result of a bunch of code thrown on top of a blockchain demo, to something more: ***PicoCoin Terminal V1***

## What's new in this dev build?

- Updated some of the code with the new 'match' statement added in Python 3.10

## What's new in V1?

- Terminal clearing and colored text. Adds a lot more cleanliness and polish to the user experience.
- Completely redesigned menu system. Once a user logs in, they stay logged in until they decide to log out.
- Users have the ability to deposit, withdraw, and delete their accounts. Account deletion cannot be done until the user has a balance of 0.
- The public key of a user is no longer generated solely from the private key, so users with the same password won't have the same public keys.
- Withdraws cannot be completed if the amount they are withdrawing is larger than their account balance.
- User balance is displayed right on their home page.
- All operations involving users (Creating, verifying, deleting, balance updating, etc.) is based entirely within the reading and writing of CSV files. Userbase is no longer based in memory.
- Blocks are now recorded in a file, and all previous blocks are references from the file as well.
- Blocks are now much more secure and include more information including, but not limited to: Timestamp, transaction index, and transaction type.
- Deposits and withdraws are now logged in the blockchain. They are also passed through a transaction handler instead of being handled by the userbase manager.
- Transactions between users are now possible, and are logged in the blockchain as well.
- Transaction history is now available. When viewing history, only transactions that involve you will be shown, public key will be replaced with your username to increase readability.
- Structure of a transaction in the history view is vastly improved upon, including the transaction type, amount, timestamp, and transaction index.
- Added requirements.txt

## Features I want to include in V1 and beyond:

- Move terminal formatting to the 'rich' library.
- Cryptography, all data written to files is encrypted, and all data read to files is decrypted.
- Friends list. If users are considered friends, you can use their username instead of the public key and their key will autopopulate for your. Ex: Instead of typing ***2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683***, you could just type ***Jacob*** and the key would populate itself.
- Verification. Like a real blockchain, users have a public record, and by computing and comparing with one another, they verify that transactions are legitimate before the block is hashed and added to the chain.
- Fractions of a PC?
- Mulitple accounts "Checking - Savings"?
- Interest rates?
- Last, certainly not least, and certainly not in V1: A full GUI built on something like PyQt5, PyGUI, or Kivy.

### PicoCoin Terminal is built with the following dependencies:

- csv
- termcolor
