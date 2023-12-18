from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9d55d!+dj8gh8fjs!d$%9(_2+qbjzcrjwbsn%5f-04zokk17-t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "debug_toolbar",
    "polls.apps.PollsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates" ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# arquivos estáticos fora do app:
# STATICFILES_DIRS = [
#     BASE_DIR / "polls/static/",
#     "arq_estaticos/static/",
# ]

# Passando arquivos estáticos sem usar o "staticfiles do django":
# STATIC_ROOT = "exemplo/static/"

# Adicionando ips internos para depuração:

INTERNAL_IPS = [
    "127.0.0.1"
]

# adicionando personalização ao painél de depuração:

# DEBUG_TOOLBAR_PANELS = [
#     "debug_toolbar.panels.history.HistoryPanel",
# ]

# Adicionando configuração de painel de depuração:

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.profiling.ProfilingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ], # Painéis desabilitados, mas ainda exibidos.
    "INSERT_BEFORE": "</body>", # Tag HTML que a barra de ferramentas se insere antes(lá ele).
    "RENDER_PANELS": None, # Modo de renderização da barra de ferramentas. "true" "false" or "none".
    "RESULTS_CACHE_SIZE": 25, # Quantidade de resultados que serão armazenados na memória.
    "ROOT_TAG_EXTRA_ATTRS": "", # Config inserida no modelo raiz. É usada principalmente para resolver conflitos no lado do cliente em relação a estruturas. Depende do tipo de debugação que está se fazendo, com "angular.js" ficaria "ng-non-bindable". 
    "SHOW_COLLAPSED": False, # Se true, a barra de ferramentas e recolhida.
    "SHOW_TOOLBAR_CALLBACK": "debug_toolbar.middleware.show_toolbar", # Config que define se a barra de ferramentas é exibida ou não, depende se a função passada retorna True ou false.
    "OBSERVE_REQUEST_CALLBACK": "debug_toolbar.toolbar.observe_request", # define se a barra de ferramentas será atualizada ou não em solicitações AJAX;
    "TOOLBAR_LANGUAGE": None, # Idioma da barra de ferramentas.
    "EXTRA_SIGNALS": [], # Adição de sináis extras no painél "signals".
    "ENABLE_STACKTRACES": True, # Config que dá detalhamento aos processos nos painéis Cache e SQL.
    # "ENABLE_STACKTRACES_LOCALS": False, | Se true o detalhamento é mais detalhado.
    "HIDE_IN_STACKTRACES": (
        "socketserver",
        "threading",
        "wsgiref",
        "debug_toolbar",
        "django.db",
        "django.core.handlers",
        "django.core.servers",
        "django.utils.decorators",
        "django.utils.deprecation",
        "django.utils.functional",
    ), # Config que ELIMINA entradas relacionadas com o servidor, evitando atrazo na renderização da barra de ferramentas e estruturas DOM extensas.
    "PRETIFY_SQL": True, # Se true, faz com que os tokens SQL fiquem agrupados, ou seja, faz o alinhamento e o recuo dos tokens.
    "PROFILER_CAPTURE_PROJECT_CODE": True, # Se true, inclúi todas as chamadas de funções do projeto no painél de depuração profile. O código do projeto(Onde se chama as funções), está no caminho definido em "BASE.DIR" de settings.  
    "PROFILER_MAX_DEPTH": 10, # definição da profundiade da chamada de funções na análise de perfil
    "PROFILER_THRESHOLD_RATIO": 8, # definindo um limite para a inclusão de chamadas no peinél de depuração de perfil. Quanto maior o limite, mais funções serão incluidas. Já se o limite for menor, o tempo de renderização será mais rápido, porém, haverá exclusão(perda) de dados.
    "SHOW_TEMPLATE_CONTEXT": True, # Se true, o contexto é incluido junto com o template no painel de renderização de template. Pode ser útil desativar esta função quando se tem contextos grandes demais ou quando estes contextos possuem estruturas de dados preguiçosas e é melhor não analisá-las.
    "SKIP_TEMPLATE_PREFIXES": (
        "django/forms/widgets/", "admin/widgets/"
    ),
    "SQL_WARNING_THRESHOLD": 500, # chamas sql que demorarem mais do que o tempo(milissegundos) definido serão destacadas no painél de depuração do SQL.

}



