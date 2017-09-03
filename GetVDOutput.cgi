#!/usr/bin/perl -w
use CGI;
use HTML::Template;
use File::Find;
use Cwd;

my $q = CGI->new();
my $sid = $q->param('id');

my $baseDir = 'virusdetect/'.$sid;
my $blastn = $baseDir.'/blastn.html';
my $blastx = $baseDir.'/blastx.html';
my $contig = $baseDir.'/contig_sequences.fa';
my $image = 'LenDistr/'.$sid.'.png';

my $template = HTML::Template->new(filename => 'template.tmpl');
$template->param(SNAME => $sid);
$template->param(IMG => $image);
$template->param(CONTIG => $contig);


if(-e $blastn){
	my $bn;
	open BLASTN, $blastn;
	while(<BLASTN>){
		if(/^\<table/){
			chomp;
			my ($style) = $_=~/(style.*)align/;
			$_=~s/$style//;
			$bn.=$_;
			while(<BLASTN>){
				chomp;
				if(my ($match)=$_=~/href=\"blastn_references\/(.*?)\.html\"/){
					my $before = 'href="blastn_references/'.$match.'.html"';
					my $change = 'href="GetRefVirus.cgi?sid='.$sid.'&vid='.$match.'&type=blastn" target=_blank';
					$_=~s/$before/$change/;
				}
				$bn.=$_;
				if(/^\<\/table\>/){
					last;
				}
			}	
		}
		else{next}
	}
	close BLASTN;
	$template->param(BLASTN => $bn);
}

if(-e $blastx){
        my $bx;
        open BLASTX, $blastx;
        while(<BLASTX>){
                if(/^\<table/){
                        chomp;
                        my ($style) = $_=~/(style.*)align/;
                        $_=~s/$style//;
                        $bx.=$_;
                        while(<BLASTX>){
                                chomp;
				if(my ($match)=$_=~/href=\"blastx_references\/(.*?)\.html\"/){
                                        my $before = 'href="blastx_references/'.$match.'.html"';
                                        my $change = 'href="GetRefVirus.cgi?sid='.$sid.'&vid='.$match.'&type=blastx" target=_blank';
                                        $_=~s/$before/$change/;
                                }
                                $bx.=$_;
                                if(/^\<\/table\>/){
                                        last;
                                }
                        }
                }
                else{next}
        }
        close BLASTX;
        $template->param(BLASTX => $bx);
}



print "Content-type: text/html\n\n";
print $template->output;



#// SNAME CONTIG IMG BLASTN BLASTX
