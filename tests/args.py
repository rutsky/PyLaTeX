#!/usr/bin/python

"""
    Calls functions with all available arguments to check whether they still 
    exist. An error from this file means that the public API has been changed.
"""

import numpy as np

from pylatex import (Document, Section, Math, Table, Figure, Package, TikZ, 
                    Axis, Plot)
from pylatex.command import Command
from pylatex.numpy import Matrix, VectorName
from pylatex.utils import (escape_latex, fix_filename, dumps_list, bold, 
                           italic, verbatim)



# Document
doc = Document(
    default_filename='default_filename', 
    documentclass='article', 
    fontenc='T1', 
    inputenc='utf8', 
    author='', 
    title='', 
    date='', 
    data=None, 
    maketitle=False
)

doc.append('Some text.')

doc.generate_tex(filename='')
doc.generate_pdf(filename='', clean=True)

# SectionBase
s = Section(title='', numbering=True, data=None)

# Math
m = Math(data=None, inline=False)

# Table
t = Table(table_spec='|c|c|', data=None, pos=None, table_type='tabular')

t.add_hline(start=None, end=None)

t.add_row(cells=(1, 2), escape=False)

t.add_multicolumn(size=2, align='|c|', content='Multicol', cells=None, 
                  escape=False)
                  
t.add_multirow(size=3, align='*', content='Multirow', hlines=True, cells=None,
               escape=False)

# Command
c = Command('documentclass', arguments=None, options=None, packages=None)

# Figure
f = Figure(data=None, position=None)

f.add_image(filename='', width=r'0.8\textwidth', placement=r'\centering')

f.add_caption('')

# Numpy
v = VectorName(name='')

M = np.matrix([[2, 3, 4],
               [0, 0, 1],
               [0, 0, 2]])
m = Matrix(matrix=M, name='', mtype='p', alignment=None)

# Package
p = Package(name='', base='usepackage', options=None)

# PGFPlots
tikz = TikZ(data=None) 

a = Axis(data=None, options=None) 

p = Plot(name=None, func=None, coordinates=None, options=None)

# Utils
escape_latex(s='')

fix_filename(filename='')

dumps_list(l=[], escape=False, token='\n')

bold(s='')

italic(s='')

verbatim(s='', delimiter='|')

