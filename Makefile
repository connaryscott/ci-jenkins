#top level build

.PHONY: all

all:
	$(MAKE) -C acme-jenkins PWD=${PWD}/acme-jenkins
	$(MAKE) -C acme-jenkins-config PWD=${PWD}/acme-jenkins-config
	$(MAKE) -C acme-jenkins-jobs PWD=${PWD}/acme-jenkins-jobs
	$(MAKE) -C acme-rundeck-config PWD=${PWD}/acme-rundeck-config
	$(MAKE) -C acme-rundeck-jobs PWD=${PWD}/acme-rundeck-jobs
	$(MAKE) -C acme-rundeck-options PWD=${PWD}/acme-rundeck-options
