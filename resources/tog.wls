#!/usr/bin/env wolframscript
(* ::Package:: *)

DSolve[{c'[t]==L/(1+E^(-k(t-t0))) (\[Alpha]-\[Gamma]*c[t]^2)},c[t],t]


Plot[1+(E^(0.8*t))^(-10*0.8/0.2),{t,0,0.01}]


Plot[{1/(1+E^-t),Tanh[t]},{t,0,10}]
