import faircoin_nrp.electrum_fair_nrp as efn

def init_electrum_fair():
    if not hasattr(efn, 'daemon'):
        try:
            daemon = efn.daemon_is_up()
        except:
            msg = "Cannot connect with daemon. Exiting."
            assert False, msg

        if not daemon or (daemon == 'ERROR'):
            return False
        else:
            efn.daemon = daemon

    if not hasattr(efn, 'network') or not efn.network:
        try:
            network = efn.is_connected()
        except:
            msg = "Cannot connect with electrum-server. Exiting."
            assert False, msg
        efn.network = network and (network != 'ERROR')

    return efn.network


def fairwallet_obj():
    if init_electrum_fair():
        return efn
    else:
        return False

def network_fee():
    if not hasattr(efn, 'netfee'):
        if init_electrum_fair() and not efn.netfee:
            network_fee = efn.network_fee()
            if network_fee != 'ERROR':
                efn.netfee = network_fee
                return network_fee
            else:
              efn.netfee = False
        else:
            efn.netfee = False
    else:
        return efn.netfee


def send_fake_faircoins(address_origin, address_end, amount):
    import time
    tx = str(time.time())
    broadcasted = True
    print "sent fake faircoins"
    return tx, broadcasted

def get_address_history(address):
    if init_electrum_fair():
        address_history = efn.get_address_history(address)
        if address_history != 'ERROR':
            return address_history

def get_address_balance(address):
    if init_electrum_fair():
        address_balance = efn.get_address_balance(address)
        if address_balance != 'ERROR':
            return address_balance

def is_valid(address):
    if init_electrum_fair():
        is_valid = efn.is_valid(address)
        if is_valid != 'ERROR':
            return is_valid

def get_confirmations(tx):
    if init_electrum_fair():
        confirmations = efn.get_confirmations(tx)
        if confirmations != 'ERROR':
            return confirmations
    return None, None

def get_transaction_info(tx_hash, address):
    if init_electrum_fair():
        transaction = efn.get_transaction(tx_hash)
        if transaction != 'ERROR':
            amount = 0
            for output in transaction['outputs']:
                if str(output['address']) == address:
                    amount += int(output['value'])

            time = transaction['time']
            return (amount, time)
    return None, None

def is_mine(address):
    if init_electrum_fair():
        is_mine = efn.is_mine(address)
        if is_mine != 'ERROR':
            return is_mine
