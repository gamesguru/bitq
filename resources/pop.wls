#!/usr/bin/env wolframscript
(* ::Package:: *)

DSolve[{y'[x]==E^(-x^1/16),y[0]==0},y[x],x]
Integrate[E^-Sqrt[x], x]
Plot[16 E^(-x/16) (-1+E^(x/16)), {x,0,150}]


DSolve[{y'[x]==x^-Log[x],y[0]==0},y[x],x]
Plot[1/2 (E^(1/4) Sqrt[\[Pi]]+E^(1/4) Sqrt[\[Pi]] Erf[1/2 (-1+2 Log[x])]), {x,0,150}]


sol=DSolve[{p'[t]==p[t](1-p[t]), p[0]==0.2},p[t],t]
y[t_] :=p[t]/.sol
y[2]
Plot[y[t],{t,0,10}]



