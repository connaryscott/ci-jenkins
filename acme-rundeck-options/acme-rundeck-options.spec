name: acme-rundeck-options
version: 1.0
release: 0
summary: options provider for the rundeck server
group: acme/releaseMgmt
license: acme inc.

requires: python26-mod_python

%description
options provider for the rundeck server.  
Includes json over python26 as well as .options cgi executable support


%files
%attr(644, root, root) /etc/httpd/conf.d/acme-rundeck-options.conf
%dir %attr(755, rundeck, rundeck) /var/rundeck/options
%attr(755, rundeck, rundeck) /var/rundeck/options/jenkins.py
