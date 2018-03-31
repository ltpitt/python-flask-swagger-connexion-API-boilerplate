# A Python script that uses Flask and Swagger with Connexion.
> A simple boilerplate to build an API using python / flask / swagger / connexion

## Prerequisites

- Download and install requirements:  
`pip install -f requirements.txt`

## How to use

- Clone this repo locally
- Customize path according to the folder where you cloned the script:  
`*/5 * * * * /yourpath/network_check.sh`
- Put the resulting row into your root crontab:  
`sudo crontab -e` 
- If you also want to reboot in case wifi is not working after the fix uncomment the required lines in the code (detailed explanation is in the script comments)
- If you want to perform automatic repair fsck in case of reboot (this is the last possible recovery action) remember to uncomment fsck autorepair here:  
`/etc/default/rcS`

## Release History

* 0.0.1
    * First commit

## Meta

Davide Nastri – [@pitto](https://twitter.com/pitto) – d.nastri@gmail.com

Distributed under the GPL license. See ``LICENSE`` for more information.

[https://github.com/ltpitt/vagrant-cloudpebble-composed](https://github.com/ltpitt/)

## Contributing

1. Fork it (<https://github.com/ltpitt/python-flask-swagger-connexion-API-boilerplate/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
