.PHONY: acme-rundeck-config

acme-rundeck-config: clean
	mkdir -p dist/RPMS/noarch
	rm -rf build-target
	cp -r buildroot build-target
	rpmbuild -bb --target=noarch --define "_topdir ${PWD}/dist" --buildroot="${PWD}/build-target" acme-rundeck-config.spec

clean:
	rm -rf build-target
	rm -rf dist
