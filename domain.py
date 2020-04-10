from config import BatmanDomainOptions

class Domain():
    def __init__(self, mcast_link, mcast_site, ipv4_gateway):
        self.mcast_link = mcast_link
        self.mcast_site = mcast_site
        self.ipv4_gateway = ipv4_gateway

    def get_ipv4_gateway(self):
        return self.ipv4_gateway

    def get_multicast_address_link(self):
        return self.mcast_link

    def get_multicast_address_site(self):
        return self.mcast_site

    def get_interfaces(self):
        raise NotImplementedException()

    def get_provider_args(self):
        return { 'mesh_ipv4': self.get_ipv4_gateway() }

class BatadvDomain(Domain):
    def __init__(self, domconfig):
        self.batman_iface = domconfig.batman_iface
        self.vpn_iface = domconfig.vpn_iface
        super().__init__(domconfig.mcast_link, domconfig.mcast_site, domconfig.ipv4_gateway)

    def get_interfaces(self):
        return [self.batman_iface, self.vpn_iface]

    def get_batman_interface(self):
        return self.batman_iface

    def get_provider_args(self):
        args = super().get_provider_args()
        args.update({ 'batadv_dev': self.get_batman_interface() })
        return args

class DomainRegistry():
    instance = None
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def __init__(self):
        self.domain_by_iface = { }
        self.default_domain = None

    def add_domain(self, dom):
        for iface in dom.get_interfaces():
            self.domain_by_iface[iface] = dom

    def get_domain_by_interface(self, iface):
        if iface in self.domain_by_iface:
            return self.domain_by_iface[iface]
        return None

    def get_interfaces(self):
        return self.domain_by_iface.keys()

    def get_default_domain(self):
        return self.default_domain

    def set_default_domain(self, dom):
        self.default_domain = dom

class DomainType():
    @staticmethod
    def get(name):
        if not name in domain_types:
            raise Exception("Unknown domain type")
        return domain_types[name]

    def __init__(self, name, options, domain_type):
        self.name = name
        self.options = options
        self.domain_type = domain_type

domain_types = {
    'batadv': DomainType('batadv', BatmanDomainOptions, BatadvDomain),
}
