name: acme-jenkins
version: 1.0
release: 0
summary: acme-jenkins platform package
group: acme/releaseMgmt
license: acme inc.

requires: jenkins

%description
jenkins base platform with value added utilities

%files
%attr(755, root, root) /usr/bin/jenkins-jobs
%dir %attr(755, jenkins, jenkins) /var/lib/jenkins/plugins
%attr(644, jenkins, jenkins) /var/lib/jenkins/plugins/git.hpi
