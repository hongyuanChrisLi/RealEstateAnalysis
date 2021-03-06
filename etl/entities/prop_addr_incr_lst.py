from pyusps.address_information import OrderedDict
from ..routines.addr_verf_etl import AddrVerfEtl


class PropAddrIncrLst:

    def __init__(self):
        self.incr_lst = []

    def parse(self, sel_rows):

        for (mls_id, area_id, addr, city, state, url) in sel_rows:
            addr_dict = dict([
                ('address', addr),
                ('city', city),
                ('state', state),
            ])
            record = {
                'mls_id': mls_id,
                'area_id': area_id,
                'addr_dict': addr_dict,
                'url': url
            }
            self.incr_lst.append(record)

        addr_verf_etl = AddrVerfEtl()
        usps_addr_dict_lst = addr_verf_etl.verify(self.__get_addr_dict_lst__())
        self.__update_incr_lst__(usps_addr_dict_lst)

    def get_incr_inserts(self):

        inserts = []
        for rec in self.incr_lst:
            value = {
                'mls_id': rec.get('mls_id'),
                'area_id': rec.get('area_id'),
                'addr': rec.get('addr_dict').get('address'),
                'url': rec.get('url')
            }
            inserts.append(value)
        return inserts

    def __get_addr_dict_lst__(self):
        addr_dict_lst = []
        for rec in self.incr_lst:
            addr_dict_lst.append(rec['addr_dict'])

        return addr_dict_lst

    def __update_incr_lst__(self, addr_dict_lst):

        lst_len = len(self.incr_lst)
        for i in range(lst_len):
            if isinstance(addr_dict_lst[i], OrderedDict):
                self.incr_lst[i]['addr_dict'] = addr_dict_lst[i]