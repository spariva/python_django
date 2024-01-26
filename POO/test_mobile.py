import pytest
from mobile import MobilePhone as Mob


@pytest.fixture
def phone():
    return Mob('Huawei', 5.3, 8)


def test_mobile_is_built(phone: Mob):
    assert isinstance(phone, Mob)
    assert phone.manufacturer == 'Huawei'
    assert phone.screen_size == 5.3
    assert phone.num_cores == 8
    assert not phone.status
    assert len(phone.apps) == 0


def test_mobile_is_switched_on(phone: Mob):
    phone.power_on()
    assert phone.status


def test_mobile_is_switched_off(phone: Mob):
    phone.power_off()
    assert not phone.status


def test_app_is_installed(phone: Mob):
    phone.install_app('Twitter')
    phone.install_app('Djangos', 'Pyc')
    assert 'Twitter' in phone.apps
    assert 'Pyc' in phone.apps


def test_app_is_not_installed_when_exists(phone: Mob):
    phone.install_app('Twitter')
    phone.install_app('Twitter')
    assert phone.apps.count('Twitter') == 1


def test_app_is_uninstalled(phone: Mob):
    phone.install_app('Twitter')
    phone.uninstall_app('Twitter')
    assert 'Twitter' not in phone.apps


def test_app_is_not_uninstalled_when_not_exists(phone: Mob):
    phone.uninstall_app('Twitter')
    assert 'Twitter' not in phone.apps
