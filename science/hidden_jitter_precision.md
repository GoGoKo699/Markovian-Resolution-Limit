# Global frequency precision with hidden pulse jitter

[Timing model and exact instruments](timing_precision.md) · [Ideal contact law](global_contact_precision.md)

In the collision sensor, a hidden pulse displacement changes how long a block can accumulate a usable phase. Shorter blocks can still be repeated, and their mixed output has a known response. Balancing their length against the number of repetitions gives a sharp global precision law across timing accuracies and contact budgets.

## Model and precision law

Use the [plain and jittered-echo menu](timing_precision.md#timing-model-and-counted-resources) at fixed coupling $`g`$, cell duration $`h`$ and nominal compensation $`\omega_0`$. The controller has no bath access. Each pulsed cell has one sensor $`Z_S`$ pulse at $`h/2+d`$ or $`h/2-d`$, with independent fair signs that are hidden from the controller. The amplitude $`0\le d\lt h/2`$ is known. With $`n`$ cells the hard horizon is $`nh`$, and the controller is allowed at most $`n-1`$ nonterminal contacts, at most $`m`$ of them inside cells, on every history. The unknown transverse angle is shared by all cells. Calibration, resets, rejected records and early readout are included in the experiment.

Let $`R^*_{n,m}(d;\Omega)`$ be the infimum of worst-case squared frequency error over this menu, including arbitrary adaptive boundary instruments and protected memory. For every fixed $`\chi=gh\in(0,\pi/4)`$, there is a fixed band $`\Omega=[\omega_0-E,\omega_0+E]`$ with $`E\gt 0`$ such that

```math
\boxed{
R^*_{n,m}(d;\Omega)
=\Theta_\chi\!\left(
\frac{1}{h^2\left[n+\min\{m^2,m(h/d)^2\}\right]}
\right),\qquad n\ge1,\quad 0\le m\le n-1 .
}
```

At $`d=0`$ the minimum is interpreted as $`m^2`$. The constants are uniform in $`n,m,d`$ for the chosen band. In particular, with $`m=\Theta(n)`$, quadratic global precision holds exactly when $`d=O(h/\sqrt n)`$. If $`d/h=n^{-\alpha}`$ with $`0\lt \alpha\lt 1/2`$, the risk instead has order $`h^{-2}n^{-1-2\alpha}`$. A fixed positive jitter amplitude gives inverse-linear risk even though the original menu can retain quadratic [local information at compensation](timing_precision.md#why-the-local-calculation-gives-a-different-answer).

## The two converse bounds

The ideal contact converse applies directly to the jittered menu. An ideal controller can draw the independent timing signs with its own parameter-independent randomness, use the resulting allowed contact times and disregard the signs. This realizes the jittered protocol, including its accessible records, within the broader ideal contact model. The [ideal adaptive converse](global_contact_precision.md#uniform-converse-for-arbitrary-adaptive-contacts) therefore gives a lower bound of order $`1/[h^2(n+m^2)]`$.

For the second bound, use $`x=h(\omega-\omega_0)`$, $`\xi=d/h`$ and work on a fixed compact subinterval strictly inside $`0\lt x\lt hE`$. Here and below primes differentiate with respect to $`x`$. Put

```math
r=\sqrt{\chi^2+x^2/4},\qquad D=\cos(2r\xi)-\cos r,\qquad
u=\cos r+\frac{\chi^2}{r^2}D,\qquad v=\frac{x}{2r}\sin r,
```

```math
w=\frac{\chi}{r}\sin(2r\xi),\qquad a=\frac{x\chi}{2r^2}D,\qquad
p_e=w^2+a^2,\qquad p_p=\frac{\chi^2}{r^2}\sin^2 r.
```

These are the [exact Kraus coefficients](timing_precision.md#exact-displaced-and-averaged-instruments), with $`a`$ the coefficient of the perpendicular transverse flip before the conditional boundary correction. Set $`u_p=\cos r`$ and take the nuisance curve with slope $`k=(u_pv'-vu_p')/p_p`$. The [jitter-channel gauge](timing_precision.md#one-nuisance-curve-and-an-environment-gauge) removes the derivative overlap of the echo on the same curve as the plain cell. Its only potentially large coefficient is

```math
t_G=\frac{uv'-vu'-p_e k}{2wa}.
```

The bound can be uniform up to the excluded endpoint $`\xi=1/2`$. At that endpoint, $`D=0`$, $`a=0`$, $`u=u_p`$ and $`p_e=p_p`$, so the numerator vanishes identically in $`x`$. Smoothness bounds its absolute value by $`C(1/2-\xi)`$. On the positive compact prior interval, $`w\ge c_1\xi`$. Also

```math
D=2\sin\bigl(r(1/2+\xi)\bigr)\sin\bigl(r(1/2-\xi)\bigr),
```

so $`a\ge c_2(1/2-\xi)`$ there. For these inequalities the band can be chosen with $`r\lt \pi/4`$. Hence $`|t_G|\le C'/\xi`$ for $`0\lt \xi\lt 1/2`$ and the gauged squared derivative norm is at most $`C''/\xi^2`$. The ungauged plain norm is bounded on the same interval. Orthogonality of the successive isometry derivatives, with at most $`m`$ echo cells on every history, gives Fisher information at most $`C(n+m/\xi^2)`$ along the nuisance curve. The same fixed compact prior and van Trees argument as in the [necessary accuracy bound](timing_precision.md#a-necessary-accuracy-scale) therefore give a risk lower bound of order $`1/[h^2(n+m/\xi^2)]`$, including biased estimators. The established bounded-loss argument also applies to the allowed controlled limits. Taking the greater of these two lower bounds gives the claimed denominator. At $`\xi=0`$ the ideal converse suffices.

## The exact mixed response of a block

Use the same logical encoding as the [ideal echo estimator](global_contact_precision.md#attainability-by-recorded-phases), beginning a block in even parity in $`|+_L\rangle`$. Choose the jittered echo from the even sector and the plain cell from the odd sector. Measure parity at each boundary, keep every result, and include the conditional $`Z_S`$ correction of an echo flip in the same boundary instrument as its frame correction and parity readout.

After this correction the two possible echo flips have weights $`a^2`$ for the shared plain flip axis $`N_\phi`$ and $`w^2`$ for the perpendicular axis $`N'_\phi`$. The perpendicular flip is an aligned flip composed with $`Z_S`$ up to a scalar phase. In a record ending even, the aligned flips cancel the unknown axis in pairs. A perpendicular flip multiplies the equatorial coherence by $`-1`$ because of its extra $`Z_S`$. The stay phases are

```math
\theta_e=2\arctan(v/u),\qquad \theta_p=2\arctan(v/u_p).
```

For an even-ending record $`\mathcal R`$ of length $`L`$, let $`N_{++}`$ and $`N_{--}`$ be its even and odd stay counts. Its exact phase function is $`\Phi_{\mathcal R}=N_{++}\theta_e-N_{--}\theta_p`$. Define, in the parity order $`(+,-)`$,

```math
P=\begin{pmatrix}1-p_e&p_e\\p_p&1-p_p\end{pmatrix},\qquad
S=\begin{pmatrix}1-p_e&a^2-w^2\\p_p&1-p_p\end{pmatrix}.
```

The product of $`P`$ entries along $`\mathcal R`$ is its record probability $`p_{\mathcal R}`$. The corresponding product of $`S`$ entries is the signed weight $`s_{\mathcal R}`$. The unnormalized logical off-diagonal element on an even record is $`s_{\mathcal R} e^{-i\Phi_{\mathcal R}}/2`$. In particular, using $`s_{\mathcal R}`$ avoids dividing by the probability of records that can vanish at compensation. Both the phase and the signed weight are independent of $`\phi`$.

Fix a sufficiently small jitter window and shrink the frequency band once, with both choices depending only on $`\chi`$. At $`x=\xi=0`$, $`p_e=0`$, $`p_p=\sin^2\chi`$, and the phase derivatives are $`A=\sin\chi/\chi`$ and $`A/\cos\chi`$ for the echo and the plain cell. By continuity we can require throughout the window and the band that

```math
p_e\le\min\{1/40,p_p/40\},\qquad p_e+p_p\lt 1,\qquad
\theta_e'\ge3A/4,\qquad 0\lt \theta_p'\le2A.
```

Accept a record if it ends even and $`N_{++}\ge 3L/4`$. Since the block starts even, the even probability at each step is at least the stationary even probability $`p_p/(p_p+p_e)\ge40/41`$, by the two-state recursion. Hence $`\mathbb E N_{++}\ge 39L/41`$. Markov's inequality on $`L-N_{++}`$, followed by a union bound with final parity, gives acceptance probability at least $`p_0=32/41`$. The phase derivative of every accepted record is at least $`(3L/4)(3A/4)-(L/4)2A=AL/16`$. Smoothness gives a uniform upper bound $`\beta L`$. Write $`\alpha=A/16`$.

Use a trial center $`c`$, measured in the same dimensionless units as $`x`$. After an accepted record, use the equatorial quadrature at known phase $`\Phi_{\mathcal R}(c)`$ and record its $`\pm1`$ outcome. Set the statistic to zero on a rejected record, retaining it in the experiment. Its exact mean is

```math
f_{L,c}(x)=\sum_{\mathcal R\,\mathrm{accepted}}
s_{\mathcal R}(x)\sin\bigl(\Phi_{\mathcal R}(x)-\Phi_{\mathcal R}(c)\bigr).
```

This expression can be evaluated by propagating signed weights in a table indexed by parity and the two stay counts, merging records with the same indices at every step. A sum over the accepted terminal indices then gives the mean. There are at most order $`L^2`$ entries per step, and each entry has two possible successors. Evaluation needs $`O(L^3)`$ arithmetic operations and $`O(L^2)`$ storage. The measured record needs just its stay counts to determine the final quadrature. Inverting the mean on a monotone interval can use scalar bisection.

### A uniform monotone branch

Along every record the products use the same sequence of parity indices. The absolute row sums of $`S`$ are at most one. Expanding a difference of products in one factor at a time and summing over all paths gives

```math
\sum_{\mathcal R}|p_{\mathcal R}-s_{\mathcal R}|\le2Lw^2,
\qquad
\sum_{\mathcal R}|s'_{\mathcal R}|\le C L.
```

For the first inequality the only changed transition is the echo flip, with difference $`2w^2`$. For the second, each derivative term has absolute row sum bounded by the maximum row sum of $`|S'|`$ on the fixed band and jitter window. All other factors have absolute row sums at most one. Also $`w^2\le4\chi^2\xi^2`$.

For $`|x-c|\le\eta/L`$ and $`\beta\eta\lt \pi/2`$, differentiating the mean and comparing its phase term to the nonnegative $`P`$ weights gives

```math
f'_{L,c}(x)\ge \alpha L p_0\cos(\beta\eta)
-2\beta L^2w^2-CL\sin(\beta\eta).
```

First choose a fixed small $`\eta\gt 0`$ so the last term cannot cancel the first. Then choose a fixed small $`b_0\gt 0`$ so the middle term cannot cancel the surviving bound whenever $`L\xi^2\le b_0`$. This yields $`f'_{L,c}\ge\kappa L`$ for a constant $`\kappa\gt 0`$ independent of $`L,\xi,c`$ in the stated range. The derivative estimates use unnormalized path weights, including at signed-weight zeros. The inverse mean on the known interval has Lipschitz constant at most $`1/(\kappa L)`$, including when the sample mean is clipped to its image.

## Global estimator within the hard contact budget

Set $`M=\min\{m,\lfloor(n-1)/2\rfloor\}`$, the budget for cells in the active experiment. Whenever $`M`$ exceeds a fixed constant and $`\xi`$ lies in a sufficiently small fixed window, take the largest dyadic $`L=2^J`$ satisfying

```math
L\le \min\{bM,b_0/\xi^2\},
```

where the jitter cap is absent at $`\xi=0`$ and $`b\gt 0`$ is a sufficiently small fixed constant. The window and the threshold for $`M`$ can be chosen so at least $`L=1`$ is feasible. This length is within a fixed factor of $`\min\{M,\xi^{-2}\}`$. Take a fixed $`s\gt 0`$ with $`2s\le\eta`$ and let $`I=[-hE,hE]`$ denote the full dimensionless band.

### Resolve phase ambiguity to scale $`1/L`$

Use plain one-cell trials for a clipped [coarse estimate](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/e4c8a7d4f15c3b35dda1507caf7e411502b9b100/science/microscopic_identifiability.md). The one-cell calibration has uniform exponential concentration at this fixed initial accuracy. With $`O(1+J+\log(M/L))`$ trials, the interval of radius $`s`$ about the estimate, intersected with $`I`$, misses the true $`x`$ with probability at most $`(L/M)8^{-J}`$. Call that interval $`I_0`$.

For $`j=1,\ldots,J`$ let $`L_j=2^j`$ and use the midpoint $`c_j`$ of the preceding interval $`I_{j-1}`$. Its radius is at most $`s/L_{j-1}`$, inside the monotone range $`\eta/L_j`$. Reset to the same logical input for each of

```math
r_j=\left\lceil C_1\bigl[\log(2M/L)+(J-j)\log 8\bigr]\right\rceil
```

fresh $`L_j`$-cell blocks. Invert $`f_{L_j,c_j}`$ on $`I_{j-1}`$ at their sample mean, clipped to the image. Intersect the previous interval with the interval of radius $`s/L_j`$ about this estimate to obtain $`I_j`$. Clipping keeps the estimate in the preceding interval, so the intersection is always nonempty. A singleton interval can use its unique value.

When the previous interval contains $`x`$, the inverse Lipschitz bound shows that an error exceeding $`s/L_j`$ requires a sample-mean error of at least $`\kappa s`$. Conditioned on the earlier data, the block statistics are independent and bounded in $`[-1,1]`$. Hoeffding's inequality gives a conditional miss probability at most $`(L/M)8^{-(J-j)}`$ with a large enough fixed $`C_1`$. Both the estimate and all later intervals are confined to $`I_{j-1}`$ on every branch. If the first failed refinement is at stage $`j`$, the final squared error is at most $`16s^2/L_j^2`$. The sum of these risk contributions is at most

```math
\sum_{j=1}^J \frac{16s^2}{L_j^2}\,\frac{L}{M}\,8^{-(J-j)}
\le \frac{32s^2}{ML}.
```

If the pilot fails, the band diameter bounds the error. Its risk contribution is also of order $`1/(ML)`$, since $`8^{-J}=L^{-3}`$.

The geometric sums of $`L_j`$ and $`(J-j)L_j`$ bound the localization cost, including the pilot, by $`C_2L[1+\log(M/L)]`$ cells. Choose $`b\le1/4`$ so $`C_2 t[1+\log(1/t)]\le1/4`$ for $`0\lt t\le b`$. At least $`3M/4`$ cells then remain. The schedule and its cost are fixed by $`n,m,d`$ and the hardware constants.

### Repeat the longest useful block

With the center of $`I_J`$, spend the remaining budget on $`r\ge M/(2L)`$ fresh independent $`L`$-cell blocks, again retaining outcomes on every attempt. Invert their clipped sample mean on $`I_J`$. On localization success, the sample-mean variance is at most $`1/r`$ and the inverse Lipschitz constant is at most $`1/(\kappa L)`$. The conditional mean-square error is therefore at most $`1/(r\kappa^2L^2)`$. On localization failure the final estimate stays in the last interval, so the first-failure bounds still apply. Restoring frequency units gives risk $`O(1/(h^2 ML))`$.

### Count every contact

Each used cell has at most one interior pulse and one endpoint instrument. An endpoint instrument can combine parity readout, frame correction, quadrature readout and preparation for the next block as needed. The last endpoint is counted even when the estimator finishes early. Thus the active experiment uses at most $`M`$ interior pulses and $`2M`$ total contacts. The ledger charges every attempted block, including rejections, and includes resets in the endpoint contacts. The classical estimate is held through the full charged horizon.

The plain-only design, with all $`n`$ cells and $`n-1`$ boundary contacts, supplies risk $`O(1/(h^2n))`$. Choose between the two designs from the known budgets. For $`n\ge3`$ and $`m\ge1`$, $`M\ge m/3`$. When the active design is available, $`ML`$ is within fixed factors of $`\min\{m^2,m/\xi^2\}`$, with the stated convention at zero jitter. When $`M`$ is bounded, this minimum is bounded by a constant. When $`\xi`$ is outside the small fixed window, it is at most a fixed multiple of $`m\le n`$. The plain design covers both cases, as well as $`m=0`$ and the smallest horizons. This proves the upper bound for every budget.

## Scope and antecedents

The precision law treats the existing plain or one-pulse menu, with one fixed, shared transverse angle and independent symmetric timing displacements of known amplitude. Additional interior pulses, unknown amplitude, correlated jitter and a fluctuating cell clock require their own analyses. The fixed sufficient band is chosen once for a given coupling and does not shrink with $`n,m,d`$.

The [ideal contact theorem](global_contact_precision.md) supplies the arbitrary-contact converse and ideal parity instrument. The [companion's recorded-phase estimator](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/e4c8a7d4f15c3b35dda1507caf7e411502b9b100/science/recorded_phase_estimation.md) supplies the multiscale localization structure. Here the hidden timing label changes the conditional state into a mixture, so the inverse uses the exact signed mean and repeats at the length permitted by the known jitter amplitude. That change yields a matched intermediate regime. The [timing comparisons](../references/RELATED_WORK.md#teixeira2016) place this result alongside earlier pulse-jitter, clock-error and phase-damping models.
