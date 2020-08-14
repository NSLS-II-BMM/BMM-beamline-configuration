#!/usr/bin/env python3

import re, requests, os


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

urlbase = 'https://wiki-nsls2.bnl.gov/beamline6BM/index.php/'
urlsuffix = '?action=raw'
pages = list()
media = list()
top = urlbase + 'Main_Page' + urlsuffix


#####################
# grab landing page #
#####################
print(f'fetching {top}')
download_file(top)

######################
# parse landing page #
######################
with open('Main_Page' + urlsuffix) as F:
    for line in F:
        z = re.search('\[\[(.*)\|(.*)\]\]', line)
        if z:
            if re.search('^(Media|File):', z.groups()[0]):
                media.append(z.groups()[0])
            elif re.search('ics$', z.groups()[0]):
                media.append(z.groups()[0])
            else:
                pages.append(z.groups()[0])

####################################
# download and parse every subpage #
####################################
for p in pages:
    this = urlbase + p + urlsuffix
    print(f'fetching {this}')
    download_file(this)
    with open(p + urlsuffix) as F:
        for line in F:
            z = re.search('\[\[(.*)\|(.*)\]\]', line)
            if z:
                if re.search('^(Media|File):', z.groups()[0]):
                    media.append(z.groups()[0])
                elif re.search('ics$', z.groups()[0]):
                    media.append(z.groups()[0])
                else:
                    continue
                    #if z.groups()[0] not in pages:
                    #    pages.append(z.groups()[0])

################################
# download all the media files #
################################
for m in media:
    mm = m
    z = re.search('([^|]*)\|(.*)', m)
    if z:
        mm = z.groups()[0]
    this = urlbase + mm
    print(f'fetching {this}')
    download_file(this)

    ## that was actually an HTML file, use this
    ## simple heuristic to find url for actual media file
    with open(mm) as html:
        for line in html:
            z = re.search('fullMedia"><a href="([^"]*)"', line)
            if z:
                thing = 'https://wiki-nsls2.bnl.gov/' + z.groups()[0]
                print(f'\tfetching {thing}')
                download_file(thing)
    os.remove(mm)

