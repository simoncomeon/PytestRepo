import pytest
from wallet import Wallet, InsufficientAmout


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Retrurn a Wallet instance with 20 units in balance'''
    return Wallet(20)

@pytest.mark.parametrize("earned, spent, expected",[
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(earned, spent, expected, empty_wallet):
    wallet = empty_wallet
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected

@pytest.mark.parametrize("earned, spent, expected",[
    ('Hello', 10, 20),
])
def test_transactions_and_exceptions(earned, spent, expected, empty_wallet):
    wallet = empty_wallet
    with pytest.raises(TypeError):
        wallet.add_cash(earned)
    with pytest.raises(InsufficientAmout):
        wallet.spend_cash(spent)

def test_default_init_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_add_cash(wallet):
    wallet.add_cash(30)
    assert wallet.balance == 50

def test_spend_cash_insufficient(wallet):
    with pytest.raises(InsufficientAmout):
        wallet.spend_cash(25)

def test_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_type():
    with pytest.raises(TypeError):
        wallet = Wallet("Hello")

def test_transfer_reset(wallet):
    wallet.transfer_reset()
    assert wallet.balance == 0

@pytest.mark.parametrize("my_stock_list, expected_sum", [
    ([10, 20, 30], 120),
    ([0, 10, 20], 60)
    ])
def test_stock_addition_empty_wallet(my_stock_list, expected_sum, empty_wallet):
    wallet = empty_wallet
    wallet.stock_addition(my_stock_list)
    assert wallet.balance == expected_sum

@pytest.mark.parametrize("my_stock_list, expected_sum", [
    ([10, 20, 30], 140),
    ([0, 10, 20], 80),
    ([0, 0, 0], 20)
    ])
def test_stock_addition_initial_value(my_stock_list, expected_sum, wallet):
    wallet.stock_addition(my_stock_list)
    assert wallet.balance == expected_sum

def test_stock_addition_wrong_type(wallet):
    with pytest.raises(TypeError):
        wallet.stock_addition(["hello", "hjel", 3])


