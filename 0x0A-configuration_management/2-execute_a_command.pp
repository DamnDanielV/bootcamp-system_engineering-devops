# execute a command with a puppet manifest
exec { 'kill process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
