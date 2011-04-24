name: acme-jenkins-jobs
version: 1.0
release: 0
summary: acme-jenkins platform package
group: acme/releaseMgmt
license: acme inc.

requires: acme-jenkins-config

%description
jenkins jobs package

%files
%dir %attr(750, jenkins, jenkins) /etc/jenkins.jobs.d
%attr(640, jenkins, jenkins) /etc/jenkins.jobs.d/helloworld.config.xml

%post

/etc/rc.d/init.d/jenkins restart
sleep 10
tries=0
while [ 1 ]
do
   echo waiting for jenkins to start
   sleep 5
   /usr/bin/jenkins-jobs list >/dev/null 2>&1
   if [ $? -eq 0 ]
   then
      break
   fi
   let tries=tries+1
   if [ $tries -eq 30 ]
   then
      echo "jenkins startup failed" 1>&2
      exit 1
   fi
done
/usr/bin/jenkins-jobs load --overwrite --file /etc/jenkins.jobs.d/helloworld.config.xml --name helloworld --username acme --password acmepass

%changelog
* Sun Mar 27 2011 Chuck Scott <chuck@acme.com> 1.0-0
    - initial version
