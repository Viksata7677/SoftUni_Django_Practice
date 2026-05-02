from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'forum_app.accounts'

    def ready(self):
        import forum_app.accounts.signals
