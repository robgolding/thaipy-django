Django
======

## Model View Template

Unlike other frameworks like Rails, which use _Model View Controller_.

**Models** are classes that provide access to the data; Django has a great ORM.

```
class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    date = models.DateField()

Event.objects.filter(
    location=draftboard,
)
```

* **Views** are just functions; class-based views are called as if they are functions.
* **Templates** are files which are used to construct the response; usually HTML (but can be anything).

## Apps

Apps are the reason Django is so popular. They're just Python modules, but can be plugged into any project.

When developing a Django project, you create your own apps too!

```
$ django-admin startapp meetup
```
