name: acme-jenkins-config
version: 1.0
release: 0
summary: acme-jenkins platform configuration package
group: acme/releaseMgmt
license: acme inc.

requires: acme-jenkins

%description
jenkins jobs configurtion platform package

%files
%attr(664, jenkins, jenkins) %config /var/lib/jenkins/config.xml
%dir %attr(755, jenkins, jenkins) /var/lib/jenkins/users
%dir %attr(755, jenkins, jenkins) /var/lib/jenkins/users/acme
%attr(664, jenkins, jenkins) %config /var/lib/jenkins/users/acme/config.xml

%post

%changelog
* Sun Mar 27 2011 Chuck Scott <chuck@acme.com> 1.0-0
    - initial version
