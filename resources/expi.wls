#!/usr/bin/env wolframscript
(* ::Package:: *)

Plot[t^-1/(1-E^-(t-0)),{t,0,10}]
NIntegrate[t^-1/(1-E^-(t-0)),{t,1,100}]


Plot[{ExpIntegralEi[t],E^t},{t,89,90}]
