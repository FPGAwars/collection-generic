## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file main.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_249 = Integer(249); _sage_const_260 = Integer(260); _sage_const_199 = Integer(199); _sage_const_265 = Integer(265); _sage_const_264 = Integer(264); _sage_const_266 = Integer(266); _sage_const_213 = Integer(213); _sage_const_0p01 = RealNumber('0.01'); _sage_const_234 = Integer(234)## This file (main.sagetex.sage) was *autogenerated* from main.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('main', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_199 
_st_.blockbegin()
try:
 x=var('x');
 t = var('t');
 x_coords = [t for t in srange(_sage_const_0 ,_sage_const_2 ,_sage_const_0p01 )];
 
 x = var('x');
 p = var('p');
 w0 = _sage_const_2 *pi; Q = _sage_const_2 ; __tmp__=var("x"); v = symbolic_expression(inverse_laplace(_sage_const_1 /p/(_sage_const_1 +p/Q/w0+p**_sage_const_2 /w0**_sage_const_2 ), p, x)).function(x);
 
 y5_coords = [v(x).n() for x in x_coords];
 
 output = "";
 for i in range(_sage_const_0 ,len(x_coords)-_sage_const_1 ):
     output += "\draw[orange, thick] ("+str(x_coords[i])+","+str(y5_coords[i])+")--("+str(x_coords[i+_sage_const_1 ])+","+str(y5_coords[i+_sage_const_1 ])+");\n";
except:
 _st_.goboom(_sage_const_213 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_234 
 _st_.inline(_sage_const_0 , output)
except:
 _st_.goboom(_sage_const_234 )
_st_.current_tex_line = _sage_const_249 
_st_.blockbegin()
try:
 z = var('z');
 p = var('p');
 T = var('T');
 
 w = _sage_const_2 *pi.n()*_sage_const_0p01 ;
 Q = _sage_const_2 ;
 
 b0 = _sage_const_1 /(_sage_const_1 +_sage_const_1 /Q/w+_sage_const_1 /w**_sage_const_2 );
 a1 = -b0/w*(_sage_const_1 /Q+_sage_const_2 /w);
 a2 = b0/w**_sage_const_2 ;
except:
 _st_.goboom(_sage_const_260 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_264 
 _st_.inline(_sage_const_1 , str(b0))
except:
 _st_.goboom(_sage_const_264 )
try:
 _st_.current_tex_line = _sage_const_265 
 _st_.inline(_sage_const_2 , str(a1))
except:
 _st_.goboom(_sage_const_265 )
try:
 _st_.current_tex_line = _sage_const_266 
 _st_.inline(_sage_const_3 , str(a2))
except:
 _st_.goboom(_sage_const_266 )
_st_.endofdoc()

