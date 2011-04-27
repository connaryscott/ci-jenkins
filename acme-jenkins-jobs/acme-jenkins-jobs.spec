name: acme-jenkins-jobs
version: 1.0
release: 1
summary: acme-jenkins platform package
group: acme/releaseMgmt
license: acme inc.

requires: acme-jenkins-config

%description
jenkins jobs package

%files
%dir %attr(750, jenkins, jenkins) /etc/jenkins.jobs.d
%attr(640, jenkins, jenkins) /etc/jenkins.jobs.d/helloworld.config.xml
%attr(640, jenkins, jenkins) /etc/jenkins.jobs.d/helloworld2.config.xml
%attr(640, jenkins, jenkins) /etc/jenkins.jobs.d/ci-jenkins.config.xml

%post

/etc/rc.d/init.d/jenkins start
sleep 10
tries=0
while [ 1 ]
do
   echo waiting for jenkins webapi 
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
echo loading helloworld
/usr/bin/jenkins-jobs load --overwrite --file /etc/jenkins.jobs.d/helloworld.config.xml --name helloworld --username acme --password acmepass
echo loading helloworld2
/usr/bin/jenkins-jobs load --overwrite --file /etc/jenkins.jobs.d/helloworld2.config.xml --name helloworld2 --username acme --password acmepass
echo loading ci-jenkins
/usr/bin/jenkins-jobs load --overwrite --file /etc/jenkins.jobs.d/ci-jenkins.config.xml --name ci-jenkins --username acme --password acmepass

%changelog
* Sun Mar 27 2011 Chuck Scott <chuck@acme.com> 1.0-0
    - initial version
* Sun Mar 27 2011 Chuck Scott <chuck@acme.com> 1.0-1
    - added ci-jenkins job to test git plugin
