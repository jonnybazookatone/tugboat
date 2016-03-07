[![Build Status](https://travis-ci.org/adsabs/tugboat.svg?branch=master)](https://travis-ci.org/adsabs/tugboat)
[![Coverage Status](https://coveralls.io/repos/github/adsabs/tugboat/badge.svg?branch=master)](https://coveralls.io/github/adsabs/tugboat?branch=master)
# Tugboat

Tugboat proxy, integration tools to use alongside harbour-service

## development

```bash
pip install virtualenvwrapper
mkvirtualenv tug
workon tug
pip install -r requirements.txt
nosetests tugboat/tests/
```

A Vagrantfile and puppet manifest are available for development within a virtual machine. To use the vagrant VM defined here you will need to install *Vagrant* and *VirtualBox*. 

  * [Vagrant](https://docs.vagrantup.com)
  * [VirtualBox](https://www.virtualbox.org)

To load and enter the VM: `vagrant up && vagrant ssh`
