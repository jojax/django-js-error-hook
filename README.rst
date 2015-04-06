#######
INSTALL
#######

To install the project from the development::

    $ git clone git://github.com/jojax/django-js-error-hook.git
    $ cd django-js-error-hook
    $ virtualenv env
    $ env/bin/python setup.py develop
    $ cd demo
    $ ../env/bin/python demo/setup.py develop

Then to try the application::

    $ demo runserver

Then access: http://localhost:8000/ - the javascript error will be log in your console.

To install the project in production::

    $ pip install django-js-error-hook

Add django-js-error-hook to your INSTALLED_APPS settings::

    INSTALLED_APPS = (
	    ...
        'django.contrib.staticfiles',
        'django_js_error_hook',
		...
    )

If you want to log the error in the console for development::

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '\033[22;32m%(levelname)s\033[0;0m %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
                },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'javascript_error': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

By default the logger is called "javascript_error", if you want you can define ``JAVASCRIPT_ERROR_ID`` in your settings::

   JAVASCRIPT_ERROR_ID = '<your logger name>'

The view will do csrf validation - if for some reason it doesn't work, set ``JAVASCRIPT_ERROR_CSRF_EXEMPT`` to ``True`` in your settings.

Then install the urls::

    urlpatterns = patterns('',
	    ...
        url(r'^js_error_hook/', include('django_js_error_hook.urls')),
        ...
    )


In your template, simply add the js_error_hook script::

    <script type="text/javascript" src="{% url 'js-error-handler-js' %}"></script>

Now every Javascript error will be logged in your logging error stream. (Mail, Sentry, ...)

Have fun and feel free to fork us and give us feedbacks!
