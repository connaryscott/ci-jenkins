name: acme-rundeck-jobs
version: 1.0
release: 0
summary: rundeck jobs package
group: acme/releaseMgmt
license: acme inc.

requires: acme-rundeck-config
requires: acme-rundeck-options

%description
rundeck jobs package
processes jobxml and dependent options service files


%files
%attr(755, rundeck, rundeck) /var/rundeck/options/jenkins.py

%dir %attr(755, rundeck, rundeck) /var/rundeck/projects/acme
%dir %attr(755, rundeck, rundeck) /var/rundeck/projects/acme/jobs.d
%attr(644, rundeck, rundeck) /var/rundeck/projects/acme/jobs.d/acme-release.xml

%post

/etc/rc.d/init.d/rundeckd start


tries=0
while [ 1 ]
do
   echo waiting for rundeck to start
   if [ ! -d /var/rundeck/projects/acme/etc ]
   then
      rd-project -p acme --action create > /dev/null 2>&1
   fi
   if [ -d /var/rundeck/projects/acme/etc ]
   then
      rd-jobs list >/dev/null 2>&1
      if [ $? -eq 0 ]
      then
         break
      fi
   fi
   let tries=tries+1
   if [ $tries -eq 30 ]
   then
      echo "rundeck startup failed" 1>&2
      exit 1
   fi
   sleep 10
done

rd-jobs load -f  /var/rundeck/projects/acme/jobs.d/acme-release.xml
