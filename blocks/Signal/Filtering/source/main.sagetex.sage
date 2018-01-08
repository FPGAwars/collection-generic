## -*- encoding: utf-8 -*-
## This file (main.sagetex.sage) was *autogenerated* from main.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('main', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = 199
_st_.blockbegin()
try:
 x=var('x');
 t = var('t');
 x_coords = [t for t in srange(0,2,0.01)];
 
 x = var('x');
 p = var('p');
 w0 = 2*pi; Q = 2; v(x) = inverse_laplace(1/p/(1+p/Q/w0+p^2/w0^2), p, x);
 
 y5_coords = [v(x).n() for x in x_coords];
 
 output = "";
 for i in range(0,len(x_coords)-1):
     output += "\draw[orange, thick] ("+str(x_coords[i])+","+str(y5_coords[i])+")--("+str(x_coords[i+1])+","+str(y5_coords[i+1])+");\n";
except:
 _st_.goboom(213)
_st_.blockend()
try:
 _st_.current_tex_line = 234
 _st_.inline(0, output)
except:
 _st_.goboom(234)
_st_.current_tex_line = 249
_st_.blockbegin()
try:
 z = var('z');
 p = var('p');
 T = var('T');
 
 w = 2*pi.n()*0.01;
 Q = 2;
 
 b0 = 1/(1+1/Q/w+1/w^2);
 a1 = -b0/w*(1/Q+2/w);
 a2 = b0/w^2;
except:
 _st_.goboom(260)
_st_.blockend()
try:
 _st_.current_tex_line = 264
 _st_.inline(1, str(b0))
except:
 _st_.goboom(264)
try:
 _st_.current_tex_line = 265
 _st_.inline(2, str(a1))
except:
 _st_.goboom(265)
try:
 _st_.current_tex_line = 266
 _st_.inline(3, str(a2))
except:
 _st_.goboom(266)
_st_.endofdoc()
