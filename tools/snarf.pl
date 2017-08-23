#!/usr/bin/perl

use strict;
use warnings;
use Statistics::Descriptive;

# monitor_para.dat
# monitor_para_0.7A.dat
# monitor_para_0.7_theta=29.62.dat
# monitor_para_1A.dat
open my $M, '<', 'monitor_para_0.7_theta=29.62.dat';
my $prev = 0;
my @spans = ();
while (<$M>) {
  next if m{\A\#};
  my @list = split(" ", $_);
  if ($prev == 0) {
    $prev = $list[0]/1000000000;
    next;
  };
  push @spans, $list[0]/1000000000 - $prev;
  $prev = $list[0]/1000000000;
};
close $M;

#print join("|", @spans), $/;

my $stat = Statistics::Descriptive::Full->new();
$stat->add_data(@spans);
printf "average = %.3f +/- %.3f, shortest = %.3f, longest = %.3f, samples = %d\n",
  $stat->mean(), $stat->standard_deviation(), $stat->min, $stat->max, $#spans;
