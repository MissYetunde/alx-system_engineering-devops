# 1. Install a package
# Using Puppet, install flask from pip3.

exec { 'apt_get_update':
  command => '/bin/apt-get update',
}

exec { 'install_python3-pip':
  command => '/bin/apt-get install -y python3-pip',
  require => Exec['apt_get_update'],
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
  require  => Exec['install_python3-pip']
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Exec['install_python3-pip'],
}
