# using Puppet to make changes to our configuration file.
include stdlib

file_line {'Turn off passwd auth':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => '  PasswordAuthentication no',
  replace  => true,
}

file_line {'Declare Identity File':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '  IdentityFile ~/.ssh/school',
  replace => true,
}
