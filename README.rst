==================
Django Status Page
==================

Django Status Page is a Django plugin which allows you to easily embed status pages into your Django project.

Quick start
-----------
1. Install python packages::

    pip install djangostatuspage

   This will install the plugin and all dependency packages, e.g. Django REST Framework.

1. Add "rest_framework" and "djangostatuspage" to your INSTALLED_APPS setting (``settings.py``) like this::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'djangostatuspage',
    ]

2. Include the API URLconf in your project ``urls.py`` like this::

    path('api/statuspage/', include('djangostatuspage.urls')),

3. Include the UI URLconf in your project ``urls.py`` like this::

    path('ui/', include('djangostatuspage-ui.urls_ui')),

3. Run ``python manage.py migrate`` to create the Status Page models.

4. Start the development server::

    python manage.py runserver

5. To manage your Status Pages, visit the Django Admin at http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled and superuser created).

6. To view actual status page, visit http://127.0.0.1:8000/ui/status-pages/(status-page-id)/

7. Status page API endpoints are available at: http://127.0.0.1:8000/api/statuspage/


