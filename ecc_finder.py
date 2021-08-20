#!/usr/bin/env python3

"""
# June 2021
# If using this pipeline please cite : XXXXXXXXXX
#--------------------------------------------------------------------------+    
#                                                   
#	ecc_finder is a tool 
#       to detect eccDNA using Illumina and ONT sequencing.  
#                                                        
#--------------------------------------------------------------------------+
#                                                      
#	AUTHOR: panpan ZHANG                            
#	CONTACT: njaupanpan@gmail.com                      
#                                                         
#	LICENSE:                                            
# 	GNU General Public License, Version 3               
#	http://www.gnu.org/licenses/gpl.html  
#                                             
#	VERSION: 1.0.0                  
#                                                                                                       
#--------------------------------------------------------------------------+
"""

import sys
import subprocess
from eccFinder_utilities.utilities import get_eccFinder_version



def main():
    VERSION = get_eccFinder_version()
    CITATION = """
Zhang et al. "Ecc_finder: a robust and accurate tool for detecting extrachromosomal circular DNA (eccDNA) from sequencing data"
    """

    description = """
ecc_Finder: Tool for detecting eccDNA loci using Illumina and ONT sequencing.
Version: %s

usage: ecc_finder.py <command> [options]
    
    Mapping mode:
      map-sr         Call candidate eccDNA loci from paired-end short reads
      map-ont        Call candidate eccDNA loci from Nanopore long reads
    
    Assembly mode:
      asm-sr         Assembly from paired-end short reads
      asm-ont        Assembly from Nanopore long reads
      
    options:
      -c, --citation  
      -v, --version""" % VERSION

    arg_len = len(sys.argv)
    if arg_len == 1:
        print(description)

    if arg_len > 1:
        cmd = sys.argv[1]

        if cmd == "-h" or cmd == "--help":
            print(description)

        elif cmd == "-v" or cmd == "--version":
            print(VERSION)

        elif cmd == "-c" or cmd == "--citation":
            print(CITATION)

        elif cmd == "map_ILL":
            subcmd = ["eccFinder_map_ILL.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "mapp_ONT":
            subcmd = ["eccFinder_map_ONT.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "asm_ILL":
            subcmd = ["eccFinder_asm_ILL.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        elif cmd == "patch":
            subcmd = ["eccFinder_asm_ONT.py"] + sys.argv[2:]
            subprocess.call(subcmd)

        else:
            print(description)
            print("\n** unrecognized command: %s **" % cmd)

if __name__ == "__main__":
    main()