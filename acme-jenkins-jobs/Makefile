.PHONY: acme-jenkins-jobs

acme-jenkins-jobs: clean
	mkdir -p dist/RPMS/noarch
	rm -rf build-target
	cp -r buildroot build-target
	rpmbuild -bb --target=noarch --define "_topdir ${PWD}/dist" --buildroot="${PWD}/build-target" acme-jenkins-jobs.spec

clean:
	rm -rf build-target
	rm -rf dist
