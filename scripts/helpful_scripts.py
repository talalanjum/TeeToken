from brownie import (
    accounts,
    network
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev", "rinkeby"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    print(accounts[0])
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
