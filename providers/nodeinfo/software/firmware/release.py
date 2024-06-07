import providers
from providers.util import call
from util import remove_enclosing_quotes

class Source(providers.DataSource):
    def call(self):
        return remove_enclosing_quotes(call(['lsb_release','-rs'])[0])
