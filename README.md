#flappi

##Overview
A boilerplate application for building a REST API in Flask, using Blueprints.

##Installing
* Create a new virtual environment:
```
virtualenv env
```
* Activate the environment:
```
source env/bin/activate
```
* Install project dependencies:
```
pip install -r requirements.txt
```

##Running the application
* Create the required databases and tables:
```
python manage.py create_db
```

* Start the server:
```
python manage.py run_dev_server
```

##Testing
* To run the tests, do:
```
nosetests tests/
```

* To run the tests with coverage, do:
```
nosetests tests/ --with-coverage --cover-package=api --cover-erase
```

##Contributing
* Fork it
* Create your feature branch ```git checkout -b my-new-feature```
* Commit your changes ```git commit -am 'Add some feature'```
* Push to the branch ```git push origin my-new-feature```
* Create new Pull Request
