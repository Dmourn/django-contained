# django-contained

Running django in containers.

Originally made for testing Clockify with some other services. With a few lines of code it can be made to work with clockify, but the main purpose was to test authentication/integration between different api's. I cut a decent amount out, but should be functional.



## Usage
I use podman, but I will add

If you use docker, you can replace podman with docker for most things with no issue.
I will try to fix my bootleg-compose script to work with docker.

cd into api-test

```
podman build --squash-all -t api-test .
```

Do the same for nginx-base.

You can also copy the config and use it in the standard docker-container, but you must commit this to nginx-base:latest for the script to work (the script is just nice to run it quickly)

```
./bootleg-compose.sh
```

This creates a pod with port 8080 exposed, add all the containers, and allows you to create a superuser account to login.

## Test the api

Classic token auth is present but conflicts with the hard requirements of the dj-oath-toolkit.

1. Go to admin dashboard, add a normal user (you can skip this just add for testing).

2. Go to 'Clockify webhooks' to enter a string, or a 'clockify webhook signing secret' if you want to test againt the clockify api. Then pick a user to asccociate with it

3. Go to 'Accounts' and add an account with id 1,

4. With your tool of choice, query the api with the header (curl & httpie):


```
curl -H 'CLOCKIFY_SIGNATURE: YOUR_STRING_HERE' http://0.0.0.0/api/clockify/accounts/1/

http http://0.0.0.0/api/clockify/accounts/1/ CLOCKIFY_SIGNATURE:YOUR_STRING_HERE

```
