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
                          url='https://api.flops.ru/api/v1/tenant/', table_format=['id', 'description'])

args_cvm = argparse.Namespace(name='Name', tenant_id=tenant_id, distr_id=distr_id, tariff_id=tariff_id, memory='1024',
                             disk='2GB', cpu='4', ip_count='1', password='password', send_password=True,
                             open_support_access=True, public_key_id=public_key_id,
                             software_id=software_id, api_key=api_key, customer_id=customer_id, raw=False)

args_vm = argparse.Namespace(vm_id=vm_id, tenant_id=tenant_id, api_key=api_key, customer_id=customer_id, raw=False)


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
                                          url='https://api.flops.ru/api/v1/vm/', table_format=['id', 'name'])

    def test_inflo_invoke_os_list(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_os_list(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/distribution/',
                                          table_format=['id', 'description'])

    def test_inflo_invoke_get_software(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_software(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/software/', table_format=['id', 'name'])

    def test_inflo_invoke_get_tariffs(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_tariffs(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/tariffs/', table_format=['id', 'name'])

    def test_inflo_invoke_get_pubkeys(self):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_pubkeys(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/pubkeys/', table_format=['id', 'publicKey'])

    def test_inflo_invoke_get_vm_snapshots(args):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_snapshots(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/vm/{0}/snapshots/'.format(vm_id),
                                          table_format=['id', 'name'])

    def test_inflo_invoke_get_vm_backups(args):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_backups(args)
        inflo.get_inflo.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                           url='https://api.flops.ru/api/v1/vm/{0}/backups/'.format(vm_id),
                                           table_format=['id', 'size'])

    def test_inflo_invoke_get_vm_info(args):
        inflo.get_info = mock.MagicMock(return_value=0)
        inflo.parser.invoke_get_vm_info(args)
        inflo.get_info.assert_called_with(api_key=args.api_key, customer_id=args.customer_id, raw=False,
                                          url='https://api.flops.ru/api/v1/vm/{0}/'.format(vm_id),
                                          table_format=['id', 'name'])

    def test_invoke_store_conf(args):
        inflo.set_conf = mock.MagicMock(return_value=0)
        inflo.parser.invoke_store_conf(args)
        inflo.set_conf.assert_called_with(ext_api=args.api_key, ext_id=args.customer_id)

    def test_invoke_create_vm(args):
        inflo.create_vm = mock.MagicMock(return_value=0)
        inflo.parser.invoke_create_vm(args)
        inflo.create_vm.assert_called_with(name=args_cvm.name, tenant_id=args_cvm.tenant_id, distr_id=args_cvm.distr_id,
                                           tariff_id=args_cvm.tariff_id, memory=args_cvm.memory, disk=args_cvm.disk,
                                           cpu=args_cvm.cpu, ip_count=args_cvm.ip_count, password=args_cvm.password,
                                           send_password=args_cvm.send_password,
                                           open_support_access=args_cvm.open_support_access,
                                           public_key_id=args_cvm.public_key_id, software_id=args_cvm.software_id,
                                           api_key=args_cvm.api_key, customer_id=args_cvm.customer_id, raw=args_cvm.raw)

    def test_invoke_delete_vm(args):
        inflo.delete_vm = mock.MagicMock(return_value=0)
        inflo.parser.invoke_delete_vm(args)
        inflo.delete_vm.assert_called_with(vm_id=args_vm.vm_id, tenant_id=args_vm.tenant_id, api_key=args_vm.api_key,
                                           customer_id=args_vm.customer_id, raw=args_vm.raw)

    def test_invoke_start_vm(args):
        inflo.start_vm = mock.MagicMock(return_value=0)
        inflo.parser.invoke_start_vm(args)
        inflo.start_vm.assert_called_with(vm_id=args_vm.vm_id, tenant_id=args_vm.tenant_id, api_key=args_vm.api_key,
                                           customer_id=args_vm.customer_id, raw=args_vm.raw)