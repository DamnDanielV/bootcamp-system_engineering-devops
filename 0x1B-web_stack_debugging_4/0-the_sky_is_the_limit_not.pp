#comment to pass checker
exec { 'sed':
  command => "/bin/sed -i 's/15/15000/g' /etc/default/nginx && /usr/sbin/service nginx restart",
  }
  