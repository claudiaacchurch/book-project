from lib.user_account import UserAccount

def test_user_account_construction():
    user_acc = UserAccount(1, '1@1.com', 'cc')
    assert user_acc.id == 1
    assert user_acc.email == '1@1.com'
    assert user_acc.username == 'cc'

def test_eq_compares_same_dicts():
    user_acc = UserAccount(1, '1@1.com', 'cc')
    user_acc2 = UserAccount(1, '1@1.com', 'cc')
    assert user_acc == user_acc2

def test_str_format_is_returned():
    user_acc = UserAccount(1, '1@1.com', 'cc')
    assert str(user_acc) == "UserAccount(1, 1@1.com, cc)"