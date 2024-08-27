# Unspendable Pubkey Generator

Generates a verifiably unspendable pubkey for the `secp256k1` elliptic curve using the strategy outlined in [bip0341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki#constructing-and-spending-taproot-outputs).

An unspendable pubkey is a point on the curve whose discrete log is not known with respect to the generator point `G`.
This can be verified by revealing the random scalar `r` used to generate the pubkey by shifting the `NUMS` point.

## Prerequisites

1. Install `sage` as per [these instructions](https://doc.sagemath.org/html/en/installation/).

2. (Optional) Install `poetry` as per [these instructions](https://python-poetry.org/docs/#installation).

## Run

### If `poetry` is installed

```bash
make
```

### If `poetry` is not installed

```bash
sage main.py
```

### Sample run

```plaintext
$ make
poetry run sage main.py
Verifiably Unspendable XOnlyPublicKey using H + rG:
===================================================
XOnlyPubkey: 0x2be4d02127fedf4c956f8e6d8248420b9af78746232315f72894f0b263c80e81
r          : 0x82758434e13488368e0781c4a94019d3d6722f854d26c15d2d157acd1f464723
```
