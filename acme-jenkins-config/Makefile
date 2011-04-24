.PHONY: acme-jenkins-config

acme-jenkins-config: clean
	mkdir -p dist/RPMS/noarch
	rm -rf build-target
	svn export buildroot build-target
	rpmbuild -bb --target=noarch --define "_topdir ${PWD}/dist" --buildroot="${PWD}/build-target" acme-jenkins-config.spec

clean:
	rm -rf build-target
	rm -rf dist
