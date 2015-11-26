
from .models import StatisticalValue

class AlreadyRegistered(Exception):
    pass


class InvalidField(Exception):
    pass


class InvalidMethod(Exception):
    pass


class Statistic(object):
    
    def __init__(self):
        self._registry = {}
        self._statistics = {
            'count': self._get_count,
        }
    
    def _get_count(self, model, field = 'id'):
        """Method to get the count of `field` from `model`"""
        if field != 'id':
            raise InvalidField("Expecting the field to be `id`")
        return model.objects.count()
        
    def get_statistic(self, label):
        model, field, method, graph = self._registry[label]
        return self._statistics[method](model, field)
    
    def update(self, save=True):
        out = {}
        for label in self._registry:
            value = self.get_statistic(label)
            out[label] = value
            if save:
                StatisticalValue.objects.create(
                    label = label,
                    model = self._registry[label][0].__module__,
                    field = self._registry[label][1],
                    method = self._registry[label][2],
                    value = value
                )
        return out
        
    def get_graphing(self):
        """Returns a list of the statistics to graph"""
        tograph = []
        for label in self._registry:
            if self._registry[label][-1] > 0:
                tograph.append((label, self._registry[label][-1]))
        return [_[0] for _ in sorted(tograph, key=lambda tup: tup[1])]
    
    def register(self, label, model, field='id', method="count", graph=False):
        """
        Registers the given model(s) with the given admin class.
        """
        if label in self._registry:
            raise AlreadyRegistered(
                'The model %s is already registered as %s' % (model.__name__, label)
            )
        if method not in self._statistics:
            raise InvalidMethod(
                'Invalid statistical method `%s`. Valid values are: %s' % (method, ",".join(self._statistics))
            )
        # Instantiate the admin class to save in the registry
        self._registry[label] = (model, field, method, graph)

statistic = Statistic()
