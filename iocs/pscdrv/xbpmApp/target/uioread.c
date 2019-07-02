#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>

int main(int argc, char *argv[])
{
    unsigned long range = 0, start = 0, offset, size = 4, i;
    long pagesize = sysconf(_SC_PAGESIZE);
    int fd;
    char *addr;

    if(argc<2){
        fprintf(stderr, "Usage: %s <dev> [range] [offset] [len]\n", argv[0]);
        return 1;
    }

    if(argc>2)
        range = strtoul(argv[2], NULL, 0);
    if(argc>3)
        start = strtoul(argv[3], NULL, 0);
    if(argc>4)
        size = strtoul(argv[4], NULL, 0);

    offset = start&(pagesize-1);

    fprintf(stderr, "Read %lu %lu %lu\n", range, start, size);

    fd = open(argv[1], O_RDWR);
    if(fd==-1) {
        perror("open");
        return 1;
    }

    addr = mmap(NULL, start+size, PROT_READ, MAP_SHARED, fd, range*pagesize);
    if(addr==MAP_FAILED) {
        perror("mmap");
        close(fd);
        return 1;
    }

    addr += offset;

    for(i=start; size; addr++, i++, size--) {
        if(start%16==0)
           printf("\n0x%16lx ", start);
        if(start%4==0)
           putchar(' ');
        printf("%02x", *addr);
    }
    printf("\n");

    if(munmap(addr-offset, start+size)) perror("munmap");

    close(fd);

    return 0;
}
