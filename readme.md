
1. First clone the project using git clone.
2. Next ```$ cd cms```

```
pip install -r requirements.txt
```

```bash
$ python manage.py runserver
```

The following paths are used for following backend purposes:

1. `/register/` to register a new user
2. `/login/` to login a new user and get authenitication token
3. `category/` to add a new category for content
4. `content/` to create a new piece of content
5. `list-content` to view the list of content from a particular user/author.
6. `admin-list-content` to view all the available content
7. `admin-update-content/<key>/` to update content with primary key as `key`
8. `admin-delete-content/<key>` to delete the content with primary key as key
9. `delete-content/<key>/` to delete a content item with primary key as `key` by author
10. `search` to search content with matching values

Use postman or django-rest-framework interface for testing.