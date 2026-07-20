===== Page 1 =====

# Concepts in Thermal Physics Second Edition

[Image: Cover page showing three spheres. The largest is a transparent sphere with a grid of 0s and 1s on its surface. In front of it is a sphere with a red metallic piston mechanism inside. Behind them is a third small sphere showing the Earth. To the right, the equation $S = -k_B \sum_i P_i \ln P_i$ is written. The authors' names are at the bottom right.]

[Image: A close-up view of a sphere showing the Earth, with a focus on the Arctic and Greenland ice caps.]

Stephen J. Blundell and Katherine M. Blundell

===== Page 2 =====

1

===== Page 3 =====

This page intentionally left blank

===== Page 4 =====

# Concepts in Thermal Physics

# Second Edition

STEPHEN J. BLUNDELL AND KATHERINE M. BLUNDELL

Department of Physics, University of Oxford, UK

===== Page 5 =====

OXFORD UNIVERSITY PRESS

Great Clarendon Street, Oxford OX2 6DP

Oxford University Press is a department of the University of Oxford. It furthers the University's objective of excellence in research, scholarship, and education by publishing worldwide in

Oxford New York
Auckland Cape Town Dar es Salaam Hong Kong Karachi
Kuala Lumpur Madrid Melbourne Mexico City Nairobi
New Delhi Shanghai Taipei Toronto

With offices in

Argentina Austria Brazil Chile Czech Republic France Greece
Guatemala Hungary Italy Japan Poland Portugal Singapore
South Korea Switzerland Thailand Turkey Ukraine Vietnam

Oxford is a registered trade mark of Oxford University Press in the UK and in certain other countries

Published in the United States by Oxford University Press Inc., New York

© Stephen J. Blundell and Katherine M. Blundell 2010

The moral rights of the authors have been asserted

Database right Oxford University Press (maker)

First edition published in 2006
Second edition published in 2010

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, without the prior permission in writing of Oxford University Press, or as expressly permitted by law, or under terms agreed with the appropriate reprographics rights organization. Enquiries concerning reproduction outside the scope of the above should be sent to the Rights Department, Oxford University Press, at the address above

You must not circulate this book in any other binding or cover and you must impose the same condition on any acquirer

British Library Cataloguing in Publication Data
Data available

Library of Congress Cataloging in Publication Data
Data available

Printed in Great Britain
on acid-free paper by
CPI Antony Rowe, Chippenham, Wilts.

ISBN 978-0-19-956209-1 (Hbk.)
ISBN 978-0-19-956210-7 (Pbk.)

10 9 8 7 6 5 4 3 2 1

===== Page 6 =====

1

===== Page 7 =====

This page intentionally left blank

===== Page 8 =====

In the beginning was the Word...

(John 1:1, first century AD)

Consider sunbeams. When the sun's rays let in
Pass through the darkness of a shuttered room,
You will see a multitude of tiny bodies
All mingling in a multitude of ways
Inside the sunbeam, moving in the void,
Seeming to be engaged in endless strife,
Battle, and warfare, troop attacking troop,
And never a respite, harried constantly,
With meetings and with partings everywhere.
From this you can imagine what it is
For atoms to be tossed perpetually
In endless motion through the mighty void.

(On the Nature of Things, Lucretius, first century BC)

... (we) have borne the burden of the work and the heat of the day.
(Matthew 20:12, first century AD)

[Image: A sphere covered in a grid of squares. Each square contains a single digit, either a 0 or a 1.]

Thermal physics forms a key part of any undergraduate physics course. It includes the fundamentals of classical thermodynamics (which was founded largely in the nineteenth century and motivated by a desire to understand the conversion of heat into work using engines) and also statistical mechanics (which was founded by Boltzmann and Gibbs, and is concerned with the statistical behaviour of the underlying microstates of the system). Students often find these topics hard, and this problem is not helped by a lack of familiarity with basic concepts in mathematics, particularly in probability and statistics. Moreover, the traditional focus of thermodynamics on steam engines seems remote and largely irrelevant to a twenty-first century student. This is unfortunate since an understanding of thermal physics is crucial to almost all modern physics and to the important technological challenges which face us in this century.

The aim of this book is to provide an introduction to the key concepts in thermal physics, fleshed out with plenty of modern examples from astrophysics, atmospheric physics, laser physics, condensed matter physics and information theory. The important mathematical principles, particularly concerning probability and statistics, are expounded in some detail. This aims to make up for the material which can no longer be automatically assumed to have been covered in every school

===== Page 9 =====

mathematics course. In addition, the appendices contain useful mathematics, such as various integrals, mathematical results and identities. There is, unfortunately, no shortcut to mastering the necessary mathematics in studying thermal physics, but the material in the appendix provides a useful aide-mémoire.

Many courses on this subject are taught historically: the kinetic theory of gases, then classical thermodynamics are taught first, with statistical mechanics taught last. In other courses, one starts with the principles of classical thermodynamics, followed then by statistical mechanics and kinetic theory is saved until the end. Although there is merit in both approaches, we have aimed at a more integrated treatment. For example, we introduce temperature using a straightforward statistical mechanical argument, rather than on the basis of a somewhat abstract Carnot engine. However, we do postpone detailed consideration of the partition function and statistical mechanics until after we have introduced the functions of state, which manipulation of the partition function so conveniently produces. We present the kinetic theory of gases fairly early on, since it provides a simple, well-defined arena in which to practise simple concepts in probability distributions. This has worked well in the course given in Oxford, but since kinetic theory is only studied at a later stage in courses in other places, we have designed the book so that the kinetic theory chapters can be omitted without causing problems; see Fig. 1.5 on page 10 for details. In addition, some parts of the book contain material that is much more advanced (often placed in boxes, or in the final part of the book), and these can be skipped at first reading.

The book is arranged in a series of short, easily digestible chapters, each one introducing a new concept or illustrating an important application. Most people learn from examples, so plenty of worked examples are given in order that the reader can gain familiarity with the concepts as they are introduced. Exercises are provided at the end of each chapter to allow the students to gain practice in each area.

In choosing which topics to include, and at what level, we have aimed for a balance between pedagogy and rigour, providing a comprehensible introduction with sufficient details to satisfy more advanced readers. We have also tried to balance fundamental principles with practical applications. However, this book does not treat real engines in any engineering depth, nor does it venture into the deep waters of ergodic theory. Nevertheless, we hope that there is enough in this book for a thorough grounding in thermal physics and the recommended further reading gives pointers for additional material. An important theme running through this book is the concept of information, and its connection with entropy. The black hole shown at the start of this preface, with its surface covered in 'bits' of information, is a helpful picture of the deep connection between information, thermodynamics, radiation, and the Universe.

The history of thermal physics is a fascinating one, and we have provided a selection of short biographical sketches of some of the key pioneers in thermal physics. To qualify for inclusion, the person had to

===== Page 10 =====

have made a particularly important contribution or had a particularly interesting life - and be dead! Therefore one should not conclude from the list of people we have chosen that the subject of thermal physics is in any sense finished, it is just harder to write with the same perspective about current work in this subject. The biographical sketches are necessarily brief, giving only a glimpse of the life-story, so the Bibliography should be consulted for a list of more comprehensive biographies. However, the sketches are designed to provide some light relief in the main narrative and demonstrate that science is a human endeavour.

It is a great pleasure to record our gratitude to those who taught us the subject while we were undergraduates in Cambridge, particularly Owen Saxton and Peter Scheuer, and to our friends in Oxford: we have benefitted from many enlightening discussions with colleagues in the physics department, from the intelligent questioning of our Oxford students and from the stimulating environments provided by both Mansfield College and St John's College. In the writing of this book, we have enjoyed the steadfast encouragement of Sonke Adlung and his colleagues at OUP, and in particular Julie Harris' black-belt $\mathrm{\LaTeX}$ support.

A number of friends and colleagues in Oxford and elsewhere have been kind enough to give their time and read drafts of chapters of this book; they have made numerous helpful comments, which have greatly improved the final result: Fathallah Alouani Bibi, James Analytis, David Andrews, Arzhang Ardavan, Tony Beasley, Michael Bowler, Peter Duffy, Paul Goddard, Stephen Justham, Michael Mackey, Philipp Podsiadlowski, Linda Schmidtobreick, John Singleton and Katrien Steenbrugge. Particular thanks are due to Tom Lancaster, who twice read the entire manuscript at early stages and made many constructive and imaginative suggestions, and to Harvey Brown, whose insights were always stimulating and whose encouragement was always constant. To all these friends, our warmest thanks are due. Errors which we discover after going to press will be posted on the book's website, which may be found at:

http://users.ox.ac.uk/~sjb/ctp

It is our earnest hope that this book will make the study of thermal physics enjoyable and fascinating and that we have managed to communicate something of the enthusiasm we feel for this subject. Moreover, understanding the concepts of thermal physics is vital for humanity's future; the impending energy crisis and the potential consequences of climate change mandate creative, scientific, and technological innovations at the highest levels. This means that thermal physics is a field that some of tomorrow's best minds need to master today.

SJB & KMB
Oxford
June 2006

===== Page 11 =====

1

## Preface to the second edition

This new edition keeps the same structure as the first edition but includes additional material on probability, Bayes' theorem, diffusion problems, osmosis, the Ising model, Monte-Carlo simulations, and radiative transfer in atmospheric physics. We have also taken the opportunity to improve the treatment of various topics, including the discussion of constraints and the presentation of the Fermi-Dirac and Bose-Einstein distributions, as well as correcting various errors. We are particularly grateful to the following people who have pointed out errors or omissions and made highly relevant comments: David Andrews, John Aveson, Ryan Buckingham, Radu Coldea, Merlin Cooper, Peter Coulon, Peter Duffy, Ted Einstein, Joe Fallon, Amy Fok, Felix Flicker, William Frass, Andrew Garner, Paul Hennin, Ben Jones, Stephen Justham, Austen Lamacraft, Peter Liley, Gabriel McManus, Adam Micolich, Robin Moss, Alan O'Neill, Elena Nickson, Wilson Poon, Caity Rice, Andrew Steane, Nicola van Leeuwen, Yan Mei Wang, Peter Watson, Helena Wilding, and Michael Williams. We have once again enjoyed the support of the staff of OUP and, in particular, our copy-editor Alison Lees, who trawled through the manuscript with meticulous care, making many important improvements. Myles Allen, David Andrews, and William Ingram gave us very pertinent and instructive comments about the treatment of atmospheric physics and their input has been invaluable. Thanks are also due to Geoff Brooker, who shared his profound insights into the nature of free energies, and Tom Lancaster, who once again made numerous helpful suggestions.

SJB & KMB
Oxford
August 2009

===== Page 12 =====

1  Introduction  2
1.1 What is a mole?  3
1.2 The thermodynamic limit  4
1.3 The ideal gas  6
1.4 Combinatorial problems  7
1.5 Plan of the book  9
Exercises  12

2  Heat  13
2.1 A definition of heat  13
2.2 Heat capacity  14
Exercises  17

3  Probability  18
3.1 Discrete probability distributions  19
3.2 Continuous probability distributions  20
3.3 Linear transformation  21
3.4 Variance  22
3.5 Linear transformation and the variance  23
3.6 Independent variables  24
3.7 Binomial distribution  26
Further reading  29
Exercises  29

4  Temperature and the Boltzmann factor  32
4.1 Thermal equilibrium  32
4.2 Thermometers  33
4.3 The microstates and macrostates  35
4.4 A statistical definition of temperature  36
4.5 Ensembles  38
4.6 Canonical ensemble  38
4.7 Applications of the Boltzmann distribution  42
Further reading  46
Exercises  46

===== Page 13 =====

5  The Maxwell-Boltzmann distribution  47
5.1 The velocity distribution  48
5.2 The speed distribution  49
5.3 Experimental justification  51
Exercises  54

6  Pressure  56
6.1 Molecular distributions  57
6.2 The ideal gas law  58
6.3 Dalton's law  60
Exercises  61

7  Molecular effusion  64
7.1 Flux  64
7.2 Effusion  66
Exercises  69

8  The mean free path and collisions  70
8.1 The mean collision time  70
8.2 The collision cross-section  71
8.3 The mean free path  73
Exercises  74

**Part III  Transport and thermal diffusion**  75

9  Transport properties in gases  76
9.1 Viscosity  76
9.2 Thermal conductivity  81
9.3 Diffusion  83
9.4 More detailed theory  86
Further reading  88
Exercises  89

10  The thermal diffusion equation  90
10.1 Derivation of the thermal diffusion equation  90
10.2 The one-dimensional thermal diffusion equation  91
10.3 The steady state  94
10.4 The thermal diffusion equation for a sphere  94
10.5 Newton's law of cooling  99
10.6 The Prandtl number  100
10.7 Sources of heat  101
10.8 Particle diffusion  102
Exercises  103

===== Page 14 =====

**Part IV  The first law**  107

11  Energy  108
11.1 Some definitions  108
11.2 The first law of thermodynamics  110
11.3 Heat capacity  112
Exercises  115

12  Isothermal and adiabatic processes  118
12.1 Reversibility  118
12.2 Isothermal expansion of an ideal gas  120
12.3 Adiabatic expansion of an ideal gas  121
12.4 Adiabatic atmosphere  121
Exercises  123

**Part V  The second law**  125

13  Heat engines and the second law  126
13.1 The second law of thermodynamics  126
13.2 The Carnot engine  127
13.3 Carnot's theorem  130
13.4 Equivalence of Clausius' and Kelvin's statements  131
13.5 Examples of heat engines  131
13.6 Heat engines running backwards  133
13.7 Clausius' theorem  134
Further reading  137
Exercises  137

14  Entropy  140
14.1 Definition of entropy  140
14.2 Irreversible change  140
14.3 The first law revisited  142
14.4 The Joule expansion  144
14.5 The statistical basis for entropy  146
14.6 The entropy of mixing  147
14.7 Maxwell's demon  149
14.8 Entropy and probability  150
Exercises  153

15  Information theory  157
15.1 Information and Shannon entropy  157
15.2 Information and thermodynamics  159
15.3 Data compression  160
15.4 Quantum information  162
15.5 Conditional and joint probabilities  165
15.6 Bayes' theorem  165
Further reading  168
Exercises  169

===== Page 15 =====

**Part VI  Thermodynamics in action**  171

16  Thermodynamic potentials  172
16.1 Internal energy, $U$  172
16.2 Enthalpy, $H$  173
16.3 Helmholtz function, $F$  174
16.4 Gibbs function, $G$  175
16.5 Constraints  176
16.6 Maxwell's relations  179
Exercises  187

17  Rods, bubbles, and magnets  191
17.1 Elastic rod  191
17.2 Surface tension  194
17.3 Electric and magnetic dipoles  195
17.4 Paramagnetism  196
Exercises  201

18  The third law  203
18.1 Different statements of the third law  203
18.2 Consequences of the third law  205
Exercises  208

**Part VII  Statistical mechanics**  209

19  Equipartition of energy  210
19.1 Equipartition theorem  210
19.2 Applications  213
19.3 Assumptions made  215
19.4 Brownian motion  217
Exercises  218

20  The partition function  219
20.1 Writing down the partition function  220
20.2 Obtaining the functions of state  221
20.3 The big idea  228
20.4 Combining partition functions  228
Exercises  232

21  Statistical mechanics of an ideal gas  233
21.1 Density of states  233
21.2 Quantum concentration  235
21.3 Distinguishability  236
21.4 Functions of state of the ideal gas  237
21.5 Gibbs paradox  240
21.6 Heat capacity of a diatomic gas  241
Exercises  243

===== Page 16 =====

22  The chemical potential  244
22.1 A definition of the chemical potential  244
22.2 The meaning of the chemical potential  245
22.3 Grand partition function  247
22.4 Grand potential  248
22.5 Chemical potential as Gibbs function per particle  250
22.6 Many types of particle  250
22.7 Particle number conservation laws  251
22.8 Chemical potential and chemical reactions  252
22.9 Osmosis  257
Further reading  261
Exercises  262

23  Photons  263
23.1 The classical thermodynamics of electromagnetic radiation  264
23.2 Spectral energy density  265
23.3 Kirchhoff's law  266
23.4 Radiation pressure  268
23.5 The statistical mechanics of the photon gas  269
23.6 Black-body distribution  270
23.7 Cosmic microwave background radiation  273
23.8 The Einstein A and B coefficients  274
Further reading  277
Exercises  278

24  Phonons  279
24.1 The Einstein model  279
24.2 The Debye model  281
24.3 Phonon dispersion  284
Further reading  287
Exercises  287

**Part VIII  Beyond the ideal gas**  289

25  Relativistic gases  290
25.1 Relativistic dispersion relation for massive particles  290
25.2 The ultrarelativistic gas  290
25.3 Adiabatic expansion of an ultrarelativistic gas  293
Exercises  295

26  Real gases  296
26.1 The van der Waals gas  296
26.2 The Dieterici equation  304
26.3 Virial expansion  306
26.4 The law of corresponding states  310
Exercises  312

===== Page 17 =====

27  Cooling real gases  313
27.1 The Joule expansion  313
27.2 Isothermal expansion  315
27.3 Joule-Kelvin expansion  316
27.4 Liquefaction of gases  318
Exercises  320

28  Phase transitions  321
28.1 Latent heat  321
28.2 Chemical potential and phase changes  324
28.3 The Clausius-Clapeyron equation  324
28.4 Stability and metastability  329
28.5 The Gibbs phase rule  332
28.6 Colligative properties  334
28.7 Classification of phase transitions  335
28.8 The Ising model  338
Further reading  343
Exercises  343

29  Bose-Einstein and Fermi-Dirac distributions  345
29.1 Exchange and symmetry  345
29.2 Wave functions of identical particles  346
29.3 The statistics of identical particles  349
Further reading  353
Exercises  354

30  Quantum gases and condensates  358
30.1 The non-interacting quantum fluid  358
30.2 The Fermi gas  361
30.3 The Bose gas  366
30.4 Bose-Einstein condensation (BEC)  367
Further reading  373
Exercises  373

**Part IX  Special topics**  375

31  Sound waves  376
31.1 Sound waves under isothermal conditions  377
31.2 Sound waves under adiabatic conditions  377
31.3 Are sound waves in general adiabatic or isothermal?  378
31.4 Derivation of the speed of sound within fluids  379
Further reading  382
Exercises  382

32  Shock waves  383
32.1 The Mach number  383
32.2 Structure of shock waves  383
32.3 Shock conservation laws  385

===== Page 18 =====

32.4 The Rankine-Hugoniot conditions  386
Further reading  389
Exercises  389

33  Brownian motion and fluctuations  390
33.1 Brownian motion  390
33.2 Johnson noise  393
33.3 Fluctuations  394
33.4 Fluctuations and the availability  395
33.5 Linear response  397
33.6 Correlation functions  400
Further reading  407
Exercises  407

34  Non-equilibrium thermodynamics  408
34.1 Entropy production  408
34.2 The kinetic coefficients  409
34.3 Proof of the Onsager reciprocal relations  410
34.4 Thermoelectricity  413
34.5 Time reversal and the arrow of time  417
Further reading  419
Exercises  419

35  Stars  420
35.1 Gravitational interaction  421
35.2 Nuclear reactions  426
35.3 Heat transfer  427
Further reading  434
Exercises  434

36  Compact objects  435
36.1 Electron degeneracy pressure  435
36.2 White dwarfs  437
36.3 Neutron stars  438
36.4 Black holes  440
36.5 Accretion  441
36.6 Black holes and entropy  442
36.7 Life, the Universe, and entropy  443
Further reading  445
Exercises  445

37  Earth's atmosphere  446
37.1 Solar energy  446
37.2 The temperature profile in the atmosphere  447
37.3 Radiative transfer  449
37.4 The greenhouse effect  452
37.5 Global warming  456
Further reading  460
Exercises  460

===== Page 19 =====

A  Fundamental constants  461
B  Useful formulae  462
C  Useful mathematics  464
C.1 The factorial integral  464
C.2 The Gaussian integral  464
C.3 Stirling's formula  467
C.4 Riemann zeta function  469
C.5 The polylogarithm  470
C.6 Partial derivatives  471
C.7 Exact differentials  472
C.8 Volume of a hypersphere  473
C.9 Jacobians  473
C.10 The Dirac delta function  475
C.11 Fourier transforms  475
C.12 Solution of the diffusion equation  476
C.13 Lagrange multipliers  477
D  The electromagnetic spectrum  479
E  Some thermodynamical definitions  480
F  Thermodynamic expansion formulae  481
G  Reduced mass  482
H  Glossary of main symbols  483
Bibliography  485
Index  489

===== Page 20 =====

1

# Preliminaries

To explore and understand the rich and beautiful subject that is thermal physics, we need some essential tools in place. Part I provides these, as follows:

In Chapter 1 we explore the concept of large numbers, showing why large numbers appear in thermal physics and explaining how to handle them. Large numbers arise in thermal physics because the number of atoms in the bit of matter under study is usually very large (for example, it can be typically of the order of \(10^{23}\)), but also because many thermal physics problems involve combinatorial calculations (and this can produce numbers like \(10^{23}!\), where "!" here means a factorial). We introduce Stirling's approximation, which is useful for handling expressions, such as \(\ln N!\), which frequently appear in thermal physics. We discuss the thermodynamic limit and state the ideal gas equation (derived later, in Chapter 6, from the kinetic theory of gases). In Chapter 2 we explore the concept of heat, defining it as "thermal energy in transit", and introduce the idea of a heat capacity. The ways in which thermal systems behave is determined by the laws of probability, so we outline the notion of probability in Chapter 3 and apply it to a number of problems. This chapter may well cover ground that is familiar to some readers, but is a useful introduction to the subject. We then use these ideas to define the temperature of a system from a statistical perspective and hence derive the Boltzmann distribution in Chapter 4. This distribution describes how a thermal system behaves when it is placed in thermal contact with a large thermal reservoir. This is a key concept in thermal physics and forms the basis of all that follows.

===== Page 21 =====

# 1 Introduction

1.1 What is a mole? 3
1.2 The thermodynamic limit 4
1.3 The ideal gas 6
1.4 Combinatorial problems 7
1.5 Plan of the book 9
Chapter summary 12
Exercises 12

Some large numbers:

| Number | Value |
| :--- | :--- |
| million | $10^6$ |
| billion | $10^9$ |
| trillion | $10^{12}$ |
| quadrillion | $10^{15}$ |
| quintillion | $10^{18}$ |
| googol | $10^{100}$ |
| googolplex | $10^{10^{100}}$ |

Note: these values assume the US billion, trillion, etc, which are now in general use.

The subject of thermal physics involves studying assemblies of large numbers of atoms. As we will see, it is the large numbers involved in macroscopic systems that allow us to treat some of their properties in a statistical fashion. What do we mean by a large number?

Large numbers turn up in many spheres of life. A book might sell a million $(10^{6})$ copies (probably not this one), the Earth's population is (at the time of writing) between six and seven billion people $(6 - 7\times 10^{9})$, and the US national debt is currently around ten trillion dollars $(10^{13}$ US$). But even these large numbers pale into insignificance compared with the numbers involved in thermal physics. The number of atoms in an average-sized piece of matter is usually ten to the power of twentysomething, and this puts extreme limits on what sort of calculations we can make to understand them.

## Example 1.1

One kilogramme of nitrogen gas contains approximately $2\times 10^{25}$ $\mathrm{N}_{2}$ molecules. Let us see how easy it would be to make predictions about the motion of the molecules in this amount of gas. In one year, there are about $3.2\times 10^{7}$ seconds, so that a 3 GHz personal computer can count molecules at a rate of roughly $10^{17}$ year$^{-1}$, if it counts one molecule every computer clock cycle. Therefore it would take about 0.2 billion years just for this computer to count all the molecules in one kilogramme of nitrogen gas (a time that is roughly a few percent of the age of the Universe!). Counting the molecules is a computationally simpler task than calculating all their movements and collisions with each other. Therefore modelling this quantity of matter by following each and every particle is a hopeless task.

Hence, to make progress in thermal physics it is necessary to make approximations and deal with the statistical properties of molecules, i.e., to study how they behave on average. Chapter 3 therefore contains a discussion of probability and statistical methods, which are foundational for understanding thermal physics. In this chapter, we will briefly review the definition of a mole (which will be used throughout the book), consider why very big numbers arise from combinatorial problems in thermal physics and introduce the thermodynamic limit and the ideal gas equation.

===== Page 22 =====

## 1.1 What is a mole?

A mole is, of course, a small burrowing animal, but also a name (first coined about a century ago from the German "Molekil" [molecule]) representing a certain numerical quantity of stuff. It functions in the same way as the word "dozen", which describes a certain number of eggs (12), or "score", which describes a certain number of years (20). It might be easier if we could use the word dozen when describing a certain number of atoms, but a dozen atoms is not many (unless you are building a quantum computer) and since a million, a billion, and even a quadrillion are also too small to be useful, we have ended up with using an even bigger number. Unfortunately, for historical reasons, it isn't a power of ten.

## The mole

A mole is defined as the quantity of matter that contains as many objects (for example, atoms, molecules, formula units, or ions) as the number of atoms in exactly $12\mathrm{g}$ $(= 0.012\mathrm{kg})$ of $^{12}\mathrm{C}$.

A mole is also approximately the quantity of matter that contains as many objects (for example, atoms, molecules, formula units, ions) as the number of atoms in exactly $1\mathrm{g}$ $(= 0.001\mathrm{kg})$ of $^{1}\mathrm{H}$, but carbon was chosen as a more convenient international standard since solids are easier to weigh accurately.

A mole of atoms is equivalent to an Avogadro number $N_{\mathrm{A}}$ of atoms. The Avogadro number, expressed to four significant figures, is

$$N_{\mathrm{A}} = 6.022\times 10^{23}. \quad (1.1)$$

One can write $N_{\mathrm{A}}$ as $6.022\times 10^{23}\mathrm{mol}^{-1}$ as a reminder of its definition, but $N_{\mathrm{A}}$ is dimensionless, as are moles. They are both numbers. By the same logic, one would have to define the 'eggbox number' as 12 dozen$^{-1}$.

## Example 1.2

- 1 mole of carbon is $6.022\times 10^{23}$ atoms of carbon.
- 1 mole of benzene is $6.022\times 10^{23}$ molecules of benzene.
- 1 mole of NaCl contains $6.022\times 10^{23}$ NaCl formula units, etc.

The Avogadro number is an exceedingly large number: a mole of eggs would make an omelette with about half the mass of the Moon!

The molar mass of a substance is the mass of one mole of the substance. Thus the molar mass of carbon is $12\mathrm{g}$, but the molar mass of water is close to $18\mathrm{g}$ (because the mass of a water molecule is about $\frac{18}{12}$ times larger than the mass of a carbon atom). The mass $m$ of a single molecule or atom is therefore the molar mass of that substance divided by the Avogadro number. Equivalently:

$$\mathrm{molar~mass} = mN_{\mathrm{A}}. \quad (1.2)$$

===== Page 23 =====

[Image: Three graphs (a), (b), and (c) of force F versus time t. (a) shows three small, sparse vertical spikes. (b) shows many more, slightly taller spikes. (c) shows a dense forest of tall spikes, with the average value appearing much more constant.]
**Fig. 1.1** Graphs of the force on a roof as a function of time due to falling rain drops.

## 1.2 The thermodynamic limit

In this section, we will explain how the large numbers of molecules in a typical thermodynamic system mean that it is possible to deal with average quantities. Our explanation proceeds using an analogy: imagine that you are sitting inside a tiny hut with a flat roof. It is raining outside, and you can hear the occasional raindrop striking the roof. The raindrops arrive randomly, so sometimes two arrive close together, but sometimes there is quite a long gap between raindrops. Each raindrop transfers its momentum to the roof and exerts an impulse on it. If you knew the mass and terminal velocity of a raindrop, you could estimate the force on the roof of the hut. The force as a function of time would look like that shown in Fig. 1.1(a), each little blip corresponding to the impulse from one raindrop.

Now imagine that you are sitting inside a much bigger hut with a flat roof a thousand times the area of the first roof. Many more raindrops will now be falling on the larger roof area and the force as a function of time would look like that shown in Fig. 1.1(b). Now scale up the area of the flat roof by a further factor of one hundred and the force would look like that shown in Fig. 1.1(c). Notice two key things about these graphs:

(1) The force, on average, gets bigger as the area of the roof gets bigger. This is not surprising because a bigger roof catches more raindrops.
(2) The fluctuations in the force get smoothed out and the force looks like it stays much closer to its average value. In fact, the fluctuations are still big but, as the area of the roof increases, they grow more slowly than the average force does.

The force grows with area, so it is useful to consider the pressure, which is defined as

$$\mathrm{pressure} = \frac{\mathrm{force}}{\mathrm{area}}. \quad (1.3)$$

The average pressure due to the falling raindrops will not change as the area of the roof increases, but the fluctuations in the pressure will decrease. In fact, we can completely ignore the fluctuations in the pressure in the limit that the area of the roof grows to infinity. This is precisely analogous to the limit we refer to as the thermodynamic limit.

Consider now the molecules of a gas which are bouncing around in a container. Each time the molecules bounce off the walls of the container, they exert an impulse on the walls. The net effect of all these impulses is a pressure, a force per unit area, exerted on the walls of the container. If the container were very small, we would have to worry about fluctuations in the pressure (the random arrival of individual molecules on the wall, much like the raindrops in Fig. 1.1(a)). However, in most cases that one meets, the number of molecules in a container of gas is extremely large, so these fluctuations can be ignored and the pressure of the gas appears to be completely uniform. Again, our description of the pressure of this

===== Page 24 =====

system can be said to be "in the thermodynamic limit", where we have let the number of molecules be regarded as tending to infinity in such a way that the density of the gas is a constant.

Suppose that the container of gas has volume $V$, that the temperature is $T$, the pressure is $p$, and the kinetic energy of all the gas molecules adds up to $U$. Imagine slicing the container of gas in half with an imaginary plane, and now just focus your attention on the gas on one side of the plane. The volume of this half of the gas, let's call it $V^{*}$, is by definition half that of the original container, i.e.,

$$V^{*} = \frac{V}{2}. \quad (1.4)$$

The kinetic energy of this half of the gas, let's call it $U^{*}$, is clearly half that of the total kinetic energy, i.e.,

$$U^{*} = \frac{U}{2}. \quad (1.5)$$

However, the pressure $p^{*}$ and the temperature $T^{*}$ of this half of the gas are the same as for the whole container of gas, so that

$$p^{*} = p, \quad T^{*} = T. \quad (1.6)$$

Variables which scale with the system size, like $V$ and $U$, are called extensive variables. Those which are independent of system size, like $p$ and $T$, are called intensive variables.

Thermal physics evolved in various stages and has left us with various approaches to the subject:

The subject of classical thermodynamics deals with macroscopic properties, such as pressure, volume, and temperature, without worrying about the underlying microscopic physics. It applies to systems that are sufficiently large that microscopic fluctuations can be ignored, and it does not assume that there is an underlying atomic structure to matter. The kinetic theory of gases tries to determine the properties of gases by considering probability distributions associated with the motions of individual molecules. This was initially somewhat controversial since the existence of atoms and molecules was doubted by many until the late nineteenth and early twentieth centuries. The realization that atoms and molecules exist led to the development of statistical mechanics. Rather than starting with descriptions of macroscopic properties (as in thermodynamics) this approach begins with trying to describe the individual microscopic states of a system and then uses statistical methods to derive the macroscopic properties from them. This approach received an additional impetus with the development of quantum theory, which showed explicitly how to describe the microscopic quantum

===== Page 25 =====

states of different systems. The thermodynamic behaviour of a system is then asymptotically approximated by the results of statistical mechanics in the thermodynamic limit, i.e., as the number of particles tends to infinity (with intensive quantities such as pressure and density remaining finite).

In the next section, we will state the ideal gas law, which was first found experimentally but can be deduced from the kinetic theory of gases (see Chapter 6).

## 1.3 The ideal gas

Experiments on gases show that the pressure $p$ of a volume $V$ of gas depends on its temperature $T$. For example, a fixed amount of gas at constant temperature obeys

$$p\propto 1/V, \quad (1.8)$$

a result which is known as Boyle's law (sometimes as the Boyle-Mariotte law); it was discovered experimentally by Robert Boyle (1627-1691) in 1662 and independently by Edmé Mariotte (1620-1684) in 1676. At constant pressure, the gas also obeys

$$V\propto T, \quad (1.9)$$

where $T$ is measured in kelvin. This is known as Charles' law and was discovered experimentally, in a crude fashion, by Jacques Charles (1746-1823) in 1787, and more completely by Joseph Louis Gay-Lussac (1778-1850) in 1802, though their work was partly anticipated by Guillaume Amontons (1663-1705) in 1699, who also noticed that a fixed volume of gas obeys

$$p\propto T, \quad (1.10)$$

a result that Gay-Lussac himself found independently in 1809 and is often known as Gay-Lussac's law.

These three empirical laws can be combined to give

$$pV\propto T. \quad (1.11)$$

It turns out that, if there are $N$ molecules in the gas, this finding can be expressed as follows:

$$pV = Nk_{\mathrm{B}}T. \quad (1.12)$$

This is known as the ideal gas equation, and the constant $k_{\mathrm{B}}$ is known as the Boltzmann constant. We now make some comments about the ideal gas equation.

We have stated this law purely as an empirical law, observed in experiment. We will derive it from first principles using the kinetic theory of gases in Chapter 6. This theory assumes that a gas can be modelled as a collection of individual tiny particles which can bounce off the walls of the container, and each other (see Fig. 1.2).

===== Page 26 =====

[Image: A square box containing several small circles, each with a line with an arrowhead attached, representing molecules moving and bouncing off the walls of the container.]
**Fig. 1.2** In the kinetic theory of gases, a gas is modelled as a number of individual tiny particles which can bounce off the walls of the container, and each other.

Why do we call it "ideal"? The microscopic justification that we will present in Chapter 6 proceeds under various assumptions: (i) we assume that there are no intermolecular forces, so that the molecules are not attracted to each other; (ii) we assume that molecules are point-like and have zero size. These are idealized assumptions and so we do not expect the ideal gas model to describe real gases under all circumstances. However, it does have the virtue of simplicity: eqn 1.12 is simple to write down and remember. Perhaps more importantly, it does describe gases quite well under quite a wide range of conditions.

The ideal gas equation forms the basis of much of our study of classical thermodynamics. Gases are common in nature: they are encountered in astrophysics and atmospheric physics; it is gases which are used to drive engines, and thermodynamics was invented to try and understand engines. Therefore this equation is fundamental in our treatment of thermodynamics and should be memorized.

The ideal gas law, however, doesn't describe all important gases, and several chapters in this book are devoted to seeing what happens when various assumptions fail. For example, the ideal gas equation assumes that the gas molecules move non-relativistically. When this is not the case, we have to develop a model of relativistic gases (see Chapter 25). At low temperatures and high densities, gas molecules do attract one another (this must occur for liquids and solids to form) and this is considered in Chapters 26, 27, and 28. Furthermore, when quantum effects are important we need a model of quantum gases, and this is outlined in Chapter 30.

Of course, thermodynamics applies also to systems which are not gaseous (so the ideal gas equation, though useful, is not a cure for all ills), and we will look at the thermodynamics of rods, bubbles, and magnets in Chapter 17.

## 1.4 Combinatorial problems

Even larger numbers than $N_{\mathrm{A}}$ occur in problems involving combinations, and these turn out to be very important in thermal physics. The following example illustrates a simple combinatorial problem which captures the essence of what we are going to have to deal with.

## Example 1.3

Let us imagine that a certain system contains ten atoms. Each of these atoms can exist in one of two states, according to whether it has zero units or one unit of energy. These "units" of energy are called quanta of energy. How many distinct arrangements of quanta are possible for this system if you have at your disposal (a) ten quanta of energy; (b) four quanta of energy?

===== Page 27 =====

[Image: Ten circles in a row. Some are open (empty) and some are filled with black (occupied by a quantum).]
**Fig. 1.3** Ten atoms that can accommodate four quanta of energy. An atom with a single quantum of energy is shown as a filled circle, otherwise it is shown as an empty circle. One configuration is shown here.

## Solution:

We can represent the ten atoms by drawing ten boxes; an empty box signifies an atom with zero quanta of energy; a filled box signifies an atom with one quantum of energy (see Fig. 1.3). We give two methods for calculating the number of ways of arranging $r$ quanta among $n$ atoms:

(1) In the first method, we realize that the first quantum can be assigned to any of the $n$ atoms, the second quantum can be assigned to any of the remaining atoms (there are $n - 1$ of them), and so on until the $r^{\mathrm{th}}$ quantum can be assigned to any of the remaining $n - r + 1$ atoms. Thus our first guess for the number of possible arrangements of the $r$ quanta we have assigned is $\Omega_{\mathrm{guess}} = n\times (n - 1)\times (n - 2)\times \ldots \times (n - r + 1)$. This can be simplified as follows:

$$\Omega_{\mathrm{guess}} = \frac{n\times(n - 1)\times(n - 2)\times\ldots\times1}{(n - r)\times(n - r - 1)\times\ldots\times1} = \frac{n!}{(n - r)!}. \quad (1.13)$$

However, this assumes that we have labelled the quanta as "the first quantum", "the second quantum" etc. In fact, we don't care which quantum is which because they are indistinguishable. We can rearrange the $r$ quanta in any one of $r!$ arrangements. Hence our answer $\Omega_{\mathrm{guess}}$ needs to be divided by $r!$, so that the number $\Omega$ of unique arrangements is

$$\Omega = \frac{n!}{(n - r)!r!}\equiv {}^{n}C_{r}, \quad (1.14)$$

where ${}^{n}C_{r}$ is the symbol for a combination.

(2) In the second method, we recognize that there are $r$ atoms each with one quantum and $n - r$ atoms with zero quanta. The number of arrangements is then simply the number of ways of arranging $r$ ones and $n - r$ zeros. There are $n!$ ways of arranging a sequence of $n$ distinguishable symbols. If $r$ of these symbols are the same (all ones), there are $r!$ ways of arranging these without changing the pattern. If the remaining $n - r$ symbols are all the same (all zeros), there are $(n - r)!$ ways of arranging these without changing the pattern. Hence we again find that

$$\Omega = \frac{n!}{(n - r)!r!}. \quad (1.15)$$

For the specific cases shown in Fig. 1.4:

(a) $n = 10$, $r = 10$ so $\Omega = 10! / (10! \times 0!)=1$. This one possibility, with each atom having a quantum of energy, is shown in Fig. 1.4(a).
(b) $n = 10$, $r = 4$ so $\Omega = 10! / (6! \times 4!)=210$. A few of these possibilities are shown in Fig. 1.4(b).

If instead we had chosen ten times as many atoms (so $n = 100$) and ten times as many quanta, the numbers for (b) would have come out much much bigger. In this case, we would have $r = 40$, $\Omega \sim 10^{28}$. A further factor of ten sends these numbers up much further, so for $n = 1000$ and $r = 400$, $\Omega \sim 10^{290}$ - a staggeringly large number.

[Image: Two rows (a) and (b). (a) shows ten filled circles. (b) shows three different rows of ten circles each, with a different pattern of open and filled circles.]
**Fig. 1.4** Each row shows the ten atoms that can accommodate $r$ quanta of energy. An atom with a single quantum of energy is shown as a filled circle, otherwise it is shown as an empty circle. (a) For $r = 10$ there is only one possible configuration. (b) For $r = 4$ there are 210 possibilities, of which three are shown.

===== Page 28 =====

The numbers in the above example are so large because factorials increase very quickly. In our example we treated 10 atoms; we are clearly going to run into trouble when we attempt to deal with a mole of atoms, i.e., when $n = 6\times 10^{23}$.

One way of bringing large numbers down to size is to look at their logarithms. Thus, if $\Omega$ is given by eqn 1.15, we could calculate

$$\ln \Omega = \ln (n!) - \ln ((n - r)! - \ln (r!). \quad (1.16)$$

This expression involves the logarithm of a factorial, and it is going to be very useful to be able to evaluate this. Most pocket calculators have difficulty in evaluating factorials above 69! (because $70! > 10^{100}$ and many pocket calculators give an overflow error for numbers above $9.999\times 10^{99}$), so some low cunning will be needed to overcome this. Such low cunning is provided by an expression termed Stirling's formula:

$$\ln n! \approx n\ln n - n. \quad (1.17)$$

This expression is derived in Appendix C.3.

## Example 1.4

Estimate the order of magnitude of $10^{23}!$

Solution:

Using Stirling's formula, we can estimate

$$\ln 10^{23}! \approx 10^{23}\ln 10^{23} - 10^{23} = 5.2\times 10^{24}, \quad (1.18)$$

and hence

$$10^{23}! = \exp (\ln 10^{23}!)\approx \exp (5.20\times 10^{24}). \quad (1.19)$$

We have our answer in the form $\mathrm{e}^{x}$, but we would really like it as ten to some power. Now if $\mathrm{e}^{x} = 10^{y}$, then $y = x / \ln 10$ and hence

$$10^{23}! \approx 10^{2.26\times 10^{24}}. \quad (1.20)$$

Just pause for a moment to take in how big this number is. It is roughly one followed by about $2.26\times 10^{24}$ zeros! Our claim that combinatorial numbers are big seems to be justified!

## 1.5 Plan of the book

This book aims to introduce the concepts of thermal physics one by one, steadily building up the techniques and ideas that make up the subject. Part I contains various preliminary topics. In Chapter 2 we define heat and introduce the idea of heat capacity. In Chapter 3, the ideas of probability are presented for discrete and continuous distributions. (For

===== Page 29 =====

[Image: A flowchart diagram showing the structure of the book. Part I (Chapters 1-4) has an arrow pointing to Part II (Chapters 5-8). A dashed arrow from Part I bypasses Part II and goes directly to Part IV. Part II has an arrow to Part III (Chapters 9-10). Part III has an arrow to Part IV. Part IV (Chapters 11-12) has an arrow to Part V (Chapters 13-15). Part V has an arrow to Part VI (Chapters 16-18). Part VI has an arrow to Part VII (Chapters 19-24). Part VII has an arrow to Part VIII (Chapters 25-30). Part VIII has an arrow to Part IX (Chapters 31-37). A grey box on the right says "omitting kinetic theory" with a dashed arrow pointing from it to Part IV.]
**Fig. 1.5** Organization of the book. The dashed line shows a possible route through the material that avoids the kinetic theory of gases. The numbers of the core chapters are given in bold type. The other chapters can be omitted on a first reading, or for a reduced-content course.

===== Page 30 =====

a reader familiar with probability theory, this chapter can be omitted.) We then define temperature in Chapter 4, and this allows us to introduce the Boltzmann distribution, which is the probability distribution for systems in contact with a thermal reservoir.

The plan for the remaining parts of the book is sketched in Fig. 1.5. The following two parts contain a presentation of the kinetic theory of gases, which justifies the ideal gas equation from a microscopic model. Part II presents the Maxwell-Boltzmann distribution of molecular speeds in a gas and the derivation of formulae for pressure, molecular effusion, and mean free path. Part III concentrates on transport and thermal diffusion. Parts II and III can be omitted in courses in which kinetic theory is treated at a later stage.

In Part IV, we begin our introduction to mainstream thermodynamics. The concept of energy is covered in Chapter 11, along with the zeroth and first laws of thermodynamics. These are applied to isothermal and adiabatic processes in Chapter 12.

Part V contains the crucial second law of thermodynamics. The idea of a heat engine is introduced in Chapter 13, which leads to various statements of the second law of thermodynamics. Hence the important concept of entropy is presented in Chapter 14 and its application to information theory is discussed in Chapter 15.

Part VI introduces the rest of the machinery of thermodynamics. Various thermodynamic potentials, such as the enthalpy, Helmholtz function, and Gibbs function, are introduced in Chapter 16, and their usage illustrated. Thermal systems include not only gases, and Chapter 17 looks at other possible systems, such as elastic rods and magnetic systems. The third law of thermodynamics is described in Chapter 18 and provides a deeper understanding of how entropy behaves as the temperature is reduced to absolute zero.

Part VII focuses on statistical mechanics. Following a discussion of the equipartition of energy in Chapter 19, so useful for understanding high temperature limits, the concept of the partition function is presented in some detail in Chapter 20, which is foundational for understanding statistical mechanics. The idea is applied to the ideal gas in Chapter 21. Particle number becomes important when considering different types of particle, so the chemical potential and grand partition function are presented in Chapter 22. Two simple applications where the chemical potential is zero are photons and phonons, discussed in Chapters 23 and 24 respectively.

The discussion up to this point has concentrated on the ideal gas model and we go beyond this in Part VIII: Chapter 25 discusses the effect of relativistic velocities and Chapters 26 and 27 discuss the effect of intermolecular interactions, while phase transitions are discussed in Chapter 28, where the important Clausius-Clapeyron equation for a phase boundary is derived. Another quantum mechanical implication is the existence of identical particles and the difference between fermions and bosons, discussed in Chapter 29; the consequences for the properties of quantum gases are presented in Chapter 30.

===== Page 31 =====

The remainder of the book, Part IX, contains more detailed information on various special topics which allow the power of thermal physics to be demonstrated. In Chapters 31 and 32 we describe sound waves and shock waves in fluids. We draw some of the statistical ideas of the book together in Chapter 33 and discuss non-equilibrium thermodynamics and the arrow of time in Chapter 34. Applications of the concepts in the book to astrophysics are described in Chapters 35 and 36 and to atmospheric physics in Chapter 37.

## Chapter summary

In this chapter, the idea of big numbers has been introduced. These arise in thermal physics for two main reasons:

(1) The number of atoms in a typical macroscopic lump of matter is large. It is measured in the units of the mole. One mole of atoms contains $N_{\mathrm{A}}$ atoms, where $N_{\mathrm{A}} = 6.022\times 10^{23}$
(2) Combinatorial problems generate very large numbers. To make these numbers manageable, we often consider their logarithms and use Stirling's approximation: $\ln n!\approx n\ln n - n$

## Exercises

(1.1) What is the mass of 3 moles of carbon dioxide $\mathrm{CO_2}$? (1 mole of oxygen atoms has a mass of $16\mathrm{g}$.)

(1.2) A typical bacterium has a mass of $10^{-12}\mathrm{g}$. Calculate the mass of a mole of bacteria. (Interestingly, this is about the total number of bacteria living in the guts of all humans resident on planet Earth.) Give your answer in units of elephant-masses (elephants have a mass $\approx 5000\mathrm{kg}$).

(1.3) (a) How many water molecules are there in your body? (Assume that you are nearly all water.)
(b) How many drops of water are there in all the oceans of the world? (The mass of the world's oceans is about $10^{21}\mathrm{kg}$. Estimate the size of a typical drop of water.)
(c) Which of these two numbers from (a) and (b) is the larger?

(1.4) A system contains $n$ atoms, each of which can only have zero or one quanta of energy. How many ways can you arrange $r$ quanta of energy when
(a) $n = 2$, $r = 1$
(b) $n = 20$, $r = 10$
(c) $n = 2\times 10^{23}$, $r = 10^{23}$?

(1.5) What fractional error do you make when using Stirling's approximation (in the form $\ln n!\approx n\ln n - n$) to evaluate
(a) $\ln 10!$
(b) $\ln 100!$
(c) $\ln 1000!$?

(1.6) Show that eqn C.19 is equivalent to writing

$$n!\approx n^{n}\mathrm{e}^{-n}\sqrt{2\pi n}, \quad (1.21)$$

and

$$n!\approx \sqrt{2\pi} n^{n + \frac{1}{2}}\mathrm{e}^{-n}. \quad (1.22)$$

===== Page 32 =====

# 2 Heat

In this chapter, we will introduce the concepts of heat and heat capacity.

## 2.1 A definition of heat

We all have an intuitive notion of what heat is: sitting next to a roaring fire in winter, we feel its heat warming us up, increasing our temperature; lying outside in the sunshine on a warm day, we feel the Sun's heat warming us up. In contrast, holding a snowball, we feel heat leaving our hand and transferring to the snowball, making our hand feel cold. Heat seems to be some sort of energy transferred from hot things to cold things when they come into contact. We therefore make the following definition:

**Heat is thermal energy in transit.**

We now stress a couple of important points about this definition.

(1) Experiments suggest that heat spontaneously transfers from a hotter body to a colder body when they are in contact, and not in the reverse direction. However, there are circumstances when it is possible for heat to go in the reverse direction. A good example of this is a kitchen freezer: you place food, initially at room temperature, into the freezer and shut the door; the freezer then sucks heat out of the food and cools the food down to below freezing point. Heat is being transferred from your warmer food to the colder freezer, apparently in the "wrong" direction. Of course, to achieve this, you have to be paying your electricity bill and therefore be putting energy in to your freezer. If there is a power cut, heat will slowly leak back into the freezer from the warmer kitchen and thaw out all your frozen food. This shows that it is possible to reverse the direction of heat flow, but only if you intervene by putting additional energy in. We will return to this point in Section 13.5 when we consider refrigerators, but for now let us note that we are defining heat as thermal energy in transit and not hard-wiring into the definition anything about which direction it goes.

(2) The "in transit" part of our definition is very important. Though you can add heat to an object, you cannot say that "an object contains a certain quantity of heat." This is very different from the case of the fuel in your car: you can add fuel to your car,

===== Page 33 =====

and you are quite entitled to say that your car "contains a certain quantity of fuel". You even have a gauge for measuring it! But heat is quite different. Objects do not and cannot have gauges which read out how much heat they contain, because heat only makes sense when it is "in transit".

To see this, consider your cold hands on a chilly winter day. You can increase the temperature of your hands in two different ways: (i) by adding heat, for example by putting your hands close to something hot, like a roaring fire; (ii) by rubbing your hands together. In one case you have added heat from the outside, in the other case you have not added any heat but have done some work. In both cases, you end up with the same final situation: hands that have increased in temperature. There is no physical difference between hands that have been warmed by heat and hands that have been warmed by work.

Heat is measured in joules (J). The rate of heating has the units of watts (W), where $1\mathrm{W} = 1\mathrm{J}\mathrm{s}^{-1}$ (i.e., 1 watt = 1 joule per second).

## Example 2.1

A 1 kW electric heater is switched on for ten minutes. How much heat does it produce?

Solution:

Ten minutes equals $600\mathrm{s}$ so the heat $Q$ is given by

$$Q = 1\mathrm{kW}\times 600\mathrm{s} = 600\mathrm{kJ}. \quad (2.1)$$

Notice in this last example that the power in the heater is supplied by electrical work. Thus it is possible to produce heat by doing work. We will return to the question of whether one can produce work from heat in Chapter 13.

## 2.2 Heat capacity

In the previous section, we explained that it is not possible for an object to contain a certain quantity of heat, because heat is defined as "thermal energy in transit". It is therefore with a somewhat heavy heart that we turn to the topic of "heat capacity", since we have argued that objects have no capacity for heat! (This is one of those occasions in physics when decades of use of a name have made it completely standard, even though it is really a misleading name to use.) What we are going to derive in this section might be better termed "energy capacity", but to do this would put us at odds with common usage throughout physics. All of this being said, we can proceed quite legitimately by asking the following simple question:

===== Page 34 =====

How much heat needs to be supplied to an object to raise its temperature by a small amount $\mathrm{d}T$?

The answer to this question is the heat $\mathrm{d}Q = C\mathrm{d}T$, where we define the heat capacity $C$ of an object using

$$C = \frac{\mathrm{d}Q}{\mathrm{d}T}. \quad (2.2)$$

As long as we remember that heat capacity tells us simply how much heat is needed to warm an object (and is nothing about the capacity of an object for heat) we shall be on safe ground. As can be inferred from eqn 2.2, the heat capacity $C$ has units $\mathrm{JK}^{-1}$.

As shown in the following example, although objects have a heat capacity, one can also express the heat capacity of a particular substance per unit mass, or per unit volume.

## Example 2.2

The heat capacity of $0.125\mathrm{kg}$ of water is measured to be $523\mathrm{JK}^{-1}$ at room temperature. Hence calculate the heat capacity of water (a) per unit mass and (b) per unit volume.

Solution:

(a) The heat capacity per unit mass $c$ is given by dividing the heat capacity by the mass, and hence

$$c = \frac{523\mathrm{JK}^{-1}}{0.125\mathrm{kg}} = 4.184\times 10^{3}\mathrm{JK}^{-1}\mathrm{kg}^{-1}. \quad (2.3)$$

(b) The heat capacity per unit volume $C$ is obtained by multiplying the previous answer by the density of water, namely $1000\mathrm{kg}\mathrm{m}^{-3}$, so that

$$C = 4.184\times 10^{3}\mathrm{JK}^{-1}\mathrm{kg}^{-1}\times 1000\mathrm{kg}\mathrm{m}^{-3} = 4.184\times 10^{6}\mathrm{JK}^{-1}\mathrm{m}^{-3}.$$

The heat capacity per unit mass $c$ occurs quite frequently, and it is given a special name: the specific heat capacity.

## Example 2.3

Calculate the specific heat capacity of water.

Solution:

This is given in answer (a) from the previous example: the specific heat capacity of water is $4.184\times 10^{3}\mathrm{JK}^{-1}\mathrm{kg}^{-1}$.

===== Page 35 =====

Also useful is the molar heat capacity, which is the heat capacity of one mole of the substance.

## Example 2.4

Calculate the molar heat capacity of water. (The molar mass of water is $18\mathrm{g}$.)

Solution:

The molar heat capacity is obtained by multiplying the specific heat capacity by the molar mass, and hence

$$C = 4.184\times 10^{3}\mathrm{J}\mathrm{K}^{-1}\mathrm{kg}^{-1}\times 0.018\mathrm{kg} = 75.2\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}. \quad (2.5)$$

[Image: Two diagrams (a) and (b) showing a gas being heated. (a) shows a gas in a sealed rigid container, with heat entering from below. (b) shows a gas in a container with a movable piston, with heat entering from below.]
**Fig. 2.1** Two methods of heating a gas: (a) constant volume, (b) constant pressure.

When we think about the heat capacity of a gas, there is a further complication. We are trying to ask the question: how much heat should you add to raise the temperature of our gas by one kelvin? But we can imagine doing the experiment in two ways (see also Fig. 2.1):

(1) Place our gas in a sealed box and add heat (Fig. 2.1(a)). As the temperature rises, the gas will not be allowed to expand because its volume is fixed, so its pressure will increase. This method is known as heating at constant volume.
(2) Place our gas in a chamber connected to a piston and heat it (Fig. 2.1(b)). The piston is well lubricated, and so will slide in and out to maintain the pressure in the chamber to be identical to that in the lab. As the temperature rises, the piston is forced out (doing work against the atmosphere) and the gas is allowed to expand, keeping its pressure constant. This method is known as heating at constant pressure.

In both cases, we are applying a constraint to the system, either constraining the volume of the gas to be fixed, or constraining the pressure of the gas to be fixed. We need to modify our definition of heat capacity given in eqn 2.2, and hence we define two new quantities: $C_V$ is the heat capacity at constant volume and $C_p$ is the heat capacity at constant pressure. We can write them using partial differentials as follows:

$$C_V = \left(\frac{\partial Q}{\partial T}\right)_V, \quad C_p = \left(\frac{\partial Q}{\partial T}\right)_p. \quad (2.6)$$

We expect that $C_p$ will be bigger than $C_V$ for the simple reason that more heat will need to be added when heating at constant pressure than when heating at constant volume. This is because in the latter case additional energy will be expended on doing work on the atmosphere as the gas expands. It turns out that indeed $C_p$ is bigger than $C_V$ in practice.

===== Page 36 =====

## Example 2.5

The specific heat capacity of helium gas is measured to be $3.12\mathrm{kJ}\mathrm{K}^{-1}\mathrm{kg}^{-1}$ at constant volume and $5.19\mathrm{kJ}\mathrm{K}^{-1}\mathrm{kg}^{-1}$ at constant pressure. Calculate the molar heat capacities. (The molar mass of helium is $4\mathrm{g}$.)

Solution:

The molar heat capacity is obtained by multiplying the specific heat capacity by the molar mass, and hence

$$C_V = 12.48\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}, \quad C_p = 20.76\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}. \quad (2.9)$$

(Interestingly, these answers are almost exactly $\frac{3}{2} R$ and $\frac{5}{2} R$ where $R$ is the gas constant. We will see why in Section 11.3.)

## Chapter summary

In this chapter, the concepts of heat and heat capacity have been introduced. Heat is "thermal energy in transit". The heat capacity $C$ of an object is given by $C = \mathrm{d}Q / \mathrm{d}T$. The heat capacity of a substance can also be expressed per unit volume or per unit mass (in the latter case it is called specific heat capacity).

## Exercises

(2.1) Using data from this chapter, estimate the energy needed to (a) boil enough tap water to make a cup of tea, (b) heat the water for a bath.

(2.2) The world's oceans contain approximately $10^{21}\mathrm{kg}$ of water. Estimate the total heat capacity of the world's oceans.

(2.3) The world's power consumption is currently about $13\mathrm{TW}$ and growing! ($\mathrm{1TW = 10^{12}W}$) Burning one ton of crude oil (which is nearly seven barrels worth) produces about $42\mathrm{GJ}$ ($\mathrm{1GJ = 10^{9}J}$). If the world's total power needs were to come from burning oil (a large fraction currently does), how much oil would we be burning per second?

(2.4) The molar heat capacity of gold is $25.4\mathrm{J}\mathrm{mol}^{-1}\mathrm{K}^{-1}$. Its density is $19.3\times 10^{3}\mathrm{kg}\mathrm{m}^{-3}$. Calculate the specific heat capacity of gold and the heat capacity per unit volume. What is the heat capacity of $4\times 10^{6}\mathrm{kg}$ of gold? (This is roughly the holdings of Fort Knox.)

(2.5) Two bodies, with heat capacities $C_1$ and $C_2$ (assumed independent of temperature) and initial temperatures $T_{1}$ and $T_{2}$ respectively, are placed in thermal contact. Show that their final temperature $T_{\mathrm{f}}$ is given by $T_{\mathrm{f}} = (C_{1}T_{1} + C_{2}T_{2}) / (C_{1} + C_{2})$. If $C_1$ is much larger than $C_2$, show that $T_{\mathrm{f}}\approx T_{1} + C_{2}(T_{2} - T_{1}) / C_{1}$.

===== Page 37 =====

# 3 Probability

3.1 Discrete probability distributions  19
3.2 Continuous probability distributions  20
3.3 Linear transformation  21
3.4 Variance  22
3.5 Linear transformation and the variance  23
3.6 Independent variables  24
3.7 Binomial distribution  26
Chapter summary  28
Further reading  29
Exercises  29

Life is full of uncertainties, and has to be lived according to our best guesses based on the information available to us. This is because the chain of events that lead to various outcomes can be so complex that the exact outcomes are unpredictable. Nevertheless, things can still be said even in an uncertain world: for example, it is more helpful to know that there is a $20\%$ chance of rain tomorrow than that the weather forecaster has absolutely no idea; or worse still that he or she claims that there will definitely be no rain, when there might be! Probability is therefore an enormously useful and powerful subject, since it can be used to quantify uncertainty.

The foundations of probability theory were laid by the French mathematicians Pierre de Fermat (1601-1665) and Blaise Pascal (1623-1662), through their correspondence in 1654, which originated from a problem set to them by a gentleman gambler. The ideas proved to be intellectually infectious and the first probability textbook was written by the Dutch physicist Christian Huygens (1629-1695) in 1657, who applied it to the working out of life expectancy. Probability was thought to be useful only for determining possible outcomes in situations in which we lacked complete knowledge. The supposition was that if we could know the motions of all particles at the microscopic level, we could determine every outcome precisely. In the twentieth century, the discovery of quantum theory has led to the understanding that, at the microscopic level, outcomes are purely probabilistic.

Probability has had a huge impact on thermal physics. This is because we are often interested in systems containing huge numbers of particles, so that predictions based on probability turn out to be precise enough for most purposes. In a thermal physics problem, one is often interested in the values of quantities that are the sum of many small contributions from individual atoms. Though each atom behaves differently, the average behaviour is what comes through, and therefore it becomes necessary to be able to extract average values from probability distributions.

In this chapter, we will define some basic concepts in probability theory. Let us begin by stating that the probability of occurrence of a particular event, taken from a finite set of possible events, is zero if that event is impossible, is one if that event is certain, and takes a value somewhere in between zero and one if that event is possible but not certain. We begin by considering two different types of probability distribution: discrete and continuous.

===== Page 38 =====

## 3.1 Discrete probability distributions

Discrete random variables can only take a finite number of values. Examples include the number obtained when throwing a die (1, 2, 3, 4, 5, or 6), the number of children in each family (0, 1, 2, ...), and the number of people killed per year in the UK in bizarre gardening accidents (0, 1, 2, ...). Let $x$ be a discrete random variable which takes values $x_{i}$ with probability $P_{i}$. We require that the sum of the probabilities of every possible outcome adds up to one. This may be written

$$\sum_{i}P_{i} = 1. \quad (3.1)$$

We define the mean (or average or expected value) of $x$ to be

$$\langle x\rangle = \sum_{i}x_{i}P_{i}. \quad (3.2)$$

The idea is that you weight by its probability each value taken by the random variable $x$.

Alternative notations for the mean of $x$ include $\bar{x}$ and $E(x)$. We prefer the one given in the main text since it is easier to distinguish quantities such as $\langle x^{2}\rangle$ and $\langle x\rangle^{2}$ with this notation, particularly when writing quickly.

## Example 3.1

Note that the mean, $\langle x\rangle$, may be a value that $x$ cannot actually take. A common example of this is the number of children in families, which is often quoted as 2.4. Any individual couple can only have an integer number of children. Thus the expected value of $x$ is actually an impossibility!

It is also possible to define the mean squared value of $x$ using

$$\langle x^{2}\rangle = \sum_{i}x_{i}^{2}P_{i}. \quad (3.3)$$

In fact, any function of $x$ can be averaged, using (by analogy)

$$\langle f(x)\rangle = \sum_{i}f(x_{i})P_{i}. \quad (3.4)$$

Now let us actually evaluate the mean of $x$ for a particular discrete distribution.

[Image: A bar chart showing a discrete probability distribution P(x) for x = 0, 1, 2. The bar at x=0 has height 1/2, at x=1 has height 1/4, and at x=2 has height 1/4.]
**Fig. 3.1** An example of a discrete probability distribution.

## Example 3.2

Let $x$ take values 0, 1, and 2 with probabilities $\frac{1}{2}, \frac{1}{4}$, and $\frac{1}{4}$ respectively. This distribution is shown in Fig. 3.1. Calculate $\langle x \rangle$ and $\langle x^{2} \rangle$.

===== Page 39 =====

Solution:

First check that $\sum P_{i} = 1$. Since $\frac{1}{2} +\frac{1}{4} +\frac{1}{4} = 1$, this is fine. Now we can calculate the averages as follows:

$$\begin{array}{rcl}{\langle x\rangle} & = & {\sum_{i}x_{i}P_{i}}\\ {} & {} & {}\\ {} & = & {0\cdot \frac{1}{2} +1\cdot \frac{1}{4} +2\cdot \frac{1}{4}}\\ {} & = & {\frac{3}{4}.} \end{array} \quad (3.5)$$

Again, we find that the mean $\langle x \rangle$ is not actually one of the possible values of $x$. We can now calculate the value of $\langle x^{2} \rangle$ as follows:

$$\begin{array}{rcl}{\langle x^2\rangle} & = & {\sum_i x_i^2 P_i}\\ {} & {} & {}\\ {} & = & {0\cdot \frac{1}{2} +1\cdot \frac{1}{4} +4\cdot \frac{1}{4}}\\ {} & = & {\frac{5}{4}.} \end{array} \quad (3.6)$$

## 3.2 Continuous probability distributions

For a continuous random variable, there are an infinite number of possible values it can take, so the probability of any one of them occurring is zero! Hence we talk about the probability of the variable lying in some range, such as "between $x$ and $x + \mathrm{d}x$"

Let $x$ now be a continuous random variable which has a probability $P(x) \mathrm{d}x$ of having a value between $x$ and $x + \mathrm{d}x$. Continuous random variables can take a range of possible values. Examples include the height of children in a class, the length of time spent in a waiting room, and the amount a person's blood pressure increases when reading their mobile-phone bill. These quantities are not restricted to any finite set of values, but can take a continuous set of values.

As before, we require that the total probability of all possible outcomes is one. Because we are dealing with continuous distributions, the sums become integrals, and we have

$$\int P(x)\mathrm{d}x = 1. \quad (3.7)$$

The mean is defined as

$$\langle x\rangle = \int x P(x)\mathrm{d}x. \quad (3.8)$$

Similarly, the mean square value is defined as

$$\langle x^2\rangle = \int x^2 P(x)\mathrm{d}x, \quad (3.9)$$

and the mean of any function of $x$, $f(x)$, can be defined as

$$\langle f(x)\rangle = \int f(x)P(x)\mathrm{d}x. \quad (3.10)$$

===== Page 40 =====

## Example 3.3

Let $P(x) = C\mathrm{e}^{- x^{2} / 2a^{2}}$ where $C$ and $a$ are constants. This probability is illustrated in Fig. 3.2 and this curve is known as a Gaussian. Calculate $\langle x\rangle$ and $\langle x^{2}\rangle$ given this probability distribution.

Solution:

The first thing to do is to normalize the probability distribution (i.e., to ensure that the sum over all probabilities is one). This allows us to find the constant $C$ using eqn C.3 to evaluate the integral:

$$\begin{array}{rcl}{1 = \int_{-\infty}^{\infty}P(x)\mathrm{d}x} & = & {C\int_{-\infty}^{\infty}\mathrm{e}^{-x^{2} / 2a^{2}}\mathrm{d}x}\\ {} & = & {C\sqrt{2\pi a^{2}},} \end{array} \quad (3.11)$$

so we find that $C = 1 / \sqrt{2\pi a^{2}}$, which gives

$$P(x) = \frac{1}{\sqrt{2\pi a^{2}}}\mathrm{e}^{-x^{2} / 2a^{2}}. \quad (3.12)$$

The mean of $x$ can then be evaluated using

$$\begin{array}{rcl}{\langle x\rangle} & = & {\frac{1}{\sqrt{2\pi a^{2}}}\int_{-\infty}^{\infty}x\mathrm{e}^{-x^{2} / 2a^{2}}\mathrm{d}x}\\ {} & = & {0,} \end{array} \quad (3.13)$$

because the integrand is an odd function. The mean of $x^{2}$ can also be evaluated as follows:

$$\begin{array}{rcl}{\langle x^2\rangle} & = & {\frac{1}{\sqrt{2\pi a^2}}\int_{-\infty}^{\infty}x^2\mathrm{e}^{-x^2 / 2a^2}\mathrm{d}x}\\ {} & = & {\frac{1}{\sqrt{2\pi a^2}}\frac{1}{2}\sqrt{8\pi a^6}}\\ {} & = & {a^2,} \end{array} \quad (3.14)$$

where the integrals are performed as described in Appendix C.2.

[Image: A bell-shaped curve representing a continuous probability distribution P(x) centered at x=0.]
**Fig. 3.2** An example continuous probability distribution.

## 3.3 Linear transformation

Sometimes one has a random variable, and one wants to make a second random variable by performing a linear transformation on the first one. If $y$ is a random variable, which is related to the random variable $x$ by the equation

$$y = ax + b, \quad (3.15)$$

where $a$ and $b$ are constants, then the average value of $y$ is given by

$$\langle y\rangle = \langle ax + b\rangle = a\langle x\rangle +b. \quad (3.16)$$

The proof of this result is straightforward and is left as an exercise.

===== Page 41 =====

## 3.4 Variance

We now know how to calculate the average of a set of values, but what about the spread in the values? The first idea one might have to quantify the spread of values in a distribution is to consider the deviation from the mean for a particular value of $x$. This is defined by

$$x - \langle x\rangle . \quad (3.17)$$

This quantity tells you by how much a particular value is above or below the mean value. We can work out the average of the deviation (averaging over all values of $x$) as follows:

$$\langle x - \langle x\rangle \rangle = \langle x\rangle -\langle x\rangle = 0, \quad (3.18)$$

which follows from the equation for linear transformation (eqn 3.16). Thus the average deviation is not going to be a very helpful indicator! Of course, the problem is that the deviation is sometimes positive and sometimes negative, and the positive and negative deviations cancel out. A more useful quantity would be the modulus of the deviation,

$$|x - \langle x\rangle |, \quad (3.19)$$

which is always positive, but this will suffer from the disadvantage that modulus signs in algebra can be both confusing and tedious. Therefore, another approach is to use a different quantity which is always positive, the square of the deviation, $(x - \langle x\rangle)^2$. This quantity is what we need: always positive and easy to manipulate algebraically. Hence, its average is given a special name, the variance. Consequently the variance of $x$, written as $\sigma_{x}^{2}$, is defined as the mean squared deviation:

$$\sigma_{x}^{2} = \langle (x - \langle x\rangle)^{2}\rangle . \quad (3.20)$$

We will call $\sigma_{x}$ the standard deviation, and it is defined as the square root of the variance:

$$\sigma_{x} = \sqrt{\langle(x - \langle x\rangle)^{2}\rangle}. \quad (3.21)$$

===== Page 42 =====

The standard deviation represents the "root mean square" (known as the "rms") scatter or spread in the data.

The following identity is extremely useful:

$$\begin{array}{rcl}{\sigma_x^2} & = & {\langle (x - \langle x\rangle)^2\rangle}\\ {} & = & {\langle x^2 -2x\langle x\rangle +\langle x\rangle^2\rangle}\\ {} & = & {\langle x^2\rangle -2\langle x\rangle \langle x\rangle +\langle x\rangle^2}\\ {} & = & {\langle x^2\rangle -\langle x\rangle^2.} \end{array} \quad (3.22)$$

## Example 3.5

For Examples 3.2 and 3.3 above, work out $\sigma_{x}^{2}$, the variance of the distribution, in each case.

Solution:

For Example 3.2

$$\sigma_{x}^{2} = \langle x^{2}\rangle -\langle x\rangle^{2} = \frac{5}{4} -\frac{9}{16} = \frac{11}{16}. \quad (3.23)$$

For Example 3.3

$$\sigma_{x}^{2} = \langle x^{2}\rangle -\langle x\rangle^{2} = a^{2} - 0 = a^{2}. \quad (3.24)$$

## 3.5 Linear transformation and the variance

We return to the problem of a linear transformation of a random variable. What happens to the variance in this case?

If $y$ is a random variable which is related to the random variable $x$ by the equation

$$y = ax + b, \quad (3.25)$$

where $a$ and $b$ are constants, then we have seen that

$$\langle y\rangle = \langle ax + b\rangle = a\langle x\rangle +b. \quad (3.26)$$

Hence, we can work out $\langle y^{2}\rangle$, which is

$$\begin{array}{rcl}{\langle y^2\rangle} & = & {\langle (ax + b)^2\rangle}\\ {} & = & {\langle a^2 x^2 +2abx + b^2\rangle}\\ {} & = & {a^2 \langle x^2\rangle +2ab\langle x\rangle +b^2.} \end{array} \quad (3.27)$$

Also, we can work out $\langle y\rangle^{2}$, which is

$$\langle y\rangle^{2} = (a\langle x\rangle +b)^{2} = a^{2}\langle x\rangle^{2} + 2ab\langle x\rangle +b^{2}. \quad (3.28)$$

===== Page 43 =====

Hence, using eqn 3.22, the variance in $y$ is given by eqn 3.27 minus eqn 3.28, i.e.

$$\begin{array}{rcl}{\sigma_y^2} & = & {\langle y^2\rangle -\langle y\rangle^2}\\ {} & = & {a^2\langle x^2\rangle -a^2\langle x\rangle^2}\\ {} & = & {a^2\sigma_x^2.} \end{array} \quad (3.29)$$

Notice that the variance depends on $a$ but not on $b$. This makes sense because the variance tells us about the width of a distribution, and nothing about its absolute position. The standard deviation of $y$ is therefore given by

$$\sigma_{y} = a\sigma_{x}. \quad (3.30)$$

## Example 3.6

The average temperature in a town in the USA in January is $23^{\circ}\mathrm{F}$ and the standard deviation is $9^{\circ}\mathrm{F}$. Convert these figures into degrees Celsius using the relation in Example 3.4.

Solution:

The average temperature in degrees Celsius is given by

$$\langle C\rangle = \frac{5}{9} (\langle F\rangle -32) = \frac{5}{9} (23 - 32) = -5^{\circ}\mathrm{C}, \quad (3.31)$$

and the standard deviation is given by $\frac{5}{9}\times 9 = 5^{\circ}\mathrm{C}$

## 3.6 Independent variables

Two random variables are independent if knowing the value of one of them yields no information about the value of the other. For example, the height of a person chosen at random from a city and the number of hours of rainfall in that city on the first Tuesday of September are two independent random variables.

If $u$ and $v$ are independent random variables the probability that $u$ is in the range from $u$ to $u + \mathrm{d}u$ and $v$ is in the range from $v$ to $v + \mathrm{d}v$ is given by the product

$$P_{u}(u)\mathrm{d}u P_{v}(v)\mathrm{d}v. \quad (3.32)$$

Hence, the average value of the product of $u$ and $v$ is

$$\begin{array}{rcl}{\langle u v\rangle} & = & {\iint u v P_{u}(u)P_{v}(v)\mathrm{d}u\mathrm{d}v}\\ {} & = & {\int u P_{u}(u)\mathrm{d}u\int v P_{v}(v)\mathrm{d}v}\\ {} & = & {\langle u\rangle \langle v\rangle ,} \end{array} \quad (3.33)$$

because the integrals separate for independent random variables. This implies that the average value of the product of $u$ and $v$ is equal to the product of their average values.

===== Page 44 =====

## Example 3.7

Suppose that there are $n$ independent random variables, $X_{i}$, each with the same mean $\langle X\rangle$ and variance $\sigma_{X}^{2}$. Let $Y$ be the sum of the random variables, so that $Y = X_{1} + X_{2} + \dots +X_{n}$. Find the mean and variance of $Y$.

Solution:

The mean of $Y$ is simply

$$\langle Y\rangle = \langle X_1\rangle +\langle X_2\rangle +\dots +\langle X_n\rangle , \quad (3.34)$$

but since all the $X_{i}$ have the same mean $\langle X\rangle$ this can be written

$$\langle Y\rangle = n\langle X\rangle . \quad (3.35)$$

Hence the mean of $Y$ is $n$ times the mean of the $X_{i}$. To find the variance of $Y$, we can use the formula

$$\sigma_{Y}^{2} = \langle Y^{2}\rangle -\langle Y\rangle^{2}. \quad (3.36)$$

Hence

$$\begin{array}{rcl}{\langle Y^2\rangle} & = & {\langle X_1^2 +\dots +X_N^2 +X_1X_2 + X_2X_1 + X_1X_3 + \dots \rangle}\\ {} & = & {\langle X_1^2\rangle +\dots +\langle X_N^2\rangle +\langle X_1X_2\rangle +\langle X_2X_1\rangle +\langle X_1X_3\rangle +\dots} \end{array} \quad (3.37)$$

There are $n$ terms like $\langle X_{1}^{2}\rangle$ on the right-hand side, and $n(n - 1)$ terms like $\langle X_{1}X_{2}\rangle$. The former terms take the value $\langle X^{2}\rangle$ and the latter terms (because they are the product of two independent random variables) take the value $\langle X\rangle \langle X\rangle = \langle X\rangle^{2}$. Hence, using eqn 3.35,

$$\langle Y^2\rangle = n\langle X^2\rangle +n(n - 1)\langle X\rangle^2, \quad (3.38)$$

so that

$$\begin{array}{rcl}{\sigma_Y^2} & = & {\langle Y^2\rangle -\langle Y\rangle^2}\\ {} & = & {n\langle X^2\rangle -n\langle X\rangle^2}\\ {} & = & {n\sigma_X^2.} \end{array} \quad (3.39)$$

The results proved in this last example have some interesting applications. The first concerns experimental measurements. Imagine that a quantity $X$ is measured $n$ times, each time with an independent error, which we call $\sigma_{X}$. If you add up the results of the measurements to make $Y = \sum X_{i}$, then the rms error in $Y$ is only $\sqrt{n}$ times the rms error of a single $X$. Hence if you try and get a good estimate of $X$ by calculating $(\sum X_{i}) / n$, the error in this quantity is equal to $\sigma_{X} / \sqrt{n}$. Thus, for example, if you make four measurements of a quantity and average your results, the random error in your average is half of what it

===== Page 45 =====

would be if you'd just taken a single measurement. Of course, you may still have systematic errors in your experiment. If you are consistently overestimating your quantity by an error in your experimental setup, that error won't reduce by repeated measurement!

A second application is in the theory of random walks. Imagine a drunken person staggering out of a pub and attempting to walk along a narrow street (which confines him or her to motion in one dimension). Let's pretend that with each inebriated step, the drunken person is equally likely to travel one step forwards or one step backwards. The effects of intoxication are such that each step is uncorrelated with the previous one. Thus the average distance travelled in a single step is $\langle X \rangle = 0$. After $n$ such steps, we would have an expected total distance travelled of $\langle Y \rangle = \sum \langle X_i \rangle = 0$. However, in this case the root mean squared distance is more revealing. In this case $\langle Y^2 \rangle = n \langle X^2 \rangle$, so that the rms length of a random walk of $n$ steps is $\sqrt{n}$ times the length of a single step. This result will be useful in considering Brownian motion in Chapter 33.

## 3.7 Binomial distribution

A probability distribution, which is very important in thermal physics, is based on what is called a Bernoulli trial, an "experiment" with two possible outcomes. One outcome (which we will call "success") occurs with probability $p$ and the other outcome (which we will call "failure") occurs with probability $1 - p$. An example of a Bernoulli trial is the tossing of a coin: one outcome is "heads", the other is "tails".

## Example 3.8

Let $x$ be a random variable which takes the value 1 for success and 0 for failure. Then, assuming $p$ to be the probability of success and using eqns 3.2, 3.3 and 3.21

$$\begin{array}{rcl}\langle x\rangle & = & 0\times (1 - p) + 1\times p = p\\ \langle x^2\rangle & = & 0^2\times (1 - p) + 1^2\times p = p\\ \sigma_x & = & \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{p(1 - p)}. \end{array} \quad (3.42)$$

The binomial distribution is the discrete probability distribution $P(n,k)$ of getting $k$ successes from $n$ independent Bernoulli trials. The function $P(n,k)$ can be worked out by realizing that (a) the probability of a particular series of $k$ successes and $n - k$ failures is $p^k (1 - p)^{n - k}$ and (b) that there are ${}^{n}C_{k}$ ways of arranging $k$ successes and $n - k$ failures in a sequence. Thus $P(n,k)$ is a product of these factors and hence

$$P(n,k) = {}^{n}C_{k}p^{k}(1 - p)^{n - k}. \quad (3.43)$$

===== Page 46 =====

The binomial theorem of elementary algebra states that

$$(x + y)^n = \sum_{k = 0}^{n}{}^{n}C_{k}x^k y^{n - k}. \quad (3.44)$$

Hence by writing $x = p$ and $y = 1 - p$ we can easily show that

$$\sum_{k = 1}^{n}P(n,k) = 1, \quad (3.45)$$

as required for a well-behaved probability distribution. Since the binomial distribution is the sum of $n$ independent Bernoulli trials, then

$$\begin{array}{rcl}{\langle k\rangle} & = & {np}\\ {\sigma_k^2} & = & {np(1 - p).} \end{array} \quad (3.47)$$

The fractional width of the distribution is obtained by dividing the standard deviation by the mean and is given by $\sigma_k / \langle k \rangle = \sqrt{(1 - p) / np}$, which is proportional to $1 / \sqrt{n}$, and therefore decreases as $n$ increases. This causes the binomial distribution to become more sharply peaked near the mean value as $n$ increases, as shown in Fig. 3.3.

[Image: Graph showing three binomial probability distributions for p=0.4, plotted as P(n,k)/max(P(n,k)) versus k/n. The curves are for n=50 (broadest), n=500, and n=5000 (narrowest).]
**Fig. 3.3** Binomial probability for $p = 0.4$. The three plots are for $n = 50$ (outermost), $n = 500$ and $n = 5000$ (innermost) and are scaled so that their maximum amplitudes are the same. This demonstrates that as $n$ increases, the fractional width decreases.

## Example 3.9

Coin tossing with a fair coin. In this case, $p = \frac{1}{2}$.

For $n = 16$ tosses, the expected number of heads is $np = 8$. The standard deviation is $\sqrt{np(1 - p)} = 2$, a quarter of the expected number. For $n = 10^{20}$ tosses, the expected number of heads is $np = 5 \times 10^{19}$. The standard deviation is $\sqrt{np(1 - p)} = 5 \times 10^{9}$, ten orders of magnitude smaller than the expected number.

===== Page 47 =====

## Example 3.10

A one-dimensional random walk can be considered as a succession of $n$ Bernoulli trials in which the choice is either a step forwards $+L$ or a step backwards $-L$, each with equal probability (so $p = \frac{1}{2}$). If there are $n$ steps, $k$ of which are forwards, the distance travelled is $x = kL - (n - k)L = (2k - n)L$. For a binomial distribution with $p = \frac{1}{2}$, $\langle k \rangle = \frac{n}{2}$, and $\sigma_k^2 = \langle k^2 \rangle - \langle k \rangle^2 = np(1 - p) = \frac{n}{4}$. This implies that $\langle k^2 \rangle = \frac{n}{4} + \frac{n^2}{4}$. Hence, the mean distance travelled is

$$\langle x\rangle = (2\langle k\rangle -n)L = 0, \quad (3.48)$$

as expected, since the random walker is just as likely to travel forwards as backwards. The mean squared distance travelled, $\langle x^2 \rangle$, is

$$\langle x^2 \rangle = (4\langle k^2 \rangle - 4\langle k \rangle n + n^2)L^2 = nL^2, \quad (3.49)$$

and hence $\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \sqrt{n} L$, in agreement with Section 3.6.

## Chapter summary

In this chapter, several introductory concepts in probability theory have been introduced.

The mean of a discrete probability distribution is given by

$$\langle x\rangle = \sum_{i}x_{i}P_{i},$$

and the mean of a continuous probability distribution is given by

$$\langle x\rangle = \int x P(x)\mathrm{d}x.$$

The variance is given by

$$\sigma_x^2 = \langle (x - \langle x \rangle)^2 \rangle ,$$

where $\sigma_x$ is the standard deviation.

If $y = ax + b$, then $\langle y \rangle = a\langle x \rangle + b$ and $\sigma_y = a\sigma_x$.

If $u$ and $v$ are independent random variables, then $\langle uv \rangle = \langle u \rangle \langle v \rangle$. In particular, if $Y = X_1 + X_2 + \dots + X_n$, where the $X_i$ are all from the same distribution, $\langle Y \rangle = n\langle x \rangle$ and $\sigma_Y = \sqrt{n} \sigma_X$.

The binomial distribution describes the probability of getting $k$ successes from $n$ independent Bernoulli trials. The mean of this distribution is $\langle k \rangle = np$ and the variance is $\sigma_k^2 = np(1 - p)$.

[Image: A portrait of Ludwig Boltzmann, a man with a full beard and glasses.]
**Fig. 3.4** Ludwig Boltzmann

## Further reading

There are many good books on probability theory and statistics. Recommended ones include Papoulis (1984), Saha (2003), Wall and Jenkins (2003), and Sivia and Skilling (2006).

## Exercises

(3.1) A throw of a regular die yields the numbers 1, 2, ..., 6, each with probability $1 / 6$. Find the mean, variance, and standard deviation of the numbers obtained.

(3.2) The mean birth-weight of babies in the UK is about $3.2\mathrm{kg}$ with a standard deviation of $0.5\mathrm{kg}$. Convert these figures into pounds (lb), given that $1\mathrm{kg} = 2.2\mathrm{lb}$.

(3.3) This question is about a discrete probability distribution known as the Poisson distribution. Let $x$ be a discrete random variable that can take the values $0,1,2,\ldots$ A quantity $x$ is said to be Poisson distributed if the probability $P(x)$ of obtaining $x$ is

$$P(x) = \frac{\mathrm{e}^{-m}m^x}{x!},$$

where $m$ is a particular number (which we will show in part (b) of this exercise is the mean value of $x$).

(a) Show that $P(x)$ is a well-behaved probability distribution in the sense that

$$\sum_{x = 0}^{\infty}P(x) = 1.$$

(Why is this condition important?)

(b) Show that the mean value of the probability distribution is $\langle x\rangle = \sum_{x = 0}^{\infty}xP(x) = m$.

(c) The Poisson distribution is useful for describing very rare events, which occur independently and whose average rate does not change over the period of interest. Examples include birth defects measured per year, traffic accidents at a particular junction per year, numbers of typographical errors on a page, and the number of activations of a Geiger counter per minute. The first recorded example of a Poisson distribution, the one which in fact motivated Poisson, was connected with the rare event of someone being kicked to death by a horse in the Prussian army. The number of horse-kick deaths of Prussian military personnel was recorded for each of 10 corps in each of 20 years from 1875-1894 and the following data recorded:

| Number of deaths per year, per corps | Observed frequency |
| :--- | :--- |
| 0 | 109 |
| 1 | 65 |
| 2 | 22 |
| 3 | 3 |
| 4 | 1 |
| ≥ 5 | 0 |
| Total | 200 |

Calculate the mean number of deaths per year per corps. Compare the observed frequency with a calculated frequency assuming the number of deaths per year per corps are Poisson distributed with this mean.

===== Page 47 =====

# Part II

## Kinetic theory of gases

In the second part of this book, we apply the results of Part I to the properties of gases. This is the kinetic theory of gases, in which it is the motion of individual gas atoms, behaving according to the Boltzmann distribution, that determines quantities such as the pressure of a gas, or the rate of effusion. This part is structured as follows:

In Chapter 5, we show that the Boltzmann distribution applied to gases gives rise to a speed distribution known as the Maxwell-Boltzmann distribution. We show how this can be measured experimentally. A treatment of pressure in Chapter 6 using the results so far developed allows us to derive Boyle's law and the ideal gas law. We are then able to treat the effusion of gases through small holes in Chapter 7, which also introduces the concept of flux. Chapter 8 considers the nature of molecular collisions and introduces the concepts of the mean scattering time, the collision cross-section and the mean free path.

===== Page 48 =====

# 5 The Maxwell-Boltzmann distribution

5.1 The velocity distribution  48
5.2 The speed distribution  49
5.3 Experimental justification  51
Chapter summary  54
Exercises  54

In this chapter we will apply the results of the Boltzmann distribution (eqn 4.13) to the problem of the motion of molecules in a gas. For the present, we will neglect any rotational or vibrational motion of the molecules and consider only translational motion (so these results are strictly applicable only to a monatomic gas). In this case the energy of a molecule is given by

$$\frac{1}{2} mv_{x}^{2} + \frac{1}{2} mv_{y}^{2} + \frac{1}{2} mv_{z}^{2} = \frac{1}{2} mv^{2}, \quad (5.1)$$

[Image: A 3D plot of velocity space with axes vx, vy, vz. A vector v is shown from the origin.]
**Fig. 5.1** The velocity of a molecule is shown as a vector in velocity space.

where $\mathbf{v} = (v_{x},v_{y},v_{z})$ is the molecular velocity, and $v = |\mathbf{v}|$ is the molecular speed. This molecular velocity can be represented in velocity space (see Fig. 5.1). The aim is to determine the distribution of molecular velocities and to determine the distribution of molecular speeds. This we will do in the next two sections. To make some progress, we will make a couple of assumptions: first, that the molecular size is much less than the intermolecular separation, so that we assume that molecules spend most of their time whizzing around and only rarely bumping into each other; second, we will ignore any intermolecular forces. Molecules can exchange energy with each other due to collisions, but everything remains in equilibrium. Each molecule therefore behaves like a small system connected to a heat reservoir at temperature $T$, where the heat reservoir is "all the other molecules in the gas". Hence the results of the Boltzmann distribution of energies (described in the previous chapter) will hold.

## 5.1 The velocity distribution

To work out the velocity distribution of molecules in a gas, we must first choose a given direction and see how many molecules have particular components of velocity along it. We define the velocity distribution function as the fraction of molecules with velocities in, say, the $x$-direction, between $v_{x}$ and $v_{x} + \mathrm{d}v_{x}$, as $g(v_{x})\mathrm{d}v_{x}$. The velocity distribution function is proportional to a Boltzmann factor, namely e to the power of the relevant energy, in this case $\frac{1}{2} mv_{x}^{2}$, divided by $k_{\mathrm{B}}T$. Hence

$$g(v_x)\propto \mathrm{e}^{-mv_x^2 /2k_{\mathrm{B}}T}. \quad (5.2)$$

===== Page 49 =====

This velocity distribution function is sketched in Fig. 5.2. To normalize this function, so that $\int_{-\infty}^{\infty}g(v_{x})\mathrm{d}v_{x} = 1$, we need to evaluate the integral

$$\int_{-\infty}^{\infty}\mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}\mathrm{d}v_{x} = \sqrt{\frac{\pi}{m / 2k_{\mathrm{B}}T}} = \sqrt{\frac{2\pi k_{\mathrm{B}}T}{m}}, \quad (5.3)$$

so that

$$g(v_{x}) = \sqrt{\frac{m}{2\pi k_{\mathrm{B}}T}}\mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}. \quad (5.4)$$

It is then possible to find the following expected values of this distribution (using the integrals in Appendix C.2):

$$\begin{array}{rcl}{\langle v_x\rangle} & = & {\int_{-\infty}^{\infty}v_xg(v_x)\mathrm{d}v_x = 0,}\\ {\langle |v_x|\rangle} & = & {2\int_0^\infty v_xg(v_x)\mathrm{d}v_x = \sqrt{\frac{2k_{\mathrm{B}}T}{\pi m}},}\\ {\langle v_x^2\rangle} & = & {\int_{-\infty}^\infty v_x^2 g(v_x)\mathrm{d}v_x = \frac{k_{\mathrm{B}}T}{m}.} \end{array} \quad (5.6)$$

Of course, it does not matter which component of the velocity was initially chosen. Identical results would have been obtained for $v_{y}$ and $v_{z}$. Hence the fraction of molecules with velocities between $(v_{x},v_{y},v_{z})$ and $(v_{x} + \mathrm{d}v_{x},v_{y} + \mathrm{d}v_{y},v_{z} + \mathrm{d}v_{z})$ is given by

$$\begin{array}{rcl}{g(v_x)\mathrm{d}v_xg(v_y)\mathrm{d}v_yg(v_z)\mathrm{d}v_z}\\ & & {\propto \mathrm{e}^{-mv_x^2 /2k_{\mathrm{B}}T}\mathrm{d}v_x\mathrm{e}^{-mv_y^2 /2k_{\mathrm{B}}T}\mathrm{d}v_y\mathrm{e}^{-mv_z^2 /2k_{\mathrm{B}}T}\mathrm{d}v_z}\\ & = & {\mathrm{e}^{-mv_z^2 /2k_{\mathrm{B}}T}\mathrm{d}v_x\mathrm{d}v_y\mathrm{d}v_z.} \end{array} \quad (5.8)$$

[Image: A graph of g(vx) versus vx, a Gaussian curve centered at vx=0.]
**Fig. 5.2** $g(v_{x})$, the distribution function for a particular component of molecular velocity (which is a Gaussian distribution).

## 5.2 The speed distribution

We now wish to turn to the problem of working out the distribution of molecular speeds in a gas. We want the fraction of molecules which are travelling with speeds between $v = |v|$ and $v + \mathrm{d}v$, and this corresponds to a spherical shell in velocity space of radius $v$ and thickness $\mathrm{d}v$ (see Fig. 5.3). The volume of velocity space corresponding to speeds between $v$ and $v + \mathrm{d}v$ is therefore equal to

$$4\pi v^{2}\mathrm{d}v, \quad (5.9)$$

so that the fraction of molecules with speeds between $v$ and $v + \mathrm{d}v$ can be defined as $f(v)\mathrm{d}v$, where $f(v)$ is given by

$$f(v)\mathrm{d}v\propto v^2\mathrm{d}v\mathrm{e}^{-mv^2 /2k_{\mathrm{B}}T}. \quad (5.10)$$

In this expression the $4\pi$ factor has been absorbed in the proportionality sign.

[Image: A 3D plot of velocity space showing a spherical shell of radius v and thickness dv. An octant of the shell is highlighted.]
**Fig. 5.3** Molecules with speeds between $v$ and $v + \mathrm{d}v$ occupy a volume of velocity space inside a spherical shell of radius $v$ and thickness $\mathrm{d}v$. (An octant of this sphere is shown cut-away.)

===== Page 50 =====

To normalize this function, so that $\int_{0}^{\infty}f(v)\mathrm{d}v = 1$, we must evaluate the integral (using eqn C.3)

$$\int_{0}^{\infty}v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}\mathrm{d}v = \frac{1}{4}\sqrt{\frac{\pi}{(m / 2k_{\mathrm{B}}T)^{3}}}, \quad (5.11)$$

so that

$$\int f(v)\mathrm{d}v = \frac{4}{\sqrt{\pi}}\left(\frac{m}{2k_{\mathrm{B}}T}\right)^{3 / 2}v^{2}\mathrm{d}v\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}. \quad (5.12)$$

[Image: A graph of f(v) versus v/v_max. The curve starts at 0, rises to a peak, and then decays. Three vertical dotted lines mark v_max, <v>, and v_rms in order.]
**Fig. 5.4** $f(v)$, the distribution function for molecular speeds (Maxwell-Boltzmann distribution).

This speed distribution function is known as the Maxwell-Boltzmann speed distribution, or sometimes simply as a Maxwellian distribution and is plotted in Fig. 5.4. Having derived the Maxwell-Boltzmann distribution function (eqn 5.10) we are now in a position to derive some of its properties.

### 5.2.1 $\langle v\rangle$ and $\langle v^2\rangle$

It is straightforward to find the following expected values of the Maxwell-Boltzmann distribution using standard integrals:

$$\begin{array}{rcl}{\langle v\rangle} & = & {\int_0^\infty vf(v)\mathrm{d}v = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}},}\\ {\langle v^2\rangle} & = & {\int_0^\infty v^2 f(v)\mathrm{d}v = \frac{3k_{\mathrm{B}}T}{m}.} \end{array} \quad (5.14)$$

Note that using eqns 5.7 and 5.14 we can write

$$\langle v_{x}^{2}\rangle +\langle v_{y}^{2}\rangle +\langle v_{z}^{2}\rangle = \frac{k_{\mathrm{B}}T}{m} +\frac{k_{\mathrm{B}}T}{m} +\frac{k_{\mathrm{B}}T}{2} = \frac{3k_{\mathrm{B}}T}{m} = \langle v^{2}\rangle \quad (5.15)$$

as expected.

Note also that the root mean squared speed of a molecule

$$v_{\mathrm{rms}} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} \quad (5.16)$$

is proportional to $m^{- 1 / 2}$.

### 5.2.2 The mean kinetic energy of a gas molecule

The mean kinetic energy of a gas molecule is given by

$$\langle E_{\mathrm{KE}}\rangle = \frac{1}{2} m\langle v^2\rangle = \frac{3}{2} k_{\mathrm{B}}T. \quad (5.17)$$

This is an important result, and we will later derive it again by a different route (see Section 19.2.1). It demonstrates that the average energy of a molecule in a gas depends only on temperature.

===== Page 51 =====

### 5.2.3 The maximum of $f(v)$

The maximum value of $f(v)$ is found by setting

$$\frac{\mathrm{d}f}{\mathrm{d}v} = 0, \quad (5.18)$$

and straightforward differentiation of eqn 5.10 yields

$$v_{\mathrm{max}} = \sqrt{\frac{2k_{\mathrm{B}}T}{m}}. \quad (5.19)$$

Since

$$\sqrt{2} < \sqrt{\frac{8}{\pi}} < \sqrt{3}, \quad (5.20)$$

we have that

$$v_{\mathrm{max}}< \langle v\rangle < v_{\mathrm{rms}} \quad (5.21)$$

and hence the points marked on Fig. 5.4 are in the order drawn. The mean speed of the Maxwell-Boltzmann distribution is higher than the value of the speed corresponding to the maximum in the distribution since the shape of $f(v)$ is such that the tail to the right is very long.

## Example 5.1

Calculate the rms speed of a nitrogen $\mathrm{N}_{2}$ molecule at room temperature. [One mole of $\mathrm{N}_{2}$ has a mass of $28\mathrm{g}$.]

Solution:

For nitrogen at room temperature, $m = (0.028\mathrm{kg}) / (6.022\times 10^{23})$ and so $v_{\mathrm{rms}}\approx 500\mathrm{m}\mathrm{s}^{-1}$. This is about 1100 miles per hour, and is the same order of magnitude as the speed of sound.

## 5.3 Experimental justification

How do you demonstrate that the velocity distribution in a gas obeys the Maxwell-Boltzmann distribution? A possible experimental apparatus is shown in Fig. 5.5. This consists of an oven, a velocity selector, and a detector, which are mounted on an optical bench. Hot gas atoms emerge from the oven and pass through a collimating slit. Velocity selection of molecules is achieved using discs with slits cut into them, which are rotated at high angular speed by a motor. A phase shifter varies the phase of the voltage fed to the motor for one disc relative to that of the other, so that the angle between the slits on the two discs can be continuously adjusted. Thus only molecules travelling with a particular speed from the oven will pass through the slits in both discs. A beam of light can be used to determine when the velocity selector is set for zero transit time. This beam is produced by a small light source near

[Image: A schematic diagram of an experimental setup. An oven emits a beam of molecules through a collimating slit. The beam then passes through a velocity selector consisting of two rotating discs. A detector is at the end of the beam path.]
**Fig. 5.5** The experimental apparatus that can be used to measure the Maxwell-Boltzmann distribution.

===== Page 52 =====

one disc and passes through the velocity selector and is detected by a photocell near the other disc.

Another way of selecting the velocity is shown in Fig. 5.6. This consists of a solid surface on whose surface is cut a helical slot, and which is capable of rotation around the cylinder's axis at a rate $\omega$. A molecule of velocity $v$ which goes through the slot without changing its position relative to the sides of the slot will satisfy the equation

$$v = \frac{\omega L}{\phi}, \quad (5.22)$$

in which $\phi$ and $L$ are the fixed angle and length shown in Fig. 5.6. Tuning $\omega$ allows you to tune the selected velocity $v$.

[Image: A 3D diagram of a velocity selector. It is a cylinder with a helical slot cut into it. The cylinder has radius r, length L, and the slot subtends an angle phi.]
**Fig. 5.6** Diagram of the velocity selector. (After R.C. Miller and P. Kusch, Phys. Rev. 99, 1314 (1955).) Copyright (1955) by the American Physical Society.

Data from this experiment are shown in Fig. 5.7. In fact, the intensity as a function of velocity $v$ does not follow the expected $v^{2}\mathrm{e}^{- mv^{2} / 2k_{\mathrm{B}}T}$ distribution but instead fits to $v^{4}\mathrm{e}^{- mv^{2} / 2k_{\mathrm{B}}T}$. What has gone wrong?

Nothing has gone wrong, but there are two factors of $v$ that must be included for two different reasons. One factor of $v$ comes from the fact that the gas atoms emerging through the small aperture in the wall of the oven are not completely representative of the atoms inside the oven. This effect will be analysed in Chapter 7. The other factor of $v$ comes from the fact that as the velocity selector is spun faster, it accepts a smaller fraction of molecules. This can be understood in detail as follows. Because of the finite width of the slit, the velocity selector selects molecules with a range of velocities. The limiting velocities correspond to molecules that enter the slot at one wall and leave the slot at the opposite wall. This leads to velocities that range all the way from $\omega L / \phi_{-}$ to $\omega L / \phi_{+}$, where $\phi_{\pm} = \phi \pm l / r$ and $l$ and $r$ are as defined in Fig. 5.6. Thus the range, $\Delta v$, of velocities transmitted is given by

$$\Delta v = \omega L\left(\frac{1}{\phi_{-}} -\frac{1}{\phi_{+}}\right)\approx \frac{2l}{\phi r} v, \quad (5.23)$$

===== Page 53 =====

and thus increases as the selected velocity increases. This gives rise to the second additional factor of $v$.

Another way to justify the treatment in this chapter experimentally is to look at spectral lines of hot gas atoms. The limit on resolution is often set by Doppler broadening: those atoms travelling towards a detector with a component of velocity $v_{x}$ towards the detector will have transition frequencies that differ from those of atoms at rest due to the Doppler shift. A spectral line with frequency $\omega_{0}$ (and wavelength $\lambda_{0} = 2\pi c / \omega_{0}$, where $c$ is the speed of light) will be Doppler-shifted to a frequency $\omega_{0}(1\pm v_{x} / c)$ and the $\pm$ sign reflects molecules travelling towards or away from the detector. The Gaussian distribution of velocities given by eqn 5.2 now gives rise to a Gaussian shape of the spectral line $I(\omega)$ (see Fig. 5.8), which is given by

$$I(\omega)\propto \exp \left(-\frac{mc^{2}(\omega_{0} - \omega)^{2}}{2k_B T\omega_{0}^{2}}\right), \quad (5.24)$$

[Image: A graph of intensity I(omega) versus omega. The curve is a Gaussian centered at omega_0. The full-width at half-maximum, Delta omega_FWHM, is marked.]
**Fig. 5.8** The intensity of a Doppler-broadened spectral line.

and the full-width at half-maximum (FWHM) of this spectral line is given by either $\Delta \omega^{\mathrm{FWHM}}$ (or in wavelength by $\Delta \lambda^{\mathrm{FWHM}}$) by

$$\frac{I(\omega_{0} + \Delta\omega^{\mathrm{FWHM}} / 2)}{I(\omega_{0})} = \frac{1}{2} \quad (5.25)$$

so that

$$\frac{\Delta\omega^{\mathrm{FWHM}}}{\omega_0} = \frac{\Delta\lambda^{\mathrm{FWHM}}}{\lambda_0} = 2\sqrt{2\ln 2\frac{k_{\mathrm{B}}T}{mc^2}}. \quad (5.26)$$

Another source of broadening of spectral lines arises from molecular collisions. This is called collisional broadening or sometimes pressure broadening (since collisions are more frequent in a gas when the pressure is higher, see Section 8.1). Doppler broadening is therefore most important in low-pressure gases.

[Image: A portrait of James Clerk Maxwell, a man with a full beard.]
**Fig. 5.9** James Clerk Maxwell

===== Page 54 =====

## Chapter summary

A physical situation that is very important in kinetic theory is the translational motion of atoms or molecules in a gas. The probability distribution for a given component of velocity is given by

$$g(v_{x})\propto \mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}.$$

We have shown that the corresponding expression for the probability distribution of molecular speeds is given by

$$\int f(v)\propto v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}.$$

This is known as a Maxwell-Boltzmann distribution, or sometimes as a Maxwellian distribution.

Two important average values of the Maxwell-Boltzmann distribution are:

$$\langle v\rangle = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}},\qquad \langle v^2\rangle = \frac{3k_{\mathrm{B}}T}{m}.$$

## Exercises

(5.1) Evaluate the integrals in eqns 5.5-5.7 and eqns 5.13 and 5.14, and check that you get the same answers.

(5.2) Calculate the rms speed of hydrogen $(\mathrm{H}_{2})$, helium (He) and oxygen $(\mathrm{O}_{2})$ at room temperature. [The atomic masses of H, He, and O are 1, 4, and 16 respectively.] Compare these speeds with the escape velocity on the surface of (i) the Earth, (ii) the Sun.

(5.3) What fractional error do you make if you approximate $\sqrt{\langle v^{2}\rangle}$ by $\langle v\rangle$ for a Maxwell-Boltzmann gas?

(5.4) A Maxwell-Boltzmann distribution implies that a given molecule (mass $m$) will have a speed between $v$ and $v + \mathrm{d}v$ with probability equal to $f(v)\mathrm{d}v$ where

$$f(v)\propto v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T},$$

and the proportionality sign is used because a normalization constant has been omitted. (You can correct for this by dividing any averages you work out by $\int_{0}^{\infty}f(v)\mathrm{d}v$.) For this distribution, calculate the mean speed $\langle v\rangle$ and the mean inverse speed $\langle 1 / v\rangle$. Show that

$$\langle v\rangle \langle 1 / v\rangle = \frac{4}{\pi}.$$

(5.5) The width of a spectral line (FWHM) is often quoted as

$$\Delta \lambda^{\mathrm{FWHM}} = 7.16\times 10^{-7}\lambda_0\sqrt{\frac{T}{m}}, \quad (5.27)$$

where $T$ is the temperature in kelvin, $\lambda_{0}$ is the wavelength at the centre of the spectral line in the rest frame and $m$ is the atomic mass of the gas measured in atomic mass units (i.e., multiples of the mass of a proton). Does this formula make sense?

(5.6) What is the Doppler broadening of the $21~\mathrm{cm}$ line in an interstellar gas cloud (temperature $100~\mathrm{K}$) composed of neutral hydrogen (i.e., non-ionized atomic hydrogen)? Express your answer in kHz.

(5.7) Calculate the rms speed of a sodium atom in the solar atmosphere at $6000~\mathrm{K}$. (The atomic mass of sodium is 23.) The sodium D lines ($\lambda = 5900\mathrm{\AA}$) are observed in a solar spectrum. Estimate the Doppler broadening in GHz.

===== Page 55 =====

## James Clerk Maxwell (1831-1879)

Born in Edinburgh, James Clerk Maxwell was brought up in the Scottish countryside at Glenair. He was educated at home until, at the age of ten, he was sent to the Edinburgh Academy where his unusual homemade clothes and distracted air earned him the nickname "Dafty".

[Image: A portrait of James Clerk Maxwell, a man with a full beard.]
**Fig. 5.9** James Clerk Maxwell

But a lot was going on in his head and he wrote his first scientific paper aged 14. Maxwell went to Peterhouse, Cambridge in 1850 but then moved to Trinity College, where he gained a fellowship in 1854. There he worked on the perception of colour, and also put Michael Faraday's ideas of lines of electrical force onto a sound mathematical basis. In 1856 he took up a chair in Natural Philosophy in Aberdeen where he worked on a theory of the rings of Saturn (confirmed by the Voyager spacecraft visits of the 1980's) and, in 1858, married the College Principal's daughter, Katherine Mary Dewar.

In 1859, he was inspired by a paper of Clausius on diffusion in gases to conceive of his theory of speed distributions in gases, outlined in Chapter 5, which, with its subsequent elaborations by Boltzmann, is known as the Maxwell-Boltzmann distribution. These triumphs were not enough to preserve him from the consequences of the merging of Aberdeen's two Universities in 1860 when, incredibly, the powers that be decided that it was Maxwell out of the two Professors of Natural Philosophy who should be made redundant. He failed to obtain a chair at Edinburgh (losing out to Tait) but instead moved to King's College, London. There, he produced the world's first colour photograph, came up with his theory of electromagnetism that proposed that light was an electromagnetic wave and explained its speed in terms of electrical properties, and chaired a committee to decide on a new system of units to incorporate the new understanding of the link between electricity and magnetism (and which became known as the "Gaussian", or cgs, system - though "Maxwellian system" would have been more appropriate). He also constructed his apparatus for measuring the viscosity of gases (see Chapter 9), verifying some of his predictions, but not others.

In 1865, he resigned his chair at King's and moved full time to Glenair, where he wrote his Theory of Heat which introduced what are now known as Maxwell relations (Chapter 16) and the concept of the Maxwell's demon (Section 14.7). He applied for, but did not get, the position of Principal of St Andrews' University, but in 1871 was appointed to the newly-established Professorship of Experimental Physics in Cambridge (after William Thomson and Hermann Helmholtz both turned the job down). There he supervised the building of the Cavendish Laboratory and wrote his celebrated A Treatise on Electricity and Magnetism (1873) where his four electromagnetic equations ("Maxwell's equations") first appear. In 1877 he was diagnosed with abdominal cancer and died in Cambridge in 1879.

In his short life Maxwell had been one of the most prolific, inspirational, and creative scientists who has ever lived. His work has had far-reaching implications in much of physics, not just in thermodynamics. He had also lived a devout and contemplative life in which he had been free of pride, selfishness, and ego, always generous and courteous to everyone. The doctor who tended him in his last days wrote:

I must say that he is one of the best men I have ever met, and a greater merit than his scientific achievements is his being, so far as human judgement can discern, a most perfect example of a Christian gentleman.

Maxwell summed up his own philosophy as follows:

Happy is the man who can recognize in the work of Today a connected portion of the work of life, and an embodiment of the work of Eternity. The foundations of his confidence are unchangeable, for he has been made a partaker of Infinity.

===== Page 56 =====

# 6 Pressure

6.1 Molecular distributions  57
6.2 The ideal gas law  58
6.3 Dalton's law  60
Chapter summary  61
Exercises  61

One of the most fundamental variables in the study of gases is pressure. The pressure $p$ due to a gas (or in fact any fluid) is defined as the ratio of the perpendicular contact force to the area of contact. The unit is therefore that of force (N) divided by that of area $(\mathrm{m}^2)$ and is called the pascal $(\mathrm{Pa} = \mathrm{Nm}^{-2})$. The direction in which pressure acts is always at right angles to the surface upon which it is acting.

Other units for measuring pressure are sometimes encountered, such as the bar (1 bar $= 10^{5}$ Pa) and the almost equivalent atmosphere (1 atm $= 1.01325\times 10^{5}$ Pa). The pressure of the atmosphere at sea level actually varies depending on the weather by approximately $\pm 50$ mbar around the standard atmosphere of 1013.25 mbar, though pressures (adjusted for sea level) as low as 882 mbar and as high as 1084 mbar have been recorded. An archaic unit is the torr, which is equal to a millimetre of mercury (Hg): 1 torr $= 133.32$ Pa.

## Example 6.1

Air has a density of about $1.29\mathrm{kgm}^{-3}$. Give a rough estimate of the height of the atmosphere assuming that the density of air in the atmosphere is uniform.

Solution:

Atmospheric pressure $p\approx 10^{5}$ Pa is due to the weight of air $\rho gh$ in the atmosphere (with assumed height $h$ and uniform density $\rho$) pressing down on each square metre. Hence $h = p / \rho g\approx 10^{4}\mathrm{m}$ (which is about the cruising altitude of planes). Of course, in reality the density of the atmosphere falls off with increasing height (see Chapter 37).

The pressure $p$ of a volume $V$ of gas (comprising $N$ molecules) depends on its temperature $T$ via an equation of state, which is an expression of the form

$$p = f(T,V,N), \quad (6.1)$$

where $f$ is some function. One example of an equation of state is that for an ideal gas, which was given in eqn 1.12:

$$pV = Nk_{\mathrm{B}}T. \quad (6.2)$$

[Image: A square box containing several small circles, each with a line with an arrowhead attached, representing molecules moving and bouncing off the walls of the container.]
**Fig. 6.1** In the kinetic theory of gases, a gas is modelled as a number of individual tiny particles (atoms or molecules), which can bounce off the walls of the container and each other.

[Image: A portrait of Robert Boyle in 17th century dress, wearing a long curly wig.]
**Fig. 6.6** Robert Boyle

===== Page 57 =====

Daniel Bernoulli (1700-1782) attempted an explanation of Boyle's law $(p \propto 1 / V)$ by assuming (controversially at the time) that gases were composed of a vast number of tiny particles (see Fig. 6.1). This was the first serious attempt at a kinetic theory of gases of the sort that we will describe in this chapter to derive the ideal gas equation.

## 6.1 Molecular distributions

In the previous chapter we derived the Maxwell-Boltzmann speed distribution function $f(v)$. We denote the total number of molecules per unit volume by the symbol $n$. The number of molecules per unit volume travelling with speeds between $v$ and $v + \mathrm{d}v$ is then given by $nf(v)\mathrm{d}v$. We now seek to determine the distribution function of molecules travelling in different directions.

### 6.1.1 Solid angles

Recall that an angle $\theta$ in a circle is defined by dividing the arc length $s$ which the angle subtends by the radius $r$ (see Fig. 6.2), so that

$$\theta = \frac{s}{r}. \quad (6.3)$$

The angle is measured in radians. The angle subtended by the whole circle at its centre is then

$$\frac{2\pi r}{r} = 2\pi . \quad (6.4)$$

By analogy, a solid angle $\Omega$ in a sphere (see Fig. 6.3) is defined by dividing the surface area $A$ which the solid angle subtends by the radius squared, so that

$$\Omega = \frac{A}{r^2}. \quad (6.5)$$

The solid angle is measured in steradians. The solid angle subtended by a whole sphere at its centre is then

$$\frac{4\pi r^2}{r^2} = 4\pi . \quad (6.6)$$

### 6.1.2 The number of molecules travelling in a certain direction at a certain speed

If all molecules are equally likely to be travelling in any direction, the fraction whose trajectories lie in an elemental solid angle $\mathrm{d}\Omega$ is

$$\frac{\mathrm{d}\Omega}{4\pi}. \quad (6.7)$$

If we choose a particular direction, then the solid angle $\mathrm{d}\Omega$ corresponding to molecules travelling at angles between $\theta$ and $\theta + \mathrm{d}\theta$ to that direction is

[Image: A diagram showing an angle theta subtended by an arc length s at the centre of a circle of radius r.]
**Fig. 6.2** The definition of angle $\theta$ in terms of the arc length.

[Image: A diagram showing a solid angle Omega subtended by a surface area A on a sphere of radius r.]
**Fig. 6.3** The definition of solid angle $\Omega = A / r^2$ where $r$ is the radius of the sphere and $A$ is the surface area over the region of the sphere indicated.

===== Page 58 =====

equal to the area of the annular region shown shaded in the unit-radius sphere of Fig. 6.4 which is given by

$$\mathrm{d}\Omega = 2\pi \sin \theta \mathrm{d}\theta , \quad (6.8)$$

so that

$$\frac{\mathrm{d}\Omega}{4\pi} = \frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.9)$$

Therefore, a number of molecules per unit volume given by

$$n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta \quad (6.10)$$

have speeds between $v$ and $v + \mathrm{d}v$ and are travelling at angles between $\theta$ and $\theta +\mathrm{d}\theta$ to the chosen direction, where $f(v)$ is the speed distribution function.

### 6.1.3 The number of molecules hitting a wall

We now let our particular direction, up until now arbitrarily chosen, lie perpendicular to a wall of area $A$ (see Fig. 6.5). In a small time $\mathrm{d}t$ the molecules travelling at angle $\theta$ to the normal to the wall sweep out a volume

$$A v\mathrm{d}t\cos \theta . \quad (6.11)$$

Multiplying this volume by the number in expression 6.10 implies that in time $\mathrm{d}t$, the number of molecules hitting a wall of area $A$ is

$$A v\mathrm{d}t\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.12)$$

Hence, the number of molecules hitting unit area of wall in unit time, and having speeds between $v$ and $v + \mathrm{d}v$ and travelling at angles between $\theta$ and $\theta +\mathrm{d}\theta$, is given by

$$v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.13)$$

[Image: A diagram of a sphere of unit radius. An annular shaded region is shown, corresponding to angles between theta and theta + dtheta from a particular direction. The radius of the annulus is sin(theta).]
**Fig. 6.4** The area of the shaded region on this sphere of unit radius is equal to the circumference of a circle of radius $\sin \theta$ multiplied by the width $d\theta$ and is hence given by $2\pi \sin \theta d\theta$.

[Image: A diagram showing a volume element swept out by molecules moving at velocity v at an angle theta to the normal of a wall of area A. The volume is A v dt cos(theta).]
**Fig. 6.5** Molecules hit a region of wall (of cross-sectional area $A^{1/2}\times A^{1/2} = A$) at an angle $\theta$. The number hitting in time $\mathrm{d}t$ is the volume of the shaded region ($A\mathrm{d}t\cos \theta$) multiplied by $n f(v)\mathrm{d}v\frac{1}{2}\sin \theta$

## 6.2 The ideal gas law

We are now in a position to calculate the pressure of a gas on its container. Each molecule hitting the wall of the container has a momentum change of $2mv\cos \theta$, which is perpendicular to the wall. This change of momentum is equivalent to an impulse. Hence, if we multiply $2mv\cos \theta$ (the momentum change arising from one molecule hitting the container walls) by the number of molecules hitting unit area per unit time, and having speeds between $v$ and $v + \mathrm{d}v$ and angles between $\theta$ and $\theta +\mathrm{d}\theta$ (which we derived in eqn 6.13), and then integrating over $\theta$ and $v$, we should get the pressure $p$. Thus

$$\begin{array}{rcl}{p}&{=}&{\int_{0}^{\infty}\int_{0}^{\pi/2}(2mv\cos\theta)\left(v\cos\theta n f(v)\mathrm{d}v\frac{1}{2}\sin\theta\mathrm{d}\theta\right)}\\{=}&{m n\int_{0}^{\infty}\mathrm{d}v v^{2}f(v)\int_{0}^{\pi/2}\cos^{2}\theta\sin\theta\mathrm{d}\theta,}\end{array} \quad (6.14)$$

===== Page 59 =====

and using the integral $\int_{0}^{\pi /2}\cos^{2}\theta \sin \theta \mathrm{d}\theta = \frac{1}{3}$, we have that

$$p = \frac{1}{3} nm\langle v^2\rangle . \quad (6.15)$$

If we write the total number of molecules $N$ in volume $V$ as

$$N = nV, \quad (6.16)$$

then this equation can be written as

$$pV = \frac{1}{3} Nm\langle v^2\rangle . \quad (6.17)$$

Using $\langle v^2 \rangle = 3k_{\mathrm{B}}T / m$, this can be rewritten as

$$pV = Nk_{\mathrm{B}}T, \quad (6.18)$$

which is the ideal gas equation we met in eqn 1.12. This completes the kinetic theory derivation of the ideal gas law.

## Equivalent forms of the ideal gas law:

The form given in eqn 6.18 is

$$pV = Nk_{\mathrm{B}}T,$$

and contains an "$N$", which we reiterate is the total number of molecules in the gas.

An equivalent form of the ideal gas equation can be derived by dividing both sides of eqn 6.18 by volume, so that

$$p = nk_{\mathrm{B}}T, \quad (6.19)$$

where $n = N / V$ is the number of molecules per unit volume.

Another form of the ideal gas law can be obtained by writing the number of molecules $N = n_{\mathrm{m}}N_{\mathrm{A}}$, where $n_{\mathrm{m}}$ is the number of moles and $N_{\mathrm{A}}$ is the Avogadro number (the number of molecules in a mole, see Section 1.1). In this case, eqn 6.18 becomes

$$pV = n_{\mathrm{m}}RT, \quad (6.20)$$

where

$$R = N_{\mathrm{A}}k_{\mathrm{B}} \quad (6.21)$$

is the gas constant $(R = 8.31447 \mathrm{J} \mathrm{K}^{-1} \mathrm{mol}^{-1})$.

The ideal gas law $(p = nk_{\mathrm{B}}T)$ expresses the important point that the pressure of an ideal gas does not depend on the mass $m$ of the molecules. Although more massive molecules transfer greater momentum to the container walls than light molecules, their mean velocity is lower and so they make fewer collisions with the walls. Therefore the pressure is the same for a gas of light or massive molecules; it depends only on $n$, the number per unit volume, and the temperature.

===== Page 60 =====

## Example 6.2

What is the volume occupied by one mole of ideal gas at standard temperature and pressure (STP, defined as $0^{\circ}\mathrm{C}$ and 1 atm)?

Solution:

At $p = 1.01325\times 10^{5}\mathrm{Pa}$ and $T = 273.15\mathrm{K}$, the molar volume $V_{\mathrm{m}}$ can be obtained from eqn 6.20 as

$$V_{\mathrm{m}} = \frac{RT}{p} = 0.022414\mathrm{m}^{3} = 22.414\mathrm{litres}. \quad (6.22)$$

## Example 6.3

What is the connection between pressure and kinetic energy density?

Solution:

The kinetic energy of a gas molecule moving with speed $v$ is

$$\frac{1}{2} mv^{2}. \quad (6.23)$$

The total kinetic energy of the molecules of a gas per unit volume, i.e., the kinetic energy density, which we will call $u$, is therefore given by

$$u = n\int_{0}^{\infty}\frac{1}{2} mv^{2}f(v)\mathrm{d}v = \frac{1}{2} nm\langle v^{2}\rangle , \quad (6.24)$$

so that comparing with eqn 6.15 we have that

$$p = \frac{2}{3} u. \quad (6.25)$$

## 6.3 Dalton's law

If one has a mixture of gases in thermal equilibrium, then the total pressure $p = nk_{\mathrm{B}}T$ is simply the sum of the pressures due to each component of the mixture. We can write $n$ as

$$n = \sum_{i}n_{i}, \quad (6.26)$$

where $n_{i}$ is the number density of the $i$th species. Therefore

$$p = \left(\sum_{i}n_{i}\right)k_{\mathrm{B}}T = \sum_{i}p_{i}, \quad (6.27)$$

where $p_{i} = n_{i}k_{\mathrm{B}}T$ is known as the partial pressure of the $i$th species. The observation that $p = \sum_{i}p_{i}$ is known as Dalton's law, after the British chemist John Dalton (1766-1844), who was a pioneer of the atomic theory.

===== Page 61 =====

## Example 6.4

Air is $75.5\%$ $\mathrm{N}_{2}$, $23.2\%$ $\mathrm{O}_{2}$, $1.3\%$ Ar, and $0.05\%$ $\mathrm{CO}_{2}$ by mass. Calculate the partial pressure of $\mathrm{CO}_{2}$ in air at atmospheric pressure.

Solution:

Dalton's law states that the partial pressure is proportional to the number density. The number density is proportional to the mass fraction divided by the molar mass. The molar masses of the species (in grammes) are 28 $\mathrm{N}_{2}$, 32 $\mathrm{O}_{2}$, 40 $\mathrm{Ar}$, and 44 $\mathrm{CO}_{2}$. Hence, the partial pressure of $\mathrm{CO}_{2}$ is

$$p_{\mathrm{CO}_{2}} = \frac{\frac{0.05}{44}}{\frac{75.5}{28} + \frac{23.2}{32} + \frac{1.3}{40} + \frac{0.05}{44}} = 0.00033\mathrm{atm}. \quad (6.28)$$

## Chapter summary

The pressure, $p$, is given by

$$p = \frac{1}{3} nm\langle v^2\rangle ,$$

where $n$ is the number of molecules per unit volume and $m$ is the molecular mass.

This expression agrees with the ideal gas equation,

$$p = nk_{\mathrm{B}}T,$$

where $V$ is the volume, $T$ is the temperature and $k_{\mathrm{B}}$ is the Boltzmann constant.

## Exercises

(6.1) What is the volume occupied by 1 mole of gas at $10^{-10}$ torr, the pressure inside an "ultra high vacuum" (UHV) chamber.

(6.2) Calculate $u$, the kinetic energy density, for air at atmospheric pressure.

(6.3) Mr Fourier sits in his living room at $18^{\circ}\mathrm{C}$. He decides he is rather cold and turns the heating up so that the temperature is $25^{\circ}\mathrm{C}$. What happens to the total energy of the air in his living room? [Hint: what controls the pressure in the room?]

(6.4) A diffuse cloud of neutral hydrogen atoms (known as HI) in space has a temperature of $50\mathrm{K}$ and number density $500\mathrm{cm}^{-3}$. Calculate the pressure (in Pa) and the volume (in cubic light years) occupied by the cloud if its mass is $100M_{\odot}$ ($M_{\odot}$ is the symbol for the mass of the Sun, see Appendix A.)

===== Page 62 =====

(6.5) (a) Given that the number of molecules hitting unit area of a surface per second with speeds between $v$ and $v + \mathrm{d}v$ and angles between $\theta$ and $\theta +d\theta$ to the normal is

$$\frac{1}{2} v n f(v)\mathrm{d}v\sin \theta \cos \theta d\theta ,$$

show that the average value of $\cos \theta$ for these molecules is $\frac{2}{3}$.

(b) Using the results above, show that for a gas obeying the Maxwellian distribution (i.e., $f(v)\propto v^{2}e^{-mv^{2} / 2k_{\mathrm{B}}T}$) the average energy of all the molecules is $\frac{3}{2} k_{\mathrm{B}}T$, but the average energy of those hitting the surface is $2k_{\mathrm{B}}T$.

(6.6) The molecules in a gas travel with different velocities. A particular molecule will have velocity $\mathbf{v}$ and speed $v = |\mathbf{v}|$ and will move at an angle $\theta$ to some chosen fixed axis. We have shown that the number of molecules in a gas with speeds between $v$ and $v + \mathrm{d}v$ and moving at angles between $\theta$ and $\theta +d\theta$ to any chosen axis is given by

$$\frac{1}{2} n f(v)\mathrm{d}v\sin \theta d\theta ,$$

where $n$ is the number of molecules per unit volume and $f(v)$ is some function of $v$ only. [$f(v)$ could be the Maxwellian distribution given above; however you should not assume this but rather calculate the general case.] Hence show by integration that:

(a) $\langle u\rangle = 0$
(b) $\langle u^{2}\rangle = \frac{1}{3}\langle v^{2}\rangle$
(c) $\langle |u|\rangle = \frac{1}{2}\langle v\rangle$

where $u$ is any one Cartesian component of $v$, i.e., $v_{x}$, $v_{y}$, or $v_{z}$.

[Hint: You can take $u$ as the $z$-component of $\mathbf{v}$ without loss of generality. Why? Then express $u$ in terms of $v$ and $\theta$ and average over $v$ and $\theta$. You can use expressions such as

$$\langle v\rangle = \frac{\int_{0}^{\infty}v f(v)\mathrm{d}v}{\int_{0}^{\infty}f(v)\mathrm{d}v}$$

and similarly for $\langle v^{2}\rangle$. Make sure you understand why.]

(6.7) If $v_{1}$, $v_{2}$, $v_{3}$ are three Cartesian components of $\mathbf{v}$ what value do you expect for $\langle v_{1}v_{2}\rangle$, $\langle v_{1}v_{3}\rangle$, and $\langle v_{2}v_{3}\rangle$? Evaluate one of them by integration to check your deduction.

(6.8) Calculate the partial pressure of $\mathrm{O}_{2}$ in air at atmospheric pressure.

(6.9) This question provides an alternative derivation of the formula for pressure. Without loss of generality, let us consider molecules travelling towards a wall which lies in the $xy$ plane. The momentum change of a molecule of mass $m$ and velocity $\mathbf{v} = (v_{x},v_{y},v_{z})$ bouncing off the wall will be $2mv_{x}$. Explain why the pressure $p$ on the wall is given by

$$p = \int_{0}^{\infty}(2mv_{x})v_{x}n g(v_{x})\mathrm{d}v_{x}, \quad (6.29)$$

where $g(v_{x})$ is the function given in eqn 5.2. Hence show that $p = nk_{\mathrm{B}}T$. Using the same approach show that $\Phi$ the number of molecules hitting unit area of the wall per second is given by

$$\Phi = \int_{0}^{\infty}v_{x}n g(v_{x})\mathrm{d}v_{x} = n\sqrt{\frac{k_{\mathrm{B}}T}{\pi m}} = \frac{1}{4} n\langle v\rangle .$$

This result will be derived using a different method in the next chapter.

===== Page 63 =====

## Robert Boyle (1627-1691)

Robert Boyle was born into wealth. His father was a self-made man of humble yeoman stock who, at the age of 22, had left England for Ireland to seek his fortune.

[Image: A portrait of Robert Boyle in 17th century dress, wearing a long curly wig.]
**Fig. 6.6** Robert Boyle

This his father found or, possibly more accurately, "grabbed" and through rapid land acquisition of a rather dubious nature Boyle senior became one of England's richest men and the Earl of Cork to boot. Robert was born when his father was in his sixties and was the last but one of his father's sixteen children. His father, as a new member of the aristocracy, believed in the best education for his children, and Robert was duly packed off to Eton and then, at the age of 12, sent off for a European Grand Tour, taking in Geneva, Venice, and Florence. Boyle studied the works of Galileo, who died in Florence while Boyle was staying in the city. Meanwhile, his father was getting into a spot of bother with the Irish rebellion of 1641-1642, resulting in the loss of the rents that kept him and his family in the manner to which they had become accustomed, and hence also causing Robert Boyle some financial difficulty. He was almost married off at this time to a wealthy heiress, but Boyle managed to escape this fate and remained unmarried for the rest of his life. His father died in 1643 and Boyle returned to England the following year, inheriting his father's Dorset estate.

However, by this time the Civil War (which had started in 1642) was in full swing and Boyle tried hard not to take sides. He kept his head down, devoting his time to study, building a chemical laboratory in his house and worked on moral and theological essays. Cromwell's defeat of the Irish in 1652 worked well for Boyle as many Irish lands were handed over to the English colonists. Financially, Boyle was now secure and ready to live the life of a gentleman. In London, he had met John Wilkins, who had founded an intellectual society, which he called "The Invisible College" and which suddenly brought Boyle into contact with the leading thinkers of the day. When Wilkins was appointed Warden of Wadham College, Oxford, Boyle decided to move to Oxford and set up a laboratory there. He set up an air pump and, together with a number of talented assistants (the most famous of which was Robert Hooke, later to discover his law of springs and to observe a cell with a microscope, in addition to numerous other discoveries) Boyle and his team conducted a large number of elaborate experiments in this new vacuum. They showed that sound did not travel in a vacuum, and that flames and living organisms could not be sustained, and discovered the "spring of air", namely that compressing air resulted in its pressure increasing, and that the pressure of a gas and its volume were in inverse proportion.

Boyle was much taken with the atomistic viewpoint as described by the French philosopher Pierre Gassendi (1592-1655), which seems particularly appropriate for someone whose work led to the path for the development of the kinetic theory of gases. His greatest legacy was in his reliance on experiment as a means of determining scientific truth. He was, however, also someone who often worked vicariously through a band of assistants, citing his weakness of health and of eyesight as a reason for failing to write his papers as he wished to and to have read other peoples' works as he ought; his writings are, however, full of criticisms of his assistants for making mistakes, failing to record data, and generally slowing down his research endeavours.

With the restoration of the monarchy in 1660, the Invisible College, which had been meeting for several years in Gresham College, London, sought the blessing of the newly crowned Charles II and became the Royal Society, which has existed ever since as a thriving scientific society. In 1680, Boyle (who had been a founding fellow of the Royal Society) was elected President of the Royal Society, but declined to hold the office, citing an unwillingness to take the necessary oaths. Boyle retained a strong Christian faith throughout his life, and prided himself on his honesty and pure seeking of the truth. In 1670, Boyle suffered a stroke but made a good recovery, staying active in research until the mid-1680's. He died in 1691, shortly after the death of his sister Katherine to whom he had been extremely close.

===== Page 64 =====

# 7 Molecular effusion

7.1 Flux  64
7.2 Effusion  66
Chapter summary  69
Exercises  69

Effusion is the process by which a gas escapes from a very small hole. The empirical relation known as Graham's law of effusion [after Thomas Graham (1805-1869)] states that the rate of effusion is inversely proportional to the square root of the mass of the effusing molecule.

Isotopes (the word means "same place") are atoms of a chemical element with the same atomic number $Z$ (and hence number of protons in the nucleus) but different atomic weights $A$ (and hence different number of neutrons in the nucleus).

## Example 7.1

Effusion can be used to separate different isotopes of a gas (which cannot be separated chemically). For example, in the separation of $^{235}\mathrm{UF}_6$ and $^{238}\mathrm{UF}_6$ the ratio of the effusion rates of the two gases is equal to

$$\sqrt{\frac{\mathrm{mass~of~}^{238}\mathrm{UF}_6}{\mathrm{mass~of~}^{235}\mathrm{UF}_6}} = \sqrt{\frac{352.0412}{348.0343}} = 1.00574, \quad (7.1)$$

which, although small, was enough for many kilogrammes of $^{235}\mathrm{UF}_6$ to be extracted for the Manhattan project in 1945 to produce the first uranium atom bomb, which was subsequently dropped on Hiroshima.

## Example 7.2

How much faster does helium gas effuse out of a small hole than $\mathrm{N}_2$?

Solution:

$$\sqrt{\frac{\mathrm{mass~of~}\mathrm{N}_2}{\mathrm{mass~of~}\mathrm{He}}} = \sqrt{\frac{28}{4}} = 2.6. \quad (7.2)$$

In this chapter, we will discover where Graham's law comes from. We begin by evaluating the flux of particles hitting the inside walls of the container of a gas.

## 7.1 Flux

The concept of flux is a very important one in thermal physics. It quantifies the flow of particles or the flow of energy or even the flow of momentum. Of relevance to this chapter is the molecular flux, $\Phi$, which

===== Page 65 =====

is defined to be the number of molecules striking unit area per second. Thus

$$\mathrm{molecular~flux} = \frac{\mathrm{number~of~molecules}}{\mathrm{area}\times\mathrm{time}}. \quad (7.3)$$

The units of molecular flux are therefore $\mathrm{m}^{-2}\mathrm{s}^{-1}$. We can also define heat flux using

$$\mathrm{heat~flux} = \frac{\mathrm{amount~of~heat}}{\mathrm{area}\times\mathrm{time}}. \quad (7.4)$$

The units of heat flux are therefore $\mathrm{Jm}^{-2}\mathrm{s}^{-1}$. In Section 9.1, we will also come across a flux of momentum.

Returning to the effusion problem, we note that the flux of molecules in a gas can be evaluated by integrating expression 6.13 over all $v$ and $\theta$, so that

$$\begin{array}{rcl}{\Phi} & = & {\int_0^\infty \int_0^{\pi /2}v\cos \theta nf(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta}\\ {} & = & {\frac{n}{2}\int_0^\infty \mathrm{d}v vf(v)\int_0^{\pi /2}\mathrm{d}\theta \cos \theta \sin \theta} \end{array} \quad (7.5)$$

so that

$$\Phi = \frac{1}{4} n\langle v\rangle . \quad (7.6)$$

An alternative expression for $\Phi$ can be found as follows: rearranging the ideal gas law $p = n k_{\mathrm{B}}T$, we can write

$$n = \frac{p}{k_{\mathrm{B}}T}, \quad (7.7)$$

and using the expression for the average speed of molecules in a gas from eqn 5.13

$$\langle v\rangle = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}}, \quad (7.8)$$

we can substitute these expressions into eqn 7.6 and obtain

$$\Phi = \frac{p}{\sqrt{2\pi m k_{\mathrm{B}}T}}. \quad (7.9)$$

Note that consideration of eqn 7.9 shows us that the effusion rate depends inversely on the square root of the mass, in agreement with Graham's law.

## Example 7.3

Calculate the particle flux from $\mathrm{N}_{2}$ gas at STP (standard temperature and pressure, i.e., 1 atm and $0^{\circ}\mathrm{C}$).

Solution:

$$\begin{array}{rl}\Phi & = \frac{1.01325\times 10^5\mathrm{Pa}}{\sqrt{2\pi\times(28\times 1.67\times 10^{-27}\mathrm{kg})\times 1.38\times 10^{-23}\mathrm{JK}^{-1}\times 273\mathrm{K}}}\\ & \approx 3\times 10^{27}\mathrm{m}^{-2}\mathrm{s}^{-1}. \end{array} \quad (7.10)$$

===== Page 66 =====

[Image: A box containing a gas, with a small hole in the top. Arrows show molecules effusing out of the hole.]
**Fig. 7.1** A gas effuses from a small hole in its container.

[Image: A box resting on a weighing scale. The box contains liquid at the bottom and gas above it, with a small hole at the top.]
**Fig. 7.2** The Knudsen method.

## 7.2 Effusion

Consider a container of gas with a small hole of area $A$ in the side. Gas will leak (i.e., effuse) out of the hole (see Fig. 7.1). The hole is small, so that the equilibrium of gas in the container is not disturbed. The number of molecules escaping per unit time is just the number of molecules hitting the hole area in the closed box per second, so is given by $\Phi A$ per second, where $\Phi$ is the molecular flux. This is the effusion rate.

## Example 7.4

In the Knudsen method of measuring vapour pressure $p$ from a liquid containing molecules of mass $m$ at temperature $T$, the liquid is placed in the bottom of a container that has a small hole of area $A$ at the top (see Fig. 7.2). The container is placed on a weighing balance and its weight $Mg$ is measured as a function of time. In equilibrium, the effusion rate is

$$\Phi A = \frac{pA}{\sqrt{2\pi mk_{\mathrm{B}}T}}, \quad (7.11)$$

so that the rate of change of mass, $\mathrm{d}M / \mathrm{d}t$ is given by $- m\Phi A$. Hence

$$p = \sqrt{\frac{2\pi k_{\mathrm{B}}T}{m}}\frac{1}{A}\left|\frac{\mathrm{d}M}{\mathrm{d}t}\right|. \quad (7.12)$$

Effusion preferentially selects faster molecules. Therefore the speed distribution of molecules effusing through the hole is not Maxwellian. This result seems paradoxical at first glance: aren't the molecules emerging from the box the same ones that were inside beforehand? How can their distribution be different?

The reason is that the faster molecules inside the box travel more quickly and have a greater probability of reaching the hole than their slower cousins. This can be expressed mathematically by noticing that the number of molecules hitting a wall (or a hole) is given by eqn 6.13 and this has an extra factor of $v$ in it. Thus the distribution of molecules effusing through the hole in some interval of time is proportional to

$$v^{3}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}. \quad (7.13)$$

Note the extra factor of $v$ in this expression compared with the usual Maxwell-Boltzmann distribution in eqn 5.10 (see Fig. 7.3). The molecules

[Image: A graph of f(v) versus v/v_max. Two curves are shown. The solid curve is proportional to v^2 exp(-mv^2/2k_B T), the Maxwellian distribution. The dashed curve is proportional to v^3 exp(-mv^2/2k_B T), the distribution for effusing gas. The dashed curve peaks at a higher velocity.]
**Fig. 7.3** The distribution function for molecular speeds (Maxwell-Boltzmann distribution) in a gas is proportional to $v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}$ (solid line) but the gas effusing from a small hole has a distribution function that is proportional to $v^{3}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}$ (dashed line). The distinction between the two situations occurs when counting the molecules crossing a fixed plane during some interval of time.

===== Page 67 =====

in the Maxwellian gas had an average energy of $\frac{1}{2} m\langle v^2\rangle = \frac{3}{2} k_{\mathrm{B}}T$, but the molecules in the effusing gas have a higher energy, as the following example will demonstrate.

## Example 7.5

What is the mean kinetic energy of gas molecules effusing out of a small hole?

Solution:

$$\langle \mathrm{kinetic~energy}\rangle = \frac{1}{2} m\langle v^2\rangle$$
$$= \frac{\frac{1}{2}m\int_0^\infty v^2v^3\mathrm{e}^{-\frac{1}{2}mv^2 / k_{\mathrm{B}}T}\mathrm{d}v}{\int_0^\infty v^3\mathrm{e}^{-\frac{1}{2}mv^2 / k_{\mathrm{B}}T}\mathrm{d}v}$$
$$= \frac{1}{2} m\left(\frac{2k_{\mathrm{B}}T}{m}\right)\frac{\int_0^\infty u^2\mathrm{e}^{-u}\mathrm{d}u}{\int_0^\infty u\mathrm{e}^{-u}\mathrm{d}u}$$

where the substitution $u = mv^2 / 2k_{\mathrm{B}}T$ has been made. Using the standard integral $\int_0^\infty x^n\mathrm{e}^{-x}\mathrm{d}x = n!$ (see Appendix C.1), we have that

$$\langle \mathrm{kinetic~energy}\rangle = 2k_{\mathrm{B}}T. \quad (7.15)$$

This is larger by a factor of $\frac{4}{3}$ than the mean kinetic energy of molecules in the gas. This is because effusion preferentially selects higher energy molecules.

The hole has to be small. How small? The diameter of the hole has to be much less than the mean free path $\lambda$, defined in Section 8.3.

## Example 7.6

Consider a container divided by a partition with a small hole, diameter $D$, containing the same gas on each side. The gas on the left-hand side has temperature $T_{1}$ and pressure $p_{1}$. The gas on the right-hand side has temperature $T_{2}$ and pressure $p_{2}$.

If $D\gg \lambda$, $p_1 = p_2$.

If $D\ll \lambda$, we are in the effusion regime and the system will achieve equilibrium when the molecular fluxes balance, so that

$$\Phi_{1} = \Phi_{2}, \quad (7.16)$$

so that, using eqn 7.9 we may write

$$\frac{p_1}{\sqrt{T_1}} = \frac{p_2}{\sqrt{T_2}}. \quad (7.17)$$

This is called the Knudsen effect, after Martin Knudsen (1871-1949).

===== Page 68 =====

A final example gives an approximate derivation of the flow rate of gas down a pipe at low pressures.

## Example 7.7

Estimate the mass flow rate of gas down a long pipe of length $L$ and diameter $D$ at very low pressures in terms of the difference in pressures $p_1 - p_2$ between the two ends of the pipe.

Solution:

This type of flow is known as Knudsen flow. At very low pressures, molecules collide with the walls of the tube much more often than they do with each other. Let us define a coordinate $x$, which measures the distance along the pipe. The net flux $\Phi (x)$ of molecules flowing down the pipe at position $x$ can be estimated by subtracting the molecules effusing down the pipe since their last collision (roughly a distance $D$ upstream) from the molecules effusing up the pipe since their last collision (roughly a distance $D$ downstream). Thus

$$\Phi (x)\approx \frac{1}{4}\langle v\rangle [n(x - D) - n(x + D)], \quad (7.18)$$

where $n(x)$ is the number density of molecules at position $x$. Using $p = \frac{1}{3} nm\langle v^2\rangle$ (eqn 6.15), this can be written

$$\Phi (x)\approx \frac{3}{4m}\frac{\langle v\rangle}{\langle v^2\rangle} [p(x - D) - p(x + D)]. \quad (7.19)$$

We can write

$$p(x - D) - p(x + D)\approx -2D\frac{\mathrm{d}p}{\mathrm{d}x}, \quad (7.20)$$

but also notice that in steady state $\Phi$ must be the same along the tube, so that

$$\frac{\mathrm{d}p}{\mathrm{d}x} = \frac{p_2 - p_1}{L}. \quad (7.21)$$

Hence the mass flow rate $\dot{M} = m\Phi (\pi D^2 /4)$ (where $\pi D^2 /4$ is the cross-sectional area of the pipe) is given by

$$\dot{M}\approx \frac{3}{8}\frac{\langle v\rangle}{\langle v^2\rangle}\pi D^3\frac{p_1 - p_2}{L}. \quad (7.22)$$

With eqns 5.13 and 5.14, we have that

$$\frac{\langle v\rangle^2}{\langle v^2\rangle} = \frac{8}{3\pi}, \quad (7.23)$$

and hence our estimate of the Knudsen flow rate is

$$\dot{M}\approx \frac{D^3}{\langle v\rangle}\frac{p_1 - p_2}{L}. \quad (7.24)$$

Note that the flow rate is proportional to $D^3$, so it is much more efficient to pump gas through wide pipes to obtain high flow rates.

===== Page 69 =====

## Chapter summary

The molecular flux, $\Phi$, is the number of molecules striking unit area per second and is given by

$$\Phi = \frac{1}{4} n\langle v\rangle .$$

This expression, together with the ideal gas equation, can be used to derive an alternative expression for the particle flux:

$$\Phi = \frac{p}{\sqrt{2\pi mk_{\mathrm{B}}T}}.$$

These expressions also govern molecular effusion through a small hole.

## Exercises

(7.1) In a vacuum chamber designed for surface-science experiments, the pressure of residual gas is kept as low as possible so that surfaces can be kept clean. The coverage of a surface by a single monolayer requires about $10^{19}$ atoms per $\mathrm{m}^2$. What pressure would be needed to deposit less than one monolayer per hour from residual gas? You may assume that if a molecule hits the surface, it sticks.

(7.2) A vessel contains a monatomic gas at temperature $T$. Use the Maxwell-Boltzmann distribution of speeds to calculate the mean kinetic energy of the molecules.

Molecules of the gas stream through a small hole into a vacuum. A box is opened for a short time and catches some of the molecules. Neglecting the thermal capacity of the box, calculate the final temperature of the gas trapped in the box.

(7.3) A closed vessel is partially filled with liquid mercury; there is a hole of area $10^{-7} \mathrm{~m}^2$ above the liquid level. The vessel is placed in a region of high vacuum at $273 \mathrm{~K}$ and after 30 days is found to be lighter by $2.4 \times 10^{-5} \mathrm{~kg}$. Estimate the vapour pressure of mercury at $273 \mathrm{~K}$. (The relative molecular mass of mercury is 200.59.)

(7.4) Calculate the mean speed and most probable speed for a molecule of mass $m$ which has effused out of an enclosure at temperature $T$. Which of the two speeds is the larger?

(7.5) A gas effuses into a vacuum through a small hole of area $A$. The particles are then collimated by passing through a very small circular hole of radius $a$, in a screen a distance $d$ from the first hole. Show that the rate at which particles emerge from the second hole is $\frac{1}{4} nA\langle v\rangle (a^2 /d^2)$, where $n$ is the particle density and $\langle v \rangle$ is the average speed. (Assume that no collisions take place after the gas effuses through the second hole, and that $d \gg a$.)

(7.6) Show that if a gas were allowed to leak through a small hole into an evacuated sphere and the particles condensed where they first hit the surface they would form a uniform coating.

(7.7) An astronaut goes for a space walk and her space suit is pressurized to 1 atm. Unfortunately, a tiny piece of space dust punctures her suit and it develops a small hole of radius $1 \mu\mathrm{m}$. What force does she feel due to the effusing gas?

(7.8) Show that the time dependence of the pressure inside an oven (volume $V$) containing hot gas (molecular mass $m$, temperature $T$) with a small hole of area $A$ is given by

$$p(t) = p(0)\mathrm{e}^{-t / \tau}, \quad (7.25)$$

with

$$\tau = \frac{V}{A}\sqrt{\frac{2\pi m}{k_{\mathrm{B}}T}}. \quad (7.26)$$

===== Page 70 =====

# 8 The mean free path and collisions

8.1 The mean collision time  70
8.2 The collision cross-section  71
8.3 The mean free path  73
Chapter summary  74
Exercises  74

It turns out that large-angle scattering dominates transport processes in most gases (described in Chapter 9) and is largely independent of energy and therefore temperature; this allows us to use a rigid-sphere model of collisions, i.e. to model atoms in a gas as billiard balls.

At room temperature, the rms speed of $\mathrm{O_2}$ or $\mathrm{N_2}$ is about $500~\mathrm{ms}^{-1}$. Processes such as the diffusion of one gas into another would therefore be almost instantaneous, were it not for the occurrence of collisions between molecules. Collisions are fundamentally quantum mechanical events, but in a dilute gas, molecules spend most of their time between collisions and so we can consider them as classical billiard balls and ignore the details of what actually happens during a collision. All that we care about is that after collisions the molecules' velocities become essentially randomized. In this chapter we will model the effect of collisions in a gas and develop the concepts of a mean collision time, the collision cross-section and the mean free path.

## 8.1 The mean collision time

In this section, we aim to calculate the average time between molecular collisions. Let us consider a particular molecule moving in a gas of other similar molecules. To make things simple to start with, we suppose that the molecule under consideration is travelling at speed $v$ and that the other molecules in the gas are stationary. This is clearly a gross over-simplification, but we will relax this assumption later. We will also attribute a collision cross-section $\sigma$ to each molecule, which is something like the cross-sectional area of our molecule. Again, we will refine this definition later in the chapter.

In a time dt, our molecule will sweep out a volume $\sigma v\mathrm{dt}$. If another molecule happens to lie inside this volume, there will be a collision. With $n$ molecules per unit volume, the probability of a collision in time dt is therefore $n\sigma v\mathrm{dt}$. Let us define $P(t)$ as follows:

$$P(t) = \mathrm{the~probability~of~a~molecule~not~colliding~up~to~time~}t. \quad (8.1)$$

Elementary calculus then implies that

$$P(t + \mathrm{d}t) = P(t) + \frac{\mathrm{d}P}{\mathrm{d}t}\mathrm{d}t, \quad (8.2)$$

but $P(t + \mathrm{d}t)$ is also the probability of a molecule not colliding up to time $t$ multiplied by the probability of not colliding in subsequent time dt, i.e.,

$$P(t + \mathrm{d}t) = P(t)(1 - n\sigma v\mathrm{d}t). \quad (8.3)$$

===== Page 71 =====

Hence rearranging gives

$$\frac{1}{P}\frac{\mathrm{d}P}{\mathrm{d}t} = -n\sigma v \quad (8.4)$$

and therefore that (using $P(0) = 1$)

$$P(t) = \mathrm{e}^{-n\sigma vt}. \quad (8.5)$$

Now the probability of surviving without collision up to time $t$ but then colliding in the next dt is

$$\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t. \quad (8.6)$$

We can check that this is a proper probability by integrating it,

$$\int_{0}^{\infty}\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t = 1, \quad (8.7)$$

and confirming that it is equal to unity. Here, use has been made of the integral

$$\int_{0}^{\infty}\mathrm{e}^{-x}\mathrm{d}x = 0! = 1 \quad (8.8)$$

(see Appendix C.1). We are now in a position to calculate the mean scattering time $\tau$, which is the average time elapsed between collisions for a given molecule. This is given by

$$\begin{array}{rcl}{\tau} & = & {\int_0^\infty t\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t}\\ {} & = & {\frac{1}{n\sigma v}\int_0^\infty (n\sigma vt)\mathrm{e}^{-n\sigma vt}\mathrm{d}(n\sigma vt)}\\ {} & = & {\frac{1}{n\sigma v}\int_0^\infty xe^{-x}\mathrm{d}x} \end{array} \quad (8.9)$$

where the integral has been simplified by the substitution $x = n\sigma vt$. Hence we find that

$$\tau = \frac{1}{n\sigma v}, \quad (8.10)$$

where use has been made of the integral (again, see Appendix C.1)

$$\int_{0}^{\infty}x\mathrm{e}^{-x}\mathrm{d}x = 1! = 1. \quad (8.11)$$

## 8.2 The collision cross-section

In this section we will consider the factor $\sigma$ in much more detail. To be as general as possible, we will consider two spherical molecules of radii $a_1$ and $a_2$ with a hard-sphere potential between them (see Fig. 8.1).

[Image: Two spheres of radii a1 and a2, touching at a point.]
**Fig. 8.1** Two spherical molecules of radii $a_1$ and $a_2$ with a hard-sphere potential between them.

===== Page 72 =====

This implies that there is a potential energy function $V(R)$ that depends on the relative separation $R$ of their centres, and is given by

$$V(R) = \left\{ \begin{array}{ll}0 & R > a_1 + a_2\\ \infty & R\leq a_1 + a_2 \end{array} \right. \quad (8.12)$$

and this is sketched in Fig. 8.2.

[Image: A graph of potential energy V(R) versus separation R. V(R) is zero for R > a1+a2 and infinite for R <= a1+a2.]
**Fig. 8.2** The hard-sphere potential $V(R)$.

The impact parameter $b$ between two moving molecules is defined as the distance of closest approach that would result if the molecular trajectories were undeflected by the collision. Thus for a hard-sphere potential there is only a collision if the impact parameter $b< a_{1}+a_{2}$. Focus on one of these molecules (let's say the one with radius $a_{1}$ - This is depicted in Fig. 8.3). Now imagine molecules of the other type (with radius $a_{2}$) nearby. A collision will only take place if the centre of these other molecules comes inside a tube of radius $a_{1} + a_{2}$ (so that the molecule labelled A would not collide, whereas B and C would). Thus our first molecule can be considered to sweep out an imaginary tube of space of cross-sectional area $\pi (a_{1} + a_{2})^{2}$ that defines its "personal space". The area of this tube is called the collision cross-section $\sigma$ and is then given by

$$\sigma = \pi (a_1 + a_2)^2. \quad (8.13)$$

If $a_{1} = a_{2} = a$, then

$$\sigma = \pi d^2 \quad (8.14)$$

where $d = 2a$ is the molecular diameter.

[Image: A diagram showing a small molecule of radius a1 moving at velocity v. A tube of radius a1+a2 is swept out. Two other molecules A and B are shown. Molecule A is outside the tube and won't collide. Molecule B is inside the tube and will collide.]
**Fig. 8.3** A molecule sweeps out an imaginary tube of space of cross-sectional area $\sigma = \pi (a_{1} + a_{2})^{2}$. If the centre of another molecule enters this tube, there will be a collision.

Is the hard-sphere potential correct? It is a good approximation at lower temperatures, but progressively worsens as the temperature increases. Molecules are not really hard spheres but slightly squashy objects, and when they move at higher speeds and plough into each other with more momentum, you need more of a direct hit to cause a collision. Thus as the gas is warmed, the molecules may appear to have a smaller cross-sectional area.

===== Page 73 =====

## 8.3 The mean free path

Having derived the mean collision time, it is tempting to derive the mean free path as

$$\lambda = \langle v\rangle \tau = \frac{\langle v\rangle}{n\sigma v} \quad (8.15)$$

but what should we take as $v$? A first guess is to use $\langle v\rangle$, but that turns out to be not quite right. What has gone wrong?

Our approach to molecular scattering has been to focus on one molecule as the moving one, and think of all of the others as sitting ducks, fixed in space waiting patiently for a collision to occur. The reality is quite different: all molecules are whizzing around. We should therefore take $v$ as the average relative velocity, i.e., $\langle v_{\mathrm{r}}\rangle$, where

$$\mathbf{v}_{\mathrm{r}} = \mathbf{v}_{1} - \mathbf{v}_{2} \quad (8.16)$$

and $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ are the velocities of two molecules labelled 1 and 2. Now,

$$v_{\mathrm{r}}^{2} = v_{1}^{2} + v_{2}^{2} - 2v_{1}\cdot v_{2}, \quad (8.17)$$

so that

$$\langle v_{\mathrm{r}}^{2}\rangle = \langle v_{1}^{2}\rangle +\langle v_{2}^{2}\rangle = 2\langle v^{2}\rangle , \quad (8.18)$$

because $\langle \mathbf{v}_1\cdot \mathbf{v}_2\rangle = 0$ (which follows because $\langle \cos \theta \rangle = 0$). The quantity which we want is $\langle v_{\mathrm{r}}\rangle$, but what we have an expression for is $\langle v_{\mathrm{r}}^{2}\rangle$. If the probability distribution describing molecular speed is a Maxwell-Boltzmann distribution, then the error in writing $\langle v_{\mathrm{r}}\rangle \approx \sqrt{\langle v_{\mathrm{r}}^{2}\rangle}$ is small, so to a reasonable degree of approximation we can write

$$\langle v_{\mathrm{r}}\rangle \approx \sqrt{\langle v_{\mathrm{r}}^{2}\rangle}\approx \sqrt{2}\langle v\rangle \quad (8.19)$$

and hence we obtain an expression for $\lambda$ as follows:

$$\lambda = \frac{1}{\sqrt{2}n\sigma}. \quad (8.20)$$

Substitution of $p = n k_{\mathrm{B}}T$ yields the expression

$$\lambda = \frac{k_{\mathrm{B}}T}{\sqrt{2}p\sigma}. \quad (8.21)$$

To increase the mean free path by a certain factor, the pressure needs to be decreased by the same factor.

## Example 8.1

Calculate the mean free path for a gas of $\mathrm{N}_{2}$ at room temperature and pressure. (For $\mathrm{N}_{2}$, take the molecular diameter to be $d = 0.37 \mathrm{nm}$.)

Solution:

The collision cross-section is $\pi d^{2} = 4.3\times 10^{-19}\mathrm{m}^{2}$. We have $p\approx 10^{5}\mathrm{Pa}$ and $T\approx 300\mathrm{K}$ so the number density is $n = p / k_{\mathrm{B}}T\approx 10^{5} / (1.38\times 10^{-23}\times 300)\approx 2\times 10^{25}\mathrm{m}^{-3}$. This leads to $\lambda = 1 / (\sqrt{2} n\sigma) = 6.8\times 10^{-8}\mathrm{m}$.

Notice that both $\lambda$ and $\tau$ decrease with increasing pressure at fixed temperature. Thus the frequency of collisions increases with increasing pressure.

===== Page 74 =====

## Chapter summary

The mean scattering time is given by

$$\tau = \frac{1}{n\sigma\langle v_t\rangle},$$

where the collision cross-section is $\sigma = \pi d^2$, $d$ is the molecular diameter and $\langle v_t \rangle \approx \sqrt{2} \langle v \rangle$.

The mean free path is

$$\lambda = \frac{1}{\sqrt{2n\sigma}}.$$

## Exercises

(8.1) What is the mean free path of an $\mathrm{N}_2$ molecule in an ultra-high-vacuum chamber at a pressure of $10^{-10}$ mbar? What is the mean collision time? The chamber has a diameter of $0.5 \mathrm{m}$. On average, how many collisions will the molecule make with the chamber walls compared with collisions with other molecules? If the pressure is suddenly raised to $10^{-6}$ mbar, how do these results change?

(8.2) (a) Show that the root mean square free path is given by $\sqrt{2} \lambda$ where $\lambda$ is the mean free path.

(b) What is the most probable free path length?

(c) What percentage of molecules travel a distance greater than (i) $\lambda$ (ii) $2\lambda$ (iii) $5\lambda$?

(8.3) Show that particles hitting a plane boundary have travelled a distance $2\lambda /3$ perpendicular to the plane since their last collision, on average.

(8.4) A diffuse cloud of neutral hydrogen atoms in space has a temperature of $50 \mathrm{K}$ and number density $500 \mathrm{cm}^{-3}$. Estimate the mean scattering time (in years) between hydrogen atoms in the cloud. Estimate the mean free path (in astronomical units). (1 astronomical unit is the Earth-Sun distance; see Appendix A for a numerical value.)

===== Page 75 =====

# Part III

# Transport and thermal diffusion

In the third part of this book, we use our results from the kinetic theory of gases to derive various transport properties of gases and then apply this to solving the thermal diffusion equation. This part is structured as follows:

In Chapter 9, we use the intuition developed from considering molecular collisions and the mean free path to determine various transport properties, in particular viscosity, thermal conductivity, and diffusion. These correspond to the transport of momentum, heat, and particles respectively. In Chapter 10, we derive the thermal diffusion equation, which shows how heat is transported between regions of different temperature. This equation is a differential equation and can be applied to a variety of physical situations, and we show how to solve it in certain cases of high symmetry.

===== Page 76 =====

# 9 Transport properties in gases

9.1 Viscosity  76
9.2 Thermal conductivity  81
9.3 Diffusion  83
9.4 More detailed theory  86
Chapter summary  88
Further reading  88
Exercises  89

In this chapter, we wish to describe how a gas can transport momentum, energy, or particles from one place to another. The model we have used so far has been that of a gas in equilibrium, so that none of its macroscopic parameters are time-dependent. Now we consider non-equilibrium situations, but still in the steady state, i.e., so that the system parameters are time-independent, but the surroundings will be time-dependent. The phenomena we want to treat are called transport properties and we will consider

(1) Viscosity, which is the transport of momentum,
(2) Thermal conductivity, which is the transport of heat, and
(3) Diffusion, which is the transport of particles.

## 9.1 Viscosity

Viscosity is the measure of the resistance of a fluid to the deformation produced by a shear stress. For straight, parallel, and uniform flow, the shear stress between the layers is proportional to the velocity gradient in the direction perpendicular to the layers. The constant of proportionality, given the symbol $\eta$, is called the coefficient of viscosity, the dynamic viscosity, or simply the viscosity.

[Image: Two parallel plates separated by a fluid. The top plate moves with velocity u, the bottom is stationary. The velocity profile of the fluid in between is linear, with average velocity <u_x> increasing from bottom to top.]
**Fig. 9.1** A fluid is sandwiched between two plates of area $A$ which each lie in an $xy$ plane (see text).

Consider the scenario in Fig. 9.1 in which a fluid is sandwiched between two plates of area $A$, which each lie in the $xy$ plane. A shear stress $\tau_{xz} = F / A$ is applied to the fluid by sliding the top plate over it at speed $u$ while keeping the bottom plate stationary. A shear force $F$ is applied. A velocity gradient $\mathrm{d}\langle u_x\rangle /\mathrm{d}z$ is set up, so that $\langle u_x \rangle = 0$ near the bottom plate and $\langle u_x \rangle = u$ near the top plate. If the fluid is a gas, then this extra motion in the $x$-direction is superimposed on the Maxwell-Boltzmann motion in the $x$, $y$ and $z$ directions (and hence the use of the average $\langle u_x \rangle$, rather than $u_x$).

The viscosity $\eta$ is then defined by

$$\tau_{xz} = \frac{F}{A} = \eta \frac{\mathrm{d}\langle u_x\rangle}{\mathrm{d}z}. \quad (9.1)$$

The units of viscosity are $\mathrm{Pa s} (= \mathrm{N m}^{-2} \mathrm{s})$. Force is rate of change of momentum, and hence transverse momentum is being transported

===== Page 77 =====

through the fluid. This is achieved because molecules travelling in the $+z$ direction move from a layer in which $\langle u_{x}\rangle$ is smaller to one in which $\langle u_{x}\rangle$ is larger, and hence they transfer net momentum to that layer in the $-x$ direction. Molecules travelling parallel to $-z$ have the opposite effect. Hence, the shear stress $\tau_{xz}$ is equal to the transverse momentum transported across each square metre per second, and $\tau_{xz}$ is equal to a flux of momentum (though note that there must be a minus sign involved, because the momentum flux must be from regions of high transverse velocity to regions of low transverse velocity, which is in the opposite direction to the velocity gradient). The velocity gradient $\partial \langle u_{x}\rangle /\partial z$ therefore drives a momentum flux $\Pi_{z}$, according to

$$\Pi_{z} = -\eta \frac{\partial\langle u_{x}\rangle}{\partial z}. \quad (9.2)$$

The viscosity can be calculated using kinetic theory as follows:

Recall first that we showed before in eqn 6.13 that the number of molecules hitting unit area per second is $v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta$. Consider molecules travelling at an angle $\theta$ to the $z$-axis (see Fig. 9.2). Then molecules crossing a plane of constant $z$ will have travelled on average a distance $\lambda$ since their last collision, and so they will have travelled a distance $\lambda \cos \theta$ parallel to the $z$-axis since their last collision. Over that distance there is an average increase in $\langle u_{x}\rangle$ given by $(\partial \langle u_{x}\rangle /\partial z)\lambda \cos \theta$ so these upwards-travelling molecules bring an excess momentum in the $x$-direction given by

$$-m\left(\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\lambda \cos \theta . \quad (9.3)$$

Hence the total $x$-momentum transported across unit area perpendicular to $z$ in unit time is the momentum flux $\Pi_{z}$ given by

$$\begin{array}{rcl}\Pi_{z} & = & \int_{0}^{\infty}\int_{0}^{\pi}v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta \cdot m\left(-\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\lambda \cos \theta \\ & = & \frac{1}{2} nm\lambda \int_{0}^{\infty}v f(v)\mathrm{d}v\left(-\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\int_{0}^{\pi}\cos^{2}\theta \sin \theta \mathrm{d}\theta \\ & = & -\frac{1}{3} nm\lambda \langle v\rangle \left(\frac{\partial\langle u_{x}\rangle}{\partial z}\right). \end{array} \quad (9.4)$$

Hence the viscosity is given by

$$\eta = \frac{1}{3} nm\lambda \langle v\rangle . \quad (9.5)$$

Equation 9.5 has some important consequences.

- $\eta$ is independent of pressure.

Because $\lambda \approx 1 / (\sqrt{2} n\sigma)\propto n^{-1}$, the viscosity is independent of $n$ and hence (at constant temperature) it is independent of pressure. This is at first sight a weird result: as you increase the pressure, and hence $n$, you should be better at transmitting momentum

[Image: A diagram showing a molecule's velocity vector v at an angle theta to the z-axis. The molecule travels a mean free path lambda before crossing a plane. The distance travelled parallel to the z-axis is lambda cos theta.]
**Fig. 9.2** Molecular velocity $\mathbf{v}$ for molecules travelling at an angle $\theta$ to the $z$-axis. These will have travelled on average a distance $\lambda$ since their last collision, and so they will have travelled a distance $\lambda \cos \theta$ parallel to the $z$-axis since their last collision.

===== Page 78 =====

because you have more molecules to do it with. However, your mean free path reduces correspondingly, so that each molecule becomes less effective at transmitting momentum in such a way as to precisely cancel out the effect of having more of them. This result holds impressively well over quite a range of pressures (see Fig. 9.3) although it begins to fail at very low or very high pressures.

[Image: A graph of apparent viscosity of air versus pressure. The viscosity is roughly constant over a wide range of pressure, but shows deviations at very low and very high pressures.]
**Fig. 9.3** The apparent viscosity of air as a function of pressure at $288\mathrm{K}$. It is found to be constant over a wide range of pressure.

- $\eta \propto T^{1/2}$

Because $\eta$ is independent of $n$, the only temperature dependence is from $\langle v\rangle \propto T^{1/2}$, and hence $\eta \propto T^{1/2}$. Note therefore that the viscosity of gases increases with $T$, which is different for most liquids, which get runnier (i.e., less viscous) when you heat them.

Substituting in $\lambda = (\sqrt{2} n\sigma)^{-1}$, $\sigma = \pi d^2$ and $\langle v\rangle = (8k_{\mathrm{B}}T / \pi m)^{1/2}$ yields a more useful (though less memorable) expression for the viscosity:

$$\eta = \frac{2}{3\pi d^2}\left(\frac{mk_{\mathrm{B}}T}{\pi}\right)^{1 / 2}. \quad (9.6)$$

Equation 9.6 predicts that the viscosity will be proportional to $\sqrt{m} /d^2$ at constant temperature. This proportionality holds very well, as shown in Fig. 9.4.

[Image: A graph of viscosity at 300 K versus sqrt(m/m_p)/d^2 for various gases. The data points follow a linear trend. The dotted line is the prediction of simple kinetic theory, and the solid line is the prediction of a more detailed theory.]
**Fig. 9.4** The dependence of the viscosity of various gases on $\sqrt{m} /d^2$. The dotted line is the prediction of eqn 9.6. The solid line is the prediction of eqn 9.45.

Various approximations have gone into this approach, and a condition for their validity is that

$$L\gg \lambda \gg d, \quad (9.7)$$

where $L$ is the size of the container holding the gas and $d$ is the molecular diameter. We need $\lambda \gg d$ (pressure not too high) so that we can neglect collisions involving more than two particles. We need $\lambda \ll L$ (pressure not too low) so that molecules mainly collide with each other and not with the container walls. If $\lambda$ is of the

===== Page 79 =====

same order of magnitude or greater than $L$, most of a molecule's collisions will be with the container walls. Figure 9.3 indeed shows that the pressure-independence of the viscosity begins to break down when the pressure is too low or too high.

The factor of $\frac{1}{3}$ in eqn 9.5 is not quite right, so that eqn 9.6 leads to the dotted line in Fig. 9.4. To get a precise numerical factor, you need to consider the fact that the velocity distribution is different in different layers (because of the shear stress applied) and then average over the distribution of path lengths. This will be done in Section 9.4 and leads to a prediction that gives the solid line in Fig. 9.4.

[Image: A graph of viscosity versus T^(1/2) for Ne, He, and H2. The data follow a roughly linear trend, but show some deviation, indicating the T^(1/2) dependence is not exact.]
**Fig. 9.5** The temperature dependence of the viscosity of various gases. The agreement with the predicted $T^{1/2}$ behaviour is satisfactory as a first approximation, but not very good in detail.

The measured temperature dependence of the viscosity of various gases broadly agrees with our prediction that $\eta \propto \sqrt{T}$, as shown in Fig. 9.5, but the agreement is not quite perfect. The reason for this is that the collision cross-section, $\sigma = \pi d^{2}$, is actually temperature-dependent. At high temperatures, molecules move faster and hence have to collide more directly to have a proper momentum-randomizing collision. We have been assuming that molecules behave as perfect hard spheres and that any collision perfectly randomizes the molecular motion, but this is not precisely true. This means that the effective molecular diameter shrinks as you increase the temperature, increasing the viscosity over and above the expected $\sqrt{T}$ dependence. This is evident in the data presented in Fig. 9.5.

Viscosity can be measured by the damping of torsional oscillations in the apparatus shown in the box.

===== Page 80 =====

## Measurement of viscosity

Maxwell developed a method for measuring the viscosity of a gas by observing the damping rate of oscillations of a disc suspended from a fixed support by a torsion fibre.

[Image: (a) A diagram of Maxwell's method. An oscillating disc is suspended between two fixed horizontal discs. (b) A diagram of the rotating-cylinder method. An inner cylinder is suspended by a torsion fibre inside an outer rotating cylinder.]
**Fig. 9.6** Measuring viscosity by (a) Maxwell's method and (b) the rotating-cylinder method.

It is positioned halfway between two fixed horizontal discs and oscillates parallel to them in the gas. This is shown in Fig. 9.6(a) with the fixed horizontal discs shaded and the oscillating disc in white. The damping of the torsional oscillations is from the viscous damping due to the gas trapped on each side of the oscillating disc between the fixed discs. The fixed discs are mounted inside a vacuum chamber in which the composition and pressure of the gas to be measured can be varied.

A very accurate method is the rotating-cylinder method, in which gas is confined between two vertical coaxial cylinders. It is shown in Fig. 9.6(b). The outer cylinder (inner radius $b$) is rotated by a motor at a constant angular speed $\omega_{0}$ while the inner cylinder (outer radius $a$) is suspended by a torsion fibre from a fixed support. The torque $G$ on the outer cylinder is transmitted via the gas to the inner cylinder and a resulting torque on the torsion fibre. The velocity gradient $u(r)$ is related to the angular velocity $\omega (r)$ by $u(r) = r\omega (r)$ and we expect that $\omega$ varies all the way from 0 at $r = a$ to $\omega_{0}$ at $r = b$. The velocity gradient is thus

$$\frac{\mathrm{d}u}{\mathrm{d}r} = \omega +r\frac{\mathrm{d}\omega}{\mathrm{d}r}, \quad (9.8)$$

but the first term on the right-hand side simply corresponds to the velocity gradient due to rigid rotation and does not contribute to the viscous shearing stress, which is thus $\eta \mathrm{rd}\omega /\mathrm{d}r$. The force $F$ on a cylindrical element of gas (of length $l$) is then just this viscous stress multiplied by the area of the cylinder $2\pi r l$, i.e.,

$$F = 2\pi r l\eta \times r\frac{\mathrm{d}\omega}{\mathrm{d}r}, \quad (9.9)$$

and so the torque $G = rF$ on this cylindrical element is

$$G = 2\pi r^{3}l\eta \frac{\mathrm{d}\omega}{\mathrm{d}r}. \quad (9.10)$$

In the steady state, there is no change in viscous torque from the outer to the inner cylinder (if there were, angular acceleration would be induced somewhere and the system would change) so this torque is transmitted to the suspended cylinder. Hence rearranging and integrating give

$$G\int_{a}^{b}\frac{\mathrm{d}r}{r^{3}} = 2\pi l\eta \int_{0}^{\omega_{0}}\mathrm{d}\omega = 2\pi l\eta \omega_{0}, \quad (9.11)$$

so that

$$\eta = \frac{G}{4\pi\omega l}\left(\frac{1}{a^2} -\frac{1}{b^2}\right). \quad (9.12)$$

The torque $G$ is related to the angular deflection $\phi$ of the inner cylinder by $G = \alpha \phi$. The angular deflection can be measured using a light beam reflected from a small mirror attached to the torsion fibre. The coefficient $\alpha$ is known as the torsion constant. This can be found by measuring the period $T$ of torsional oscillations of an object of moment of inertia $I$ suspended from the wire, which is

$$T = 2\pi \sqrt{\frac{I}{\alpha}}. \quad (9.13)$$

Knowledge of $I$ and $T$ yields $\alpha$ which can be used with the measured $\phi$ to obtain $G$ and hence $\eta$.

===== Page 81 =====

## 9.2 Thermal conductivity

We have defined heat as "thermal energy in transit". It quantifies the transfer of energy in response to a temperature gradient. The amount of heat that flows along a temperature gradient depends on the thermal conductivity of the material, which we will now define.

Thermal conductivity can be considered in one dimension using the diagram shown in Fig. 9.7. Heat flows from hot to cold, and so flows against the temperature gradient. The flow of heat can be described by a heat flux vector $J$, whose direction lies along the direction of flow of heat and whose magnitude is equal to the heat energy flowing per unit time per unit area (measured in $\mathrm{J s^{-1}m^{-2} = W m^{-2}}$). The heat flux $J_{z}$ in the $z$-direction is given by

$$J_{z} = -\kappa \left(\frac{\partial T}{\partial z}\right), \quad (9.14)$$

where the negative sign is because heat flows "downhill". The constant $\kappa$ is called the thermal conductivity of the gas. In general, in three dimensions we can write that the heat flux $J$ is related to temperature using

$$J = -\kappa \nabla T. \quad (9.15)$$

How do molecules in a gas "carry" heat? Gas molecules have energy, and as we found in eqn 5.17 their mean translational kinetic energy $\langle \frac{1}{2} mv^2\rangle = \frac{3}{2} k_{\mathrm{B}}T$ depends on the temperature. Therefore to increase the temperature of a gas by $1\mathrm{K}$, one has to increase the mean kinetic energy by $\frac{3}{2} k_{\mathrm{B}}$ per molecule. The heat capacity $C$ of the gas is the heat required to increase the temperature of gas by $1\mathrm{K}$. The heat capacity $C_{\mathrm{molecule}}$ of a gas molecule is therefore equal to $\frac{3}{2} k_{\mathrm{B}}$, though we will later see that it can be larger than this if the molecule can store energy in forms other than translational kinetic energy.

The derivation of the thermal conductivity of a gas is very similar to that for viscosity. Consider molecules travelling along the $z$-axis. Then molecules crossing a plane of constant $z$ will have travelled on average a distance $\lambda$ since their last collision, and so they will have travelled a distance $\lambda \cos \theta$ parallel to the $z$-axis since their last collision. Therefore they bring a deficit of thermal energy given by

$$C_{\mathrm{molecule}}\times \Delta T = C_{\mathrm{molecule}}\frac{\partial T}{\partial z}\lambda \cos \theta , \quad (9.16)$$

where $C_{\mathrm{molecule}}$ is the heat capacity of a single molecule. Hence the total thermal energy transported across unit area in unit time, i.e., the heat flux, is given by

$$\begin{array}{rcl}{J_z} & = & {\int_0^\infty \mathrm{d}v\int_0^\pi \left(-C_{\mathrm{molecule}}\frac{\partial T}{\partial z}\lambda \cos \theta\right)v\cos \theta nf(v)\frac{1}{2}\sin \theta \mathrm{d}\theta}\\ {} & = & {-\frac{1}{2} nC_{\mathrm{molecule}}\lambda \int_0^\infty vf(v)\mathrm{d}v\frac{\partial T}{\partial z}\int_0^\pi \cos^2\theta \sin \theta \mathrm{d}\theta}\\ {} & = & {-\frac{1}{3} nC_{\mathrm{molecule}}\lambda \langle v\rangle \frac{\partial T}{\partial z}.} \end{array} \quad (9.17)$$

[Image: A diagram showing two horizontal lines at temperatures T2 (top) and T1 (bottom), with T1 > T2. An arrow labelled Jz points upwards, opposite to the temperature gradient vector.]
**Fig. 9.7** Heat flows in the opposite direction to the temperature gradient.

===== Page 82 =====

Hence the thermal conductivity $\kappa$ is given by

$$\kappa = \frac{1}{3} C_V\lambda \langle v\rangle , \quad (9.18)$$

where $C_V = nC_{\mathrm{molecule}}$ is the heat capacity per unit volume (though the subscript $V$ here refers to a temperature change at constant volume). Equation 9.18 has some important consequences.

[Image: A graph of thermal conductivity versus T^(1/2) for He, Ne, and Ar. The data follow a roughly linear trend.]
**Fig. 9.8** The thermal conductivity of various gases as a function of temperature. The agreement with the predicted $T^{1/2}$ behaviour is satisfactory as a first approximation, but not very good in detail.

[Image: A graph of thermal conductivity versus 1/(sqrt(m)d^2) for various gases. The data follow a linear trend for noble gases, but N2 deviates slightly.]
**Fig. 9.9** The dependence of the thermal conductivity of various gases on $1 / (\sqrt{m} d^2)$. The dotted line is the prediction of eqn 9.19. The solid line is the prediction of eqn 9.46, which works very well for the monatomic noble gases, but a little less well for diatomic $\mathrm{N}_2$.

- $\kappa$ is independent of pressure. The argument is the same as for $\eta$. Because $\lambda \approx 1 / (\sqrt{2} n\sigma)\propto n^{-1}$, $\kappa$ is independent of $n$ and hence (at constant temperature) it is independent of pressure.
- $\kappa \propto T^{1/2}$. The argument is also the same as for $\eta$. Because $\kappa$ is independent of $n$, the only temperature dependence is from $\langle v\rangle \propto \sqrt{T}$, and hence $\eta \propto T^{1/2}$. This holds quite well for a number of gases (see Fig. 9.8). As for viscosity, substituting in $\lambda = (\sqrt{2} n\sigma)^{-1}$, $\sigma = \pi d^2$ and $\langle v\rangle = (8k_{\mathrm{B}}T / \pi m)^{1/2}$ yields a more useful (though less memorable) expression for the thermal conductivity:

$$\kappa = \frac{2}{3\pi d^2} C_{\mathrm{molecule}}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1/2}. \quad (9.19)$$

$L\gg \lambda \gg d$ is again the relevant condition for our treatment to hold. Equation 9.19 predicts that the thermal conductivity will be proportional to $1 / (\sqrt{m} d^2)$ at constant temperature. This holds very well, as shown in Fig. 9.9. Thermal conductivity can be measured by various techniques; see the box.

The similarity of $\eta$ and $\kappa$ would suggest that

$$\frac{\kappa}{\eta} = \frac{C_{\mathrm{molecule}}}{m}. \quad (9.20)$$

The ratio $C_{\mathrm{molecule}} / m$ is the specific heat capacity $c_{\mathrm{V}}$ (the subscript $V$ indicating a measurement at constant volume), so equivalently

$$\kappa = c_{\mathrm{V}}\eta . \quad (9.21)$$

However, neither of these relations hold too well. Faster molecules cross a given plane more often than slow ones. These carry more kinetic energy and therefore do carry more heat. However, they don't necessarily carry more average momentum in the $x$-direction. We will return to this point in Section 9.4.

===== Page 83 =====

## Measurement of thermal conductivity

The thermal conductivity $\kappa$ can be measured using the hot-wire method. Gas fills the space between two coaxial cylinders (inner cylinder radius $a$, outer cylinder radius $b$ as shown in Fig. 9.10).

[Image: A diagram of the hot-wire method. An inner cylinder of radius a at temperature Ta is inside an outer cylinder of radius b at temperature Tb. The space between them is filled with gas.]
**Fig. 9.10** The hot-wire method for measuring thermal conductivity.

The outer cylinder is connected to a constant-temperature bath of temperature $T_{b}$ while heat is generated in the inner cylinder (the hot wire) at rate $Q$ per unit length of the cylinder (measured in units of $\mathrm{Wm^{-1}}$). The temperature of the inner cylinder rises to $T_{a}$. The rate $Q$ can be connected with the radial heat flux $J_{r}$ using

$$Q = 2\pi rJ_{r}, \quad (9.22)$$

and $J_{r}$ itself is given by $- \kappa \partial T / \partial r$ as in eqn 9.14. Hence

$$Q = -2\pi r\kappa \left(\frac{\partial T}{\partial r}\right), \quad (9.23)$$

and rearranging and integrating yields

$$Q\int_{a}^{b}\frac{\mathrm{d}r}{r} = -2\pi \kappa \int_{T_{a}}^{T_{b}}\mathrm{d}T, \quad (9.24)$$

and hence

$$\kappa = \frac{Q}{2\pi}\frac{\ln b / a}{T_a - T_b}. \quad (9.25)$$

Since $Q$ is known (it is the power supplied to heat the inner cylinder) and $T_{a}$ and $T_{b}$ can be measured, the value of $\kappa$ can be deduced.

An important application of this technique is in the Pirani gauge, which is commonly used in vacuum systems to measure pressure. A sensor wire is heated electrically, and the pressure of the gas is determined by measuring the current needed to keep the wire at a constant temperature. (The resistance of the wire is temperature dependent, so the temperature is estimated by measuring the resistance of the wire.) The Pirani gauge thus relies on the fact that at low pressure the thermal conductivity is a function of pressure (since the condition $\lambda \ll L$, where $L$ is a linear dimension in the gauge, is not met). In fact, a typical Pirani gauge will not work to detect pressures much above 1 mbar because, above these pressures, the thermal conductivity of the gases no longer changes with pressure. The thermal conductivity of each gas is different, so the gauge has to be calibrated for the individual gas being measured.

## 9.3 Diffusion

Consider a distribution of similar molecules, some of which are labelled (e.g., by being radioactive). Let there be $n^{*}(z)$ of these labelled molecules per unit volume, but note that $n^{*}$ is allowed to be a function of the $z$ coordinate. The flux $\Phi_{z}$ of labelled molecules parallel to the $z$-direction (measured in $\mathrm{m}^{-2}\mathrm{s}^{-1}$) is

$$\Phi_{z} = -D\left(\frac{\partial n^{*}}{\partial z}\right), \quad (9.26)$$

where $D$ is the coefficient of self-diffusion. Now consider a thin slab of gas of thickness dz and area $A$ as shown in Fig. 9.11. The flux into the slab is

$$A\Phi_{z}, \quad (9.27)$$

===== Page 84 =====

and the flux out of the slab is

$$A\left(\Phi_{z} + \frac{\partial\Phi_{z}}{\partial z}\mathrm{d}z\right). \quad (9.28)$$

[Image: A diagram of a thin slab of gas of thickness dz and area A. An upward arrow shows the flux into the slab, A Phi_z. A downward arrow shows the flux out of the slab, A [Phi_z + (dPhi_z/dz) dz]. The number of particles in the slab is A n* dz.]
**Fig. 9.11** The fluxes into and out of a thin slab of gas of thickness $\mathrm{d}z$ and area $A$.

The difference in these two fluxes must be balanced by the time-dependent changes in the number of labelled particles inside the region. Hence

$$\frac{\partial}{\partial t} (n^{*}A\mathrm{d}z) = -A\frac{\partial\Phi_{z}}{\partial z}\mathrm{d}z, \quad (9.29)$$

so that

$$\frac{\partial n^{*}}{\partial t} = -\frac{\partial\Phi_{z}}{\partial z}, \quad (9.30)$$

and hence that

$$\frac{\partial n^{*}}{\partial t} = D\frac{\partial^{2}n^{*}}{\partial z^{2}}. \quad (9.31)$$

This is the diffusion equation. A derivation of the diffusion equation in three dimensions is shown in the box.

## Three-dimensional derivation of the diffusion equation

The total number of labelled particles that flow out of a closed surface $S$ is given by the integral

$$\int_{S}\Phi \cdot \mathrm{d}S, \quad (9.32)$$

and this must be balanced by the rate of decrease of labelled particles inside the volume $V$ surrounded by $S$, i.e.,

$$\int_{S}\Phi \cdot \mathrm{d}S = -\frac{\partial}{\partial t}\int_{V}n^{*}\mathrm{d}V. \quad (9.33)$$

The divergence theorem implies that

$$\int_{S}\Phi \cdot \mathrm{d}S = \int_{V}\nabla \cdot \Phi \mathrm{d}V, \quad (9.34)$$

and hence that

$$\nabla \cdot \Phi = -\frac{\partial n^{*}}{\partial t}. \quad (9.35)$$

Substituting in $\Phi = - D\nabla n^{*}$ then yields the diffusion equation, which is

$$\frac{\partial n^{*}}{\partial t} = D\nabla^{2}n^{*}. \quad (9.36)$$

A kinetic theory derivation of $D$ proceeds as follows. The excess labelled molecules hitting unit area per second is

$$\begin{array}{rcl}{\Phi_z} & = & {\int_0^\pi \mathrm{d}\theta \int_0^\infty \mathrm{d}v v\cos \theta f(v)\frac{1}{2}\sin \theta \left(-\frac{\partial n^*}{\partial z}\lambda \cos \theta\right)}\\ {} & = & {-\frac{1}{3}\lambda \langle v\rangle \frac{\partial n^*}{\partial z},} \end{array} \quad (9.37)$$

===== Page 85 =====

and hence

$$D = \frac{1}{3}\lambda \langle v\rangle . \quad (9.38)$$

This equation has some important implications:

- $D\propto p^{-1}$ In this case, there is no factor of $n$, but $\lambda \propto 1 / n$ and hence $D\propto n^{-1}$ and at fixed temperature $D\propto p^{-1}$ (this holds quite well experimentally, see Fig. 9.12).
- $D\propto T^{3/2}$ Because $p = nk_{\mathrm{B}}T$ and $\langle v\rangle \propto T^{1/2}$, we have that $D\propto T^{3/2}$ at fixed pressure.
- $D\rho = \eta$ The only difference between the formula for $D$ and that for $\eta$ is a factor of $\rho = nm$, and so

$$D\rho = \eta . \quad (9.39)$$

- $D\propto m^{-1/2}d^{-2}$, which is the same dependence as thermal conductivity.

The less memorable formula for $D$ is, as before, obtained by substituting in the expressions for $\langle v\rangle$ and $\lambda$, yielding

$$D = \frac{2}{3\pi nd^2}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}. \quad (9.40)$$

[Image: Two graphs showing diffusion constant D versus pressure. The left graph shows D versus p, with a curve decaying as 1/p. The right graph shows D versus 1/p, with a linear trend.]
**Fig. 9.12** Diffusion as a function of pressure.

This section has been about self-diffusion, where labelled atoms (or molecules) diffuse amongst unlabelled, but otherwise identical, atoms (or molecules). Experimentally, it is easier to measure the diffusion of atoms (or molecules) of one type (call them type 1, mass $m_{1}$, diameter $d_{1}$) amongst atoms (or molecules) of another type (call them type 2, mass $m_{2}$, diameter $d_{2}$). In this case the diffusion constant $D_{12}$ is used which is given by eqn 9.40 with $d$ replaced by $(d_{1} + d_{2}) / 2$ and $m$ replaced by $2m_{1}m_{2} / (m_{1} + m_{2})$, so that

$$D_{12} = \frac{2}{3\pi n(\frac{1}{2}[d_1 + d_2])^2}\left(\frac{k_{\mathrm{B}}T(m_1 + m_2)}{2\pi m_1m_2}\right)^{1 / 2}. \quad (9.41)$$

===== Page 86 =====

## 9.4 More detailed theory

The treatment of the transport properties presented so far in this chapter has the merit that it allows one to get the basic dependences fairly straightforwardly, and gives good insight as to what is going on. However, some of the details of the predictions are not in complete agreement with experiment and it is the purpose of this section to offer a critique of this approach and see how things might be improved. This section contains more advanced material than considered in the rest of this chapter and can be skipped at first reading.

One effect, which we have ignored, is the persistence of velocity after a collision. Our assumption has been that following a collision, a molecule's velocity becomes completely randomized and is completely uncorrelated with its velocity before the collision. However, although that is the simplest approximation to take, it is not correct. After most collisions, a molecule will retain some component of its velocity in the direction of its original motion. Moreover, our treatment has implicitly assumed a Maxwellian distribution of molecular velocities and that the different components of $\mathbf{v}$ are uncorrelated with each other, so that they can be considered to be independent random variables. However, these components are actually partially correlated with each other and so are not independent random variables.

A further effect which becomes important at low pressure is the presence of boundaries; the details of the collisions of molecules with walls of a container can be quite important, and such collisions become more important as the pressure is reduced so that the mean free path increases.

Yet another consideration is the interconversion between the internal energy of a molecule and its translational degrees of freedom. As we will see in later chapters, the heat capacity of a molecule contains terms not only due to its translational motion ( $C_{\mathrm{molecule}} = \frac{3}{2} k_{\mathrm{B}}$ ) but also due to its rotational and vibrational degrees of freedom. Collisions can give rise to processes where a molecule's energy can be redistributed throughout these different degrees of freedom. Thus if the molar heat capacity $C_{V}$ can be written as the sum of two terms, $C_{V} = C_{V}^{\prime} + C_{V}^{\prime \prime}$, where $C_{V}^{\prime}$ is due to translational degrees of freedom and $C_{V}^{\prime \prime}$ is due to other degrees of freedom, then it turns out that eqn 9.21 should be amended to give

$$\kappa = \left(\frac{5}{2} C_{V}^{\prime} + C_{V}^{\prime \prime}\right)\eta . \quad (9.42)$$

The $\frac{5}{2}$ factor reflects the correlations that exist between momentum, energy, and translational motion. The most energetic molecules are the most rapid and therefore possess longer mean free paths. This leads to Eucken's formula, which states that

$$\kappa = \frac{1}{4} (9\gamma -5)\eta C_{V}. \quad (9.43)$$

For an ideal monatomic gas $\gamma = \frac{5}{3}$ and hence

$$\kappa = \frac{5}{2}\eta C_{V}, \quad (9.44)$$

===== Page 87 =====

which supersedes eqn 9.21.

A more accurate treatment of the effects mentioned in this section has been performed by Chapman and Enskog (in the twentieth century); the methods used go beyond the scope of this text, but we summarize the results.

The viscosity, which was written as $\eta = (2 / 3\pi d^2)(mk_B T / \pi)^{1 / 2}$ in eqn 9.6, should be replaced by

$$\eta = \frac{5}{16}\frac{1}{d^2}\left(\frac{mk_B T}{\pi}\right)^{1 / 2}, \quad (9.45)$$

i.e., the $2 / 3\pi$ should be replaced by $5 / 16$.

The corrected formula for $\kappa$ (which we had evaluated in eqn 9.19) can be obtained from this expression of $\eta$ using Eucken's formula, eqn 9.43, and hence reads

$$\kappa = \frac{25}{32d^2} C_{\mathrm{molecule}}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}, \quad (9.46)$$

i.e., the $2 / 3\pi$ should be replaced by $25 / 32$.

The formula for $D$, which appears in eqn 9.40, should now be replaced by

$$D = \frac{3}{8}\frac{1}{nd^2}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}, \quad (9.47)$$

i.e., the $2 / 3\pi$ should be replaced by $3 / 8$. Similarly, eqn 9.41 should be replaced by

$$D = \frac{3}{8n(\frac{1}{2}[d_1 + d_2])^2}\left(\frac{k_{\mathrm{B}}T(m_1 + m_2)}{2\pi m_1m_2}\right)^{1 / 2}. \quad (9.48)$$

This also alters other conclusions, such as eqn 9.39, which becomes

$$D\rho = \frac{\frac{3}{3}\eta}{\frac{5}{16}} = \frac{6\eta}{5}. \quad (9.49)$$

===== Page 88 =====

## Chapter summary

Viscosity, $\eta$, defined by $\Pi_{z} = - \eta \partial \langle u_{x} \rangle / \partial z$ is (approximately)

$$\eta = \frac{1}{3} nm\lambda \langle v \rangle .$$

Thermal conductivity, $\kappa$, defined by $J_{z} = - \kappa \partial T / \partial z$ is (approximately)

$$\kappa = \frac{1}{3} C_{V}\lambda \langle v \rangle .$$

Diffusion, $D$, defined by $\Phi_{z} = - D\partial n^{*} / \partial z$ is (approximately)

$$D = \frac{1}{3}\lambda \langle v \rangle .$$

These relationships assume that

$$L\gg \lambda \gg d.$$

The results of a more detailed theory have been summarized (and serve only to alter the numerical factors at the start of each equation).

The predicted pressure, temperature, molecular mass and molecular diameter dependences are:

| | $\eta$ | $\kappa$ | $D$ |
| :--- | :--- | :--- | :--- |
| $p$ | $\propto p^0$ | $\propto p^0$ | $\propto p^{-1}$ |
| $T$ | $\propto T^{1/2}$ | $\propto T^{1/2}$ | $\propto T^{3/2}$ |
| $m$ | $\propto m^{1/2}d^{-2}$ | $\propto m^{-1/2}d^{-2}$ | $\propto m^{-1/2}d^{-2}$ |

(In this table, $\propto p^{0}$ means independent of pressure.)

## Further reading

Chapman and Cowling (1970) is the classic treatise describing the more advanced treatment of transport properties in gases.

===== Page 89 =====

## Exercises

(9.1) Is air more viscous than water? Compare the dynamic viscosity $\eta$ and the kinematic viscosity $\nu = \eta /\rho$ using the following data:

| | $\rho$ (kg m$^{-3}$) | $\eta$ (Pa s) |
| :--- | :--- | :--- |
| Air | 1.31 | $17.4\times10^{-6}$ |
| Water | 1000 | $1.0\times10^{-3}$ |

(9.2) Obtain an expression for the thermal conductivity of a gas at ordinary pressures. The thermal conductivity of argon (atomic weight 40) at STP is $1.6 \times 10^{-2} \mathrm{Wm}^{-1} \mathrm{K}^{-1}$. Use this to calculate the mean free path in argon at STP. Express the mean free path in terms of an effective atomic radius for collisions and find the value of this radius. Solid argon has a close-packed cubic structure in which, if the atoms are regarded as hard spheres, 0.74 of the volume of the structure is filled. The density of solid argon is $1.6 \times 10^{3} \mathrm{kg m}^{-3}$. Compare the effective atomic radius obtained from this information with your effective collision radius. Comment on your result.

(9.3) Define the coefficient of viscosity. Use kinetic theory to show that the coefficient of viscosity of a gas is given, with suitable approximations, by

$$\eta = K\rho \langle c\rangle \lambda$$

where $\rho$ is the density of the gas, $\lambda$ is the mean free path of the gas molecules, $\langle c \rangle$ is their mean speed, and $K$ is a number that depends on the approximations you make.

In 1660 Boyle set up a pendulum inside a vessel that was attached to a pump that could remove air from the vessel. He was surprised to find that there was no observable change in the rate of damping of the swings of the pendulum when the pump was set going. Explain his observation in terms of the above formula.

Make a rough order-of-magnitude estimate of the lower limit to the pressure that Boyle obtained; use reasonable assumptions concerning the apparatus that Boyle might have used. [The viscosity of air at atmospheric pressure and at $293 \mathrm{K}$ is $18.2 \mu \mathrm{N} \mathrm{s} \mathrm{m}^{-2}$.]

Explain why the damping is nearly independent of pressure despite the fact that fewer molecules collide with the pendulum as the pressure is reduced.

(9.4) Two plane discs, each of radius $5 \mathrm{cm}$ are mounted coaxially with their adjacent surfaces $1 \mathrm{mm}$ apart. They are in a chamber containing Ar gas at STP (viscosity $2.1 \times 10^{-5} \mathrm{Ns} \mathrm{m}^{-2}$) and are free to rotate about their common axis. One of them rotates with an angular velocity of $10 \mathrm{rad} \mathrm{s}^{-1}$. Find the torque that must be applied to the other to keep it stationary.

(9.5) Measurements of the viscosity, $\eta$ of argon gas $(^{40}\mathrm{Ar})$ over a range of pressures yield the following results at two temperatures:

$$\mathrm{at} 500\mathrm{K}\quad \eta \approx 3.5\times10^{-5}\mathrm{kg}\mathrm{m}^{-1}\mathrm{s}^{-1};$$
$$\mathrm{at} 2000\mathrm{K}\quad \eta \approx 8.0\times10^{-5}\mathrm{kg}\mathrm{m}^{-1}\mathrm{s}^{-1}.$$

The viscosity is found to be approximately independent of pressure. Discuss the extent to which these data are consistent with (i) simple kinetic theory, and (ii) the diameter of the argon atom (0.34 nm) deduced from the density of solid argon at low temperatures.

(9.6) In Section 11.3, we will define the ratio of $C_{p}$ to $C_{V}$ as given by the number $\gamma$. We will also show that $C_{p} = C_{V} + R$, where the heat capacities here are per mole. Show that these definitions lead to

$$C_{V} = \frac{R}{(\gamma - 1)}. \quad (9.50)$$

Starting with the formulae $C_{V} = C_{V}^{\prime} + C_{V}^{\prime \prime}$ and $\kappa = \left(\frac{5}{2} C_{V}^{\prime} + C_{V}^{\prime \prime}\right)\eta$, show that if $C_{V}^{\prime} / R = \frac{3}{2}$, then

$$\kappa = \frac{1}{4} (9\gamma -5)\eta C_{V}, \quad (9.51)$$

which is Eucken's formula. Deduce the value of $\gamma$ for each of the following monatomic gases measured at room temperatures.

| Species | $\kappa/(\eta C_V)$ |
| :--- | :--- |
| He | 2.45 |
| Ne | 2.52 |
| Ar | 2.48 |
| Kr | 2.54 |
| Xe | 2.58 |

Deduce what proportion of the heat capacity of the molecules is associated with the translational degrees of freedom for these gases. (Hint: notice the word "monatomic".)

===== Page 90 =====

# 10 The thermal diffusion equation

10.1 Derivation of the thermal diffusion equation  90
10.2 The one-dimensional thermal diffusion equation  91
10.3 The steady state  94
10.4 The thermal diffusion equation for a sphere  94
10.5 Newton's law of cooling  99
10.6 The Prandtl number  100
10.7 Sources of heat  101
10.8 Particle diffusion  102
Chapter summary  103
Exercises  103

This section assumes familiarity with solving differential equations (see, e.g., Boas (1983), Riley et al. (2006)). It can be omitted at first reading.

[Image: A closed surface S encloses a volume V. Arrows labelled J point outward from the surface, representing heat flux.]
**Fig. 10.1** A closed surface $S$ encloses a volume $V$. The total heat flow out of $S$ is given by $\int_{S} \mathbf{J} \cdot \mathrm{d} \mathbf{S}$.

In the previous chapter, we have seen how the thermal conductivity of a gas can be calculated using kinetic theory. In this chapter, we look at solving problems involving the thermal conductivity of matter using a technique developed by mathematicians in the late eighteenth and early nineteenth centuries. The key equation describes thermal diffusion, i.e., how heat appears to "diffuse" from one place to the other, and most of this chapter introduces techniques for solving this equation.

## 10.1 Derivation of the thermal diffusion equation

Recall from eqn 9.15 that the heat flux $J$ is given by

$$\mathbf{J} = -\kappa \nabla T. \quad (10.1)$$

This equation is very similar mathematically to the equation for particle flux $\Phi$ in eqn 9.26 which is, in three dimensions,

$$\Phi = -D\nabla n, \quad (10.2)$$

where $D$ is the diffusion constant, and also to the flow of electrical current given by the current density $\mathbf{J}_{e}$ defined by

$$\mathbf{J}_{e} = \sigma \mathbf{E} = -\sigma \nabla \phi , \quad (10.3)$$

where $\sigma$ is the conductivity, $\mathbf{E}$ is the electric field and $\phi$ here is the electric potential. Because of this mathematical similarity, an equation that is analogous to the diffusion equation (eqn 9.36) holds in each case. We will derive the thermal diffusion equation in this section.

In fact in all these phenomena, there needs to be some account of the fact that you can't destroy energy, or particles, or charge. (We will only treat the thermal case here.) The total heat flow out of a closed surface $S$ (as in Fig. 10.1) is given by the integral

$$\int_{S} \mathbf{J} \cdot \mathrm{d} \mathbf{S}, \quad (10.4)$$

and is a quantity with the dimension of power. It is therefore equal to the rate which the material inside the surface is losing energy. This can

===== Page 91 =====

be expressed as the rate of change of the total thermal energy inside the volume $V$ surrounded by the closed surface $S$. The thermal energy can be written as the volume integral $\int_{V}CT\mathrm{d}V$, where $C$ here is the heat capacity per unit volume (measured in $\mathrm{JK}^{-1}\mathrm{m}^{-3}$) and is equal to $\rho c$, where $\rho$ is the density and $c$ is the heat capacity per unit mass (the specific heat capacity, see Section 2.2). Hence

$$\int_{S}\mathbf{J}\cdot \mathrm{d}\mathbf{S} = -\frac{\partial}{\partial t}\int_{V}CT\mathrm{d}V. \quad (10.5)$$

We haven't worried about what the "zero" of thermal energy is; there could also be an additive, time-independent, constant in the expression for total thermal energy, but since we are going to differentiate this with respect to time to obtain the rate of change of thermal energy, it doesn't matter.

The divergence theorem implies that

$$\int_{S}\mathbf{J}\cdot \mathrm{d}\mathbf{S} = \int_{V}\nabla \cdot \mathbf{J}\mathrm{d}V, \quad (10.6)$$

and hence that

$$\nabla \cdot \mathbf{J} = -C\frac{\partial T}{\partial t}. \quad (10.7)$$

Substituting in eqn 10.1 then yields the thermal diffusion equation which is

$$\frac{\partial T}{\partial t} = D\nabla^2 T, \quad (10.8)$$

where $D = \kappa /C$ is the thermal diffusivity. Since $\kappa$ has units $\mathrm{Wm}^{-1}\mathrm{K}^{-1}$ and $C = \rho c$ has units $\mathrm{JK}^{-1}\mathrm{m}^{-3}$, $D$ has units $\mathrm{m}^2\mathrm{s}^{-1}$.

## 10.2 The one-dimensional thermal diffusion equation

In one dimension, this equation becomes

$$\frac{\partial T}{\partial t} = D\frac{\partial^2T}{\partial x^2}, \quad (10.9)$$

and can be solved using conventional methods.

## Example 10.1

Solution of the one-dimensional thermal diffusion equation

The one-dimensional thermal diffusion equation looks a bit like a wave equation. Therefore, one method to solve eqn 10.9 is to look for wave-like solutions of the form

$$T(x,t)\propto \exp (\mathrm{i}(kx - \omega t)), \quad (10.10)$$

where $k = 2\pi /\lambda$ is the wave vector, $\omega = 2\pi f$ is the angular frequency, $\lambda$ is the wavelength and $f$ is the frequency. Substitution of this equation into eqn 10.9 yields

$$-\mathrm{i}\omega = -Dk^2 \quad (10.11)$$

===== Page 92 =====

and hence

$$k^{2} = \frac{\mathrm{i}\omega}{D} \quad (10.12)$$

so that

$$k = \pm (1 + \mathrm{i})\sqrt{\frac{\omega}{2D}}. \quad (10.13)$$

The spatial part of the wave, which looks like $\exp (\mathrm{i}k x)$, can either be of the form

$$\exp \left((\mathrm{i} - 1)\sqrt{\frac{\omega}{2D}} x\right), \quad \text{which blows up as } x \to -\infty , \quad (10.14)$$

or

$$\exp \left((-\mathrm{i} + 1)\sqrt{\frac{\omega}{2D}} x\right), \quad \text{which blows up as } x \to \infty . \quad (10.15)$$

Let us now solve a problem in which a boundary condition is applied at $x = 0$ and a solution is desired in the region $x > 0$. We don't want solutions that blow up as $x \to \infty$ and pick the first type of solution (i.e., eqn 10.14). Hence our general solution for $x \geq 0$ can be written as

$$T(x,t) = \sum_{\omega}A(\omega)\exp (-\mathrm{i}\omega t)\exp \left((\mathrm{i} - 1)\sqrt{\frac{\omega}{2D}} x\right), \quad (10.16)$$

where we have summed over all possible frequencies. To find which frequencies are needed, we have to be specific about the boundary condition for which we want to solve.

Let us imagine that we want to solve the one-dimensional problem of the propagation of sinusoidal temperature waves into the ground. The waves could be due to the alternation of day and night (for a wave with period 1 day), or winter and summer (for a wave with period 1 year). The boundary condition can be written as

$$T(0,t) = T_0 + \Delta T\cos \Omega t. \quad (10.17)$$

This boundary condition can be rewritten

$$T(0,t) = T_0 + \frac{\Delta T}{2}\mathrm{e}^{\mathrm{i}\Omega t} + \frac{\Delta T}{2}\mathrm{e}^{-\mathrm{i}\Omega t}. \quad (10.18)$$

However, at $x = 0$ the general solution (eqn 10.16) becomes

$$T(0,t) = \sum_{\omega}A(\omega)\exp (-\mathrm{i}\omega t). \quad (10.19)$$

Comparison of eqns 10.18 and 10.19 implies that the only non-zero values of $A(\omega)$ are

$$A(0) = T_0,\qquad A(-\Omega) = \frac{\Delta T}{2},\qquad \mathrm{and}\qquad A(\Omega) = \frac{\Delta T}{2}. \quad (10.20)$$

Hence the solution to our problem for $x \geq 0$ is

$$T(x,t) = T_0 + \Delta T\mathrm{e}^{-x / \delta}\cos \left(\Omega t - \frac{x}{\delta}\right), \quad (10.21)$$

===== Page 93 =====

where

$$\delta = \sqrt{\frac{2D}{\Omega}} = \sqrt{\frac{2\kappa}{\Omega C}} \quad (10.22)$$

is known as the skin depth. The solution in eqn 10.21 is plotted in Fig. 10.2. [Note that the use of the term skin depth brings out the analogy between this effect and the skin depth that arises when electromagnetic waves are incident on a metal surface, see e.g. Griffiths (2003).] We note the following important features of this solution:

- $T$ falls off exponentially as $\mathrm{e}^{-x/\delta}$.
- There is a phase shift of $x/\delta$ radians in the oscillations.
- $\delta \propto \Omega^{-1/2}$ so that faster oscillations fall off faster.

[Image: Two plots of the solution T(x,t). The top is a contour plot of x/delta versus Omega t. The bottom is a 3D surface plot of T versus x/delta and Omega t, showing exponential decay and a phase shift with depth.]
**Fig. 10.2** A contour plot and a three-dimensional surface plot of eqn 10.21, showing that the temperature falls off exponentially as $\mathrm{e}^{-x/\delta}$. The contour plot shows that there is a phase shift in the oscillations as $x$ increases.

===== Page 94 =====

## 10.3 The steady state

If the system has reached a steady state, its properties are not time-dependent. This includes the temperature, so that

$$\frac{\partial T}{\partial t} = 0. \quad (10.23)$$

Hence in this case, the thermal diffusion equation reduces to

$$\nabla^2 T = 0, \quad (10.24)$$

which is Laplace's equation. Note that the thermal diffusivity $D = \kappa /C$ plays no role in this equation. However, there is still a heat flux $J = - \kappa \nabla T$ and so the thermal conductivity $\kappa$ is still relevant.

## Example 10.2

The plane $x = 0$ is maintained at a temperature $T_{1}$ and the plane $x = L$ is maintained at a temperature $T_{2}< T_{1}$. Find the heat flux.

Solution:

The steady state implies that we must use Laplace's equation in one dimension so $\partial^2 T / \partial x^2 = 0$. Integrating twice and putting in the boundary conditions yields

$$T = \frac{(T_2 - T_1)x}{L} +T_1\mathrm{for}0\leq x\leq L, \quad (10.25)$$

and hence the heat flux is

$$J = -\kappa \left(\frac{\partial T}{\partial x}\right) = \frac{\kappa}{L} (T_1 - T_2). \quad (10.26)$$

The quantity $\frac{\kappa}{L}$ is called the thermal conductance or sometimes the U value and is measured in $\mathrm{Wm}^{-2}\mathrm{K}^{-1}$. Its reciprocal $\frac{L}{\kappa}$ is called the thermal resistance or sometimes the R value and is measured in $\mathrm{m}^2\mathrm{KW}^{-1}$. The thermal resistance of duvets is measured in togs, where 1 tog is equal to $0.1\mathrm{m}^2\mathrm{KW}^{-1}$.

## 10.4 The thermal diffusion equation for a sphere

Very often, heat transfer problems have spherical symmetry (e.g., the cooling of the Earth or the Sun). In this section we will show that one can also solve the (rather forbidding looking) problem of the thermal diffusion equation in a system with spherical symmetry. In spherical polar coordinates, we have in general that $\nabla^2 T$ is given by

===== Page 95 =====

$$\nabla^2 T = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right) + \frac{1}{r^2}\frac{\partial}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin \theta \frac{\partial T}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2T}{\partial\phi^2}, \quad (10.27)$$

so that if $T$ is not a function of $\theta$ or $\phi$ we can write

$$\nabla^2 T = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right), \quad (10.28)$$

and hence the diffusion equation becomes

$$\frac{\partial T}{\partial t} = \frac{\kappa}{C}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right). \quad (10.29)$$

## Example 10.3

The thermal diffusion equation for a sphere in the steady state

In the steady state, $\partial T / \partial t = 0$ and hence we need to solve

$$\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right) = 0. \quad (10.30)$$

Now if $T$ is independent of $r$, $\partial T / \partial r = 0$ and this will be a solution. Moreover, if $r^2 (\partial T / \partial r)$ is independent of $r$, this will generate another solution. Now $r^2 (\partial T / \partial r) =$ constant implies that $T\propto r^{-1}$. Hence a general solution is

$$T = A + \frac{B}{r}, \quad (10.31)$$

where $A$ and $B$ are constants. This should not surprise us if we know some electromagnetism, as we are solving Laplace's equation in spherical coordinates assuming spherical symmetry, and in electromagnetism the solution for the electric potential in this case is an arbitrary constant plus a Coulomb potential, proportional to $1 / r$.

A practical problem one often needs to solve is cooking a quantity of meat. The meat is initially at some cool temperature (the temperature of the kitchen or of the refrigerator) and it is placed into a hot oven. The skill in cooking is getting the inside up to temperature. How long does it take? The next example shows how to calculate this for the (rather artificial) example of a spherical chicken!

## Example 10.4

## The spherical chicken

A spherical chicken of radius $a$ at initial temperature $T_0$ is placed into an oven at temperature $T_{1}$ at time $t = 0$ (see Fig. 10.3). The boundary conditions are that the oven is at temperature $T_{1}$ so that

$$T(a,t) = T_{1}, \quad (10.32)$$

===== Page 96 =====

and the chicken is originally at temperature $T_{0}$, so that for $r < a$

$$T(r,0) = T_0. \quad (10.33)$$

[Image: A circle representing a spherical chicken of radius a at initial temperature T0. It is surrounded by a grey region representing the oven at temperature T1.]
**Fig. 10.3** Initial condition of a spherical chicken of radius $a$ at initial temperature $T_{0}$, which is placed into an oven at temperature $T_{1}$ at time $t = 0$.

We want to obtain the temperature as a function of time at the centre of the chicken, i.e., $T(0,t)$.

Solution:

We will show how we can transform this to a one-dimensional diffusion equation. This is accomplished using a substitution

$$T(r,t) = T_{1} + \frac{B(r,t)}{r}, \quad (10.34)$$

where $B(r,t)$ is now a function of $r$ and $t$. This substitution is motivated by the solution to the steady-state problem in eqn 10.31 and of course means that we can write $B$ as $B = r(T - T_{1})$.

We now need to work out some partial differentials:

$$\frac{\partial T}{\partial t} = \frac{1}{r}\frac{\partial B}{\partial t}, \quad (10.35)$$

$$\frac{\partial T}{\partial r} = -\frac{B}{r^2} +\frac{1}{r}\frac{\partial B}{\partial r}, \quad (10.36)$$

and hence multiplying eqn 10.36 by $r^{2}$ we have that

$$r^{2}\frac{\partial T}{\partial r} = -B + r\frac{\partial B}{\partial r}, \quad (10.37)$$

and therefore

$$\frac{\partial}{\partial r}\left[r^{2}\frac{\partial T}{\partial r}\right] = r\frac{\partial^{2}B}{\partial r^{2}}, \quad (10.38)$$

which means that eqn 10.29 becomes

$$\frac{\partial B}{\partial t} = D\frac{\partial^{2}B}{\partial r^{2}}, \quad (10.39)$$

where $D = \kappa /C$. This is a one-dimensional diffusion equation and is therefore much easier to solve than the one with which we started.

The new boundary conditions can be rewritten as follows:

(1) Because $B = r(T - T_{1})$ we have that $B = 0$ when $r = 0$:

$$B(0,t) = 0; \quad (10.40)$$

(2) Because $T = T_{1}$ at $r = a$ we have that:

$$B(a,t) = 0; \quad (10.41)$$

(3) Because $T = T_{0}$ at $t = 0$ we have that (for $r<a$ ):

$$B(r,0) = r(T_0 - T_1). \quad (10.42)$$

===== Page 97 =====

We look for wave-like solutions with these boundary conditions and hence are led to try

$$B = \sin (kr)\mathrm{e}^{-\mathrm{i}\omega t}, \quad (10.43)$$

and substituting this into eqn 10.39 yields

$$\mathrm{i}\omega = Dk^2. \quad (10.44)$$

The relation $ka = n\pi$ where $n$ is an integer fits the first two boundary conditions and hence

$$\mathrm{i}\omega = D\left(\frac{n\pi}{a}\right)^2, \quad (10.45)$$

and hence our general solution is

$$B(r,t) = \sum_{n = 1}^{\infty}A_{n}\sin \left(\frac{n\pi r}{a}\right)\mathrm{e}^{-D\left(\frac{n\pi}{a}\right)^{2}t}. \quad (10.46)$$

To find $A_{n}$, we need to match this solution at $t = 0$ using our third boundary condition. Hence

$$r(T_0 - T_1) = \sum_{n = 1}^{\infty}A_n\sin \left(\frac{n\pi r}{a}\right). \quad (10.47)$$

We multiply both sides by $\sin \left(\frac{n\pi r}{a}\right)$ and integrate, so that

$$\int_0^a\sin \left(\frac{n\pi r}{a}\right)r(T_0 - T_1)\mathrm{d}r = \sum_{n = 1}^{\infty}A_n\int_0^a\sin \left(\frac{n\pi r}{a}\right)\sin \left(\frac{n\pi r}{a}\right)\mathrm{d}r. \quad (10.48)$$

The right-hand side yields $A_{n}a / 2$ and the left-hand side can be integrated by parts. This yields

$$A_{m} = \frac{2a}{m\pi} (T_{1} - T_{0})(-1)^{m}, \quad (10.49)$$

and hence by substituting this back into eqn 10.46 we obtain

$$B(r,t) = \frac{2a}{\pi} (T_1 - T_0)\sum_{n = 1}^{\infty}\frac{(-1)^n}{n}\sin \left(\frac{n\pi r}{a}\right)\mathrm{e}^{-D(n\pi / a)^2t}. \quad (10.50)$$

Putting this back into eqn 10.34 shows that the temperature $T(r,t)$ inside the chicken $(r\leq a)$ behaves as

$$T(r,t) = T_{1} + \frac{2a}{\pi} (T_{1} - T_{0})\sum_{n = 1}^{\infty}\frac{(-1)^{n}}{n}\frac{\sin(n\pi r / a)}{r}\mathrm{e}^{-D(n\pi / a)^{2}t}. \quad (10.51)$$

The centre of the chicken has temperature

$$T(0,t) = T_{1} + 2(T_{1} - T_{0})\sum_{n = 1}^{\infty}(-1)^{n}\mathrm{e}^{-D(n\pi / a)^{2}t}, \quad (10.52)$$

which is deduced from eqn 10.51 using the fact that as $r \to 0$

$$\frac{1}{r}\sin \left(\frac{n\pi r}{a}\right)\to \frac{n\pi}{a}. \quad (10.53)$$

===== Page 98 =====

[Image: A graph of temperature T versus time t for the centre of a spherical chicken. The graph shows T starting at T0, dipping slightly, and then rising asymptotically towards T1. Several curves show the sum of an increasing number of terms from the series solution.]
**Fig. 10.4** The sum of the first few terms of eqn 10.52, shown together with $T(0,t)$ evaluated from all terms (thick solid line). The sums of only the first few terms fail near $t = 0$ and one needs more and more terms to give an accurate estimate of the temperatures as $t$ gets closer to 0 (although this is the region where one knows what the temperature is anyway!).

The expression in eqn 10.52 (see Fig. 10.4) becomes dominated by the first exponential in the sum as time $t$ increases, so that

$$T(0,t)\approx T_{1} - 2(T_{1} - T_{0})\mathrm{e}^{-D(\pi /a)^{2}t}, \quad (10.54)$$

for $t\gg a^{2} / D\pi^{2}$. Analogous behaviour is of course found for a warm sphere cooling in a colder environment. A cooling or warming body thus behaves like a low-pass filter, with the smallest exponent dominating at long times. The smaller the sphere, the shorter the time before it warms or cools, according to a simple exponential law.

This example shows that the cooking time $t$ is proportional to $a^{2}$. It therefore scales with the surface area $4\pi a^{2}$ and not the volume $\frac{4}{3}\pi a^{3}$. The mass $m$ of the chicken is proportional to its volume (assuming the density of chickens is constant) and therefore

$$t\propto m^{2 / 3}. \quad (10.55)$$

However, cookery books give a different "law" for cooking chickens: they often quote a rule which is something like 40 minutes per kg plus 30 minutes "for the pot". This is clearly nonsense, since the pot doesn't need cooking, and the rule fails for stir-frying small pieces of chicken (which cook in seconds in a hot pan and clearly don't need 30 minutes added on). However, the two approaches give approximately the same answer for most normal-sized chickens (see Fig. 10.5).

[Image: A graph of cooking time t versus chicken mass m. A solid curve shows t proportional to m^(2/3). A dashed line shows a typical cookery book rule (40 minutes per kg plus 30 minutes). The two lines agree for most normal-sized chickens.]
**Fig. 10.5** The cooking time for a chicken according to eqn 10.55 (solid line) and the cook's rule of 40 minutes per kg plus 30 minutes "for the pot" given in many cookery books. The two rules agree for most normal-sized chickens. [Note 1 kg is approximately 2.2 lb.]

===== Page 99 =====

## Example 10.5

The surface of a spherical animal of radius $a$ is maintained at a temperature $T_{0}$ by its internal metabolism. It sits in a medium of thermal conductivity $\kappa$ which is at a lower temperature $T_{1}$ as measured at a large distance from the animal). Assuming steady-state conditions, find the rate at which the animal loses heat.

Solution:

In the region outside the animal, $\partial T / \partial t = 0$ and hence by eqns 10.30 and 10.31 we have that $T(r) = A + B / r$ where $A$ and $B$ are constants. Since $T(a) = T_{0}$ and $T(r)\rightarrow T_{1}$ for $r\rightarrow \infty$, we have $A = T_{1}$ and $B = a(T_{0}-T_{1})$. The heat flux is radial and is given by $J = - \kappa \partial T / \partial r = \kappa a(T_{0}-T_{1}) / r^{2}$ and so at the surface $(r = a)$ is given by $J = \kappa (T_{0} - T_{1}) / a$. The total amount of heat lost at the surface per second is therefore obtained by multiplying $J$ by the surface area of the sphere, yielding $4\pi a^{2}J = 4\pi \kappa a(T_{0} - T_{1})$. Note that the heat lost per second is proportional to $a$ even though the heat generated by the animal presumably scales with its volume and hence with $a^{3}$. Therefore heat loss is much more important for small animals than for large ones.

## 10.5 Newton's law of cooling

Newton's law of cooling states that the temperature of a cooling body falls exponentially towards the temperature of its surroundings with a rate proportional to the area of contact between the body and the environment. The results of the previous section indicate that it is an approximation to reality, as a cooling sphere only cools exponentially at long times.

Newton's law of cooling is often stated as follows: the heat loss of a solid or liquid surface (a hot central-heating pipe or the exposed surface of a cup of tea) to the surrounding gas (usually air, which is free to convect the heat away) is proportional to the area of contact multiplied by the temperature difference between the solid/liquid and the gas. Mathematically, this can be expressed as an equation for the heat flux $J$, which is

$$J = h\Delta T, \quad (10.56)$$

where $\Delta T$ is the temperature difference between the body and its environment and $h$ is a vector whose direction is normal to the surface of the body and whose magnitude $h = |h|$ is a heat transfer coefficient. In general, $h$ depends on the temperature of the body and its surroundings and varies over the surface, so that Newton's "law" of cooling is more of an empirical relation.

The steps leading from eqn 10.56 to an exponential decay of temperature are demonstrated in the following example.

===== Page 100 =====

## Example 10.6

A polystyrene cup containing tea at temperature $T_{\mathrm{hot}}$ at $t = 0$ stands for a while in a room with air temperature $T_{\mathrm{air}}$. The heat loss through the surface area $A$ exposed to the air is, according to Newton's law of cooling, proportional to $A(T(t) - T_{\mathrm{air}})$, where $T(t)$ is the temperature of the tea at time $t$. Ignoring the heat lost by other means, we have that

$$-C\frac{\partial T}{\partial t} = JA = hA(T - T_{\mathrm{air}}), \quad (10.57)$$

where $J$ is the heat flux, $C$ is the heat capacity of the cup of tea and $h$ is a constant, so that

$$T = T_{\mathrm{air}} + (T_{\mathrm{hot}} - T_{\mathrm{air}}) \mathrm{e}^{-\lambda t} \quad (10.58)$$

where $\lambda = Ah / C$.

What makes these types of calculations of heat transfer so difficult is that heat transfer from bodies into their surrounding gas or liquid is often dominated by convection. Convection can be defined as the transfer of heat by the motion of or within a fluid (i.e., within a liquid or a gas). Convection is often driven by the fact that warmer fluid expands and rises, while colder fluid contracts and sinks; this causes currents in the fluid to be set up, which rather efficiently transfer heat. Our analysis of the thermal conductivity in a gas ignores such currents. Convection is a very complicated process and can depend on the precise details of the geometry of the surroundings. A third form of heat transfer is by thermal radiation, and this will be the subject of chapter 23.

## 10.6 The Prandtl number

How valid is it to ignore convection? It's clearly fine to ignore it in a solid, but for a fluid we need to know the relative strength of the diffusion of momentum and heat. Convection dominates if momentum diffusion dominates (because convection involves transport of the gas itself) but conduction dominates if heat diffusion dominates. We can express these two diffusivities using the kinematic viscosity $\nu = \eta /\rho$ (with units $\mathrm{m}^2 \mathrm{s}^{-1}$) and the thermal diffusivity $D = \kappa /\rho c_p$ (also with units $\mathrm{m}^2 \mathrm{s}^{-1}$), where $\rho$ is the density. To examine their relative magnitudes, we define the Prandtl number as the dimensionless ratio $\sigma_{\mathrm{p}}$ obtained by dividing $\nu$ by $D$, so that

$$\sigma_{\mathrm{p}} = \frac{\nu}{D} = \frac{\eta c_{\mathrm{p}}}{\kappa}. \quad (10.59)$$

For an ideal gas, we can use $c_{\mathrm{p}} / c_{\mathrm{V}} = \gamma = \frac{5}{3}$, and using eqn 9.21 (which states that $\kappa = c_{\mathrm{V}}\eta$) we arrive at $\sigma_{\mathrm{p}} = \frac{5}{3}$. However, eqn 9.21 resulted

===== Page 101 =====

from an approximate treatment, and the corrected version is eqn 9.44 (which states that $\kappa = \frac{5}{2}\eta c_V$), and hence we arrive at

$$\sigma_{\mathrm{p}} = \frac{2}{3}. \quad (10.60)$$

For many gases, the Prandtl number is found to be around this value. It is between 100 and 40000 for engine oil and around 0.015 for mercury. When $\sigma_{\mathrm{p}} \gg 1$, diffusion of momentum (i.e., viscosity) dominates over diffusion of heat (i.e., thermal conductivity), and convection is the dominant mode of heat transport. When $\sigma_{\mathrm{p}} \ll 1$ the reverse is true, and thermal conduction dominates the heat transport.

## 10.7 Sources of heat

If heat is generated at a rate $H$ per unit volume (so $H$ is measured in $\mathrm{Wm}^{-3}$), this will add to the divergence of $\mathbf{J}$ so that eqn 10.7 becomes

$$\nabla \cdot \mathbf{J} = -C\frac{\partial T}{\partial t} +H, \quad (10.61)$$

and hence the thermal diffusion equation becomes

$$\nabla^2 T = \frac{C}{\kappa}\frac{\partial T}{\partial t} -\frac{H}{\kappa}, \quad (10.62)$$

or equivalently

$$\frac{\partial T}{\partial t} = D\nabla^2 T + \frac{H}{C}. \quad (10.63)$$

## Example 10.7

A metallic bar of length $L$ with both ends maintained at $T = T_0$ passes a current, which generates heat $H$ per unit length of the bar per second. Find the temperature at the centre of the bar in steady state.

Solution: In steady state,

$$\frac{\partial T}{\partial t} = 0, \quad (10.64)$$

and so

$$\frac{\partial^2T}{\partial x^2} = -\frac{H}{\kappa}. \quad (10.65)$$

Integrating this twice yields

$$T = \alpha x + \beta -\frac{H}{2\kappa} x^2, \quad (10.66)$$

where $\alpha$ and $\beta$ are constants of integration. The boundary conditions imply that

$$T - T_0 = \frac{H}{2\kappa} x(L - x), \quad (10.67)$$

so that at $x = L / 2$ we have that the temperature is

$$T = T_0 + \frac{HL^2}{8\kappa}. \quad (10.68)$$

===== Page 102 =====

## 10.8 Particle diffusion

This chapter has been concerned with the diffusion of heat, but as stated at the beginning of the chapter, the same laws apply to diffusion of particles. Just as heat diffuses down a temperature gradient $\nabla T$ from hot to cold, so particles diffuse down a concentration gradient $\nabla n$ from high concentration to low concentration. The mathematics are analogous since the diffusion equation $\partial n / \partial t = D\nabla^{2}n$ (with $D$ as a diffusion constant) is essentially the same as the thermal diffusion equation $\partial T / \partial t = D\nabla^{2}T$ (with $D = \kappa /C$ as the thermal diffusivity). The techniques presented in this chapter can be used to solve many problems in diffusion physics.

## Example 10.8

A sphere of radius $a$ is placed in an infinite medium containing certain particles with number density $n_0$. The sphere absorbs these particles with great efficiency so that the number density at distance $r = a$ from the centre of the sphere is zero. Find the rate of absorption of the particles by the sphere.

Solution:

This problem is entirely analogous to that of Example 10.5. Using the same methods, we find

$$n(r) = n_0\left(1 - \frac{a}{r}\right) \quad (10.69)$$

outside the sphere, so that the flux $\Phi$ at the surface is

$$\Phi = -D\left(\frac{\partial n}{\partial r}\right)_{r = a} = \frac{Dn_0}{a}, \quad (10.70)$$

and so the total rate of absorption is obtained by multiplying $\Phi$ by the surface area of the sphere which gives

$$\mathrm{rate~of~absorption} = 4\pi an_0. \quad (10.71)$$

Notice that this rate is (again) proportional to the radius $a$ and not to the area (or even the volume). This has important implications in biology. Bacteria absorb oxygen from their environment and this is at a maximum rate $4\pi an_0$ (assuming them to be spherical and maximally efficient absorbers), but their consumption of oxygen scales with their volume and hence with $a^3$. This sets a maximum limit on the size of a bacterium, because if it is too big the bacterium will not be able to supply its internal oxygen needs. Large organisms are multicellular.

[Image: A portrait of J.B.J. Fourier, a man with curly hair and wearing a high collar.]
**Fig. 10.6** J.B.J. Fourier

===== Page 103 =====

## Chapter summary

The thermal diffusion equation (in the absence of a heat source) is

$$\frac{\partial T}{\partial t} = D\nabla^2 T, \quad (10.72)$$

where $D = \kappa /C$ is the thermal diffusivity.

"Steady state" implies that

$$\frac{\partial}{\partial t} (\mathrm{physical~quantity}) = 0. \quad (10.73)$$

If heat is generated at a rate $H$ per unit volume per unit time, then the thermal diffusion equation becomes

$$\frac{\partial T}{\partial t} = D\nabla^2 T + \frac{H}{C}. \quad (10.74)$$

Newton's law of cooling states that the heat loss from a solid or liquid surface is proportional to the area of the surface multiplied by the temperature difference between the solid/liquid and the gas.

The particle diffusion equation is

$$\frac{\partial n}{\partial t} = D\nabla^2 n, \quad (10.75)$$

where $D$ is the diffusion constant.

## Exercises

(10.1) One face of a thick uniform layer is subject to sinusoidal temperature variations of angular frequency $\omega$. Show that damped sinusoidal temperature oscillations propagate into the layer and give an expression for the decay length of the oscillation amplitude. A cellar is built underground and is covered by a ceiling, which is $3\mathrm{m}$ thick and made of limestone. The outside temperature is subject to daily fluctuations of amplitude $10^{\circ}\mathrm{C}$ and annual fluctuations of $20^{\circ}\mathrm{C}$. Estimate the magnitude of the daily and annual temperature variations within the cellar. Assuming that January is the coldest month of the year, when will the cellar's temperature be at its lowest?

[The thermal conductivity of limestone is $1.6\mathrm{Wm}^{-1}\mathrm{K}^{-1}$, and the heat capacity of limestone is $2.5\times 10^{6}\mathrm{J}\mathrm{K}^{-1}\mathrm{m}^{-3}$.]

(10.2) (a) A cylindrical wire of thermal conductivity $\kappa$, radius $a$ and resistivity $\rho$ uniformly carries a current $I$. The temperature of its surface is fixed at $T_{0}$ using water cooling. Show that the temperature $T(r)$ inside the wire at radius $r$ is given by

$$T(r) = T_0 + \frac{\rho I^2}{4\pi^2a^4\kappa} (a^2 -r^2).$$

(b) The wire is now placed in air at temperature $T_{\mathrm{air}}$ and the wire loses heat from its surface according to Newton's law of cooling (so that the heat flux from the surface of the wire is given by $\alpha (T(a) - T_{\mathrm{air}})$ where $\alpha$ is a constant). Find the temperature $T(r)$.

===== Page 104 =====

(10.3) Show that for the problem of a spherical chicken being cooked in an oven considered in Example 10.4, the temperature $T$ gets $90\%$ of the way from $T_{0}$ to $T_{1}$ after a time $\sim a^{2}\ln 20 / \pi^{2}D$.

(10.4) A microprocessor has an array of metal fins attached to it, whose purpose is to remove heat generated within the processor. Each fin may be represented by a long thin cylindrical copper rod with one end attached to the processor; heat received by the rod through this end is lost to the surroundings through its sides.

Show that the temperature $T(x,t)$ at location $x$ along the rod at time $t$ obeys the equation

$$\rho C_{P}\frac{\partial T}{\partial t} = \kappa \frac{\partial^{2}T}{\partial x^{2}} -\frac{2}{a} R(T),$$

where $a$ is the radius of the rod, and $R(T)$ is the rate of heat loss per unit area of surface at temperature $T$. The surroundings of the rod are at temperature $T_{0}$. Assume that $R(T)$ has the form of Newton's law of cooling, namely

$$R(T) = A(T - T_{0}).$$

In the steady state:

(a) obtain an expression for $T$ as a function of $x$ for the case of an infinitely long rod whose hot end has temperature $T_{\mathrm{m}}$;

(b) show that the heat that can be transported away by a long rod (with radius $a$) is proportional to $a^{3/2}$ provided that $A$ is independent of $a$.

In practice the rod is not infinitely long. What length does it need to have for the results above to be approximately valid? The radius of the rod, $a$ is 1.5 mm.

[The thermal conductivity of copper is $380\mathrm{Wm}^{-1}\mathrm{K}^{-1}$. The cooling constant $A = 250\mathrm{Wm}^{-2}\mathrm{K}^{-1}$.]

(10.5) For oscillations at frequency $\omega$, a viscous penetration depth $\delta_{\mathrm{v}}$ can be defined by

$$\delta_{\mathrm{v}} = \left(\frac{2\eta}{\rho\omega}\right)^{1 / 2}, \quad (10.76)$$

analogously to the thermal penetration depth

$$\delta = \left(\frac{2\kappa}{\rho c_{\mathrm{p}}\omega}\right)^{1 / 2} \quad (10.77)$$

defined in this chapter. Show that

$$\left(\frac{\delta_{\mathrm{v}}}{\delta}\right)^{2} = \sigma_{\mathrm{p}}, \quad (10.78)$$

where $\sigma_{\mathrm{p}}$ is the Prandtl number (see eqn 10.59).

(10.6) For thermal waves, calculate the magnitude of the group velocity. This shows that the thermal diffusion equation cannot hold exactly since the velocity of propagation can become larger than that of any particles that could carry heat through the material. We now consider a modification of the thermal diffusion equation which fixes this problem. Consider the number density $n$ of thermal carriers in a material. In equilibrium, $n = n_{0}$, so that

$$\left(\frac{\partial n}{\partial t}\right) = -\mathbf{v}\cdot \nabla n + \frac{n - n_{0}}{\tau}, \quad (10.79)$$

where $\tau$ is a relaxation time and $\mathbf{v}$ is the carrier velocity. Multiply this equation by $\omega \tau \mathbf{v}$, where $\omega$ is the energy of a carrier, and sum over all $k$ states. Using the fact that $\sum_{k}n_{0}v = 0$ and $J = \sum_{k}\omega n v$ and that $|n - n_{0}|\ll n_{0}$ show that

$$\mathbf{J} + \tau \frac{\mathrm{d}\mathbf{J}}{\mathrm{d}t} = -\kappa \nabla T, \quad (10.80)$$

and hence the modified thermal diffusion equation becomes

$$\frac{\partial T}{\partial t} +\tau \frac{\partial^{2}T}{\partial t^{2}} = D\nabla^{2}T. \quad (10.81)$$

Show that this modified equation gives a group velocity whose magnitude remains finite. Is this modification ever necessary?

(10.7) A series of $N$ large, flat rectangular slabs with thickness $\Delta x_{i}$ and thermal conductivity $\kappa_{i}$ are placed on top of one another. The top and bottom surfaces are maintained at temperature $T_{i}$ and $T_{f}$ respectively. Show that the heat flux $J$ through the slabs is given by $J = (T_{i} - T_{f}) / \sum_{i}R_{i}$, where $R_{i} = \Delta x_{i} / \kappa_{i}$.

(10.8) The space between two concentric cylinders is filled with material of thermal conductivity $\kappa$. The inner (outer) cylinder has radius $r_1$ ($r_2$) and is maintained at temperature $T_{1}$ ($T_{2}$). Derive an expression for the heat flow per unit length between the cylinders.

(10.9) A pipe of radius $R$ is maintained at a uniform temperature $T$. To reduce heat loss from the pipe, it is lagged by an insulating material of thermal conductivity $\kappa$. The lagged pipe has radius $r > R$. Assume that all surfaces lose heat according to Newton's law of cooling $\mathbf{J} = \mathbf{h}\Delta T$, where $h = |\mathbf{h}|$ can be taken to be a constant. Show that the heat loss per unit length of pipe is inversely proportional to

$$\frac{1}{hr} +\frac{1}{\kappa}\ln \left(\frac{r}{R}\right), \quad (10.82)$$

and hence show that thin lagging doesn't reduce heat loss if $R< \kappa /h$.

===== Page 107 =====

# Part IV

## The first law

In this part we are now ready to think about energy in some detail and hence introduce the first law of thermodynamics. This part is structured as follows:

In Chapter 11, we present the notion of a function of state, of which internal energy is one of the most useful. We discuss in detail the first law of thermodynamics, which states that energy is conserved and heat is a form of energy. We derive expressions for the heat capacity measured at constant volume or pressure for an ideal gas. In Chapter 12 we introduce the key concept of reversibility and discuss isothermal and adiabatic processes.

===== Page 108 =====

# 11 Energy

11.1 Some definitions  108
11.2 The first law of thermodynamics  110
11.3 Heat capacity  112
Chapter summary  115
Exercises  115

In this chapter we are going to focus on one of the key concepts in thermal physics, that of energy. What happens when energy is changed from one form to another? How much work can you get out of a quantity of heat? These are key questions to be answered. We are now beginning a study of thermodynamics proper, and in this chapter we will introduce the first law of thermodynamics. Before the first law, the most important concept in this chapter, we will introduce some additional ideas.

## 11.1 Some definitions

### 11.1.1 A system in thermal equilibrium

In thermodynamics, we define a system to be whatever part of the Universe we select for study. Near the system are its surroundings. We recall from Section 4.1 that a system is in thermal equilibrium when its macroscopic observables (such as its pressure or its temperature) have ceased to change with time. If you take a gas in a container, which has been held at a certain stable temperature for a considerable period of time, the gas is likely to be in thermal equilibrium. A system in thermal equilibrium having a particular set of macroscopic observables is said to be in a particular equilibrium state. If however, you suddenly apply a lot of heat to one side of the box, then initially at least, the gas is likely to be in a non-equilibrium state.

### 11.1.2 Functions of state

A system is in an equilibrium state if macroscopic observable properties have fixed, definite values, independent of "how they got there". These properties are functions of state (sometimes called variables of state). A function of state is any physical quantity that has a well-defined value for each equilibrium state of the system. Thus, in thermal equilibrium these variables of state have no time dependence. Examples are volume, pressure, temperature, and internal energy, and we will introduce a lot more in what follows. Examples of quantities that are not functions of state include the position of particle number 4325667, the total work done on a system, and the total heat put into the system. Later, we will show in detail why work and heat are not functions of state. However, the point can be understood as follows: the fact that

===== Page 109 =====

your hands are warm or cold depends on their current temperature (a function of state), independently of how you got them to that temperature. For example, you can get to the same final thermodynamic state of having warm hands by different combinations of working and heating, e.g., you can end up with warm hands by rubbing them together (using the muscles in your arms to do work on them) or putting them in a toaster (adding heat).

We now give a more mathematical treatment of what is meant by a function of state. Let the state of a system be described by parameters $\mathbf{x} = (x_{1},x_{2},\ldots)$ and let $f(\mathbf{x})$ be some function of state. [Note that this could be a very trivial function, such as $f(\mathbf{x}) = x_{1}$, since what we've called "parameters" are themselves functions of state. But we want to allow for more complicated functions of state which might be combinations of these "parameters".] Then if the system parameters change from $\mathbf{x}_{\mathrm{i}}$ to $\mathbf{x}_{\mathrm{f}}$, the change in $f$ is

$$\Delta f = \int_{\mathbf{x}_1}^{\mathbf{x}_{\mathrm{f}}}\mathrm{d}f = f(\mathbf{x}_{\mathrm{f}}) - f(\mathbf{x}_{\mathrm{i}}). \quad (11.1)$$

This only depends on the end points $\mathbf{x}_{\mathrm{i}}$ and $\mathbf{x}_{\mathrm{f}}$. The quantity $\mathrm{d}f$ is an exact differential (see Appendix C.7) and functions of state have exact differentials. By contrast, a quantity that is represented by an inexact differential is not a function of state. The following example illustrates these kinds of differential.

## Example 11.1

Let a system be described by two parameters, $x$ and $y$. Let $f = xy$ so that

$$\mathrm{d}f = \mathrm{d}(xy) = y\mathrm{d}x + x\mathrm{d}y. \quad (11.2)$$

Then if $(x,y)$ changes from $(0,0)$ to $(1,1)$, the change in $f$ is given by

$$\Delta f = \int_{(0,0)}^{(1,1)}\mathrm{d}f = [xy]_{(0,0)}^{(1,1)} = (1\times 1) - (0\times 0) = 1. \quad (11.3)$$

This answer is independent of the exact path taken (it could be any of those shown in Fig. 11.1) because $\mathrm{d}f$ is an exact differential.

Now consider $\mathrm{d}g = y\mathrm{d}x$. The change in $g$ when $(x,y)$ changes from $(0,0)$ to $(1,1)$ along the path shown in Fig. 11.1(a) is given by

$$\Delta g = \int_{(0,0)}^{(1,1)}y\mathrm{d}x = \int_{0}^{1}x\mathrm{d}x = \frac{1}{2}. \quad (11.4)$$

However when the integral is not carried out along the line $y = x$, but along the path shown in Fig. 11.1(b), it is given by

$$\Delta g = \int_{(0,0)}^{(1,0)}y\mathrm{d}x + \int_{(1,0)}^{(1,1)}y\mathrm{d}x = 0. \quad (11.5)$$

[Image: Three different paths (a, b, c) between the points (0,0) and (1,1) in the xy-plane.]
**Fig. 11.1** Three possible paths between the points $(x,y) = (0,0)$ and $(x,y) = (1,1)$.

If the integral is taken along the path shown in Fig. 11.1(c), yet another result would be obtained, but we are not going to attempt to calculate that!

Hence we find that the value of $\Delta g$ depends on the path taken, and this is because $\mathrm{d}g$ is an inexact differential.

Recall from Section 1.2 that functions of state can either be:

- extensive (proportional to system size), e.g., energy, volume, magnetization, mass, or
- intensive (independent of system size), e.g., temperature, pressure, magnetic field, density, energy density.

In general one can find an equation of state that connects functions of state: for a gas this takes the form $f(p,V,T) = 0$. An example is the equation of state for an ideal gas, $pV = nRT$, which we met in eqn 1.12.

===== Page 110 =====

## 11.2 The first law of thermodynamics

Though the idea that heat and work are both forms of energy seems obvious to a modern physicist, the idea took some getting used to. Lavoisier had, in 1789, proposed that heat was a weightless, conserved fluid called caloric. Caloric was a fundamental element that couldn't be created or destroyed. Lavoisier's notion "explained" a number of phenomena, such as combustion (fuels have stored caloric which is released on burning). Rumford in 1798 realized that something was wrong with the caloric theory: heating could be produced by friction, and if you keep on drilling through a cannon barrel (to take the example that drew the problem to his attention) almost limitless supplies of heat can be extracted. Where does all this caloric come from? Mayer quantified this in 1842 with an elegant experiment in which he frictionally generated heat in paper pulp and measured the temperature rise. Joule independently performed similar experiments, but more accurately, in the period 1840-1845 (and his results became better known so that he was able to claim the credit!) Joule let a mass tied to a string slowly descend a certain height, while the other end of the string turns a paddle wheel immersed in a certain mass of water. The turning of the paddle frictionally heats the water. After a number of descents, Joule measured the temperature rise of the water. In this way he was able to deduce the "mechanical equivalent of heat". He also measured the heat output of a resistor (which, in modern units, is equal to $I^2 R$, where $I$ is the current and $R$ the resistance). He was able to show that the same heat was produced for the same energy used, independent of the method of delivery. This implied that heat is a form of energy. Joule's experiments therefore consigned the caloric theory of heat to a footnote in history.

However, it was Mayer and later Helmholtz who elevated the experimental observations into a grand principle, which we can state as follows:

## The first law of thermodynamics

Energy is conserved and heat and work are both forms of energy.

A system has an internal energy $U$, which is the sum of the energy of all the internal degrees of freedom that the system possesses. $U$ is a function of state because it has a well-defined value for each equilibrium state of the system. We can change the internal energy of the system by heating it or by doing work on it. The heat $Q$ and work $W$ are not functions of state since they concern the manner in which energy is delivered to (or extracted from) the system. After the event of delivering energy to the system, you have no way of telling which of $Q$ or $W$ was added to (or subtracted from) the system by examining the system's state.

The following analogy may be helpful: your personal bank balance behaves something like the internal energy $U$ in that it acts like a function of state of your finances; cheques and cash are like heat and work in that they both result in a change in your bank balance, but after they have been paid in, you can't tell by simply looking at the value of your bank balance by which method the money was paid in.

The change in internal energy $U$ of a system can be written

$$\Delta U = \Delta Q + \Delta W, \quad (11.6)$$

where $\Delta Q$ is the heat supplied to the system and $\Delta W$ is the work done on the system. Note the convention: $\Delta Q$ is positive for heat supplied to the system; if $\Delta Q$ is negative, heat is extracted from the system; $\Delta W$ is positive for work done on the system; if $\Delta W$ is negative, the system does work on its surroundings.

We define a thermally isolated system as a system that cannot exchange heat with its surroundings. In this case we find that $\Delta U = \Delta W$, because no heat can pass in or out of a thermally isolated system.

For a differential change, we write eqn 11.6 as

$$\mathrm{d}U = \mathrm{d}Q + \mathrm{d}W, \quad (11.7)$$

where $\mathrm{d}W$ and $\mathrm{d}Q$ are inexact differentials.

The work done on stretching a wire by a distance $\mathrm{d}x$ with a tension $F$ is (see Fig. 11.2(a))

$$\mathrm{d}W = F\mathrm{d}x. \quad (11.8)$$

The work done by compressing a gas (pressure $p$, volume $V$) by a piston can be calculated in a similar fashion (see Fig. 11.2(b)). In this case the force is $F = pA$, where $A$ is the area of the piston, and $\mathrm{d}Ax = -\mathrm{d}V$, so that

$$\mathrm{d}W = -p\mathrm{d}V. \quad (11.9)$$

In this equation, the negative sign ensures that the work $\mathrm{d}W$ done on the system is positive when $\mathrm{d}V$ is negative, i.e., when the gas is being compressed.

[Image: (a) A wire is stretched by a force F through a distance dx. (b) A gas in a cylinder with a piston is compressed by a distance dx, corresponding to a volume change dV.]
**Fig. 11.2** (a) The work done stretching a wire by a distance $\mathrm{d}x$ is $F\mathrm{d}x$. (b) The work done compressing a gas is $-p\mathrm{d}V$.

It turns out that eqn 11.9 is only strictly true for a reversible change, a point we will explain further in Section 12.1. The idea is that if the piston is not frictionless, or if you move the piston too suddenly and generate shock waves, you will need to do more work to compress the gas because more heat is dissipated in the process.

===== Page 112 =====

## 11.3 Heat capacity

We now want to understand in greater detail how adding heat can change the internal energy of gas. In general, the internal energy will be a function of temperature and volume, so that we can write $U = U(T,V)$. Hence a small change in $U$ can be related to changes in $T$ and $V$ by

$$\mathrm{d}U = \left(\frac{\partial U}{\partial T}\right)_V\mathrm{d}T + \left(\frac{\partial U}{\partial V}\right)_T\mathrm{d}V. \quad (11.10)$$

Rearranging eqn 11.7 with eqn 11.9 yields

$$\mathrm{d}Q = \mathrm{d}U + p\mathrm{d}V, \quad (11.11)$$

and now using eqn 11.10 we have that

$$\mathrm{d}Q = \left(\frac{\partial U}{\partial T}\right)_V\mathrm{d}T + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\mathrm{d}V. \quad (11.12)$$

We can divide eqn 11.12 by $\mathrm{d}T$ to obtain

$$\frac{\mathrm{d}Q}{\mathrm{d}T} = \left(\frac{\partial U}{\partial T}\right)_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\frac{\mathrm{d}V}{\mathrm{d}T}, \quad (11.13)$$

which is valid for any change in $T$ or $V$. However, what we want to know is what is the amount of heat we have to add to effect a change of temperature under certain constraints. The first constraint is that of keeping the volume constant. We recall the definition of the heat capacity at constant volume $C_V$ (see Section 2.2, eqn 2.6) as

$$C_V = \left(\frac{\partial Q}{\partial T}\right)_V. \quad (11.14)$$

From eqn 11.13, this constraint knocks out the second term and implies that

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V. \quad (11.15)$$

The heat capacity at constant pressure is then, using eqns 2.7 and 11.13, given by

$$C_p = \left(\frac{\partial Q}{\partial T}\right)_p \quad (11.16)$$

$$= \left(\frac{\partial U}{\partial T}\right)_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p \quad (11.17)$$

===== Page 113 =====

so that

$$C_p - C_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p. \quad (11.18)$$

Recall from Section 2.2 that heat capacities are measured in $\mathrm{JK}^{-1}$ and refer to the heat capacity of a certain quantity of gas. We will sometimes wish to talk about the heat capacity per mole of gas, or sometimes the heat capacity per mass of gas. We will use small $c$ for the latter, known as the specific heat capacities:

$$\begin{array}{rcl}{c_V} & = & {\frac{C_V}{M}}\\ {c_p} & = & {\frac{C_p}{M},} \end{array} \quad (11.19)$$

where $M$ is the mass of the material. Specific heat capacities are measured in $\mathrm{JK}^{-1}\mathrm{kg}^{-1}$.

## Example 11.2

## Heat capacity of an ideal monatomic gas

For an ideal monatomic gas, the internal energy $U$ is due to the kinetic energy, and hence $U = \frac{3}{2} RT$ per mole (see eqn 5.17; this result arises from the kinetic theory of gases). This means that $U$ is only a function of temperature. Hence

$$\left(\frac{\partial U}{\partial V}\right)_T = 0. \quad (11.21)$$

The equation of state for 1 mole of ideal gas is

$$pV = RT, \quad (11.22)$$

so that

$$V = \frac{RT}{p}, \quad (11.23)$$

and hence

$$\left(\frac{\partial V}{\partial T}\right)_p = \frac{R}{p}, \quad (11.24)$$

and hence using eqns 11.18, 11.21 and 11.24 we have that

$$C_p - C_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p = R. \quad (11.25)$$

Because $U = \frac{3}{2} RT$, we therefore have that

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = \frac{3}{2} R\mathrm{~per~mole}, \quad (11.26)$$

and

$$C_p = C_V + R = \frac{5}{2} R\mathrm{~per~mole}. \quad (11.27)$$

===== Page 114 =====

## Example 11.3

Is it always true that $\mathrm{d}U = C_V\mathrm{d}T$?

Solution:

No, in general eqn 11.10 and eqn 11.15 imply that

$$\mathrm{d}U = C_V\mathrm{d}T + \left(\frac{\partial U}{\partial V}\right)_T\mathrm{d}V. \quad (11.28)$$

For an ideal gas, $\left(\frac{\partial U}{\partial V}\right)_T = 0$ (eqn 11.21) so it is true that

$$\mathrm{d}U = C_V\mathrm{d}T, \quad (11.29)$$

but for non-ideal gases, $\left(\frac{\partial U}{\partial V}\right)_T \neq 0$ and hence $\mathrm{d}U \neq C_V \mathrm{d}T$.

The ratio of $C_p$ to $C_V$ turns out to be a very useful quantity (we will see why in the following chapter) and therefore we give it a special name. We define the adiabatic index $\gamma$ as the ratio of $C_p$ and $C_V$, so that

$$\gamma = \frac{C_p}{C_V}. \quad (11.30)$$

The reason for the name will become clear in the following chapter.

## Example 11.4

What is $\gamma$ for an ideal monatomic gas?

Solution:

Using the results from the previous example

$$\gamma = \frac{C_p}{C_V} = \frac{C_V + R}{C_V} = 1 + \frac{R}{C_V} = \frac{5}{3}. \quad (11.31)$$

## Example 11.5

Assuming $U = C_V T$ for an ideal gas, find (i) the internal energy per unit mass and (ii) the internal energy per unit volume.

Solution: Using the ideal gas equation $pV = Nk_B T$ and the density $\rho = Nm / V$ (where $m$ is the mass of one molecule), we find that

$$\frac{p}{\rho} = \frac{k_{\mathrm{B}}T}{m}. \quad (11.32)$$

===== Page 115 =====

Using eqn 11.31, we have that the heat capacity per mole is given by

$$C_{V} = \frac{R}{\gamma - 1}. \quad (11.33)$$

Hence, we can write that the internal energy for one mole of gas is

$$U = C_{V}T = \frac{RT}{\gamma - 1} = \frac{N_{\mathrm{A}}k_{\mathrm{B}}T}{\gamma - 1}. \quad (11.34)$$

The molar mass is $mN_{\mathrm{A}}$, and so dividing eqn 11.34 by the molar mass, yields $\tilde{u}$, the internal energy per unit mass, given by

$$\tilde{u} = \frac{p}{\rho(\gamma - 1)}. \quad (11.35)$$

Multiplying $\tilde{u}$ by the density $\rho$ gives $u$, the internal energy per unit volume, as

$$u = \rho \tilde{u} = \frac{p}{\gamma - 1}. \quad (11.36)$$

## Chapter summary

Functions of state have exact differentials.

The first law of thermodynamics states that "energy is conserved and heat is a form of energy".

$$\mathrm{d}U = \mathrm{d}W + \mathrm{d}Q$$

For a reversible change, $\mathrm{d}W = - p\mathrm{d}V$

$$C_{V} = \left(\frac{\partial Q}{\partial T}\right)_{V} = \left(\frac{\partial U}{\partial T}\right)_{V}.$$

$$C_{p} = \left(\frac{\partial Q}{\partial T}\right)_{P} \mathrm{and} C_{p} - C_{V} = R \mathrm{for a mole of ideal gas.}$$

The adiabatic index is $\gamma = C_{p} / C_{V}$.

## Exercises

(11.1) One mole of ideal monatomic gas is confined in a cylinder by a piston and is maintained at a constant temperature $T_{0}$ by thermal contact with a heat reservoir. The gas slowly expands from $V_{1}$ to $V_{2}$ while being held at the same temperature $T_{0}$. Why does the internal energy of the gas not change? Calculate the work done by the gas and the heat flow into the gas.

(11.2) Show that, for an ideal gas,

$$\frac{R}{C_{V}} = \gamma -1 \quad (11.37)$$

and

$$\frac{R}{C_p} = \frac{\gamma - 1}{\gamma}, \quad (11.38)$$

where $C_V$ and $C_p$ are the heat capacities per mole.

(11.3) Consider the differential

$$\mathrm{d}z = 2xy\mathrm{d}x + (x^2 +2y)\mathrm{d}y. \quad (11.39)$$

Evaluate the integral $\int_{(x_1,y_1)}^{(x_2,y_2)}\mathrm{d}z$ along the paths consisting of straight-line segments

(i) $(x_{1},y_{1})\rightarrow (x_{2},y_{1})$ and then $(x_{2},y_{1})\rightarrow (x_{2},y_{2})$
(ii) $(x_{1},y_{1})\rightarrow (x_{1},y_{2})$ and then $(x_{1},y_{2})\rightarrow (x_{2},y_{2})$

Is dz an exact differential?

(11.4) In polar coordinates, $x = r\cos \theta$ and $y = r\sin \theta$. The definition of $x$ implies that

$$\frac{\partial x}{\partial r} = \cos \theta = \frac{x}{r}. \quad (11.40)$$

But we also have $x^{2} + y^{2} = r^{2}$, so differentiating with respect to $r$ gives

$$2x\frac{\partial x}{\partial r} = 2r\Rightarrow \frac{\partial x}{\partial r} = \frac{r}{x}. \quad (11.41)$$

But eqns 11.40 and 11.41 imply that

$$\frac{\partial x}{\partial r} = \frac{\partial r}{\partial x}. \quad (11.42)$$

What's gone wrong?

(11.5) In the comic song by Flanders and Swann about the laws of thermodynamics, they summarize the first law by the statement:

Heat is work and work is heat

Is that a good summary?

[Image: A portrait of Antoine Lavoisier in 18th century dress.]
**Fig. 11.3** Antoine Lavoisier

[Image: A portrait of Benjamin Thompson, Count Rumford, in a red military uniform.]
**Fig. 11.4** Benjamin Thompson

===== Page 118 =====

# 12 Isothermal and adiabatic processes

12.1 Reversibility  118
12.2 Isothermal expansion of an ideal gas  120
12.3 Adiabatic expansion of an ideal gas  121
12.4 Adiabatic atmosphere  121
Chapter summary  123
Exercises  123

In this chapter we will apply the results of the previous chapter to illustrate some properties concerning isothermal and adiabatic expansions of gases. These results will assume that the expansions are reversible, and so the first part of this chapter explores the key concept of reversibility. This will be important for our discussion of entropy in subsequent chapters.

## 12.1 Reversibility

The laws of physics are reversible, so that if any process is allowed, then the time-reversed process can also occur. For example, if you could film the molecules in a gas bouncing off each other and the container walls, then when watching the film it would be hard to tell whether the film was being played forwards or backwards.

However, there are plenty of processes that you see in nature which seem to be irreversible. For example, consider an egg rolling off the edge of a table and smashing on the floor. Potential energy is converted into kinetic energy as the egg falls, and ultimately the energy ends up as a small amount of heat in the broken egg and the floor. The law of conservation of energy does not forbid the conversion of that heat back into kinetic energy of the reassembled egg which would then leap off the ground and back on to the table. However, this is never observed to happen. As another example, consider a battery driving a current $I$ through a resistor with resistance $R$ and dissipating heat $I^{2}R$ into the environment. Again, one never finds heat being absorbed by a resistor from its environment, resulting in the generation of a spontaneous current that can used to recharge the battery.

Lots of processes are like this, in which the final outcome is some potential, chemical, or kinetic energy that gets converted into heat, which is then dissipated into the environment. As we shall see, the reason seems to be that there are lots more ways that the energy can be distributed in heat than in any other way, and this is therefore the most probable outcome. To try and understand this statistical nature of reversibility, it is helpful to consider the following example.

===== Page 119 =====

## Example 12.1

We return to the situation described in Example 4.1. To recap, you are given a large box containing 100 identical coins. With the lid on the box, you give it a really good long and hard shake, so that you can hear the coins flipping, rattling, and being generally tossed around. Now you open the lid and look inside the box. Some of the coins will be lying with heads facing up and some with tails facing up. We assume that each of the $2^{100}$ possible configurations (the microstates) are equally likely to be found. Each of these is equally likely and so each has a probability of occurrence of approximately $10^{-30}$. However, the measurement made is counting the number of heads and the number of tails (the macrostates), and the results of this measurement are not equally likely. In Example 4.1 we showed that of the $\approx 10^{30}$ individual microstates, a large number $(\approx 4\times 10^{27})$ corresponded to 50 heads and 50 tails, but only one microstate corresponded to 100 heads and 0 tails.

Now, imagine that you had in fact carefully prepared the coins so that they were lying heads up. Following a good shake, the coins will most probably be a mixture of heads and tails. If, on the other hand, you carefully prepared a mixed arrangement of heads and tails, a good shake of the box is very unlikely to achieve a state in which all the coins lie with heads facing up. The process of shaking the box seems almost always to randomize the number of heads and tails, and this is an irreversible process.

This shows that the statistical behaviour of large systems is such as to make certain outcomes (such as a box of coins with mixed heads and tails) more likely than certain others (such as a box of coins containing coins the same way up). The statistics of large numbers therefore seems to drive many physical changes in an irreversible direction. How can we carry out a process in a reversible fashion?

The early researchers in thermodynamics wrestled with this problem, which was of enormous practical importance in the design of engines, in which you want to waste as little heat as possible to make your engine as efficient as possible. It was realized that when gases are expanded or compressed, it is possible to convert energy irreversibly into heat, and this will generally occur when we perform the expansion or the compression very fast, causing shock waves to be propagated through the gas (we will consider this effect in more detail in Chapter 32). However, it is possible to perform the expansion or compression reversibly if we do it sufficiently slowly so that the gas remains in equilibrium throughout the entire process and passes seamlessly from one equilibrium state to the next, each equilibrium state differing from the previous one by an infinitesimal change in the system parameters. Such a process is said to be quasistatic, since the process is almost in completely unchanging static equilibrium. As we shall see, heat can nevertheless be absorbed or

===== Page 120 =====

emitted in the process, while still maintaining reversibility. In contrast, for an irreversible process, a non-zero change (rather than a sequence of infinitesimal changes) is made to the system, and therefore the system is not in equilibrium throughout the process.

An important (but given the name, perhaps not surprising) property of reversible processes is that you can run them in reverse. This fact we will use a great deal in Chapter 13. Of course, it would take an infinite amount of time for a strictly reversible process to occur, so most processes we term reversible are approximations to the "real thing".

## 12.2 Isothermal expansion of an ideal gas

In this section, we will calculate the heat change in a reversible isothermal expansion of an ideal gas. The word isothermal means "at constant temperature", and hence in an isothermal process

$$\Delta T = 0. \quad (12.1)$$

For an ideal gas, we showed in eqn 11.29 that $\mathrm{d}U = C_V\mathrm{d}T$, and so this means that for an isothermal change

$$\Delta U = 0, \quad (12.2)$$

since $U$ is a function of temperature only. Equation 12.2 implies that $\mathrm{d}U = 0$ and hence from eqn 11.7

$$\mathrm{d}W = -\mathrm{d}Q, \quad (12.3)$$

so that the work done by the gas on its surroundings as it expands is equal to the heat absorbed by the gas. We can use $\mathrm{d}W = - p\mathrm{d}V$ (eqn 11.9), which is the correct expression for the work done in a reversible expansion. Hence the heat absorbed by the gas during an isothermal expansion from volume $V_{1}$ to volume $V_{2}$ of 1 mole of an ideal gas at temperature $T$ is

$$\begin{array}{rcl}{\Delta Q} & = & {\int \mathrm{d}Q}\\ {} & {} & {}\\ {} & = & {-\int \mathrm{d}W}\\ {} & {} & {}\\ {} & = & {\int_{V_1}^{V_2}p\mathrm{d}V}\\ {} & {} & {}\\ {} & = & {\int_{V_1}^{V_{2}}\frac{RT}{V}\mathrm{d}V}\\ {} & {} & {}\\ {} & = & {RT\ln \frac{V_2}{V_1}.} \end{array} \quad (12.8)$$

For an expansion, $V_{2} > V_{1}$, and so $\Delta Q > 0$. The internal energy has stayed the same, but the volume has increased so that the energy density has gone down. The energy density and the pressure are proportional to one another, so that pressure will also have decreased.

===== Page 121 =====

## 12.3 Adiabatic expansion of an ideal gas

The word adiathermal means "without flow of heat". A system bounded by adiathermal walls is said to be thermally isolated. Any work done on such a system produces an adiathermal change. We define a change to be adiabatic if it is both adiathermal and reversible. In an adiabatic expansion, therefore, there is no flow of heat and we have

$$\mathrm{d}Q = 0. \quad (12.9)$$

The first law of thermodynamics therefore implies that

$$\mathrm{d}U = \mathrm{d}W. \quad (12.10)$$

For an ideal gas, $\mathrm{d}U = C_V\mathrm{d}T$, and using $\mathrm{d}W = - p\mathrm{d}V$ for a reversible change, we find that, for 1 mole of ideal gas,

$$C_V\mathrm{d}T = -p\mathrm{d}V = -\frac{RT}{V}\mathrm{d}V, \quad (12.11)$$

so that

$$\ln \frac{T_2}{T_1} = -\frac{R}{C_V}\ln \frac{V_2}{V_1}. \quad (12.12)$$

Now $C_p = C_V + R$, and dividing this by $C_V$ yields

$$\gamma = \frac{C_p}{C_V} = 1 + \frac{R}{C_V}, \quad (12.13)$$

and therefore $-(R / C_V) = 1 - \gamma$, so that eqn 12.12 becomes

$$T V^{\gamma -1} = \mathrm{constant}, \quad (12.14)$$

or equivalently (using $pV\propto T$ for an ideal gas)

$$p^{1 - \gamma}T^{\gamma} = \mathrm{constant} \quad (12.15)$$

and

$$pV^{\gamma} = \mathrm{constant}, \quad (12.16)$$

the last equation probably being the most memorable.

Figure 12.1 shows isotherms (lines of constant temperature, as would be followed in an isothermal expansion) and adiabats (lines followed by an adiabatic expansion in which heat cannot enter or leave the system) for an ideal gas on a graph of pressure against volume. At each point, the adiabats have a steeper gradient than the isotherms, a fact we will return to in a later chapter.

[Image: A graph of p versus V showing several isotherms (solid curves) and adiabats (dashed curves). The adiabats are steeper than the isotherms.]
**Fig. 12.1** Isotherms (solid lines) and adiabats (dashed lines).

## 12.4 Adiabatic atmosphere

The hydrostatic equation (eqn 4.23) expresses the additional pressure due to a thickness $\mathrm{d}z$ of atmosphere with density $\rho$ and is

$$\mathrm{d}p = -\rho g\mathrm{d}z. \quad (12.17)$$

===== Page 122 =====

Since $p = nk_{\mathrm{B}}T$ and $\rho = nm$, where $m$ is the mass of one molecule, we can write $\rho = mp / k_{\mathrm{B}}T$ and hence

$$\frac{\mathrm{d}p}{\mathrm{d}z} = -\frac{mgp}{k_{\mathrm{B}}T}, \quad (12.18)$$

which implies that

$$T\frac{\mathrm{d}p}{p} = -\frac{mg}{k_{\mathrm{B}}}\mathrm{d}z. \quad (12.19)$$

For an isothermal atmosphere, $T$ is a constant, and one obtains the results of Example 4.4. This assumes that the whole atmosphere is at a uniform temperature, which is unrealistic. A much better approximation (although nevertheless still an approximation to reality) is that each parcel of air does not exchange heat with its surroundings. This means that if a parcel of air rises, it expands adiabatically. In this case, eqn 12.19 can be solved by recalling that for an adiabatic expansion $p^{1 - \gamma}T^{\gamma}$ is a constant (see eqn 12.15) and hence that

$$(1 - \gamma)\frac{\mathrm{d}p}{p} +\gamma \frac{\mathrm{d}T}{T} = 0. \quad (12.20)$$

Substituting this into eqn 12.19 yields

$$\frac{\mathrm{d}T}{\mathrm{d}z} = -\left(\frac{\gamma - 1}{\gamma}\right)\frac{mg}{k_{\mathrm{B}}}, \quad (12.21)$$

which is an expression relating the rate of decrease of temperature with height, predicting it to be linear. We can rewrite $(\gamma - 1) / \gamma = R / C_{p}$ and using $R = N_{\mathrm{A}}k_{\mathrm{B}}$ and writing the molar mass $M_{\mathrm{molar}} = N_{\mathrm{A}}m$ we can write eqn 12.21 as

$$\frac{\mathrm{d}T}{\mathrm{d}z} = -\frac{M_{\mathrm{molar}}g}{C_p}. \quad (12.22)$$

The quantity $M_{\mathrm{molar}}g / C_p$ is known as the adiabatic lapse rate. For dry air (mostly nitrogen), it comes out as $9.7 \mathrm{K} \mathrm{km}^{-1}$. Experimental values in the atmosphere are closer to $6 - 7 \mathrm{K} \mathrm{km}^{-1}$ (partly because the atmosphere isn't dry, and latent heat effects, due to the heat needed to evaporate water droplets [and sometimes that ice crystals], are also important).

[Image: A diagram of Richhardt's apparatus. A ball of mass m oscillates in a tube. The tube is connected to a container of gas of volume V and pressure p. The pressure outside is p0.]
**Fig. 12.2** Richhardt's apparatus for measuring $\gamma$. A ball of mass $m$ oscillates up and down inside a tube.

===== Page 123 =====

## Chapter summary

- In an isothermal expansion $\Delta T = 0$.
- An adiabatic change is both adiathermal (no flow of heat) and reversible. In an adiabatic expansion of an ideal gas, $pV^{\gamma}$ is constant.

## Exercises

(12.1) In an adiabatic expansion of an ideal gas, $pV^{\gamma}$ is constant. Show also that

$$\begin{array}{rcl}{TV^{\gamma -1}} & = & {\mathrm{constant},}\\ {T} & = & {\mathrm{constant}\times p^{1 - 1 / \gamma}.} \end{array} \quad (12.24)$$

(12.2) Assume that gases behave according to a law given by $pV = f(T)$, where $f(T)$ is a function of temperature. Show that this implies

$$\left(\frac{\partial p}{\partial T}\right)_V = \frac{1}{V}\frac{\mathrm{d}f}{\mathrm{d}T}, \quad (12.25)$$

$$\left(\frac{\partial V}{\partial T}\right)_p = \frac{1}{p}\frac{\mathrm{d}f}{\mathrm{d}T}, \quad (12.26)$$

Show also that

$$\left(\frac{\partial Q}{\partial V}\right)_p = C_p\left(\frac{\partial T}{\partial V}\right)_p, \quad (12.27)$$

and

$$\left(\frac{\partial Q}{\partial p}\right)_V = C_V\left(\frac{\partial T}{\partial p}\right)_V. \quad (12.28)$$

In an adiabatic change, we have that

$$\mathrm{d}Q = \left(\frac{\partial Q}{\partial p}\right)_V\mathrm{d}p + \left(\frac{\partial Q}{\partial V}\right)_p\mathrm{d}V = 0. \quad (12.29)$$

Hence show that $pV^{\gamma}$ is a constant.

(12.3) Explain why we can write

$$\begin{array}{rcl}{\mathrm{d}Q} & = & {C_p\mathrm{d}T + A\mathrm{d}p\quad \mathrm{and}}\\ {\mathrm{d}Q} & = & {C_V\mathrm{d}T + B\mathrm{d}V,} \end{array} \quad (12.31)$$

where $A$ and $B$ are constants. Subtract these equations and show that

$$(C_p - C_V)\mathrm{d}T = B\mathrm{d}V - A\mathrm{d}p, \quad (12.32)$$

and that at constant temperature

$$\left(\frac{\partial p}{\partial V}\right)_T = \frac{B}{A}. \quad (12.33)$$

In an adiabatic change, show that

$$\begin{array}{rcl}{\mathrm{d}p} & = & {-(C_p / A)\mathrm{d}T,}\\ {\mathrm{d}V} & = & {-(C_V / B)\mathrm{d}T.} \end{array} \quad (12.34)$$

Hence show that in an adiabatic change, we have that

$$\begin{array}{rcl}{\left(\frac{\partial p}{\partial V}\right)_{\mathrm{adiabatic}}} & = & {\gamma \left(\frac{\partial p}{\partial V}\right)_T,}\\ {\left(\frac{\partial V}{\partial T}\right)_{\mathrm{adiabatic}}} & = & {\frac{1}{1 - \gamma}\left(\frac{\partial V}{\partial T}\right)_p,}\\ {\left(\frac{\partial p}{\partial T}\right)_{\mathrm{adiabatic}}} & = & {\frac{\gamma}{\gamma - 1}\left(\frac{\partial p}{\partial T}\right)_V.} \end{array} \quad (12.36)$$

(12.4) Using eqn 12.36, relate the gradients of adiabats and isotherms on a $p - V$ diagram.

(12.5) Two thermally insulated cylinders, A and B, of equal volume, both equipped with pistons, are connected by a valve. Initially A has its piston fully withdrawn and contains a perfect monatomic gas at temperature $T$, while B has its piston fully inserted, and the valve is closed. Calculate the final temperature of the gas after the following operations, which each start with the same initial arrangement. The thermal capacity of the cylinders is to be ignored.

(a) The valve is fully opened and the gas slowly drawn into B by pulling out the piston B; piston A remains stationary.

(b) Piston B is fully withdrawn and the valve is opened slightly; the gas is then driven as far as it will go into B by pushing home piston A at such a rate that the pressure in A remains constant: the cylinders are in thermal contact.

(12.6) In Richhardt's method of measuring $\gamma$, illustrated in Fig. 12.2, a ball of mass $m$ is placed snugly inside a tube (cross-sectional area $A$) connected to a container of gas (volume $V$). The pressure $p$ of the gas inside the container is slightly greater than atmospheric pressure $p_0$ because of the downwards force of the ball, so that

$$p = p_0 + \frac{mg}{A}. \quad (12.39)$$

Show that if the ball is given a slight downwards displacement, it will undergo simple harmonic motion with period $\tau$ given by

$$\tau = 2\pi \sqrt{\frac{mV}{\gamma pA^2}}. \quad (12.40)$$

[You may neglect friction. As the oscillations are fairly rapid, the changes in $p$ and $V$ that occur can be treated as occurring adiabatically.]

In Rinkel's 1929 modification of this experiment, the ball is held in position in the neck where the gas pressure $p$ in the container is exactly equal to air pressure, and then let drop, the distance $L$ that it falls before it starts to go up again is measured. Show that this distance is given by

$$mgL = \frac{\gamma pA^2L^2}{8V}. \quad (12.41)$$

===== Page 125 =====

# Part V

## The second law

In this part we introduce the second law of thermodynamics and follow its consequences. This part is structured as follows:

In Chapter 13, we consider heat engines, which are cyclic processes that convert heat into work. We state various forms of the second law of thermodynamics and prove their equivalence, in particular showing that no engine can be more efficient than a Carnot engine. We also prove Clausius' theorem, which applies to any cyclic process. In Chapter 14 we show how the results from the preceding chapter lead to the concept of entropy. We derive the important equation $\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V$, which combines the first and second laws of thermodynamics. We also introduce the Joule expansion and use it to discuss the statistical interpretation of entropy and Maxwell's demon. There is a very deep connection between entropy and information, and we explore this in Chapter 15, briefly touching on data compression and quantum information.

===== Page 126 =====

# 13 Heat engines and the second law

13.1 The second law of thermodynamics  126
13.2 The Carnot engine  127
13.3 Carnot's theorem  130
13.4 Equivalence of Clausius' and Kelvin's statements  131
13.5 Examples of heat engines  131
13.6 Heat engines running backwards  133
13.7 Clausius' theorem  134
Chapter summary  137
Further reading  137
Exercises  137

A reservoir in this context is a body, which is sufficiently large that we can consider it to have essentially infinite heat capacity. This means that you can keep sucking heat out of it, or dumping heat into it, without its temperature changing. See Section 4.6.

In this chapter, we introduce the second law of thermodynamics, probably the most important and far-reaching of all concepts in thermal physics. We are going to illustrate it with an application to the theory of "heat engines", which are machines that produce work from a temperature difference between two reservoirs. It was by considering these engines that such nineteenth century physicists as Carnot, Clausius and Kelvin came to develop their different statements of the second law of thermodynamics. However, as we will see in subsequent chapters, the second law of thermodynamics has a wider applicability, affecting all types of processes in large systems and bringing insights in information theory and cosmology. In this chapter, we will begin by stating two alternative forms of the second law of thermodynamics and then discuss how these statements impact on the efficiency of heat engines.

## 13.1 The second law of thermodynamics

The second law of thermodynamics can be formulated as a statement about the direction of heat flow that occurs as a system approaches equilibrium (and hence there is a connection with the direction of the "arrow of time"). Heat is always observed to flow from a hot body to a cold body, and the reverse process, in isolation, never occurs. Therefore, following Clausius, we can state the second law of thermodynamics as follows:

**Clausius' statement of the second law of thermodynamics**
"No process is possible whose sole result is the transfer of heat from a colder to a hotter body."

It turns out that an equivalent statement of the second law of thermodynamics can be made, concerning how easy it is to change energy between different forms, in particular between work and heat. It is very easy to convert work into heat. For example, pick up a brick of mass $m$ and carry it up to the top of a building of height $h$ (thus doing work on it equal to $mgh$) and then let it fall back to ground level by dropping it off the top (being careful not to hit passing pedestrians). All the work that you've done in carrying the brick to the top of the building will be dissipated in heat (and a small amount of sound energy) as the brick hits the ground. However, conversion of heat into work is much harder, and in fact the complete conversion of heat into work is impossible. This point is expressed in Kelvin's statement of the second law of thermodynamics:

**Kelvin's statement of the second law of thermodynamics:**
"No process is possible whose sole result is the complete conversion of heat into work."

These two statements of the second law of thermodynamics do not seem to be obviously connected, but the equivalence of these two statements will be shown in Section 13.4.

## 13.2 The Carnot engine

Kelvin's statement of the second law of thermodynamics says that you can't completely convert heat into work. However, it does not forbid some conversion of heat into work. How good a conversion from heat to work is possible? To answer this question, we have to introduce the concept of an engine. We define an engine as a system operating a cyclic process that converts heat into work. It has to be cyclic so that it can be continuously operated, producing a steady power.

[Image: A p-V diagram showing a Carnot cycle. It consists of two isotherms (AB and CD) and two adiabats (BC and DA). The cycle is traversed clockwise A -> B -> C -> D -> A.]
**Fig. 13.1** A Carnot cycle consists of two reversible adiabats (BC and DA) and two reversible isotherms (AB and CD). The Carnot cycle is here shown on a $p - V$ plot. It is operated in the direction A→B→C→D→A, i.e., clockwise around the solid curve. Heat $Q_{\mathrm{h}}$ enters in the isotherm A→B and heat $Q_{\ell}$ leaves in the isotherm C→D.

[Image: A T-S diagram for a Carnot cycle. The cycle is a rectangle. The top isotherm is at T_h, the bottom isotherm at T_l. Heat Q_h enters along the top isotherm A->B. Heat Q_l leaves along the bottom isotherm D->C.]
**Fig. 13.2** A Carnot cycle can be drawn on replotted axes where the isotherms are shown as horizontal lines ( $T$ is constant for an isotherm) and the adiabats are shown as vertical lines (where the quantity $S$, which must be some function of $pV^{\gamma}$, is constant in an adiabatic expansion; in Chapter 14 we will give a physical interpretation of $S$).

One such engine is the Carnot engine, which is based on a process called a Carnot cycle and which is illustrated in Fig. 13.1. An equivalent plot which is easier to sketch is shown in Fig. 13.2. The Carnot cycle consists of two reversible adiabats and two reversible isotherms for an ideal gas. The engine operates between two heat reservoirs, one at a higher temperature $T_{\mathrm{h}}$ and one at a lower temperature $T_{\ell}$. Heat enters and leaves only during the reversible isotherms (because no heat can enter or leave during an adiabat). Heat $Q_{\mathrm{h}}$ enters during the expansion A→B and heat $Q_{\ell}$ leaves during the compression C→D. Because the process is cyclic, the change of internal energy (a state function) in going round the cycle is zero. Hence the work output by the engine, $W$, is given by

$$W = Q_{\mathrm{h}} - Q_{\ell}. \quad (13.1)$$

## Example 13.1

Find an expression for $Q_{\mathrm{h}} / Q_{\ell}$ for an ideal gas undergoing a Carnot cycle in terms of the temperatures $T_{\mathrm{h}}$ and $T_{\ell}$.

Solution:

Using the results of Section 12.2, we can write down

$$\begin{array}{rcl}{{\bf A}}&{{\bf B}:}&{{Q_{\mathrm{h}}=RT_{\mathrm{h}}\ln\frac{V_{\mathrm{B}}}{V_{\mathrm{A}}}}},\\{{\bf B}}&{{\bf C}:}&{{\left(\frac{T_{\mathrm{h}}}{T_{\ell}}\right)=\left(\frac{V_{\mathrm{C}}}{V_{\mathrm{B}}}\right)^{\gamma-1}}},\\{{\bf C}}&{{\bf D}:}&{{Q_{\ell}=-RT_{\ell}\ln\frac{V_{\mathrm{D}}}{V_{\mathrm{C}}}}},\\{{\bf D}}&{{\bf A}:}&{{\left(\frac{T_{\ell}}{T_{\mathrm{h}}}\right)=\left(\frac{V_{\mathrm{A}}}{V_{\mathrm{D}}}\right)^{\gamma-1}}}. \end{array} \quad (13.5)$$

Equations 13.3 and 13.5 lead to

$$\frac{V_{\mathrm{B}}}{V_{\mathrm{A}}} = \frac{V_{\mathrm{C}}}{V_{\mathrm{D}}}, \quad (13.6)$$

and dividing eqn 13.2 by eqn 13.4 and substituting in eqn 13.6 leads to

$$\frac{Q_{\mathrm{h}}}{Q_{\ell}} = \frac{T_{\mathrm{h}}}{T_{\ell}}. \quad (13.7)$$

This is a key result.

[Image: A schematic diagram of a Carnot engine. A circle labeled "Carnot" has an input arrow Q_h from a hot reservoir at T_h, an output arrow W for work, and an output arrow Q_l to a cold reservoir at T_l.]
**Fig. 13.3** A Carnot engine shown schematically. In diagrams such as this one, the arrows are labelled with the heat and work flowing in one cycle of the engine.

The Carnot engine is shown schematically in Fig. 13.3. It is drawn as a machine with heat input $Q_{\mathrm{h}}$ from a reservoir at temperature $T_{\mathrm{h}}$ drawn as a horizontal line, and two outputs, one of work $W$ and the other of heat $Q_{\ell}$, which passes into the reservoir at temperature $T_{\ell}$.

The concept of efficiency is important to characterize engines. It is the ratio of "what you want to achieve" to "what you have to do to achieve it". For an engine, what you want to achieve is work (to pull a train up a hill for example) and what you have to do to achieve it is to put heat in (by shovelling coal into the furnace), keeping the hot reservoir at $T_{\mathrm{h}}$ and providing heat $Q_{\mathrm{h}}$ for the engine. We therefore define the efficiency $\eta$ of an engine as the ratio of the work out to the heat in. Thus

$$\eta = \frac{W}{Q_{\mathrm{h}}} \quad (13.8)$$

Note that since the work out cannot be greater than the heat in (i.e., $W< Q_{\mathrm{h}}$) we must have that $\eta < 1$. The efficiency must be below $100\%$.

## Example 13.2

For the Carnot engine, the efficiency can be calculated using eqns 13.1, 13.7, and 13.8 as follows: substituting eqn 13.1 into 13.8 yields

$$\eta_{\mathrm{Carnot}} = \frac{Q_{\mathrm{h}} - Q_{\ell}}{Q_{\mathrm{h}}}, \quad (13.9)$$

and eqn 13.7 then implies that

$$\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}} - T_{\ell}}{T_{\mathrm{h}}} = 1 - \frac{T_{\ell}}{T_{\mathrm{h}}}. \quad (13.10)$$

How does this efficiency compare to that of a real engine? It turns out that real engines are much less efficient than Carnot engines.

## Example 13.3

A power station steam turbine operates between $T_{\mathrm{h}} \sim 800 \mathrm{~K}$ and $T_{\ell} = 300 \mathrm{~K}$. If it were a Carnot engine, it could achieve an efficiency of $\eta_{\mathrm{Carnot}} = (T_{\mathrm{h}} - T_{\ell}) / T_{\mathrm{h}} \approx 60\%$, but in fact real power stations do not achieve the maximum efficiency and figures closer to $40\%$ are typical.

===== Page 130 =====

## 13.3 Carnot's theorem

The Carnot engine is in fact the most efficient engine possible! This is stated in Carnot's theorem, as follows:

## Carnot's theorem

Of all the heat engines working between two given temperatures, none is more efficient than a Carnot engine.

Remarkably, one can prove Carnot's theorem on the basis of Clausius' statement of the second law of thermodynamics. The proof follows a reductio ad absurdum argument.

[Image: A schematic diagram showing engine E connected to a Carnot engine running backwards. Engine E takes heat Q_h' from T_h, outputs work W, and rejects heat Q_l' to T_l. The Carnot engine takes work W, takes heat Q_l from T_l, and dumps heat Q_h to T_h.]
**Fig. 13.4** A hypothetical engine E, which is more efficient than a Carnot engine, is connected to a Carnot engine.

Proof: Imagine that E is an engine that is more efficient than a Carnot engine (i.e., $\eta_{\mathrm{E}} > \eta_{\mathrm{Carnot}}$). The Carnot engine is reversible so one can run it in reverse. Engine E, and a Carnot engine run in reverse, are connected together as shown in Fig. 13.4. Now since $\eta_{\mathrm{E}} > \eta_{\mathrm{Carnot}}$, we have that

$$\frac{W}{Q_{\mathrm{h}}^{\prime}} > \frac{W}{Q_{\mathrm{h}}}, \quad (13.11)$$

and so

$$Q_{\mathrm{h}} > Q_{\mathrm{h}}^{\prime}. \quad (13.12)$$

The first law of thermodynamics implies that

$$W = Q_{\mathrm{h}}^{\prime} - Q_{\ell}^{\prime} = Q_{\mathrm{h}} - Q_{\ell}, \quad (13.13)$$

so that

$$Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime} = Q_{\ell} - Q_{\ell}^{\prime}. \quad (13.14)$$

Now $Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime}$ is positive because of eqn 13.12, and therefore so is $Q_{\ell} - Q_{\ell}^{\prime}$. The expression $Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime}$ is the net amount of heat dumped into the reservoir at temperature $T_{\mathrm{h}}$. The expression $Q_{\ell} - Q_{\ell}^{\prime}$ is the net amount of heat extracted from the reservoir at temperature $T_{\ell}$. Because both these expressions are positive, the combined system shown in Fig. 13.4 simply extracts heat from the reservoir at $T_{\ell}$ and dumps it into the reservoir at $T_{\mathrm{h}}$. This violates Clausius' statement of the second law of thermodynamics, and therefore engine E cannot exist.

[Image: A schematic diagram showing a Carnot engine connected to a reversible engine R running backwards. The Carnot engine takes heat Q_h from T_h, outputs work W, and rejects heat Q_l to T_l. Engine R takes work W, takes heat Q_l' from T_l, and dumps heat Q_h' to T_h.]
**Fig. 13.5** A hypothetical reversible engine R is connected to a Carnot engine.

Corollary: All reversible engines working between two temperatures have the same efficiency $\eta_{\mathrm{Carnot}}$.

Proof: Imagine another reversible engine R. Its efficiency $\eta_{\mathrm{R}} \leq \eta_{\mathrm{Carnot}}$ by Carnot's theorem. We run it in reverse and connect it to a Carnot engine going forwards, as shown in Fig. 13.5. This arrangement will simply transfer heat from the cold reservoir to the hot reservoir and violates Clausius' statement of the second law of thermodynamics unless $\eta_{\mathrm{R}} = \eta_{\mathrm{Carnot}}$. Therefore all reversible engines have the same efficiency

$$\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}} - T_{\ell}}{T_{\mathrm{h}}}. \quad (13.15)$$

===== Page 131 =====

## 13.4 Equivalence of Clausius' and Kelvin's statements

We first prove the proposition that if a system violates Kelvin's statement of the second law of thermodynamics, it violates Clausius' statement of the second law of thermodynamics.

Proof: If a system violates Kelvin's statement of the second law of thermodynamics, one could connect it to a Carnot engine as shown in Fig. 13.6. The first law implies that

$$Q_{\mathrm{h}}^{\prime} = W \quad (13.16)$$

and that

$$Q_{\mathrm{h}} = W + Q_{\ell}. \quad (13.17)$$

The heat dumped in the reservoir at temperature $T_{\mathrm{h}}$ is

$$Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime} = Q_{\ell}. \quad (13.18)$$

This is also equal to the heat extracted from the reservoir at temperature $T_{\ell}$. The combined process therefore has the net result of transferring heat $Q_{\ell}$ from the reservoir at $T_{\ell}$ to the reservoir at $T_{\mathrm{h}}$ as its sole effect and thus violates Clausius' statement of the second law of thermodynamics. Therefore the Kelvin violator does not exist.

We now prove the opposite proposition, that if a system violates Clausius' statement of the second law of thermodynamics, it violates Kelvin's statement of the second law of thermodynamics.

Proof: If a system violates Clausius' statement of the second law of thermodynamics, one could connect it to a Carnot engine as shown in Fig. 13.7. The first law implies that

$$Q_{\mathrm{h}} - Q_{\ell} = W. \quad (13.19)$$

The sole effect of this process is thus to convert heat $Q_{\mathrm{h}} - Q_{\ell}$ into work and thus violates Kelvin's statement.

We have thus shown the equivalence of Clausius' and Kelvin's statements of the second law of thermodynamics.

[Image: A schematic diagram showing a Kelvin violator connected to a Carnot engine. The Kelvin violator takes heat Q_h' and outputs work W. The Carnot engine takes work W, takes heat Q_l from T_l, and dumps heat Q_h to T_h.]
**Fig. 13.6** A Kelvin violator is connected to a Carnot engine.

[Image: A schematic diagram showing a Clausius violator connected to a Carnot engine. The Clausius violator takes heat Q_l from T_l and dumps it to T_h. The Carnot engine takes heat Q_h from T_h, outputs work W, and rejects heat Q_l to T_l.]
**Fig. 13.7** A Clausius violator is connected to a Carnot engine.

## 13.5 Examples of heat engines

One of the first engines to be constructed was made in the first century by Hero of Alexandria, and is sketched in Fig. 13.8(a). It consists of a hollow sphere with a pair of bent pipes projecting from it. Steam is fed via another pair of pipes and once expelled through the bent pipes causes rotational motion. Though Hero's engine convincingly converts heat into work, and thus qualifies as a bona fide heat engine, it was little more than an entertaining toy. More practical was the engine sketched in Fig. 13.8(b), which was designed by Thomas Newcomen (1664-1729). This was one of the first practical steam engines and was used for pumping water out of mines. Steam is used to push the piston upwards. Then cold water is injected from the tank and condenses the steam, reducing the pressure in the piston. Atmospheric pressure then pushes the piston down and raises the beam on the other side of the fulcrum. The problem with Newcomen's engine was that one had then to heat up the steam chamber again before steam could be readmitted and so it was extremely inefficient. James Watt (1736-1819) famously improved the design so that condensation took place in a separate chamber, which was connected to the steam cylinder by a pipe. This work led the foundation of the industrial revolution.

[Image: Sketches of three engines. (a) Hero's engine: a sphere with bent pipes that rotates when steam is expelled. (b) Newcomen's engine: a beam engine with a piston and a separate boiler. (c) Stirling's engine: a hot and cold cylinder arrangement driving a flywheel.]
**Fig. 13.8** Sketches of (a) Hero's engine, (b) Newcomen's engine, and (c) Stirling's engine.

Another design of an engine is Stirling's engine, the brainchild of the Rev. Robert Stirling (1790-1878), which is sketched in Fig. 13.8(c). It works purely by the repeated heating and cooling of a sealed amount of gas. In the particular engine shown in Fig. 13.8(c), the crankshaft is driven by the two pistons in an oscillatory fashion, but the $90^{\circ}$ bend ensures that the two pistons move out of phase. The motion is driven by a temperature differential between the top and bottom surfaces of the engine. The design is very simple and contains no valves and operates at relatively low pressures. However, such an engine literally has to "warm up" to establish the temperature differential and so it is harder to regulate power output.

One of the most popular engines is the internal combustion engine used in most automobile applications. Rather than externally heating water to produce steam (as with Newcomen's and Watt's engines) or to produce a temperature differential (as with Stirling's engine), here the burning of fuel inside the engine's combustion chamber generates the high temperature and pressure necessary to produce useful work. Different fuels can be used to drive these engines, including diesel, gasoline, natural gas, and even biofuels, such as ethanol. These engines all produce carbon dioxide, and this has important consequences for Earth's atmosphere, as we shall discuss in Chapter 37. There are many different types of internal combustion engines, including piston engines (in which pressure is converted into rotating motion using a set of pistons), combustion turbines (in which gas flow is used to spin a turbine's blades), and jet engines (in which a fast moving jet of gas is used to generate thrust).

[Image: A schematic diagram of a heat engine running backwards (a refrigerator or heat pump). An input of work W into the engine allows heat Q_l to be taken from a cold reservoir T_l and heat Q_h to be dumped into a hot reservoir T_h.]
**Fig. 13.9** A refrigerator or a heat pump. Both devices are heat engines run in reverse (i.e., reversing the arrows on the cycle shown in Fig. 13.3).

## 13.6 Heat engines running backwards

In this section we discuss two applications of heat engines in which the engine is run in reverse, putting in work to move heat around.

## Example 13.4

### (a) The refrigerator

The refrigerator is a heat engine that is run backwards so that you put work in and cause a heat flow from a cold reservoir to a hot reservoir (see Fig. 13.9). In this case, the cold reservoir is the food inside the refrigerator that you wish to keep cold and the hot reservoir is usually your kitchen. For a refrigerator, we must define the efficiency in a different way from the efficiency of a heat engine. This is because what you want to achieve is "heat sucked out of the contents of the refrigerator" and what you have to do to achieve it is "electrical work" from the mains electricity supply. Thus we define the efficiency of a refrigerator as

$$\eta = \frac{Q_{\ell}}{W}. \quad (13.20)$$

For a refrigerator fitted with a Carnot engine, it is then easy to show that

$$\eta_{\mathrm{Carnot}} = \frac{T_{\ell}}{T_{\mathrm{h}} - T_{\ell}}, \quad (13.21)$$

which can yield an efficiency above $100\%$.

### (b) The heat pump

A heat pump is essentially a refrigerator (Fig. 13.9 applies also for a heat pump), but it is utilized in a different way. It is used to pump heat from a reservoir, to a place where it is desired to add heat. For example, the reservoir could be the soil/rock several metres underground and heat could be pumped out of the reservoir into a house which needs heating. In one cycle of the engine, we want to add heat $Q_{\mathrm{h}}$ to the house, and now $W$ is the work we must apply (in the form of electrical work) to accomplish this. The efficiency of a heat pump is therefore defined as

$$\eta = \frac{Q_{\mathrm{h}}}{W}. \quad (13.22)$$

Note that $Q_{\mathrm{h}} > W$ and so $\eta > 1$. The efficiency is always above $100\%$ (See Exercise 13.1.) This shows why heat pumps are attractive for heating. It is always possible to turn work into heat with $100\%$ efficiency (an electric fire turns electrical work into heat in this way), but a heat pump can allow you to get even more heat into your house for the same electrical work (and hence for the same electricity bill!).

For a heat pump fitted with a Carnot engine, it is easy to show that

$$\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}}}{T_{\mathrm{h}} - T_{\ell}}. \quad (13.23)$$

## 13.7 Clausius' theorem

Consider a Carnot cycle. In one cycle, heat $Q_{\mathrm{h}}$ enters and heat $Q_{\ell}$ leaves. Heat is therefore not a conserved quantity of the cycle. However, we found in eqn 13.7 that for a Carnot cycle

$$\frac{Q_{\mathrm{h}}}{Q_{\ell}} = \frac{T_{\mathrm{h}}}{T_{\ell}}, \quad (13.24)$$

and so if we define $\Delta Q_{\mathrm{rev}}$ as the heat entering the system at each point, we have that

$$\sum_{\mathrm{cycle}}\frac{\Delta Q_{\mathrm{rev}}}{T} = \frac{Q_{\mathrm{h}}}{T_{\mathrm{h}}} +\frac{(-Q_{\ell})}{T_{\ell}} = 0, \quad (13.25)$$

and so $\Delta Q_{\mathrm{rev}} / T$ sums to zero around the cycle. Replacing the sum by an integral, we could write

$$\oint \frac{\mathrm{d}Q_{\mathrm{rev}}}{T} = 0 \quad (13.26)$$

for this Carnot cycle.

Our argument so far has been in terms of a Carnot cycle operating between two distinct heat reservoirs. Real engine cycles can be much more complicated than this in that their "working substance" changes temperature in a much more complicated way and, moreover, real engines do not behave perfectly reversibly. Therefore we would like to generalize our treatment so that it can be applied to a general cycle operating between a whole series of reservoirs and we would like the cycle to be either reversible or irreversible. Our general cycle is illustrated in Fig. 13.10(a). For this cycle, heat $\mathrm{d}Q_{i}$ enters at a particular part of the cycle. At this point the system is connected to a reservoir, which is at temperature $T_{i}$. The total work extracted from the cycle is $\Delta W$, given by

$$\Delta W = \sum_{\mathrm{cycle}}\mathrm{d}Q_{i}, \quad (13.27)$$

from the first law of thermodynamics. The sum here is taken around the whole cycle, indicated schematically by the dotted circle in Fig. 13.10(a).

[Image: (a) A general cycle in the p-V plane. Heat dQ_i enters from a reservoir at T_i. Work Delta W is extracted. (b) The same cycle, but the heat dQ_i is supplied via a Carnot engine C_i operating between a common reservoir at T and the reservoir at T_i.]
**Fig. 13.10** (a) A general cycle in which heat $\mathrm{d}Q_{i}$ enters in part of the cycle from a reservoir at temperature $T_{i}$. Work $\Delta W$ is extracted from each cycle. (b) The same cycle, but showing the heat $\mathrm{d}Q_{i}$ entering the reservoir at $T_{i}$ from a reservoir at temperature $T$ via a Carnot engine (labelled $C_{i}$).

Next we imagine that the heat at each point is supplied via a Carnot engine, which is connected between a reservoir at temperature $T$ and the reservoir at temperature $T_{i}$ (see Fig. 13.10(b)). The reservoir at $T$ is common for all the Carnot engines connected at all points of the cycle. Each Carnot engine produces work $\mathrm{d}W_{i}$, and for a Carnot engine we know that

$$\frac{\mathrm{heat~to~reservoir~at~}T_{i}}{T_{i}} = \frac{\mathrm{heat~from~reservoir~at~}T}{T}, \quad (13.28)$$

and hence

$$\frac{\mathrm{d}Q_{i}}{T_{i}} = \frac{\mathrm{d}Q_{i} + \mathrm{d}W_{i}}{T}. \quad (13.29)$$

Rearranging, we have that

$$\mathrm{d}W_{i} = \mathrm{d}Q_{i}\left(\frac{T}{T_{i}} -1\right). \quad (13.30)$$

The thermodynamic system in Fig. 13.10(b) looks at first sight to do nothing other than convert heat to work, which is not allowed according to Kelvin's statement of the second law of thermodynamics, and hence we must insist that this is not the case. Hence

$$\mathrm{total~work~produced~per~cycle} = \Delta W + \sum_{\mathrm{cycle}}\mathrm{d}W_{i}\leq 0. \quad (13.31)$$

Using eqns 13.27, 13.30, and 13.31, we therefore have that

$$T\sum_{\mathrm{cycle}}\frac{\mathrm{d}Q_i}{T_i}\leq 0. \quad (13.32)$$

Since $T > 0$, we have that

$$\sum_{\mathrm{cycle}}\frac{\mathrm{d}Q_i}{T_i}\leq 0, \quad (13.33)$$

and replacing the sum by an integral, we can write this as

$$\oint \frac{\mathrm{d}Q}{T}\leq 0, \quad (13.34)$$

which is known as the Clausius inequality, embodied in the expression of Clausius' theorem:

**Clausius' theorem** For any closed cycle, $\oint \frac{\mathrm{d}Q}{T}\leq 0$, where equality necessarily holds for a reversible cycle.

## Example 13.5

Two bodies with temperature-independent heat capacities $C_h$ and $C_\ell$ are used as reservoirs for a Carnot heat engine (see Fig. 13.11). Derive an expression for the total work obtainable.

Solution: In an infinitesimal change we have that

$$\begin{array}{rcl}{\mathrm{d}Q_{\mathrm{h}}} & = & {-C_{\mathrm{h}}\mathrm{d}T_{\mathrm{h}}}\\ {\mathrm{d}Q_{\ell}} & = & {C_{\ell}\mathrm{d}T_{\ell},} \end{array} \quad (13.36)$$

and for a Carnot engine we have that

$$\frac{\mathrm{d}Q_{\mathrm{h}}}{T_{\mathrm{h}}} = \frac{\mathrm{d}Q_{\ell}}{T_{\ell}}, \quad (13.37)$$

and integrating gives $\begin{array}{r}{T_{\ell}^{T_{\ell}}\frac{\mathrm{d}Q_{\ell}}{T_{\ell}} = -\int_{T_{\mathrm{h}}}^{T_{\mathrm{f}}}\frac{\mathrm{d}Q_{\mathrm{h}}}{T_{\mathrm{h}}}} \end{array}$ and hence

$$C_{\ell}\ln \frac{T_{\mathrm{f}}}{T_{\ell}} = -C_{\mathrm{h}}\ln \frac{T_{\mathrm{f}}}{T_{\mathrm{h}}}, \quad (13.38)$$

where $T_{\mathrm{f}}$ is the final temperature of each reservoir. Thus

$$T_{\mathrm{f}}^{C_{\mathrm{h}} + C_{\ell}} = T_{\mathrm{h}}^{C_{\mathrm{h}}}T_{\ell}^{C_{\ell}}. \quad (13.39)$$

The total heat extracted from each reservoir is $\Delta Q_{\mathrm{h}} = C_{\mathrm{h}}(T_{\mathrm{h}} - T_{\mathrm{f}})$ and $\Delta Q_{\ell} = C_{\ell}(T_{\mathrm{f}} - T_{\ell})$ respectively and so the total work is

$$\Delta W = \Delta Q_{\mathrm{h}} - \Delta Q_{\ell} = C_{\mathrm{h}}T_{\mathrm{h}} + C_{\ell}T_{\ell} - (C_{\mathrm{h}} + C_{\ell})T_{\mathrm{f}}. \quad (13.40)$$

[Image: A schematic diagram of a Carnot engine. It takes heat dQ_h from a hot reservoir C_h at T_h, outputs work dW, and rejects heat dQ_l to a cold reservoir C_l at T_l.]
**Fig. 13.11** A Carnot engine shown schematically. In diagrams such as this one, the arrows are labelled with the heat and work flowing in one cycle of the engine.

[Image: A portrait of Sadi Carnot as a young man in military uniform.]
**Fig. 13.13** Sadi Carnot

===== Page 140 =====

# 14 Entropy

14.1 Definition of entropy  140
14.2 Irreversible change  140
14.3 The first law revisited  142
14.4 The Joule expansion  144
14.5 The statistical basis for entropy  146
14.6 The entropy of mixing  147
14.7 Maxwell's demon  149
14.8 Entropy and probability  150
Chapter summary  153
Exercises  153

In this chapter we will use the results from Chapter 13 to define a quantity called entropy and to understand how entropy changes in reversible and irreversible processes. We will also consider the statistical basis for entropy, and use this to understand the entropy of mixing, the apparent conundrum of Maxwell's demon and the connection between entropy and probability.

## 14.1 Definition of entropy

In this section, we introduce a thermodynamic definition of entropy. We begin by recalling from eqn 13.26 that $\oint \mathrm{d}Q_{\mathrm{rev}} / T = 0$. This means that the integral

$$\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}$$

is path independent (see Appendix C.7). Therefore the quantity $\mathrm{d}Q_{\mathrm{rev}} / T$ is an exact differential and we can write down a new state function which we call entropy. We therefore define the entropy $S$ by

$$\mathrm{d}S = \frac{\mathrm{d}Q_{\mathrm{rev}}}{T}, \quad (14.1)$$

so that

$$S(\mathrm{B}) - S(\mathrm{A}) = \int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}, \quad (14.2)$$

and $S$ is a function of state. For an adiabatic process (a reversible adiathermal process) we have that

$$\mathrm{d}Q_{\mathrm{rev}} = 0. \quad (14.3)$$

Hence an adiabatic process involves no change in entropy (the process is also called isentropic).

## 14.2 Irreversible change

Entropy $S$ is defined in terms of reversible changes of heat. Since $S$ is a state function, then the integral of $S$ around a closed loop is zero, so that

$$\oint \frac{\mathrm{d}Q_{\mathrm{rev}}}{T} = 0. \quad (14.4)$$

[Image: A p-V diagram showing an irreversible path A->B and a reversible path B->A between two points A and B.]
**Fig. 14.1** An irreversible and a reversible change between two points A and B in $p - V$ parameter space.

Let us now consider a loop which contains an irreversible section (A→B) and a reversible section (B→A), as shown in Fig. 14.1. The Clausius inequality (eqn 13.34) implies that, integrating around this loop, we have that

$$\oint \frac{\mathrm{d}Q}{T}\leq 0. \quad (14.5)$$

Writing out the left-hand side in detail, we have that

$$\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q}{T} +\int_{\mathrm{B}}^{\mathrm{A}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}\leq 0, \quad (14.6)$$

and hence rearranging gives

$$\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q}{T}\leq \int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}. \quad (14.7)$$

This is true however close A and B get to each other, so in general we can write that the change in entropy $\mathrm{d}S$ is given by

$$\mathrm{d}S = \frac{\mathrm{d}Q_{\mathrm{rev}}}{T}\geq \frac{\mathrm{d}Q}{T}. \quad (14.8)$$

The equality in this expression is only obtained (somewhat trivially) if the process on the right-hand side is actually reversible. Note that because $S$ is a state function, the entropy change in going from A to B is independent of the route.

Consider a thermally isolated system. In such a system $\mathrm{d}Q = 0$ for any process, so that the above inequality becomes

$$\mathrm{d}S\geq 0. \quad (14.9)$$

This is a very important equation and is, in fact, another statement of the second law of thermodynamics. It shows that any change for this thermally isolated system always results in the entropy either staying the same (for a reversible change) or increasing (for an irreversible change). This gives us yet another statement of the second law, namely that: "the entropy of an isolated system tends to a maximum." We can tentatively apply these ideas to the Universe as a whole, under the assumption that the Universe itself is a thermally isolated system:

## Application to the Universe

Assuming that the Universe can be treated as an isolated system, the first two laws of thermodynamics become:

(1) $U_{\mathrm{Universe}} =$ constant.
(2) $S_{\mathrm{Universe}}$ can only increase.

The following example illustrates how the entropy of a particular system and a reservoir, as well as that of the Universe (taken to be the system plus reservoir), changes in an irreversible process.

[Image: A graph of entropy change versus the ratio T_system / T_reservoir. The graph shows Delta S_system, Delta S_reservoir, and Delta S_Universe. Delta S_Universe is always positive or zero.]
**Fig. 14.2** The entropy change in the simple process in which a small system is placed in contact with a large reservoir.

## Example 14.1

A large reservoir at temperature $T_{\mathrm{R}}$ is placed in thermal contact with a small system at temperature $T_{\mathrm{S}}$. They both end up at the temperature of the reservoir, $T_{\mathrm{R}}$. The heat transferred from the reservoir to the system is $\Delta Q = C(T_{\mathrm{R}} - T_{\mathrm{S}})$, where $C$ is the heat capacity of the system.

If $T_{\mathrm{R}} > T_{\mathrm{S}}$, heat is transferred from reservoir to system, the system warms and its entropy increases; the entropy of the reservoir decreases, because heat flows out of it. If $T_{\mathrm{R}}< T_{\mathrm{S}}$, heat is transferred from system to reservoir, the system cools and its entropy decreases; the entropy of the reservoir increases, because heat flows into it.

Let us calculate these entropy changes in detail: The entropy change in the reservoir, which has constant temperature $T_{\mathrm{R}}$, is

$$\Delta S_{\mathrm{reservoir}} = \int \frac{\mathrm{d}Q}{T_{\mathrm{R}}} = \frac{1}{T_{\mathrm{R}}}\int \mathrm{d}Q = \frac{\Delta Q}{T_{\mathrm{R}}} = \frac{C(T_{\mathrm{S}} - T_{\mathrm{R}})}{T_{\mathrm{R}}}, \quad (14.10)$$

while the entropy change in the system is

$$\Delta S_{\mathrm{system}} = \int \frac{\mathrm{d}Q}{T} = \int_{T_{\mathrm{S}}}^{T_{\mathrm{R}}}\frac{C\mathrm{d}T}{T} = C\ln \frac{T_{\mathrm{R}}}{T_{\mathrm{S}}}. \quad (14.11)$$

Hence, the total entropy change in the Universe is

$$\Delta S_{\mathrm{Universe}} = \Delta S_{\mathrm{system}} + \Delta S_{\mathrm{reservoir}} = C\left[\ln \frac{T_{\mathrm{R}}}{T_{\mathrm{S}}} +\frac{T_{\mathrm{S}}}{T_{\mathrm{R}}} -1\right]. \quad (14.12)$$

These expressions are plotted in Fig. 14.2 and demonstrate that even though $\Delta S_{\mathrm{reservoir}}$ and $\Delta S_{\mathrm{system}}$ can each be positive or negative, we always have that

$$\Delta S_{\mathrm{Universe}}\geq 0. \quad (14.13)$$

## 14.3 The first law revisited

Using our new notion of entropy, it is possible to obtain a much more elegant and useful statement of the first law of thermodynamics. We recall from eqn 11.7 that the first law is given by

$$\mathrm{d}U = \mathrm{d}Q + \mathrm{d}W. \quad (14.14)$$

Now, for a reversible change only, we have that

$$\mathrm{d}Q = T\mathrm{d}S \quad (14.15)$$

and

$$\mathrm{d}W = -pdV. \quad (14.16)$$

Combining these, we find that

$$\mathrm{d}U = T\mathrm{d}S - pdV. \quad (14.17)$$

Constructing this equation, we stress, has assumed that the change is reversible. However, since all the quantities in eqn 14.17 are functions of state, and are therefore path independent, this equation holds for irreversible processes as well! For an irreversible change, $\mathrm{d}Q \leq T \mathrm{~d}S$ and also $\mathrm{d}W \geq - p \mathrm{~d}V$, but with $\mathrm{d}Q$ being smaller than for the reversible case and $\mathrm{d}W$ being larger than for the reversible case so that $\mathrm{d}U$ is the same whether the change is reversible or irreversible.

Therefore, we always have that:

$$\mathrm{d}U = T\mathrm{d}S - pdV. \quad (14.18)$$

This equation implies that the internal energy $U$ changes when either $S$ or $V$ changes. Thus, the function $U$ can be written in terms of the variables $S$ and $V$, which are its so-called natural variables. These variables are both extensive (i.e., they scale with the size of the system). The variables $p$ and $T$ are both intensive (i.e., they do not scale with the size of the system) and behave a bit like forces, since they show how the internal energy changes with respect to some parameter. In fact, since mathematically we can write $\mathrm{d}U$ as

$$\mathrm{d}U = \left(\frac{\partial U}{\partial S}\right)_V\mathrm{d}S + \left(\frac{\partial U}{\partial V}\right)_S\mathrm{d}V, \quad (14.19)$$

we can make the identification of $T$ and $p$ using

$$\begin{array}{rcl}{T}&{=}&{\left(\frac{\partial U}{\partial S}\right)_V\mathrm{and}}\\ {p}&{=}&{-\left(\frac{\partial U}{\partial V}\right)_S.}\end{array} \quad (14.21)$$

The ratio of $p$ and $T$ can also be written in terms of the variables $U$, $S$ and $V$, as follows:

$$\frac{p}{T} = -\left(\frac{\partial U}{\partial V}\right)_S\left(\frac{\partial S}{\partial U}\right)_V, \quad (14.22)$$

using the reciprocal theorem (see eqn C.41). Hence

$$\frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_U, \quad (14.23)$$

using the reciprocity theorem (see eqn C.42). These equations are used in the following example.

[Image: Two systems, 1 and 2, connected by a pipe. An arrow shows that internal energy Delta U and volume Delta V can be transferred between them.]
**Fig. 14.3** Two systems, 1 and 2, which are able to exchange volume and internal energy.

## Example 14.2

Consider two systems, with pressures $p_1$ and $p_2$ and temperatures $T_1$ and $T_2$. If internal energy $\Delta U$ is transferred from system 1 to system 2, and volume $\Delta V$ is transferred from system 1 to system 2 (see Fig. 14.3), find the change of entropy. Show that equilibrium results when $T_1 = T_2$ and $p_1 = p_2$.

Solution:

Equation 14.18 can be rewritten as

$$\mathrm{d}S = \frac{1}{T}\mathrm{d}U + \frac{p}{T}\mathrm{d}V. \quad (14.24)$$

If we now apply this to our problem, the change in entropy is then straightforwardly

$$\Delta S = \left(\frac{1}{T_1} -\frac{1}{T_2}\right)\Delta U + \left(\frac{p_1}{T_1} -\frac{p_2}{T_2}\right)\Delta V. \quad (14.25)$$

Equation 14.9 shows that the entropy always increases in any physical process. Thus, when equilibrium is achieved, the entropy will have achieved a maximum, so that $\Delta S = 0$. This means that the joint system cannot increase its entropy by further exchanging volume or internal energy between system 1 and system 2. $\Delta S = 0$ can only be achieved when $T_1 = T_2$ and $p_1 = p_2$.

Eqn 14.18 is an important equation that will be used a great deal in subsequent chapters. Before proceeding, we pause to summarize the most important equations in this section and state their applicability.

| Summary | |
| :--- | :--- |
| $\mathrm{d}U = \mathrm{d}Q + \mathrm{d}W$ | always true |
| $\mathrm{d}Q = T \mathrm{d}S$ | only true for reversible changes |
| $\mathrm{d}W = -p \mathrm{d}V$ | only true for reversible changes |
| $\mathrm{d}U = T \mathrm{d}S - p \mathrm{d}V$ | always true |
| For irreversible changes: | $\mathrm{d}Q \leq T \mathrm{d}S, \mathrm{d}W \geq -p \mathrm{d}V$ |

## 14.4 The Joule expansion

In this section, we describe in detail an irreversible process known as the Joule expansion (see Fig. 14.4). One mole of ideal gas (pressure $p_1$, temperature $T_1$) is confined to the left-hand side of a thermally isolated container and occupies a volume $V_0$. The right-hand side of the container (also volume $V_0$) is evacuated. The tap between the two parts of the container is then suddenly opened and the gas fills the entire container of volume $2V_0$ (and has new temperature $T_{\mathrm{f}}$ and pressure $p_{\mathrm{f}}$). Both containers are assumed to be thermally isolated from their surroundings. For the initial state, the ideal gas law implies that

$$p_{\mathrm{I}}V_{0} = RT_{\mathrm{I}}, \quad (14.26)$$

and for the final state that

$$p_{\mathrm{f}}(2V_{0}) = RT_{\mathrm{f}}. \quad (14.27)$$

Since the system is thermally isolated from its surroundings, $\Delta U = 0$. Also, since $U$ is only a function of $T$ for an ideal gas, $\Delta T = 0$ and hence $T_{\mathrm{i}} = T_{\mathrm{f}}$. This implies that $p_{\mathrm{i}}V_{0} = p_{\mathrm{f}}(2V_{0})$, so that the pressure halves, i.e.,

$$p_{\mathrm{f}} = \frac{p_{\mathrm{i}}}{2}. \quad (14.28)$$

It is hard to calculate directly the change of entropy of a gas in a Joule expansion along the route that it takes from its initial state to the final state. The pressure and volume of the system are undefined during the process immediately after the partition is removed since the gas is in a non-equilibrium state. However, entropy is a function of state and therefore for the purposes of the calculation, we can take another route from the initial state to the final state since changes of functions of state are independent of the route taken. Let us calculate the change in entropy for a reversible isothermal expansion of the gas from volume $V_{0}$ to volume $2V_{0}$ (as indicated in Fig. 14.5). Since the internal energy is constant in the isothermal expansion of an ideal gas, $\mathrm{d}U = 0$, and hence the new form of the first law in eqn 14.18 gives us $T\mathrm{d}S = p\mathrm{d}V$, so that

$$\Delta S = \int_{\mathrm{i}}^{\mathrm{f}}\mathrm{d}S = \int_{V_{0}}^{2V_{0}}\frac{p\mathrm{d}V}{T} = \int_{V_{0}}^{2V_{0}}\frac{R\mathrm{d}V}{V} = R\ln 2. \quad (14.29)$$

Since $S$ is a function of state, this increase in entropy $R\ln 2$ is also the change of entropy for the Joule expansion.

[Image: (a) A container divided into two equal parts by a tap. The left part contains a gas at pressure p_i and volume V_0. The right part is evacuated. (b) After the tap is opened, the gas fills both parts, at a new pressure p_f and volume 2V_0.]
**Fig. 14.4** The Joule expansion between volume $V_{0}$ and volume $2V_{0}$. One mole of ideal gas (pressure $p_{\mathrm{i}}$, temperature $T_{\mathrm{i}}$) is confined to the left-hand side of a container in a volume $V_{0}$. The container is thermally isolated from its surroundings. The tap between the two parts of the container is then suddenly opened and the gas fills the entire container of volume $2V_{0}$ (and has new temperature $T_{\mathrm{f}}$ and pressure $p_{\mathrm{f}}$).

[Image: A p-V diagram showing the Joule expansion between volumes V_0 and 2V_0. The path is undefined (dotted). A reversible isothermal expansion path between the same volumes is also shown (solid curve).]
**Fig. 14.5** The Joule expansion between volume $V_{0}$ and volume $2V_{0}$ and a reversible isothermal expansion of a gas between the same volumes. The path in the $p - V$ plane for the Joule expansion is undefined, whereas it is well defined for the reversible isothermal expansion. In each case however, the start and end points are well defined. Since entropy is a function of state, the change in entropy for the two processes is the same, regardless of route.

## Example 14.3

What is the change of entropy in the gas, surroundings, and Universe during a Joule expansion?

Solution:

Above, we have worked out $\Delta S_{\mathrm{gas}}$ for the reversible isothermal expansion and the Joule expansion: they have to be the same. What about the surroundings and the Universe in each case?

For the reversible isothermal expansion of the gas, we deduce the change of entropy in the surroundings so that the entropy in the Universe does not increase (because we are dealing with a reversible situation).

$$\begin{array}{rcl}{\Delta S_{\mathrm{gas}}} & = & {R\ln 2,}\\ {\Delta S_{\mathrm{surroundings}}} & = & {-R\ln 2,}\\ {\Delta S_{\mathrm{Universe}}} & = & {\Delta S_{\mathrm{gas}} + \Delta S_{\mathrm{surroundings}} = 0.} \end{array} \quad (14.30)$$

Notice that the entropy of the surroundings goes down. This does not contradict the second law of thermodynamics. The entropy of something can decrease if that something is not isolated. Here the surroundings are not isolated because they are able to exchange heat with the system.

For the Joule expansion, the system is thermally isolated so that the entropy of the surroundings does not change. Hence

$$\begin{array}{rcl}{\Delta S_{\mathrm{gas}}} & = & {R\ln 2,}\\ {\Delta S_{\mathrm{surroundings}}} & = & {0,}\\ {\Delta S_{\mathrm{Universe}}} & = & {\Delta S_{\mathrm{gas}} + \Delta S_{\mathrm{surroundings}} = R\ln 2.} \end{array} \quad (14.31)$$

Once the Joule expansion has occurred, you can only put the gas back in the left-hand side by compressing it. The best you can do is to do this reversibly, by a reversible isothermal compression, which takes work $\Delta W$ given (for 1 mole of gas) by

$$\Delta W = -\int_{2V_0}^{V_0}p\mathrm{d}V = -\int_{2V_0}^{V_0}\frac{RT}{V}\mathrm{d}V = RT\ln 2 = T\Delta S_{\mathrm{gas}}. \quad (14.32)$$

The increase of entropy in a Joule expansion is thus $\Delta W / T$.

## A paradox?

In the Joule expansion, the system is thermally isolated so no heat can be exchanged: $\Delta Q = 0$. Now work is done: $\Delta W = 0$. Hence $\Delta U = 0$ (so for an ideal gas, $\Delta T = 0$). But if $\Delta Q = 0$, doesn't that imply that $\Delta S = \Delta Q / T = 0$?

The above reasoning is correct, until the very end: the answer to the question in the last point is NO! The equation $\mathrm{d}Q = T\mathrm{d}S$ is only true for reversible changes. In general $\mathrm{d}Q\leq T\mathrm{d}S$, and here we have $\Delta Q = 0$ and $\Delta S = R\ln 2$, so we have that $\Delta Q\leq T\Delta S$.

## 14.5 The statistical basis for entropy

We now want to show that in addition to defining entropy via thermodynamics, i.e., using $\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}} / T$, it is also possible to define entropy via statistics. We will motivate this as follows:

As we showed in eqn 14.20, the first law $\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V$ implies that

$$T = \left(\frac{\partial U}{\partial S}\right)_V, \quad (14.33)$$

or equivalently

$$\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_V. \quad (14.34)$$

Now, recall from eqn 4.7 that

$$\frac{1}{k_{\mathrm{B}}T} = \frac{\mathrm{d}\ln\Omega}{\mathrm{d}E}. \quad (14.35)$$

Comparing these last two equations motivates the identification of $S$ with $k_{\mathrm{B}}\ln \Omega$, i.e.,

$$S = k_{\mathrm{B}}\ln \Omega. \quad (14.36)$$

This is the expression for the entropy of a system that is in a particular macrostate in terms of $\Omega$, the number of microstates associated with that macrostate. We are assuming that the system is in a particular macrostate with fixed energy, and this situation is known as the microcanonical ensemble (see Section 4.5). Later in this chapter (see Section 14.8), and also later in the book, we will generalize this result to express the entropy for more complicated situations. Nevertheless, this expression is sufficiently important that it was inscribed on Boltzmann's tombstone, although on the tombstone the symbol $\Omega$ is written as a "W". In the following example, we will apply this expression to understanding the Joule expansion, which we introduced in Section 14.4.

## Example 14.4

## Joule expansion

Following a Joule expansion, each molecule can be either on the left-hand side or the right-hand side of the container. For each molecule there are therefore two ways of placing it. For one mole $(N_{\mathrm{A}}$ molecules) there are $2^{N_{\mathrm{A}}}$ ways of placing them. The number of microstates associated with the gas being in a container twice as big as the initial volume is larger by a multiplicative factor

$$2^{N_{\mathrm{A}}}, \quad (14.37)$$

so that the additional entropy is

$$\Delta S = k_{\mathrm{B}}\ln 2^{N_{\mathrm{A}}} = k_{\mathrm{B}}N_{\mathrm{A}}\ln 2 = R\ln 2, \quad (14.38)$$

which is the same expression as written in eqn 14.29.

## 14.6 The entropy of mixing

Consider two different ideal gases (call them 1 and 2) which are in separate vessels with volumes $xV$ and $(1 - x)V$ respectively at the same pressures $p$ and temperatures $T$ (see Fig. 14.6). Since the pressures and temperatures are the same on each side, and since $p = (N / V)k_{\mathrm{B}}T$, the number of molecules of gas 1 is $xN$ and of gas 2 is $(1 - x)N$, where $N$ is the total number of molecules.

[Image: Two vessels connected by a pipe with a closed tap. The left vessel contains gas 1 of volume xV. The right vessel contains gas 2 of volume (1-x)V. Both are at pressure p and temperature T.]
**Fig. 14.6** Gas 1 is confined in a vessel of volume $xV$, while gas 2 is confined in a vessel of volume $(1 - x)V$. Both gases are at pressure $p$ and temperature $T$. Mixing occurs once the tap on the pipe connecting the two vessels is opened.

If the tap on the pipe connecting the two vessels is opened, the gases will spontaneously mix, resulting in an increase in entropy, known as the entropy of mixing. As for the Joule expansion, we can imagine going from the starting state (gas 1 in the first vessel, gas 2 in the second vessel) to the final state (a homogeneous mixture of gas 1 and gas 2 distributed throughout both vessels) via a reversible route, so that we imagine a reversible expansion of gas 1 from $xV$ into the combined volume $V$ and a reversible expansion of gas 2 from $(1 - x)V$ into the combined volume $V$. For an isothermal expansion of an ideal gas, the internal energy doesn't change and hence $T\mathrm{d}S = p\mathrm{d}V$ so that $\mathrm{d}S = (p / T)\mathrm{d}V = Nk_{\mathrm{B}}\mathrm{d}V / V$ using the ideal gas law. This means that the entropy of mixing for our problem is

$$\Delta S = xNk_{\mathrm{B}}\int_{xV}^{V}\frac{\mathrm{d}V_{1}}{V_{1}} +(1 - x)Nk_{\mathrm{B}}\int_{(1 - x)V}^{V}\frac{\mathrm{d}V_{2}}{V_{2}} \quad (14.39)$$

and hence

$$\Delta S = -Nk_{\mathrm{B}}(x\ln x + (1 - x)\ln (1 - x)). \quad (14.40)$$

This equation is plotted in Fig. 14.7. As expected, there is no entropy increase when $x = 0$ or $x = 1$. The maximum entropy change occurs when $x = \frac{1}{2}$, in which case $\Delta S = Nk_{\mathrm{B}}\ln 2$. This of course corresponds to the equilibrium state in which no further increase of entropy is possible.

[Image: A graph of the entropy of mixing Delta S / N k_B versus x. The curve is symmetric, starting at 0 for x=0, rising to a maximum of ln 2 at x=0.5, and returning to 0 at x=1.]
**Fig. 14.7** The entropy of mixing according to eqn 14.40.

This expression for $x = \frac{1}{2}$ also admits to a very simple statistical interpretation. Before the mixing of the gases takes place, we know that gas 1 is only in the first vessel and gas 2 is only in the second vessel. After mixing, each molecule can exist in additional "microstates"; for every microstate with a molecule of gas 1 on the left there is now an additional one with a molecule of gas 1 now on the right. Therefore $\Omega$ must be multiplied by $2^{N}$ and hence $S$ must increase by $k_{\mathrm{B}}\ln 2^{N}$, which is $Nk_{\mathrm{B}}\ln 2$.

This treatment has a profound consequence: distinguishability is an important concept! We have assumed that there is some tangible difference between gas 1 and gas 2, so that there is some way to label whether a particular molecule is gas 1 or gas 2. For example, if the two gases were nitrogen and oxygen, one could measure the mass of the molecules to determine which was which. But what if the two gases were actually the same? Physically, we would expect that mixing them would have no observable consequences, so there should be no increase in entropy. Thus mixing should only increase entropy if the gases really are distinguishable. We will return to this issue of distinguishability in Chapter 29.

[Image: A sketch of Maxwell's demon. A box is divided into two chambers A and B by a wall with a small trap door. A small demon-like creature sits by the trap door, holding a string to open and close it. Molecules are shown moving in both chambers.]
**Fig. 14.8** Maxwell's demon watches the gas molecules in chambers A and B and intelligently opens and shuts the trap door connecting the chambers. The demon is therefore able to reverse the Joule expansion and only let molecules travel from B to A, thus apparently contravening the second law of thermodynamics.

[Image: A portrait of Robert Mayer, a man with glasses and a beard.]
**Fig. 14.10** Robert Mayer

[Image: A portrait of James Joule, a man with a long white beard.]
**Fig. 14.11** James Joule

[Image: A portrait of Rudolf Clausius, a man with dark hair and a beard.]
**Fig. 14.12** Rudolf Clausius

===== Page 145 =====

# Part VI

# Thermodynamics in action

In this part we use the laws of thermodynamics developed in Part V to solve real problems in thermodynamics. Part VI is structured as follows:

In Chapter 16 we derive various functions of state, called thermodynamic potentials, in particular the enthalpy, Helmholtz function and Gibbs function, and show how they can be used to investigate thermodynamic systems under various constraints. We introduce the Maxwell relations, which allow us to relate various partial differentials in thermal physics. In Chapter 17 we show that the results derived so far can be extended straightforwardly to a variety of different thermodynamic systems other than the ideal gas. In Chapter 18 we introduce the third law of thermodynamics, which is really an addendum to the second law, and explain some of its consequences.

===== Page 146 =====

This page intentionally left blank

===== Page 147 =====

# 15 Information theory

15.1 Information and Shannon entropy  157
15.2 Information and thermodynamics  159
15.3 Data compression  160
15.4 Quantum information  162
15.5 Conditional and joint probabilities  165
15.6 Bayes' theorem  165
Chapter summary  168
Further reading  168
Exercises  169

In this chapter we are going to examine the concept of information and relate it to thermodynamic entropy. At first sight, this seems a slightly crazy thing to do. What on earth do something to do with heat engines and something to do with bits and bytes have in common? It turns out that there is a very deep connection between these two concepts. To understand why, we begin our account by trying to formulate one definition of information.

## 15.1 Information and Shannon entropy

Consider the following three true statements about Isaac Newton and his birthday.

(1) Isaac Newton's birthday falls on a particular day of the year.
(2) Isaac Newton's birthday falls in the second half of the year.
(3) Isaac Newton's birthday falls on the 25th of a month.

The first statement has, by any sensible measure, no information content. All birthdays fall on a particular day of the year. The second statement has more information content: at least we now know which half of the year his birthday is. The third statement is much more specific and has the greatest information content.

How do we quantify information content? Well, one property we could notice is that the greater the probability of the statement being true in the absence of any prior information, the less the information content of the statement. Thus if you knew no prior information about Newton's birthday, then you would say that statement 1 has probability $P_{1} = 1$, statement 2 has probability $P_{2} = \frac{1}{2}$, and statement 3 has probability $P_{3} = \frac{12}{365}$; so as the probability decreases, the information content increases. Moreover, since the useful statements 2 and 3 are independent, then if you are given statements 2 and 3 together, their information contents should add. Moreover, the probability of statements 2 and 3 both being true, in the absence of prior information, is $P_{2} \times P_{3} = \frac{6}{365}$. Since the probability of two independent statements being true is the product of their individual probabilities, and since it is natural to assume that information content is additive, one is motivated to adopt the definition of information which was proposed by Claude Shannon (1916-2001) as follows:

The information content $Q$ of a statement is defined by

$$Q = -k\log P, \quad (15.1)$$

where $P$ is the probability of the statement and $k$ is a positive constant. If we use $\log_2$ (log to the base 2) for the logarithm in this expression and also $k = 1$, then the information $Q$ is measured in bits. If instead we use $\ln \equiv \log_{\mathrm{e}}$ and choose $k = k_{\mathrm{B}}$, then we have a definition that, as we shall see, will match what we have found in thermodynamics. In this chapter, we will stick with the former convention since bits are a useful quantity with which to think about information.

Thus, if we have a set of statements with probability $P_{i}$, with corresponding information $Q_{i} = - k\log P_{i}$, then the average information content $S$ is given by

$$S = \langle Q\rangle = \sum_{i}Q_{i}P_{i} = -k\sum_{i}P_{i}\log P_{i}. \quad (15.2)$$

The average information is called the Shannon entropy.

## Example 15.1

A fair die produces outcomes 1, 2, 3, 4, 5, and 6 with probabilities $\frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}$. The information associated with each outcome is $Q = - k\log \frac{1}{6} = k\log 6$ and the average information content is then $S = k\log 6$. Taking $k = 1$ and using log to the base 2 gives a Shannon entropy of 2.58 bits. A biased die produces outcomes 1, 2, 3, 4, 5, and 6 with probabilities $\frac{1}{10}, \frac{1}{10}, \frac{1}{10}, \frac{1}{10}, \frac{1}{10}, \frac{1}{2}$. The information contents associated with the outcomes are $k\log 10$ (for the first five outcomes) and $k\log 2$ (for the last outcome). (These are 3.32 bits for the first five outcomes and 1 bit for the last outcome.) If we take $k = 1$ again, the Shannon entropy is then $S = k(5\times \frac{1}{10}\log 10 + \frac{1}{2}\log 2) = k(\log \sqrt{20})$ (this is 2.16 bits). This Shannon entropy is smaller than in the case of the fair die.

The Shannon entropy quantifies how much information we gain, on average, following a measurement of a particular quantity. (Another way of looking at it is to say the Shannon entropy quantifies the amount of uncertainty we have about a quantity before we measure it.) To make these ideas more concrete, let us study a simple example in which there are only two possible outcomes of a particular random process (such as the tossing of a coin, or asking the question "will it rain tomorrow?").

## Example 15.2

What is the Shannon entropy for a Bernoulli trial (a two-outcome random variable) with probabilities $P$ and $1 - P$ of the two outcomes?

Solution:

$$S = -\sum_{i}P_{i}\log P_{i} = -P\log P - (1 - P)\log (1 - P), \quad (15.3)$$

where we have set $k = 1$. This behaviour is sketched in Fig. 15.1. The Shannon entropy has a maximum when $p = \frac{1}{2}$ (greatest uncertainty about the outcome, or greatest information gained, 1 bit, following a trial) and a minimum when $p = 0$ or 1 (least uncertainty about the outcome, or least information gained, 0 bit, following a trial).

[Image: A graph of Shannon entropy S(P) in bits versus probability P. The curve is an inverted U-shape, reaching a maximum of 1 bit at P=0.5. Dotted lines show the information associated with each outcome, -log2 P and -log2 (1-P).]
**Fig. 15.1** The Shannon entropy of a Bernoulli trial (a two-outcome random variable) with probabilities of the two outcomes given by $P$ and $1 - P$. The units are chosen so that the Shannon entropy is in bits. Also shown is the information associated with each outcome (dotted lines).

The information associated with each of the two possible outcomes is also shown in Fig. 15.1 as dotted lines. The information associated with the outcome having probability $P$ is given by $Q_{1} = -\log_{2}P$ and decreases as $P$ increases. Clearly when this outcome is very unlikely ( $P$ small) the information associated with getting that outcome is very large ($Q_{1}$ is many bits of information). However, such an outcome doesn't happen very often so it doesn't contribute much to the average information (i.e., to the Shannon entropy, the solid line in Fig. 15.1). When this outcome is almost certain ( $P$ almost 1) it contributes a lot to the average information but has very little information content. For the other outcome, with probability $1 - P$, $Q_{2} = -\log_{2}(1 - P)$ and the behaviour is simply a mirror image of this. The maximum average information is when $P = 1 - P = \frac{1}{2}$ and both outcomes have 1 bit of information associated with them.

## 15.2 Information and thermodynamics

Remarkably, the formula for Shannon entropy in eqn 15.2 is identical (apart from whether you take your constant as $k$ or $k_{\mathrm{B}}$) to Gibbs' expression for thermodynamic entropy in eqn 14.48. This gives us a useful perspective on what thermodynamic entropy is. It is a measure of our uncertainty of a system, based on our limited knowledge of its properties and ignorance about which of its microstates it is in. In making inferences on the basis of partial information, we can assign probabilities on the basis that we maximize entropy subject to the constraints provided by what is known about the system. This is exactly what we did in Example 14.7, when we maximized the Gibbs' entropy of an isolated system subject to the constraint that the total energy $U$ was constant; hey presto, we found that we recovered the Boltzmann probability distribution. With this viewpoint, one can begin to understand thermodynamics from an information theory viewpoint.

However, not only does information theory apply to physical systems, but as pointed out by Rolf Landauer (1927-1999), information itself is a physical quantity. Imagine a physical computing device which has stored $N$ bits of information and is connected to a thermal reservoir of temperature $T$. The bits can be either one or zero. Now we decide to physically erase that information. Erasure must be irreversible. There must be no vestige of the original stored information left in the erased state of the system. Let us erase the information by resetting all the bits to zero. Then this irreversible process reduces the number of states of the system by $\ln 2^{N}$ and hence the entropy of the system goes down by $Nk_{\mathrm{B}}\ln 2$, or $k_{\mathrm{B}}\ln 2$ per bit. For the total entropy of the Universe not to decrease, the entropy of the surroundings must go up by $k_{\mathrm{B}}\ln 2$ per bit and so we must dissipate heat in the surroundings equal to $k_{\mathrm{B}}T\ln 2$ per bit erased.

This connection between entropy and information helps us in our understanding of Maxwell's demon discussed in Section 14.7. By performing computations about molecules and their velocities, the demon has to store information. Each bit of information is associated with entropy, as becomes clear when the demon has to free up some space on its hard disk to continue computing. The process of erasing one bit of information gives rise to an increase of entropy of $k_{\mathrm{B}}\ln 2$. If Maxwell's demon reverses the Joule expansion of 1 mole of gas, it might therefore seem that it has decreased the entropy of the Universe by $N_{\mathrm{A}}k_{\mathrm{B}}\ln 2 = R\ln 2$, but it will have had to store at least $N_{\mathrm{A}}$ bits of information to do this. Assuming that Maxwell's demons only have on-board a storage capacity of a few hundred gigabytes, which is much less than $N_{\mathrm{A}}$ bits, the demon will have had to erase its disk many, many times in the process of its operation, thus leading to an increase in entropy of the Universe which at least equals, and probably outweighs, the decrease of entropy of the Universe it was aiming to achieve.

If the demon is somehow fitted with a vast on-board memory so that it doesn't have to erase its memory to do the computation, then the increase in entropy of the Universe can be delayed until the demon needs to free up some memory space. Eventually, one supposes, as the demon begins to age and becomes forgetful, the Universe will reclaim all that entropy!

## 15.3 Data compression

Information must be stored, or sometimes transmitted from one place to another. It is therefore useful if it can be compressed down to its minimum possible size. This really begs the question what the actual irreducible amount of real information in a particular block of data really is; many messages, political speeches, and even sometimes book chapters, contain large amounts of extraneous padding that is not really needed. Of course, when we compress a file on a computer we often get something that is unreadable to human beings. The English language has various quirks, such as when you see a letter "q" it is almost always followed by a "u", so is that second "u" really needed when you know it is coming? A good data compression algorithm will get rid of extra things like that, plus much more besides. Hence, the question of how many bits are in a given source of data seems like a useful question for computer scientists to attempt to answer; in fact we will see it has implications for physics!

We will not prove Shannon's noiseless channel coding theorem here, but motivate it and then state it.

## Example 15.3

Let us consider the simplest case in which our data are stored in the form of the binary digits "0" and "1". Let us further suppose that the data contain "0" with probability $P$ and "1" with probability $1 - P$. If $P = \frac{1}{2}$ then our data cannot really be compressed, as each bit of data contains real information. Let us now suppose that $P = 0.9$ so that the data contain more "0"s than "1"s. In this case, the data contain less information, and it is not hard to find a way of taking advantage of this. For example, let us read the data into our compression algorithm in pairs of bits, rather than one bit at a time, and make the following transformations:

| Input | Output |
| :--- | :--- |
| 00 | 0 |
| 01 | 10 |
| 10 | 110 |
| 11 | 111 |

In each of the transformations, we end on a single "0", which lets the decompression algorithm know that it can start reading the next sequence. Now, of course, although the pair of symbols "00" has been compressed to "0", saving a bit, the pair of symbols "01" has been enlarged to "110" and "11" has been even more enlarged to "111", costing one extra or two extra bits respectively. However, "00" is very likely to occur (probability 0.81) while "01" and "11" are much less likely to occur (probabilities 0.09 and 0.01 respectively), so overall we save bits using this compression scheme.

This example gives us a clue as to how to compress data more generally. The aim is to identify in a sequence of data what the typical sequences are and then efficiently code only those. When the amount of data becomes very large, then anything other than these typical sequences is very unlikely to occur. Because there are fewer typical sequences than there are sequences in general, a saving can be made. Hence, let us divide up some data into sequences of length $n$. Assuming the elements in the data do not depend on each other, then the probability of finding a sequence $x_{1}, x_{2}, \ldots , x_{n}$ is

$$P(x_{1}, x_{2}, \ldots , x_{n}) = P(x_{1})P(x_{2}) \ldots P(x_{n}) \approx P^{nP}(1 - P)^{n(1 - P)}, \quad (15.4)$$

for typical sequences. Taking logarithms to base 2 of both sides gives

$$-\log_{2}P(x_{1},x_{2},\ldots ,x_{n})\approx -nP\log_{2}P - n(1 - P)\log_{2}(1 - P) = nS, \quad (15.5)$$

where $S$ is the entropy for a Bernoulli trial with probability $P$. Hence

$$P(x_{1},x_{2},\ldots ,x_{n})\approx \frac{1}{2^{nS}}. \quad (15.6)$$

This shows that there are at most only $2^{nS}$ typical sequences and hence it only requires $nS$ bits to code them. As $n$ becomes larger, and the typical sequences become longer, the possibility of this scheme failing becomes smaller and smaller.

A compression algorithm will take a typical sequence of $n$ terms $x_{1}, x_{2}, \ldots , x_{n}$ and turn them into a string of length $nR$. Hence, the smaller $R$ is, the greater the compression. Shannon's noiseless channel coding theorem states that if we have a source of information with entropy $S$, and if $R > S$, then there exists a reliable compression scheme of compression factor $R$. Conversely, if $R < S$ then any compression scheme will not be reliable. Thus the entropy $S$ sets the ultimate compression limit on a set of data.

## 15.4 Quantum information

This section shows how the concept of information can be extended to quantum systems and assumes familiarity with the main results of quantum mechanics.

In this chapter we have seen that in classical systems the information content is connected with the probability. In quantum systems, these probabilities are replaced by density matrices. A density matrix is used to describe the statistical state of a quantum system, as can arise for a quantum system in thermal equilibrium at finite temperature. A summary of the main results concerning density matrices is given in the box below.

## The density matrix

If a quantum system is in one of a number of states $|\psi_i\rangle$ with probability $P_{i}$, then the density matrix $\rho$ for the system is defined by

$$\rho = \sum_{i}P_{i}|\psi_{i}\rangle \langle \psi_{i}|. \quad (15.9)$$

As an example, think of a three-state system and think of $|\psi_{1}\rangle$ as a column vector $\begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}$, and hence $\langle \psi_{1}\rangle$ as a row vector $(1,0,0)$ and similarly for $|\psi_{2}\rangle$, $\langle \psi_{2}|$, $|\psi_{3}\rangle$ and $\langle \psi_{3}|$. Then

$$\begin{array}{rcl}{\rho} & = & {P_1\left( \begin{array}{ccc}1 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0 \end{array} \right) + P_2\left( \begin{array}{ccc}0 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 0 \end{array} \right) + P_3\left( \begin{array}{ccc}0 & 0 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0 \end{array} \right)}\\ {} & = & {\left( \begin{array}{ccc}P_1 & 0 & 0\\ 0 & P_2 & 0\\ 0 & 0 & P_3 \end{array} \right).} \end{array} \quad (15.10)$$

This form of the density matrix looks very simple, but this is only because we have expressed it in a very simple basis.

If $P_{j}\neq 0$ and $P_{i\neq j} = 0$, then the system is said to be in a pure state and $\rho$ can be written in the simple form

$$\rho = |\psi_j\rangle \langle \psi_j|. \quad (15.11)$$

Otherwise, it is said to be in a mixed state.

One can show that the expectation value $\langle \hat{A}\rangle$ of a quantum mechanical operator $\hat{A}$ is equal to

$$\langle \hat{A}\rangle = \mathrm{Tr}(\hat{A}\rho). \quad (15.12)$$

One can also prove that

$$\mathrm{Tr}\rho = 1, \quad (15.13)$$

where $\mathrm{Tr}\rho$ means the trace of the density matrix. This expresses the fact that the sum of the probabilities must equal unity, and is in fact a special case of eqn 15.12, setting $\hat{A} = 1$.

One can also show that $\mathrm{Tr}\rho^2 \leq 1$ with equality if and only if the state is pure.

For a system in thermal equilibrium at temperature $T$, $P_{i}$ is given by the Boltzmann factor $\mathrm{e}^{-\beta E_{i}}$ where $E_{i}$ is an eigenvalue of the Hamiltonian $\hat{H}$. The thermal density matrix $\rho_{\mathrm{th}}$ is

$$\rho_{\mathrm{th}} = \sum_{i}\mathrm{e}^{-\beta E_{i}}|\psi_{i}\rangle \langle \psi_{i}| = \exp (-\beta \hat{H}). \quad (15.14)$$

For quantum systems, the information is represented by the operator $- k \log \rho$, where $\rho$ is the density matrix; as before we take $k = 1$. Hence the average information, or entropy, would be $\langle -\log \rho \rangle$. This leads to the definition of the von Neumann entropy $S$ as

$$S(\rho) = -\mathrm{Tr}(\rho \log \rho). \quad (15.7)$$

If the eigenvalues of $\rho$ are $\lambda_{1}, \lambda_{2} \ldots$, then the von Neumann entropy becomes

$$S(\rho) = -\sum_{i}\lambda_{i}\log \lambda_{i}, \quad (15.8)$$

which looks like the Shannon entropy.

## Example 15.4

Show that the entropy of a pure state is zero. How can you maximize the entropy?

Solution:

(i) As shown in the box on page 163, the trace of the density matrix is equal to one $(\mathrm{Tr}\rho = 1)$, and hence the sum of the eigenvalues of the density matrix is

$$\sum \lambda_{i} = 1. \quad (15.15)$$

For a pure state only one eigenvalue will be one and all the other eigenvalues will be zero, and hence $S(\rho) = 0$, i.e., the entropy of a pure state is zero. This is not surprising, since for a pure state there is no "uncertainty" about the state of the system.

(ii) The entropy $S(\rho) = -\sum_{i}\lambda_{i}\log \lambda_{i}$ is maximized when $\lambda_{i} = 1 / n$ for all $i$, where $n$ is the dimension of the density matrix. In this case, the entropy is $S(\rho) = n\times (- \frac{1}{n}\log \frac{1}{n}) = \log n$. This corresponds to there being maximal uncertainty in its precise state.

Classical information is made up only of sequences of "0"s and "1"s (in a sense, all information can be broken down into a series of "yes/no" questions). Quantum information is composed of quantum bits (known as qubits), that are two-level quantum systems which can be represented by linear combinations of the states $|0\rangle$ and $|1\rangle$. Quantum mechanical states can also be entangled with each other. The phenomenon of entanglement has no classical counterpart. Quantum information therefore also contains entangled superpositions such as $(|01\rangle +|10\rangle) / \sqrt{2}$. Here the quantum states of two objects must be described with reference to each other; measurement of the first bit in the sequence to be a 0 forces the second bit to be 1; if the measurement of the first bit gives a 1, the second bit has to be 0; these correlations persist in an entangled quantum system even if the individual objects encoding each bit are spatially separated. Entangled systems cannot be described by pure states of the individual subsystems, and this is where entropy plays a role, as a quantifier of the degree of mixing of states. If the overall system is pure, the entropy of its subsystems can be used to measure its degree of entanglement with the other subsystems.

In this text we do not have space to provide many details about the subject of quantum information, which is a rapidly developing area of current research. Suffice it to say that the processing of information in quantum mechanical systems has some intriguing facets, which are not present in the study of classical information. Entanglement of bits is just one example. As another example, the no-cloning theorem states that it is impossible to make a copy of non-orthogonal quantum mechanical states (for classical systems, there is no physical mechanism to stop you copying information, only copyright laws). All of these features lead to the very rich structure of quantum information theory.

## 15.5 Conditional and joint probabilities

To explore some implications of information theory in more depth we need to introduce some more ideas from probability theory. Now the probability of something often depends on information about what has happened before. Whether it rains tomorrow may depend on whether it has actually rained today. This means that having the information about whether it has rained today may affect how you assign the probability of it raining tomorrow. Not having that information may lead to a different result. This allows us to define the conditional probability $P(\mathrm{A}|\mathrm{B})$ as the probability that event A occurs given that event B has happened. We can also define the joint probability $P(\mathrm{A}\cap \mathrm{B})$ as the probability that event A and event B both occur. The joint probability $P(\mathrm{A}\cap \mathrm{B})$ is equal to the probability that event B occurred multiplied by the probability that A occurred, given that B did, i.e.,

$$P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{A}|\mathrm{B})P(\mathrm{B}), \quad (15.16)$$

and, equally well,

$$P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{B}|\mathrm{A})P(\mathrm{A}). \quad (15.17)$$

If A and B are independent events, then $P(\mathrm{A}|\mathrm{B}) = P(\mathrm{A})$ (because the probability that A occurs is independent of whether B has occurred or not) and hence

$$P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{A})P(\mathrm{B}). \quad (15.18)$$

Now consider the case where there are a number of mutually exclusive events $\mathrm{A}_i$ such that

$$\sum_{i}P(\mathrm{A}_{i}) = 1. \quad (15.19)$$

Then we can write the probability of some other event $X$ as

$$P(X) = \sum_{i}P(X|\mathrm{A}_{i})P(\mathrm{A}_{i}). \quad (15.20)$$

In the following section, these ideas will be used to prove a very important theorem.

## 15.6 Bayes' theorem

Very often, you know that if you are given some hypothesis H you can use it to compute the probability of some outcome O assuming that hypothesis (i.e., you can compute $P(\mathrm{O}|\mathrm{H})$). But what you often want to do is the reverse: you know the outcome because it has actually occurred and you want to choose an explanation out of the possible hypotheses. In other words, given the outcome you want to know the probability that the hypothesis is true. This transformation of $P(\mathrm{O}|\mathrm{H})$ into $P(\mathrm{H}|\mathrm{O})$ can be accomplished using Bayes' theorem. This can be stated as follows:

$$P(\mathrm{A}|\mathrm{B}) = \frac{P(\mathrm{B}|\mathrm{A})P(\mathrm{A})}{P(\mathrm{B})}. \quad (15.21)$$

Here $P(\mathrm{A})$ is called the prior probability, since it is the probability of A occurring without any knowledge as to the outcome of B. The quantity which you derive is $P(\mathrm{A}|\mathrm{B})$, the posterior probability. The proof of Bayes' theorem is very simple: one simply equates eqns 15.16 and 15.17 and rearranges.

## Example 15.5

It is known that one per cent of a group of athletes are using illegal drugs to boost their performance. The drug test is $95\%$ accurate (and so will give a correct diagnosis $95\%$ of the time). A particular athlete is tested and gets a positive result. Is he guilty?

Solution:

The prior probabilities are

$$\begin{array}{rcl}{P(\mathrm{D})} & = & {0.01}\\ {P(\bar{\mathrm{D}})} & = & {0.99,} \end{array} \quad (15.22)$$

where $\mathrm{D}$ means "taking drugs" and $\bar{\mathrm{D}}$ means "not taking drugs". We will also define $\mathrm{Y}$ to mean "test positive" and $\bar{\mathrm{Y}}$ to mean "test negative". Since he tested positive, what we want to know is the probability of his guilt, which is $P(\mathrm{D}|\mathrm{Y})$. Because the drug test is $95\%$ accurate, we have

$$\begin{array}{rcl}{P(\mathrm{Y}|\mathrm{D})} & = & {0.95\qquad \mathrm{(true~positive)}}\\ {P(\mathrm{Y}|\bar{\mathrm{D}})} & = & {0.05\qquad \mathrm{(false~positive)}}\\ {P(\bar{\mathrm{Y}}|\bar{\mathrm{D}})} & = & {0.95\qquad \mathrm{(true~negative)}}\\ {P(\bar{\mathrm{Y}}|\mathrm{D})} & = & {0.05\qquad \mathrm{(false~negative)}}. \end{array} \quad (15.23)$$

The probability $P(\mathrm{Y})$ of a positive test is given by eqn 15.20 as

$$P(\mathrm{Y}) = P(\mathrm{Y}|\mathrm{D})P(\mathrm{D}) + P(\mathrm{Y}|\bar{\mathrm{D}})P(\bar{\mathrm{D}}) = 0.95\times 0.01 + 0.05\times 0.99\approx 0.06. \quad (15.24)$$

Bayes' theorem then gives

$$P(\mathrm{D}|\mathrm{Y}) = \frac{P(\mathrm{Y}|\mathrm{D})P(\mathrm{D})}{P(\mathrm{Y})} = 0.16. \quad (15.25)$$

Hence there is only a $16\%$ probability that he took the drug. This surprising result occurs because although the test is very accurate, the case of illegal drug use in athletes is actually very rare (at least under the assumptions given in this example) and so most positive results are false positives.

The next example demonstrates very powerfully that the probabilities you assign depend very strongly on the information you are given, and sometimes in a surprising way.

## Example 15.6

Mrs Trellis (from North Wales) has two children, born three years apart. One of them is a boy. What is the probability that Mrs Trellis has a daughter? [Not all of the information given to you here is relevant!] If, instead, you had been told that "Mrs Trellis has two children and the taller of her children was a boy", would that have changed your answer?

Solution:

This is another question that emphasizes the fact that probability all depends on the information you know. Some of the information you are given here is indeed irrelevant (the three years apart and the North Wales are irrelevant). The information you have is that one of the children is a boy. There are now three possibilities for the sexes of Mrs Trellis' children (in order of seniority):

(1) boy; boy,
(2) boy; girl,
(3) girl; boy.

The fourth possibility you might think of, "girl; girl", is discounted by the information that one of the children is a boy. Thus the probability that Mrs Trellis has a daughter is $\frac{2}{3}$ [assuming of course that Mrs Trellis has a 50:50 chance of producing a male or female baby at every birth]. The reason that the answer to this question is not $\frac{1}{2}$ is that we don't know which of Mrs Trellis' two children our initial bit of information refers to (i.e., that the child is a boy), whether it refers to the older or the younger one.

Forget older versus younger, we could distinguish between the two children in many different ways: in order of height, weight, number of freckles, etc. Thus the table of possibilities listed above could be written, not in order of seniority, but in order of height, darkness of hair, blueness of eyes, etc. So, if instead we were told that it was the taller of the children that was a boy, then amazingly that additional information changes the probabilities. All our attention is now focused on the other child, the shorter one, who can either be male or female. It's now a probability of $\frac{1}{2}$ that the shorter child is a daughter.

Astonishingly, knowledge of the height of one of the children alters the probability of sex, even though we have assumed that height and sex are uncorrelated. If you like, we could have replaced the statement "the taller of the children was a boy" with "the child with a first name earlier in the alphabet was a boy" and that would also have the same effect! This demonstrates the important role of distinguishability in statistics, a concept that will return!

In physics, we try to make inferences about the world based on what we can measure. Those inferences are made on the basis of probability and information theory and this feeds into the Shannon entropy. When we cover the indistinguishability of particles in a gas in Chapter 21 we will find that this has real thermodynamic implications and the above example prepares us not to be surprised by this.

Furthermore, information theory provides a rationale for setting up probability distributions on the basis of partial knowledge; one simply maximizes the entropy of the distribution subject to the constraints provided by the data. This so-called maximum entropy estimate is the least biased estimate consistent with the given data. Thermodynamics also gives the best description of the properties of a system that has so many $(\approx 10^{23})$ particles that one cannot follow it precisely; the Boltzmann probability obtained by maximizing the Gibbs entropy is the least-biased estimate of the probability consistent with the constraint that a system has fixed internal energy $U$.

## Chapter summary

- The information $Q$ is given by $Q = -\ln P$ where $P$ is the probability.
- The entropy is the average information $S = \langle Q \rangle = -\sum_{i} P_{i} \log P_{i}$.
- The quantum mechanical generalization of this is the von Neumann entropy given by $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ where $\rho$ is the density matrix.
- Bayes' theorem relates the posterior probability (which is a conditional probability) to the prior probability.

## Further reading

The results that we have stated in this chapter concerning Shannon's coding theorems, and which we considered only for the case of Bernoulli trials, i.e., for binary outputs, can be proved for the general case. Shannon also studied communication over noisy channels, in which the presence of noise randomly flips bits with a certain probability. In this case it is also possible to show how much information can be reliably transmitted using such a channel (essentially how many times you have to "repeat" the message to get yourself "heard", though actually this is done using error-correcting codes). Further information may be found in Feynman (1996) and Mackay (2003). An excellent account of the problem of Maxwell's demon may be found in Leff and Rex (2003). Quantum information theory has become a very hot research topic in the last few years and an excellent introduction is Nielsen and Chuang (2000).

===== Page 171 =====

This page intentionally left blank

===== Page 172 =====

# 16 Thermodynamic potentials

16.1 Internal energy, $U$  172
16.2 Enthalpy, $H$  173
16.3 Helmholtz function, $F$  174
16.4 Gibbs function, $G$  175
16.5 Constraints  176
16.6 Maxwell's relations  179
Chapter summary  187
Exercises  187

The internal energy $U$ of a system is a function of state, which means that a system undergoes the same change in $U$ when we move it from one equilibrium state to another, irrespective of which route we take through parameter space. This makes $U$ a very useful quantity, though not a uniquely useful quantity. In fact, we can make a number of other functions of state, simply by adding to $U$ various other combinations of the functions of state $p$, $V$, $T$, and $S$ in such a way as to give the resulting quantity the dimensions of energy. These new functions of state are called thermodynamic potentials, and examples include $U + TS$, $U - pV$, $U + 2pV - 3TS$. However, most thermodynamic potentials that one could pick are really not very useful (including the ones we've just quoted as examples!) but three of them are extremely useful and are given special symbols: $H = U + pV$, $F = U - TS$ and $G = U + pV - TS$. In this chapter, we will explore why these three quantities are so useful. First, however, we will review some properties concerning the internal energy $U$.

## 16.1 Internal energy, $U$

Let us review the results concerning the internal energy that were derived in Section 14.3. Changes in the internal energy $U$ of a system are given by the first law of thermodynamics written in the form (eqn 14.17):

$$\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V. \quad (16.1)$$

This equation shows that the natural variables to describe $U$ are $S$ and $V$, since changes in $U$ are due to changes in $S$ or $V$. Hence we write $U = U(S,V)$ to show that $U$ is a function of $S$ and $V$. Moreover, if $S$ and $V$ are held constant for the system, then

$$\mathrm{d}U = 0, \quad (16.2)$$

which is the same as saying that $U$ is a constant. Equation 16.1 implies that the temperature $T$ can be expressed as a differential of $U$ using

$$T = \left(\frac{\partial U}{\partial S}\right)_V, \quad (16.3)$$

and similarly the pressure $p$ can be expressed as

$$p = -\left(\frac{\partial U}{\partial V}\right)_S. \quad (16.4)$$

We also have that for isochoric processes (where isochoric means that $V$ is constant),

$$\mathrm{d}U = T\mathrm{d}S, \quad (16.5)$$

and for reversible isochoric processes

$$\mathrm{d}U = \mathrm{d}Q_{\mathrm{rev}} = C_V\mathrm{d}T, \quad (16.6)$$

and hence

$$\Delta U = \int_{T_1}^{T_2}C_V\mathrm{d}T. \quad (16.7)$$

This is only true for systems held at constant volume; we would like to be able to extend this to systems held at constant pressure (an easier constraint to apply experimentally), and this can be achieved using the thermodynamic potential called enthalpy, which we describe next.

## 16.2 Enthalpy, $H$

We define the enthalpy $H$ by

$$H = U + pV. \quad (16.8)$$

This definition together with eqn 16.1 implies that

$$\begin{array}{rcl}{\mathrm{d}H} & = & {T\mathrm{d}S - p\mathrm{d}V + p\mathrm{d}V + V\mathrm{d}p}\\ {} & = & {T\mathrm{d}S + V\mathrm{d}p.} \end{array} \quad (16.9)$$

The natural variables for $H$ are thus $S$ and $p$, and we have that $H = H(S,p)$. We can therefore immediately write down that for a isobaric (i.e., constant pressure) process,

$$\mathrm{d}H = T\mathrm{d}S, \quad (16.10)$$

and for a reversible isobaric process

$$\mathrm{d}H = \mathrm{d}Q_{\mathrm{rev}} = C_p\mathrm{d}T, \quad (16.11)$$

so that

$$\Delta H = \int_{T_1}^{T_2}C_p\mathrm{d}T. \quad (16.12)$$

This shows the importance of $H$, that for reversible isobaric processes the enthalpy represents the heat absorbed by the system. Isobaric conditions are relatively easy to obtain: an experiment that is open to the air in a laboratory is usually at constant pressure since pressure is provided by the atmosphere. We also conclude from eqn 16.9 that if both $S$ and $p$ are constant, we have that $\mathrm{d}H = 0$.

Equation 16.9 also implies that

$$T = \left(\frac{\partial H}{\partial S}\right)_p, \quad (16.13)$$

and

$$V = \left(\frac{\partial H}{\partial p}\right)_S. \quad (16.14)$$

Both $U$ and $H$ suffer from the drawback that one of their natural variables is the entropy $S$, which is not a very easy parameter to vary in a lab. It would be more convenient if we could substitute that for the temperature $T$, which is, of course, a much easier quantity to control and to vary. This is accomplished for both of our next two functions of state, the Helmholtz and Gibbs functions.

## 16.3 Helmholtz function, $F$

We define the Helmholtz function using

$$F = U - TS. \quad (16.15)$$

Hence we find that

$$\begin{array}{rcl}{\mathrm{d}F} & = & {T\mathrm{d}S - p\mathrm{d}V - T\mathrm{d}S - S\mathrm{d}T}\\ {} & = & {- S\mathrm{d}T - p\mathrm{d}V.} \end{array} \quad (16.16)$$

This implies that the natural variables for $F$ are $V$ and $T$, and we can therefore write $F = F(T,V)$. For an isothermal process (constant $T$), we can simplify eqn 16.16 further and write that

$$\mathrm{d}F = -p\mathrm{d}V, \quad (16.17)$$

and hence

$$\Delta F = -\int_{V_1}^{V_2}pdV. \quad (16.18)$$

Hence a positive change in $F$ represents reversible work done on the system by the surroundings, while a negative change in $F$ represents reversible work done on the surroundings by the system. As we shall see in Section 16.5, $F$ represents the maximum amount of work you can get out of a system at constant temperature, since the system will do work on its surroundings until its Helmholtz function reaches a minimum. Equation 16.16 implies that the entropy $S$ can be written as

$$S = -\left(\frac{\partial F}{\partial T}\right)_V, \quad (16.19)$$

and the pressure $p$ as

$$p = -\left(\frac{\partial F}{\partial V}\right)_T. \quad (16.20)$$

If $T$ and $V$ are constant, we have that $\mathrm{d}F = 0$ and $F$ is a constant.

## 16.4 Gibbs function, $G$

We define the Gibbs function using

$$G = H - TS. \quad (16.21)$$

Hence we find that

$$\begin{array}{rcl}{\mathrm{d}G} & = & {T\mathrm{d}S + V\mathrm{d}p - T\mathrm{d}S - S\mathrm{d}T}\\ {} & = & {- S\mathrm{d}T + V\mathrm{d}p,} \end{array} \quad (16.22)$$

and the natural variables of $G$ are $T$ and $p$. [Hence we can write $G = G(T,p)$.]

Having $T$ and $p$ as natural variables is particularly convenient as $T$ and $p$ are the easiest quantities to manipulate and control for most experimental systems. In particular, note that if $T$ and $p$ are constant, $\mathrm{d}G = 0$. Hence $G$ is conserved in any isothermal isobaric process.

The expression in eqn 16.22 allows us to write down expressions for entropy and volume as follows:

$$S = -\left(\frac{\partial G}{\partial T}\right)_p \quad (16.23)$$

and

$$V = \left(\frac{\partial G}{\partial p}\right)_T. \quad (16.24)$$

We have now defined the four main thermodynamic potentials, which are useful in much of thermal physics: the internal energy $U$, the enthalpy $H$, the Helmholtz function $F$, and the Gibbs function $G$. Before proceeding further, we summarize the main equations which we have used so far.

| Function of state | Differential | Natural variables | First derivatives |
| :--- | :--- | :--- | :--- |
| Internal energy $U$ | $\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V$ | $U = U(S, V)$ | $T = \left(\frac{\partial U}{\partial S}\right)_V$, $p = -\left(\frac{\partial U}{\partial V}\right)_S$ |
| Enthalpy $H = U + pV$ | $\mathrm{d}H = T\mathrm{d}S + V\mathrm{d}p$ | $H = H(S, p)$ | $T = \left(\frac{\partial H}{\partial S}\right)_p$, $V = \left(\frac{\partial H}{\partial p}\right)_S$ |
| Helmholtz function $F = U - TS$ | $\mathrm{d}F = -S\mathrm{d}T - p\mathrm{d}V$ | $F = F(T, V)$ | $S = -\left(\frac{\partial F}{\partial T}\right)_V$, $p = -\left(\frac{\partial F}{\partial V}\right)_T$ |
| Gibbs function $G = H - TS$ | $\mathrm{d}G = -S\mathrm{d}T + V\mathrm{d}p$ | $G = G(T, p)$ | $S = -\left(\frac{\partial G}{\partial T}\right)_p$, $V = \left(\frac{\partial G}{\partial p}\right)_T$ |

Note that to derive these equations quickly, all you need to do is memorize the definitions of $H$, $F$ and $G$ and the first law in the form $\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V$ and the rest can be written down straightforwardly.

## Example 16.1

Show that $U = - T^{2}\left(\frac{\partial}{\partial T}\right)_{V}\frac{F}{T}$ and $H = - T^{2}\left(\frac{\partial}{\partial T}\right)_{p}\frac{G}{T}$.

Solution:

Using the expressions

$$S = -\left(\frac{\partial F}{\partial T}\right)_V\qquad \mathrm{and}\qquad S = -\left(\frac{\partial G}{\partial T}\right)_p,$$

we can write down

$$U = F + TS = F - T\left(\frac{\partial F}{\partial T}\right)_V = -T^2\left(\frac{\partial(F / T)}{\partial T}\right)_V \quad (16.25)$$

and

$$H = G + TS = G - T\left(\frac{\partial G}{\partial T}\right)_p = -T^2\left(\frac{\partial(G / T)}{\partial T}\right)_p. \quad (16.26)$$

These equations are known as the Gibbs-Helmholtz equations and are useful in chemical thermodynamics.

## 16.5 Constraints

We have seen that the thermodynamic potentials are valid functions of state and have particular properties. But we have not yet seen how they might be useful, and there might be a suspicion lurking that $H$, $F$, and $G$ are rather artificial objects whereas $U$, the internal energy, is the only natural one. This is not the case, as we shall now show. However, which of these functions of state is the most useful one depends on the context of the problem, and in particular on the type of constraint that is applied to the system.

Consider a large mass sitting on the top of a cliff, near the edge. This system has the potential to provide useful work, since one could connect the mass to a pulley system, lower the mass down the cliff edge and extract mechanical work. When the mass lies at the bottom of the cliff, no more useful work can be obtained. It would be very useful to have a quantity that depends on the amount of available useful work a system can provide, and we call such a quantity the free energy. In working out what the free energy is in any particular situation, we have to remember that a system can exchange energy with its surroundings, and how it does that rather depends on what sort of constraint the surroundings apply to the system. We shall first demonstrate this using a particular case, and then proceed to the general case.

Consider first a system with fixed volume, held at a temperature $T$ by its contact with the surroundings. If heat $\mathrm{d}Q$ enters the system, the entropy $S_{0}$ of the surroundings changes by $\mathrm{d}S_{0} = - \mathrm{d}Q / T$ and the change in entropy of the system, $\mathrm{d}S$, must be such that the total change in entropy of the Universe must be greater than, or equal to, zero (i.e., $\mathrm{d}S + \mathrm{d}S_{0}\geq 0$). Hence $\mathrm{d}S - \mathrm{d}Q / T\geq 0$ and so $T\mathrm{d}S\geq \mathrm{d}Q$. Now by the first law, $\mathrm{d}Q = \mathrm{d}U - \mathrm{d}W$ and so the work added to the system must satisfy

$$\mathrm{d}W\geq \mathrm{d}U - T\mathrm{d}S. \quad (16.27)$$

Now since $T$ is fixed, $\mathrm{d}F = \mathrm{d}(U - TS) = \mathrm{d}U - T\mathrm{d}S$, and hence eqn 16.27 can be written

$$\mathrm{d}W\geq \mathrm{d}F. \quad (16.28)$$

What we have shown is that adding work to the system increases the system's Helmholtz function (which we may now call a Helmholtz free energy). In a reversible process, $\mathrm{d}W = \mathrm{d}F$ and the work added to the system goes directly into an increase of Helmholtz free energy. If we extract a certain amount of work from the system $(\mathrm{d}W< 0)$, then this will be associated with at least as big a drop in the sample's Helmholtz free energy (equality only being obtained in a reversible process). Returning to our analogy, adding work to the system hauls the mass up to the top of the cliff and gives it the potential to do work in the future (adding free energy to the system), extracting work from the system occurs by letting the mass drop down the cliff and reduces its potential to provide work in the future (subtracting free energy from the system).

Another example is a quantity of oil, which stores free energy that can be released when the oil is burned. However, how that free energy is defined depends on how the oil is burned. If it burns inside a sealed drum containing only oil and air, then the combustion will take place in a fixed volume. In this case, the relevant free energy is the Helmholtz function, as above. However, if the oil is burned in the open air, then the combustion products will need to push against the atmosphere and the free energy will be the Gibbs function, as we shall show.

Note that if the system is mechanically isolated from its surroundings, so that no work can be applied or extracted, then $\mathrm{d}W = 0$ and eqn 16.28 becomes

$$\mathrm{d}F\leq 0. \quad (16.29)$$

Thus any change in $F$ will be negative. As the system settles down towards equilibrium, all processes will tend to force $F$ downwards. Once the system has reached equilibrium, $F$ will be constant at this minimum level. Hence equilibrium can only be achieved by minimizing $F$.

We now need to repeat the argument we used to justify eqns 16.28 and 16.29 for more general constraints. In general, a system is able to exchange heat with its surroundings and also, if the system's volume changes, it may do work on its surroundings. Let us now consider a system in contact with surroundings at temperature $T_{0}$ and pressure $p_{0}$ (see Fig. 16.1). As described above, if heat $\mathrm{d}Q$ enters the system, the entropy change of the system satisfies $T_{0}\mathrm{d}S\geq \mathrm{d}Q$. In the general case, we write the first law as

$$\mathrm{d}Q = \mathrm{d}U - \mathrm{d}W - (-p_0\mathrm{d}V), \quad (16.30)$$

[Image: A diagram showing a system (white box) surrounded by surroundings (grey area) at temperature T0 and pressure p0.]
**Fig. 16.1** A system in contact with surroundings at temperature $T_{0}$ and pressure $p_{0}$.

where we have explicitly separated the mechanical work $\mathrm{d}W$ added to the system from the work $- p_0\mathrm{d}V$ done by the surroundings due to the volume change of the system. Putting this all together gives

$$\mathrm{d}W\geq \mathrm{d}U + p_0\mathrm{d}V - T_0\mathrm{d}S. \quad (16.31)$$

We now define the availability $A$ by

$$A = U + p_0V - T_0S, \quad (16.32)$$

and because $p_0$ and $T_0$ are constants, we have

$$\mathrm{d}A = \mathrm{d}U + p_0\mathrm{d}V - T_0\mathrm{d}S. \quad (16.33)$$

Hence eqn 16.31 becomes

$$\mathrm{d}W\geq \mathrm{d}A, \quad (16.34)$$

which generalizes eqn 16.28. Changes in availability provide free energy "available" for doing work. $A$ will change its form depending on the type of constraint, as shown below. First, note that just as we found eqn 16.29 for the specific case of fixed $V$ and $T$, in the general case the availability can be used to express a general minimization principle. If the system is mechanically isolated, then

$$\mathrm{d}A\leq 0, \quad (16.35)$$

which generalizes eqn 16.29. We have derived this inequality from the second law of thermodynamics. It demonstrates that changes in $A$ are always negative. All processes will tend to force $A$ downwards towards a minimum value. Once the system has reached equilibrium, $A$ will be constant at this minimum level. Hence equilibrium can only be achieved by minimizing $A$. However, the type of equilibrium achieved depends on the nature of the constraints, as we will now show.

**System thermally isolated and with fixed volume:**
Since no heat can enter the system and the system can do no work on its surroundings, $\mathrm{d}U = 0$. Hence eqn 16.33 becomes $\mathrm{d}A = - T_0\mathrm{d}S$ and therefore $\mathrm{d}A\leq 0$ implies that $\mathrm{d}S\geq 0$. Thus we must maximize $S$ to find the equilibrium state.

**System with fixed volume at constant temperature:**
$\mathrm{d}A = \mathrm{d}U - T_0\mathrm{d}S\leq 0$ but the temperature is fixed, $\mathrm{d}T = 0$, and so $\mathrm{d}F = \mathrm{d}U - T_0\mathrm{d}S - S\mathrm{d}T = \mathrm{d}U - T_0\mathrm{d}S$, leading to

$$\mathrm{d}A = \mathrm{d}F\leq 0, \quad (16.36)$$

so we must minimize $F$ to find the equilibrium state.

**System at constant pressure and temperature:**
Eqn 16.33 gives $\mathrm{d}A = \mathrm{d}U - T_0\mathrm{d}S + p_0\mathrm{d}V\leq 0$. We can write dG (from the definition $G = H - TS$) as

$$\mathrm{d}G = \mathrm{d}U + p_0\mathrm{d}V + V\mathrm{d}p - T_0\mathrm{d}S - S\mathrm{d}T = \mathrm{d}U - T_0\mathrm{d}S + p_0\mathrm{d}V, \quad (16.37)$$

because $p$ and $T$ are both constant and hence $\mathrm{d}p = 0$ and $\mathrm{d}T = 0$. Thus

$$\mathrm{d}A = \mathrm{d}G\leq 0, \quad (16.38)$$

so we must minimize $G$ to find the equilibrium state.

## Example 16.2

Chemistry laboratories are usually at constant pressure. If a chemical reaction is carried out at constant pressure, then by eqn 16.11 we have

$$\Delta H = \Delta Q, \quad (16.39)$$

and hence $\Delta H$ is the reversible heat added to the system, i.e., the heat absorbed by the reaction. (Recall that our convention is that $\Delta Q$ is the heat entering the system, and in this case the system is the reacting chemicals.)

If $\Delta H< 0$ the reaction is called exothermic and heat will be emitted. If $\Delta H > 0$ the reaction is called endothermic and heat will be absorbed.

However, this does not tell you whether or not a chemical reaction will actually proceed. Usually reactions occur at constant $T$ and $p$ so if the system is trying to minimize its availability, then we need to consider $\Delta G$. The second law of thermodynamics (via eqn 16.35 and hence eqn 16.38) therefore implies that a chemical system will minimize $G$ so that if $\Delta G< 0$ the reaction may spontaneously occur.

## 16.6 Maxwell's relations

In this section, we are going to derive four equations, which are known as Maxwell's relations. These equations are very useful in solving problems in thermodynamics, since each one relates a partial differential between quantities that can be hard to measure to a partial differential between quantities that can be much easier to measure. The derivation proceeds along the following lines: a state function $f$ is a function of variables $x$ and $y$. A change in $f$ can be written as

$$\mathrm{d}f = \left(\frac{\partial f}{\partial x}\right)_y\mathrm{d}x + \left(\frac{\partial f}{\partial y}\right)_x\mathrm{d}y. \quad (16.40)$$

Because df is an exact differential (see Appendix C.7), we have

$$\left(\frac{\partial^2f}{\partial x\partial y}\right) = \left(\frac{\partial^2f}{\partial y\partial x}\right). \quad (16.41)$$

Hence writing

$$F_{x} = \left(\frac{\partial f}{\partial x}\right)_{y}\mathrm{and}F_{y} = \left(\frac{\partial f}{\partial y}\right)_{x}, \quad (16.42)$$

we have

$$\left(\frac{\partial F_y}{\partial x}\right) = \left(\frac{\partial F_x}{\partial y}\right). \quad (16.43)$$

We can now apply this idea to each of the state variables $U$, $H$, $F$, and $G$ in turn.

## Example 16.3

The Maxwell relation based on $G$ can be derived as follows. We write down an expression for $\mathrm{d}G$:

$$\mathrm{d}G = -S\mathrm{d}T + V\mathrm{d}p. \quad (16.44)$$

We can also write

$$\mathrm{d}G = \left(\frac{\partial G}{\partial T}\right)_p\mathrm{d}T + \left(\frac{\partial G}{\partial p}\right)_T\mathrm{d}p, \quad (16.45)$$

and hence we can write $S = - (\partial G / \partial T)_p$ and $V = (\partial G / \partial p)_T$. Because $\mathrm{d}G$ is an exact differential, we have

$$\left(\frac{\partial^2G}{\partial T\partial p}\right) = \left(\frac{\partial^2G}{\partial p\partial T}\right), \quad (16.46)$$

and hence we have the following Maxwell relation:

$$-\left(\frac{\partial S}{\partial p}\right)_T = \left(\frac{\partial V}{\partial T}\right)_p. \quad (16.47)$$

This reasoning can be applied to each of the thermodynamic potentials $U$, $H$, $F$, and $G$ to yield the four Maxwell's relations:

**Maxwell's relations:**

$$\begin{array}{rcl}\left(\frac{\partial T}{\partial V}\right)_S & = & -\left(\frac{\partial p}{\partial S}\right)_V\\ \left(\frac{\partial T}{\partial p}\right)_S & = & \left(\frac{\partial V}{\partial S}\right)_p\\ \left(\frac{\partial S}{\partial V}\right)_T & = & \left(\frac{\partial p}{\partial T}\right)_V\\ \left(\frac{\partial S}{\partial p}\right)_T & = & -\left(\frac{\partial V}{\partial T}\right)_p \end{array} \quad (16.50)$$

We have said that Maxwell's relations relate a partial differential that corresponds to something that can be easily measured to a partial differential that cannot. For example, in eqn 16.51 the term $(\partial V / \partial T)_p$ on the right-hand side tells you how the volume changes as you increase the temperature while keeping the pressure fixed. This is related to a quantity called the isobaric expansivity and is a quantity you can easily imagine being something one could measure in a laboratory. However, the term on the left-hand side of eqn 16.51, $(\partial S / \partial p)_T$, is much more mysterious and it is not obvious how a change of entropy with pressure at constant temperature could actually be measured. Fortunately, a Maxwell relation relates it to something which can be.

Maxwell's relations should not be memorized; rather it is better to remember how to derive them!

A more sophisticated way of deriving these equations based on Jacobians (which may not be to everybody's taste) is outlined in the box below. It has the attractive virtue of producing all four relations in one go by directly relating the work done and heat absorbed in a cyclic process, but the unfortunate vice of requiring easy familiarity with the use of Jacobian transformations.

## An alternative derivation of Maxwell's relations

The following derivation is more elegant, but requires a knowledge of Jacobians (see Appendix C.9). Consider a cyclic process that can be described in both the $T - S$ and $p - V$ planes. The internal energy $U$ is a state function and therefore doesn't change in a cycle, so $\oint \mathrm{d}U = 0$ which implies that $\oint p\mathrm{d}V = \oint T\mathrm{d}S$, and hence

$$\int \int \mathrm{d}p\mathrm{d}V = \int \int \mathrm{d}T\mathrm{d}S. \quad (16.52)$$

This says that the work done (the area enclosed by the cycle in the $p - V$ plane) is equal to the heat absorbed (the area enclosed by the cycle in the $T - S$ plane). However, one can also write

$$\int \int \mathrm{d}p\mathrm{d}V\frac{\partial(T,S)}{\partial(p,V)} = \int \int \mathrm{d}T\mathrm{d}S, \quad (16.53)$$

where $\partial (T,S) / \partial (p,V)$ is the Jacobian of the transformation from the $p - V$ plane to the $T - S$ plane, and so these two equations imply that

$$\frac{\partial(T,S)}{\partial(p,V)} = 1. \quad (16.54)$$

This equation is sufficient to generate all four Maxwell relations via

$$\frac{\partial(T,S)}{\partial(x,y)} = \frac{\partial(p,V)}{\partial(x,y)}, \quad (16.55)$$

where $(x,y)$ are taken as (i) $(T,p)$, (ii) $(T,V)$, (iii) $(p,S)$, and (iv) $(S,V)$, and using the identities in Appendix C.9.

We will now give several examples of how Maxwell's relations can be used to solve problems in thermodynamics.

## Example 16.4

Find expressions for $(\partial C_p/\partial p)_T$ and $(\partial C_V / \partial V )_T$ in terms of $p, V$, and $T$.

Solution:

By the definitions of $C_V$ and $C_p$ we have that

$$C_V = \left(\frac{\partial Q}{\partial T}\right)_V = T\left(\frac{\partial S}{\partial T}\right)_V \quad (16.56)$$

and

$$C_p = \left(\frac{\partial Q}{\partial T}\right)_p = T\left(\frac{\partial S}{\partial T}\right)_p. \quad (16.57)$$

Now

$$\left(\frac{\partial C_p}{\partial p}\right)_T = \left(\frac{\partial}{\partial p}T\left(\frac{\partial S}{\partial T}\right)_p\right)_T = T\left(\frac{\partial}{\partial p}\left(\frac{\partial S}{\partial T}\right)_p\right)_T = T\left(\frac{\partial}{\partial T}\left(\frac{\partial S}{\partial p}\right)_T\right)_p \quad (16.58)$$

and therefore, using one of the Maxwell's relations,

$$\left(\frac{\partial C_p}{\partial p}\right)_T = -T\left(\frac{\partial}{\partial T}\left(\frac{\partial V}{\partial T}\right)_p\right)_p = -T\left(\frac{\partial^2 V}{\partial T^2}\right)_p. \quad (16.59)$$

Similarly

$$\left(\frac{\partial C_V}{\partial V}\right)_T = T\left(\frac{\partial^2 p}{\partial T^2}\right)_V. \quad (16.60)$$

Both the expressions in eqns 16.59 and 16.60 are zero for a perfect gas.

Before proceeding further with the examples, we will pause to list the tools which you have at your disposal to solve these sorts of problems. Any given problem may not require you to use all of these, but you may have to use more than one of these "techniques".

(1) Write down a thermodynamic potential in terms of particular variables.

If $f$ is a function of $x$ and $y$, so that $f = f(x, y)$, you then have immediately that

$$df = \left(\frac{\partial f}{\partial x}\right)_y dx + \left(\frac{\partial f}{\partial y}\right)_x dy. \quad (16.61)$$

(2) Use Maxwell's relations to transform the partial differential you start with into a more convenient one. Use the Maxwell's relations in eqns 16.48–16.51.

(3) Invert a Maxwell's relation using the reciprocal theorem. The reciprocal theorem states that

$$\left(\frac{\partial x}{\partial z}\right)_y = \frac{1}{\left(\frac{\partial z}{\partial x}\right)_y}, \quad (16.62)$$

and this is proved in Appendix C.6 (see eqn C.41).

(4) Combine partial differentials using the reciprocity theorem. The reciprocity theorem states that

$$\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1, \quad (16.63)$$

which is proved in Appendix C.6 (see eqn C.42). This can be combined with the reciprocal theorem to write that

$$\left(\frac{\partial x}{\partial y}\right)_z = -\left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x, \quad (16.64)$$

which is a very useful identity.

(5) Identify a heat capacity. Some of the partial differentials appearing in Maxwell's relations relate to real, measurable properties. As we have seen in Example 16.4, both $\left(\frac{\partial S}{\partial T}\right)_V$ and $\left(\frac{\partial S}{\partial T}\right)_p$ can be related to heat capacities:

$$\frac{C_V}{T} = \left(\frac{\partial S}{\partial T}\right)_V \quad \text{and} \quad \frac{C_p}{T} = \left(\frac{\partial S}{\partial T}\right)_p. \quad (16.65)$$

(6) Identify a "generalized susceptibility". A generalized susceptibility quantifies how much a particular variable changes when a generalized force is applied. A generalized force is a variable such as $T$ or $p$ which is a differential of the internal energy with respect to some other parameter. An example of a generalized susceptibility is $\left(\frac{\partial V}{\partial T}\right)_x$ which, you will recall, answers the question "keeping $x$ constant, how much does the volume change when you change the temperature?" It is related to the thermal expansivity at constant $x$, where $x$ is pressure or entropy. Thus the isobaric expansivity $\beta_p$ is defined as

$$\beta_p = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p, \quad (16.66)$$

while the adiabatic expansivity $\beta_S$ is defined as

$$\beta_S = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_S. \quad (16.67)$$

Expansivities measure the fractional change in volume with a change in temperature.

Another useful generalized susceptibility is the compressibility. This quantifies how large a fractional volume change you achieve when you apply pressure. The isothermal compressibility $\kappa_T$ is defined as

$$\kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T, \quad (16.68)$$

while the adiabatic compressibility $\kappa_S$ is defined as

$$\kappa_S = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_S. \quad (16.69)$$

Both quantities have a minus sign so that the compressibilities are positive (this is because things get smaller when you press them, so fractional volume changes are negative when positive pressure is applied). None of these expansivities or compressibilities appears directly in a Maxwell relation, but each can easily be related to those that do using the reciprocal and reciprocity theorems.

## Example 16.5

By considering $S = S(T, V)$, show that $C_p - C_V = V T\beta^2_p/\kappa_T$.

Solution:

Considering $S = S(T, V)$ allows us to write down immediately that

$$dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV. \quad (16.70)$$

Differentiating this equation with respect to $T$ at constant $p$ yields

$$\left(\frac{\partial S}{\partial T}\right)_p = \left(\frac{\partial S}{\partial T}\right)_V + \left(\frac{\partial S}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p. \quad (16.71)$$

Now the first two terms can be replaced by $C_p/T$ and $C_V/T$ respectively, while use of a Maxwell's relation and a partial differential identity (see eqn 16.64) yields

$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V = -\left(\frac{\partial p}{\partial V}\right)_T \left(\frac{\partial V}{\partial T}\right)_p \quad (16.72)$$

and hence using eqns 16.66 and 16.68 we have that

$$C_p - C_V = \frac{V T\beta^2_p}{\kappa_T}. \quad (16.73)$$

The next example shows how to calculate the entropy of an ideal gas.

## Example 16.6

Find the entropy of 1 mole of ideal gas.

Solution:

For one mole of ideal gas $pV = RT$. Consider the entropy $S$ as a function of volume and temperature, i.e.,

$$S = S(T, V), \quad (16.74)$$

so that

$$dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV \quad (16.75)$$
$$= \frac{C_V}{T} dT + \left(\frac{\partial p}{\partial T}\right)_V dV, \quad (16.76)$$

using eqn 16.50 and eqn 16.65. The ideal gas law for 1 mole, $p = RT/V$, implies that

$$\left(\frac{\partial p}{\partial T}\right)_V = R/V, \quad (16.77)$$

and hence, if we integrate eqn 16.76,

$$S = \int \frac{C_V}{T} dT + \int \frac{RdV}{V}. \quad (16.78)$$

If $C_V$ is not a function of temperature (which is true for an ideal gas) simple integration yields

$$S = C_V \ln T + R \ln V + \text{constant}. \quad (16.79)$$

The entropy of an ideal gas increases with increasing temperature and increasing volume.

The final example in this chapter shows how to prove that the ratio of the isothermal and adiabatic compressibilities, $\kappa_T/\kappa_S$, is equal to $\gamma$.

## Example 16.7

Find the ratio of the isothermal and adiabatic compressibilities.

Solution:

This follows using straightforward manipulations of partial differentials. To begin with, we write

$$\frac{\kappa_T}{\kappa_S} = \frac{\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T}{\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_S}, \quad (16.80)$$

which follows from the definitions of $\kappa_T$ and $\kappa_S$ (eqns 16.68 and 16.69). Then we proceed as follows:

$$\frac{\kappa_T}{\kappa_S} = \frac{-\left(\frac{\partial V}{\partial T}\right)_p \left(\frac{\partial T}{\partial p}\right)_V}{-\left(\frac{\partial V}{\partial S}\right)_p \left(\frac{\partial S}{\partial p}\right)_V} \quad \text{(reciprocity theorem, eqn 16.64)}$$
$$= \frac{\left(\frac{\partial V}{\partial T}\right)_p \left(\frac{\partial S}{\partial V}\right)_p}{\left(\frac{\partial p}{\partial T}\right)_V \left(\frac{\partial S}{\partial p}\right)_V} \quad \text{(reciprocal theorem, eqn 16.62)}$$
$$= \frac{\left(\frac{\partial S}{\partial T}\right)_p}{\left(\frac{\partial S}{\partial T}\right)_V} \quad \text{(simplify numerator and denominator)}$$
$$= \frac{C_p/T}{C_V/T} = \gamma. \quad (16.81)$$

We can show that this equation is correct for the case of an ideal gas as follows. Assuming the ideal gas equation $pV \propto T$, we have for constant temperature that

$$\frac{dp}{p} = -\frac{dV}{V}, \quad (16.82)$$

and hence using eqn 16.68 we have

$$\kappa_T = \frac{1}{p}. \quad (16.83)$$

For an adiabatic change $p \propto V^{-\gamma}$ and hence

$$\frac{dp}{p} = -\gamma \frac{dV}{V}, \quad (16.84)$$

and hence using eqn 16.69 we have

$$\kappa_S = \frac{1}{\gamma p}. \quad (16.85)$$

This agrees with eqn 16.81 above. We note that because $\kappa_T$ is larger than $\kappa_S$ (because $\gamma > 1$), the isotherms always have a smaller gradient than the adiabats on a $p$–$V$ plot (see Fig. 12.1).

## Chapter summary

- We define the following thermodynamic potentials:
$$U,$$
$$H = U + pV,$$
$$F = U - TS,$$
$$G = H - TS,$$
which are then related by the following differentials:

| | |
| :--- | :--- |
| $dU$ | $= TdS - pdV$ |
| $dH$ | $= TdS + Vdp$ |
| $dF$ | $= -SdT - pdV$ |
| $dG$ | $= -SdT + Vdp$ |

- The availability $A$ is given by $A = U + p_0V - T_0S$, and for any spontaneous change we have that $dA \leq 0$. This means that a system in contact with a reservoir (temperature $T_0$, pressure $p_0$) will minimize $A$ which means
  - minimizing $U$ when $S$ and $V$ are fixed;
  - minimizing $H$ when $S$ and $p$ are fixed;
  - minimizing $F$ when $T$ and $V$ are fixed;
  - minimizing $G$ when $T$ and $p$ are fixed.
- Four Maxwell's relations can be derived from the boxed equations above, and used to solve many problems in thermodynamics.

## Exercises

(16.1) (a) Using the first law $dU = TdS - pdV$ to provide a reminder, write down the definitions of the four thermodynamic potentials $U, H, F, G$ (in terms of $U, S, T, p, V$), and give $dU, dH, dF, dG$ in terms of $T, S, p, V$ and their derivatives.

(b) Derive all the Maxwell's relations.

(16.2) (a) Derive the following general relations

(i) $\left(\frac{\partial T}{\partial V}\right)_U = -\frac{1}{C_V}\left[T\left(\frac{\partial p}{\partial T}\right)_V - p\right]$,

(ii) $\left(\frac{\partial T}{\partial V}\right)_S = -\frac{1}{C_V}T\left(\frac{\partial p}{\partial T}\right)_V$,

(iii) $\left(\frac{\partial T}{\partial p}\right)_H = \frac{1}{C_p}\left[T\left(\frac{\partial V}{\partial T}\right)_p - V\right]$.

In each case the quantity on the left-hand side is the appropriate thing to consider for a particular type of expansion. State what type of expansion each refers to.

(b) Using these relations, verify that for an ideal gas $(\partial T/\partial V)_U = 0$ and $(\partial T/\partial p)_H = 0$, and that $(\partial T/\partial V)_S$ leads to the familiar relation $pV^\gamma = \text{constant}$ along an isentrope (a curve of constant entropy).

(16.3) Use the first law of thermodynamics to show that

$$\left(\frac{\partial U}{\partial V}\right)_T = \frac{C_p - C_V}{V\beta_p} - p, \quad (16.86)$$

where $\beta_p$ is the coefficient of volume expansivity and the other symbols have their usual meanings.

(16.4) (a) The natural variables for $U$ are $S$ and $V$. This means that if you know $S$ and $V$, you can find $U(S, V)$. Show that this also gives you simple expressions for $T$ and $p$.

(b) Suppose instead that you know $V$, $T$ and the function $U(T, V)$ (i.e., you have expressed $U$ in terms of variables that are not all the natural variables of $U$). Show that this leads to a (much more complicated) expression for $p$, namely

$$\frac{p}{T} = \int \left(\frac{\partial U}{\partial V}\right)_T \frac{dT}{T^2} + f(V), \quad (16.87)$$

where $f(V)$ is some (unknown) function of $V$.

(16.5) Use thermodynamic arguments to obtain the general result that, for any gas at temperature $T$, the pressure is given by

$$P = T\left(\frac{\partial P}{\partial T}\right)_V - \left(\frac{\partial U}{\partial V}\right)_T, \quad (16.88)$$

where $U$ is the total energy of the gas.

(16.6) Show that another expression for the entropy per mole of an ideal gas is

$$S = C_p \ln T - R \ln p + \text{constant}. \quad (16.89)$$

(16.7) Show that the entropy of an ideal gas can be expressed as

$$S = C_V \ln \left(\frac{p}{\rho^\gamma}\right) + \text{constant}. \quad (16.90)$$

[Image: A portrait of H. von Helmholtz]
**Fig. 16.2** H. von Helmholtz

[Image: A portrait of William Thomson]
**Fig. 16.3** William Thomson

[Image: A portrait of J. W. Gibbs]
**Fig. 16.4** J. W. Gibbs

===== Page 191 =====

# 17 Rods, bubbles, and magnets

17.1 Elastic rod  191
17.2 Surface tension  194
17.3 Electric and magnetic dipoles  195
17.4 Paramagnetism  196
Chapter summary  200
Exercises  201

In this book, we have been illustrating the development of thermodynamics using the ideal gas as our chief example. We have written the first law of thermodynamics as

$$dU = T dS - p dV, \quad (17.1)$$

and everything has followed from this. However, in this chapter we want to show that thermodynamics can be applied to other types of system. In general we will write the work $\bar{d}W$ as

$$\bar{d}W = X dx, \quad (17.2)$$

where $X$ is some (intensive) generalized force and $x$ is some (extensive) generalized displacement. Examples of these are given in Table 17.1. In this chapter we will examine only three of these examples in detail: the elastic rod, the surface tension in a liquid and the assembly of magnetic moments in a paramagnet.

| $X$ | $x$ | $\bar{d}W$ |
| :--- | :--- | :--- |
| fluid | $-p$ | $V$ | $-p dV$ |
| elastic rod | $f$ | $L$ | $f dL$ |
| liquid film | $\gamma$ | $A$ | $\gamma dA$ |
| dielectric | $E$ | $p_E$ | $-p_E \cdot dE$ |
| magnetic | $B$ | $m$ | $-m \cdot dB$ |

**Table 17.1** Generalized force $X$ and generalized displacement $x$ for various different systems. In this table, $p =$ pressure, $V =$ volume, $f =$ tension, $L =$ length, $\gamma =$ surface tension, $A =$ area, $E =$ electric field, $p_E =$ electric dipole moment, $B =$ magnetic field, $m =$ magnetic dipole moment.

## 17.1 Elastic rod

Consider a rod with cross-sectional area $A$ and length $L$, held at temperature $T$. The rod is made from any elastic material (such as a metal or rubber) and is placed under an infinitesimal tension $df$, which leads to the rod extending by an infinitesimal length $dL$ (see Fig. 17.1). We define the isothermal Young's modulus $E_T$ as the ratio of stress $\sigma = df/A$ to strain $\epsilon = dL/L$, so that

$$E_T = \frac{\sigma}{\epsilon} = \frac{L}{A}\left(\frac{\partial f}{\partial L}\right)_T. \quad (17.3)$$

The Young's modulus $E_T$ is always a positive quantity.

There is another useful quantity that characterizes an elastic rod. We can also define the linear expansivity at constant tension, $\alpha_f$, by

$$\alpha_f = \frac{1}{L}\left(\frac{\partial L}{\partial T}\right)_f, \quad (17.4)$$

which is the fractional change in length with temperature. This quantity is positive in most elastic systems (though not rubber). If you hang a weight onto the end of a metal wire (thus keeping the tension $f$ in the wire constant) and heat the wire, it will extend. This implies that $\alpha_f > 0$ for a metal wire. However, if you hang a weight by a piece of rubber and supply heat, you will find that the rubber will contract, which implies that $\alpha_f < 0$ for rubber.

[Image: An elastic material of length L and cross-sectional area A is extended a length dL by a tension df.]
**Fig. 17.1** An elastic material of length $L$ and cross-sectional area $A$ is extended a length $dL$ by a tension $df$.

## Example 17.1

How does the tension of a wire held at constant length change with temperature?

Solution: Our definitions of $E_T$ and $\alpha_f$ allow us to calculate this. Using eqn C.42, we have that

$$\left(\frac{\partial f}{\partial T}\right)_L = -\left(\frac{\partial f}{\partial L}\right)_T \left(\frac{\partial L}{\partial T}\right)_f = -A E_T \alpha_f, \quad (17.5)$$

where the last step is obtained using eqns 17.3 and 17.4. This result is familiar to anyone who plays a metal-stringed instrument where $\alpha_f > 0$ and hence $(\partial f/\partial T)_L < 0$ from eqn 17.5; hot weather causes the strings (held at constant length) to slacken (reduce their tension).

We are now in a position to do some thermodynamics on our elastic system. We will rewrite the first law of thermodynamics for this case as

$$dU = T dS + f dL. \quad (17.6)$$

We can also obtain other thermodynamic potentials, such as the Helmholtz function $F = U - TS$, so that $dF = dU - T dS - S dT$, and hence

$$dF = -S dT + f dL. \quad (17.7)$$

Equation 17.7 implies that the entropy $S$ is

$$S = -\left(\frac{\partial F}{\partial T}\right)_L, \quad (17.8)$$

and similarly the tension $f$ is

$$f = \left(\frac{\partial F}{\partial L}\right)_T. \quad (17.9)$$

A Maxwell's-relation-type-step then leads to an expression for the isothermal change in entropy on extension as

$$\left(\frac{\partial S}{\partial L}\right)_T = -\left(\frac{\partial f}{\partial T}\right)_L. \quad (17.10)$$

The right-hand side of this equation was worked out in eqn 17.5, so that

$$\left(\frac{\partial S}{\partial L}\right)_T = A E_T \alpha_f, \quad (17.11)$$

where $A$ is the area (presumed not to change), and so stretching the rod (increasing $L$) results in an increase in entropy if $\alpha_f > 0$. This is like the case of an ideal gas for which

$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V > 0, \quad (17.12)$$

so that expanding the gas (increasing $V$) results in an increase in entropy. If the entropy of the system goes up as it is expanded isothermally, then heat must be absorbed. For the case of the elastic rod (assuming it is not made of rubber), extending it isothermally (and reversibly) by $\Delta L$ would then lead to an absorption of heat $\Delta Q$ given by

$$\Delta Q = T\Delta S = A E_T T \alpha_f \Delta L. \quad (17.13)$$

Why does stretching a wire increase its entropy? Let us consider the case of a metallic wire. This contains many small crystallites, which have low entropy. The action of stretching the wire distorts those small crystallites, and that increases their entropy and so heat is absorbed. In addition, the stretching of the wire may increase the volume per atom in the wire and this also increases the entropy.

However, for rubber $\alpha_f < 0$, and hence an isothermal extension means that heat is emitted. The action of stretching a piece of rubber at constant temperature results in the alignment of the long rubber molecules, reducing their entropy (see Fig. 17.2) and causing heat to be released.

[Image: Rubber consists of long-chain molecules. (a) With no force applied, the rubber molecule is quite coiled up and the average end-to-end distance is short, and the entropy is large. (b) With a force applied (along a vertical axis in this diagram), the molecule becomes more aligned with the direction of the applied force, and the end-to-end distance is large, reducing the entropy.]
**Fig. 17.2** Rubber consists of long-chain molecules. (a) With no force applied, the rubber molecule is quite coiled up and the average end-to-end distance is short, and the entropy is large. (b) With a force applied, the molecule becomes more aligned with the direction of the applied force, and the end-to-end distance is large, reducing the entropy.

## Example 17.2

The internal energy $U$ for an ideal gas does not change when it is expanded isothermally. How does $U$ change for an elastic rod when it is extended isothermally?

Solution: The change in internal energy on isothermal extension can be worked out from eqn 17.6 and eqn 17.11 by writing

$$\left(\frac{\partial U}{\partial L}\right)_T = T\left(\frac{\partial S}{\partial L}\right)_T + f = f + A T E_T \alpha_f. \quad (17.14)$$

This is the sum of a positive term expressing the energy going into the rod by work and a term expressing the heat flow into the rod due to an isothermal change of length. (For an ideal gas, a similar analysis applies, but the work done by the gas and the heat that flows into it balance perfectly, so that $U$ does not change.)

## 17.2 Surface tension

We now consider the case of a liquid surface with surface area $A$. Liquid surfaces cost energy, which is why a liquid will tend to form droplets (or, even better, a single droplet) to minimize this surface energy. The work needed to change the area of a liquid surface is given by

$$\bar{d}W = \gamma dA, \quad (17.15)$$

where $\gamma$ is a parameter known as the surface tension.

Consider the arrangement shown in Fig. 17.3. If the piston moves down, work $\bar{d}W = F dx = +p dV$ is done on the liquid (which is assumed to be incompressible). The droplet radius will therefore increase by an amount $dr$ such that $dV = 4\pi r^2 dr$, and the surface area of the droplet will change by an amount

$$dA = 4\pi(r + dr)^2 - 4\pi r^2 \approx 8\pi r dr, \quad (17.16)$$

so that

$$\bar{d}W = \gamma dA = 8\pi\gamma r dr. \quad (17.17)$$

Equating this to $\bar{d}W = F dx = +p dV = p \cdot 4\pi r^2 dr$ yields

$$p = \frac{2\gamma}{r}. \quad (17.18)$$

The pressure $p$ in this expression is, of course, really the pressure difference between the pressure in the liquid and the atmospheric pressure against which the surface of the drop pushes.

[Image: A spherical droplet of liquid of radius r is suspended from a thin pipe connected to a piston, which maintains the pressure p of the liquid.]
**Fig. 17.3** A spherical droplet of liquid of radius $r$ is suspended from a thin pipe connected to a piston, which maintains the pressure $p$ of the liquid.

## Example 17.3

What is the pressure of gas inside a spherical bubble of radius $r$?

Solution: The bubble (see Fig. 17.4) has two surfaces, and so the pressure $p_{\text{bubble}}$ of gas inside the bubble, minus the pressure $p_0$ outside the bubble, has to support two lots of surface tension. Hence, assuming the liquid wall of the bubble is thin (so that the radii of inner and outer walls are both $\approx r$),

$$p_{\text{bubble}} - p_0 = \frac{4\gamma}{r}. \quad (17.19)$$

[Image: A bubble of radius r has an inner and an outer surface.]
**Fig. 17.4** A bubble of radius $r$ has an inner and an outer surface.

Notice that surface tension has a microscopic explanation. A molecule in the bulk of the liquid is attracted to its nearest neighbours by intermolecular forces (which is what holds a liquid together), and these forces are applied to a given molecule by its neighbours from all directions. One can think of these forces almost as weak chemical bonds. The molecules at the surface are only attracted by their neighbouring molecules in one direction, back towards the bulk of the liquid, but there is no corresponding attractive force out into the "wild blue yonder". The surface has a higher energy than the bulk because bonds have to be broken in order to make a surface, and $\gamma$ tells you how much energy you need to form a unit area of surface (which gives an estimate of the size of the intermolecular forces).

We can write the first law of thermodynamics for our surface of area $A$ as

$$dU = T dS + \gamma dA \quad (17.20)$$

and similarly changes in the Helmholtz function can be written

$$dF = -S dT + \gamma dA, \quad (17.21)$$

which yields the Maxwell's relation

$$\left(\frac{\partial S}{\partial A}\right)_T = -\left(\frac{\partial \gamma}{\partial T}\right)_A. \quad (17.22)$$

Equation 17.20 implies that

$$\left(\frac{\partial U}{\partial A}\right)_T = T\left(\frac{\partial S}{\partial A}\right)_T + \gamma, \quad (17.23)$$

and hence using eqn 17.22, we have

$$\left(\frac{\partial U}{\partial A}\right)_T = \gamma - T\left(\frac{\partial \gamma}{\partial T}\right)_A, \quad (17.24)$$

the sum of a positive term expressing the energy going into a surface by work and a negative term expressing the heat flow into the surface due to an isothermal change of area. Usually, the surface tension has a temperature dependence as shown in Fig. 17.5, and hence $(\partial\gamma/\partial T)_A < 0$, so in fact both terms contribute a positive amount.

Heat $\Delta Q$ is given by

$$\Delta Q = T\left(\frac{\partial S}{\partial A}\right)_T \Delta A = -T\Delta A\left(\frac{\partial \gamma}{\partial T}\right)_A > 0, \quad (17.25)$$

and this is absorbed on isothermally stretching a surface to increase its area by $\Delta A$. This quantity is positive and so heat really is absorbed. Since $\left(\frac{\partial S}{\partial A}\right)_T$ is positive, this shows that the surface has an additional entropy compared with the bulk, in addition to costing extra energy.

[Image: Schematic diagram of the surface tension gamma of a liquid as a function of temperature. Since gamma must vanish at the boiling temperature Tb, we expect that (dgamma/dT)_A < 0.]
**Fig. 17.5** Schematic diagram of the surface tension $\gamma$ of a liquid as a function of temperature. Since $\gamma$ must vanish at the boiling temperature $T_b$, we expect that $(\partial\gamma/\partial T)_A < 0$.

## 17.3 Electric and magnetic dipoles

An electric dipole moment $p_E$ can interact with an electric field $E$. The potential energy of the dipole in the electric field is $-p_E \cdot E$. If the electric field changes, the interaction energy can change by

$$d(-p_E \cdot E) = -p_E \cdot dE - E \cdot dp_E. \quad (17.26)$$

There is also some stored energy in the dipole itself. An electric dipole consists of charges $+q$ and $-q$ separated by a distance $a$, so that the dipole moment has magnitude $p_E = qa$. The force on each charge due to the electric field has magnitude $qE$. A small change $da$ in the length $a$ means that the dipole moment changes by $dp_E = q da$. Modelling the bond between the charges as a spring, the work done on this spring because of the change of length is given by the force $qE$ times the distance $da$ which equals $E(q da) = E dp_E$. In the case in which the electric field is at an angle to the dipole moment, only the component of the electric field parallel to the dipole moment acts to stretch the spring, so in general we can write this contribution as $+E \cdot dp_E$. Adding this stored energy to the interaction energy from eqn 17.26 gives the work supplied to the system as

$$\bar{d}W = -p_E \cdot dE. \quad (17.27)$$

Analogous arguments can be used to show that the work supplied to a magnetic dipole is given by

$$\bar{d}W = -m \cdot dB. \quad (17.28)$$

We consider assemblies of magnetic moments in more detail in the next section.

## 17.4 Paramagnetism

Consider a system of magnetic moments arranged in a lattice at temperature $T$. We assume that the magnetic moments cannot interact with each other. If the application of a magnetic field causes the magnetic moments to line up, the system is said to exhibit paramagnetism. The equivalent formulation of the first law of thermodynamics for a paramagnet is

$$dU = T dS - m dB, \quad (17.29)$$

where $m$ is the magnetic moment and $B$ is the magnetic field. The magnetic moment $m = MV$, where $M$ is the magnetization and $V$ is the volume. The magnetic susceptibility $\chi$ is given by

$$\chi = \lim_{H \to 0} \frac{M}{H}. \quad (17.30)$$

For most paramagnets $\chi \ll 1$, so that $M \ll H$ and hence $B = \mu_0(H + M) \approx \mu_0 H$. This implies that we can write the magnetic susceptibility $\chi$ as

$$\chi \approx \frac{\mu_0 M}{B}. \quad (17.31)$$

Paramagnetic systems obey Curie's law, which states that

$$\chi \propto \frac{1}{T}, \quad (17.32)$$

as shown in Fig. 17.6, and hence

$$\left(\frac{\partial \chi}{\partial T}\right)_B < 0, \quad (17.33)$$

a result that we shall use later.

[Image: The magnetic susceptibility for a paramagnet follows Curie's law which states that chi ∝ 1/T.]
**Fig. 17.6** The magnetic susceptibility for a paramagnet follows Curie's law which states that $\chi \propto 1/T$.

## Example 17.4

Show that heat is emitted in an isothermal increase in $B$ (a process known as isothermal magnetization) but that temperature is reduced for an adiabatic reduction in $B$ (a process known as adiabatic demagnetization). This coupling between thermal and magnetic properties is known as the magnetocaloric effect.

Solution: Eqn 17.29 implies that changes in the Helmholtz function $F = U - TS$ follows

$$dF = -S dT - m dB, \quad (17.34)$$

which yields the Maxwell relation

$$\left(\frac{\partial S}{\partial B}\right)_T = \left(\frac{\partial m}{\partial T}\right)_B \approx \frac{V B}{\mu_0}\left(\frac{\partial \chi}{\partial T}\right)_B, \quad (17.35)$$

which relates the isothermal change of entropy with field at constant temperature to a differential of the susceptibility $\chi$.

The heat absorbed in an isothermal change of $B$ is

$$\Delta Q = T\left(\frac{\partial S}{\partial B}\right)_T \Delta B = \frac{T V B}{\mu_0}\left(\frac{\partial \chi}{\partial T}\right)_B \Delta B < 0, \quad (17.36)$$

and since it is negative it implies that heat is actually emitted. The change in temperature in an adiabatic change of $B$ is

$$\left(\frac{\partial T}{\partial B}\right)_S = -\left(\frac{\partial T}{\partial S}\right)_B \left(\frac{\partial S}{\partial B}\right)_T. \quad (17.37)$$

If we define $C_B = T\left(\frac{\partial S}{\partial T}\right)_B$, the heat capacity at constant $B$, then substitution of this and eqn 17.35 into eqn 17.37 yields

$$\left(\frac{\partial T}{\partial B}\right)_S = -\frac{T V B}{\mu_0 C_B}\left(\frac{\partial \chi}{\partial T}\right)_B. \quad (17.38)$$

Equation 17.33 implies that $\left(\frac{\partial T}{\partial B}\right)_S > 0$, and hence we can cool a material using an adiabatic demagnetization, i.e., by reducing the magnetic field on a sample while keeping it at constant entropy. This can yield temperatures as low as a few millikelvin for electronic systems and a few microkelvin for nuclear systems.

Let us now consider why adiabatic demagnetization results in the cooling of a material from a microscopic point of view. Consider a sample of a paramagnetic salt, which contains $N$ independent magnetic moments. Without a magnetic field applied, the magnetic moments will point in random directions (because we are assuming that they do not interact with each other) and the system will have no net magnetization. An applied field $B$ will, however, tend to line up the magnetic moments and produce a magnetization. Increasing temperature reduces the magnetization, and increasing magnetic field increases the magnetization. At very high temperature, the magnetic moments all point in random directions and the net magnetization is zero (see Fig. 17.7(a)). The thermal energy $k_B T$ is so large that all states are equally populated, irrespective of whether or not the state is energetically favourable. If the magnetic moments have angular momentum quantum number $J = \frac{1}{2}$ they can only point parallel or antiparallel to the magnetic field: hence there are $\Omega = 2^N$ ways of arranging up and down magnetic moments. Hence the magnetic contribution to the entropy, $S$, is

$$S = k_B \ln \Omega = N k_B \ln 2. \quad (17.39)$$

In the general case of $J > \frac{1}{2}$, $\Omega = (2J + 1)^N$ and the entropy is

$$S = N k_B \ln(2J + 1). \quad (17.40)$$

At lower temperature, the entropy of the paramagnetic salt must reduce as only the lowest energy levels are occupied, corresponding to the average alignment of the magnetic moments with the applied field increasing. At very low temperature, all the magnetic moments will align with the magnetic field to minimize their energy (see Fig. 17.7(b)). In this case there is only one way of arranging the system (with all spins aligned) so $\Omega = 1$ and $S = 0$.

[Image: (a) At high temperature, the spins in a paramagnet are in random directions because the thermal energy k_B T is much larger than the magnetic energy mB. (b) At low temperature, the spins become aligned with the field because the thermal energy k_B T is much smaller than the magnetic energy mB.]
**Fig. 17.7** (a) At high temperature, the spins in a paramagnet are in random directions because the thermal energy $k_B T$ is much larger than the magnetic energy $mB$. This state has high entropy. (b) At low temperature, the spins become aligned with the field because the thermal energy $k_B T$ is much smaller than the magnetic energy $mB$. This state has low entropy.

The procedure for magnetically cooling a sample is as follows. The paramagnet is first cooled to a low starting temperature using liquid helium. The magnetic cooling then proceeds via two steps (see also Fig. 17.8).

The first step is isothermal magnetization. The energy of a paramagnet is reduced by alignment of the moments parallel to a magnetic field. At a given temperature the alignment of the moments may therefore be enhanced by increasing the strength of an applied magnetic field. This is performed isothermally (see Fig. 17.8, step a → b) by having the sample thermally connected to a bath of liquid helium (the boiling point of helium at atmospheric pressure is 4.2 K), or perhaps with the liquid helium bath at reduced pressure so that the temperature can be less than 4.2 K. The temperature of the sample does not change and the helium bath absorbs the heat liberated by the sample as its energy and entropy decrease. The thermal connection is usually provided by low-pressure helium gas in the sample chamber, which conducts heat between the sample and the chamber walls, the chamber itself sitting inside the helium bath. (The gas is often called "exchange" gas because it allows the sample and the bath to exchange heat.)

The second step is to thermally isolate the sample from the helium bath (by pumping away the exchange gas). The magnetic field is then slowly reduced to zero, slowly so that the process is quasistatic and the entropy is constant. This step is called adiabatic demagnetization (see Fig. 17.8, step b → c) and it reduces the temperature of the system. During adiabatic demagnetization the entropy of the sample remains constant; the entropy of the magnetic moments increases (because the moments randomize as the field is turned down) and this is precisely balanced by the decrease in the entropy of the phonons (the lattice vibrations) as the sample cools. Entropy is thus exchanged between the phonons and the spins.

[Image: The entropy of a paramagnetic salt as a function of temperature for several different applied magnetic fields between zero and some maximum value, which we will call Bb. Magnetic cooling of a paramagnetic salt from temperature Ti to Tf is accomplished as indicated in two steps: first, isothermal magnetization from a to b by increasing the magnetic field from 0 to Bb at constant temperature Ti; second, adiabatic demagnetization from b to c. The S(T) curves have been calculated assuming J = 1/2. A term ∝ T^3 has been added to these curves to simulate the entropy of the lattice vibrations. The curve for B = 0 is actually for small, but non-zero, B to simulate the effect of a small residual field.]
**Fig. 17.8** The entropy of a paramagnetic salt as a function of temperature for several different applied magnetic fields between zero and some maximum value, which we will call $B_b$. Magnetic cooling of a paramagnetic salt from temperature $T_i$ to $T_f$ is accomplished as indicated in two steps: first, isothermal magnetization from a to b by increasing the magnetic field from 0 to $B_b$ at constant temperature $T_i$; second, adiabatic demagnetization from b to c. The $S(T)$ curves have been calculated assuming $J = \frac{1}{2}$. A term $\propto T^3$ has been added to these curves to simulate the entropy of the lattice vibrations. The curve for $B = 0$ is actually for small, but non-zero, $B$ to simulate the effect of a small residual field.

There is another way of looking at adiabatic demagnetization. Consider the energy levels of magnetic ions in a paramagnetic salt subjected to an applied magnetic field. The population of magnetic ions in each energy level is given by the Boltzmann distribution, as indicated schematically in Fig. 17.9(a). The rate at which the levels decrease in population as the energy increases is determined by the temperature $T$. When we perform an isothermal magnetization (increasing the applied magnetic field while keeping the temperature constant) we are increasing the spacing between the energy levels of the paramagnetic salt [see Fig. 17.9(b)], but the occupation of each level is determined by the same Boltzmann distribution because the temperature $T$ is constant. Thus the higher-energy levels become depopulated. This depopulation is the result of transitions between energy levels caused by interaction with the surroundings, which are keeping the system at constant temperature. In an adiabatic demagnetization, the external magnetic field is reduced to its original value, closing up the energy levels again. However, because the salt is now thermally isolated, no transitions between energy levels are possible and the populations of each level remain the same [see Fig. 17.9(c)]. Another way of saying this is that in an adiabatic process the entropy $S = -k_B \sum_i P_i \ln P_i$ (eqn 14.48) of the system is constant, and this expression only involves the probability $P_i$ of occupying the $i$th level, not the energy. Thus the temperature of the paramagnetic salt following the adiabatic demagnetization is lower because the occupancies now correspond to a Boltzmann distribution with a lower temperature.

[Image: Schematic diagram showing the energy levels in a magnetic system (a) initially, (b) following isothermal magnetization, and (c) following adiabatic demagnetization.]
**Fig. 17.9** Schematic diagram showing the energy levels in a magnetic system (a) initially, (b) following isothermal magnetization, and (c) following adiabatic demagnetization.

Does adiabatic demagnetization as a method of cooling have a limit? At first sight it looks as though the entropy would be $S = N k_B \ln(2J + 1)$ at $B = 0$ for all $T > 0$, and therefore with $B \neq 0$, $S \to 0$ only at absolute zero, implying that adiabatic demagnetization might be used to cool all the way to absolute zero. However, in real paramagnetic salts there is always some small residual internal field due to interactions between the moments which ensures that the entropy falls prematurely towards zero when the temperature is a little above absolute zero (see Fig. 17.8). The size of this field puts a limit on the lowest temperature to which the paramagnetic salt can be cooled. In certain paramagnetic salts, which have a very small residual internal field, temperatures of a few millikelvin can be achieved. The failure of Curie's law as we approach $T = 0$ is just one of the consequences of the third law of thermodynamics, which we shall treat in the following chapter.

## Chapter summary

- The first law for a gas is $dU = T dS - p dV$. An isothermal expansion results in $S$ increasing. An adiabatic compression results in $T$ increasing.
- The first law for an elastic rod is $dU = T dS + f dL$. An isothermal extension of a metal wire results in $S$ increasing but for rubber $S$ decreases. An adiabatic contraction of a metal wire results in $T$ increasing (but for rubber $T$ decreases).
- The first law for a liquid surface is $dU = T dS + \gamma dA$. An isothermal stretching results in $S$ increasing. An adiabatic contraction results in $T$ increasing.
- The first law is $dU = T dS - m dB$ for a magnetic system. An isothermal magnetization results in $S$ decreasing. An adiabatic demagnetization results in $T$ decreasing.

[Image: Entropy increases when (a) a gas is expanded isothermally, (b) a metallic rod is stretched isothermally. Entropy decreases when (c) rubber is stretched isothermally and (d) a paramagnet is magnetized isothermally.]
**Fig. 17.10** Entropy increases when (a) a gas is expanded isothermally, (b) a metallic rod is stretched isothermally. Entropy decreases when (c) rubber is stretched isothermally and (d) a paramagnet is magnetized isothermally.

===== Page 203 =====

# 18 The third law

18.1 Different statements of the third law  203
18.2 Consequences of the third law  205
Chapter summary  208
Exercises  208

In Chapter 13, we presented the second law of thermodynamics in various different forms. In Chapter 14, we related this to the concept of entropy and showed that the entropy of an isolated system always either stays the same or increases with time. But what value does the entropy of a system take, and how can you measure it?

One way of measuring the entropy of a system is to measure its heat capacity. For example, if measurements of $C_p$, the heat capacity at constant pressure, are made as a function of temperature, then using

$$C_p = T\left(\frac{\partial S}{\partial T}\right)_p, \quad (18.1)$$

we can obtain entropy $S$ by integration, so that

$$S = \int \frac{C_p}{T} dT. \quad (18.2)$$

This is all very well, but when you integrate, you have to worry about constants of integration. Writing eqn 18.2 as a definite integral, we have that the entropy $S(T)$, measured at temperature $T$, is

$$S(T) = S(T_0) + \int_{T_0}^T \frac{C_p}{T} dT, \quad (18.3)$$

where $T_0$ is some different temperature (see Fig. 18.1). Thus it seems that we are only able to learn about changes in entropy, for example as a system is warmed from $T_0$ to $T$, and we are not able to obtain an absolute measurement of entropy itself. The third law of thermodynamics, presented in this chapter, gives us additional information because it provides a value for the entropy at one particular temperature, namely absolute zero.

[Image: A graphical representation of eqn 18.3.]
**Fig. 18.1** A graphical representation of eqn 18.3.

## 18.1 Different statements of the third law

Walter H. Nernst (1864-1941) (Fig. 18.2) came up with the first statement of the third law of thermodynamics after examining data on chemical thermodynamics and doing experiments with electrochemical cells. The essential conclusion he came to concerned the change in enthalpy $\Delta H$ in a reaction (the heat of the reaction, positive if endothermic, negative if exothermic; see Section 16.5), and the change in Gibbs' function $\Delta G$ (that determines in which direction the reaction goes). Since $G = H - TS$, we expect that

$$\Delta G = \Delta H - T\Delta S, \quad (18.4)$$

so that as $T \to 0$, $\Delta G \to \Delta H$. Experimental data showed that this was true, but $\Delta G$ and $\Delta H$ not only came closer together on cooling, but they approached each other asymptotically. On the basis of the data, Nernst also postulated that $\Delta S \to 0$ as $T \to 0$. His statement of the third law, dating from 1906, can be written as

**Nernst's statement of the third law**
Near absolute zero, all reactions in a system in internal equilibrium take place with no change in entropy.

[Image: W. Nernst]
**Fig. 18.2** W. Nernst

Max Planck (1858-1947) (Fig. 18.3) added more meat to the bones of the statement by making a further hypothesis in 1911, namely that:

**Planck's statement of the third law**
The entropy of all systems in internal equilibrium is the same at absolute zero, and may be taken to be zero.

[Image: M. Planck]
**Fig. 18.3** M. Planck

Planck actually made his statement only about perfect crystals. However, it is believed to be true about any system, as long as it is in internal equilibrium (i.e., that all parts of a system are in equilibrium with each other). There are a number of systems, such as $^4$He and $^3$He, which are liquids even at very low temperature. Electrons in a metal can be treated as a gas all the way down to $T = 0$. The third law applies to all of these systems. However, note that the systems have to be in internal equilibrium for the third law to apply. An example of a system not in equilibrium is a glass, which has frozen-in disorder. For a solid, the lowest-energy phase is the perfect crystal, but the glass phase is higher in energy and is unstable. The glass phase will eventually relax back to the perfect crystalline phase but it may take many centuries to do this, and possibly a time greater than the age of the Universe.

Planck's choice of zero for the entropy was further motivated by the development of statistical mechanics, a subject we will tackle later in this book. It suffices to say here that the statistical definition of entropy, presented in eqn 14.36 ($S = k_B \ln \Omega$), implies that zero entropy is equivalent to $\Omega = 1$. Thus at absolute zero, when a system finds its ground state, the entropy being equal to zero implies that this ground state is non-degenerate.

At this point, we can raise a potential objection to the third law in Planck's form. Consider a perfect crystal composed of $N$ spinless atoms. We are told by the third law that its entropy is zero. However, let us further suppose that each atom has at its centre a nucleus with angular momentum quantum number $I$. If no magnetic field is applied to this system, then we appear to have a contradiction. The degeneracy of the nuclear spin is $2I + 1$ and if $I > 0$, this will not be equal to one. How can we reconcile this with zero entropy since the non-zero nuclear spin implies that the entropy $S$ of this system should be $S = N k_B \ln(2I + 1)$, to however low a temperature we cool it?

The answer to this apparent contradiction is as follows: in a real system in internal equilibrium, the individual components of the system must be able to exchange energy with each other, i.e., to interact with each other. Nuclear spins actually feel a tiny, but non-zero, magnetic field due to the dipolar fields produced each other, and this lifts the degeneracy. Another way of looking at this is to say that the interactions give rise to collective excitations of the nuclear spins. These collective excitations are nuclear spin waves, and the lowest-energy nuclear spin wave, corresponding to the longest-wavelength mode, will be non-degenerate. At sufficiently low temperatures (and this will be extremely low!) only that long-wavelength mode will be thermally occupied and the entropy of the nuclear spin system will be zero.

However, this example raises an important point. If we cool a crystal, we will extract energy from the lattice and its entropy will drop towards zero. However, the nuclear spins will still retain their entropy until cooled to a much lower temperature (reflecting the weaker interactions between nuclear spins compared with the bonds between atoms in the lattice). If we find a method of cooling the nuclei, there might still be some residual entropy associated with the individual nucleons. All these thermodynamic subsystems (the electrons, the nuclear spins, and the nucleons) are very weakly coupled to each other, but their entropies are additive. Francis Simon (1893-1956) (Fig. 18.4) in 1937 called these different subsystems "aspects" and formulated the third law as follows:

**Simon's statement of the third law**
The contribution to the entropy of a system by each aspect of the system which is in internal thermodynamic equilibrium tends to zero as $T \to 0$.

[Image: F. E. Simon]
**Fig. 18.4** F. E. Simon

Simon's statement is convenient because it allows us to focus on a particular aspect of interest, knowing that its entropy will tend to zero as $T$ approaches 0, while ignoring the aspects that we don't care about and which might not lose their entropy until much closer to $T = 0$.

## 18.2 Consequences of the third law

Having provided various statements of the third law, it is time to examine some of its consequences.

- **Heat capacities tend to zero as $T \to 0$**
This consequence is easy to prove. Any heat capacity $C$ given by

$$C = T\left(\frac{\partial S}{\partial T}\right) = \left(\frac{\partial S}{\partial \ln T}\right) \to 0, \quad (18.5)$$

because as $T \to 0$, $\ln T \to -\infty$ and $S \to 0$. Hence $C \to 0$.

Note that this result disagrees with the classical prediction of $C = R/2$ per mole per degree of freedom. (We note for future reference that this observation emphasizes the fact that the equipartition theorem, to be presented in Chapter 19, is a high temperature theory and fails at low temperature.)

- **Thermal expansion stops**
Since $S \to 0$ as $T \to 0$, we have for example that

$$\left(\frac{\partial S}{\partial p}\right)_T \to 0 \quad (18.6)$$

as $T \to 0$, but by a Maxwell relation, this implies that

$$\frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p \to 0 \quad (18.7)$$

and hence the isobaric expansivity $\beta_p \to 0$.

- **No gases remain ideal as $T \to 0$**
The ideal monatomic gas has served us well in this book as a simple model that allows us to obtain tractable results. One of these results is eqn 11.25, which states that for an ideal gas, $C_p - C_V = R$ per mole. However, as $T \to 0$, both $C_p$ and $C_V$ tend to zero, and this equation cannot be satisfied. Moreover, we expect that $C_V = 3R/2$ per mole, and as we have seen, this also does not work down to absolute zero. Yet another nail in the coffin of the ideal gas is the expression for its entropy given in eqn 16.79 ($S = C_V \ln T + R \ln V + \text{constant}$). As $T \to 0$, this equation yields $S \to -\infty$, which is as far from zero as you can get!

Thus we see that the third law forces us to abandon the ideal gas model when thinking about gases at low temperature. Of course, it is at low temperature that the weak interactions between gas molecules (blissfully neglected so far since we have modelled gas molecules as independent entities) become more important. More sophisticated models of gases will be considered in Chapter 26.

- **Curie's law breaks down**
Curie's law states that the susceptibility $\chi$ is proportional to $1/T$ and hence $\chi \to \infty$ as $T \to 0$. However, the third law implies that $(\partial S/\partial B)_T \to 0$ and hence

$$\left(\frac{\partial S}{\partial B}\right)_T = \left(\frac{\partial m}{\partial T}\right)_B = \frac{V B}{\mu_0}\left(\frac{\partial \chi}{\partial T}\right)_B \quad (18.8)$$

must tend to zero. Thus $\left(\frac{\partial \chi}{\partial T}\right) \to 0$, in disagreement with Curie's law. Why does it break down? You may begin to see a theme developing: it is interactions again! Curie's law is derived by considering magnetic moments to be entirely independent, in which case their properties can be determined by considering only the balance between the applied field (driving the moments to align) and temperature (driving the moments to randomize). The susceptibility measures their infinitesimal response to an infinitesimal applied field; this becomes infinite when the thermal fluctuations are removed at $T = 0$. However, if interactions between the magnetic moments are switched on, then an applied field will have much less of an effect because the magnetic moments will already be driven into some partially ordered state by each other.

There is a basic underlying message here: the microscopic parts of a system can behave independently at high temperature, where the thermal energy $k_B T$ is much larger than any interaction energy. At low temperature, these interactions become important and all notions of independence break down. To paraphrase (badly) the poet John Donne:

No man is an island, and especially not as $T \to 0$.

- **Unattainability of absolute zero**
The final point can almost be elevated to the status of another statement of the third law:

It is impossible to cool to $T = 0$ in a finite number of steps.

This is messy to prove rigorously, but we can justify the argument by reference to Fig. 18.5, which shows plots of $S$ against $T$ for different values of a parameter $X$ (which might be magnetic field, for example). Cooling is produced by isothermal increases in $X$ and adiabatic decreases in $X$. If the third law did not hold, it would be possible to proceed according to Fig. 18.5(a) and cool all the way to absolute zero. However, because of the third law, the situation is as in Fig. 18.5(b) and the number of steps needed to get to absolute zero becomes infinite.

[Image: (a) If S does not go to 0 as T → 0 it is possible to cool to absolute zero in a finite number of steps. (b) If the third law is obeyed, then it is impossible to cool to absolute zero in a finite number of steps.]
**Fig. 18.5** The entropy as a function of temperature for two different values of a parameter $X$. Cooling is produced by isothermal increases in $X$ (i.e., $X_1 \to X_2$) and adiabatic decreases in $X$ (i.e., $X_2 \to X_1$). (a) If $S$ does not go to 0 as $T \to 0$ it is possible to cool to absolute zero in a finite number of steps. (b) If the third law is obeyed, then it is impossible to cool to absolute zero in a finite number of steps.

Before concluding this chapter, we make one remark concerning Carnot engines. Consider a Carnot engine, operating between reservoirs with temperatures $T_\ell$ and $T_h$, having an efficiency $\eta = 1 - (T_\ell/T_h)$ (eqn 13.10). If $T_\ell \to 0$, the efficiency $\eta$ tends to 1. If you operated this Carnot engine, you would then get perfect conversion of heat into work, in violation of Kelvin's statement of the second law of thermodynamics. It seems at first sight that the unattainability of absolute zero (a version of the third law) is a simple consequence of the second law. However, there are difficulties in considering a Carnot engine operating between two reservoirs, one of which is at absolute zero. It is not clear how you can perform an isothermal process at absolute zero, because once a system is at absolute zero it is not possible to get it to change its thermodynamical state without warming it. Thus it is generally believed that the third law is indeed a separate postulate which is independent of the second law. The third law points to the fact that many of our "simple" thermodynamic models, such as the ideal gas equation and Curie's law of paramagnets, need substantial modification if they are to give correct predictions as $T \to 0$. It is therefore opportune to consider more sophisticated models based on the microscopic properties of real systems, and that brings us to statistical mechanics, the subject of the next part of this book.

## Chapter summary

- The third law of thermodynamics can be stated in various ways:
  - Nernst: Near absolute zero, all reactions in a system in internal equilibrium take place with no change in entropy.
  - Planck: The entropy of all systems in internal equilibrium is the same at absolute zero, and may be taken to be zero.
  - Simon: The contribution to the entropy of a system by each aspect of the system which is in internal thermodynamic equilibrium tends to zero as $T \to 0$.
  - Unattainability of $T = 0$: it is impossible to cool to $T = 0$ in a finite number of steps.
- The third law implies that heat capacities and thermal expansivities tend to zero as $T \to 0$.
- Interactions between the constituents of a system become important as $T \to 0$, and this leads to the breakdown of the concept of an ideal gas and also the breakdown of Curie's law.

## Exercises

(18.1) Summarize the main consequences of the third law of thermodynamics. Explain how it casts a shadow of doubt on some of the conclusions from various thermodynamic models.

(18.2) Recall from eqn 16.26 that

$$H = G - T\left(\frac{\partial G}{\partial T}\right)_p. \quad (18.9)$$

Hence show that

$$\Delta G - \Delta H = T\left(\frac{\partial \Delta G}{\partial T}\right)_p, \quad (18.10)$$

and explain what happens to these terms as the temperature $T \to 0$.

===== Page 209 =====

# Part VII

## Statistical mechanics

In this part we introduce the subject of statistical mechanics. This is a thermodynamic theory in which account is taken of the microscopic properties of individual atoms or molecules analysed in a statistical fashion. Statistical mechanics allows macroscopic properties to be calculated from the statistical distribution of the microscopic behaviour of individual atoms and molecules. This part is structured as follows:

- In Chapter 19, we present the equipartition theorem, a principle that states that the internal energy of a classical system composed of a large number of particles in thermal equilibrium will distribute itself evenly among each of the quadratic degrees of freedom accessible to the particles of the system.
- In Chapter 20 we introduce the partition function, which encodes all the information concerning the states of a system and their thermal occupation. Having the partition function allows you to calculate all the thermodynamic properties of the system.
- In Chapter 21 we calculate the partition function for an ideal gas and use this to define the quantum concentration. We show how the indistinguishability of molecules affects the statistical properties and has thermodynamic consequences.
- In Chapter 22 we extend our results on partition functions to systems in which the number of particles can vary. This allows us to define the chemical potential and introduce the grand partition function.
- In Chapter 23, we consider the statistical mechanics of light, which is quantized as photons, introducing black-body radiation, radiation pressure, and the cosmic microwave background.
- In Chapter 24, we discuss the analogous behaviour of lattice vibrations, quantized as phonons, and introduce the Einstein model and Debye model of the thermal properties of solids.

===== Page 210 =====

# 19 Equipartition of energy

19.1 Equipartition theorem  210
19.2 Applications  213
19.3 Assumptions made  215
19.4 Brownian motion  217
Chapter summary  218
Exercises  218

Before introducing the partition function in Chapter 20, which will allow us to calculate many different properties of thermodynamic systems on the basis of their microscopic energy levels (which can be deduced using quantum mechanics), we devote this chapter to the equipartition theorem. This theorem provides a simple, classical theory of thermal systems. It gives remarkably good answers, but only at high temperature, where the details of quantized energy levels can be safely ignored. We will motivate and prove this theorem in the following section, and then apply it to various physical situations in Section 19.2, demonstrating that it provides a rapid and straightforward method for deriving heat capacities. Finally, in Section 19.3, we will critically examine the assumptions that we have made in the derivation of the equipartition theorem.

## 19.1 Equipartition theorem

Very often in physics one is faced with an energy dependence that is quadratic in some variable. An example would be the kinetic energy $E_{\mathrm{KE}}$ of a particle with mass $m$ and velocity $v$, which is given by

$$E_{\mathrm{KE}} = \frac{1}{2}mv^2. \quad (19.1)$$

Another example would be the potential energy $E_{\mathrm{PE}}$ of a mass suspended at one end of a spring with spring constant $k$ and displaced by a distance $x$ from its equilibrium point (see Fig. 19.1). This is given by

$$E_{\mathrm{PE}} = \frac{1}{2}kx^2. \quad (19.2)$$

[Image: A mass m suspended on a spring with spring constant k. The mass is displaced by a distance x from its equilibrium or "rest" position.]
**Fig. 19.1** A mass $m$ suspended on a spring with spring constant $k$. The mass is displaced by a distance $x$ from its equilibrium or "rest" position.

In fact, the total energy $E$ of a moving mass on the end of a spring is given by the sum of these two terms, so that

$$E = E_{\mathrm{KE}} + E_{\mathrm{PE}} = \frac{1}{2}mv^2 + \frac{1}{2}kx^2, \quad (19.3)$$

and, as the mass undergoes simple harmonic motion, energy is exchanged between $E_{\mathrm{KE}}$ and $E_{\mathrm{PE}}$, while the total energy remains fixed.

Let us suppose that a system whose energy has a quadratic dependence on some variable is allowed to interact with a heat bath. It is then able to borrow energy occasionally from its environment, or even give it back into the environment. What mean thermal energy would it have? The thermal energy would be stored as kinetic or potential energy, so if a mass on a spring is allowed to come into thermal equilibrium with its environment, one could in principle take a very big magnifying glass and see the mass on a spring jiggling around all by itself owing to such thermal vibrations. How big would such vibrations be? The calculation is quite straightforward.

Let the energy $E$ of a particular system be given by

$$E = \alpha x^2, \quad (19.4)$$

where $\alpha$ is some positive constant and $x$ is some variable (see Fig. 19.2). Let us also assume that $x$ could in principle take any value with equal probability. The probability $P(x)$ of the system having a particular energy $\alpha x^2$ is proportional to the Boltzmann factor $e^{-\beta\alpha x^2}$ (see eqn 4.13), so that after normalizing, we have

$$P(x) = \frac{e^{-\beta\alpha x^2}}{\int_{-\infty}^{\infty} e^{-\beta\alpha x^2} dx}, \quad (19.5)$$

and the mean energy is

$$\langle E \rangle = \int_{-\infty}^{\infty} E P(x) dx = \frac{\int_{-\infty}^{\infty} \alpha x^2 e^{-\beta\alpha x^2} dx}{\int_{-\infty}^{\infty} e^{-\beta\alpha x^2} dx} = \frac{1}{2\beta} = \frac{1}{2}k_B T. \quad (19.6)$$

[Image: The energy E of a system is E = αx².]
**Fig. 19.2** The energy $E$ of a system is $E = \alpha x^2$.

This is a really remarkable result. It is independent of the constant $\alpha$ and gives a mean energy that is proportional to temperature. The theorem can be extended straightforwardly to the energy being the sum of $n$ quadratic terms, as shown in the following example.

## Example 19.1

Assume that the energy $E$ of a system can be given by the sum of $n$ independent quadratic terms, so that

$$E = \sum_{i=1}^n \alpha_i x_i^2, \quad (19.7)$$

where $\alpha_i$ are constants and $x_i$ are some variables. Assume also that each $x_i$ could in principle take any value with equal probability. Calculate the mean energy.

Solution:

The mean energy $\langle E \rangle$ is given by

$$\langle E \rangle = \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} E P(x_1, x_2, \ldots x_n) dx_1 dx_2 \cdots dx_n. \quad (19.8)$$

This now looks quite complicated when we substitute in the probability as follows

$$\langle E \rangle = \frac{\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \left(\sum_{i=1}^n \alpha_i x_i^2\right) \exp\left(-\beta \sum_{j=1}^n \alpha_j x_j^2\right) dx_1 dx_2 \cdots dx_n}{\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \exp\left(-\beta \sum_{j=1}^n \alpha_j x_j^2\right) dx_1 dx_2 \cdots dx_n}, \quad (19.9)$$

where $i$ and $j$ have been used to distinguish different sums. This expression can be simplified by recognizing that it is the sum of $n$ similar terms (write out the sums to convince yourself):

$$\langle E \rangle = \sum_{i=1}^n \frac{\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \alpha_i x_i^2 \exp\left(-\beta \sum_{j=1}^n \alpha_j x_j^2\right) dx_1 dx_2 \cdots dx_n}{\int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} \exp\left(-\beta \sum_{j=1}^n \alpha_j x_j^2\right) dx_1 dx_2 \cdots dx_n}, \quad (19.10)$$

and then all but one integral cancels between the numerator and denominator of each term, so that

$$\langle E \rangle = \sum_{i=1}^n \frac{\int_{-\infty}^{\infty} \alpha_i x_i^2 \exp\left(-\beta \alpha_i x_i^2\right) dx_i}{\int_{-\infty}^{\infty} \exp\left(-\beta \alpha_i x_i^2\right) dx_i}. \quad (19.11)$$

Now each term in this sum is the same as the one treated above in eqn 19.6. Hence

$$\langle E \rangle = \sum_{i=1}^n \alpha_i \langle x_i^2 \rangle = \sum_{i=1}^n \frac{1}{2} k_B T = \frac{n}{2} k_B T. \quad (19.12)$$

Each quadratic energy dependence of the system is called a mode of the system (or sometimes a degree of freedom of the system). The spring, our example at the beginning of this chapter, has two such modes. The result of the example above shows that each mode of the system contributes an amount of energy equal to $\frac{1}{2} k_B T$ to the total mean energy of the system. This result is the basis of the equipartition theorem, which we state as follows:

**Equipartition theorem**
If the energy of a classical system is the sum of $n$ quadratic modes, and that system is in contact with a heat reservoir at temperature $T$, the mean energy of the system is given by $n \times \frac{1}{2} k_B T$.

The equipartition theorem expresses the fact that energy is "equally partitioned" between all the separate modes of the system, each mode having a mean energy of precisely $\frac{1}{2} k_B T$.

## Example 19.2

We return to our example of a mass on a spring, whose energy is given by the sum of two quadratic energy modes (see eqn 19.3). The equipartition theorem then implies that the mean energy is given by

$$2 \times \frac{1}{2} k_B T = k_B T. \quad (19.13)$$

How big is this energy? At room temperature, $k_B T \approx 4 \times 10^{-21} \text{ J} \approx 0.025 \text{ eV}$, which is a tiny energy. This energy isn't going to set a 10 kg mass on a stiff spring vibrating very much! However, the extraordinary thing about the equipartition theorem is that the result holds independently of the size of the system, so that $k_B T = 0.025$ eV is also the mean energy of an atom on the end of a chemical bond (which can be modelled as a spring) at room temperature. For an atom, $k_B T = 0.025$ eV goes a very long way and this explains why atoms in molecules jiggle around a lot at room temperature. We will explore this in more detail below.

## 19.2 Applications

We now consider four applications of the equipartition theorem.

### 19.2.1 Translational motion in a monatomic gas

The energy of each atom in a monatomic gas is given by

$$E = \frac{1}{2} mv_x^2 + \frac{1}{2} mv_y^2 + \frac{1}{2} mv_z^2, \quad (19.14)$$

where $v = (v_x, v_y, v_z)$ is the velocity of the atom (see Fig. 19.3). This energy is the sum of three independent quadratic modes, and thus the equipartition theorem gives the mean energy as

$$\langle E \rangle = 3 \times \frac{1}{2} k_B T = \frac{3}{2} k_B T. \quad (19.15)$$

This is in agreement with our earlier derivation of the mean kinetic energy of a gas (see eqn 5.17).

[Image: The velocity of a molecule in a gas.]
**Fig. 19.3** The velocity of a molecule in a gas.

### 19.2.2 Rotational motion in a diatomic gas

In a diatomic gas, there is an additional possible energy source to consider, namely that of rotational kinetic energy. This adds two terms to the energy

$$\frac{L_1^2}{2I_1} + \frac{L_2^2}{2I_2}, \quad (19.16)$$

where $L_1$ and $L_2$ are the angular momenta along the two principal directions shown in Fig. 19.4 and $I_1$ and $I_2$ are the corresponding moments of inertia. We do not need to worry about the direction along the diatomic molecule's bond, the axis labelled "3" in Fig. 19.4. (This is because the moment of inertia in this direction is very small (so that the corresponding rotational kinetic energy is very large), so rotational modes in this direction cannot be excited at ordinary temperature; such rotational modes are connected with the individual molecular electronic levels and we will therefore ignore them.)

The total energy is thus the sum of five terms, three due to translational kinetic energy and two due to rotational kinetic energy

$$E = \frac{1}{2} mv_x^2 + \frac{1}{2} mv_y^2 + \frac{1}{2} mv_z^2 + \frac{L_1^2}{2I_1} + \frac{L_2^2}{2I_2}, \quad (19.17)$$

and all of these energy modes are independent of one another. Using the equipartition theorem, we can immediately write down the mean energy as

$$\langle E \rangle = 5 \times \frac{1}{2} k_B T = \frac{5}{2} k_B T. \quad (19.18)$$

[Image: Rotational motion in a diatomic gas.]
**Fig. 19.4** Rotational motion in a diatomic gas.

### 19.2.3 Vibrational motion in a diatomic gas

If we also include the vibrational motion of the bond linking the two atoms in our diatomic molecule, there are two additional modes to include. The intramolecular bond can be modelled as a spring (see Fig. 19.5), so that the two extra energy terms are the kinetic energy due to relative motion of the two atoms and the potential energy in the bond (let us suppose it has spring constant $k$). Writing the positions of the two atoms as $\mathbf{r}_1$ and $\mathbf{r}_2$ with respect to some fixed origin, the energy of the atom can be written

$$E = \frac{1}{2} mv_x^2 + \frac{1}{2} mv_y^2 + \frac{1}{2} mv_z^2 + \frac{L_1^2}{2I_1} + \frac{L_2^2}{2I_2} + \frac{1}{2} \mu(\dot{\mathbf{r}}_1 - \dot{\mathbf{r}}_2)^2 + \frac{1}{2} k(\mathbf{r}_1 - \mathbf{r}_2)^2, \quad (19.19)$$

where $\mu = m_1 m_2/(m_1 + m_2)$ is the reduced mass of the system. The equipartition theorem just cares about the number of modes in the system, so the mean energy is simply

$$\langle E \rangle = 7 \times \frac{1}{2} k_B T = \frac{7}{2} k_B T. \quad (19.20)$$

[Image: A diatomic molecule can be modelled as two masses connected by a spring.]
**Fig. 19.5** A diatomic molecule can be modelled as two masses connected by a spring.

The heat capacity of the systems described above can be obtained by differentiating the energy with respect to temperature. The mean energy is given by

$$\langle E \rangle = \frac{f}{2} k_B T, \quad (19.21)$$

where $f$ is the number of degrees of freedom. This equation implies that

$$C_V \text{ per mole} = \frac{f}{2} R, \quad (19.22)$$

and using eqn 11.27 we have

$$C_p \text{ per mole} = \left(\frac{f}{2} + 1\right) R, \quad (19.23)$$

from which we may derive

$$\gamma = \frac{C_p}{C_V} = \frac{\left(\frac{f}{2} + 1\right)R}{\frac{f}{2}R} = 1 + \frac{2}{f}. \quad (19.24)$$

We can summarize our results for the heat capacity of gases, per atom or molecule, as follows:

| Gas | Modes | $f$ | $\langle E \rangle$ | $\gamma$ |
| :--- | :--- | :--- | :--- | :--- |
| Monatomic | Translational only | 3 | $\frac{3}{2} k_B$ | $\frac{5}{3}$ |
| Diatomic | Translational and rotational | 5 | $\frac{5}{2} k_B$ | $\frac{7}{5}$ |
| Diatomic | Translational, rotational, and vibrational | 7 | $\frac{7}{2} k_B$ | $\frac{9}{7}$ |

### 19.2.4 The heat capacity of a solid

In a solid, the atoms are held rigidly in the lattice and there is no possibility of translational motion. However, the atoms can vibrate about their mean positions. Consider a cubic solid (Fig. 19.6) in which each atom is connected by springs (chemical bonds) to six neighbours (one above, one below, one in front, one behind, one to the right, one to the left). Since each spring joins two atoms, then if there are $N$ atoms in the solid, there are $3N$ springs (neglecting the surface of the solid, a reasonable approximation if $N$ is large). Each spring has two quadratic modes of energy (one kinetic, one potential) and hence a mean thermal energy equal to $2 \times \frac{1}{2} k_B T = k_B T$. Hence the mean energy of the solid is

$$\langle E \rangle = 3N k_B T, \quad (19.25)$$

and the heat capacity is $\partial \langle E \rangle / \partial T = 3N k_B$. Because $R = N_A k_B$, the molar heat capacity of a solid is then expected to be $3N_A k_B = 3R$. This result agrees quite well with experiment and is known as the Dulong–Petit rule (see Section 24.1).

[Image: In a cubic solid, each atom is connected by chemical bonds, modelled as springs, to six nearest neighbours, two along each of the three Cartesian axes. Each spring is shared between two atoms.]
**Fig. 19.6** In a cubic solid, each atom is connected by chemical bonds, modelled as springs, to six nearest neighbours, two along each of the three Cartesian axes. Each spring is shared between two atoms.

## 19.3 Assumptions made

The equipartition theorem seems to be an extremely powerful tool for evaluating thermal energies of systems. However, it does have some limitations, and to discover what these are, it is worth thinking about the assumptions we have made in deriving it.

- We have assumed that the parameter for which we have taken the energy to be quadratic can take any possible value. In the derivation, the variables $x_i$ could be integrated continuously from $-\infty$ to $\infty$. However, quantum mechanics insists that certain quantities can only take particular "quantized" values. For example, the problem of a mass on a spring is shown by quantum mechanics to have an energy spectrum that is quantized into levels given by $(n + \frac{1}{2})\hbar\omega$. When the thermal energy $k_B T$ is of the same order, or lower than, $\hbar\omega$, the approximation made by ignoring the quantized nature of this energy spectrum is going to be a very bad one. However, when $k_B T \gg \hbar\omega$, the quantized nature of the energy spectrum is going to be largely irrelevant, in much the same way that you don't notice that the different shades of grey in a newspaper photograph are actually made up of lots of little dots if you don't look closely. Thus we come to an important conclusion:

The equipartition theorem is generally valid only at high temperature, so that the thermal energy is larger than the energy gap between quantized energy levels. Results based on the equipartition theorem should emerge as the high-temperature limit of more detailed theories.

- We have assumed throughout that modes are quadratic. Is that always valid? To give a concrete example, imagine that an atom moves with coordinate $x$ in a potential well given by $V(x)$, which is a function that might be more complicated than a quadratic (see, for example, Fig. 19.7). At absolute zero, the atom finds a potential minimum at say $x_0$ (so that, for the usual reasons, $\partial V/\partial x = 0$ and $\partial^2 V/\partial x^2 > 0$ at $x = x_0$). At temperature $T > 0$, the atom can explore regions away from $x_0$ by borrowing energy of order $k_B T$ from its environment. Near $x_0$, the potential $V(x)$ can be expanded using a Taylor expansion as

$$V(x) = V(x_0) + \left(\frac{\partial V}{\partial x}\right)_{x_0} (x - x_0) + \frac{1}{2} \left(\frac{\partial^2 V}{\partial x^2}\right)_{x_0} (x - x_0)^2 + \cdots,$$

so that using $(\partial V/\partial x)_{x_0} = 0$, we find that the potential energy is

$$V(x) = \text{constant} + \frac{1}{2} \left(\frac{\partial^2 V}{\partial x^2}\right)_{x_0} (x - x_0)^2 + \cdots,$$

which is a quadratic again. This demonstrates that the bottom of almost all potential wells tends to be approximately quadratic (this is known as the harmonic approximation).

[Image: A graph of V(x) versus x, showing a potential well that is deeper and more complex than a simple quadratic, with a minimum at x=x0.]
**Fig. 19.7** $V(x)$ is a function that is more complicated than a quadratic but has a minimum at $x = x_0$.

If the temperature gets too high, the system will be able to access positions far away from $x_0$ and the approximation of ignoring the higher order (cubic, quartic, etc.) terms (known as the anharmonic terms) in the Taylor expansion may become important.

## 19.4 Brownian motion

We close this chapter with one example in which the effect of the equipartition of energy is encountered.

## Example 19.3

## Brownian motion

In 1827, Robert Brown used a microscope to observe pollen grains jiggling about in water. He was not the first to make such an observation (any small particles suspended in a fluid will do the same, and are very apparent when looking down a microscope), but this effect has come to be known as Brownian motion.

The motion is very irregular, consisting of translations and rotations, with grains moving independently, even when moving close to each other. The motion is found to be more active the smaller the particles. The motion is also found to be more active the less viscous the fluid. Brown was able to discount a "vital" explanation of the effect, i.e., that the pollen grains were somehow "alive", but he was not able to give a correct explanation. Something resembling a modern theory of Brownian motion was proposed by Christian Wiener in 1863, though the major breakthrough was made by Einstein in 1905.

We will postpone a full discussion of Brownian motion until Chapter 33, but using the equipartition theorem, the origin of the effect can be understood in outline. Each pollen grain (of mass $m$) is free to move translationally and so has mean kinetic energy $\frac{1}{2} m\langle v^2\rangle = \frac{3}{2} k_B T$. This energy is very small, as we have seen, but leads to a measurable amplitude of vibration for a small pollen grain. The amplitude of vibration is greater for smaller pollen grains because a mean kinetic energy of $\frac{3}{2} k_B T$ gives more mean square velocity $\langle v^2\rangle$ to less massive grains. The thermally excited vibrations are resisted by viscous damping, so the motion is expected to be more pronounced in less viscous fluids.

## Chapter summary

- The equipartition theorem states that if the energy of a system is the sum of $n$ quadratic modes, and that the system is in contact with a heat reservoir of temperature $T$, the mean energy of the system is given by $n \times \frac{1}{2} k_B T$.
- The equipartition theorem is a high-temperature result and gives incorrect predictions at low temperature, where the discrete nature of the energy spectrum cannot be ignored.

## Exercises

(19.1) What is the mean kinetic energy in eV at room temperature of a gaseous (a) He atom, (b) Xe atom, (c) Ar atom, and (d) Kr atom. [Hint: do you have to make four separate calculations?]

(19.2) Comment on the following values of molar heat capacity in J K⁻¹ mol⁻¹, all measured at constant pressure at 298 K.

| Al | Ar | Au | Cu | He | H₂ | Fe | Pb | Ne | N₂ | O₂ | Ag | Xe | Zn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 24.35 | 20.79 | 25.42 | 24.44 | 20.79 | 28.82 | 25.10 | 26.44 | 20.79 | 29.13 | 29.36 | 25.53 | 20.79 | 25.40 |

[Hint: express them in terms of $R$; which of the substances is a solid and which is gaseous?]

(19.3) A particle at position $\mathbf{r}$ is in a potential well $V(\mathbf{r})$ given by

$$V(\mathbf{r}) = \frac{A}{r^n} - \frac{B}{r},$$

where $A$ and $B$ are positive constants and $n > 2$. Show that the bottom of the well is approximately quadratic in $\mathbf{r}$. Hence find the particle's mean thermal energy at temperature $T$ above the bottom of the well assuming the validity of the equipartition theorem in this situation.

(19.4) In Example 19.1, show that

$$\langle x_i^2 \rangle = \frac{k_B T}{2\alpha_i}.$$

(19.5) If the energy $E$ of a system is not quadratic, but behaves like $E = \alpha |x|$ where $\alpha > 0$, show that the average energy is $\langle E \rangle = k_B T$.

(19.6) If the energy $E$ of a system behaves like $E = \alpha |x|^n$, where $n = 1, 2, 3 \ldots$ and $\alpha > 0$, show that the average energy is $\langle E \rangle = \xi k_B T$, where $\xi$ is a numerical constant.

(19.7) A simple pendulum with length $\ell$ makes an angle $\theta$ with the vertical, where $\theta \ll 1$. Show that it oscillates with a period given by $2\pi\sqrt{\ell/g}$. The pendulum is now placed at rest and allowed to come into equilibrium with its surroundings at temperature $T$. Derive an expression for $\langle \theta^2 \rangle$.

===== Page 219 =====

# 20 The partition function

20.1 Writing down the partition function  220
20.2 Obtaining the functions of state  221
20.3 The big idea  228
20.4 Combining partition functions  228
Chapter summary  231
Exercises  232

The probability that a system is in some particular state $\alpha$ is proportional to the Boltzmann factor $e^{-\beta E_\alpha}$. We define the partition function $Z$ by a sum over all the states of the Boltzmann factors, so that

$$Z = \sum_{\alpha} e^{-\beta E_\alpha} \tag{20.1}$$

where the sum is over all states of the system (each one labelled by $\alpha$). The partition function $Z$ contains all the information about the energies of the states of the system, and the fantastic thing about the partition function is that all thermodynamical quantities can be obtained from it. It behaves like a zipped-up and compressed version of all the properties of the system; once you have $Z$, you only have to know how to uncompress and unzip it to get functions of state like energy, entropy, Helmholtz function, or heat capacity to simply drop out. We can therefore reduce problem solving in statistical mechanics to two steps:

**Steps to solving statistical mechanics problems**

(1) Write down the partition function $Z$. (see Section 20.1)
(2) Go through some standard procedures to obtain the functions of state you want from $Z$. (see Section 20.2)

We will outline these two steps in the sections that follow. Before we do that, let us pause to notice an important feature about the partition function.

- The zero of energy is always somewhat arbitrary: one can always choose to measure energy with respect to a different zero, since it is only energy differences that are important. Hence the partition function is defined up to an arbitrary multiplicative constant. This seems somewhat strange, but it turns out that many physical quantities are related to the logarithm of the partition function and therefore these quantities are defined up to an additive constant (which might reflect, for example, the rest mass of particles). Other physical quantities, however, are determined by a differential of the logarithm of the partition function and therefore these quantities can be determined precisely.

## 20.1 Writing down the partition function

The partition function contains all the information we need to work out the thermodynamical properties of a system. In this section, we show how you can write down the partition function in the first place.

This procedure is not complicated! Writing down the partition function is nothing more than evaluating eqn 20.1 for different situations. We demonstrate this for a couple of commonly encountered and important examples.

## Example 20.1

**(a) The two-level system (see Fig. 20.1(a))**

Let the energy of a system be either $-\Delta/2$ or $\Delta/2$. Then

$$Z = \sum_{\alpha} e^{-\beta E_\alpha} = e^{\beta\Delta/2} + e^{-\beta\Delta/2} = 2 \cosh\left(\frac{\beta\Delta}{2}\right), \tag{20.2}$$

where the final result follows from the definition of $\cosh x \equiv \frac{1}{2}(e^x + e^{-x})$ (see Appendix B).

[Image: Two diagrams (a) and (b). (a) shows two horizontal lines representing energy levels, one at -Delta/2 and one at +Delta/2. (b) shows a ladder of evenly spaced energy levels, labelled n=0, 1, 2, ..., each with energy (n+1/2)hbar omega.]
**Fig. 20.1** Energy levels of (a) a two-level system and (b) a simple harmonic oscillator.

**(b) The simple harmonic oscillator (see Fig. 20.1(b))**

The energy of the system is $(n + \frac{1}{2})\hbar\omega$ where $n = 0, 1, 2, \ldots$, and hence

$$Z = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{n=0}^{\infty} e^{-\beta(n + \frac{1}{2})\hbar\omega} = e^{-\beta\frac{1}{2}\hbar\omega} \sum_{n=0}^{\infty} e^{-n\beta\hbar\omega} = \frac{e^{-\frac{1}{2}\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}, \tag{20.3}$$

where the sum is evaluated using the standard result for the sum of an infinite geometric progression, see Appendix B. (An alternative form of this result is found by multiplying top and bottom by $e^{\beta\frac{1}{2}\hbar\omega}$ to obtain the result $Z = \frac{1}{2\sinh(\beta\hbar\omega/2)}$.)

Two further, slightly more complicated, examples are the set of $N$ equally spaced energy levels and the energy levels appropriate for the rotational states of a diatomic molecule.

## Example 20.2

**(c) The N-level system (see Fig. 20.2(c))**

Let the energy levels of a system be $0, \hbar\omega, 2\hbar\omega, \ldots, (N-1)\hbar\omega$. Then

$$Z = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{j=0}^{N-1} e^{-j\beta\hbar\omega} = \frac{1 - e^{-N\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}, \tag{20.4}$$

where the sum is evaluated using the standard result for the sum of a finite geometric progression, see Appendix B.

**(d) Rotational energy levels (see Fig. 20.2(d))**

The rotational kinetic energy of a molecule with moment of inertia $I$ is given by $\hat{J}^2/2I$, where $\hat{J}$ is the total angular momentum operator. The eigenvalues of $\hat{J}^2$ are given by $\hbar^2 J(J+1)$, where the angular momentum quantum number, $J$, takes the values $J = 0, 1, 2, \ldots$. The energy levels of this system are given by

$$E_J = \frac{\hbar^2}{2I} J(J+1), \tag{20.5}$$

and have degeneracy $2J + 1$. Hence the partition function is

$$Z = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\hbar^2 J(J+1)/2I}, \tag{20.6}$$

where the factor $(2J+1)$ takes into account the degeneracy of each level.

[Image: Two diagrams (c) and (d). (c) shows N discrete energy levels, equally spaced from 0 to (N-1)hbar omega. (d) shows rotational energy levels that get closer together as J increases, with degeneracies indicated.]
**Fig. 20.2** Energy levels of (c) an N-level system and (d) a rotational system.

## 20.2 Obtaining the functions of state

[Image: A diagram of a sausage machine. An input labelled "Z" goes in one side, and various outputs like U, F, S, p, H, G, C_V come out the other.]
**Fig. 20.3** Given $Z$, it takes only a turn of the handle on our "sausage machine" to produce other functions of state.

Once $Z$ has been written down, we can place it in our mathematical sausage machine (see Fig. 20.3), which processes it and spits out fully-fledged thermodynamical functions of state. We now outline the derivations of the components of our sausage machine so that you can derive all these functions of state for any given $Z$.

- **Internal energy $U$**
The internal energy $U$ is given by

$$U = \frac{\sum_i E_i e^{-\beta E_i}}{\sum_i e^{-\beta E_i}}. \tag{20.7}$$

Now the denominator of this expression is the partition function $Z = \sum_i e^{-\beta E_i}$, but the numerator is simply

$$-\frac{dZ}{d\beta} = \sum_i E_i e^{-\beta E_i}. \tag{20.8}$$

Thus $U = -(1/Z)(dZ/d\beta)$, or more simply,

$$U = -\frac{d\ln Z}{d\beta}. \tag{20.9}$$

This is a useful form since $Z$ is normally expressed in terms of $\beta$. If you prefer things in terms of temperature $T$, then using $\beta = 1/k_B T$ (and hence $d/d\beta = -k_B T^2(d/dT)$) one obtains

$$U = k_B T^2 \frac{d\ln Z}{dT}. \tag{20.10}$$

- **Entropy $S$**
Since the probability $P_j$ is given by a Boltzmann factor divided by the partition function (so that the sum of the probabilities is one, as can be shown using eqn 20.1), we have $P_j = e^{-\beta E_j}/Z$ and hence

$$\ln P_j = -\beta E_j - \ln Z. \tag{20.11}$$

Equation 14.48 therefore gives us an expression for the entropy as follows:

$$S = -k_B \sum_i P_i \ln P_i = k_B \sum_i P_i (\beta E_i + \ln Z) = k_B (\beta U + \ln Z), \tag{20.12}$$

where we have used $U = \sum_i P_i E_i$ and $\sum_i P_i = 1$. Substituting the definition of $\beta$, namely $\beta = 1/k_B T$, into this equation gives

$$S = \frac{U}{T} + k_B \ln Z. \tag{20.13}$$

- **Helmholtz function $F$**
The Helmholtz function is defined via $F = U - TS$, so using eqn 20.13 we have that

$$F = -k_B T \ln Z. \tag{20.14}$$

This can also be cast into the memorable form

$$Z = e^{-\beta F}. \tag{20.15}$$

Once we have an expression for the Helmholtz function, a lot of things come out in the wash. For example, using eqn 16.19 we have that

$$S = -\left(\frac{\partial F}{\partial T}\right)_V = k_B \ln Z + k_B T \left(\frac{\partial \ln Z}{\partial T}\right)_V, \tag{20.16}$$

which, using eqn 20.10, is equivalent to eqn 20.13 above. This expression then leads to the heat capacity, via (recall eqn 16.65)

$$C_V = T \left(\frac{\partial S}{\partial T}\right)_V, \tag{20.17}$$

or one can use

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V. \tag{20.18}$$

Either way,

$$C_V = k_B T \left[ 2 \left(\frac{\partial \ln Z}{\partial T}\right)_V + T \left(\frac{\partial^2 \ln Z}{\partial T^2}\right)_V \right]. \tag{20.19}$$

- **Pressure $p$**
The pressure can be obtained from $F$ using eqn 16.20, so that

$$p = -\left(\frac{\partial F}{\partial V}\right)_T = k_B T \left(\frac{\partial \ln Z}{\partial V}\right)_T. \tag{20.20}$$

Having got the pressure we can then write down the enthalpy and the Gibbs function.

- **Enthalpy $H$**
$$H = U + pV = k_B T \left[ T \left(\frac{\partial \ln Z}{\partial T}\right)_V + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]. \tag{20.21}$$

- **Gibbs function $G$**
$$G = F + pV = k_B T \left[ -\ln Z + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]. \tag{20.22}$$

These relations are summarized in Table 20.1. In practice, it is easiest to remember only the relations for $U$ and $F$, since the others can be derived (using the relations shown in the left column of the table).

**Table 20.1** Thermodynamic quantities derived from the partition function $Z$.

| Function of state | Statistical mechanical expression |
| :--- | :--- |
| $U$ | $-\frac{d\ln Z}{d\beta}$ |
| $F$ | $-k_B T \ln Z$ |
| $S$ | $= -\left(\frac{\partial F}{\partial T}\right)_V = \frac{U-F}{T} = k_B \ln Z + k_B T \left(\frac{\partial \ln Z}{\partial T}\right)_V$ |
| $p$ | $= -\left(\frac{\partial F}{\partial V}\right)_T = k_B T \left(\frac{\partial \ln Z}{\partial V}\right)_T$ |
| $H$ | $= U + pV = k_B T \left[ T \left(\frac{\partial \ln Z}{\partial T}\right)_V + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]$ |
| $G$ | $= F + pV = H - TS = k_B T \left[ -\ln Z + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]$ |
| $C_V$ | $= \left(\frac{\partial U}{\partial T}\right)_V = k_B T \left[ 2 \left(\frac{\partial \ln Z}{\partial T}\right)_V + T \left(\frac{\partial^2 \ln Z}{\partial T^2}\right)_V \right]$ |

Now that we have described how the process works, we can set about practising this for different partition functions.

## Example 20.3

**(a) Two-level system**
The partition function for a two-level system (whose energy is either $-\Delta/2$ or $\Delta/2$) is given by eqn 20.2, which states that

$$Z = 2 \cosh\left(\frac{\beta\Delta}{2}\right). \tag{20.23}$$

Having obtained $Z$, we can immediately compute the internal energy $U$ and find that

$$U = -\frac{d\ln Z}{d\beta} = -\frac{\Delta}{2} \tanh\left(\frac{\beta\Delta}{2}\right). \tag{20.24}$$

Hence the heat capacity $C_V$ is

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = k_B \left(\frac{\beta\Delta}{2}\right)^2 \operatorname{sech}^2\left(\frac{\beta\Delta}{2}\right). \tag{20.25}$$

The Helmholtz function is

$$F = -k_B T \ln Z = -k_B T \ln\left[ 2 \cosh\left(\frac{\beta\Delta}{2}\right) \right], \tag{20.26}$$

and hence the entropy is

$$S = \frac{U - F}{T} = -\frac{\Delta}{2T} \tanh\left(\frac{\beta\Delta}{2}\right) + k_B \ln\left[ 2 \cosh\left(\frac{\beta\Delta}{2}\right) \right]. \tag{20.27}$$

These results are plotted in Fig. 20.4(a). At low temperature, the system is in the lower level and the internal energy $U$ is $-\Delta/2$. The entropy $S$ is $k_B \ln \Omega$, where $\Omega$ is the degeneracy and hence $\Omega = 1$ and so $S = k_B \ln 1 = 0$. At high temperature, the two levels are each occupied with probability $\frac{1}{2}$, $U$ therefore tends to 0 (which is halfway between $-\Delta/2$ and $\Delta/2$), and the entropy tends to $k_B \ln 2$ as expected. The entropy rises as the temperature increases because it reflects the freedom of the system to exist in different states, and at high temperature the system has more freedom (in that it can exist in either of the two states). Conversely, cooling corresponds to a kind of "ordering" in which the system can only exist in one state (the lower), and this gives rise to a reduction in the entropy.

[Image: Three graphs, each with two columns. Column (a) shows U, S, and C_V for a two-state system. Column (b) shows U, S, and C_V for a simple harmonic oscillator.]
**Fig. 20.4** The internal energy $U$, the entropy $S$, and the heat capacity $C_V$ for (a) the two-state system (with energy levels $\pm\Delta/2$) and (b) the simple harmonic oscillator.

The heat capacity is very small both (i) at low temperature ($k_B T \ll \Delta$) and (ii) at very high temperature ($k_B T \gg \Delta$), because changes in temperature have no effect on the internal energy when (i) the temperature is so low that only the lower level is occupied and even a small change in temperature won't alter that, and (ii) the temperature is so high that both levels are occupied equally and a small change in temperature won't alter this. At very low temperature, it is hard to change the energy of the system because there is not enough energy to excite transitions from the ground state and therefore the system is "stuck". At very high temperature, it is hard to change the energy of the system because both states are equally occupied. In between, roughly around a temperature $T \approx \Delta/k_B$, the heat capacity rises to a maximum, known as a Schottky anomaly, as shown in the lowest panel of Fig. 20.4(a). This arises because at this temperature, it is possible to thermally excite transitions between the two states of the system. Note, however, that the Schottky anomaly is not a sharp peak, cusp, or spike, as might be associated with a phase transition (see Section 28.7), but is a smooth, fairly broad maximum.

**(b) Simple harmonic oscillator**
The partition function for the simple harmonic oscillator (from eqn 20.3) is

$$Z = \frac{e^{-\frac{1}{2}\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}. \tag{20.28}$$

Hence (referring to Table 20.1), we find that $U$ is given by

$$U = -\frac{d\ln Z}{d\beta} = \hbar\omega \left( \frac{1}{2} + \frac{1}{e^{\beta\hbar\omega} - 1} \right) \tag{20.29}$$

and hence that $C_V$ is

$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = k_B (\beta\hbar\omega)^2 \frac{e^{\beta\hbar\omega}}{(e^{\beta\hbar\omega} - 1)^2}. \tag{20.30}$$

At high temperature, $\beta\hbar\omega \ll 1$ and so $(e^{\beta\hbar\omega} - 1) \approx \beta\hbar\omega$ and $C_V \to k_B$ (the equipartition result). Similarly, $U \to \frac{\hbar\omega}{2} + k_B T \approx k_B T$. The Helmholtz function is (referring to Table 20.1)

$$F = -k_B T \ln Z = \frac{\hbar\omega}{2} + k_B T \ln(1 - e^{-\beta\hbar\omega}), \tag{20.31}$$

and hence the entropy is (referring again to Table 20.1)

$$S = \frac{U - F}{T} = k_B \left[ \frac{\beta\hbar\omega}{e^{\beta\hbar\omega} - 1} - \ln(1 - e^{-\beta\hbar\omega}) \right]. \tag{20.32}$$

These results are plotted in Fig. 20.4(b). At absolute zero, only the lowest level is occupied, so the internal energy is $\frac{1}{2}\hbar\omega$ and the entropy is $k_B \ln 1 = 0$. The heat capacity is also zero. As the temperature rises, more and more energy levels in the ladder can be occupied, and $U$ rises without limit. The entropy also rises (and follows a dependence which is approximately $k_B \ln(k_B T/\hbar\omega)$ where $k_B T/\hbar\omega$ is approximately the number of occupied levels). Both functions carry on rising because the ladder of energy levels increases without limit. The heat capacity rises to a plateau at $C_V = k_B$, which is the equipartition result (see eqn 19.13).

The results for two further examples are plotted in Fig. 20.5 and are shown without derivation. The first is an $N$-level system and is shown in Fig. 20.5(a). At low temperature, the behaviour of the thermodynamic functions resembles that of the simple harmonic oscillator, but at higher temperature, $U$ and $S$ begin to saturate and $C_V$ falls, because the system has a limited number of energy levels.

[Image: Two graphs, each with three columns. Column (a) shows U, S, and C_V for an N-level system (N=20). Column (b) shows U, S, and C_V for a rotating diatomic molecule.]
**Fig. 20.5** The internal energy $U$, the entropy $S$, and the heat capacity $C_V$ for (a) the N-level system (the simulation is shown for $N = 20$) and (b) the rotating diatomic molecule (in this case $\Delta = \hbar^2/2I$ where $I$ is the moment of inertia).

Fig. 20.5(b) shows calculations for the rotating diatomic molecule. This resembles the simple harmonic oscillator at higher temperature (the heat capacity saturates at $C_V = k_B$) but differs at low temperature owing to the detailed difference in the structure of the energy levels. At high temperature, the heat capacity is given by the equipartition result (see eqn 19.13). This can be verified directly using the partition function, which, at high temperature, can be represented by the following integral:

$$Z = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\Delta J(J+1)} \approx \int_0^{\infty} (2J + 1)e^{-\beta\Delta J(J+1)} dJ, \tag{20.33}$$

where $\Delta = \hbar^2/2I$. Using

$$\frac{d}{dJ} e^{-\beta\Delta J(J+1)} = -(2J + 1)\beta\Delta e^{-\beta\Delta J(J+1)}, \tag{20.34}$$

we have that

$$Z = -\left[ \frac{1}{\beta\Delta} e^{-\beta\Delta J(J+1)} \right]_0^{\infty} = \frac{1}{\beta\Delta}. \tag{20.35}$$

This implies that $U = -d\ln Z/d\beta = 1/\beta = k_B T$ and hence $C_V = (dU/dT)_V = k_B$.

## 20.3 The big idea

The examples above illustrate the "big idea" of statistical mechanics: you describe a system by its energy levels $E_\alpha$ and evaluate its properties by following the prescription given by the two steps:

(1) Write down $Z = \sum_\alpha e^{-\beta E_\alpha}$.
(2) Evaluate various functions of state using the expressions given in Table 20.1.

And that's really all there is to it!

You can understand the results by comparing the energy $k_B T$ with the spacings between energy levels.

- If $k_B T$ is much less than the spacing between the lowest energy level and the first excited level then the system will sit in the lowest level.
- If there are a finite set of levels and $k_B T$ is much larger than the energy spacing between the lowest and highest levels, then each energy level will be occupied with equal probability.
- If there are an infinite ladder of levels and $k_B T$ is much larger than the energy spacing between adjacent levels, then the mean energy rises linearly with $T$ and one obtains a result consistent with the equipartition theorem.

## 20.4 Combining partition functions

Consider the case when the energy $E$ of a particular system depends on various independent contributions. For example, suppose it is a sum of two contributions $a$ and $b$, so that the energy levels are given by $E_{i,j}$ where

$$E_{i,j} = E^{(a)}_i + E^{(b)}_j, \tag{20.36}$$

and where $E^{(a)}_i$ is the $i$th level due to contribution $a$ and $E^{(b)}_j$ is the $j$th level due to contribution $b$, so the partition function $Z$ is

$$Z = \sum_i \sum_j e^{-\beta(E^{(a)}_i + E^{(b)}_j)} = \sum_i e^{-\beta E^{(a)}_i} \sum_j e^{-\beta E^{(b)}_j} = Z_a Z_b, \tag{20.37}$$

so that the partition functions of the independent contributions multiply. Hence also $\ln Z = \ln Z_a + \ln Z_b$, and the effect on functions of state which depend on $\ln Z$ is that the independent contributions add.

## Example 20.4

(i) The partition function $Z$ for $N$ independent simple harmonic oscillators is given by

$$Z = Z_{\text{SHO}}^N, \tag{20.38}$$

where $Z_{\text{SHO}} = e^{-\frac{1}{2}\beta\hbar\omega}/(1 - e^{-\beta\hbar\omega})$, from eqn 20.3, is the partition function for a single simple harmonic oscillator.

(ii) A diatomic molecule with both vibrational and rotational degrees of freedom has a partition function $Z$ given by

$$Z = Z_{\text{vib}} Z_{\text{rot}}, \tag{20.39}$$

where $Z_{\text{vib}}$ is the vibrational partition function $Z_{\text{vib}} = e^{-\frac{1}{2}\beta\hbar\omega}/(1 - e^{-\beta\hbar\omega})$, from eqn 20.3, and $Z_{\text{rot}}$ is the rotational partition function

$$Z_{\text{rot}} = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\hbar^2 J(J+1)/2I}. \tag{20.40}$$

from eqn 20.6. For a gas of diatomic molecules, we would also need a factor in the partition function corresponding to translational motion. We will derive this in the following chapter.

The final example of the chapter applies this to a simple magnetic system and allows us to derive Curie's law.

## Example 20.5

## The spin-$\frac{1}{2}$ paramagnet

In quantum mechanics, a particle with spin angular momentum equal to $\frac{1}{2}$, placed in a magnetic field $B$ along the $z$ direction, can exist in one of two eigenstates:

- $|\uparrow\rangle$, with angular momentum parallel to the $B$ field, and hence magnetic moment along $z$ equal to $-\mu_B$ (costing an energy $+\mu_B B$).
- $|\downarrow\rangle$, with angular momentum antiparallel to the $B$ field, and hence magnetic moment along $z$ equal to $+\mu_B$ (costing an energy $-\mu_B B$).

Here $\mu_B = e\hbar/2m$ is the Bohr magneton and we have used the fact that energy = $-\mathbf{m} \cdot \mathbf{B}$, and also that for a negatively charged particle (the electron) the angular momentum is antiparallel to the magnetic moment.

One spin-$\frac{1}{2}$ particle thus behaves like a two-state system, with the two states having energy $E$ given by: $E = \mu_B B$ and $E = -\mu_B B$. Therefore, the single-particle partition function (which we will call $Z_1$) is simply

$$Z_1 = e^{\beta\mu_B B} + e^{-\beta\mu_B B} = 2 \cosh(\beta\mu_B B). \tag{20.41}$$

A spin-$\frac{1}{2}$ paramagnet is an assembly of $N$ such particles, which are assumed to be non-interacting: thus each particle is independent and "does its own thing". Note that although it might be energetically favourable for all the spins to line up along the magnetic field, producing a state like $\cdots \uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\cdots$, such a state is not very likely: there is only one microstate associated with it. However, even though it is less energetically favourable, there are lots of microstates associated with having half of the states up and half of them down, e.g. $\cdots \uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\downarrow\downarrow\uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\uparrow\uparrow\uparrow\downarrow\uparrow\downarrow\uparrow\uparrow\downarrow\downarrow\downarrow\uparrow\cdots$

The balance between energy $U$ and entropy $S$ is encoded in the Helmholtz function $F = U - TS$ which shows that entropy becomes more important as $T$ gets larger, whereas $U$ is more relevant at low temperature.

Because the spins do not interact with each other the $N$-particle partition function $Z_N$ can be obtained by multiplying $N$ single-particle partition functions (using the result in eqn 20.37 for combining partition functions of independent systems). Therefore

$$Z_N = Z_1^N, \tag{20.42}$$

and hence $F$ is given by

$$F = -k_B T \ln Z_N = -N k_B T \ln [2 \cosh(\beta\mu_B B)]. \tag{20.43}$$

We can work out the magnetic moment $m$ of the paramagnet by computing

$$m = -\left(\frac{\partial F}{\partial B}\right)_T = N\mu_B \tanh(\beta\mu_B B), \tag{20.44}$$

(see Fig. 20.6) and it is worth considering this equation for a moment. Note that when $B$ gets very big (or $T$ gets very small), the magnetic moment tends to $N\mu_B$, corresponding to all the magnetic moments pointing up, i.e., to a state like $\cdots \uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\cdots$
On the other hand, if $B$ is very small (or $T$ gets very large), the magnetic moment tends to zero, corresponding to a state in which half of the magnetic moments are up and half are down, i.e., to a state like $\cdots \uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\downarrow\downarrow\uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\uparrow\uparrow\uparrow\downarrow\uparrow\downarrow\uparrow\uparrow\downarrow\downarrow\downarrow\uparrow\cdots$

We now want to calculate the magnetic susceptibility and show that it leads to what is known as Curie's law. Here is how we do it: the magnetization $M$ is the magnetic moment per unit volume, so writing the volume of the paramagnet as $V$ we have

$$M = \frac{m}{V} = \frac{N\mu_B}{V} \tanh(\beta\mu_B B). \tag{20.45}$$

[Image: A 3D plot of magnetic moment m versus field B and temperature T, showing a smooth surface that saturates at high B and low T.]
**Fig. 20.6** The behaviour of the magnetic moment $m$ as a function of field $B$ and temperature $T$ for a spin-$\frac{1}{2}$ paramagnet, as given by eqn 20.44.

Magnetic susceptibility is measured in a very weak field, so we can look in the limit when $B$ is small so that $\beta\mu_B B \ll 1$ and use $\tanh x \approx x$ for $x \ll 1$, and hence have that

$$M \approx \frac{N\mu_B^2 B}{V k_B T}. \tag{20.46}$$

Recall that $B = \mu_0(H + M)$, but for a weakly magnetic material (like a paramagnet), $M \approx \chi H$ and $\chi \ll 1$ is the magnetic susceptibility. Thus we can write that

$$B \approx \mu_0(1 + \chi)H \approx \frac{\mu_0 M}{\chi}$$

and hence

$$\chi \approx \frac{\mu_0 M}{B}. \tag{20.47}$$

This implies that

$$\chi \approx \frac{N\mu_0 \mu_B^2}{V k_B T}. \tag{20.48}$$

This result obeys Curie's law: $\chi \propto 1/T$.

## Chapter summary

- The partition function $Z = \sum_\alpha e^{-\beta E_\alpha}$ contains the information needed to find many thermodynamic properties.
- The equations $U = -d\ln Z/d\beta$, $F = -k_B T \ln Z$, $S = (U - F)/T$, $p = -\left(\frac{\partial F}{\partial V}\right)_T$, $H = U + pV$, $G = H - TS$ can be used to generate the relevant thermodynamic properties from $Z$.

## Exercises

(20.1) Show that at high temperature, such that $k_B T \gg \hbar\omega$, the partition function of the simple harmonic oscillator is approximately $Z \approx (\beta\hbar\omega)^{-1}$. Hence find $U, C, F$, and $S$ at high temperature. Repeat the problem for the high temperature limit of the rotational energy levels of the diatomic molecule for which $Z \approx (\beta\hbar^2/2I)^{-1}$ (see eqn 20.35).

(20.2) Show that

$$\ln P_j = \beta(F - E_j). \tag{20.49}$$

(20.3) Show that eqn 20.29 can be rewritten as

$$U = \frac{\hbar\omega}{2} \coth\left(\frac{\beta\hbar\omega}{2}\right), \tag{20.50}$$

and eqn 20.32 can be rewritten as

$$S = k_B \left[ \frac{\hbar\omega}{2} \coth\left(\frac{\beta\hbar\omega}{2}\right) - \ln\left( 2 \sinh\left(\frac{\beta\hbar\omega}{2}\right) \right) \right]. \tag{20.51}$$

(20.4) Show that the zero-point energy of a simple harmonic oscillator does not contribute to its entropy or heat capacity, but does contribute to its internal energy and Helmholtz function.

(20.5) Show that for $N$ non-interacting spin-$\frac{1}{2}$ particles in a magnetic field $B$ the energy $U$ is given by

$$U = -N\mu_B B \tanh\left(\frac{\mu_B B}{k_B T}\right), \tag{20.52}$$

the heat capacity is given by

$$\frac{C}{N k_B} = \left(\frac{\mu_B B}{k_B T}\right)^2 \operatorname{sech}^2\left(\frac{\mu_B B}{k_B T}\right), \tag{20.53}$$

and the entropy is given by

$$\frac{S}{N k_B} = \ln\left[ 2 \cosh\left(\frac{\mu_B B}{k_B T}\right) \right] - \frac{\mu_B B}{k_B T} \tanh\left(\frac{\mu_B B}{k_B T}\right). \tag{20.54}$$

(20.6) A certain magnetic system contains $n$ independent molecules per unit volume, each of which has four energy levels given by $0, \Delta - g\mu_B B, \Delta, \Delta + g\mu_B B$ ($g$ is a constant). Write down the partition function, compute the Helmholtz function and hence compute the magnetization $M$. Hence show that the magnetic susceptibility $\chi$ is given by

$$\chi = \lim_{B \to 0} \frac{\mu_0 M}{B} = \frac{2n\mu_0 g^2 \mu_B^2}{k_B T(3 + e^{\Delta/k_B T})}. \tag{20.55}$$

(20.7) The energy $E$ of a system of three independent harmonic oscillators is given by

$$E = (n_x + \tfrac{1}{2})\hbar\omega + (n_y + \tfrac{1}{2})\hbar\omega + (n_z + \tfrac{1}{2})\hbar\omega. \tag{20.56}$$

Show that the partition function $Z$ is given by

$$Z = Z_{\text{SHO}}^3, \tag{20.57}$$

where $Z_{\text{SHO}}$ is the partition function of a simple harmonic oscillator given in eqn 20.3. Hence show that the Helmholtz function is given by

$$F = \frac{3}{2}\hbar\omega + 3k_B T \ln(1 - e^{-\beta\hbar\omega}), \tag{20.58}$$

and that the heat capacity tends to $3k_B$ at high temperature.

(20.8) The internal levels of an isolated hydrogen atom are given by $E = -R/n^2$ where $R = 13.6$ eV. The degeneracy of each level is given by $2n^2$.
(a) Sketch the energy levels.
(b) Show that

$$Z = \sum_{n=1}^{\infty} 2n^2 \exp\left(\frac{R}{n^2 k_B T}\right). \tag{20.59}$$

Note that when $T \neq 0$, this expression for $Z$ diverges. This is because of the large degeneracy of the hydrogen atom's highly excited states. If the hydrogen atom were to be confined in a box of finite size, this would cut off the highly excited states and $Z$ would not then diverge. By approximating $Z$ as follows:

$$Z \approx \sum_{n=1}^{2} 2n^2 \exp\left(\frac{R}{n^2 k_B T}\right), \tag{20.60}$$

i.e., by ignoring all but the $n=1$ and $n=2$ states, estimate the mean energy of a hydrogen atom at 300 K.

(20.9) The energy of a paramagnet can be written as $U = -\mathbf{m} \cdot \mathbf{B}$. Writing $TS = U + F$, show that if $B$ is varied isothermally then

$$T \delta S = -\mathbf{B} \cdot \delta \mathbf{m}. \tag{20.61}$$

[Hint: use $\mathbf{m} = -(\partial F/\partial B)_T$.] Show that this is consistent with $\delta U = T \delta S - \mathbf{m} \cdot \delta \mathbf{B}$ (as in eqn 17.29).


===== Page 289 =====

# Part VIII

## Beyond the ideal gas

The discussion up to this point has concentrated on the ideal gas model and we go beyond this in Part VIII. This part is structured as follows:

- In Chapter 25 we discuss the effect of relativistic velocities on the properties of gases.
- In Chapters 26 and 27 we discuss the effect of intermolecular interactions and how real gases differ from the ideal gas.
- In Chapter 28 we discuss phase transitions, where the important Clausius-Clapeyron equation for a phase boundary is derived.
- In Chapter 29 we discuss the quantum mechanical implication of the existence of identical particles and the difference between fermions and bosons.
- In Chapter 30 we present the consequences for the properties of quantum gases.

===== Page 290 =====

# 25 Relativistic gases

25.1 Relativistic dispersion relation for massive particles  290
25.2 The ultrarelativistic gas  290
25.3 Adiabatic expansion of an ultrarelativistic gas  293
Chapter summary  295
Exercises  295

In the previous chapters we have assumed that the gas molecules move non-relativistically, so that the energy of a molecule is given by $E = p^2/2m$. However, there are many instances in physics where particles move at relativistic speeds. These include electrons in white dwarf stars, photons in a black-body cavity, and particles created in the early Universe. This chapter therefore considers the modifications that have to be made to the ideal gas law when the particles become relativistic.

## 25.1 Relativistic dispersion relation for massive particles

For a particle of mass $m$ and momentum $p$, the relativistic energy is given by

$$E = \sqrt{p^2 c^2 + m^2 c^4}. \quad (25.1)$$

This can be expanded in the non-relativistic limit $p \ll mc$ to give

$$E = mc^2 + \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \cdots \quad (25.2)$$

The first term $mc^2$ is just the rest energy of the particle (which we usually ignore by redefining the zero of energy). The second term is the familiar non-relativistic kinetic energy. The third term is the leading relativistic correction.

In the ultrarelativistic limit, when $p \gg mc$, the energy is given by

$$E = pc. \quad (25.3)$$

This is the same as the energy of a photon (which has $m = 0$). In this chapter, we will consider the case of an ultrarelativistic gas, i.e., a gas for which eqn 25.3 holds.

## 25.2 The ultrarelativistic gas

We can treat an ultrarelativistic gas of massive particles in much the same way as we treated the photon gas in Chapter 23. We start by writing down the density of states. As for the photon gas, the density of states (including a factor of 2 for the two spin states of the particle) is given by

$$g(p) dp = \frac{V}{h^3} 4\pi p^2 dp \times 2 = \frac{8\pi V}{h^3} p^2 dp. \quad (25.4)$$

The energy of a particle is $E = pc$, so that

$$g(E) dE = \frac{8\pi V}{h^3 c^3} E^2 dE. \quad (25.5)$$

The mean number of particles in a state with energy $E$ is given by the Bose-Einstein or Fermi-Dirac distribution (see Chapter 29). However, in the classical limit (when the gas is dilute), these distributions reduce to the Boltzmann distribution. For the present, we will assume that the gas is dilute so that the Boltzmann distribution applies. Then the number of particles with energy between $E$ and $E + dE$ is

$$n(E) dE = g(E) dE \, e^{-\beta E}, \quad (25.6)$$

where $\beta = 1/k_B T$. The total number of particles is

$$N = \int_0^\infty n(E) dE = \frac{8\pi V}{h^3 c^3} \int_0^\infty E^2 e^{-\beta E} dE. \quad (25.7)$$

Using the integral $\int_0^\infty E^2 e^{-\beta E} dE = 2/\beta^3$, we get

$$N = \frac{8\pi V}{h^3 c^3} \frac{2}{\beta^3} = \frac{16\pi V}{(h c)^3} (k_B T)^3. \quad (25.8)$$

The internal energy is

$$U = \int_0^\infty E n(E) dE = \frac{8\pi V}{h^3 c^3} \int_0^\infty E^3 e^{-\beta E} dE. \quad (25.9)$$

Using $\int_0^\infty E^3 e^{-\beta E} dE = 6/\beta^4$, we get

$$U = \frac{8\pi V}{h^3 c^3} \frac{6}{\beta^4} = \frac{48\pi V}{(h c)^3} (k_B T)^4. \quad (25.10)$$

Thus, the energy density $u = U/V$ is given by

$$u = \frac{48\pi}{(h c)^3} (k_B T)^4. \quad (25.11)$$

Comparing this with the result for a photon gas (eqn 23.37), we see that the ultrarelativistic gas has the same $T^4$ dependence, but with a different numerical coefficient. For photons, the coefficient is $\pi^2 k_B^4/(15 c^3 \hbar^3) = 8\pi^5 k_B^4/(15 h^3 c^3)$. The difference arises because photons have two polarizations (spin states) and a different dispersion relation (they have no rest mass).

We can also calculate the pressure. For an ultrarelativistic gas, we have

$$p = \frac{1}{3} n \langle p v \rangle = \frac{1}{3} n \langle p c \rangle = \frac{1}{3} n \langle E \rangle = \frac{1}{3} u. \quad (25.12)$$

So, for an ultrarelativistic gas,

$$p = \frac{u}{3}. \quad (25.13)$$

This is the same as the result for a photon gas (eqn 23.4), and differs from the non-relativistic result $p = 2u/3$ (eqn 6.25). The difference arises because for ultrarelativistic particles, $E = pc$, whereas for non-relativistic particles, $E = p^2/2m$.

## 25.3 Adiabatic expansion of an ultrarelativistic gas

We now consider what happens when an ultrarelativistic gas expands adiabatically. For a reversible adiabatic (isentropic) process, the entropy is constant. The entropy of an ultrarelativistic gas can be obtained from the thermodynamic relation

$$S = \frac{U + pV - \mu N}{T}. \quad (25.14)$$

For a dilute gas, the chemical potential $\mu$ is given by (see eqn 22.15)

$$\mu = k_B T \ln(n \lambda_{\text{th}}^3), \quad (25.15)$$

where now the thermal wavelength must be modified for relativistic particles. However, for an ultrarelativistic gas, we can derive the adiabatic relation directly from the first law.

For an adiabatic process, $\mathrm{d}Q = 0$, so

$$\mathrm{d}U = -p \mathrm{d}V. \quad (25.16)$$

We have $U = a V T^4$, where $a$ is a constant (from eqn 25.10), and $p = u/3 = a T^4/3$. Thus

$$\mathrm{d}U = a T^4 \mathrm{d}V + 4a V T^3 \mathrm{d}T. \quad (25.17)$$

Substituting into eqn 25.16 gives

$$a T^4 \mathrm{d}V + 4a V T^3 \mathrm{d}T = -\frac{a}{3} T^4 \mathrm{d}V. \quad (25.18)$$

Rearranging,

$$\frac{4}{3} T^4 \mathrm{d}V + 4 V T^3 \mathrm{d}T = 0, \quad (25.19)$$

or

$$\frac{\mathrm{d}V}{V} = -3 \frac{\mathrm{d}T}{T}. \quad (25.20)$$

Integrating gives

$$V T^3 = \text{constant}. \quad (25.21)$$

Using $p = a T^4/3$, we can also write this as

$$p V^{4/3} = \text{constant}. \quad (25.22)$$

This is the adiabatic equation for an ultrarelativistic gas. Compare this with the non-relativistic result $p V^\gamma = \text{constant}$, where $\gamma = 5/3$ for a monatomic gas. For an ultrarelativistic gas, the effective value of $\gamma$ is $4/3$.

## Chapter summary

- For an ultrarelativistic gas, the energy of a particle is $E = pc$.
- The energy density is $u \propto T^4$.
- The pressure is $p = u/3$.
- For an adiabatic expansion, $V T^3 = \text{constant}$, or equivalently $p V^{4/3} = \text{constant}$.

## Exercises

(25.1) Show that for an ultrarelativistic gas, the average energy per particle is $\langle E \rangle = 3k_B T$. Compare this with the non-relativistic result $\langle E \rangle = \frac{3}{2} k_B T$.

(25.2) Derive the entropy of an ultrarelativistic gas and show that it is given by $S = \frac{4}{3} U/T$.

(25.3) Consider a gas of ultrarelativistic particles in a volume $V$. Show that the pressure is given by $p = \frac{1}{3} u$, where $u$ is the energy density. (Hint: use the kinetic theory result $p = \frac{1}{3} n \langle p v \rangle$.)

(25.4) Show that for an ultrarelativistic gas, the heat capacity at constant volume is $C_V = 3N k_B$. (Hint: use $U = 3N k_B T$.)

(25.5) Derive the adiabatic relation $p V^{4/3} = \text{constant}$ for an ultrarelativistic gas using the first law of thermodynamics.

===== Page 296 =====

# 26 Real gases

26.1 The van der Waals gas  296
26.2 The Dieterici equation  304
26.3 Virial expansion  306
26.4 The law of corresponding states  310
Chapter summary  312
Exercises  312

So far in this book, we have concentrated on the ideal gas, which obeys the equation of state $pV = N k_B T$. This model assumes that the gas molecules have zero size and do not interact with each other. However, real gases do not obey this equation exactly, especially at high densities and low temperatures, where the molecules are close together and the intermolecular forces become important. In this chapter, we will consider how the ideal gas equation of state can be modified to account for these effects.

## 26.1 The van der Waals gas

The van der Waals equation of state is one of the simplest and most famous modifications of the ideal gas law. It is given by

$$\left(p + \frac{a N^2}{V^2}\right) (V - bN) = N k_B T, \quad (26.1)$$

or, in terms of the molar volume $V_m = V/N_A$ (where $N_A$ is Avogadro's number), it can be written as

$$\left(p + \frac{a}{V_m^2}\right) (V_m - b) = RT, \quad (26.2)$$

where $R = N_A k_B$ is the gas constant.

The van der Waals equation accounts for two effects:

1. The term $V - bN$ (or $V_m - b$) accounts for the finite size of the molecules. The parameter $b$ is related to the volume excluded by the molecules. If the molecules are hard spheres of diameter $d$, then $b = \frac{2}{3} \pi d^3 N_A$ (the excluded volume per mole). This term reduces the available volume for the molecules to move in.

2. The term $a N^2/V^2$ (or $a/V_m^2$) accounts for the attractive forces between the molecules. The parameter $a$ is a measure of the strength of the attractive interactions. This term reduces the pressure because the attractive forces between the molecules pull them together.

## Example 26.1

Show that the van der Waals equation reduces to the ideal gas equation in the limit of low density.

Solution: In the low-density limit, $V$ is large, so $V - bN \approx V$ and $a N^2/V^2$ is small. Thus the van der Waals equation becomes approximately

$$pV \approx N k_B T, \quad (26.3)$$

which is the ideal gas equation.

The van der Waals equation can be written in the form

$$p = \frac{N k_B T}{V - bN} - \frac{a N^2}{V^2}. \quad (26.4)$$

This shows that the pressure is reduced compared to the ideal gas value because of the attractive forces (the second term), and increased because of the finite size of the molecules (the denominator of the first term is smaller than $V$).

## Example 26.2

Find the critical point of the van der Waals gas.

Solution: The critical point is the point at which the isotherms of the $p$-$V$ diagram have an inflection point. That is, at the critical point,

$$\left(\frac{\partial p}{\partial V}\right)_T = 0, \quad \left(\frac{\partial^2 p}{\partial V^2}\right)_T = 0. \quad (26.5)$$

Using eqn 26.4 (with $N = N_A$ for one mole), we have

$$p = \frac{RT}{V_m - b} - \frac{a}{V_m^2}. \quad (26.6)$$

Differentiating with respect to $V_m$ at constant $T$,

$$\left(\frac{\partial p}{\partial V_m}\right)_T = -\frac{RT}{(V_m - b)^2} + \frac{2a}{V_m^3}. \quad (26.7)$$

$$\left(\frac{\partial^2 p}{\partial V_m^2}\right)_T = \frac{2RT}{(V_m - b)^3} - \frac{6a}{V_m^4}. \quad (26.8)$$

Setting these equal to zero and solving gives

$$V_c = 3b, \quad T_c = \frac{8a}{27 R b}, \quad p_c = \frac{a}{27 b^2}. \quad (26.9)$$

These are the critical volume, temperature, and pressure for a van der Waals gas.

## Example 26.3

Show that the van der Waals equation can be written in reduced form as

$$\left(p_r + \frac{3}{V_r^2}\right) (3V_r - 1) = 8T_r, \quad (26.10)$$

where $p_r = p/p_c$, $V_r = V_m/V_c$, and $T_r = T/T_c$.

Solution: Substituting $p = p_r p_c$, $V_m = V_r V_c$, and $T = T_r T_c$ into eqn 26.6, and using the expressions for $p_c$, $V_c$, and $T_c$ from eqn 26.9, gives the reduced equation of state. This is the law of corresponding states (see Section 26.4).

The van der Waals equation is not exact, but it captures the essential physics of real gases. Many other equations of state have been proposed, some of which are more accurate. We will discuss two of these in the next section.

## 26.2 The Dieterici equation

The Dieterici equation of state is another two-parameter equation that often gives a better fit to experimental data than the van der Waals equation. It is given by

$$p(V_m - b) = RT e^{-a/(R T V_m)}. \quad (26.11)$$

This equation can also be written as

$$p = \frac{RT}{V_m - b} e^{-a/(R T V_m)}. \quad (26.12)$$

The Dieterici equation accounts for the attractive forces between molecules through the exponential factor. In the low-density limit, the exponential is approximately $1 - a/(R T V_m)$, and the equation reduces to the van der Waals equation.

## Example 26.4

Find the critical point of the Dieterici gas.

Solution: At the critical point, we again require

$$\left(\frac{\partial p}{\partial V_m}\right)_T = 0, \quad \left(\frac{\partial^2 p}{\partial V_m^2}\right)_T = 0. \quad (26.13)$$

Using eqn 26.12, we have

$$\ln p = \ln(RT) - \ln(V_m - b) - \frac{a}{R T V_m}. \quad (26.14)$$

Differentiating with respect to $V_m$ at constant $T$,

$$\frac{1}{p}\left(\frac{\partial p}{\partial V_m}\right)_T = -\frac{1}{V_m - b} + \frac{a}{R T V_m^2}. \quad (26.15)$$

$$\frac{1}{p}\left(\frac{\partial^2 p}{\partial V_m^2}\right)_T - \frac{1}{p^2}\left(\frac{\partial p}{\partial V_m}\right)_T^2 = \frac{1}{(V_m - b)^2} - \frac{2a}{R T V_m^3}. \quad (26.16)$$

Setting the first derivative to zero gives

$$V_c = 2b, \quad T_c = \frac{a}{4 R b}. \quad (26.17)$$

Substituting these into eqn 26.12 gives

$$p_c = \frac{a}{4 e^2 b^2}. \quad (26.18)$$

## 26.3 Virial expansion

The virial expansion is a general way of writing the equation of state of a real gas as a power series in the density. It is given by

$$\frac{p}{n k_B T} = 1 + B_2(T) n + B_3(T) n^2 + \cdots, \quad (26.19)$$

where $n = N/V$ is the number density, and $B_2(T), B_3(T), \ldots$ are the virial coefficients. The first virial coefficient is 1 (corresponding to the ideal gas). The second virial coefficient $B_2(T)$ accounts for two-body interactions, the third virial coefficient $B_3(T)$ accounts for three-body interactions, and so on.

For a van der Waals gas, we can find the virial coefficients by expanding eqn 26.4 in powers of $n$:

$$\frac{p}{n k_B T} = \frac{1}{1 - b n} - \frac{a n}{k_B T} = 1 + \left(b - \frac{a}{k_B T}\right) n + b^2 n^2 + \cdots \quad (26.20)$$

Thus, for the van der Waals gas,

$$B_2(T) = b - \frac{a}{k_B T}, \quad B_3(T) = b^2, \quad \text{etc.} \quad (26.21)$$

The second virial coefficient is an important quantity because it can be measured experimentally and contains information about the intermolecular potential.

## Example 26.5

The Boyle temperature $T_B$ is the temperature at which the second virial coefficient vanishes, i.e., $B_2(T_B) = 0$. For the van der Waals gas, show that $T_B = a/(k_B b)$.

Solution: From eqn 26.21, $B_2(T) = b - a/(k_B T)$. Setting this to zero gives $T_B = a/(k_B b)$.

## 26.4 The law of corresponding states

The law of corresponding states states that all gases obey the same equation of state when expressed in terms of their reduced variables $p_r = p/p_c$, $V_r = V/V_c$, and $T_r = T/T_c$. This is true for the van der Waals equation, as we saw in Example 26.3. It is also approximately true for real gases, although it is not exact. The law of corresponding states is a consequence of the fact that the intermolecular potential has a similar form for all gases, with only two parameters (the depth of the potential well and the range of the potential).

## Chapter summary

- Real gases deviate from the ideal gas law because molecules have finite size and interact with each other.
- The van der Waals equation is $\left(p + \frac{a N^2}{V^2}\right) (V - bN) = N k_B T$.
- The Dieterici equation is $p(V_m - b) = RT e^{-a/(R T V_m)}$.
- The virial expansion is $\frac{p}{n k_B T} = 1 + B_2(T) n + B_3(T) n^2 + \cdots$.
- The law of corresponding states states that all gases obey the same equation of state in terms of reduced variables.

## Exercises

(26.1) Show that the van der Waals equation can be written in the form

$$Z = \frac{pV_m}{RT} = \frac{V_m}{V_m - b} - \frac{a}{R T V_m}, \quad (26.22)$$

where $Z$ is the compressibility factor.

(26.2) For a van der Waals gas, show that the internal energy is given by

$$U = C_V T - \frac{a N^2}{V} + \text{constant}. \quad (26.23)$$

(26.3) Show that for a van der Waals gas, the entropy is given by

$$S = C_V \ln T + N k_B \ln(V - bN) + \text{constant}. \quad (26.24)$$

(26.4) The second virial coefficient for a Lennard-Jones potential can be written as

$$B_2(T) = \frac{2}{3} \pi \sigma^3 \left[ 1 - \frac{1}{k_B T} \int_0^\infty \left(1 - e^{-V(r)/k_B T}\right) r^2 dr \right]. \quad (26.25)$$

Discuss the temperature dependence of $B_2(T)$ for a Lennard-Jones potential.

(26.5) Show that the law of corresponding states holds for the Dieterici equation.

===== Page 313 =====

# 27 Cooling real gases

27.1 The Joule expansion  313
27.2 Isothermal expansion  315
27.3 Joule-Kelvin expansion  316
27.4 Liquefaction of gases  318
Chapter summary  320
Exercises  320

In this chapter, we examine the thermodynamic properties of real gases, focusing on how they can be cooled by various expansion processes. Cooling real gases is important for liquefaction and for achieving low temperatures. We will consider three types of expansion: the Joule expansion (free expansion), the isothermal expansion, and the Joule-Kelvin (or Joule-Thomson) expansion.

## 27.1 The Joule expansion

The Joule expansion (also called free expansion) is an irreversible process in which a gas expands into a vacuum without doing any work. We considered this process for an ideal gas in Section 14.4, and found that the temperature does not change because the internal energy depends only on temperature.

For a real gas, the internal energy depends on both temperature and volume, so the temperature can change during a Joule expansion. The Joule coefficient $\mu_J$ is defined as

$$\mu_J = \left(\frac{\partial T}{\partial V}\right)_U. \quad (27.1)$$

We can relate $\mu_J$ to other thermodynamic quantities. From the first law, $dU = T dS - p dV$. For a Joule expansion, $dU = 0$, so

$$0 = T dS - p dV \Rightarrow dS = \frac{p}{T} dV. \quad (27.2)$$

But $S = S(T, V)$, so

$$dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV. \quad (27.3)$$

Using $(\partial S/\partial T)_V = C_V/T$ and a Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$, we get

$$dS = \frac{C_V}{T} dT + \left(\frac{\partial p}{\partial T}\right)_V dV. \quad (27.4)$$

Setting $dS = p/T dV$ (from eqn 27.2), we get

$$\frac{C_V}{T} dT + \left(\frac{\partial p}{\partial T}\right)_V dV = \frac{p}{T} dV. \quad (27.5)$$

Rearranging gives

$$\left(\frac{\partial T}{\partial V}\right)_U = \frac{1}{C_V} \left[ p - T \left(\frac{\partial p}{\partial T}\right)_V \right]. \quad (27.6)$$

Thus,

$$\mu_J = \frac{1}{C_V} \left[ p - T \left(\frac{\partial p}{\partial T}\right)_V \right]. \quad (27.7)$$

For an ideal gas, $p = N k_B T/V$, so $T(\partial p/\partial T)_V = p$, and thus $\mu_J = 0$, as expected.

For a van der Waals gas, we can calculate $\mu_J$ and see that it is non-zero. This means that a real gas changes temperature when it undergoes a Joule expansion.

## Example 27.1

Calculate the Joule coefficient for a van der Waals gas.

Solution: For a van der Waals gas,

$$p = \frac{N k_B T}{V - bN} - \frac{a N^2}{V^2}. \quad (27.8)$$

Then,

$$\left(\frac{\partial p}{\partial T}\right)_V = \frac{N k_B}{V - bN}. \quad (27.9)$$

Substituting into eqn 27.7,

$$\mu_J = \frac{1}{C_V} \left[ \frac{N k_B T}{V - bN} - \frac{a N^2}{V^2} - T \frac{N k_B}{V - bN} \right] = -\frac{1}{C_V} \frac{a N^2}{V^2}. \quad (27.10)$$

Thus, for a van der Waals gas, $\mu_J$ is negative, so the temperature decreases during a Joule expansion (if $a > 0$). This makes sense: the gas does work against the attractive forces between molecules as it expands, so its internal energy decreases, leading to a temperature drop.

## 27.2 Isothermal expansion

In an isothermal expansion, the temperature is kept constant by allowing heat to flow into or out of the gas. For a real gas, the internal energy changes with volume even at constant temperature. The heat absorbed during an isothermal expansion of a real gas is given by

$$\Delta Q = T \Delta S. \quad (27.11)$$

We can calculate the entropy change using

$$\Delta S = \int_{V_1}^{V_2} \left(\frac{\partial S}{\partial V}\right)_T dV = \int_{V_1}^{V_2} \left(\frac{\partial p}{\partial T}\right)_V dV. \quad (27.12)$$

For a van der Waals gas, $(\partial p/\partial T)_V = N k_B/(V - bN)$, so

$$\Delta S = N k_B \ln\left(\frac{V_2 - bN}{V_1 - bN}\right). \quad (27.13)$$

Thus, the heat absorbed is

$$\Delta Q = T N k_B \ln\left(\frac{V_2 - bN}{V_1 - bN}\right). \quad (27.14)$$

For an ideal gas ($b = 0$), this reduces to $\Delta Q = N k_B T \ln(V_2/V_1)$, as expected.

## 27.3 Joule-Kelvin expansion

The Joule-Kelvin expansion (also called the Joule-Thomson expansion) is a process in which a gas is forced through a porous plug or a throttle valve, so that it expands from a high pressure to a low pressure without any heat exchange with the surroundings ($\Delta Q = 0$). This is a throttling process, and it is isenthalpic (constant enthalpy) because no work is done on the gas and no heat is exchanged.

The Joule-Kelvin coefficient $\mu_{JK}$ is defined as

$$\mu_{JK} = \left(\frac{\partial T}{\partial p}\right)_H. \quad (27.15)$$

We can relate $\mu_{JK}$ to other thermodynamic quantities. Since $H = U + pV$, and $dH = T dS + V dp$. For an isenthalpic process, $dH = 0$, so

$$0 = T dS + V dp \Rightarrow dS = -\frac{V}{T} dp. \quad (27.16)$$

But $S = S(T, p)$, so

$$dS = \left(\frac{\partial S}{\partial T}\right)_p dT + \left(\frac{\partial S}{\partial p}\right)_T dp. \quad (27.17)$$

Using $(\partial S/\partial T)_p = C_p/T$ and a Maxwell relation $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$, we get

$$dS = \frac{C_p}{T} dT - \left(\frac{\partial V}{\partial T}\right)_p dp. \quad (27.18)$$

Setting $dS = -V/T dp$ (from eqn 27.16), we get

$$\frac{C_p}{T} dT - \left(\frac{\partial V}{\partial T}\right)_p dp = -\frac{V}{T} dp. \quad (27.19)$$

Rearranging gives

$$\left(\frac{\partial T}{\partial p}\right)_H = \frac{1}{C_p} \left[ T \left(\frac{\partial V}{\partial T}\right)_p - V \right]. \quad (27.20)$$

Thus,

$$\mu_{JK} = \frac{1}{C_p} \left[ T \left(\frac{\partial V}{\partial T}\right)_p - V \right]. \quad (27.21)$$

For an ideal gas, $V = N k_B T/p$, so $T(\partial V/\partial T)_p = V$, and thus $\mu_{JK} = 0$. For a real gas, $\mu_{JK}$ can be positive (cooling) or negative (heating) depending on the temperature and pressure.

## Example 27.2

Calculate the Joule-Kelvin coefficient for a van der Waals gas in the low-density limit.

Solution: For a van der Waals gas, we can write (for one mole)

$$V_m = \frac{RT}{p} + b - \frac{a}{RT}. \quad (27.22)$$

Then,

$$\left(\frac{\partial V_m}{\partial T}\right)_p = \frac{R}{p} + \frac{a}{R T^2}. \quad (27.23)$$

Substituting into eqn 27.21,

$$\mu_{JK} = \frac{1}{C_p} \left[ T \left(\frac{R}{p} + \frac{a}{R T^2}\right) - \left(\frac{RT}{p} + b - \frac{a}{RT}\right) \right]. \quad (27.24)$$

Simplifying,

$$\mu_{JK} = \frac{1}{C_p} \left[ \frac{2a}{RT} - b \right]. \quad (27.25)$$

The temperature at which $\mu_{JK} = 0$ is called the inversion temperature $T_i$. From eqn 27.25,

$$T_i = \frac{2a}{R b}. \quad (27.26)$$

Above the inversion temperature, the gas heats up on expansion; below it, the gas cools. This is important for liquefaction.

## 27.4 Liquefaction of gases

The Joule-Kelvin effect can be used to liquefy gases. The gas is first cooled below its inversion temperature (by using a refrigerator or by pre-cooling with another gas). Then it is passed through a throttle valve, where it expands and cools further. The cooled gas is passed through a heat exchanger to pre-cool the incoming gas, and the process is repeated until the gas liquefies. This is the principle of the Linde process for liquefying air.

## Chapter summary

- The Joule coefficient is $\mu_J = \frac{1}{C_V} \left[ p - T \left(\frac{\partial p}{\partial T}\right)_V \right]$. It describes the temperature change during a free expansion.
- The Joule-Kelvin coefficient is $\mu_{JK} = \frac{1}{C_p} \left[ T \left(\frac{\partial V}{\partial T}\right)_p - V \right]$. It describes the temperature change during a throttling process.
- Real gases cool on expansion if the Joule-Kelvin coefficient is positive. This is the basis for liquefaction.

## Exercises

(27.1) Show that for a van der Waals gas, the Joule coefficient is $\mu_J = -a N^2/(C_V V^2)$.

(27.2) Show that for a van der Waals gas, the Joule-Kelvin coefficient in the low-density limit is $\mu_{JK} = \frac{1}{C_p} \left( \frac{2a}{RT} - b \right)$.

(27.3) Calculate the inversion temperature for a van der Waals gas. For helium, $a = 0.0034 \, \text{Pa m}^6 \text{mol}^{-2}$ and $b = 2.37 \times 10^{-5} \, \text{m}^3 \text{mol}^{-1}$. Estimate the inversion temperature.

(27.4) Explain why the Joule-Kelvin expansion can be used to liquefy gases, and why pre-cooling is often necessary.

(27.5) For a gas obeying the Dieterici equation, find the Joule-Kelvin coefficient and the inversion temperature.

===== Page 321 =====

# 28 Phase transitions

28.1 Latent heat  321
28.2 Chemical potential and phase changes  324
28.3 The Clausius-Clapeyron equation  324
28.4 Stability and metastability  329
28.5 The Gibbs phase rule  332
28.6 Colligative properties  334
28.7 Classification of phase transitions  335
28.8 The Ising model  338
Chapter summary  343
Further reading  343
Exercises  343

A phase transition is a change of a substance from one phase (solid, liquid, or gas) to another. Examples include the melting of ice, the boiling of water, and the condensation of a vapour into a liquid. Phase transitions are of great importance in physics, chemistry, and materials science. In this chapter, we will use thermodynamics to understand the conditions under which phase transitions occur, and we will derive the Clausius-Clapeyron equation, which describes the phase boundary between two phases. We will also discuss the classification of phase transitions and introduce the Ising model as a simple model of a phase transition.

## 28.1 Latent heat

When a substance undergoes a phase transition, it absorbs or releases heat without changing its temperature. This heat is called the latent heat (or enthalpy of transformation). For example, when ice melts at $0^\circ \text{C}$, it absorbs $333 \, \text{kJ kg}^{-1}$ of heat (the latent heat of fusion). When water boils at $100^\circ \text{C}$, it absorbs $2260 \, \text{kJ kg}^{-1}$ of heat (the latent heat of vaporization).

The latent heat $L$ is defined as the heat absorbed per unit mass (or per mole) during a phase transition at constant temperature and pressure:

$$L = \frac{\Delta Q}{m} = T \Delta s, \quad (28.1)$$

where $\Delta s$ is the change in specific entropy (entropy per unit mass) between the two phases.

Alternatively, in molar terms,

$$L = T \Delta s_m, \quad (28.2)$$

where $\Delta s_m$ is the change in molar entropy.

Since the transition occurs at constant pressure, the latent heat is equal to the change in enthalpy:

$$L = \Delta h = T \Delta s. \quad (28.3)$$

## Example 28.1

Calculate the change in entropy when 1 kg of ice melts at $0^\circ \text{C}$.

Solution: The latent heat of fusion of ice is $L = 3.33 \times 10^5 \, \text{J kg}^{-1}$. The entropy change is

$$\Delta S = \frac{L}{T} = \frac{3.33 \times 10^5}{273} \approx 1.22 \times 10^3 \, \text{J K}^{-1}. \quad (28.4)$$

## 28.2 Chemical potential and phase changes

At equilibrium, the chemical potentials of the two phases must be equal. For a phase transition between phase 1 and phase 2,

$$\mu_1(T, p) = \mu_2(T, p). \quad (28.5)$$

This equation determines the phase boundary in the $p$-$T$ plane. The Clausius-Clapeyron equation (derived below) gives the slope of the phase boundary.

## 28.3 The Clausius-Clapeyron equation

The Clausius-Clapeyron equation relates the slope of the phase boundary to the latent heat and the change in volume:

$$\frac{dp}{dT} = \frac{L}{T \Delta V}, \quad (28.6)$$

where $\Delta V = V_2 - V_1$ is the change in volume (per mole or per unit mass) when the substance changes from phase 1 to phase 2.

We can derive the Clausius-Clapeyron equation as follows. Along the phase boundary, $\mu_1 = \mu_2$. Therefore,

$$d\mu_1 = d\mu_2. \quad (28.7)$$

Using $d\mu = -s dT + v dp$ (where $s$ is the entropy per mole and $v$ is the volume per mole), we get

$$-s_1 dT + v_1 dp = -s_2 dT + v_2 dp. \quad (28.8)$$

Rearranging,

$$(v_2 - v_1) dp = (s_2 - s_1) dT. \quad (28.9)$$

Thus,

$$\frac{dp}{dT} = \frac{s_2 - s_1}{v_2 - v_1} = \frac{L}{T (v_2 - v_1)}. \quad (28.10)$$

This is the Clausius-Clapeyron equation.

For a liquid-gas transition, $v_2 \gg v_1$ (since the molar volume of the gas is much larger than that of the liquid), and if we assume the gas is ideal, $v_2 = RT/p$, then eqn 28.10 becomes

$$\frac{dp}{dT} = \frac{L}{T} \frac{p}{RT} = \frac{L p}{R T^2}. \quad (28.11)$$

This can be rewritten as

$$\frac{d \ln p}{dT} = \frac{L}{R T^2}. \quad (28.12)$$

If $L$ is approximately constant, this can be integrated to give

$$\ln p = -\frac{L}{R T} + \text{constant}, \quad (28.13)$$

or

$$p = p_0 e^{-L/(R T)}. \quad (28.14)$$

This shows that the vapour pressure of a liquid increases exponentially with temperature.

## Example 28.2

The latent heat of vaporization of water is approximately $L = 2.26 \times 10^6 \, \text{J kg}^{-1}$. At $100^\circ \text{C}$ (373 K), the vapour pressure is 1 atm. Estimate the vapour pressure at $90^\circ \text{C}$ (363 K).

Solution: Using eqn 28.13,

$$\ln\left(\frac{p_2}{p_1}\right) = -\frac{L}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right). \quad (28.15)$$

Here, $L = 2.26 \times 10^6 \, \text{J kg}^{-1}$, and the molar mass of water is $0.018 \, \text{kg mol}^{-1}$, so the molar latent heat is $L_m = 2.26 \times 10^6 \times 0.018 \approx 4.07 \times 10^4 \, \text{J mol}^{-1}$. Then,

$$\ln\left(\frac{p_2}{1}\right) = -\frac{4.07 \times 10^4}{8.314} \left(\frac{1}{363} - \frac{1}{373}\right). \quad (28.16)$$

$$\ln p_2 = -4896 \times (0.00275 - 0.00268) = -4896 \times 7.4 \times 10^{-5} \approx -0.362. \quad (28.17)$$

Thus, $p_2 \approx e^{-0.362} \approx 0.696 \, \text{atm}$. So the vapour pressure at $90^\circ \text{C}$ is about 0.7 atm.

## 28.4 Stability and metastability

A phase transition occurs when the system can lower its Gibbs free energy by changing phase. However, it is possible for a system to be in a metastable state, where it is not in global equilibrium but is locally stable. Examples include supercooled water (liquid water below $0^\circ \text{C}$) and supersaturated vapour (vapour above the saturation pressure). A metastable state can persist for a long time if there is no nucleation site to trigger the phase transition.

The stability of a phase is determined by the curvature of the Gibbs free energy. For a single phase to be stable, we require

$$\left(\frac{\partial^2 G}{\partial p^2}\right)_T < 0, \quad \text{or equivalently} \quad \kappa_T > 0, \quad (28.18)$$

where $\kappa_T$ is the isothermal compressibility. If $\kappa_T$ becomes negative, the phase becomes unstable and a phase transition occurs.

## 28.5 The Gibbs phase rule

The Gibbs phase rule gives the number of degrees of freedom (the number of independent intensive variables) for a system in equilibrium. It is given by

$$F = C - P + 2, \quad (28.19)$$

where $C$ is the number of components (chemically distinct constituents) and $P$ is the number of phases. For a pure substance ($C = 1$), we have:

- $P = 1$: $F = 2$ (we can vary $T$ and $p$ independently).
- $P = 2$: $F = 1$ (the phase boundary is a line in the $p$-$T$ plane).
- $P = 3$: $F = 0$ (the triple point, where all three phases coexist, is a point).

## Example 28.3

How many degrees of freedom does a mixture of two components (e.g., water and salt) have at a triple point where three phases coexist?

Solution: Here $C = 2$ and $P = 3$, so $F = 2 - 3 + 2 = 1$. So there is one degree of freedom. This means that at a triple point of a binary mixture, the temperature and pressure are not both fixed; one can vary one of them and the other will adjust.

## 28.6 Colligative properties

Colligative properties are properties of solutions that depend only on the number of solute particles, not on their identity. Examples include:

- Boiling point elevation: $\Delta T_b = K_b m$, where $m$ is the molality of the solute.
- Freezing point depression: $\Delta T_f = K_f m$.
- Osmotic pressure: $\Pi = nRT/V$, where $n$ is the number of moles of solute.

These properties arise because the chemical potential of the solvent is lowered by the presence of the solute, which shifts the phase equilibrium.

## Example 28.4

Calculate the freezing point depression of water when 1 mol of NaCl is dissolved in 1 kg of water. (For water, $K_f = 1.86 \, \text{K kg mol}^{-1}$.)

Solution: NaCl dissociates into two ions, so the effective molality is $m = 2 \, \text{mol kg}^{-1}$. Then,

$$\Delta T_f = K_f m = 1.86 \times 2 = 3.72 \, \text{K}. \quad (28.20)$$

So the freezing point is depressed by $3.72^\circ \text{C}$.

## 28.7 Classification of phase transitions

Phase transitions are classified according to the behaviour of the thermodynamic potentials. A first-order phase transition has a discontinuity in the first derivative of the Gibbs free energy (e.g., a discontinuity in entropy and volume). This means that the latent heat is non-zero and the volume changes discontinuously. Examples include melting, boiling, and sublimation.

A second-order phase transition has a continuous first derivative but a discontinuity in the second derivative (e.g., a discontinuity in heat capacity or compressibility). Examples include the ferromagnetic transition (Curie point) and the superfluid transition.

## 28.8 The Ising model

The Ising model is a simple model of a phase transition. It consists of a lattice of spins $s_i = \pm 1$ (corresponding to up or down magnetic moments). The energy of a configuration is

$$E = -J \sum_{\langle i,j \rangle} s_i s_j - B \sum_i s_i, \quad (28.21)$$

where $J$ is the exchange interaction (positive for ferromagnetic, negative for antiferromagnetic), the sum is over nearest-neighbour pairs, and $B$ is an external magnetic field. The partition function of the Ising model can be solved exactly in one and two dimensions. In two dimensions, it exhibits a phase transition at a critical temperature $T_c$ given by

$$\frac{k_B T_c}{J} = \frac{2}{\ln(1 + \sqrt{2})} \approx 2.269. \quad (28.22)$$

Below $T_c$, the system develops a spontaneous magnetization.

## Chapter summary

- The Clausius-Clapeyron equation is $\frac{dp}{dT} = \frac{L}{T \Delta V}$.
- The Gibbs phase rule is $F = C - P + 2$.
- Colligative properties depend only on the number of solute particles.
- Phase transitions are classified as first-order or second-order depending on the behaviour of the Gibbs free energy.
- The Ising model is a simple model of a ferromagnetic phase transition.

## Exercises

(28.1) Show that the Clausius-Clapeyron equation can be written as $\frac{d \ln p}{dT} = \frac{L}{R T^2}$ for a liquid-gas transition.

(28.2) Calculate the slope of the melting curve of ice at $0^\circ \text{C}$, given that the latent heat of fusion is $L = 3.33 \times 10^5 \, \text{J kg}^{-1}$, the density of ice is $916 \, \text{kg m}^{-3}$, and the density of water is $1000 \, \text{kg m}^{-3}$.

(28.3) Explain why the freezing point of a solution is lower than that of the pure solvent.

(28.4) Derive the expression for the osmotic pressure of a dilute solution: $\Pi = nRT/V$.

(28.5) For the Ising model in one dimension, show that there is no phase transition at finite temperature (i.e., $T_c = 0$). (Hint: calculate the partition function and show that the free energy is analytic for all $T > 0$.)

===== Page 345 =====

# 29 Bose-Einstein and Fermi-Dirac distributions

29.1 Exchange and symmetry  345
29.2 Wave functions of identical particles  346
29.3 The statistics of identical particles  349
Chapter summary  353
Further reading  353
Exercises  354

In Chapter 21, we considered the statistical mechanics of an ideal gas of classical particles, which are distinguishable and obey the Boltzmann distribution. However, in quantum mechanics, particles of the same type are indistinguishable. This leads to two possible types of quantum statistics: Bose-Einstein statistics (for bosons) and Fermi-Dirac statistics (for fermions). In this chapter, we will derive the Bose-Einstein and Fermi-Dirac distributions and discuss their properties.

## 29.1 Exchange and symmetry

In quantum mechanics, the wave function of a system of identical particles must be either symmetric or antisymmetric under the exchange of any two particles. Particles with symmetric wave functions are called bosons, and they have integer spin (0, 1, 2, ...). Particles with antisymmetric wave functions are called fermions, and they have half-integer spin ($\frac{1}{2}, \frac{3}{2}, \ldots$). This is the spin-statistics theorem.

For two identical particles, the wave function is either

$$\psi(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\mathbf{r}_1)\phi_b(\mathbf{r}_2) + \phi_b(\mathbf{r}_1)\phi_a(\mathbf{r}_2)] \quad \text{(bosons)}, \quad (29.1)$$

or

$$\psi(\mathbf{r}_1, \mathbf{r}_2) = \frac{1}{\sqrt{2}} [\phi_a(\mathbf{r}_1)\phi_b(\mathbf{r}_2) - \phi_b(\mathbf{r}_1)\phi_a(\mathbf{r}_2)] \quad \text{(fermions)}. \quad (29.2)$$

For fermions, if $a = b$, the wave function vanishes. This is the Pauli exclusion principle: two fermions cannot occupy the same quantum state.

## 29.2 Wave functions of identical particles

For a system of $N$ identical particles, the wave function is a sum over all permutations of the particles. For bosons, the wave function is symmetric under exchange, so we sum over all permutations with a plus sign. For fermions, the wave function is antisymmetric, so we sum over all permutations with a sign equal to the parity of the permutation (the Slater determinant).

The occupation numbers $n_i$ describe how many particles are in each quantum state. For bosons, any number of particles can occupy the same state ($n_i = 0, 1, 2, \ldots$). For fermions, each state can be occupied by at most one particle ($n_i = 0$ or 1).

## 29.3 The statistics of identical particles

We can derive the probability distribution for the occupation numbers by maximizing the entropy subject to the constraints of fixed total energy and fixed total number of particles. The result is

- For bosons:

$$\bar{n}_i = \frac{1}{e^{\beta(E_i - \mu)} - 1}. \quad (29.3)$$

- For fermions:

$$\bar{n}_i = \frac{1}{e^{\beta(E_i - \mu)} + 1}. \quad (29.4)$$

- In the classical limit (when the gas is dilute, so that $\bar{n}_i \ll 1$), both distributions reduce to the Boltzmann distribution:

$$\bar{n}_i \approx e^{-\beta(E_i - \mu)}. \quad (29.5)$$

The Bose-Einstein distribution is characterized by the fact that $\bar{n}_i$ can be greater than 1. In fact, as $E_i \to \mu$, the occupancy diverges. This leads to the phenomenon of Bose-Einstein condensation, which we will discuss in Chapter 30.

The Fermi-Dirac distribution is characterized by the fact that $\bar{n}_i \le 1$. At zero temperature, all states with $E_i < \mu$ are occupied, and all states with $E_i > \mu$ are empty. The chemical potential at zero temperature is called the Fermi energy $E_F$.

## Example 29.1

Show that in the classical limit, both the Bose-Einstein and Fermi-Dirac distributions reduce to the Boltzmann distribution.

Solution: In the classical limit, $\bar{n}_i \ll 1$, so $e^{\beta(E_i - \mu)} \gg 1$. Then,

$$\bar{n}_i \approx \frac{1}{e^{\beta(E_i - \mu)}} = e^{-\beta(E_i - \mu)}. \quad (29.6)$$

This is the Boltzmann distribution.

## Chapter summary

- Bosons have symmetric wave functions and obey Bose-Einstein statistics: $\bar{n}_i = \frac{1}{e^{\beta(E_i - \mu)} - 1}$.
- Fermions have antisymmetric wave functions and obey Fermi-Dirac statistics: $\bar{n}_i = \frac{1}{e^{\beta(E_i - \mu)} + 1}$.
- In the classical limit, both distributions reduce to the Boltzmann distribution.
- The Pauli exclusion principle states that two fermions cannot occupy the same quantum state.

## Exercises

(29.1) Show that for a Fermi gas at zero temperature, the average occupancy is $\bar{n}_i = 1$ for $E_i < E_F$ and $0$ for $E_i > E_F$, where $E_F$ is the Fermi energy.

(29.2) For a Bose gas, show that the chemical potential $\mu$ must be less than the lowest energy level.

(29.3) Derive the expression for the average occupation number $\bar{n}_i$ for bosons by maximizing the entropy $S = -k_B \sum_i [n_i \ln n_i - (1 + n_i) \ln(1 + n_i)]$ subject to the constraints $\sum_i n_i = N$ and $\sum_i n_i E_i = U$.

(29.4) Derive the expression for the average occupation number $\bar{n}_i$ for fermions by maximizing the entropy $S = -k_B \sum_i [n_i \ln n_i + (1 - n_i) \ln(1 - n_i)]$ subject to the same constraints.

(29.5) Show that the entropy of a Fermi gas can be written as $S = -k_B \sum_i [\bar{n}_i \ln \bar{n}_i + (1 - \bar{n}_i) \ln(1 - \bar{n}_i)]$.

===== Page 358 =====

# 30 Quantum gases and condensates

30.1 The non-interacting quantum fluid  358
30.2 The Fermi gas  361
30.3 The Bose gas  366
30.4 Bose-Einstein condensation (BEC)  367
Chapter summary  373
Further reading  373
Exercises  373

In this chapter, we apply the quantum distributions derived in Chapter 29 to ideal gases of fermions and bosons. We will see that the behaviour of these gases is very different from the classical ideal gas, especially at low temperatures. We will derive the properties of the Fermi gas (which is important for understanding metals, white dwarfs, and neutron stars) and the Bose gas (which exhibits Bose-Einstein condensation at low temperatures).

## 30.1 The non-interacting quantum fluid

We consider a gas of $N$ non-interacting identical particles in a volume $V$. The single-particle energy levels are given by

$$E = \frac{\hbar^2 k^2}{2m}, \quad (30.1)$$

for non-relativistic particles. The density of states (including spin degeneracy $g_s = 2s + 1$) is

$$g(E) dE = \frac{g_s V}{4\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2} dE. \quad (30.2)$$

The total number of particles is

$$N = \int_0^\infty g(E) \bar{n}(E) dE, \quad (30.3)$$

and the internal energy is

$$U = \int_0^\infty E g(E) \bar{n}(E) dE, \quad (30.4)$$

where $\bar{n}(E)$ is either the Fermi-Dirac or the Bose-Einstein distribution.

## 30.2 The Fermi gas

For a Fermi gas, $\bar{n}(E) = \frac{1}{e^{\beta(E - \mu)} + 1}$. At zero temperature, the distribution is a step function: $\bar{n}(E) = 1$ for $E < E_F$ and $0$ for $E > E_F$, where $E_F$ is the Fermi energy. The Fermi energy is determined by

$$N = \int_0^{E_F} g(E) dE = \frac{g_s V}{4\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \frac{2}{3} E_F^{3/2}. \quad (30.5)$$

Solving for $E_F$,

$$E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}, \quad (30.6)$$

where $n = N/V$ is the number density.

The total energy at zero temperature is

$$U_0 = \int_0^{E_F} E g(E) dE = \frac{3}{5} N E_F. \quad (30.7)$$

The pressure at zero temperature is

$$p_0 = \frac{2}{5} n E_F. \quad (30.8)$$

This is the degeneracy pressure of a Fermi gas. It is a purely quantum mechanical effect, arising from the Pauli exclusion principle.

## Example 30.1

Calculate the Fermi energy of electrons in a metal, assuming $n \approx 10^{28} \, \text{m}^{-3}$.

Solution: Using eqn 30.6 with $g_s = 2$,

$$E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}. \quad (30.9)$$

Substituting the values,

$$E_F \approx \frac{(1.055 \times 10^{-34})^2}{2 \times 9.11 \times 10^{-31}} (3\pi^2 \times 10^{28})^{2/3} \approx 1.1 \times 10^{-18} \, \text{J} \approx 7 \, \text{eV}. \quad (30.10)$$

This is the characteristic energy scale of electrons in metals.

## 30.3 The Bose gas

For a Bose gas, $\bar{n}(E) = \frac{1}{e^{\beta(E - \mu)} - 1}$. The chemical potential $\mu$ must be less than the lowest energy level (which we take as 0). As the temperature is lowered, $\mu$ increases towards 0. At a critical temperature $T_c$, the chemical potential reaches 0, and the occupation of the ground state becomes macroscopic. This is Bose-Einstein condensation.

The critical temperature is given by

$$k_B T_c = \frac{2\pi \hbar^2}{m} \left(\frac{n}{g_s \zeta(3/2)}\right)^{2/3}, \quad (30.11)$$

where $\zeta(3/2) \approx 2.612$ is the Riemann zeta function.

Below $T_c$, a fraction of the particles occupy the ground state:

$$\frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^{3/2}. \quad (30.12)$$

The internal energy below $T_c$ is

$$U = \frac{3}{2} N k_B T \frac{\zeta(5/2)}{\zeta(3/2)} \left(\frac{T}{T_c}\right)^{3/2}. \quad (30.13)$$

The heat capacity has a cusp at $T_c$, which is characteristic of a phase transition.

## 30.4 Bose-Einstein condensation (BEC)

Bose-Einstein condensation was first observed in 1995 in dilute atomic gases (rubidium, sodium, and lithium) at temperatures below about 1 microkelvin. The condensate is a macroscopic quantum state, in which all the atoms occupy the same quantum state. This is a fascinating phenomenon that has led to many important discoveries, including the observation of superfluidity, vortices, and atom lasers.

## Chapter summary

- The Fermi energy is $E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}$.
- The degeneracy pressure of a Fermi gas is $p_0 = \frac{2}{5} n E_F$.
- Bose-Einstein condensation occurs below a critical temperature $T_c = \frac{2\pi \hbar^2}{m k_B} \left(\frac{n}{g_s \zeta(3/2)}\right)^{2/3}$.
- Below $T_c$, a macroscopic fraction of the particles occupy the ground state.

## Exercises

(30.1) Show that the density of states for a gas of non-relativistic particles is $g(E) = \frac{g_s V}{4\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2}$.

(30.2) Derive the expression for the Fermi energy $E_F = \frac{\hbar^2}{2m} (3\pi^2 n)^{2/3}$.

(30.3) Calculate the Fermi energy and the degeneracy pressure of electrons in a white dwarf star, assuming $n \approx 10^{36} \, \text{m}^{-3}$.

(30.4) Show that the heat capacity of a Fermi gas at low temperatures is $C_V = \frac{\pi^2}{2} N k_B \frac{T}{T_F}$, where $T_F = E_F/k_B$ is the Fermi temperature.

(30.5) Derive the expression for the critical temperature of Bose-Einstein condensation: $k_B T_c = \frac{2\pi \hbar^2}{m} \left(\frac{n}{g_s \zeta(3/2)}\right)^{2/3}$.

(30.6) Show that below $T_c$, the fraction of particles in the ground state is $N_0/N = 1 - (T/T_c)^{3/2}$.
