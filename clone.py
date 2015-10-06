#!/usr/bin/python

import sys
import os
from commands import *

os.umask(022)

def run_command(cmd):
        print 'Running: "%s"' % cmd
        text = getstatusoutput(cmd)
        print text

def create_closed(closed_dir):
        os.mkdir(closed_dir)
        os.chdir(closed_dir)
        run_command('hg clone ssh://on12.us.oracle.com//export/on12-clone/usr/closed .')
        run_command('cd ../../')
        run_command('build nightly bldrc')

def create_dir(name, path):
        os.chdir(path)
        os.mkdir(name)
        os.chdir(name)
        print "CWD: ",os.getcwd()
        run_command('hg clone ssh://on12.us.oracle.com//export/on12-clone .')
        closed_dir = raw_input("Enter closed dir:");
        create_closed(closed_dir);
        return;

name = raw_input("Enter The Directory Nmae:");
path = raw_input("Enter The Path to create Dir:");

run_command('export PATH=/ws/on12-tools/onbld/bin/:/ws/onnv-tools/teamware/bin:/opt/onbld/bin/`uname -p`:/usr/bin:/usr/sbin')
create_dir(name, path);
