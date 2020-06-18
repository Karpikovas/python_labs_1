class Medicament(object):
    vendor_code = None
    name = None
    cost = None
    description = None
    producer_name = None
    producer_country = None


    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def save(self):
        return '{0} {1} {2} {3} {4}'.format(self.vendor_code, self.name, self.cost,
                                            'да' if self.has_prescription else 'нет', self.description)