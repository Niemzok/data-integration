# data-integration

## Project Description

This project was part of a company hackathon with [InterWorks](www.interworks.com).

In the current status the project pulls answer and respondent data from [Netigate](
https://www.netigate.net/de/) surveys and pushes those into any database that is supported by [SQL Alchemy](http://sqlalche.me/).


Export csv or API possible

https://www.netigate.net/de/


## Check prerequisites:

Install python 3. [Here is a good guide for the installation](https://realpython.com/installing-python/)


Install Pip. [Here is another good guide for installing pip](https://www.makeuseof.com/tag/install-pip-for-python/)

## Installation

I recommend working with a virtualenvironment in order to keep all the dependencies clean. In case you need a quick refreshing reminder have a look at the guid [here](https://docs.python-guide.org/dev/virtualenvs/).

In order to install all the packages activate your virtualenvironment and run:

```
pip install -r requirements.txt
```

For authenticating with the [Netigate API](https://www.netigate.net/api/) you need to receive a X-API-Key. Once you have the key you will need to store it in in config.py.

## Run the module

In order to run the main script use:

```
python main.py
```

## Modules
- Data Input:
   - read a csv file
   - input is file path
  - output is pythonic way to pass on data (json)


- Data transformation:
  - transform data into relational SQL structure (In scenario to push for SQL Server, dependend on output)
  - input is data json
  - output is SQL table

- data output
  - parses data into database
  - connects to database
  - inout is SQL table
  - output is a log that the data is parsed