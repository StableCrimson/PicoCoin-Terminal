# Preface

This project started with a simple question: **"This 'blockchain' thing is really important to crypto. How does blockchain work?"** After watching a phenomenal explanation of the concept and execution on YouTube, I decided to give it a shot. So I wrote a simple blockchain in Python. "Cool," I thought. "What if I could make transactions myself, instead of hard-coding the debug ones?" So I added that. "What if I could view the previous transactions?" So I added that. "What if it was a menu-driven program that had user management, authentication, key generation/verificiation, and balance tracking?" So I added that. This project outgrew it's scope within a matter of hours. It was built with one intention, and each new feature I dreamt up had to be adapted more and more to work with my increasingly archaic code. So it's time for a complete rewrite. Start from scratch with a whole host of new QoL and security features in mind. This commit marks the transition from an ad-hoc crypto wallet that's the result of a bunch of code thrown on top of a blockchain demo, to something more: ***PicoCoin Terminal V1***

## What's new in this dev build?

- Updated *requirements.txt*
- Begun the move from *termcolor* to *rich*
- Menus are changed, and will be subject to change in the future
- Transaction history is now tabular, and it's orders of magnitude nicer.
- The timestamps on the transaction history are now processed into a far more readable format
- The mining process now has a status spinner, just a nice little touch.
- Cryptography is working, but not integrated into the Resource Manager yet.

## Features I want to include in V1 and beyond:

- Move terminal formatting to the 'rich' library.
- Completely remaster or scrap the *TerminalManager*
- Work more with layouts and menus
- Get the user email address
- Implement a username feature
- Use rich prompts instead of regular text input
- Maybe QR code feature if the zbar library starts playing nice with Python 3.10
- Cryptography, all data written to files is encrypted, and all data read to files is decrypted.
- Friends list. If users are considered friends, you can use their username instead of the public key and their key will autopopulate for your. Ex: Instead of typing ***2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683***, you could just type ***Jacob*** and the key would populate itself.
- Verification. Like a real blockchain, users have a public record, and by computing and comparing with one another, they verify that transactions are legitimate before the block is hashed and added to the chain.
- Fractions of a PC?
- Mulitple accounts "Checking - Savings"?
- Interest rates?
- Last, certainly not least, and certainly not in V1: A full GUI built on something like PyQt5, PyGUI, or Kivy.

### PicoCoin Terminal is built with the following dependencies:

- csv
- rich