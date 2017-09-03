#!/usr/bin/perl
use CGI;

my $q = CGI->new();

my $value = $q->param('id');


print "Content-type: text/html\n\n";

print "value is $value\n";
