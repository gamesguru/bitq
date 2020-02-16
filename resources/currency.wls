#!/usr/bin/env wolframscript
(* ::Package:: *)

(* Constraint: "carrying capacity" *)
L = 10000000;

(* initial conditions *)
t0 = 0; (* months *)
n0 = 1; (* people *)
t1 = 36;
n1 = 100000;
(* Other constraints: solved *)
b = L / n0 - 1;
k = -1 / t1 * Log[(L / n1 - 1) / b];

(* Population eq *)
n[t_] := L / (1 + b * E^(-k*t));
Manipulate[Plot[n[t], {t, 0, m}, AxesLabel->{"t (months)", "n(t) [# of users]"}], {m, 1, 80, 1}]

(* Currency diff-eq *)
\[Alpha] = 1/20;
\[Gamma] = 1/100;

(*sol = NDSolve[{c'[t] == n[t]*(\[Gamma] - \[Alpha]*c[t]), c[0]\[Equal]1}, c[t], {t, 0, 100}]
Plot[c[t]/.sol, {t, 0, 100}]*)

sol = NDSolve[{c'[t] + \[Alpha]*c[t] == \[Gamma] * n[t], c[0]==1}, c[t], {t, 0, 10000}];
Plot[c[t]/.sol, {t, 0, 1000}]



