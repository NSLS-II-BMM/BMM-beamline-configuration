set term qt persist
set xlabel 'time (min)'
set ylabel 'temperature (C)'
set y2label 'following error (mm)'
set y2tics
#set y2tics -0.001,0.0001,0.001
#set y2range [-0.001:0.001]
set ytics nomirror
#unset xrange
set grid
set key bottom left box opaque height 2 width 0 noreverse
plot 'monitor_para.dat' u ($1/1000000000/60):($2-$3) w l lt 2 axes x1y2 title 'position - target',\
     'monitor_para.dat' u ($1/1000000000/60):4       w l lt 1 axes x1y1 title 'temperature'