<h1 align="center">Welcome to Elyadata_scraper 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="test" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://twitter.com/abhd96" target="_blank">
    <img alt="Twitter: abhd96" src="https://img.shields.io/twitter/follow/abhd96.svg?style=social" />
  </a>
</p>

> This a repository for the testing phase of Elyadata. It is an api to scrape public pages from facebook and save the data into a postgres database. 

## Install
To deploy the API we use docker-compose:
```sh
docker-compose -f stack.yml up -d
```
![Deployment](./image/container.jpg)

## Usage
Use postman to send requests to the API.
Request body:
```sh
{
  "page": name of the page,
  "number_pages": number of pages to scrape

}
```
![Postman Example](./image/postman.jpg)

## Run tests
For running FastAPI test:
```sh
pytest
```
![FastAPI Test](./image/test.jpg)

## DataBase
We use Postgres as our database for this project:

![Database](./image/adminer.jpg)

The schema for the Database is defined at _init.sql_
## Author

👤 **Ahmed Belarbi**

* Twitter: [@abhd96](https://twitter.com/abhd96)
* Github: [@ahbe](https://github.com/ahbe)
* LinkedIn: [@ahmedbelarbi96](https://linkedin.com/in/ahmedbelarbi96)

## Show your support

Give a ⭐️ if you liked this project!

***