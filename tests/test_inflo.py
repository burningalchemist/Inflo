import argparse
import mock
import unittest

import inflo


api_key = 'test_key'
customer_id = 'test_id'
vm_id = 'test_vm_id'
tenant_id = 'test_tenant_id'
distr_id = 'test_distr_id'
tariff_id = 'test_tariff_id'
public_key_id = 'test_public_key_id'
software_id = 'test_software_id'


table_format = ['header1', 'header2']

script_args = ['-a', api_key, '-i', customer_id, 'tenant-info']
args = argparse.Namespace(api_key=api_key, customer_id=customer_id, raw=False,
                          url='https://api.flops.ru/api/v1/tenant/', table_format=['id', 'description'],
                          vm_id=vm_id, tenant_id=tenant_id, name='Name', distr_id=distr_id, tariff_id=tariff_id,
                          memory='2', disk='1024', cpu='4', ip_count='1', password='password', send_password=True,
                          open_support_access=True, public_key_id=public_key_id, software_id=software_id)


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
                                          url='https://api.flops.ru/api/v1/distribution/',
                                          table_format=['id', 'name', 'description', 'bitness'])

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
                                          url='https://api.flops.ru/api/v1/pubkeys/', table_format=['id', 'name',
                                              'type', 'publicKey', 'timeAdded'])

    def test_inflo_invoke_get_vm_snapshots(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_snapshots(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/vm/{0}/snapshots/'.format(vm_id),
                                          table_format=['id', 'name', 'description', 'bitness', 'parentSnapshotId',
                                               'timeAdded'])

    def test_inflo_invoke_get_vm_backups(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_backups(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                           url='https://api.flops.ru/api/v1/vm/{0}/backups/'.format(vm_id),
                                           table_format=['id', 'size', 'timeAdded'])

    def test_inflo_invoke_get_vm_info(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_info(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/vm/{0}/'.format(vm_id),
                                          table_format=['id', 'name', 'cpu', 'memory', 'disk', 'bandwidth',
                                               'ipAddresses', 'privateIpAddress', 'state', 'timeAdded',
                                                (2, 'distribution', 'name')])

    def test_invoke_store_conf(self):
        inflo.set_conf = mock.MagicMock(return_value=0)
        inflo.parser.invoke_store_conf(args)
        inflo.set_conf.assert_called_with(ext_api=args.api_key, ext_id=args.customer_id)

    def test_invoke_create_vm(self):
        inflo.create_vm = mock.MagicMock(return_value=0)
        inflo.parser.invoke_create_vm(args)
        inflo.create_vm.assert_called_with(args.name, args.tenant_id, args.distr_id, args.tariff_id,
                                           args.memory, args.disk, args.cpu, args.ip_count,
                                           args.password, args.send_password, args.open_support_access,
                                           args.public_key_id, args.software_id,
                                           api_key=args.api_key, customer_id=args.customer_id, raw=args.raw)

    def test_invoke_delete_vm(self):
        inflo.delete_vm = mock.MagicMock(return_value=0)
        inflo.parser.invoke_delete_vm(args)
        inflo.delete_vm.assert_called_with(args.vm_id, args.tenant_id, api_key=args.api_key,
            customer_id=args.customer_id, raw=False)

    def test_invoke_start_vm(self):
        inflo.start_server = mock.MagicMock(return_value=0)
        inflo.parser.invoke_start_vm(args)
        inflo.start_server.assert_called_with(args.vm_id, args.tenant_id, api_key=args.api_key,
            customer_id=args.customer_id, raw=False)
