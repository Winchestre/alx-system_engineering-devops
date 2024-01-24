#!/usr/bin/env bash
# Using puppet to automate changes to client config file

file { '/etc/ssh/ssh_config':
	ensure => present,
	content =>"
		#SSH Client Configuration
		Host *
		IdentityFile ~/.ssh/school
		PasswordAuthentication no"
}
