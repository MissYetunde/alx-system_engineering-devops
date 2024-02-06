# Puppet manifest to configure the nginx server
include stdlib

package { 'nginx':
  ensure => 'installed'
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  content => "Hello World!\n",
  require => Package['nginx']
}

$str = "        server_name _;
        rewrite ^/redirect_me$ http:x.com permanent;
        rewrite ^/redirect_me/$ http:x.com permanent;
"

file_line { 'redirection_server':
  path  => '/etc/nginx/sites-enabled/default',
  line  => $str,
  match => '^\s*server_name _;.*$',
  after => '^\s*server_name _;.*$'
}

exec { 'restart nginx':
  path    => '/usr/bin',
  command => 'sudo service nginx restart',
  require => [Package['nginx'], File_line['redirection_server']]
}
