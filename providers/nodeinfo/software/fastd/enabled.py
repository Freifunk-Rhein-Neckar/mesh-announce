import providers


class Source(providers.DataSource):
    def call(self, vpn_protos):
        if 'fastd' in vpn_protos:
            return True

    def required_args(self):
        return ['vpn_protos']
