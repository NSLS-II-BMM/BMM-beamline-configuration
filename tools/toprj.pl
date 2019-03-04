#!/usr/bin/env perl

use Demeter qw(:data);

use File::Spec;
use Getopt::Long;
use vars qw($folder $name $base $start $end $bounds $mode);
my $result = GetOptions (
			 "folder=s" => \$folder,
			 "name=s"   => \$name,
			 "base=s"   => \$base,
			 "start=i"  => \$start,
			 "end=i"    => \$end,
			 "bounds=s" => \$bounds,
			 "mode=s"   => \$mode,
			);

my $xanes = 1;
my $last = (split(" ", $bounds))[-1];


if ($last =~ m{k\z}) {
  chop($last);
  $xanes = 0 if $last >= 9;
} elsif ($last > 308) {
  $xanes = 0;
}

my @common = (energy=>qw($1),
	      numerator=>qw($8+$9+$10+$11),
	      denominator=>qw($5),
	      ln=>0);

if ($mode eq 'reference') {
  @common = (energy=>qw($1),
	     numerator=>qw($6),
	     denominator=>qw($7),
	     ln=>1);
} elsif ($mode eq 'transmission') {
  @common = (energy=>qw($1),
	     numerator=>qw($5),
	     denominator=>qw($6),
	     ln=>1);
} elsif ($mode eq 'test') {
  @common = (energy=>qw($1),
	     numerator=>qw($5),
	     denominator=>1,
	     ln=>0);
  $xanes = 1;
};

my @list;
foreach my $ext (int($start) .. int($end)) {

  my $f = sprintf('%s.%3.3d', $name, $ext);
  next if not -e $f;
  my $data = Demeter::Data->new(file=>File::Spec->catfile($folder, $f),
				@common
			       );
  $data->_update('all');
  push @list, $data;
};

my $project = sprintf('%s.prj', $base);
Demeter->co->set_default("gnuplot","terminal", 'pngcairo');
Demeter->po->terminal_number('');
Demeter->co->set_default("gnuplot","termparams", 'enhanced');

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
