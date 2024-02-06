# 0. Create a file
# Using Puppet, create a file in /tmp.

exec { 'create_school_file':
    command => '/bin/touch /tmp/school',
}

file { '/tmp/school':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    require => Exec['create_school_file'],
}

exec { 'write_school_file':
    command => '/bin/echo "I love Puppet" > /tmp/school',
    require => [Exec['create_school_file'], File['/tmp/school']],
}
