#!/usr/bin/perl -w
use CGI;
use HTML::Template;
use File::Find;
use Cwd;

my $q = CGI->new();
my $sid = $q->param('sid');
my $vid = $q->param('vid');
my $type = $q->param('type');

my $file = 'virusdetect/'.$sid.'/'.$type.'_references/'.$vid.'.html';

my $template = HTML::Template->new(filename => 'template_vir.tmpl');

$template->param(VNAME => $vid);
$template->param(SNAME => $sid);

my $content;
open IN,$file ;
while(<IN>){
	next if $. <= 6;
	if(my ($m)=$_=~/\<img\s+src=\"(.*?)\//){
		my $newDir = 'virusdetect/'.$sid.'/'.$type.'_references/'.$vid;
		$_=~s/$m/$newDir/;
	}
	$content .= $_;
}

$template->param(CONTENT => $content);


print "Content-type: text/html\n\n";
print $template->output;

