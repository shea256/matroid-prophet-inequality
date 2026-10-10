# Limitation of the conservative certificate family

This is a limitation of the explicit scalar bound used in
[parameter_refinement.md](parameter_refinement.md), not an upper bound on
the algorithm's actual reward or on matroid prophet inequalities.

Allow every integer `a>=2`, `b>=1`, `m>=4`, and `r>=1`; put
`kappa=2^a`, `B=2^b`, and allow any positive thinning rate `t` for which the
certificate applies. Define

\[
 \gamma_m=\frac{2^{-m}}8
   \left[1-2^{1-m}\left(\frac7{10}(m+2)+1\right)\right],
\]

and the residual error from our conservative tail argument,

\[
 \epsilon=\frac1{8\kappa}+\frac{6a+13+r}{\kappa}+2^{-r}.
\]

For `m=4`, `gamma_m=7/2560<2^-8`. For `m=5`, it is
`101/40960<7/2560`. For `m>=6`, it is at most `2^-m/8<=1/512<7/2560`.
Thus `gamma_m<=7/2560` throughout this family.

The positive-slack requirement implies `epsilon<gamma_m/2`. However,
`(6a+13)/2^a` decreases for `a>=2`, and at `a=16` it equals
`109/65536>7/5120`. Consequently any positive certificate in this family
requires `a>=17`, so `kappa>=2^17`.

Writing `z=t kappa`, discarding all other nonnegative errors and taking the
branch probability and `beta` at most one gives the following upper bound
on the *coefficient produced by the certificate*:

\[
 C\le\frac{t}{b\kappa}(\gamma_m/2-t\kappa)
 =\frac{z(\gamma_m/2-z)}{b\kappa^2}
 \le\frac{\gamma_m^2}{16b\kappa^2}<2^{-54}.
\]

This follows by completing the square and is not a finite-grid conclusion.
In particular, extending our parameter grid while keeping this certificate
cannot exceed the announced `2^-47`. Further progress needs a sharper exit
or residual argument, a different construction, or access to the announced
stronger proof. This limitation does not cover those possibilities, and its
novelty has not been established.
