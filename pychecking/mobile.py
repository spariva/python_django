class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = False
        self.apps = []
        
    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, *args: str):
        for app in args:
            if app in self.apps:
                print(f"{app} already installed!")
            else:
                self.apps.append(app)
        

    def uninstall_app(self, app: str):
        if app not in self.apps:
            print(f"{app} not installed!")
        else:
            self.apps.remove(app)

