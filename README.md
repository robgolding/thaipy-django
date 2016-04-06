Django
======

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

Apps are the reason Django is so popular. They're just Python modules, but can be plugged into any project.

When developing a Django project, you create your own apps too!

```sh
$ django-admin startapp meetup
```

Apps contain your `models.py`, `urls.py`, `views.py` etc.
