# Time Tracking
built for trying Clockify api. A time tracking service.

they say they use 'webhook secrets'

I will let the reader decide if this is an accurate description. I followed the docs, and asked support about it.


After making an admin account. You can add data using the django-admin drop down menus.

To test the api:

1. Go to admin dashboard, add a normal user (if you have problem call the user clock as I may have hardcoded that (: ).

2. Go 'Clockify webhooks' to enter a string, or a 'clockify webhook signing secret' if you want to test againt the clockify api.

3. With your tool of choice, query the api with the header:

```
curl -H 'CLOCKIFY_SIGNATURE: YOUR_STRING_HERE' http://0.0.0.0/api/
```

## Environmental Variables

DJ_DB_USER
DJ_DB_PASSWORD

DJ_DB_HOST
DJ_DB_NAME




No data gets loaded,


