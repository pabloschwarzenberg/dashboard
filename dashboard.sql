# create user "icf"@"%" identified by "Secret.123";
# grant all privileges on *.* to "icf"@"%" identified by "Secret.123";
create database dashboard character set utf8 collate utf8_bin;
grant all on dashboard.* to "icf"@"%" identified by "Secret.123";
