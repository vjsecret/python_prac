from contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Used to create a superuser.'
    stealth_options = ('stdin',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()
        print(self.UserModel)