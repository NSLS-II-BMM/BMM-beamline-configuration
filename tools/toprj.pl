#!/usr/bin/env perl

use Demeter qw(:data);

use File::Spec;
use Getopt::Long;
use vars qw($folder $name $base $start $end $bounds $mode);
my $result = GetOptions (
			 "folder=s" => \$folder, # data folder
			 "name=s"   => \$name,	 # file stub
			 "base=s"   => \$base,	 # basename (without scan sequence numbering)
			 "start=i"  => \$start,	 # first suffix number
			 "end=i"    => \$end,	 # last suffix number
			 "bounds=s" => \$bounds, # scan boundaries (used to distinguish XANES from EXAFS)
			 "mode=s"   => \$mode,	 # measurement mode
			);

my $xanes = 1;
my $last = (split(" ", $bounds))[-1];
# $folder =~ s/'//g;
# $name   =~ s/'//g;
# $base   =~ s/'//g;
# $bounds =~ s/'//g;

sub ktoe {
  my $KTOE = 3.8099819442818976;
  return $_[0]*$_[0]*$KTOE;
};

###########################################
# XANES-length scan or EXAFS-length scan? #
###########################################
if ($last =~ m{(.*)k\z}) {
  chop($last);
  $last = ktoe($1);
};
if ($last > 308) {
  $xanes = 0;
}


#################################
# file column import parameters #
#################################
my @common = (energy      => qw($1),
	      numerator   => qw($8+$9+$10+$11),
	      denominator => qw($5),
	      ln=>0);

if ($mode eq 'reference') {
  @common = (energy       => qw($1),
	     numerator    => qw($6),
	     denominator  => qw($7),
	     ln           => 1);
} elsif ($mode eq 'transmission') {
  @common = (energy       => qw($1),
	     numerator    => qw($5),
	     denominator  => qw($6),
	     ln           => 1);
} elsif ($mode eq 'test') {
  @common = (energy       => qw($1),
	     numerator    => qw($5),
	     denominator  => 1,
	     ln           => 0);
  $xanes = 1;
};


######################################################
# make a list of Demeter::Data objects for each file #
######################################################
my @list;
foreach my $ext ($start .. $end) {

  my $f = sprintf('%s.%3.3d', $name, $ext);
  my $file = File::Spec->catfile($folder, $f);
  next if not -e $file;
  my $data = Demeter::Data->new(file=>$file,
				@common
			       );
  $data->_update('all');
  push @list, $data;
};

exit if not @list;

#################
# prep for plot #
#################
my $project = sprintf('%s.prj', $base);
Demeter->co->set_default("gnuplot","terminal", 'pngcairo');
Demeter->po->terminal_number('');
Demeter->co->set_default("gnuplot","termparams", 'enhanced');

##########################
# plot XANES or quadplot #
##########################
if ($start == $end) {
  $list[0] -> write_athena(File::Spec->catfile($folder, 'prj', $project), @list);
  if ($xanes) {
    $list[0]->plot('ed');
  } else {
    $list[0]->quadplot;
  };
} else {
  my $merge = $list[0]->merge('e', @list);
  $list[0] -> write_athena(File::Spec->catfile($folder, 'prj', $project), @list, $merge);
  if ($xanes) {
    $merge->plot('ed');
  } else {
    $merge->quadplot;
  };
};


sleep(0.25)
## convert  foo.pdf -background white  -alpha remove foo.png
