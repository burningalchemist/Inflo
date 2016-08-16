import argparse
import mock
import unittest

import inflo


api_key = 'test_key'
customer_id = 'test_id'
vm_id = 'test_vm_id'
table_format = ['header1', 'header2']

script_args = ['-a', api_key, '-i', customer_id, 'tenant-info']
args = argparse.Namespace(api_key=api_key, customer_id=customer_id, raw=False,
                          url='https://api.flops.ru/api/v1/tenant/', table_format=['id', 'description'])


class TestInflo(unittest.TestCase):
    def setUp(self):
        pass

    def test_inflo_invoke_get_tenant(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_tenant_info(args)
        inflo.get_info.assert_called_with(api_key=api_key, customer_id=customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/tenant/', table_format=['id', 'description'])

    def test_inflo_invoke_server_list(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_server_list(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/vm/', table_format=['id', 'name', 'memory',
                                               'disk', 'cpu', 'ipAddresses', ('2', 'distribution', 'name')])

    def test_inflo_invoke_os_list(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_os_list(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/distribution/', table_format=['id', 'name',
                                              'description', 'bitness'])

    def test_inflo_invoke_get_software(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_software(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/software/', table_format=['id', 'name'])

    def test_inflo_invoke_get_tariffs(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_tariffs(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/tariffs/', table_format=['id', 'name',
                                          'memory', 'disk', 'cpu', 'ipCount', 'onDemand', 'forWindows'])

    def test_inflo_invoke_get_pubkeys(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_pubkeys(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                        url='https://api.flops.ru/api/v1/pubkeys/', table_format=['id', 'name', 'type', 'publicKey',
                             'timeAdded'])
