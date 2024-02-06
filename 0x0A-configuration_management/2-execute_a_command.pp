# 2. Execute a command
# Using Puppet, create a manifest that kills a process named killmenow.
# Requirements: 
# - Must use the exec Puppet resource
# - Must use pkill

exec { 'killmenow':
    command  => '/bin/pkill killmenow',
}
