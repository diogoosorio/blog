[![Build Status](https://travis-ci.org/diogoosorio/blog.svg?branch=master)](https://travis-ci.org/diogoosorio/blog)

## Welcome to Diogo's personal blog

My poor attempt of writing a small static blog generator (à la Jekyll). This time the main weapons of choice were Python and Flask.

During this first (quick) iteration, the blog entries are being loaded and parsed from the hard-drive when a request comes in. In the near future, the objective is to have this proccess automatized, whenever a blog entry is edited/added (add a watch operation).

I had three main objectives in mind, developing this: 

* To remove the MongoDB dependency that the previous blog version had 
* To add a simpler, content centered, responsive design
* To be able to write the entries using Markdown

The three of them were achieved. There are a lot of nice-to-have's that I'd like to add, but one just has so many off-days per week. :)

## Running the blog

To run the blog, do the following:

```bash
cp env.sample .env # edit the secrets present there
docker-compose up -d
```

The http server should be listening on port 4000.
