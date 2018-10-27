import logging, time, re, base64

logging.basicConfig(format='[%(levelname)s]%(filename)s - %(funcName)s: %(message)s', level=logging.DEBUG)


def bin_to_hex_str(data):
    return data.hex()


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    return base64.standard_b64decode(data)


def get_time():
    return int(time.time() * 1000)


def get_ss_check_item_by_scheme(scheme):
    config = {}
    mode = None
    if (scheme.startswith('ssr://')):
        mode = 'ssr'
    if (scheme.startswith('ss://')):
        mode = 'ss'
    if not mode:
        raise Exception('not support scheme')
    scheme = re.sub('ssr://|ss://', '', scheme)
    content = str(decode_base64(scheme), 'utf-8')
    logging.debug(content)
    if mode == 'ssr':
        base_config_arr = content.split('/?')[0].split(':')
        external_config_arr = content.split('/?')[1].split('&')
        config['service_ip'] = base_config_arr[0]
        config['service_port'] = base_config_arr[1]
        config['protocol'] = base_config_arr[2]
        config['method'] = base_config_arr[3]
        config['obfs'] = base_config_arr[4]
        config['password'] = base64.standard_b64decode(base_config_arr[5])
        external_config_dict = {v.split('=')[0]: v.split('=')[1] for v in external_config_arr}
        if 'obfsparam' in external_config_dict:
            config['obfs_param'] = external_config_dict['obfsparam']
        if 'protoparam' in external_config_dict:
            config['protocol_param'] = external_config_dict['protoparam']
        return config
    else:
        raise Exception('no support scheme')


def get_tornado_event_name(event):
    dt = {
        0: 'NONE',
        1: 'READ',
        4: 'WRITE',
        24: 'ERROR'
    }
    return dt[event]
