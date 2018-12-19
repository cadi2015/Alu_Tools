import abc


class BaseView(object):

    @abc.abstractmethod
    def set_presenter(self):
        return

