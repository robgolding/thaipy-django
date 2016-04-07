Django ("from the ground up")
=============================

> The web framework for perfectionists with deadlines.

* No magic!
* "Batteries included"
  - ORM, database connection handling + migrations
  - Template language
  - Forms
  - Authentication + sessions
  - Static media
  - etc.
* Very stable APIs, long deprecation policies
* Huge developer community

## Model View Template

Unlike other frameworks like Rails, which use _Model View Controller_.

**Models** are classes that provide access to the data; Django has a great ORM.

```py
class Location(models.Model):
    name = models.CharField(max_length=200)

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    date = models.DateField()

draft_board = Location.objects.get(name='DraftBoard')
Event.objects.filter(location=draft_board).count()
```

**Views** are just functions that return an HTTP response.

```py
def index(request):
    return HttpResponse('Welcome to my website!')
```

**Templates** are files which are used to construct the response; usually HTML (but can be anything).

```py
<html>
  <ul>
    {% for event in event_list %}
        <li>{{ event.name }} ({{ event.date }})</li>
    {% endfor %}
  </ul>
</html>
```

## Apps

Apps are the reason Django is so popular. They're just Python modules, but can be plugged into any project. `django-registration` is a great example.

When developing a Django project, you create your own apps too!

Apps contain your `models.py`, `urls.py`, `views.py` etc.

## A Typical Project

```sh
$ django-admin startproject my_project
```

```
├── manage.py
└── thaipy
    ├── meetup
    │   ├── admin.py
    │   ├── migrations
    │   │   └── 0001_initial.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── settings.py
    ├── static
    │   ├── css
    │   ├── img
    │   └── js
    ├── templates
    │   ├── base.html
    │   └── index.html
    └── urls.py
```