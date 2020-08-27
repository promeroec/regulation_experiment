from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.50,
    'participation_fee': 10.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'bret',
        'display_name': 'Regulation Experiment',
        'num_demo_participants': 1,
        'app_sequence': ['bret','ball_catch','survey'],
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOM_DEFAULTS = {}

ROOMS = [
    {
        'name': 'excel_lab',
        'display_name': 'EXCEL Lab',
        'participant_label_file': 'excel_lab.txt',
        'use_secure_urls': False,
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'v-qg9l5pk-_t*$&s#^b(vv2$$$_23nqv&dq$c8ikiga1f(oayy'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
