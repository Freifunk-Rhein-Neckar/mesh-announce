import providers


class Source(providers.DataSource):
    def call(self, vpn_proto):
        if 'fastd' == vpn_proto:
            return True

    def required_args(self):
        return ['vpn_proto']
