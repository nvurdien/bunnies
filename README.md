# bunnynet

Bunnynet is a democratic rabbit breed classification platform.


## Platform

Flask

SQLite

Python3.6


## TODO

* Hand-crafted autocomplete (probably using Levenshtein distance)
* Allow user upload (recaptcha?)
* Deep learning integration for predictions
* Prediction API

## Design choices:

* Image -> vote many-to-one, better than one-to-one, no extremely large and  sparse objects. 
* MD5 isn't secure, but we don't think that it matters for this usecase. MD5 is pretty fast, so we go with the fastest algorithm.


### But seriously

This is a PET project, GET IT?
