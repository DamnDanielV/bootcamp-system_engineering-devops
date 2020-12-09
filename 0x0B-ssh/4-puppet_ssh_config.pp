# puppet to connect to a server without password
file_line {'no_password':
path => 'etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

file_line {'identity_file':
path => 'etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton'
}
