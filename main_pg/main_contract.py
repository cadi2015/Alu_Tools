import abc
import base_view
import base_presenter


class View(base_view.BaseView):

    @abc.abstractmethod
    def set_presenter(self):
        return

    @abc.abstractmethod
    def show_loading(self):
        return

    @abc.abstractmethod
    def show_success_toast(self,showMessage):
        return

    @abc.abstractmethod
    def show_fail_reason(self):
        return

    @abc.abstractmethod
    def show_devices_info(self):
        return


class Presenter(base_presenter.BasePresenter):

    @abc.abstractmethod
    def start(self):
        return

    @abc.abstractmethod
    def monkey_start(self):
        return

    @abc.abstractmethod
    def monkey_stop(self):
        return

    @abc.abstractmethod
    def query_devices(self):
        return

    @abc.abstractmethod
    def install_apk(self):
        return

    @abc.abstractmethod
    def uninstall_apk(self):
        return

    @abc.abstractmethod
    def select_apk_package(self):
        return
