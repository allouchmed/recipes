# Recipes ![CI](https://github.com/vabene1111/recipes/workflows/Continous%20Integration/badge.svg?branch=develop)
Recipes is a Django application to manage, tag and search recipes using either built in models or external storage providers hosting PDF's, Images or other files.

![Preview](docs/preview.png)

### Features

- :package: **Sync** files with Dropbox and Nextcloud (more can easily be added)
- :mag: Powerful **search** with Djangos [TrigramSimilarity](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/search/#trigram-similarity)
- :label: Create and search for **tags**, assign them in batch to all files matching certain filters
- :page_facing_up: **Create recipes** locally within a nice, standardized web interface 
- :iphone: Optimized for use on **mobile** devices like phones and tablets
- :shopping_cart: Generate **shopping** lists from recipes
- :calendar: Create a **Plan** on what to eat when
- :person_with_blond_hair: **Share** recipes with friends and comment on them to suggest or remember changes you made
- :whale: Easy setup with **Docker**
- :art: Customize your interface with **themes**
- :heavy_plus_sign: Many more like recipe scaling, image compression, cookbooks, printing views, ...

This application is meant for people with a collection of recipes they want to share with family and friends or simply store them in a nicely organized way. A basic permission system exists but this application is not meant to be run as a public page.

# Documentation

Most things should be straight forward but there are some more complicated things.
##### Storage Backends
A `Storage Backend` is a remote storage location where files are stored. To add a new backend click on `Storage Data` and then on `Storage Backends`. There click the plus button.

Enter a name (just a display name for you to identify it) and an API access Token for the account you want to use.
Dropboxes API tokens can be found on the [Dropboxes API explorer](https://dropbox.github.io/dropbox-api-v2-explorer/#auth_token/from_oauth1)
with the button on the top right. For Nextcloud you can use a App apssword created in the settings.

##### Adding Synced Paths
To add a new path from your Storage backend to the sync list, go to `Storage Data >> Configure Sync` and select the storage backend you want to use.
Then enter the path you want to monitor starting at the storage root (e.g. `/Folder/RecipesFolder`) and save it.

##### Syncing Data
To sync the recipes app with the storage backends press `Sync now` under `Storage Data >> Configure Sync`.
##### Import Recipes
All files found by the sync can be found under `Manage Data >> Import recipes`. There you can either import all at once without modifying them or import one by one, adding tags while importing.
##### Batch Edit
If you have many untagged recipes, you may want to edit them all at once. To do so, go to
`Storage Data >> Batch Edit`. Enter a word which should be contained in the recipe name and select the tags you want to apply.
When clicking submit, every recipe containing the word will be updated (tags are added).

> Currently the only option is word contains, maybe some more SQL like operators will be added later.

## Installation

### Docker-Compose
1. Clone this repository to your desired install location
2. Choose one of the included `docker-compose.yml` files [here](https://github.com/vabene1111/recipes/tree/develop/docs/docker).
3. Copy it to the root directory (where this readme is)
4. Start the container (`docker-compose up -d`)
5. This time and **on each update** run `update.sh` to apply migrations and collect static files
6. Create a default user by executing into the container with `docker-compose exec web_recipes sh` and run `python3 manage.py createsuperuser`.

### Manual
Copy `.env.template` to `.env` and fill in the missing values accordingly.  
Make sure all variables are available to whatever serves your application.

Otherwise simply follow the instructions for any django based deployment
(for example [this one](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)).

## Updating
0. Before updating it is recommended to **backup your database**
1. Stop the container using `docker-compose down`. 
2. Pull the project files and start the container again using `docker-compose up -d --build`.
3. Run `update.sh`

## Contributing
Pull Requests and ideas are welcome, feel free to contribute in any way.
For any questions on how to work with django please refer to their excellent [documentation](https://www.djangoproject.com/start/).

## License
This project is licensed under the MIT license. Even though it is not required to publish derivatives, I highly encourage pushing changes upstream and letting people profit from any work done on this project.
