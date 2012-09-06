#######
INSTALL
#######

To install the project from the development::

    $ git clone git://github.com/jojax/django-js-error-hook.git
    $ cd django-js-error-hook
    $ virtualenv env
    $ env/bin/python setup.py develop
    $ env/bin/python demo/setup.py develop

Then to try the application::

    $ demo runserver

The access : http://localhost:8000/ the javascript error will be log in your console.

To install the project in production::

    $ pip install django-js-error-hook

Add django-js-error-hook to your INSTALLED_APPS settings::

    INSTALLED_APPS = (
	    ...
        'django.contrib.staticfiles',
        'django_js_error_hook',
		...
    )

Then install the urls::

    urlpatterns = patterns('',
	    ...
        url(r'^js_error_hook/', include('django_js_error_hook.urls')),
        ...
    )

In your template, simply add the js_error_hook script::
    
    <script type="text/javascript" src="http://code.jquery.com/jquery.min.js"></script>
    <script type="text/javascript" src="{% url js-error-handler-js %}"></script>

Now every Javascript error will be logged in your logging error stream. (Mail, Sentry, ...)

Have fun and feel free to fork us and give us feedbacks!
