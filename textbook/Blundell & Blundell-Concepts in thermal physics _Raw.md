===== Page 1 =====

# Concepts in Thermal Physics Second edition

[Image: Cover page showing three spheres. The largest is a transparent sphere with a grid of 0s and 1s on its surface. In front of it is a sphere with a red metallic piston mechanism inside. Behind them is a third small sphere showing the Earth. To the right, the equation S = -k_B ∑ P_i ln P_i is written. The authors' names are at the bottom right.]

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

0XFORDBUNIVERSITY PRESSGreat Clarendon Street, Oxford OX2 6DPOxford University Press is a department of the University of Oxford. It furthers the University's objective of excellence in research, scholarship, and education by publishing worldwide inOxford New YorkAuckland Cape Town Dar es Salaam Hong Kong KarachiKuala Lumpur Madrid Melbourne Mexico City NairobiNew Delhi Shanghai Taipei TorontoWith offices inArgentina Austria Brazil Chile Czech Republic France Greece Guatemala Hungary Italy Japan Poland Portugal SingaporeSouth Korea Switzerland Thailand Turkey Ukraine VietnamOxford is a registered trade mark of Oxford University Press in the UK and in certain other countriesPublished in the United States by Oxford University Press Inc., New York© Stephen J. Blundell and Katherine M. Blundell 2010The moral rights of the authors have been assertedDatabase right Oxford University Press (maker)First edition published in 2006Second edition published in 2010All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, without the prior permission in writing of Oxford University Press, or as expressly permitted by law, or under terms agreed with the appropriate reprographics rights organization. Enquiries concerning reproduction outside the scope of the above should be sent to the Rights Department, Oxford University Press, at the address aboveYou must not circulate this book in any other binding or cover and you must impose the same condition on any acquirerBritish Library Cataloguing in Publication DataData availableLibrary of Congress Cataloging in Publication DataData availablePrinted in Great Britainon acid- free paper byCPI Antony Rowe, Chippenham, Wilts.ISBN 978- 0- 19- 956209- 1 (Hbk.)ISBN 978- 0- 19- 956210- 7 (Pbk.)10987654321

===== Page 6 =====

1

===== Page 7 =====

This page intentionally left blank

===== Page 8 =====

 In the beginning was the Word...

(John 1:1, first century AD)

Consider sunbeams. When the sun's rays let in Pass through the darkness of a shuttered room, You will see a multitude of tiny bodies All mingling in a multitude of ways Inside the sunbeam, moving in the void, Seeming to be engaged in endless strife, Battle, and warfare, troop attacking troop, And never a respite, harried constantly, With meetings and with partings everywhere. From this you can imagine what it is For atoms to be tossed perpetually In endless motion through the mighty void.

(On the Nature of Things, Lucretius, first century BC)

... (we) have borne the burden of the work and the heat of the day. (Matthew 20:12, first century AD)

[Image: A sphere covered in a grid of squares. Each square contains a single digit, either a 0 or a 1.]

Thermal physics forms a key part of any undergraduate physics course. It includes the fundamentals of classical thermodynamics (which was founded largely in the nineteenth century and motivated by a desire to understand the conversion of heat into work using engines) and also statistical mechanics (which was founded by Boltzmann and Gibbs, and is concerned with the statistical behaviour of the underlying microstates of the system). Students often find these topics hard, and this problem is not helped by a lack of familiarity with basic concepts in mathematics, particularly in probability and statistics. Moreover, the traditional focus of thermodynamics on steam engines seems remote and largely irrelevant to a twenty- first century student. This is unfortunate since an understanding of thermal physics is crucial to almost all modern physics and to the important technological challenges which face us in this century.

The aim of this book is to provide an introduction to the key concepts in thermal physics, fleshed out with plenty of modern examples from astrophysics, atmospheric physics, laser physics, condensed matter physics and information theory. The important mathematical principles, particularly concerning probability and statistics, are expounded in some detail. This aims to make up for the material which can no longer be automatically assumed to have been covered in every school

===== Page 9 =====

 mathematics course. In addition, the appendices contain useful mathematics, such as various integrals, mathematical results and identities. There is, unfortunately, no shortcut to mastering the necessary mathematics in studying thermal physics, but the material in the appendix provides a useful aide- mémoire.

Many courses on this subject are taught historically: the kinetic theory of gases, then classical thermodynamics are taught first, with statistical mechanics taught last. In other courses, one starts with the principles of classical thermodynamics, followed then by statistical mechanics and kinetic theory is saved until the end. Although there is merit in both approaches, we have aimed at a more integrated treatment. For example, we introduce temperature using a straightforward statistical mechanical argument, rather than on the basis of a somewhat abstract Carnot engine. However, we do postpone detailed consideration of the partition function and statistical mechanics until after we have introduced the functions of state, which manipulation of the partition function so conveniently produces. We present the kinetic theory of gases fairly early on, since it provides a simple, well- defined arena in which to practise simple concepts in probability distributions. This has worked well in the course given in Oxford, but since kinetic theory is only studied at a later stage in courses in other places, we have designed the book so that the kinetic theory chapters can be omitted without causing problems; see Fig. 1.5 on page 10 for details. In addition, some parts of the book contain material that is much more advanced (often placed in boxes, or in the final part of the book), and these can be skipped at first reading.

The book is arranged in a series of short, easily digestible chapters, each one introducing a new concept or illustrating an important application. Most people learn from examples, so plenty of worked examples are given in order that the reader can gain familiarity with the concepts as they are introduced. Exercises are provided at the end of each chapter to allow the students to gain practice in each area.

In choosing which topics to include, and at what level, we have aimed for a balance between pedagogy and rigour, providing a comprehensible introduction with sufficient details to satisfy more advanced readers. We have also tried to balance fundamental principles with practical applications. However, this book does not treat real engines in any engineering depth, nor does it venture into the deep waters of ergodic theory. Nevertheless, we hope that there is enough in this book for a thorough grounding in thermal physics and the recommended further reading gives pointers for additional material. An important theme running through this book is the concept of information, and its connection with entropy. The black hole shown at the start of this preface, with its surface covered in 'bits' of information, is a helpful picture of the deep connection between information, thermodynamics, radiation, and the Universe.

The history of thermal physics is a fascinating one, and we have provided a selection of short biographical sketches of some of the key pioneers in thermal physics. To qualify for inclusion, the person had to

===== Page 10 =====

ive made a particularly important contribution or had a particularly interesting life - and be dead! Therefore one should not conclude from the list of people we have chosen that the subject of thermal physics is in any sense finished, it is just harder to write with the same perspective about current work in this subject. The biographical sketches are necessarily brief, giving only a glimpse of the life- story, so the Bibliography should be consulted for a list of more comprehensive biographies. However, the sketches are designed to provide some light relief in the main narrative and demonstrate that science is a human endeavour.

It is a great pleasure to record our gratitude to those who taught us the subject while we were undergraduates in Cambridge, particularly Owen Saxton and Peter Scheuer, and to our friends in Oxford: we have benefitted from many enlightening discussions with colleagues in the physics department, from the intelligent questioning of our Oxford students and from the stimulating environments provided by both Mansfield College and St John's College. In the writing of this book, we have enjoyed the steadfast encouragement of Sonke Adlung and his colleagues at OUP, and in particular Julie Harris' black- belt \(\mathrm{BTEX}\) support.

A number of friends and colleagues in Oxford and elsewhere have been kind enough to give their time and read drafts of chapters of this book; they have made numerous helpful comments, which have greatly improved the final result: Fathallah Alouani Bibi, James Analytis, David Andrews, Arzhang Ardavan, Tony Beasley, Michael Bowler, Peter Duffy, Paul Goddard, Stephen Justham, Michael Mackey, Philipp Podsiadlowski, Linda Schmidtobreick, John Singleton and Katrien Steenbrugge. Particular thanks are due to Tom Lancaster, who twice read the entire manuscript at early stages and made many constructive and imaginative suggestions, and to Harvey Brown, whose insights were always stimulating and whose encouragement was always constant. To all these friends, our warmest thanks are due. Errors which we discover after going to press will be posted on the book's website, which may be found at:

http://users.ox.ac.uk/\~sjb/ctp

It is our earnest hope that this book will make the study of thermal physics enjoyable and fascinating and that we have managed to communicate something of the enthusiasm we feel for this subject. Moreover, understanding the concepts of thermal physics is vital for humanity's future; the impending energy crisis and the potential consequences of climate change mandate creative, scientific, and technological innovations at the highest levels. This means that thermal physics is a field that some of tomorrow's best minds need to master today.

SJB & KMB Oxford June 2006

===== Page 11 =====

1

## Preface to the second edition

This new edition keeps the same structure as the first edition but includes additional material on probability, Bayes' theorem, diffusion problems, osmosis, the Ising model, Monte- Carlo simulations, and radiative transfer in atmospheric physics. We have also taken the opportunity to improve the treatment of various topics, including the discussion of constraints and the presentation of the Fermi- Dirac and Bose- Einstein distributions, as well as correcting various errors. We are particularly grateful to the following people who have pointed out errors or omissions and made highly relevant comments: David Andrews, John Aveson, Ryan Buckingham, Radu Coldea, Merlin Cooper, Peter Coulon, Peter Duffy, Ted Einstein, Joe Fallon, Amy Fok, Felix Flicker, William Frass, Andrew Garner, Paul Hennin, Ben Jones, Stephen Justham, Austen Lamacraft, Peter Liley, Gabriel McManus, Adam Micolich, Robin Moss, Alan O'Neill, Elena Nickson, Wilson Poon, Caity Rice, Andrew Steane, Nicola van Leeuwen, Yan Mei Wang, Peter Watson, Helena Wilding, and Michael Williams. We have once again enjoyed the support of the staff of OUP and, in particular, our copy- editor Alison Lees, who trawled through the manuscript with meticulous care, making many important improvements. Myles Allen, David Andrews, and William Ingram gave us very pertinent and instructive comments about the treatment of atmospheric physics and their input has been invaluable. Thanks are also due to Geoff Brooker, who shared his profound insights into the nature of free energies, and Tom Lancaster, who once again made numerous helpful suggestions.

SJB & KMB Oxford August 2009

===== Page 12 =====

1 Introduction 2 1.1 What is a mole? 3 1.2 The thermodynamic limit 4 1.3 The ideal gas 6 1.4 Combinatorial problems 7 1.5 Plan of the book 9 Exercises 12 2 Heat 13 2.1 A definition of heat 13 2.2 Heat capacity 14 Exercises 17 3 Probability 18 3.1 Discrete probability distributions 19 3.2 Continuous probability distributions 20 3.3 Linear transformation 21 3.4 Variance 22 3.5 Linear transformation and the variance 23 3.6 Independent variables 24 3.7 Binomial distribution 26 Further reading 29 Exercises 29 4 Temperature and the Boltzmann factor 32 4.1 Thermal equilibrium 32 4.2 Thermometers 33 4.3 The microstates and macrostates 35 4.4 A statistical definition of temperature 36 4.5 Ensembles 38 4.6 Canonical ensemble 38 4.7 Applications of the Boltzmann distribution 42 Further reading 46 Exercises 46

===== Page 13 =====

47

5 The Maxwell- Boltzmann distribution 48

5.1 The velocity distribution 48  5.2 The speed distribution 49  5.3 Experimental justification 51  Exercises 54

6 Pressure 56  6.1 Molecular distributions 57  6.2 The ideal gas law 58  6.3 Dalton's law 60  Exercises 61

7 Molecular effusion 64

7.1 Flux 64  7.2 Effusion 66  Exercises 69

8 The mean free path and collisions 70

8.1 The mean collision time 70  8.2 The collision cross- section 71  8.3 The mean free path 73  Exercises 74

III Transport and thermal diffusion 75

9 Transport properties in gases 76

9.1 Viscosity 76  9.2 Thermal conductivity 81  9.3 Diffusion 83  9.4 More detailed theory 86  Further reading 88  Exercises 89

10 The thermal diffusion equation 90

10.1 Derivation of the thermal diffusion equation 90  10.2 The one- dimensional thermal diffusion equation 91  10.3 The steady state 94  10.4 The thermal diffusion equation for a sphere 94  10.5 Newton's law of cooling 99  10.6 The Prandtl number 100  10.7 Sources of heat 101  10.8 Particle diffusion 102  Exercises 103

===== Page 14 =====

107

11 Energy 108 11.1 Some definitions 108 11.2 The first law of thermodynamics 110 11.3 Heat capacity 112 Exercises 115

12 Isothermal and adiabatic processes 118 12.1 Reversibility 118 12.2 Isothermal expansion of an ideal gas 120 12.3 Adiabatic expansion of an ideal gas 121 12.4 Adiabatic atmosphere 121 Exercises 123

V The second law 125

13 Heat engines and the second law 126 13.1 The second law of thermodynamics 126 13.2 The Carnot engine 127 13.3 Carnot's theorem 130 13.4 Equivalence of Clausius' and Kelvin's statements 131 13.5 Examples of heat engines 131 13.6 Heat engines running backwards 133 13.7 Clausius' theorem 134 Further reading 137 Exercises 137

14 Entropy 140 14.1 Definition of entropy 140 14.2 Irreversible change 140 14.3 The first law revisited 142 14.4 The Joule expansion 144 14.5 The statistical basis for entropy 146 14.6 The entropy of mixing 147 14.7 Maxwell's demon 149 14.8 Entropy and probability 150 Exercises 153

15 Information theory 157 15.1 Information and Shannon entropy 157 15.2 Information and thermodynamics 159 15.3 Data compression 160 15.4 Quantum information 162 15.5 Conditional and joint probabilities 165 15.6 Bayes' theorem 165 Further reading 168 Exercises 169

===== Page 15 =====

171

16 Thermodynamic potentials 172

16 Thermodynamic potentials 17216.1 Internal energy, \(U\) 17216.2 Enthalpy, \(H\) 17316.3 Helmholtz function, \(F\) 17416.4 Gibbs function, \(G\) 17516.5 Constraints 17616.6 Maxwell's relations 179Exercises 187

17 Rods, bubbles, and magnets 191

17 Rods, bubbles, and magnets 19117.1 Elastic rod 19117.2 Surface tension 19417.3 Electric and magnetic dipoles 19517.4 Paramagnetism 196Exercises 201

18 The third law 20318.1 Different statements of the third law 20318.2 Consequences of the third law 205Exercises 208

VII Statistical mechanics 209

19 Equipartition of energy 210

19 Equipartition of energy 21019.1 Equipartition theorem 21019.2 Applications 21319.3 Assumptions made 21519.4 Brownian motion 217Exercises 218

20 The partition function 219

20 The partition function 21920.1 Writing down the partition function 22020.2 Obtaining the functions of state 22120.3 The big idea 22820.4 Combining partition functions 228Exercises 232

21 Statistical mechanics of an ideal gas 233

21 Statistical mechanics of an ideal gas 23321.1 Density of states 23321.2 Quantum concentration 23521.3 Distinguishability 23621.4 Functions of state of the ideal gas 23721.5 Gibbs paradox 24021.6 Heat capacity of a diatomic gas 241Exercises 243

===== Page 16 =====

22 The chemical potential 244 22.1 A definition of the chemical potential 244 22.2 The meaning of the chemical potential 245 22.3 Grand partition function 247 22.4 Grand potential 248 22.5 Chemical potential as Gibbs function per particle 250 22.6 Many types of particle 250 22.7 Particle number conservation laws 251 22.8 Chemical potential and chemical reactions 252 22.9 Osmosis 257 Further reading 261 Exercises 262

# 23 Photons

# 263

23 Photons 263 23.1 The classical thermodynamics of electromagnetic radiation 264 23.2 Spectral energy density 265 23.3 Kirchhoff's law 266 23.4 Radiation pressure 268 23.5 The statistical mechanics of the photon gas 269 23.6 Black- body distribution 270 23.7 Cosmic microwave background radiation 273 23.8 The Einstein A and B coefficients 274 Further reading 277 Exercises 278

# 24 Phonons

# 279

24 Phonons 279 24.1 The Einstein model 279 24.2 The Debye model 281 24.3 Phonon dispersion 284 Further reading 287 Exercises 287

# VIII Beyond the ideal gas

# 289

# 25 Relativistic gases

25 Relativistic gases 290 25.1 Relativistic dispersion relation for massive particles 290 25.2 The ultrarelativistic gas 290 25.3 Adiabatic expansion of an ultrarelativistic gas 293 Exercises 295

# 26 Real gases

26 Real gases 296 26.1 The van der Waals gas 296 26.2 The Dieterici equation 304 26.3 Virial expansion 306 26.4 The law of corresponding states 310 Exercises 312

===== Page 17 =====

27 Cooling real gases 313 27.1 The Joule expansion 313 27.2 Isothermal expansion 315 27.3 Joule- Kelvin expansion 316 27.4 Liquefaction of gases 318 Exercises 320

# 28 Phase transitions 321

28 Phase transitions 321 28.1 Latent heat 321 28.2 Chemical potential and phase changes 324 28.3 The Clausius- Clapeyron equation 324 28.4 Stability and metastability 329 28.5 The Gibbs phase rule 332 28.6 Colligative properties 334 28.7 Classification of phase transitions 335 28.8 The Ising model 338 Further reading 343 Exercises 343

# 29 Bose-Einstein and Fermi-Dirac distributions 345

29 Bose- Einstein and Fermi- Dirac distributions 345 29.1 Exchange and symmetry 345 29.2 Wave functions of identical particles 346 29.3 The statistics of identical particles 349 Further reading 353 Exercises 354

# 30 Quantum gases and condensates 358

30 Quantum gases and condensates 358 30.1 The non- interacting quantum fluid 358 30.2 The Fermi gas 361 30.3 The Bose gas 366 30.4 Bose- Einstein condensation (BEC) 367 Further reading 373 Exercises 373

# IX Special topics 375

# 31 Sound waves 376

31 Sound waves 376 31.1 Sound waves under isothermal conditions 377 31.2 Sound waves under adiabatic conditions 377 31.3 Are sound waves in general adiabatic or isothermal? 378 31.4 Derivation of the speed of sound within fluids 379 Further reading 382 Exercises 382

# 32 Shock waves 383

32 Shock waves 383 32.1 The Mach number 383 32.2 Structure of shock waves 383 32.3 Shock conservation laws 385

===== Page 18 =====

32.4 The Rankine- Hugoniot conditions 386  Further reading 389  Exercises 389

# 33 Brownian motion and fluctuations 390

33 Brownian motion and fluctuations 390  33.1 Brownian motion 390  33.2 Johnson noise 393  33.3 Fluctuations 394  33.4 Fluctuations and the availability 395  33.5 Linear response 397  33.6 Correlation functions 400  Further reading 407  Exercises 407

# 34 Non-equilibrium thermodynamics 408

34 Non- equilibrium thermodynamics 408  34.1 Entropy production 408  34.2 The kinetic coefficients 409  34.3 Proof of the Onsager reciprocal relations 410  34.4 Thermoelectricity 413  34.5 Time reversal and the arrow of time 417  Further reading 419  Exercises 419

# 35 Stars 420

35 Stars 420  35.1 Gravitational interaction 421  35.2 Nuclear reactions 426  35.3 Heat transfer 427  Further reading 434  Exercises 434

# 36 Compact objects 435

36 Compact objects 435  36.1 Electron degeneracy pressure 435  36.2 White dwarfs 437  36.3 Neutron stars 438  36.4 Black holes 440  36.5 Accretion 441  36.6 Black holes and entropy 442  36.7 Life, the Universe, and entropy 443  Further reading 445  Exercises 445

# 37 Earth's atmosphere 446

37 Earth's atmosphere 446  37.1 Solar energy 446  37.2 The temperature profile in the atmosphere 447  37.3 Radiative transfer 449  37.4 The greenhouse effect 452  37.5 Global warming 456  Further reading 460  Exercises 460

===== Page 19 =====

461 A Fundamental constants 461 B Useful formulae 462 C Useful mathematics 464 C.1 The factorial integral 464 C.2 The Gaussian integral 464 C.3 Stirling's formula 467 C.4 Riemann zeta function 469 C.5 The polylogarithm 470 C.6 Partial derivatives 471 C.7 Exact differentials 472 C.8 Volume of a hypersphere 473 C.9 Jacobians 473 C.10 The Dirac delta function 475 C.11 Fourier transforms 475 C.12 Solution of the diffusion equation 476 C.13 Lagrange multipliers 477 D The electromagnetic spectrum 479 E Some thermodynamical definitions 480 F Thermodynamic expansion formulae 481 G Reduced mass 482 H Glossary of main symbols 483 Bibliography 485 Index 489

===== Page 20 =====

1

# Preliminaries

To explore and understand the rich and beautiful subject that is thermal physics, we need some essential tools in place. Part I provides these, as follows:

In Chapter 1 we explore the concept of large numbers, showing why large numbers appear in thermal physics and explaining how to handle them. Large numbers arise in thermal physics because the number of atoms in the bit of matter under study is usually very large (for example, it can be typically of the order of \(10^{23}\) ), but also because many thermal physics problems involve combinatorial calculations (and this can produce numbers like \(10^{23}\) !, where "!" here means a factorial). We introduce Stirling's approximation, which is useful for handling expressions, such as \(\ln N!\) , which frequently appear in thermal physics. We discuss the thermodynamic limit and state the ideal gas equation (derived later, in Chapter 6, from the kinetic theory of gases). In Chapter 2 we explore the concept of heat, defining it as "thermal energy in transit", and introduce the idea of a heat capacity. The ways in which thermal systems behave is determined by the laws of probability, so we outline the notion of probability in Chapter 3 and apply it to a number of problems. This chapter may well cover ground that is familiar to some readers, but is a useful introduction to the subject. We then use these ideas to define the temperature of a system from a statistical perspective and hence derive the Boltzmann distribution in Chapter 4. This distribution describes how a thermal system behaves when it is placed in thermal contact with a large thermal reservoir. This is a key concept in thermal physics and forms the basis of all that follows.

===== Page 21 =====

1 Introduction

1.1 What is a mole? 3 1.2 The thermodynamic limit 4 1.3 The ideal gas 6 1.4 Combinatorial problems 7 1.5 Plan of the book 9 Chapter summary 12 Exercises 12

Some large numbers:

<table>million106billion109trillion1012quadrillion1015quintillion1018googol10100googolplex1010100</table>

Note: these values assume the US billion, trillion, etc, which are now in general use.

The subject of thermal physics involves studying assemblies of large numbers of atoms. As we will see, it is the large numbers involved in macroscopic systems that allow us to treat some of their properties in a statistical fashion. What do we mean by a large number?

Large numbers turn up in many spheres of life. A book might sell a million \((10^{6})\) copies (probably not this one), the Earth's population is (at the time of writing) between six and seven billion people \((6 - 7\times 10^{9})\) , and the US national debt is currently around ten trillion dollars \((10^{13}\) US\\$). But even these large numbers pale into insignificance compared with the numbers involved in thermal physics. The number of atoms in an average- sized piece of matter is usually ten to the power of twentysomething, and this puts extreme limits on what sort of calculations we can make to understand them.

## Example 1.1

One kilogramme of nitrogen gas contains approximately \(2\times 10^{25}\mathrm{N}_{2}\) molecules. Let us see how easy it would be to make predictions about the motion of the molecules in this amount of gas. In one year, there are about \(3.2\times 10^{7}\) seconds, so that a 3 GHz personal computer can count molecules at a rate of roughly \(10^{17}\) year \(^{- 1}\) , if it counts one molecule every computer clock cycle. Therefore it would take about 0.2 billion years just for this computer to count all the molecules in one kilogramme of nitrogen gas (a time that is roughly a few percent of the age of the Universe!). Counting the molecules is a computationally simpler task than calculating all their movements and collisions with each other. Therefore modelling this quantity of matter by following each and every particle is a hopeless task.

Hence, to make progress in thermal physics it is necessary to make approximations and deal with the statistical properties of molecules, i.e., to study how they behave on average. Chapter 3 therefore contains a discussion of probability and statistical methods, which are foundational for understanding thermal physics. In this chapter, we will briefly review the definition of a mole (which will be used throughout the book), consider why very big numbers arise from combinatorial problems in thermal physics and introduce the thermodynamic limit and the ideal gas equation.

===== Page 22 =====

1.1 What is a mole?

A mole is, of course, a small burrowing animal, but also a name (first coined about a century ago from the German "Molekil" [molecule]) representing a certain numerical quantity of stuff. It functions in the same way as the word "dozen", which describes a certain number of eggs (12), or "score", which describes a certain number of years (20). It might be easier if we could use the word dozen when describing a certain number of atoms, but a dozen atoms is not many (unless you are building a quantum computer) and since a million, a billion, and even a quadrillion are also too small to be useful, we have ended up with using an even bigger number. Unfortunately, for historical reasons, it isn't a power of ten.

## The mole

A mole is defined as the quantity of matter that contains as many objects (for example, atoms, molecules, formula units, or ions) as the number of atoms in exactly \(12\mathrm{g}\) ( \(= 0.012\mathrm{kg}\) ) of \(^{12}\mathrm{C}\) .

A mole is also approximately the quantity of matter that contains as many objects (for example, atoms, molecules, formula units, ions) as the number of atoms in exactly \(1\mathrm{g}\) ( \(= 0.001\mathrm{kg}\) ) of \(^{1}\mathrm{H}\) , but carbon was chosen as a more convenient international standard since solids are easier to weigh accurately.

A mole of atoms is equivalent to an Avogadro number \(N_{\mathrm{A}}\) of atoms. The Avogadro number, expressed to four significant figures, is

\[N_{\mathrm{A}} = 6.022\times 10^{23}. \quad (1.1)\]

One can write \(N_{\mathrm{A}}\) as \(6.022\times 10^{23}\mathrm{mol}^{- 1}\) as a reminder of its definition, but \(N_{\mathrm{A}}\) is dimensionless, as are moles. They are both numbers. By the same logic, one would have to define the 'eggbox number' as 12 dozen \(- 1\) .

## Example 1.2

Example 1.2- 1 mole of carbon is \(6.022\times 10^{23}\) atoms of carbon.- 1 mole of benzene is \(6.022\times 10^{23}\) molecules of benzene.- 1 mole of NaCl contains \(6.022\times 10^{23}\) NaCl formula units, etc.

The Avogadro number is an exceedingly large number: a mole of eggs would make an omelette with about half the mass of the Moon!

The molar mass of a substance is the mass of one mole of the substance. Thus the molar mass of carbon is \(12\mathrm{g}\) , but the molar mass of water is close to \(18\mathrm{g}\) (because the mass of a water molecule is about \(\frac{18}{12}\) times larger than the mass of a carbon atom). The mass \(m\) of a single molecule or atom is therefore the molar mass of that substance divided by the Avogadro number. Equivalently:

\[\mathrm{molar~mass} = mN_{\mathrm{A}}. \quad (1.2)\]

===== Page 23 =====

2 An impulse is the product of force and a time interval. The impulse is equal to the change of momentum.

[Image: Three graphs (a), (b), and (c) of force F versus time t. (a) shows three small, sparse vertical spikes. (b) shows many more, slightly taller spikes. (c) shows a dense forest of tall spikes, with the average value appearing much more constant.]
Fig. 1.1 Graphs of the force on a roof as a function of time due to falling rain drops.

### 1.2 The thermodynamic limit

In this section, we will explain how the large numbers of molecules in a typical thermodynamic system mean that it is possible to deal with average quantities. Our explanation proceeds using an analogy: imagine that you are sitting inside a tiny hut with a flat roof. It is raining outside, and you can hear the occasional raindrop striking the roof. The raindrops arrive randomly, so sometimes two arrive close together, but sometimes there is quite a long gap between raindrops. Each raindrop transfers its momentum to the roof and exerts an impulse on it. If you knew the mass and terminal velocity of a raindrop, you could estimate the force on the roof of the hut. The force as a function of time would look like that shown in Fig. 1.1(a), each little blip corresponding to the impulse from one raindrop.

Now imagine that you are sitting inside a much bigger hut with a flat roof a thousand times the area of the first roof. Many more raindrops will now be falling on the larger roof area and the force as a function of time would look like that shown in Fig. 1.1(b). Now scale up the area of the flat roof by a further factor of one hundred and the force would look like that shown in Fig. 1.1(c). Notice two key things about these graphs:

(1) The force, on average, gets bigger as the area of the roof gets bigger. This is not surprising because a bigger roof catches more raindrops.
(2) The fluctuations in the force get smoothed out and the force looks like it stays much closer to its average value. In fact, the fluctuations are still big but, as the area of the roof increases, they grow more slowly than the average force does.

The force grows with area, so it is useful to consider the pressure, which is defined as

\[\mathrm{pressure} = \frac{\mathrm{force}}{\mathrm{area}}. \quad (1.3)\]

The average pressure due to the falling raindrops will not change as the area of the roof increases, but the fluctuations in the pressure will decrease. In fact, we can completely ignore the fluctuations in the pressure in the limit that the area of the roof grows to infinity. This is precisely analogous to the limit we refer to as the thermodynamic limit.

Consider now the molecules of a gas which are bouncing around in a container. Each time the molecules bounce off the walls of the container, they exert an impulse on the walls. The net effect of all these impulses is a pressure, a force per unit area, exerted on the walls of the container. If the container were very small, we would have to worry about fluctuations in the pressure (the random arrival of individual molecules on the wall, much like the raindrops in Fig. 1.1(a)). However, in most cases that one meets, the number of molecules in a container of gas is extremely large, so these fluctuations can be ignored and the pressure of the gas appears to be completely uniform. Again, our description of the pressure of this

===== Page 24 =====

1.2 The thermodynamic limit 5

system can be said to be "in the thermodynamic limit", where we have let the number of molecules be regarded as tending to infinity in such a way that the density of the gas is a constant.

Suppose that the container of gas has volume \(V\) , that the temperature is \(T\) , the pressure is \(p\) , and the kinetic energy of all the gas molecules adds up to \(U\) . Imagine slicing the container of gas in half with an imaginary plane, and now just focus your attention on the gas on one side of the plane. The volume of this half of the gas, let's call it \(V^{*}\) , is by definition half that of the original container, i.e.,

\[V^{*} = \frac{V}{2}. \quad (1.4)\]

The kinetic energy of this half of the gas, let's call it \(U^{*}\) , is clearly half that of the total kinetic energy, i.e.,

\[U^{*} = \frac{U}{2}. \quad (1.5)\]

However, the pressure \(p^{*}\) and the temperature \(T^{*}\) of this half of the gas are the same as for the whole container of gas, so that

\[p^{*} = p, \quad T^{*} = T. \quad (1.6)\]

Variables which scale with the system size, like \(V\) and \(U\) , are called extensive variables. Those which are independent of system size, like \(p\) and \(T\) , are called intensive variables.

Thermal physics evolved in various stages and has left us with various approaches to the subject:

The subject of classical thermodynamics deals with macroscopic properties, such as pressure, volume, and temperature, without worrying about the underlying microscopic physics. It applies to systems that are sufficiently large that microscopic fluctuations can be ignored, and it does not assume that there is an underlying atomic structure to matter. The kinetic theory of gases tries to determine the properties of gases by considering probability distributions associated with the motions of individual molecules. This was initially somewhat controversial since the existence of atoms and molecules was doubted by many until the late nineteenth and early twentieth centuries. The realization that atoms and molecules exist led to the development of statistical mechanics. Rather than starting with descriptions of macroscopic properties (as in thermodynamics) this approach begins with trying to describe the individual microscopic states of a system and then uses statistical methods to derive the macroscopic properties from them. This approach received an additional impetus with the development of quantum theory, which showed explicitly how to describe the microscopic quantum

===== Page 25 =====

 states of different systems. The thermodynamic behaviour of a system is then asymptotically approximated by the results of statistical mechanics in the thermodynamic limit, i.e., as the number of particles tends to infinity (with intensive quantities such as pressure and density remaining finite).

In the next section, we will state the ideal gas law, which was first found experimentally but can be deduced from the kinetic theory of gases (see Chapter 6).

### 1.3 The ideal gas

Experiments on gases show that the pressure \(p\) of a volume \(V\) of gas depends on its temperature \(T\) . For example, a fixed amount of gas at constant temperature obeys

\[p\propto 1 / V, \quad (1.8)\]

a result which is known as Boyle's law (sometimes as the Boyle- Mariotte law); it was discovered experimentally by Robert Boyle (1627- 1691) in 1662 and independently by Edmé Mariotte (1620- 1684) in 1676. At constant pressure, the gas also obeys

\[V\propto T, \quad (1.9)\]

where \(T\) is measured in kelvin. This is known as Charles' law and was discovered experimentally, in a crude fashion, by Jacques Charles (1746- 1823) in 1787, and more completely by Joseph Louis Gay- Lussac (1778- 1850) in 1802, though their work was partly anticipated by Guillaume Amontons (1663- 1705) in 1699, who also noticed that a fixed volume of gas obeys

\[p\propto T, \quad (1.10)\]

a result that Gay- Lussac himself found independently in 1809 and is often known as Gay- Lussac's law.3

These three empirical laws can be combined to give

\[pV\propto T. \quad (1.11)\]

It turns out that, if there are \(N\) molecules in the gas, this finding can be expressed as follows:

\[pV = Nk_{\mathrm{B}}T. \quad (1.12)\]

This is known as the ideal gas equation, and the constant \(k_{\mathrm{B}}\) is known as the Boltzmann constant.4 We now make some comments about the ideal gas equation.

We have stated this law purely as an empirical law, observed in experiment. We will derive it from first principles using the kinetic theory of gases in Chapter 6. This theory assumes that a gas can be modelled as a collection of individual tiny particles which can bounce off the walls of the container, and each other (see Fig. 1.2).

===== Page 26 =====

1.4 Combinatorial problems 7

Why do we call it "ideal"? The microscopic justification that we will present in Chapter 6 proceeds under various assumptions: (i) we assume that there are no intermolecular forces, so that the molecules are not attracted to each other; (ii) we assume that molecules are point- like and have zero size. These are idealized assumptions and so we do not expect the ideal gas model to describe real gases under all circumstances. However, it does have the virtue of simplicity: eqn 1.12 is simple to write down and remember. Perhaps more importantly, it does describe gases quite well under quite a wide range of conditions.

The ideal gas equation forms the basis of much of our study of classical thermodynamics. Gases are common in nature: they are encountered in astrophysics and atmospheric physics; it is gases which are used to drive engines, and thermodynamics was invented to try and understand engines. Therefore this equation is fundamental in our treatment of thermodynamics and should be memorized.

The ideal gas law, however, doesn't describe all important gases, and several chapters in this book are devoted to seeing what happens when various assumptions fail. For example, the ideal gas equation assumes that the gas molecules move non- relativistically. When this is not the case, we have to develop a model of relativistic gases (see Chapter 25). At low temperatures and high densities, gas molecules do attract one another (this must occur for liquids and solids to form) and this is considered in Chapters 26, 27, and 28. Furthermore, when quantum effects are important we need a model of quantum gases, and this is outlined in Chapter 30.

Of course, thermodynamics applies also to systems which are not gaseous (so the ideal gas equation, though useful, is not a cure for all ills), and we will look at the thermodynamics of rods, bubbles, and magnets in Chapter 17.

### 1.4 Combinatorial problems

Even larger numbers than \(N_{\mathrm{A}}\) occur in problems involving combinations, and these turn out to be very important in thermal physics. The following example illustrates a simple combinatorial problem which captures the essence of what we are going to have to deal with.

## Example 1.3

Let us imagine that a certain system contains ten atoms. Each of these atoms can exist in one of two states, according to whether it has zero units or one unit of energy. These "units" of energy are called quanta of energy. How many distinct arrangements of quanta are possible for this system if you have at your disposal (a) ten quanta of energy; (b) four quanta of energy?

[Image: A square box containing several small circles, each with a line with an arrowhead attached, representing molecules moving and bouncing off the walls of the container.]
Fig. 1.2 In the kinetic theory of gases, a gas is modelled as a number of individual tiny particles which can bounce off the walls of the container, and each other.

===== Page 27 =====

 Fig. 1.3 Ten atoms that can accommodate four quanta of energy. An atom with a single quantum of energy is shown as a filled circle, otherwise it is shown as an empty circle. One configuration is shown here.

[Image: Ten circles in a row. Some are open (empty) and some are filled with black (occupied by a quantum).]
Fig. 1.3 Ten atoms that can accommodate four quanta of energy. An atom with a single quantum of energy is shown as a filled circle, otherwise it is shown as an empty circle. One configuration is shown here.

\(^{5}\) Other symbols sometimes used for \(^{n}C_{r}\) include \(^{n}C\) and \(\binom{n}{r}\) .

[Image: Two rows (a) and (b). (a) shows ten filled circles. (b) shows three different rows of ten circles each, with a different pattern of open and filled circles.]
Fig. 1.4 Each row shows the ten atoms that can accommodate \(r\) quanta of energy. An atom with a single quantum of energy is shown as a filled circle, otherwise it is shown as an empty circle. (a) For \(r = 10\) there is only one possible configuration. (b) For \(r = 4\) there are 210 possibilities, of which three are shown.

## Solution:

We can represent the ten atoms by drawing ten boxes; an empty box signifies an atom with zero quanta of energy; a filled box signifies an atom with one quantum of energy (see Fig. 1.3). We give two methods for calculating the number of ways of arranging \(r\) quanta among \(n\) atoms:

(1) In the first method, we realize that the first quantum can be assigned to any of the \(n\) atoms, the second quantum can be assigned to any of the remaining atoms (there are \(n - 1\) of them), and so on until the \(r^{\mathrm{th}}\) quantum can be assigned to any of the remaining \(n - r + 1\) atoms. Thus our first guess for the number of possible arrangements of the \(r\) quanta we have assigned is \(\Omega_{\mathrm{guess}} = n\times (n - 1)\times (n - 2)\times \ldots \times (n - r + 1)\) . This can be simplified as follows:

\[\Omega_{\mathrm{guess}} = \frac{n\times(n - 1)\times(n - 2)\times\ldots\times1}{(n - r)\times(n - r - 1)\times\ldots\times1} = \frac{n!}{(n - r)!}. \quad (1.13)\]

However, this assumes that we have labelled the quanta as "the first quantum", "the second quantum" etc. In fact, we don't care which quantum is which because they are indistinguishable. We can rearrange the \(r\) quanta in any one of \(r!\) arrangements. Hence our answer \(\Omega_{\mathrm{guess}}\) needs to be divided by \(r!\) , so that the number \(\Omega\) of unique arrangements is

\[\Omega = \frac{n!}{(n - r)!r!}\equiv {}^{n}C_{r}, \quad (1.14)\]

where \({}^{n}C_{r}\) is the symbol for a combination.

(2) In the second method, we recognize that there are \(r\) atoms each with one quantum and \(n - r\) atoms with zero quanta. The number of arrangements is then simply the number of ways of arranging \(r\) ones and \(n - r\) zeros. There are \(n!\) ways of arranging a sequence of \(n\) distinguishable symbols. If \(r\) of these symbols are the same (all ones), there are \(r!\) ways of arranging these without changing the pattern. If the remaining \(n - r\) symbols are all the same (all zeros), there are \((n - r)!\) ways of arranging these without changing the pattern. Hence we again find that

\[\Omega = \frac{n!}{(n - r)!r!}. \quad (1.15)\]

For the specific cases shown in Fig. 1.4:

(a) \(n = 10\) \(r = 10\) so \(\Omega = 10! / (10! \times 0!)=1\) . This one possibility, with each atom having a quantum of energy, is shown in Fig. 1.4(a).
(b) \(n = 10\) \(r = 4\) so \(\Omega = 10! / (6! \times 4!)=210\) . A few of these possibilities are shown in Fig. 1.4(b).

If instead we had chosen ten times as many atoms (so \(n = 100\) ) and ten times as many quanta, the numbers for (b) would have come out much much bigger. In this case, we would have \(r = 40\) \(\Omega \sim 10^{28}\) . A further factor of ten sends these numbers up much further, so for \(n = 1000\) and \(r = 400\) \(\Omega \sim 10^{290}\) - a staggeringly large number.

===== Page 28 =====

1.5 Plan of the book 9

The numbers in the above example are so large because factorials increase very quickly. In our example we treated 10 atoms; we are clearly going to run into trouble when we attempt to deal with a mole of atoms, i.e., when \(n = 6\times 10^{23}\) .

One way of bringing large numbers down to size is to look at their logarithms.6 Thus, if \(\Omega\) is given by eqn 1.15, we could calculate

\[\ln \Omega = \ln (n!) - \ln ((n - r)! - \ln (r!). \quad (1.16)\]

This expression involves the logarithm of a factorial, and it is going to be very useful to be able to evaluate this. Most pocket calculators have difficulty in evaluating factorials above 69! (because \(70! > 10^{100}\) and many pocket calculators give an overflow error for numbers above \(9.999\times 10^{99}\) ), so some low cunning will be needed to overcome this. Such low cunning is provided by an expression termed Stirling's formula:

\[\ln n! \approx n\ln n - n. \quad (1.17)\]

This expression7 is derived in Appendix C.3.

## Example 1.4

Estimate the order of magnitude of \(10^{23}\) !

Solution:

Using Stirling's formula, we can estimate

\[\ln 10^{23}! \approx 10^{23}\ln 10^{23} - 10^{23} = 5.2\times 10^{24}, \quad (1.18)\]

and hence

\[10^{23}! = \exp (\ln 10^{23}!)\approx \exp (5.20\times 10^{24}). \quad (1.19)\]

We have our answer in the form \(\mathrm{e}^{x}\) , but we would really like it as ten to some power. Now if \(\mathrm{e}^{x} = 10^{y}\) , then \(y = x / \ln 10\) and hence

\[10^{23}! \approx 10^{2.26\times 10^{24}}. \quad (1.20)\]

Just pause for a moment to take in how big this number is. It is roughly one followed by about \(2.26\times 10^{24}\) zeros! Our claim that combinatorial numbers are big seems to be justified!

### 1.5 Plan of the book

This book aims to introduce the concepts of thermal physics one by one, steadily building up the techniques and ideas that make up the subject. Part I contains various preliminary topics. In Chapter 2 we define heat and introduce the idea of heat capacity. In Chapter 3, the ideas of probability are presented for discrete and continuous distributions. (For

===== Page 29 =====

1

[Image: A flowchart diagram showing the structure of the book. Part I (Chapters 1-4) has an arrow pointing to Part II (Chapters 5-8). A dashed arrow from Part I bypasses Part II and goes directly to Part IV. Part II has an arrow to Part III (Chapters 9-10). Part III has an arrow to Part IV. Part IV (Chapters 11-12) has an arrow to Part V (Chapters 13-15). Part V has an arrow to Part VI (Chapters 16-18). Part VI has an arrow to Part VII (Chapters 19-24). Part VII has an arrow to Part VIII (Chapters 25-30). Part VIII has an arrow to Part IX (Chapters 31-37). A grey box on the right says "omitting kinetic theory" with a dashed arrow pointing from it to Part IV.]
Fig. 1.5 Organization of the book. The dashed line shows a possible route through the material that avoids the kinetic theory of gases. The numbers of the core chapters are given in bold type. The other chapters can be omitted on a first reading, or for a reduced-content course.

===== Page 30 =====

 a reader familiar with probability theory, this chapter can be omitted.) We then define temperature in Chapter 4, and this allows us to introduce the Boltzmann distribution, which is the probability distribution for systems in contact with a thermal reservoir.

The plan for the remaining parts of the book is sketched in Fig. 1.5. The following two parts contain a presentation of the kinetic theory of gases, which justifies the ideal gas equation from a microscopic model. Part II presents the Maxwell- Boltzmann distribution of molecular speeds in a gas and the derivation of formulae for pressure, molecular effusion, and mean free path. Part III concentrates on transport and thermal diffusion. Parts II and III can be omitted in courses in which kinetic theory is treated at a later stage.

In Part IV, we begin our introduction to mainstream thermodynamics. The concept of energy is covered in Chapter 11, along with the zeroth and first laws of thermodynamics. These are applied to isothermal and adiabatic processes in Chapter 12.

Part V contains the crucial second law of thermodynamics. The idea of a heat engine is introduced in Chapter 13, which leads to various statements of the second law of thermodynamics. Hence the important concept of entropy is presented in Chapter 14 and its application to information theory is discussed in Chapter 15.

Part VI introduces the rest of the machinery of thermodynamics. Various thermodynamic potentials, such as the enthalpy, Helmholtz function, and Gibbs function, are introduced in Chapter 16, and their usage illustrated. Thermal systems include not only gases, and Chapter 17 looks at other possible systems, such as elastic rods and magnetic systems. The third law of thermodynamics is described in Chapter 18 and provides a deeper understanding of how entropy behaves as the temperature is reduced to absolute zero.

Part VII focuses on statistical mechanics. Following a discussion of the equipartition of energy in Chapter 19, so useful for understanding high temperature limits, the concept of the partition function is presented in some detail in Chapter 20, which is foundational for understanding statistical mechanics. The idea is applied to the ideal gas in Chapter 21. Particle number becomes important when considering different types of particle, so the chemical potential and grand partition function are presented in Chapter 22. Two simple applications where the chemical potential is zero are photons and phonons, discussed in Chapters 23 and 24 respectively.

The discussion up to this point has concentrated on the ideal gas model and we go beyond this in Part VIII: Chapter 25 discusses the effect of relativistic velocities and Chapters 26 and 27 discuss the effect of intermolecular interactions, while phase transitions are discussed in Chapter 28, where the important Clausius- Clapeyron equation for a phase boundary is derived. Another quantum mechanical implication is the existence of identical particles and the difference between fermions and bosons, discussed in Chapter 29; the consequences for the properties of quantum gases are presented in Chapter 30.

===== Page 31 =====

12 Exercises

The remainder of the book, Part IX, contains more detailed information on various special topics which allow the power of thermal physics to be demonstrated. In Chapters 31 and 32 we describe sound waves and shock waves in fluids. We draw some of the statistical ideas of the book together in Chapter 33 and discuss non- equilibrium thermodynamics and the arrow of time in Chapter 34. Applications of the concepts in the book to astrophysics are described in Chapters 35 and 36 and to atmospheric physics in Chapter 37.

## Chapter summary

In this chapter, the idea of big numbers has been introduced. These arise in thermal physics for two main reasons:

(1) The number of atoms in a typical macroscopic lump of matter is large. It is measured in the units of the mole. One mole of atoms contains \(N_{\mathrm{A}}\) atoms, where \(N_{\mathrm{A}} = 6.022\times 10^{23}\) (2) Combinatorial problems generate very large numbers. To make these numbers manageable, we often consider their logarithms and use Stirling's approximation: \(\ln n!\approx n\ln n - n\)

## Exercises

(1.1) What is the mass of 3 moles of carbon dioxide \(\mathrm{CO_2}\) ? (1 mole of oxygen atoms has a mass of \(16\mathrm{g}\) .

(1.2) A typical bacterium has a mass of \(10^{- 12}\mathrm{g}\) . Calculate the mass of a mole of bacteria. (Interestingly, this is about the total number of bacteria living in the guts of all humans resident on planet Earth.) Give your answer in units of elephant- masses (elephants have a mass \(\approx 5000\mathrm{kg}\) .

(1.3) (a) How many water molecules are there in your body? (Assume that you are nearly all water.) (b) How many drops of water are there in all the oceans of the world? (The mass of the world's oceans is about \(10^{21}\mathrm{kg}\) . Estimate the size of a typical drop of water.) (c) Which of these two numbers from (a) and (b) is the larger?

(1.4) A system contains \(n\) atoms, each of which can only have zero or one quanta of energy. How many ways can you arrange \(r\) quanta of energy when (a) \(n = 2\) \(r = 1\) b \(n = 20\) \(r = 10\) c \(n = 2\times 10^{23}\) \(r = 10^{23}\) ?

(1.5) What fractional error do you make when using Stirling's approximation (in the form \(\ln n!\approx n\ln n - n\) to evaluate

a \(\ln 10!\) b \(\ln 100!\) and c \(\ln 1000!\) ?

(1.6) Show that eqn C.19 is equivalent to writing

\[n!\approx n^{n}\mathrm{e}^{-n}\sqrt{2\pi n}, \quad (1.21)\]

and

\[n!\approx \sqrt{2\pi} n^{n + \frac{1}{2}}\mathrm{e}^{-n}. \quad (1.22)\]

===== Page 32 =====

2

In this chapter, we will introduce the concepts of heat and heat capacity.

### 2.1 A definition of heat

We all have an intuitive notion of what heat is: sitting next to a roaring fire in winter, we feel its heat warming us up, increasing our temperature; lying outside in the sunshine on a warm day, we feel the Sun's heat warming us up. In contrast, holding a snowball, we feel heat leaving our hand and transferring to the snowball, making our hand feel cold. Heat seems to be some sort of energy transferred from hot things to cold things when they come into contact. We therefore make the following definition:

We now stress a couple of important points about this definition.

(1) Experiments suggest that heat spontaneously transfers from a hotter body to a colder body when they are in contact, and not in the reverse direction. However, there are circumstances when it is possible for heat to go in the reverse direction. A good example of this is a kitchen freezer: you place food, initially at room temperature, into the freezer and shut the door; the freezer then sucks heat out of the food and cools the food down to below freezing point. Heat is being transferred from your warmer food to the colder freezer, apparently in the "wrong" direction. Of course, to achieve this, you have to be paying your electricity bill and therefore be putting energy in to your freezer. If there is a power cut, heat will slowly leak back into the freezer from the warmer kitchen and thaw out all your frozen food. This shows that it is possible to reverse the direction of heat flow, but only if you intervene by putting additional energy in. We will return to this point in Section 13.5 when we consider refrigerators, but for now let us note that we are defining heat as thermal energy in transit and not hard- wiring into the definition anything about which direction it goes.

(2) The "in transit" part of our definition is very important. Though you can add heat to an object, you cannot say that "an object contains a certain quantity of heat." This is very different from the case of the fuel in your car: you can add fuel to your car,

===== Page 33 =====

1We will see later that objects can contain a certain quantity of energy, so it is possible, at least in principle, to have a gauge that reads out how much energy is contained.

2Work is also a type of energy in transit, since you always do work on something. For example you do work on a mass by lifting it a height \(h\) .We could define work as "mechanical energy in transit". We will explore how work and heat can be interchanged in Chapter 13.

3We have made this point by giving a plausible example, but in Chapter 11 we will show using more mathematical arguments that heat only makes sense as energy "in transit".

and you are quite entitled to say that your car "contains a certain quantity of fuel". You even have a gauge for measuring it! But heat is quite different. Objects do not and cannot have gauges which read out how much heat they contain, because heat only makes sense when it is "in transit".1

To see this, consider your cold hands on a chilly winter day. You can increase the temperature of your hands in two different ways: (i) by adding heat, for example by putting your hands close to something hot, like a roaring fire; (ii) by rubbing your hands together. In one case you have added heat from the outside, in the other case you have not added any heat but have done some work.2 In both cases, you end up with the same final situation: hands that have increased in temperature. There is no physical difference between hands that have been warmed by heat and hands that have been warmed by work.3

Heat is measured in joules (J). The rate of heating has the units of watts (W), where \(1\mathrm{W} = 1\mathrm{J}\mathrm{s}^{- 1}\) (i.e., 1 watt=1 joule per second).

## Example 2.1

A 1 kW electric heater is switched on for ten minutes. How much heat does it produce?

Solution:

Ten minutes equals \(600\mathrm{s}\) so the heat \(Q\) is given by

\[Q = 1\mathrm{kW}\times 600\mathrm{s} = 600\mathrm{kJ}. \quad (2.1)\]

Notice in this last example that the power in the heater is supplied by electrical work. Thus it is possible to produce heat by doing work. We will return to the question of whether one can produce work from heat in Chapter 13.

### 2.2 Heat capacity

In the previous section, we explained that it is not possible for an object to contain a certain quantity of heat, because heat is defined as "thermal energy in transit". It is therefore with a somewhat heavy heart that we turn to the topic of "heat capacity", since we have argued that objects have no capacity for heat! (This is one of those occasions in physics when decades of use of a name have made it completely standard, even though it is really a misleading name to use.) What we are going to derive in this section might be better termed "energy capacity", but to do this would put us at odds with common usage throughout physics. All of this being said, we can proceed quite legitimately by asking the following simple question:

===== Page 34 =====

2.2 Heat capacity 15

How much heat needs to be supplied to an object to raise its temperature by a small amount \(\mathrm{d}T\) ?

The answer to this question is the heat \(\mathrm{d}Q = C\mathrm{d}T\) , where we define the heat capacity \(C\) of an object using

\[C = \frac{\mathrm{d}Q}{\mathrm{d}T}. \quad (2.2)\]

As long as we remember that heat capacity tells us simply how much heat is needed to warm an object (and is nothing about the capacity of an object for heat) we shall be on safe ground. As can be inferred from eqn 2.2, the heat capacity \(C\) has units \(\mathrm{JK}^{- 1}\) .

As shown in the following example, although objects have a heat capacity, one can also express the heat capacity of a particular substance per unit mass, or per unit volume.4

4We will use the symbol \(C\) to represent a heat capacity, whether of an object, or per unit volume, or per mole. We will always state which is being used. The heat capacity per unit mass is distinguished by the use of the lower- case symbol \(c\) . We will usually reserve the use of subscripts on the heat capacity to denote the constraint being applied (see eqns 2.6 and 2.7).

## Example 2.2

The heat capacity of \(0.125\mathrm{kg}\) of water is measured to be \(523\mathrm{JK}^{- 1}\) at room temperature. Hence calculate the heat capacity of water (a) per unit mass and (b) per unit volume.

Solution:

(a) The heat capacity per unit mass \(c\) is given by dividing the heat capacity by the mass, and hence

\[c = \frac{523\mathrm{JK}^{-1}}{0.125\mathrm{kg}} = 4.184\times 10^{3}\mathrm{JK}^{-1}\mathrm{kg}^{-1}. \quad (2.3)\]

(b) The heat capacity per unit volume \(C\) is obtained by multiplying the previous answer by the density of water, namely \(1000\mathrm{kg}\mathrm{m}^{- 3}\) , so that

\[C = 4.184\times 10^{3}\mathrm{JK}^{-1}\mathrm{kg}^{-1}\times 1000\mathrm{kg}\mathrm{m}^{-3} = 4.184\times 10^{6}\mathrm{JK}^{-1}\mathrm{m}^{-3}.\]

The heat capacity per unit mass \(c\) occurs quite frequently, and it is given a special name: the specific heat capacity.

## Example 2.3

Calculate the specific heat capacity of water.

Solution:

This is given in answer (a) from the previous example: the specific heat capacity of water is \(4.184\times 10^{3}\mathrm{JK}^{- 1}\mathrm{kg}^{- 1}\) .

===== Page 35 =====

 Also useful is the molar heat capacity, which is the heat capacity of one mole of the substance.

## Example 2.4

Calculate the molar heat capacity of water. (The molar mass of water is \(18\mathrm{g}\) .)

Solution:

The molar heat capacity is obtained by multiplying the specific heat capacity by the molar mass, and hence

\[C = 4.184\times 10^{3}\mathrm{J}\mathrm{K}^{-1}\mathrm{kg}^{-1}\times 0.018\mathrm{kg} = 75.2\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}. \quad (2.5)\]

5This complication is there for liquids and solids, but doesn't make such a big difference.

[Image: Two diagrams (a) and (b) showing a gas being heated. (a) shows a gas in a sealed rigid container, with heat entering from below. (b) shows a gas in a container with a movable piston, with heat entering from below.]
Fig.2.1 Two methods of heating a gas: (a) constant volume, (b) constant pressure.

When we think about the heat capacity of a gas, there is a further complication. We are trying to ask the question: how much heat should you add to raise the temperature of our gas by one kelvin? But we can imagine doing the experiment in two ways (see also Fig. 2.1):

(1) Place our gas in a sealed box and add heat (Fig. 2.1(a)). As the temperature rises, the gas will not be allowed to expand because its volume is fixed, so its pressure will increase. This method is known as heating at constant volume.
(2) Place our gas in a chamber connected to a piston and heat it (Fig. 2.1(b)). The piston is well lubricated, and so will slide in and out to maintain the pressure in the chamber to be identical to that in the lab. As the temperature rises, the piston is forced out (doing work against the atmosphere) and the gas is allowed to expand, keeping its pressure constant. This method is known as heating at constant pressure.

In both cases, we are applying a constraint to the system, either constraining the volume of the gas to be fixed, or constraining the pressure of the gas to be fixed. We need to modify our definition of heat capacity given in eqn 2.2, and hence we define two new quantities: \(C_V\) is the heat capacity at constant volume and \(C_p\) is the heat capacity at constant pressure. We can write them using partial differentials as follows:

\[C_V = \left(\frac{\partial Q}{\partial T}\right)_V, \quad C_p = \left(\frac{\partial Q}{\partial T}\right)_p. \quad (2.6)\]

We expect that \(C_p\) will be bigger than \(C_V\) for the simple reason that more heat will need to be added when heating at constant pressure than when heating at constant volume. This is because in the latter case additional energy will be expended on doing work on the atmosphere as the gas expands. It turns out that indeed \(C_p\) is bigger than \(C_V\) in practice.

===== Page 36 =====

 Example 2.5

The specific heat capacity of helium gas is measured to be \(3.12\mathrm{kJ}\mathrm{K}^{- 1}\mathrm{kg}^{- 1}\) at constant volume and \(5.19\mathrm{kJ}\mathrm{K}^{- 1}\mathrm{kg}^{- 1}\) at constant pressure. Calculate the molar heat capacities. (The molar mass of helium is \(4\mathrm{g}\) Solution:

Solution:

The molar heat capacity is obtained by multiplying the specific heat capacity by the molar mass, and hence

\[C_V = 12.48\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}, \quad C_P = 20.76\mathrm{J}\mathrm{K}^{-1}\mathrm{mol}^{-1}. \quad (2.9)\]

(Interestingly, these answers are almost exactly \(\frac{3}{2} R\) and \(\frac{5}{2} R\) where \(R\) is the gas constant. We will see why in Section 11.3. )

\(7R = 8.31447\mathrm{J}\mathrm{K}^{- 1}\mathrm{mol}^{- 1}\) is known as the gas constant and is equal to the product of the Avogadro number \(N_{\mathrm{A}}\) and the Boltzmann constant \(k_{\mathrm{B}}\) (see Section 6.2).

## Chapter summary

In this chapter, the concepts of heat and heat capacity have been introduced. Heat is "thermal energy in transit". The heat capacity \(C\) of an object is given by \(C = \mathrm{d}Q / \mathrm{d}T\) . The heat capacity of a substance can also be expressed per unit volume or per unit mass (in the latter case it is called specific heat capacity).

## Exercises

(2.1) Using data from this chapter, estimate the energy needed to (a) boil enough tap water to make a cup of tea, (b) heat the water for a bath.

(2.2) The world's oceans contain approximately \(10^{21}\mathrm{kg}\) of water. Estimate the total heat capacity of the world's oceans.

(2.3) The world's power consumption is currently about \(13\mathrm{TW}\) and growing! \(\mathrm{(1TW = 10^{12}W)}\) Burning one ton of crude oil (which is nearly seven barrels worth) produces about \(42\mathrm{GJ}\) \(\mathrm{(1GJ = 10^{9}J)}\) . If the world's total power needs were to come from burning oil (a large fraction currently does), how much oil would we be burning per second?

(2.4) The molar heat capacity of gold is \(25.4\mathrm{J}\mathrm{mol}^{- 1}\mathrm{K}^{- 1}\) Its density is \(19.3\times 10^{3}\mathrm{kg}\mathrm{m}^{- 3}\) . Calculate the specific heat capacity of gold and the heat capacity per unit volume. What is the heat capacity of \(4\times 10^{6}\mathrm{kg}\) of gold? (This is roughly the holdings of Fort Knox.)

(2.5) Two bodies, with heat capacities \(C_1\) and \(C_2\) (assumed independent of temperature) and initial temperatures \(T_{1}\) and \(T_{2}\) respectively, are placed in thermal contact. Show that their final temperature \(T_{\mathrm{f}}\) is given by \(T_{\mathrm{f}} = (C_{1}T_{1} + C_{2}T_{2}) / (C_{1} + C_{2})\) . If \(C_1\) is much larger than \(C_2\) , show that \(T_{\mathrm{f}}\approx T_{1} + C_{2}(T_{2} - T_{1}) / C_{1}\) .

===== Page 37 =====

3 Probability

3.1 Discrete probability distributions 19 3.2 Continuous probability distributions 20 3.3 Linear transformation 21 3.4 Variance 22 3.5 Linear transformation and the variance 23 3.6 Independent variables 24 3.7 Binomial distribution 26 Chapter summary 28 Further reading 29 Exercises 29

Life is full of uncertainties, and has to be lived according to our best guesses based on the information available to us. This is because the chain of events that lead to various outcomes can be so complex that the exact outcomes are unpredictable. Nevertheless, things can still be said even in an uncertain world: for example, it is more helpful to know that there is a \(20\%\) chance of rain tomorrow than that the weather forecaster has absolutely no idea; or worse still that he or she claims that there will definitely be no rain, when there might be! Probability is therefore an enormously useful and powerful subject, since it can be used to quantify uncertainty.

The foundations of probability theory were laid by the French mathematicians Pierre de Fermat (1601- 1665) and Blaise Pascal (1623- 1662), through their correspondence in 1654, which originated from a problem set to them by a gentleman gambler. The ideas proved to be intellectually infectious and the first probability textbook was written by the Dutch physicist Christian Huygens (1629- 1695) in 1657, who applied it to the working out of life expectancy. Probability was thought to be useful only for determining possible outcomes in situations in which we lacked complete knowledge. The supposition was that if we could know the motions of all particles at the microscopic level, we could determine every outcome precisely. In the twentieth century, the discovery of quantum theory has led to the understanding that, at the microscopic level, outcomes are purely probabilistic.

Probability has had a huge impact on thermal physics. This is because we are often interested in systems containing huge numbers of particles, so that predictions based on probability turn out to be precise enough for most purposes. In a thermal physics problem, one is often interested in the values of quantities that are the sum of many small contributions from individual atoms. Though each atom behaves differently, the average behaviour is what comes through, and therefore it becomes necessary to be able to extract average values from probability distributions.

In this chapter, we will define some basic concepts in probability theory. Let us begin by stating that the probability of occurrence of a particular event, taken from a finite set of possible events, is zero if that event is impossible, is one if that event is certain, and takes a value somewhere in between zero and one if that event is possible but not certain. We begin by considering two different types of probability distribution: discrete and continuous.

===== Page 38 =====

3.1 Discrete probability distributions

Discrete random variables can only take a finite number of values. Examples include the number obtained when throwing a die (1, 2, 3, 4, 5, or 6), the number of children in each family (0, 1, 2, ...), and the number of people killed per year in the UK in bizarre gardening accidents (0, 1, 2, ...). Let \(x\) be a discrete random variable which takes values \(x_{i}\) with probability \(P_{i}\) . We require that the sum of the probabilities of every possible outcome adds up to one. This may be written

\[\sum_{i}P_{i} = 1. \quad (3.1)\]

We define the mean (or average or expected value) of \(x\) to be

\[\langle x\rangle = \sum_{i}x_{i}P_{i}. \quad (3.2)\]

The idea is that you weight by its probability each value taken by the random variable \(x\) .

Alternative notations for the mean of \(x\) include \(\bar{x}\) and \(E(x)\) . We prefer the one given in the main text since it is easier to distinguish quantities such as \(\langle x^{2}\rangle\) and \(\langle x\rangle^{2}\) with this notation, particularly when writing quickly.

## Example 3.1

Note that the mean, \(\langle x\rangle\) , may be a value that \(x\) cannot actually take. A common example of this is the number of children in families, which is often quoted as 2.4. Any individual couple can only have an integer number of children. Thus the expected value of \(x\) is actually an impossibility!

It is also possible to define the mean squared value of \(x\) using

\[\langle x^{2}\rangle = \sum_{i}x_{i}^{2}P_{i}. \quad (3.3)\]

In fact, any function of \(x\) can be averaged, using (by analogy)

\[\langle f(x)\rangle = \sum_{i}f(x_{i})P_{i}. \quad (3.4)\]

Now let us actually evaluate the mean of \(x\) for a particular discrete distribution.

[Image: A bar chart showing a discrete probability distribution P(x) for x = 0, 1, 2. The bar at x=0 has height 1/2, at x=1 has height 1/4, and at x=2 has height 1/4.]
Fig. 3.1 An example of a discrete probability distribution.

## Example 3.2

Let \(x\) take values 0, 1, and 2 with probabilities \(\frac{1}{2}, \frac{1}{4}\) , and \(\frac{1}{4}\) respectively. This distribution is shown in Fig. 3.1. Calculate \(\langle x \rangle\) and \(\langle x^{2} \rangle\) .

===== Page 39 =====

20 Probability

Solution:

First check that \(\sum P_{i} = 1\) . Since \(\frac{1}{2} +\frac{1}{4} +\frac{1}{4} = 1\) , this is fine. Now we can calculate the averages as follows:

\[\begin{array}{rcl}{\langle x\rangle} & = & {\sum_{i}x_{i}P_{i}}\\ {} & {} & {}\\ {} & = & {0\cdot \frac{1}{2} +1\cdot \frac{1}{4} +2\cdot \frac{1}{4}}\\ {} & = & {\frac{3}{4}.} \end{array} \quad (3.5)\]

Again, we find that the mean \(\langle x \rangle\) is not actually one of the possible values of \(x\) . We can now calculate the value of \(\langle x^{2} \rangle\) as follows:

\[\begin{array}{rcl}{\langle x^2\rangle} & = & {\sum_i x_i^2 P_i}\\ {} & {} & {}\\ {} & = & {0\cdot \frac{1}{2} +1\cdot \frac{1}{4} +4\cdot \frac{1}{4}}\\ {} & = & {\frac{5}{4}.} \end{array} \quad (3.6)\]

### 3.2 Continuous probability distributions

For a continuous random variable, there are an infinite number of possible values it can take, so the probability of any one of them occurring is zero! Hence we talk about the probability of the variable lying in some range, such as "between \(x\) and \(x + \mathrm{d}x\) "

Let \(x\) now be a continuous random variable which has a probability \(P(x) \mathrm{d}x\) of having a value between \(x\) and \(x + \mathrm{d}x\) . Continuous random variables can take a range of possible values. Examples include the height of children in a class, the length of time spent in a waiting room, and the amount a person's blood pressure increases when reading their mobile- phone bill. These quantities are not restricted to any finite set of values, but can take a continuous set of values.

As before, we require that the total probability of all possible outcomes is one. Because we are dealing with continuous distributions, the sums become integrals, and we have

\[\int P(x)\mathrm{d}x = 1. \quad (3.7)\]

The mean is defined as

\[\langle x\rangle = \int x P(x)\mathrm{d}x. \quad (3.8)\]

Similarly, the mean square value is defined as

\[\langle x^2\rangle = \int x^2 P(x)\mathrm{d}x, \quad (3.9)\]

and the mean of any function of \(x\) , \(f(x)\) , can be defined as

\[\langle f(x)\rangle = \int f(x)P(x)\mathrm{d}x. \quad (3.10)\]

===== Page 40 =====

3.3 Linear transformation 21

## Example 3.3

Let \(P(x) = C\mathrm{e}^{- x^{2} / 2a^{2}}\) where \(C\) and \(a\) are constants. This probability is illustrated in Fig. 3.2 and this curve is known as a Gaussian. Calculate \(\langle x\rangle\) and \(\langle x^{2}\rangle\) given this probability distribution.

Solution:

The first thing to do is to normalize the probability distribution (i.e., to ensure that the sum over all probabilities is one). This allows us to find the constant \(C\) using eqn C.3 to evaluate the integral:

\[\begin{array}{rcl}{1 = \int_{-\infty}^{\infty}P(x)\mathrm{d}x} & = & {C\int_{-\infty}^{\infty}\mathrm{e}^{-x^{2} / 2a^{2}}\mathrm{d}x}\\ {} & = & {C\sqrt{2\pi a^{2}},} \end{array} \quad (3.11)\]

so we find that \(C = 1 / \sqrt{2\pi a^{2}}\) , which gives

\[P(x) = \frac{1}{\sqrt{2\pi a^{2}}}\mathrm{e}^{-x^{2} / 2a^{2}}. \quad (3.12)\]

The mean of \(x\) can then be evaluated using

\[\begin{array}{rcl}{\langle x\rangle} & = & {\frac{1}{\sqrt{2\pi a^{2}}}\int_{-\infty}^{\infty}x\mathrm{e}^{-x^{2} / 2a^{2}}\mathrm{d}x}\\ {} & = & {0,} \end{array} \quad (3.13)\]

because the integrand is an odd function. The mean of \(x^{2}\) can also be evaluated as follows:

\[\begin{array}{rcl}{\langle x^2\rangle} & = & {\frac{1}{\sqrt{2\pi a^2}}\int_{-\infty}^{\infty}x^2\mathrm{e}^{-x^2 / 2a^2}\mathrm{d}x}\\ {} & = & {\frac{1}{\sqrt{2\pi a^2}}\frac{1}{2}\sqrt{8\pi a^6}}\\ {} & = & {a^2,} \end{array} \quad (3.14)\]

where the integrals are performed as described in Appendix C.2.

[Image: A bell-shaped curve representing a continuous probability distribution P(x) centered at x=0.]
Fig. 3.2 An example continuous probability distribution.

### 3.3 Linear transformation

Sometimes one has a random variable, and one wants to make a second random variable by performing a linear transformation on the first one. If \(y\) is a random variable, which is related to the random variable \(x\) by the equation

\[y = ax + b, \quad (3.15)\]

where \(a\) and \(b\) are constants, then the average value of \(y\) is given by

\[\langle y\rangle = \langle ax + b\rangle = a\langle x\rangle +b. \quad (3.16)\]

The proof of this result is straightforward and is left as an exercise.

===== Page 41 =====

3.4 Variance

We now know how to calculate the average of a set of values, but what about the spread in the values? The first idea one might have to quantify the spread of values in a distribution is to consider the deviation from the mean for a particular value of \(x\) . This is defined by

\[x - \langle x\rangle . \quad (3.17)\]

This quantity tells you by how much a particular value is above or below the mean value. We can work out the average of the deviation (averaging over all values of \(x\) ) as follows:

\[\langle x - \langle x\rangle \rangle = \langle x\rangle -\langle x\rangle = 0, \quad (3.18)\]

which follows from the equation for linear transformation (eqn 3.16). Thus the average deviation is not going to be a very helpful indicator! Of course, the problem is that the deviation is sometimes positive and sometimes negative, and the positive and negative deviations cancel out. A more useful quantity would be the modulus of the deviation,

\[|x - \langle x\rangle |, \quad (3.19)\]

which is always positive, but this will suffer from the disadvantage that modulus signs in algebra can be both confusing and tedious. Therefore, another approach is to use a different quantity which is always positive, the square of the deviation, \((x - \langle x\rangle)^2\) . This quantity is what we need: always positive and easy to manipulate algebraically. Hence, its average is given a special name, the variance. Consequently the variance of \(x\) , written as \(\sigma_{x}^{2}\) , is defined as the mean squared deviation:

\[\sigma_{x}^{2} = \langle (x - \langle x\rangle)^{2}\rangle . \quad (3.20)\]

We will call \(\sigma_{x}\) the standard deviation, and it is defined as the square root of the variance:

\[\sigma_{x} = \sqrt{\langle(x - \langle x\rangle)^{2}\rangle}. \quad (3.21)\]

===== Page 42 =====

3.5 Linear transformation and the variance 23

The standard deviation represents the "root mean square" (known as the "rms") scatter or spread in the data.

The following identity is extremely useful:

\[\begin{array}{rcl}{\sigma_x^2} & = & {\langle (x - \langle x\rangle)^2\rangle}\\ {} & = & {\langle x^2 -2x\langle x\rangle +\langle x\rangle^2\rangle}\\ {} & = & {\langle x^2\rangle -2\langle x\rangle \langle x\rangle +\langle x\rangle^2}\\ {} & = & {\langle x^2\rangle -\langle x\rangle^2.} \end{array} \quad (3.22)\]

## Example 3.5

For Examples 3.2 and 3.3 above, work out \(\sigma_{x}^{2}\) , the variance of the distribution, in each case.

Solution:

For Example 3.2

\[\sigma_{x}^{2} = \langle x^{2}\rangle -\langle x\rangle^{2} = \frac{5}{4} -\frac{9}{16} = \frac{11}{16}. \quad (3.23)\]

For Example 3.3

\[\sigma_{x}^{2} = \langle x^{2}\rangle -\langle x\rangle^{2} = a^{2} - 0 = a^{2}. \quad (3.24)\]

### 3.5 Linear transformation and the variance

We return to the problem of a linear transformation of a random variable. What happens to the variance in this case?

If \(y\) is a random variable which is related to the random variable \(x\) by the equation

\[y = ax + b, \quad (3.25)\]

where \(a\) and \(b\) are constants, then we have seen that

\[\langle y\rangle = \langle ax + b\rangle = a\langle x\rangle +b. \quad (3.26)\]

Hence, we can work out \(\langle y^{2}\rangle\) , which is

\[\begin{array}{rcl}{\langle y^2\rangle} & = & {\langle (ax + b)^2\rangle}\\ {} & = & {\langle a^2 x^2 +2abx + b^2\rangle}\\ {} & = & {a^2 \langle x^2\rangle +2ab\langle x\rangle +b^2.} \end{array} \quad (3.27)\]

Also, we can work out \(\langle y\rangle^{2}\) , which is

\[\langle y\rangle^{2} = (a\langle x\rangle +b)^{2} = a^{2}\langle x\rangle^{2} + 2ab\langle x\rangle +b^{2}. \quad (3.28)\]

===== Page 43 =====

24 Probability

Hence, using eqn 3.22, the variance in \(y\) is given by eqn 3.27 minus eqn 3.28, i.e.

\[\begin{array}{rcl}{\sigma_y^2} & = & {\langle y^2\rangle -\langle y\rangle^2}\\ {} & = & {a^2\langle x^2\rangle -a^2\langle x\rangle^2}\\ {} & = & {a^2\sigma_x^2.} \end{array} \quad (3.29)\]

Notice that the variance depends on \(a\) but not on \(b\) . This makes sense because the variance tells us about the width of a distribution, and nothing about its absolute position. The standard deviation of \(y\) is therefore given by

\[\sigma_{y} = a\sigma_{x}. \quad (3.30)\]

## Example 3.6

The average temperature in a town in the USA in January is \(23^{\circ}\mathrm{F}\) and the standard deviation is \(9^{\circ}\mathrm{F}\) . Convert these figures into degrees Celsius using the relation in Example 3.4.

Solution:

The average temperature in degrees Celsius is given by

\[\langle C\rangle = \frac{5}{9} (\langle F\rangle -32) = \frac{5}{9} (23 - 32) = -5^{\circ}\mathrm{C}, \quad (3.31)\]

and the standard deviation is given by \(\frac{5}{9}\times 9 = 5^{\circ}\mathrm{C}\)

### 3.6 Independent variables

Two random variables are independent if knowing the value of one of them yields no information about the value of the other. For example, the height of a person chosen at random from a city and the number of hours of rainfall in that city on the first Tuesday of September are two independent random variables.

If \(u\) and \(v\) are independent random variables the probability that \(u\) is in the range from \(u\) to \(u + \mathrm{d}u\) and \(v\) is in the range from \(v\) to \(v + \mathrm{d}v\) is given by the product

\[P_{u}(u)\mathrm{d}u P_{v}(v)\mathrm{d}v. \quad (3.32)\]

Hence, the average value of the product of \(u\) and \(v\) is

\[\begin{array}{rcl}{\langle u v\rangle} & = & {\iint u v P_{u}(u)P_{v}(v)\mathrm{d}u\mathrm{d}v}\\ {} & = & {\int u P_{u}(u)\mathrm{d}u\int v P_{v}(v)\mathrm{d}v}\\ {} & = & {\langle u\rangle \langle v\rangle ,} \end{array} \quad (3.33)\]

because the integrals separate for independent random variables. This implies that the average value of the product of \(u\) and \(v\) is equal to the product of their average values.

===== Page 44 =====

3.6 Independent variables 25

## Example 3.7

Suppose that there are \(n\) independent random variables, \(X_{i}\) , each with the same mean \(\langle X\rangle\) and variance \(\sigma_{X}^{2}\) . Let \(Y\) be the sum of the random variables, so that \(Y = X_{1} + X_{2} + \dots +X_{n}\) . Find the mean and variance of \(Y\) .

Solution:

The mean of \(Y\) is simply

\[\langle Y\rangle = \langle X_1\rangle +\langle X_2\rangle +\dots +\langle X_n\rangle , \quad (3.34)\]

but since all the \(X_{i}\) have the same mean \(\langle X\rangle\) this can be written

\[\langle Y\rangle = n\langle X\rangle . \quad (3.35)\]

Hence the mean of \(Y\) is \(n\) times the mean of the \(X_{i}\) . To find the variance of \(Y\) , we can use the formula

\[\sigma_{Y}^{2} = \langle Y^{2}\rangle -\langle Y\rangle^{2}. \quad (3.36)\]

Hence

\[\begin{array}{rcl}{\langle Y^2\rangle} & = & {\langle X_1^2 +\dots +X_N^2 +X_1X_2 + X_2X_1 + X_1X_3 + \dots \rangle}\\ {} & = & {\langle X_1^2\rangle +\dots +\langle X_N^2\rangle +\langle X_1X_2\rangle +\langle X_2X_1\rangle +\langle X_1X_3\rangle +\dots} \end{array} \quad (3.37)\]

There are \(n\) terms like \(\langle X_{1}^{2}\rangle\) on the right- hand side, and \(n(n - 1)\) terms like \(\langle X_{1}X_{2}\rangle\) . The former terms take the value \(\langle X^{2}\rangle\) and the latter terms (because they are the product of two independent random variables) take the value \(\langle X\rangle \langle X\rangle = \langle X\rangle^{2}\) . Hence, using eqn 3.35,

\[\langle Y^2\rangle = n\langle X^2\rangle +n(n - 1)\langle X\rangle^2, \quad (3.38)\]

so that

\[\begin{array}{rcl}{\sigma_Y^2} & = & {\langle Y^2\rangle -\langle Y\rangle^2}\\ {} & = & {n\langle X^2\rangle -n\langle X\rangle^2}\\ {} & = & {n\sigma_X^2.} \end{array} \quad (3.39)\]

The results proved in this last example have some interesting applications. The first concerns experimental measurements. Imagine that a quantity \(X\) is measured \(n\) times, each time with an independent error, which we call \(\sigma_{X}\) . If you add up the results of the measurements to make \(Y = \sum X_{i}\) , then the rms error in \(Y\) is only \(\sqrt{n}\) times the rms error of a single \(X\) . Hence if you try and get a good estimate of \(X\) by calculating \((\sum X_{i}) / n\) , the error in this quantity is equal to \(\sigma_{X} / \sqrt{n}\) . Thus, for example, if you make four measurements of a quantity and average your results, the random error in your average is half of what it

===== Page 45 =====

 would be if you'd just taken a single measurement. Of course, you may still have systematic errors in your experiment. If you are consistently overestimating your quantity by an error in your experimental setup, that error won't reduce by repeated measurement!

A second application is in the theory of random walks. Imagine a drunken person staggering out of a pub and attempting to walk along a narrow street (which confines him or her to motion in one dimension). Let's pretend that with each inebriated step, the drunken person is equally likely to travel one step forwards or one step backwards. The effects of intoxication are such that each step is uncorrelated with the previous one. Thus the average distance travelled in a single step is \(\langle X \rangle = 0\) . After \(n\) such steps, we would have an expected total distance travelled of \(\langle Y \rangle = \sum \langle X_i \rangle = 0\) . However, in this case the root mean squared distance is more revealing. In this case \(\langle Y^2 \rangle = n \langle X^2 \rangle\) , so that the rms length of a random walk of \(n\) steps is \(\sqrt{n}\) times the length of a single step. This result will be useful in considering Brownian motion in Chapter 33.

### 3.7 Binomial distribution

A probability distribution, which is very important in thermal physics, is based on what is called a Bernoulli trial, an "experiment" with two possible outcomes. One outcome (which we will call "success") occurs with probability \(p\) and the other outcome (which we will call "failure") occurs with probability \(1 - p\) . An example of a Bernoulli trial is the tossing of a coin: one outcome is "heads", the other is "tails".

## Example 3.8

Let \(x\) be a random variable which takes the value 1 for success and 0 for failure. Then, assuming \(p\) to be the probability of success and using eqns 3.2, 3.3 and 3.21

\[\begin{array}{rcl}\langle x\rangle & = & 0\times (1 - p) + 1\times p = p\\ \langle x^2\rangle & = & 0^2\times (1 - p) + 1^2\times p = p\\ \sigma_x & = & \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{p(1 - p)}. \end{array} \quad (3.42)\]

The binomial distribution is the discrete probability distribution \(P(n,k)\) of getting \(k\) successes from \(n\) independent Bernoulli trials. The function \(P(n,k)\) can be worked out by realizing that (a) the probability of a particular series of \(k\) successes and \(n - k\) failures is \(p^k (1 - p)^{n - k}\) and (b) that there are \(n^k C_k\) ways of arranging \(k\) successes and \(n - k\) failures in a sequence. Thus \(P(n,k)\) is a product of these factors and hence

\[P(n,k) = {}^{n}C_{k}p^{k}(1 - p)^{n - k}. \quad (3.43)\]

===== Page 46 =====

 The binomial theorem of elementary algebra states that

\[(x + y)^n = \sum_{k = 0}^{n}nC_kx^k y^{n - k}. \quad (3.44)\]

Hence by writing \(x = p\) and \(y = 1 - p\) we can easily show that

\[\sum_{k = 1}^{n}P(n,k) = 1, \quad (3.45)\]

as required for a well- behaved probability distribution. Since the binomial distribution is the sum of \(n\) independent Bernoulli trials, then

\[\begin{array}{rcl}{\langle k\rangle} & = & {np}\\ {\sigma_k^2} & = & {np(1 - p).} \end{array} \quad (3.47)\]

The fractional width of the distribution is obtained by dividing the standard deviation by the mean and is given by \(\sigma_k / \langle k \rangle = \sqrt{(1 - p) / np}\) , which is proportional to \(1 / \sqrt{n}\) , and therefore decreases as \(n\) increases. This causes the binomial distribution to become more sharply peaked near the mean value as \(n\) increases, as shown in Fig. 3.3.

[Image: Graph showing three binomial probability distributions for p=0.4, plotted as P(n,k)/max(P(n,k)) versus k/n. The curves are for n=50 (broadest), n=500, and n=5000 (narrowest).]
Fig. 3.3 Binomial probability for \(p = 0.4\) . The three plots are for \(n = 50\) (outermost), \(n = 500\) and \(n = 5000\) (innermost) and are scaled so that their maximum amplitudes are the same. This demonstrates that as \(n\) increases, the fractional width decreases.

\(^{6}\mathrm{The}\) mean, \(\langle k \rangle\) is proportional to \(n\) . The standard deviation \(\sigma_k\) is proportional to \(\sqrt{n}\) . Both quantities increase with \(n\) , but the mean increases faster. The fractional width is the width of the distribution (the standard deviation) divided by the mean, and so decreases with \(n\) because the mean increases faster than the standard deviation.

## Example 3.9

Coin tossing with a fair coin. In this case, \(p = \frac{1}{2}\) .

For \(n = 16\) tosses, the expected number of heads is \(np = 8\) . The standard deviation is \(\sqrt{np(1 - p)} = 2\) , a quarter of the expected number. For \(n = 10^{20}\) tosses, the expected number of heads is \(np = 5 \times 10^{19}\) . The standard deviation is \(\sqrt{np(1 - p)} = 5 \times 10^{9}\) , ten orders of magnitude smaller than the expected number.

===== Page 47 =====

28 Probability

## Example 3.10

A one- dimensional random walk can be considered as a succession of \(n\) Bernoulli trials in which the choice is either a step forwards \(+L\) or a step backwards \(- L\) , each with equal probability (so \(p = \frac{1}{2}\) ). If there are \(n\) steps, \(k\) of which are forwards, the distance travelled is \(x = kL - (n - k)L = (2k - n)L\) . For a binomial distribution with \(p = \frac{1}{2}\) , \(\langle k \rangle = \frac{n}{2}\) , and \(\sigma_k^2 = \langle k^2 \rangle - \langle k \rangle^2 = np(1 - p) = \frac{n}{4}\) . This implies that \(\langle k^2 \rangle = \frac{n}{4} + \frac{n^2}{4}\) . Hence, the mean distance travelled is

\[\langle x\rangle = (2\langle k\rangle -n)L = 0, \quad (3.48)\]

as expected, since the random walker is just as likely to travel forwards as backwards. The mean squared distance travelled, \(\langle x^2 \rangle\) , is

\[\langle x^2 \rangle = (4\langle k^2 \rangle - 4\langle k \rangle n + n^2)L^2 = nL^2, \quad (3.49)\]

and hence \(\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \sqrt{n} L\) , in agreement with Section 3.6.

## Chapter summary

In this chapter, several introductory concepts in probability theory have been introduced.

The mean of a discrete probability distribution is given by

\[\langle x\rangle = \sum_{i}x_{i}P_{i},\]

and the mean of a continuous probability distribution is given by

\[\langle x\rangle = \int x P(x)\mathrm{d}x.\]

The variance is given by

\[\sigma_x^2 = \langle (x - \langle x \rangle)^2 \rangle ,\]

where \(\sigma_x\) is the standard deviation.

If \(y = ax + b\) , then \(\langle y \rangle = a\langle x \rangle + b\) and \(\sigma_y = a\sigma_x\) .

If \(u\) and \(v\) are independent random variables, then \(\langle uv \rangle = \langle u \rangle \langle v \rangle\) . In particular, if \(Y = X_1 + X_2 + \dots + X_n\) , where the \(X_i\) are all from the same distribution, \(\langle Y \rangle = n\langle x \rangle\) and \(\sigma_Y = \sqrt{n} \sigma_X\) .

The binomial distribution describes the probability of getting \(k\) successes from \(n\) independent Bernoulli trials. The mean of this distribution is \(\langle k \rangle = np\) and the variance is \(\sigma_k^2 = np(1 - p)\) .

===== Page 48 =====

 Further reading

There are many good books on probability theory and statistics. Recommended ones include Papoulis (1984), Saha (2003), Wall and Jenkins (2003), and Sivia and Skilling (2006).

## Exercises

(3.1) A throw of a regular die yields the numbers 1, 2, ..., 6, each with probability \(1 / 6\) . Find the mean, variance, and standard deviation of the numbers obtained.

(3.2) The mean birth-weight of babies in the UK is about \(3.2\mathrm{kg}\) with a standard deviation of \(0.5\mathrm{kg}\) . Convert these figures into pounds (lb), given that \(1\mathrm{kg} = 2.2\mathrm{lb}\) .

(3.3) This question is about a discrete probability distribution known as the Poisson distribution. Let \(x\) be a discrete random variable that can take the values \(0,1,2,\ldots\) A quantity \(x\) is said to be Poisson distributed if the probability \(P(x)\) of obtaining \(x\) is

\[P(x) = \frac{\mathrm{e}^{-m}m^x}{x!},\]

where \(m\) is a particular number (which we will show in part (b) of this exercise is the mean value of \(x\) ).

(a) Show that \(P(x)\) is a well-behaved probability distribution in the sense that

\[\sum_{x = 0}^{\infty}P(x) = 1.\]

(Why is this condition important?)

(b) Show that the mean value of the probability distribution is \(\langle x\rangle = \sum_{x = 0}^{\infty}xP(x) = m\) .

(c) The Poisson distribution is useful for describing very rare events, which occur independently and whose average rate does not change over the period of interest. Examples include birth defects measured per year, traffic accidents at a particular junction per year, numbers of typographical errors on a page, and the number of activations of a Geiger counter per minute. The first recorded example of a

Poisson distribution, the one which in fact motivated Poisson, was connected with the rare event of someone being kicked to death by a horse in the Prussian army. The number of horse- kick deaths of Prussian military personnel was recorded for each of 10 corps in each of 20 years from 1875- 1894 and the following data recorded:

<table>Number of deaths per year, per corpsObserved frequency01091652223341≥ 50Total200</table>

Calculate the mean number of deaths per year per corps. Compare the observed frequency with a calculated frequency assuming the number of deaths per year per corps are Poisson distributed with this mean.

(3.4) This question is about a continuous probability distribution known as the exponential distribution. Let \(x\) be a continuous random variable that can take any value \(x \geq 0\) . A quantity is said to be exponentially distributed if it takes values between \(x\) and \(x + dx\) with probability

\[P(x)\mathrm{d}x = A\mathrm{e}^{-x / \lambda}\mathrm{d}x,\]

where \(\lambda\) and \(A\) are constants.

(a) Find the value of \(A\) that makes \(P(x)\) a well- defined continuous probability distribution so

===== Page 49 =====

 that \(\int_{0}^{\infty}P(x)\mathrm{d}x = 1\) .

(b) Show that the mean value of the probability distribution is \(\langle x\rangle = \int_{0}^{\infty}xP(x)\mathrm{d}x = \lambda\) .

(c) Find the variance and standard deviation of this probability distribution. Both the exponential distribution and the Poisson distribution are used to describe similar processes, but for the exponential distribution \(x\) is the actual time between, for example, successive radioactive decays, successive molecular collisions, or successive horse-licking incidents (rather than, as with the Poisson distribution, \(x\) being simply the number of such events in a specified interval).

(3.5) If \(\theta\) is a continuous random variable which is uniformly distributed between 0 and \(\pi\) , write down an expression for \(P(\theta)\) . Hence find the value of the following averages:

(a) \(\langle \theta \rangle\) (b) \(\langle \theta - \frac{\pi}{2}\rangle\) (c) \(\langle \theta^2\rangle\) (d) \(\langle \theta^n\rangle\) (for the case \(n\geq 0\) (e) \(\langle \cos \theta \rangle\) (f) \(\langle \sin \theta \rangle\) (g) \(\langle |\cos \theta |\rangle\) (h) \(\langle \cos^2\theta \rangle\) (i) \(\langle \sin^2\theta \rangle\) (j) \(\langle \cos^2\theta +\sin^2\theta \rangle\)

Check that your answers are what you expect.

(3.6) In experimental physics, it is important to repeat measurements. Assuming that errors are random, show that if the error in making a single measurement of a quantity \(X\) is \(\Delta\) , the error obtained after using \(n\) measurements is \(\Delta /\sqrt{n}\) . (Hint: after \(n\) measurements, the procedure would be to take the \(n\) results and average them. So you require the standard deviation of the quantity \(Y = (X_1 + X_2 + \dots +X_n) / n\) where \(X_1, X_2, \ldots , X_n\) can be assumed to be independent, and each has standard deviation \(\Delta\) .

(3.7) (a) Show that the binomial distribution can be approximated by a Poisson distribution with mean \(np\) when \(n \gg 1\) but \(np\) remains small. (This therefore represents the case when \(p \ll 1\) so that "success" is a rare event.)

(b) A harder problem is to show that when \(n \gg 1\) and also \(np(1 - p) \gg 1\) the binomial distribution can be approximated by a Gaussian distribution with mean \(np\) and variance \(np(1 - p)\) . Assuming this to be the case, revisit the one-dimensional random walk in Example 3.10 and assume that the walker takes a

step when time \(t = n\tau\) ,where \(n\) is an integer. Writing \(D = L^2 /2\tau\) and using eqns 3.48 and 3.49 show that when \(t\gg \tau\) the probability of finding the particle between \(x\) and \(x + \mathrm{d}x\) is

\[P(x)\mathrm{d}x = \frac{1}{\sqrt{4\pi Dt}}\mathrm{e}^{-x^2 /4Dt}\mathrm{d}x. \quad (3.50)\]

[See also Appendix C.12 for an alternative derivation of eqn 3.50. ]

(c) Show that the standard deviation of the distribution in eqn 3.50 is given by \(\sigma_{x} = \sqrt{2Dt}\) . As the random walker "diffuses" backwards and forwards, you could try and define its diffusion speed by \(\sigma_{x} / t\) . This gives a speed that is proportional to \(t^{-1 / 2}\) and is clearly nonsense. The point about diffusion (the behaviour of random walkers) is that since \(\sigma_{x} \propto t^{1 / 2}\) you need 100 times as much time to diffuse a distance 10 times as big. A small molecule in water diffuses at a rate governed by \(D = 10^{-9} \mathrm{~m}^{2} \mathrm{~s}^{-1}\) . Estimate the time needed for this molecule to diffuse about (i) \(1 \mu \mathrm{m}\) (the width of a bacterium) and (ii) \(1 \mathrm{~cm}\) (the width of a test tube).

(3.8) This question introduces a rather efficient method for calculating the mean and variance of probability distributions. We define the moment generating function \(M(t)\) for a random variable \(x\) by

\[M(t) = \langle \mathrm{e}^{tx}\rangle . \quad (3.51)\]

Show that this definition implies that

\[\langle x^n\rangle = M^{(n)}(0), \quad (3.52)\]

where \(M^{(n)}(t) = \mathrm{d}^n M / \mathrm{d}t^n\) and further that the mean \(\langle x\rangle = M^{(1)}(0)\) and the variance \(\sigma_{x} = M^{(2)}(0) - [M^{(1)}(0)]^2\) . Hence show that:

(a) for a single Bernoulli trial,

\[M(t) = \mathrm{pe}^t +1 - p; \quad (3.53)\]

(b) for the binomial distribution,

\[M(t) = (p\mathrm{e}^t +1 - p)^n; \quad (3.54)\]

(c) for the Poisson distribution,

\[M(t) = \mathrm{e}^{m(\mathrm{e}^{t} - 1)}; \quad (3.55)\]

(d) for the exponential distribution,

\[M(t) = \frac{\lambda}{\lambda - t}. \quad (3.56)\]

Hence derive the mean and variance in each case and show that they agree with the results derived earlier.

===== Page 50 =====

1

Ludwig Boltzmann made major contributions to the applications of probability to thermal physics. He worked out much of the kinetic theory of gases independently of Maxwell, and

[Image: A portrait of Ludwig Boltzmann, a man with a full beard and glasses.]
Fig.3.4 Ludwig Boltzmann

together they share the credit for the Maxwell- Boltzmann distribution (see Chapter 5). Boltzmann was very much in awe of Maxwell all his life, and was one of the first to see the significance of Maxwell's theory of electromagnetism. "Was it a god who wrote these lines?" was Boltzmann's comment (quoting Goethe) on Maxwell's

work. Boltzmann's great insight was to recognize the statistical connection between thermodynamic entropy and the number of microstates, and through a series of technical papers was able to put the subject of statistical mechanics on a firm footing (his work was, independently, substantially extended by the American physicist Gibbs). Boltzmann was able to show that the second law of thermodynamics (considered in Part IV of this book) could be derived from the principles of classical mechanics, although the fact that classical mechanics makes no distinction between the direction of time meant that he had to smuggle in some assumptions, which mired his approach in some controversy. However, his derivation of what is known as the Boltzmann transport equation, which extends the ideas of the kinetic theory of gases, led to important developments in the electron transport theory of metals and in plasma physics.

Boltzmann also showed how to derive from the principles of thermodynamics the empirical law discovered by his teacher, Josef Stefan, which stated that the total radiation from a hot body was proportional to the fourth power of its absolute temperature (see Chapter 23).

Boltzmann was born in Vienna and did his doctorate in the kinetic theory of gases at the Uni

Boltzmann was born in Vienna and did his doctorate in the kinetic theory of gases at the University of Vienna under the supervision of Stefan. His subsequent career took him to Graz, Heidelberg, Berlin, then Vienna again, back to Graz, then Vienna, Leipzig, and finally back to Vienna. His own temperament was in accord with this physical restlessness and lack of stability. The moving around was also partly due to his difficult relationships with various other physicists, particularly Ernst Mach, who was appointed to a chair in Vienna (which occasioned Boltzmann's move to Leipzig in 1900), and Wilhelm Ostwald (whose opposition in Leipzig, together with Mach's retirement in 1901, motivated Boltzmann's return to Vienna in 1902, although not before Boltzmann had attempted suicide).

The notions of irreversibility inherent in thermodynamics led to some controversial implications, particularly to a Universe based on Newtonian mechanics, which are reversible in time. Boltzmann's approach used probability to understand how the behaviour of atoms determined the properties of matter. Ostwald, a physical chemist, who had himself recognized the importance of Gibbs' work (see Chapters 16, 20, and 22) to the extent that he had translated Gibbs' papers into German, was nevertheless a vigorous opponent of theories that involved what he saw as unmeasurable quantities. Ostwald was one of the last opponents of atomism, and became a dedicated opponent of Boltzmann. Ostwald himself was finally convinced of the validity of atoms nearly a decade after Boltzmann's death, by which time Ostwald had been awarded a Nobel Prize, in 1909, for his work on catalysis.

Boltzmann died just before his atomistic viewpoint became obviously vindicated and universally accepted. Boltzmann had suffered from depression and mood swings throughout his life. On holiday in Italy in 1906, Ludwig Boltzmann hanged himself while his wife and daughter were swimming. His famous equation relating entropy \(S\) with number of microstates \(W\) ( \(\Omega\) in this book) is

\[S = k\log W \quad (3.57)\]

and is engraved on his tombstone in Vienna. The constant \(k\) is called the Boltzmann constant, and is written as \(k_{\mathrm{B}}\) in this book.

===== Page 51 =====

4

## Temperature and the Boltzmann factor

4.1 Thermal equilibrium 32 4.2 Thermometers 33 4.3 The microstates and macrostates 35 4.4 A statistical definition of temperature 36 4.5 Ensembles 38 4.6 Canonical ensemble 38 4.7 Applications of the Boltzmann distribution 42 Chapter summary 45 Further reading 46 Exercises

In this chapter, we will explore the concept of temperature and show how it can be defined in a statistical manner. This leads to the idea of a Boltzmann distribution and a Boltzmann factor. Now of course the concept of temperature seems such an intuitively obvious one that you might wonder why we need a whole chapter to discuss it. Temperature is simply a measure of "hotness" or "coldness", so that we say that a hot body has a higher temperature than a cold one. For example, as shown in Fig. 4.1(a) if an object has temperature \(T_{1}\) and is hotter than a second body with temperature \(T_{2}\) , we expect that \(T_{1} > T_{2}\) . But what do these numbers \(T_{1}\) and \(T_{2}\) signify? What does temperature actually mean?

### 4.1 Thermal equilibrium

[Image: Three diagrams (a), (b), and (c). (a) shows two separate boxes, one labelled "hot T1" and the other "cold T2". (b) shows the two boxes connected by a thick line with an arrow pointing from the hot to the cold box, labelled "flow of heat". (c) shows the two connected boxes at the same final temperature Tf.]
Fig. 4.1 (a) Two objects at different temperatures. (b) The objects are now placed in thermal contact and heat flows from the hot object to the cold object. (c) After a long time, the two objects have the same final temperature \(T_{1}\) .

To begin to answer these questions, let us consider what happens if our hot and cold bodies are placed in thermal contact which means that they are able to exchange energy. As described in Chapter 2, heat is "thermal energy in transit" and experiment suggests that, if nothing else is going on, heat will always flow from the hotter body to the colder body, as shown in Fig. 4.1(b). This is backed up by our experience of the world: we always seem to burn ourselves when we touch something very hot (heat flows into us from the hot object) and become very chilled when we touch something very cold (heat flows out of us into the cold object). As heat flows from the hotter body to the colder body, we expect that the energy content and the temperatures of the two bodies will each change with time.

After some time being in thermal contact, we reach the situation in Fig. 4.1(c). The macroscopic properties of the two bodies are now no longer changing with time. If any energy flows from the first body to the second body, this is equal to the energy flowing from the second body to the first body; thus, there is no net heat flow between the two bodies. The two bodies are said to be in thermal equilibrium, which

===== Page 52 =====

 is defined by saying that the energy content and the temperatures of the two bodies will no longer be changing with time. We would expect that the two bodies in thermal equilibrium are now at the same temperature.

It seems that something irreversible has happened. Once the two bodies are put in thermal contact, the change from Fig. 4.1(b) to Fig. 4.1(c) proceeds inevitably. However, if we started with two bodies at the same temperature and placed them in thermal contact as in Fig. 4.1(c), the reverse process, i.e., ending up with Fig. 4.1(b), would not occur.2 Thus as a function of time, systems in thermal contact tend towards thermal equilibrium, rather than away from it. The process that leads to thermal equilibrium is called thermalization.

If various bodies are all in thermal equilibrium with each other, then we would expect that their temperatures should be the same. This idea is encapsulated in the zeroth law of thermodynamics:

# Zeroth law of thermodynamics

Two systems, each separately in thermal equilibrium with a third, are in equilibrium with each other.

You can tell by the numbering of the law that although it is an assumption that comes before the other laws of thermodynamics, it was added after the first three laws had been formulated. Early workers in thermodynamics took the content of the zeroth law as so obvious it hardly needed stating, and you might well agree with them! Nevertheless, the zeroth law gives us some justification for how to actually measure temperature: we place the body whose temperature needs to be measured in thermal contact with a second body, which displays some property that has a well- known dependence on temperature, and wait for them to come into thermal equilibrium. The second body is called a thermometer. The zeroth law then guarantees that if we have calibrated this second body against any other standard thermometer, we should always get consistent results. Thus, a more succinct statement of the zeroth law is: "thermometers work".

### 4.2 Thermometers

We now make some remarks concerning thermometers.

For a thermometer to work well, its heat capacity must be much lower than that of the object whose temperature one wants to measure. If this is not the case, the action of measurement (placing the thermometer in thermal contact with the object) could alter the temperature of the object. A common type of thermometer utilizes the fact that liquids expand when they are heated. Galileo Galilei used a water thermometer based on this principle in 1593, but it was Daniel Gabriel Fahrenheit (1686- 1736) who devised thermometers based on al

2 Thermal processes thus define an arrow of time. We will return to this point later in Section 34.5.

===== Page 53 =====

200 100 200 400 600 800 T (K)

[Image: A graph showing resistance R (in Ohms) versus temperature T (in Kelvin). A straight line starts from the origin and goes up to the right, indicating R is proportional to T.]
Fig. 4.2 The temperature dependence of the resistance of a typical platinum sensor.

[Image: A graph showing resistance R (in kOhms) versus temperature T (in Kelvin) on a logarithmic scale. The curve goes down and flattens out as T increases.]
Fig. 4.3 The temperature dependence of the resistance of a typical RuO \(_2\) sensor.

[Image: A graph showing vapour pressure p (in 10^5 Pa) versus temperature T (in Kelvin) for ^4He. A curve goes up from zero. A dashed line indicates atmospheric pressure, and another dashed line drops down to the corresponding boiling point temperature on the x-axis.]
Fig. 4.4 The vapour pressure of \(^4\mathrm{He}\) as a function of temperature. The dashed line labels atmospheric pressure and the corresponding boiling point for liquid \(^4\mathrm{He}\) .

\(^4\mathrm{We}\) will introduce the Carnot engine in Section 13.2. The definition of temperature that arises from this is based on eqn 13.7 and states that the ratio of the temperature of a body to the heat flow from it is a constant in a reversible Carnot cycle.

coho1 (1709) and mercury (1714) that bear most resemblance to modern household thermometers. He introduced his famous temperature scale, which was then superseded by the more logical scheme devised by Anders Celsius (1701- 1744).

Another method is to measure the electrical resistance of a material which has a well- known dependence of resistance on temperature. Platinum is a popular choice since it is chemically resistant, ductile (so can be easily drawn into wires) and has a large temperature- coefficient of resistance; see Fig. 4.2. Other commonly used thermometers are based on doped germanium (a semiconductor that is very stable after repeated thermal cycling), carbon sensors and \(\mathrm{RuO_2}\) (in contrast with platinum, the electrical resistance of these thermometers increases as they are cooled; see Fig. 4.3).

Using the ideal gas equation (eqn 1.12), one can measure the temperature of a gas by measuring its pressure with its volume fixed (or by measuring its volume with its pressure fixed). This works well as far as the ideal gas equation works, although at very low temperature gases liquefy and show departures from the ideal gas equation.

Another method, which is useful in cryogenics, is to have a liquid coexisting with its vapour and to measure the vapour pressure. For example, liquid helium ( \(^4\mathrm{He}\) , the most common isotope) has the vapour pressure dependence on temperature shown in Fig. 4.4.

All of these methods use some measurable property, like resistance or pressure, which depends in some, sometimes complicated, manner on temperature. However, none of them is completely linear across the entire temperature range of interest: mercury solidifies at very low temperature and becomes gaseous at very high temperature, the resistance of platinum saturates at very low temperature and platinum wire melts at very high temperature, etc. However, against what standard thermometer can one possibly assess the relative merits of these different thermometers? Which thermometer is perfect and gives the real thing, against which all other thermometers should be judged?

It is clear that we need some absolute definition of temperature based on fundamental physics. In the nineteenth century, one such definition was found, and it was based on a hypothetical machine, which has never been built, called a Carnot engine. Subsequently, it was found that temperature could be defined in terms of a purely statistical argument using ideas from probability theory, and this is the definition we will use, which we introduce in Section 4.4. In the following section we will introduce the terminology of microstates and macrostates that will be needed for this argument.

===== Page 54 =====

4.3 The microstates and macrostates

To make the distinction between microstates and macrostates, consider the following example.

## Example 4.1

Imagine that you have a large box containing 100 identical coins. With the lid on the box, you give it a really good long and hard shake, so that you can hear the coins flipping, rattling, and being generally tossed around. Now you open the lid and look inside the box. Some of the coins will be lying with heads facing up and some with tails facing up. There are lots of possible configurations that one could achieve \((2^{100}\) to be precise, which is approximately \(10^{30}\) ) and we will assume that each of these different configurations is equally likely. Each possible configuration therefore has a probability of approximately \(10^{- 30}\) . We will call each particular configuration a microstate of this system. An example of one of these microstates would be: "Coin number 1 is heads, coin number 2 is heads, coin number 3 is tails, etc". To identify a microstate, you would somehow need to identify each coin individually, which would be a bit of a bore. However, probably the way you would categorize the outcome of this experiment is by simply counting the number of coins which are heads and the number which are tails (e.g., 53 heads and 47 tails). This sort of categorization we call a macrostate of this system. The macrostates are not equally likely. For example, of the \(\approx 10^{30}\) possible individual configurations (microstates),

\[\mathrm{the~number~with~50~heads~and~50~tails~} = \frac{100!}{(50!)^2}\approx 4\times 10^{27},\] \[\mathrm{the~number~with~53~heads~and~47~tails~} = \frac{100!}{53147!}\approx 3\times 10^{27},\] \[\mathrm{the~number~with~90~heads~and~10~tails~} = \frac{100!}{90!10!}\approx 10^{13},\mathrm{and}\] \[\mathrm{the~number~with~100~heads~and~0~tails~} = 1.\]

Thus, the outcome with all 100 coins with their heads facing up is a very unlikely outcome. This macrostate contains only a single microstate. If that were the result of the experiment, you would probably conclude that (i) your shaking had not been very vigorous and that (ii) someone had carefully prepared the coins to be lying heads up at the start of the experiment. Of course, a particular microstate with 53 heads and 47 tails is just as unlikely; it is just that there are about \(3\times 10^{27}\) other microstates having 53 heads and 47 tails that look extremely similar.

This simple example shows two crucial points:

The system could be described by a very large number of equally likely microstates. What you actually measure is a property of the macrostate of the

In our example, the measurement was opening the large box and counting the number of coins that were heads and those that were tails.

===== Page 55 =====

36 Temperature and the Boltzmann factor

system. The macrostates are not equally likely, because different macrostates correspond to different numbers of microstates.

The most likely macrostate that the system will find itself in is the one that corresponds to the largest number of microstates.

Thermal systems behave in a very similar way to the example we have just considered. To specify a microstate for a thermal system, you would need to give the microscopic configurations (perhaps position and velocity, or perhaps energy) of each and every atom in the system. In general it is impossible to measure which microstate the system is in. The macrostate of a thermal system on the other hand would be specified only by giving the macroscopic properties of the system, such as the pressure, the total energy, or the volume. A macroscopic configuration, such as a gas with pressure \(10^{5}\) Pa in a volume \(1\mathrm{m}^{3}\) , would be associated with an enormous number of microstates. In the next section, we are going to give a statistical definition of temperature, which is based on the idea that a thermal system can have a large number of equally likely microstates, but you are only able to measure the macrostate of the system. At this stage, we are not going to worry about what the microstates of the system actually are; we are simply going to posit their existence and say that if the system has energy \(E\) , then it could be in any one of \(\Omega (E)\) equally likely microstates, where \(\Omega (E)\) is some enormous number.

[Image: Two boxes labelled 1 and 2, connected by a small pipe. Box 1 has energy E1 and Omega1(E1). Box 2 has energy E2 and Omega2(E2).]
Fig. 4.5 Two systems able only to exchange energy between themselves.

We return to our example of Section 4.1 and consider two large systems that can exchange energy with each other, but not with anything else (Fig. 4.5). In other words, the two systems are in thermal contact with each other, but thermally isolated from their surroundings. The first system has energy \(E_{1}\) and the second system has energy \(E_{2}\) . The total energy \(E = E_{1} + E_{2}\) is therefore assumed fixed since the two systems cannot exchange energy with anything else. Hence the value of \(E_{1}\) is enough to determine the macrostate of this joint system. Each of these systems can be in a number of possible microstates. This number of possible microstates could in principle be calculated as in Section 1.4 (and in particular, Example 1.3) and will be a very large, combinatorial number, but we will not worry about the details of this. Let us assume that the first system can be in any one of \(\Omega_{1}(E_{1})\) microstates and the second system can be in any one of \(\Omega_{2}(E_{2})\) microstates. Thus the whole system can be in any one of \(\Omega_{1}(E_{1})\Omega_{2}(E_{2})\) microstates.6

The systems are able to exchange energy with each other, and we will assume that they have been left in the condition of being joined together for a sufficiently long time that they have come into thermal equilibrium. This means that \(E_{1}\) and \(E_{2}\) have come to fixed values. The crucial insight which we must make is that a system will appear to choose a macroscopic configuration that maximizes the number of microstates. This idea is based on the following assumptions:

===== Page 56 =====

1 Each one of the possible microstates of a system is equally likely to occur; (2) The system's internal dynamics are such that the microstates of the system are continually changing; (3) Given enough time, the system will explore all possible microstates and spend an equal time in each of them.7

These assumptions imply that the system will most likely be found in a configuration that is represented by the most microstates. For a large system our phrase "most likely" becomes "absolutely, overwhelmingly likely"; what appears at first sight to be a somewhat weak, probabilistic statement (perhaps on the same level as a five- day weather forecast) becomes an utterly reliable prediction on whose basis you can design an aircraft engine and trust your life to it!

For our problem of two connected systems, the most probable division of energy between the two systems is the one that maximizes \(\Omega_{1}(E_{1})\Omega_{2}(E_{2})\) , because this will correspond to the greatest number of possible microstates. Our systems are large and hence we can use calculus to study their properties; we can therefore consider making infinitesimal changes to the energy of one of the systems and seeing what happens. Therefore, we can maximize this expression with respect to \(E_{1}\) by writing

\[\frac{\mathrm{d}}{\mathrm{d}E_1} (\Omega_1(E_1)\Omega_2(E_2)) = 0 \quad (4.1)\]

and hence, using standard rules for the differentiation of a product,

\[\Omega_{2}(E_{2})\frac{\mathrm{d}\Omega_{1}(E_{1})}{\mathrm{d}E_{1}} +\Omega_{1}(E_{1})\frac{\mathrm{d}\Omega_{2}(E_{2})}{\mathrm{d}E_{2}}\frac{\mathrm{d}E_{2}}{\mathrm{d}E_{1}} = 0. \quad (4.2)\]

Since the total energy \(E = E_{1} + E_{2}\) is assumed fixed, this implies that

\[\mathrm{d}E_{1} = -\mathrm{d}E_{2}, \quad (4.3)\]

and hence

\[\frac{\mathrm{d}E_2}{\mathrm{d}E_1} = -1, \quad (4.4)\]

so that eqn 4.2 becomes

\[\frac{1}{\Omega_1}\frac{\mathrm{d}\Omega_1}{\mathrm{d}E_1} -\frac{1}{\Omega_2}\frac{\mathrm{d}\Omega_2}{\mathrm{d}E_2} = 0, \quad (4.5)\]

and hence

\[\frac{\mathrm{d}\ln\Omega_1}{\mathrm{d}E_1} = \frac{\mathrm{d}\ln\Omega_2}{\mathrm{d}E_2}. \quad (4.6)\]

This condition defines the most likely division of energy between the two systems if they are allowed to exchange energy since it maximizes the total number of microstates. This division of energy is, of course, more usually called "being at the same temperature", and so we identify \(\mathrm{d}\ln \Omega /\mathrm{d}E\) with the temperature \(T\) (so that \(T_{1} = T_{2}\) ). We will define the temperature \(T\) by

\[\frac{1}{k_{\mathrm{B}}T} = \frac{\mathrm{d}\ln\Omega}{\mathrm{d}E}, \quad (4.7)\]

===== Page 57 =====

38 Temperature and the Boltzmann factor

We will see later (Section 14.5) that in statistical mechanics, the quantity \(k_{\mathrm{B}}\ln \Omega\) is called the entropy, \(S\) , and hence eqn 4.7 is equivalent to

\[\frac{1}{T} = \frac{\mathrm{d}S}{\mathrm{d}E}.\]

where \(k_{\mathrm{B}}\) is the Boltzmann constant, which is given by

\[k_{\mathrm{B}} = 1.3807\times 10^{-23}\mathrm{J}\mathrm{K}^{-1}. \quad (4.8)\]

With this choice of constant, \(T\) has its usual interpretation and is measured in kelvin. We will show in later chapters that this choice of definition leads to experimentally verifiable consequences, such as the correct expression for the pressure of a gas.

### 4.5 Ensembles

We are using probability to describe thermal systems and our approach is to imagine repeating an experiment to measure a property of a system again and again because we cannot control the microscopic properties (as described by the system's microstates). In an attempt to formalize this, Josiah Willard Gibbs in 1878 introduced a concept known as an ensemble. This is an idealization in which one considers making a large number of mental "photocopies" of the system, each one of which represents a possible state the system could be in. There are three main ensembles that tend to be used in thermal physics:

(1) The microcanonical ensemble: an ensemble of systems that each have the same fixed energy.
(2) The canonical ensemble: an ensemble of systems, each of which can exchange its energy with a large reservoir of heat. As we shall see, this fixes (and defines) the temperature of the system.
(3) The grand canonical ensemble: an ensemble of systems, each of which can exchange both energy and particles with a large reservoir. (This fixes the system's temperature and a quantity known as the system's chemical potential. We will not consider this again until Chapter 22 and it can be ignored for the present.)

[Image: A large box labelled "reservoir at T" with energy E-epsilon, connected to a small circle labelled "system" with energy epsilon.]
Fig. 4.6 A large reservoir (or heat bath) at temperature \(T\) connected to a small system.

In the next section we will consider the canonical ensemble in more detail and use it to derive the probability of a system at a fixed temperature being in a particular microstate.

### 4.6 Canonical ensemble

We now consider two systems coupled as before in such a way that they can exchange energy (Fig. 4.6). This time, we will make one of them enormous, and call it the reservoir (also known as a heat bath). It is so large that you can take quite a lot of energy out of it and yet it can remain at essentially the same temperature. In the same way, if you stand on the seashore and take an eggcupful of water out of the ocean, you do not notice the level of the ocean going down (although it does in fact go down, but by an unmeasurably small amount). The number of ways of arranging the quanta of energy of the reservoir will therefore be colossal. The other system is small and will be known as the system.

===== Page 58 =====

4.6 Canonical ensemble 39

We will assume that for each allowed energy of the system there is only a single microstate, and therefore the system always has a value of \(\Omega\) equal to one. Once again, we fix \(^{8}\) the total energy of the system plus reservoir to be \(E\) . The energy of the reservoir is taken to be \(E - \epsilon\) while the energy of the system is taken to be \(\epsilon\) . This situation of a system in thermal contact with a large reservoir is very important and is known as the canonical ensemble. \(^{9}\)

The probability \(P(\epsilon)\) that the system has energy \(\epsilon\) is proportional to the number of microstates that are accessible to the reservoir multiplied by the number of microstates that are accessible to the system. This is therefore

\[P(\epsilon)\propto \Omega (E - \epsilon)\times 1. \quad (4.9)\]

Since we have an expression for temperature in terms of the logarithm of \(\Omega\) (eqn 4.7), and since \(\epsilon \ll E\) , we can perform a Taylor expansion \(^{10}\) of \(\ln \Omega (E - \epsilon)\) around \(\epsilon = 0\) , so that

\[\ln \Omega (E - \epsilon) = \ln \Omega (E) - \frac{\mathrm{d}\ln\Omega(E)}{\mathrm{d}E}\epsilon +\dots \quad (4.10)\]

and so now using eqn. 4.7, we have

\[\ln \Omega (E - \epsilon) = \ln \Omega (E) - \frac{\epsilon}{k_{\mathrm{B}}T} +\dots , \quad (4.11)\]

where \(T\) is the temperature of the reservoir. In fact, we can neglect the further terms in the Taylor expansion (see Exercise 4.4) and hence eqn 4.11 becomes

\[\Omega (E - \epsilon) = \Omega (E)\mathrm{e}^{-\epsilon /k_{\mathrm{B}}T}. \quad (4.12)\]

Using eqn 4.9 we thus arrive at the following result for the probability distribution describing the system, which is given by

\[P(\epsilon)\propto \mathrm{e}^{-\epsilon /k_{\mathrm{B}}T}. \quad (4.13)\]

Since the system is now in equilibrium with the reservoir, it must also have the same temperature as the reservoir. But notice that although the system therefore has fixed temperature \(T\) , its energy \(\epsilon\) is not a constant but is governed by the probability distribution in eqn 4.13 (and is plotted in Fig. 4.7). This is known as the Boltzmann distribution and also as the canonical distribution. The term \(\mathrm{e}^{-\epsilon /k_{\mathrm{B}}T}\) is known as a Boltzmann factor.

We now have a probability distribution that describes exactly how a small system behaves when coupled to a large reservoir at temperature \(T\) . The system has a reasonable chance of achieving an energy \(\epsilon\) that is less than \(k_{\mathrm{B}}T\) , but the exponential in the Boltzmann distribution quickly begins to reduce the probability of achieving an energy much greater than \(k_{\mathrm{B}}T\) . However, to quantify this properly we need to normalize the probability distribution. If a system is in contact with a reservoir and has a microstate \(r\) with energy \(E_{r}\) , then

\[P(\mathrm{microstate} r) = \frac{\mathrm{e}^{-E_r / k_{\mathrm{B}}T}}{\sum_i \mathrm{e}^{-E_i / k_{\mathrm{B}}T}}, \quad (4.14)\]

\(^{8}\) In this respect, the system plus reservoir as a whole can be considered as being in the microcanonical ensemble, which has fixed energy, with each of the microstates of the combined entity being equally likely.

\(^{9}\) "Canonical" means part of the "canon", the store of generally accepted things one should know. It's an odd word, but we're stuck with it. Focussing on a system whose energy is not fixed, but which can exchange energy with a big reservoir, is something we do a lot in thermal physics and is therefore in some sense canonical. \(^{10}\) See Appendix B.

[Image: A graph of P(epsilon) versus epsilon. It is a decaying exponential curve. A dashed curve is also shown, corresponding to a higher temperature.]
Fig. 4.7 The Boltzmann distribution. The dashed curve corresponds to a higher temperature than the solid curve.

===== Page 59 =====

40 Temperature and the Boltzmann factor

The partition function is the subject of Chapter 20.

where the sum in the denominator makes sure that the probability is normalized. The sum in the denominator is called the partition function and is given the symbol \(Z\) .

We have derived the Boltzmann distribution on the basis of statistical arguments that show that this distribution of energy maximizes the number of microstates. It is instructive to verify this for a small system, so the following example presents the results of a computer experiment to demonstrate the validity of the Boltzmann distribution.

## Example 4.2

To illustrate the statistical nature of the Boltzmann distribution, let us play a game in which quanta of energy are distributed in a lattice. We choose a lattice of 400 sites, arranged for convenience on a \(20 \times 20\) grid. Each site initially contains a single energy quantum, as shown in Fig. 4.8(a). The adjacent histogram shows that there are 400 sites with one quantum on each. We now choose a site at random and remove the quantum from that site and place it on a second, randomly chosen site. The resulting distribution is shown in Fig. 4.8(b), and the histogram shows that we now have 398 sites each with 1 quantum, 1 site with no quanta and 1 site with two quanta. This redistribution process is repeated many times and the resulting distribution is as shown in Fig. 4.8(c). The histogram describing this looks very much like a Boltzmann exponential distribution.

The initial distribution shown in Fig. 4.8(a) is very equitable and gives a distribution of energy quanta between sites of which Karl Marx would have been proud. It is however very statistically unlikely because it is associated with only a single microstate, i.e., \(\Omega = 1\) . There are many more microstates associated with other macrostates, as we shall now show. For example, the state obtained after a single iteration, such as the one shown in Fig. 4.8(b), is much more likely, since there are 400 ways to choose the site from which a quantum has been removed, and then 399 ways to choose the site to which a quantum is added; hence \(\Omega = 400 \times 399 = 19600\) for this histogram (which contains 398 singly occupied sites, one site with zero quanta and one site with two quanta). The state obtained after many iterations in Fig. 4.8(c) is much, much more likely to occur if quanta are allowed to rearrange randomly as the number of microstates associated with the Boltzmann distribution is absolutely enormous. The Boltzmann distribution is simply a matter of probability.

In the model considered in this example, the role of temperature is played by the total number of energy quanta in play. So, for example, if instead the initial arrangement had been two quanta per site rather than one quantum per site, then after many iterations one would obtain the arrangement shown in Fig. 4.8(d). Since the initial arrangement has more energy, the final state is a Boltzmann distribution with a higher temperature (leading to more sites with more energy quanta).

===== Page 60 =====

[Image: Four 20x20 grids (a, b, c, d) showing the distribution of quanta. Next to each grid is a histogram. (a) All sites have 1 quantum. Histogram shows one bar at 1. (b) One site has 0, one has 2, the rest have 1. Histogram shows bars at 0, 1, 2. (c) After many iterations, the grid shows random-looking numbers. The histogram is a decaying distribution, resembling a Boltzmann distribution. (d) A similar result to (c), but starting with 2 quanta per site, leading to a distribution with a larger mean and variance.]
Fig. 4.8 Energy quanta distributed on a \(20\times 20\) lattice. (a) In the initial state, one quantum is placed on each site. (b) A site is chosen at random and a quantum is removed from that site and placed on a second randomly chosen site. (c) After many repetitions of this process, the resulting distribution resembles a Boltzmann distribution. (d) The analogous final distribution following redistribution from an initial state with two quanta per site. The adjacent histogram in each case shows how many quanta are placed on each site.

Let us now start with a bigger lattice, now containing \(10^{6}\) sites, and place a quantum of energy on each site. We randomly move quanta from site to site as before, and in our computer program we let this proceed for a large number of iterations (in this case \(10^{10}\) ). The resulting distribution is shown in Fig. 4.9, which displays a graph on a logarithmic scale of the number of sites \(N\) with \(n\) quanta. The straight line is a fit to the expected Boltzmann distribution. This example is considered in more detail in the exercises.

===== Page 61 =====

[Image: A log-linear plot of N versus n. The data points fall on a straight line, indicating an exponential distribution. Error bars are shown, increasing for larger n.]
Fig. 4.9 The final distribution for a lattice of size \(1000 \times 1000\) with one quantum of energy initially placed on each site. The error bars are calculated by assuming Poisson statistics and have length \(\sqrt{N}\) , where \(N\) is the number of sites having \(n\) quanta.

### 4.7 Applications of the Boltzmann distribution

To illustrate the application of the Boltzmann distribution, we now conclude this chapter with some examples. These examples involve little more than a simple application of the Boltzmann distribution, but they have important consequences.

Before we do so, let us introduce a piece of shorthand. Since we will often need to write the quantity \(1 / k_{\mathrm{B}}T\) , we will use the shorthand

\[\beta \equiv \frac{1}{k_{\mathrm{B}}T}, \quad (4.15)\]

so that the Boltzmann factor becomes simply \(\mathrm{e}^{- \beta E}\) . Using this shorthand, we can also write eqn 4.7 as

\[\beta = \frac{\mathrm{d}\ln\Omega}{\mathrm{d}E}. \quad (4.16)\]

## Example 4.3

## The two state system

The first example is one of the simplest one can think of. In a two- state system, there are only two states, one with energy 0 and the other with energy \(\epsilon > 0\) . What is the average energy of the system?

===== Page 62 =====

 Solution:

The probability of being in the lower state is given by eqn 4.14, so we have

\[P(0) = \frac{1}{1 + \mathrm{e}^{-\beta\epsilon}}. \quad (4.17)\]

Similarly, the probability of being in the upper state is

\[P(\epsilon) = \frac{\mathrm{e}^{-\beta\epsilon}}{1 + \mathrm{e}^{-\beta\epsilon}}. \quad (4.18)\]

The average energy \(\langle E \rangle\) of the system is then

\[\begin{array}{rcl}{\langle E\rangle} & = & {0\cdot P(0) + \epsilon \cdot P(\epsilon)}\\ {} & = & {\epsilon \frac{\mathrm{e}^{-\beta\epsilon}}{1 + \mathrm{e}^{-\beta\epsilon}}}\\ {} & = & {\frac{\epsilon}{\mathrm{e}^{\beta\epsilon} + 1}.} \end{array} \quad (4.19)\]

This expression (plotted in Fig. 4.10) behaves as expected: when \(T\) is very low, \(k_{\mathrm{B}}T \ll \epsilon\) , and so \(\beta \epsilon \gg 1\) and \(\langle E \rangle \to 0\) (the system is in the ground state). When \(T\) is very high, \(k_{\mathrm{B}}T \gg \epsilon\) , and so \(\beta \epsilon \ll 1\) and \(\langle E \rangle \to \epsilon /2\) (both levels are equally occupied on average).

[Image: A plot of average energy <E> versus epsilon / k_B T. The curve starts at epsilon/2 at x=0 and decays towards 0 as x increases.]
Fig. 4.10 The value of \(\langle E \rangle\) as a function of \(\epsilon /k_{\mathrm{B}}T = \beta \epsilon\) , following eqn 4.19. As \(T \to \infty\) , each energy level is equally likely to be occupied and so \(\langle E \rangle = \epsilon /2\) . When \(T \to 0\) , only the lower level is occupied and \(\langle E \rangle = 0\) .

## Example 4.4

## Isothermal atmosphere

Estimate the number of molecules in an isothermal \(^{11}\) atmosphere as a function of height.

Solution:

This is our first attempt at modelling the atmosphere, where we make the rather naive assumption that the temperature of the atmosphere is constant. Consider a molecule in an ideal gas at temperature \(T\) in the presence of gravity. The probability \(P(z)\) of the molecule of mass \(m\) being at height \(z\) is given by

\[P(z)\propto \mathrm{e}^{-mgz / k_{\mathrm{B}}T}, \quad (4.20)\]

because its potential energy is \(mgz\) . Hence, the number density \(^{12}\) of molecules \(n(z)\) at height \(z\) , which will be proportional to the probability function \(P(z)\) of finding a molecule at height \(z\) , is given by

\[n(z) = n(0)\mathrm{e}^{-mgz / k_{\mathrm{B}}T}. \quad (4.21)\]

This result (plotted in Fig. 4.11) agrees with a more pedestrian derivation, which goes as follows: consider a layer of gas between height \(z\) and \(z + \mathrm{d}z\) . There are \(n \mathrm{~d}z\) molecules per unit area in this layer, and therefore they exert a pressure (force per unit area)

\[\mathrm{d}p = -n\mathrm{d}z\cdot mg \quad (4.22)\]

\(^{11}\) "Isothermal" means constant temperature. A more sophisticated treatment of the atmosphere is postponed until Section 12.4; see also Chapter 37.

\(^{12}\) Number density means number per unit volume.

===== Page 63 =====

44 Temperature and the Boltzmann factor

downwards (because each molecule has weight \(mg\) ). We note in passing that eqn 4.22 can be rearranged using \(\rho = nm\) to show that

\[\mathrm{d}p = -\rho g\mathrm{d}z, \quad (4.23)\]

which is known as the hydrostatic equation. Using the ideal gas law (in the form derived in Chapter 6), which is \(p = nk_{\mathrm{B}}T\) , we have that

\[\frac{\mathrm{d}n}{n} = -\frac{mg}{k_{\mathrm{B}}T}\mathrm{d}z, \quad (4.24)\]

which is a simple differential equation yielding

\[\ln n(z) - \ln n(0) = -\frac{mg}{k_{\mathrm{B}}T} z, \quad (4.25)\]

so that, again, we have

\[n(z) = n(0)\mathrm{e}^{-mgz / k_{\mathrm{B}}T}. \quad (4.26)\]

[Image: A plot of height z versus number density n(z). The curve starts at n(0) and decays exponentially as z increases.]
Fig. 4.11 The number density \(n(z)\) of molecules at height \(z\) for an isothermal atmosphere.

Our prediction is that the number density falls off exponentially with height, but the reality is somewhat different. Our assumption of constant \(T\) is at fault (the temperature falls as the altitude increases, at least initially) and we will return to this problem in Section 12.4, and also in Chapter 37.

## Example 4.5

## Chemical reactions

Many chemical reactions have an activation energy \(E_{\mathrm{act}}\) of about \(\frac{1}{2}\mathrm{eV}\) . At \(T = 300\mathrm{K}\) , which is about room temperature, the probability that a particular reaction occurs is proportional to

\[\exp (-E_{\mathrm{act}} / (k_{\mathrm{B}}T)). \quad (4.27)\]

If the temperature is increased to \(T + \Delta T = 310\mathrm{K}\) , the probability increases to

\[\exp (-E_{\mathrm{act}} / (k_{\mathrm{B}}(T + \Delta T)), \quad (4.28)\]

which is larger by a factor

\[\begin{array}{rcl}\frac{\exp(-E_{\mathrm{act}} / (k_{\mathrm{B}}(T + \Delta T))}{\exp(-E_{\mathrm{act}} / (k_{\mathrm{B}}T))} & = & \exp \left(-\frac{E_{\mathrm{act}}}{k_{\mathrm{B}}} [(T + \Delta T)^{-1} - T^{-1}]\right)\\ & \approx & \exp \left(\frac{E_{\mathrm{act}}}{k_{\mathrm{B}}T}\frac{\Delta T}{T}\right)\\ & \approx & 2. \end{array} \quad (4.29)\]

Hence many chemical reactions roughly double in speed when the temperature is increased by about \(10\mathrm{K}\) .

===== Page 64 =====

4.7 Applications of the Boltzmann distribution 45

## Example 4.6

## The Sun

The SunThe main fusion reaction in the Sun \(^{13}\) is

\[\mathrm{p^{+} + p^{+}\rightarrow d^{+} + e^{+} + \bar{\nu}} \quad (4.30)\]

but the main barrier to this occuring is the electrostatic repulsion of the two protons coming together in the first place. This energy is

\[E = \frac{e^2}{4\pi\epsilon_0r}, \quad (4.31)\]

which for \(r = 10^{- 15}\mathrm{m}\) the distance which they must approach each other for fusion to occur, \(E\) is about \(1\mathrm{MeV}\) . The Boltzmann factor for this process at a temperature of \(T\approx 10^{7}\mathrm{K}\) (at the centre of the Sun) is

\[\mathrm{e}^{-E / k_{\mathrm{B}}T}\approx 10^{-400}. \quad (4.32)\]

This is extremely small, suggesting that the Sun is unlikely to undergo fusion. However, our lazy sunny afternoons are saved by the fact that quantum mechanical tunnelling allows the protons to pass through this barrier vastly more often than this calculation predicts that they could pass over the top of it.

## Chapter summary

The temperature \(T\) of a system is given by

\[\beta \equiv \frac{1}{k_{\mathrm{B}}T} = \frac{\mathrm{d}\ln\Omega}{\mathrm{d}E},\]

where \(k_{\mathrm{B}}\) is the Boltzmann constant, \(E\) is its energy, and \(\Omega\) is the number of microstates (i.e., the number of ways of arranging the quanta of energy in the system).

The microcanonical ensemble is an idealized collection of systems that each have the same fixed energy.

The canonical ensemble is an idealized collection of systems, each of which can exchange its energy with a large reservoir of heat.

For the canonical ensemble, the probability that a particular system has energy \(\epsilon\) is given by

\[P(\epsilon)\propto e^{-\beta \epsilon}\]

(Boltzmann distribution), and the factor \(e^{-\beta \epsilon}\) is known as the Boltzmann factor. Its use has been illustrated for a number of physical situations.

===== Page 65 =====

46 Exercises

## Further reading

Methods of measuring temperature are described in Pobell (1996) and White and Meeson (2002).

## Exercises

(4.1) Check that the probability in eqn 4.14 is normalized, so that the sum of all possible probabilities is one.

(4.2) For the two- state system described in Example 4.3, derive an expression for the variance of the energy.

(4.3) A system comprises \(N\) states, which can have energy 0 or \(\Delta\) . Show that the number of ways \(\Omega (E)\) of arranging the total system to have energy \(E = r\Delta\) (where \(r\) is an integer) is given by

\[\Omega (E) = \frac{N!}{r!(N - r)!}. \quad (4.33)\]

Now remove a small amount of energy \(s\Delta\) from the system, where \(s\ll r\) . Show that

\[\Omega (E - \epsilon)\approx \Omega (E)\frac{r^s}{(N - r)^s}, \quad (4.34)\]

and hence show that the system has temperature \(T\) given by

\[\frac{1}{k_{\mathrm{B}}T} = \frac{1}{\Delta}\ln \left(\frac{N - r}{r}\right). \quad (4.35)\]

Sketch \(k_{\mathrm{B}}T\) as a function of \(r\) from \(r = 0\) to \(r = N\) and explain the result.

(4.4) In eqn 4.11, we neglected the next term in the Taylor expansion, which is

\[\frac{\mathrm{d}^2\ln\Omega}{\mathrm{d}E^2}\epsilon^2. \quad (4.36)\]

Show that this term equals

\[-\frac{\epsilon^2}{k_{\mathrm{B}}T^2}\frac{\mathrm{d}T}{\mathrm{d}E}, \quad (4.37)\]

and hence show that it can be neglected compared with the first two terms if the reservoir is large. (Hint: how much should the temperature of the reservoir change when you change its energy by order \(\epsilon\) ?)

(4.5) A photon of visible light with energy \(2\mathrm{eV}\) is absorbed by a macroscopic body held at room temperature. By what factor does \(\Omega\) for the macroscopic body change? Repeat the calculation for a photon that originated from an FM radio transmitter.

(4.6) Figure 4.10 is a plot of \(\langle E \rangle\) as a function of \(\beta \epsilon\) . Sketch \(\langle E \rangle\) as a function of temperature \(T\) (measured in units of \(\epsilon /k_{\mathrm{B}}\) ).

(4.7) Find the average energy \(\langle E \rangle\) for (a) An \(n\) - state system, in which a given state can have energy \(0, \epsilon , 2\epsilon , \ldots , n\epsilon\) . (b) A harmonic oscillator, in which a given state can have energy \(0, \epsilon , 2\epsilon , \ldots\) (i.e., with no upper limit).

(4.8) Estimate \(k_{\mathrm{B}}T\) at room temperature, and convert this energy into electronvolts (eV). Using this result, answer the following:

(a) Would you expect hydrogen atoms to be ionized at room temperature? (The binding energy of an electron in a hydrogen atom is \(13.6 \mathrm{eV}\) .)

(b) Would you expect the rotational energy levels of diatomic molecules to be excited at room temperature? (It costs about \(10^{-4} \mathrm{eV}\) to promote such a system to an excited rotational energy level.)

(4.9) Write a computer program to reproduce the results in Example 4.2. For the case of \(\mathcal{N} \gg 1\) sites with initially one quantum per site, show that after many iterations you would expect there to be \(N(n)\) sites with \(n\) quanta, where

\[N(n)\approx 2^{-n}\mathcal{N}, \quad (4.38)\]

and explain why this is a Boltzmann distribution. Generalize your results for \(\mathcal{Q} \gg 1\) quanta distributed on \(\mathcal{N} \gg 1\) sites.

===== Page 66 =====

1

# Part II

## Kinetic theory of gases

In the second part of this book, we apply the results of Part I to the properties of gases. This is the kinetic theory of gases, in which it is the motion of individual gas atoms, behaving according to the Boltzmann distribution, that determines quantities such as the pressure of a gas, or the rate of effusion. This part is structured as follows:

In Chapter 5, we show that the Boltzmann distribution applied to gases gives rise to a speed distribution known as the MaxwellBoltzmann distribution. We show how this can be measured experimentally. A treatment of pressure in Chapter 6 using the results so far developed allows us to derive Boyle's law and the ideal gas law. We are then able to treat the effusion of gases through small holes in Chapter 7, which also introduces the concept of flux. Chapter 8 considers the nature of molecular collisions and introduces the concepts of the mean scattering time, the collision crosssection and the mean free path.

===== Page 67 =====

5

## The Maxwell-Boltzmann distribution

5.1 The velocity distribution 48 5.2 The speed distribution 49 5.3 Experimental justification 51 Chapter summary 54 Exercises 54

In this chapter we will apply the results of the Boltzmann distribution (eqn 4.13) to the problem of the motion of molecules in a gas. For the present, we will neglect any rotational or vibrational motion of the molecules and consider only translational motion (so these results are strictly applicable only to a monatomic gas). In this case the energy of a molecule is given by

\[\frac{1}{2} mv_{x}^{2} + \frac{1}{2} mv_{y}^{2} + \frac{1}{2} mv_{z}^{2} = \frac{1}{2} mv^{2}, \quad (5.1)\]

[Image: A 3D plot of velocity space with axes vx, vy, vz. A vector v is shown from the origin.]
Fig. 5.1 The velocity of a molecule is shown as a vector in velocity space.

where \(\pmb {v} = (v_{x},v_{y},v_{z})\) is the molecular velocity, and \(v = |\pmb {v}|\) is the molecular speed. This molecular velocity can be represented in velocity space (see Fig. 5.1). The aim is to determine the distribution of molecular velocities and to determine the distribution of molecular speeds. This we will do in the next two sections. To make some progress, we will make a couple of assumptions: first, that the molecular size is much less than the intermolecular separation, so that we assume that molecules spend most of their time whizzing around and only rarely bumping into each other; second, we will ignore any intermolecular forces. Molecules can exchange energy with each other due to collisions, but everything remains in equilibrium. Each molecule therefore behaves like a small system connected to a heat reservoir at temperature \(T\) , where the heat reservoir is "all the other molecules in the gas". Hence the results of the Boltzmann distribution of energies (described in the previous chapter) will hold.

### 5.1 The velocity distribution

To work out the velocity distribution of molecules in a gas, we must first choose a given direction and see how many molecules have particular components of velocity along it. We define the velocity distribution function as the fraction of molecules with velocities in, say, the \(x\) - direction, between \(v_{x}\) and \(v_{x} + \mathrm{d}v_{x}\) , as \(g(v_{x})\mathrm{d}v_{x}\) . The velocity distribution function is proportional to a Boltzmann factor, namely e to the power of the relevant energy, in this case \(\frac{1}{2} mv_{x}^{2}\) , divided by \(k_{\mathrm{B}}T\) . Hence

\[g(v_x)\propto \mathrm{e}^{-mv_x^2 /2k_{\mathrm{B}}T}. \quad (5.2)\]

===== Page 68 =====

5.2 The speed distribution 49

This velocity distribution function is sketched in Fig. 5.2. To normalize this function, so that \(\int_{-\infty}^{\infty}g(v_{x})\mathrm{d}v_{x} = 1\) , we need to evaluate the integral2

\[\int_{-\infty}^{\infty}\mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}\mathrm{d}v_{x} = \sqrt{\frac{\pi}{m / 2k_{\mathrm{B}}T}} = \sqrt{\frac{2\pi k_{\mathrm{B}}T}{m}}, \quad (5.3)\]

so that

\[g(v_{x}) = \sqrt{\frac{m}{2\pi k_{\mathrm{B}}T}}\mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}. \quad (5.4)\]

It is then possible to find the following expected values of this distribution (using the integrals in Appendix C.2):

\[\begin{array}{rcl}{\langle v_x\rangle} & = & {\int_{-\infty}^{\infty}v_xg(v_x)\mathrm{d}v_x = 0,}\\ {\langle |v_x|\rangle} & = & {2\int_0^\infty v_xg(v_x)\mathrm{d}v_x = \sqrt{\frac{2k_{\mathrm{B}}T}{\pi m}},}\\ {\langle v_x^2\rangle} & = & {\int_{-\infty}^\infty v_x^2 g(v_x)\mathrm{d}v_x = \frac{k_{\mathrm{B}}T}{m}.} \end{array} \quad (5.6)\]

Of course, it does not matter which component of the velocity was initially chosen. Identical results would have been obtained for \(v_{y}\) and \(v_{z}\) . Hence the fraction of molecules with velocities between \((v_{x},v_{y},v_{z})\) and \((v_{x} + \mathrm{d}v_{x},v_{y} + \mathrm{d}v_{y},v_{z} + \mathrm{d}v_{z})\) is given by

\[\begin{array}{rcl}{g(v_x)\mathrm{d}v_xg(v_y)\mathrm{d}v_yg(v_z)\mathrm{d}v_z}\\ & & {\propto \mathrm{e}^{-mv_x^2 /2k_{\mathrm{B}}T}\mathrm{d}v_x\mathrm{e}^{-mv_y^2 /2k_{\mathrm{B}}T}\mathrm{d}v_y\mathrm{e}^{-mv_z^2 /2k_{\mathrm{B}}T}\mathrm{d}v_z}\\ & = & {\mathrm{e}^{-mv_z^2 /2k_{\mathrm{B}}T}\mathrm{d}v_x\mathrm{d}v_y\mathrm{d}v_z.} \end{array} \quad (5.8)\]

### 5.2 The speed distribution

We now wish to turn to the problem of working out the distribution of molecular speeds in a gas. We want the fraction of molecules which are travelling with speeds between \(v = |v|\) and \(v + \mathrm{d}v\) , and this corresponds to a spherical shell in velocity space of radius \(v\) and thickness \(\mathrm{d}v\) (see Fig. 5.3). The volume of velocity space corresponding to speeds between \(v\) and \(v + \mathrm{d}v\) is therefore equal to

\[4\pi v^{2}\mathrm{d}v, \quad (5.9)\]

so that the fraction of molecules with speeds between \(v\) and \(v + \mathrm{d}v\) can be defined as \(f(v)\mathrm{d}v\) , where \(f(v)\) is given by

\[f(v)\mathrm{d}v\propto v^2\mathrm{d}v\mathrm{e}^{-mv^2 /2k_{\mathrm{B}}T}. \quad (5.10)\]

In this expression the \(4\pi\) factor has been absorbed in the proportionality sign.

[Image: A graph of g(vx) versus vx, a Gaussian curve centered at vx=0.]
2The integral may be evaluated using eqn C.3. Fig.5.2 \(g(v_{x})\) , the distribution function for a particular component of molecular velocity (which is a Gaussian distribution).

[Image: A 3D plot of velocity space showing a spherical shell of radius v and thickness dv. An octant of the shell is highlighted.]
Fig.5.3 Molecules with speeds between \(v\) and \(v + \mathrm{d}v\) occupy a volume of velocity space inside a spherical shell of radius \(v\) and thickness \(\mathrm{d}v\) . (An octant of this sphere is shown cut-away.)

===== Page 69 =====

3We integrate between 0 and \(\infty\) not between \(- \infty\) and \(\infty\) , because the speed \(v = |\boldsymbol {v}|\) is a positive quantity.

To normalize \(^3\) this function, so that \(\int_{0}^{\infty}f(v)\mathrm{d}v = 1\) , we must evaluate the integral (using eqn C.3)

\[\int_{0}^{\infty}v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}\mathrm{d}v = \frac{1}{4}\sqrt{\frac{\pi}{(m / 2k_{\mathrm{B}}T)^{3}}}, \quad (5.11)\]

so that

\[\int f(v)\mathrm{d}v = \frac{4}{\sqrt{\pi}}\left(\frac{m}{2k_{\mathrm{B}}T}\right)^{3 / 2}v^{2}\mathrm{d}v\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}. \quad (5.12)\]

[Image: A graph of f(v) versus v/v_max. The curve starts at 0, rises to a peak, and then decays. Three vertical dotted lines mark v_max, <v>, and v_rms in order.]
Fig.5.4 \(f(v)\) , the distribution function for molecular speeds (MaxwellBoltzmann distribution).

This speed distribution function is known as the Maxwell- Boltzmann speed distribution, or sometimes simply as a Maxwellian distribution and is plotted in Fig. 5.4. Having derived the Maxwell- Boltzmann distribution function (eqn 5.10) we are now in a position to derive some of its properties.

#### 5.2.1 \(\langle v\rangle\) and \(\langle v^2\rangle\)

It is straightforward to find the following expected values of the MaxwellBoltzmann distribution using standard integrals:

\[\begin{array}{rcl}{\langle v\rangle} & = & {\int_0^\infty vf(v)\mathrm{d}v = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}},}\\ {\langle v^2\rangle} & = & {\int_0^\infty v^2 f(v)\mathrm{d}v = \frac{3k_{\mathrm{B}}T}{m}.} \end{array} \quad (5.14)\]

Note that using eqns 5.7 and 5.14 we can write

\[\langle v_{x}^{2}\rangle +\langle v_{y}^{2}\rangle +\langle v_{z}^{2}\rangle = \frac{k_{\mathrm{B}}T}{m} +\frac{k_{\mathrm{B}}T}{m} +\frac{k_{\mathrm{B}}T}{2} = \frac{3k_{\mathrm{B}}T}{m} = \langle v^{2}\rangle \quad (5.15)\]

as expected.

Note also that the root mean squared speed of a molecule

\[v_{\mathrm{rms}} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} \quad (5.16)\]

is proportional to \(m^{- 1 / 2}\) .

#### 5.2.2 The mean kinetic energy of a gas molecule

The mean kinetic energy of a gas molecule is given by

\[\langle E_{\mathrm{KE}}\rangle = \frac{1}{2} m\langle v^2\rangle = \frac{3}{2} k_{\mathrm{B}}T. \quad (5.17)\]

This is an important result, and we will later derive it again by a different route (see Section 19.2.1). It demonstrates that the average energy of a molecule in a gas depends only on temperature.

===== Page 70 =====

5.2.3 The maximum of \(f(v)\)

The maximum value of \(f(v)\) is found by setting

\[\frac{\mathrm{d}f}{\mathrm{d}v} = 0, \quad (5.18)\]

and straightforward differentiation of eqn 5.10 yields

\[v_{\mathrm{max}} = \sqrt{\frac{2k_{\mathrm{B}}T}{m}}. \quad (5.19)\]

Since

\[\sqrt{2} < \sqrt{\frac{8}{\pi}} < \sqrt{3}, \quad (5.20)\]

we have that

\[v_{\mathrm{max}}< \langle v\rangle < v_{\mathrm{rms}} \quad (5.21)\]

and hence the points marked on Fig. 5.4 are in the order drawn. The mean speed of the Maxwell- Boltzmann distribution is higher than the value of the speed corresponding to the maximum in the distribution since the shape of \(f(v)\) is such that the tail to the right is very long.

## Example 5.1

Calculate the rms speed of a nitrogen \(\mathrm{N}_{2}\) molecule at room temperature. [One mole of \(\mathrm{N}_{2}\) has a mass of \(28\mathrm{g}\) ]

Solution:

For nitrogen at room temperature, \(m = (0.028\mathrm{kg}) / (6.022\times 10^{23})\) and so \(v_{\mathrm{rms}}\approx 500\mathrm{m}\mathrm{s}^{- 1}\) . This is about 1100 miles per hour, and is the same order of magnitude as the speed of sound.

### 5.3 Experimental justification

How do you demonstrate that the velocity distribution in a gas obeys the Maxwell- Boltzmann distribution? A possible experimental apparatus is shown in Fig. 5.5. This consists of an oven, a velocity selector, and a detector, which are mounted on an optical bench. Hot gas atoms emerge from the oven and pass through a collimating slit. Velocity selection of molecules is achieved using discs with slits cut into them, which are rotated at high angular speed by a motor. A phase shifter varies the phase of the voltage fed to the motor for one disc relative to that of the other, so that the angle between the slits on the two discs can be continuously adjusted. Thus only molecules travelling with a particular speed from the oven will pass through the slits in both discs. A beam of light can be used to determine when the velocity selector is set for zero transit time. This beam is produced by a small light source near

[Image: A schematic diagram of an experimental setup. An oven emits a beam of molecules through a collimating slit. The beam then passes through a velocity selector consisting of two rotating discs. A detector is at the end of the beam path.]
Fig. 5.5 The experimental apparatus that can be used to measure the Maxwell-Boltzmann distribution.

===== Page 71 =====

52 The Maxwell- Boltzmann distribution

[Image: A 3D diagram of a velocity selector. It is a cylinder with a helical slot cut into it. The cylinder has radius r, length L, and the slot subtends an angle phi.]
Fig. 5.6 Diagram of the velocity selector. (After R.C. Miller and P. Kusch, Phys. Rev. 99, 1314 (1955).) copyright (1955) by the American Physical Society.

one disc and passes through the velocity selector and is detected by a photocell near the other disc.

Another way of selecting the velocity is shown in Fig. 5.6. This consists of a solid surface on whose surface is cut a helical slot, and which is capable of rotation around the cylinder's axis at a rate \(\omega\) . A molecule of velocity \(v\) which goes through the slot without changing its position relative to the sides of the slot will satisfy the equation

\[v = \frac{\omega L}{\phi}, \quad (5.22)\]

in which \(\phi\) and \(L\) are the fixed angle and length shown in Fig. 5.6. Tuning \(\omega\) allows you to tune the selected velocity \(v\) .

[Image: A graph showing intensity versus velocity. Data points (solid circles) follow a curve that is not a simple Maxwellian, but fits to a v^4 exp(-mv^2/2k_B T) form.]
Fig. 5.7 Intensity data measured for potassium atoms using the velocity selector shown in Fig. 5.6 (from R.C. Miller and P. Kusch, Phys. Rev. 99, 1314 (1955), Copyright (1955) by the American Physical Society). The line shows the best fit to an expression of the form \(v^{4}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}\) (see text).

Data from this experiment are shown in Fig. 5.7. In fact, the intensity as a function of velocity \(v\) does not follow the expected \(v^{2}\mathrm{e}^{- mv^{2} / 2k_{\mathrm{B}}T}\) distribution but instead fits to \(v^{4}\mathrm{e}^{- mv^{2} / 2k_{\mathrm{B}}T}\) . What has gone wrong?

Nothing has gone wrong, but there are two factors of \(v\) that must be included for two different reasons. One factor of \(v\) comes from the fact that the gas atoms emerging through the small aperture in the wall of the oven are not completely representative of the atoms inside the oven. This effect will be analysed in Chapter 7. The other factor of \(v\) comes from the fact that as the velocity selector is spun faster, it accepts a smaller fraction of molecules. This can be understood in detail as follows. Because of the finite width of the slit, the velocity selector selects molecules with a range of velocities. The limiting velocities correspond to molecules that enter the slot at one wall and leave the slot at the opposite wall. This leads to velocities that range all the way from \(\omega L / \phi_{- }\) to \(\omega L / \phi_{+}\) , where \(\phi_{\pm} = \phi \pm l / r\) and \(l\) and \(r\) are as defined in Fig. 5.6. Thus the range, \(\Delta v\) , of velocities transmitted is given by

\[\Delta v = \omega L\left(\frac{1}{\phi_{-}} -\frac{1}{\phi_{+}}\right)\approx \frac{2l}{\phi r} v, \quad (5.23)\]

===== Page 72 =====

5.3 Experimental justification 53

and thus increases as the selected velocity increases. This gives rise to the second additional factor of \(v\) .

Another way to justify the treatment in this chapter experimentally is to look at spectral lines of hot gas atoms. The limit on resolution is often set by Doppler broadening: those atoms travelling towards a detector with a component of velocity \(v_{x}\) towards the detector will have transition frequencies that differ from those of atoms at rest due to the Doppler shift. A spectral line with frequency \(\omega_{0}\) (and wavelength \(\lambda_{0} = 2\pi c / \omega_{0}\) , where \(c\) is the speed of light) will be Doppler- shifted to a frequency \(\omega_{0}(1\pm v_{x} / c)\) and the \(\pm\) sign reflects molecules travelling towards or away from the detector. The Gaussian distribution of velocities given by eqn 5.2 now gives rise to a Gaussian shape of the spectral line \(I(\omega)\) (see Fig. 5.8), which is given by

\[I(\omega)\propto \exp \left(-\frac{mc^{2}(\omega_{0} - \omega)^{2}}{2k_{B}T\omega_{0}^{2}}\right), \quad (5.24)\]

[Image: A graph of intensity I(omega) versus omega. The curve is a Gaussian centered at omega_0. The full-width at half-maximum, Delta omega_FWHM, is marked.]
Fig. 5.8 The intensity of a Doppler-broadened spectral line.

and the full- width at half- maximum (FWHM) of this spectral line is given by either \(\Delta \omega^{\mathrm{FWHM}}\) (or in wavelength by \(\Delta \lambda^{\mathrm{FWHM}}\) ) by

\[\frac{I(\omega_{0} + \Delta\omega^{\mathrm{FWHM}} / 2)}{I(\omega_{0})} = \frac{1}{2} \quad (5.25)\]

so that

\[\frac{\Delta\omega^{\mathrm{FWHM}}}{\omega_0} = \frac{\Delta\lambda^{\mathrm{FWHM}}}{\lambda_0} = 2\sqrt{2\ln 2\frac{k_{\mathrm{B}}T}{mc^2}}. \quad (5.26)\]

Another source of broadening of spectral lines arises from molecular collisions. This is called collisional broadening or sometimes pressure broadening (since collisions are more frequent in a gas when the pressure is higher, see Section 8.1). Doppler broadening is therefore most important in low- pressure gases.

===== Page 73 =====

54 Exercises

## Chapter summary

A physical situation that is very important in kinetic theory is the translational motion of atoms or molecules in a gas. The probability distribution for a given component of velocity is given by

\[g(v_{x})\propto \mathrm{e}^{-mv_{x}^{2} / 2k_{\mathrm{B}}T}.\]

We have shown that the corresponding expression for the probability distribution of molecular speeds is given by

\[\int f(v)\propto v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}.\]

This is known as a Maxwell- Boltzmann distribution, or sometimes as a Maxwellian distribution.

Two important average values of the Maxwell- Boltzmann distribution are:

\[\langle v\rangle = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}},\qquad \langle v^2\rangle = \frac{3k_{\mathrm{B}}T}{m}.\]

## Exercises

(5.1) Evaluate the integrals in eqns 5.5- 5.7 and eqns 5.13 and 5.14, and check that you get the same answers.

(5.2) Calculate the rms speed of hydrogen \((\mathrm{H}_{2})\) , helium (He) and oxygen \((\mathrm{O}_{2})\) at room temperature. [The atomic masses of H, He, and O are 1, 4, and 16 respectively.] Compare these speeds with the escape velocity on the surface of (i) the Earth, (ii) the Sun.

(5.3) What fractional error do you make if you approximate \(\sqrt{\langle v^{2}\rangle}\) by \(\langle v\rangle\) for a Maxwell- Boltzmann gas?

(5.4) A Maxwell- Boltzmann distribution implies that a given molecule (mass \(m\) ) will have a speed between \(v\) and \(v + \mathrm{d}v\) with probability equal to \(f(v)\mathrm{d}v\) where

\[f(v)\propto v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T},\]

and the proportionality sign is used because a normalization constant has been omitted. (You can correct for this by dividing any averages you work out by \(\int_{0}^{\infty}f(v)\mathrm{d}v\) .) For this distribution, calculate the mean speed \(\langle v\rangle\) and the mean inverse speed \(\langle 1 / v\rangle\) . Show that

\[\langle v\rangle \langle 1 / v\rangle = \frac{4}{\pi}.\]

(5.5) The width of a spectral line (FWHM) is often quoted as

\[\Delta \lambda^{\mathrm{FWHM}} = 7.16\times 10^{-7}\lambda_0\sqrt{\frac{T}{m}}, \quad (5.27)\]

where \(T\) is the temperature in kelvin, \(\lambda_{0}\) is the wavelength at the centre of the spectral line in the rest frame and \(m\) is the atomic mass of the gas measured in atomic mass units (i.e., multiples of the mass of a proton). Does this formula make sense?

(5.6) What is the Doppler broadening of the \(21~\mathrm{cm}\) line in an interstellar gas cloud (temperature \(100~\mathrm{K}\) ) composed of neutral hydrogen (i.e., non- ionized atomic hydrogen)? Express your answer in kHz.

(5.7) Calculate the rms speed of a sodium atom in the solar atmosphere at \(6000~\mathrm{K}\) . (The atomic mass of sodium is 23. ) The sodium D lines ( \(\lambda = 5900\mathrm{\AA}\) ) are observed in a solar spectrum. Estimate the Doppler broadening in GHz.

===== Page 74 =====

## James Clerk Maxwell (1831-1879)

Born in Edinburgh, James Clerk Maxwell was brought up in the Scottish countryside at Glenair. He was educated at home until, at the age of ten, he was sent to the Edinburgh Academy where his unusual homemade clothes and distracted air earned him the nickname "Dafty".

[Image: A portrait of James Clerk Maxwell, a man with a full beard.]
Fig. 5.9 James Clerk Maxwell

But a lot was going on in his head and he wrote his first scientific paper aged 14. Maxwell went to Peterhouse, Cambridge in 1850 but then moved to Trinity College, where he gained a fellowship in 1854. There he worked on the perception of colour, and also put Michael Faraday's ideas of lines of electrical force onto a sound mathematical basis. In 1856 he took up a chair in Natural Philosophy in Aberdeen

where he worked on a theory of the rings of Saturn (confirmed by the Voyager spacecraft visits of the 1980's) and, in 1858, married the College Principal's daughter, Katherine Mary Dewar.

In 1859, he was inspired by a paper of Clausius on diffusion in gases to conceive of his theory of speed distributions in gases, outlined in Chapter 5, which, with its subsequent elaborations by Boltzmann, is known as the Maxwell- Boltzmann distribution. These triumphs were not enough to preserve him from the consequences of the merging of Aberdeen's two Universities in 1860 when, incredibly, the powers that be decided that it was Maxwell out of the two Professors of Natural Philosophy who should be made redundant. He failed to obtain a chair at Edinburgh (losing out to Tait) but instead moved to King's College, London. There, he produced the world's first colour photograph, came up with his theory of electromagnetism that proposed that light was an electromagnetic wave and explained its speed in terms of electrical properties, and chaired a committee to decide on a new system of units in incorpo

rate the new understanding of the link between electricity and magnetism (and which became known as the "Gaussian", or cgs, system - though "Maxwellian system" would have been more appropriate). He also constructed his apparatus for measuring the viscosity of gases (see Chapter 9), verifying some of his predictions, but not others.

In 1865, he resigned his chair at King's and moved full time to Glenair, where he wrote his Theory of Heat which introduced what are now known as Maxwell relations (Chapter 16) and the concept of the Maxwell's demon (Section 14.7). He applied for, but did not get, the position of Principal of St Andrews' University, but in 1871 was appointed to the newly- established Professorship of Experimental Physics in Cambridge (after William Thomson and Hermann Helmholtz both turned the job down). There he supervised the building of the Cavendish Laboratory and wrote his celebrated A Treatise on Electricity and Magnetism (1873) where his four electromagnetic equations ("Maxwell's equations") first appear. In 1877 he was diagnosed with abdominal cancer and died in Cambridge in 1879.

In his short life Maxwell had been one of the most prolific, inspirational, and creative scientists who has ever lived. His work has had far- reaching implications in much of physics, not just in thermodynamics. He had also lived a devout and contemplative life in which he had been free of pride, selfishness, and ego, always generous and courteous to everyone. The doctor who tended him in his last days wrote:

I must say that he is one of the best men I have ever met, and a greater merit than his scientific achievements is his being, so far as human judgement can discern, a most perfect example of a Christian gentleman.

Maxwell summed up his own philosophy as follows:

Happy is the man who can recognize in the work of Today a connected portion of the work of life, and an embodiment of the work of Eternity. The foundations of his confidence are unchangeable, for he has been made a partaker of Infinity.

===== Page 75 =====

6 Pressure

6.1 Molecular distributions 57 6.2 The ideal gas law 58 6.3 Dalton's law 60 Chapter summary 61 Exercises 61

One of the most fundamental variables in the study of gases is pressure. The pressure \(p\) due to a gas (or in fact any fluid) is defined as the ratio of the perpendicular contact force to the area of contact. The unit is therefore that of force (N) divided by that of area \((\mathrm{m}^2)\) and is called the pascal \((\mathrm{Pa} = \mathrm{Nm}^{- 2})\) . The direction in which pressure acts is always at right angles to the surface upon which it is acting.

Other units for measuring pressure are sometimes encountered, such as the bar (1 bar \(= 10^{5}\) Pa) and the almost equivalent atmosphere (1 atm \(= 1.01325\times 10^{5}\) Pa). The pressure of the atmosphere at sea level actually varies depending on the weather by approximately \(\pm 50\) mbar around the standard atmosphere of 1013.25 mbar, though pressures (adjusted for sea level) as low as 882 mbar and as high as 1084 mbar have been recorded. An archaic unit is the torr, which is equal to a millimetre of mercury (Hg): 1 torr \(= 133.32\) Pa.

## Example 6.1

Air has a density of about \(1.29\mathrm{kgm}^{- 3}\) .Give a rough estimate of the height of the atmosphere assuming that the density of air in the atmosphere is uniform.

Solution:

Atmospheric pressure \(p\approx 10^{5}\) Pa is due to the weight of air \(\rho gh\) in the atmosphere (with assumed height \(h\) and uniform density \(\rho\) ) pressing down on each square metre. Hence \(h = p / \rho g\approx 10^{4}\mathrm{m}\) (which is about the cruising altitude of planes). Of course, in reality the density of the atmosphere falls off with increasing height (see Chapter 37).

The pressure \(p\) of a volume \(V\) of gas (comprising \(N\) molecules) depends on its temperature \(T\) via an equation of state, which is an expression of the form

\[p = f(T,V,N), \quad (6.1)\]

where \(f\) is some function. One example of an equation of state is that for an ideal gas, which was given in eqn 1.12:

\[pV = Nk_{\mathrm{B}}T. \quad (6.2)\]

===== Page 76 =====

 Daniel Bernoulli (1700- 1782) attempted an explanation of Boyle's law \((p \propto 1 / V)\) by assuming (controversially at the time) that gases were composed of a vast number of tiny particles (see Fig. 6.1). This was the first serious attempt at a kinetic theory of gases of the sort that we will describe in this chapter to derive the ideal gas equation.

### 6.1 Molecular distributions

In the previous chapter we derived the Maxwell- Boltzmann speed distribution function \(f(v)\) . We denote the total number of molecules per unit volume by the symbol \(n\) . The number of molecules per unit volume travelling with speeds between \(v\) and \(v + \mathrm{d}v\) is then given by \(nf(v)\mathrm{d}v\) . We now seek to determine the distribution function of molecules travelling in different directions.

#### 6.1.1 Solid angles

Recall that an angle \(\theta\) in a circle is defined by dividing the arc length \(s\) which the angle subtends by the radius \(r\) (see Fig. 6.2), so that

\[\theta = \frac{s}{r}. \quad (6.3)\]

The angle is measured in radians. The angle subtended by the whole circle at its centre is then

\[\frac{2\pi r}{r} = 2\pi . \quad (6.4)\]

By analogy, a solid angle \(\Omega\) in a sphere (see Fig. 6.3) is defined by dividing the surface area \(A\) which the solid angle subtends by the radius squared, so that

\[\Omega = \frac{A}{r^2}. \quad (6.5)\]

The solid angle is measured in steradians. The solid angle subtended by a whole sphere at its centre is then

\[\frac{4\pi r^2}{r^2} = 4\pi . \quad (6.6)\]

#### 6.1.2 The number of molecules travelling in a certain direction at a certain speed

If all molecules are equally likely to be travelling in any direction, the fraction whose trajectories lie in an elemental solid angle \(\mathrm{d}\Omega\) is

\[\frac{\mathrm{d}\Omega}{4\pi}. \quad (6.7)\]

If we choose a particular direction, then the solid angle \(\mathrm{d}\Omega\) corresponding to molecules travelling at angles between \(\theta\) and \(\theta + \mathrm{d}\theta\) to that direction is

[Image: A square box containing several small circles, each with a line with an arrowhead attached, representing molecules moving and bouncing off the walls of the container.]
Fig. 6.1 In the kinetic theory of gases, a gas is modelled as a number of individual tiny particles (atoms or molecules), which can bounce off the walls of the container and each other.

[Image: A diagram showing an angle theta subtended by an arc length s at the centre of a circle of radius r.]
Fig. 6.2 The definition of angle \(\theta\) in terms of the arc length.

[Image: A diagram showing a solid angle Omega subtended by a surface area A on a sphere of radius r.]
Fig. 6.3 The definition of solid angle \(\Omega = A / r^2\) where \(r\) is the radius of the sphere and \(A\) is the surface area over the region of the sphere indicated.

===== Page 77 =====

58 Pressure

[Image: A diagram of a sphere of unit radius. An annular shaded region is shown, corresponding to angles between theta and theta + dtheta from a particular direction. The radius of the annulus is sin(theta).]
Fig.6.4 The area of the shaded region on this sphere of unit radius is equal to the circumference of a circle of radius \(\sin \theta\) multiplied by the width \(d\theta\) and is hence given by \(2\pi \sin \theta d\theta\) .

equal to the area of the annular region shown shaded in the unit- radius sphere of Fig. 6.4 which is given by

\[\mathrm{d}\Omega = 2\pi \sin \theta \mathrm{d}\theta , \quad (6.8)\]

so that

\[\frac{\mathrm{d}\Omega}{4\pi} = \frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.9)\]

Therefore, a number of molecules per unit volume given by

\[n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta \quad (6.10)\]

have speeds between \(v\) and \(v + \mathrm{d}v\) and are travelling at angles between \(\theta\) and \(\theta +\mathrm{d}\theta\) to the chosen direction, where \(f(v)\) is the speed distribution function.

#### 6.1.3 The number of molecules hitting a wall

We now let our particular direction, up until now arbitrarily chosen, lie perpendicular to a wall of area \(A\) see Fig.6.5).In a small time \(\mathrm{d}t\) the molecules travelling at angle \(\theta\) to the normal to the wall sweep out a volume

\[A v\mathrm{d}t\cos \theta . \quad (6.11)\]

Multiplying this volume by the number in expression 6.10 implies that in time \(\mathrm{d}t\) , the number of molecules hitting a wall of area \(A\) is

\[A v\mathrm{d}t\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.12)\]

Hence, the number of molecules hitting unit area of wall in unit time, and having speeds between \(v\) and \(v + \mathrm{d}v\) and travelling at angles between \(\theta\) and \(\theta +\mathrm{d}\theta\) , is given by

\[v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta . \quad (6.13)\]

[Image: A diagram showing a volume element swept out by molecules moving at velocity v at an angle theta to the normal of a wall of area A. The volume is A v dt cos(theta).]
Fig.6.5 Molecules hit a region of wall (of cross-sectional area \(A^{1 / 2}\times A^{1 / 2} =\) \(A\) ) at an angle \(\theta\) .The number hitting in time \(\mathrm{d}t\) is the volume of the shaded region ( \(A\mathrm{d}t\cos \theta\) ) multiplied by \(n f(v)\mathrm{d}v\frac{1}{2}\sin \theta\)

### 6.2 The ideal gas law

We are now in a position to calculate the pressure of a gas on its container. Each molecule hitting the wall of the container has a momentum change of \(2mv\cos \theta\) , which is perpendicular to the wall. This change of momentum is equivalent to an impulse. Hence, if we multiply \(2mv\cos \theta\) (the momentum change arising from one molecule hitting the container walls) by the number of molecules hitting unit area per unit time, and having speeds between \(v\) and \(v + \mathrm{d}v\) and angles between \(\theta\) and \(\theta +\mathrm{d}\theta\) (which we derived in eqn 6.13), and then integrating over \(\theta\) and \(v\) , we should get the pressure \(p\) . Thus

\[\begin{array}{rcl}{p}&{=}&{\int_{0}^{\infty}\int_{0}^{\pi/2}(2mv\cos\theta)\left(v\cos\theta n f(v)\mathrm{d}v\frac{1}{2}\sin\theta\mathrm{d}\theta\right)}\\{=}&{m n\int_{0}^{\infty}\mathrm{d}v v^{2}f(v)\int_{0}^{\pi/2}\cos^{2}\theta\sin\theta\mathrm{d}\theta,}\end{array} \quad (6.14)\]

===== Page 78 =====

 and using the integral \(\int_{0}^{\pi /2}\cos^{2}\theta \sin \theta \mathrm{d}\theta = \frac{1}{3}\) , we have that

\[p = \frac{1}{3} nm\langle v^2\rangle . \quad (6.15)\]

If we write the total number of molecules \(N\) in volume \(V\) as

\[N = nV, \quad (6.16)\]

then this equation can be written as

\[pV = \frac{1}{3} Nm\langle v^2\rangle . \quad (6.17)\]

Using \(\langle v^2 \rangle = 3k_{\mathrm{B}}T / m\) , this can be rewritten as

\[pV = Nk_{\mathrm{B}}T, \quad (6.18)\]

which is the ideal gas equation we met in eqn 1.12. This completes the kinetic theory derivation of the ideal gas law.

## Equivalent forms of the ideal gas law:

The form given in eqn 6.18 is

\[pV = Nk_{\mathrm{B}}T,\]

and contains an " \(N\) ", which we reiterate is the total number of molecules in the gas.

An equivalent form of the ideal gas equation can be derived by dividing both sides of eqn 6.18 by volume, so that

\[p = nk_{\mathrm{B}}T, \quad (6.19)\]

where \(n = N / V\) is the number of molecules per unit volume.

Another form of the ideal gas law can be obtained by writing the number of molecules \(N = n_{\mathrm{m}}N_{\mathrm{A}}\) , where \(n_{\mathrm{m}}\) is the number of moles and \(N_{\mathrm{A}}\) is the Avogadro number (the number of molecules in a mole, see Section 1.1). In this case, eqn 6.18 becomes

\[pV = n_{\mathrm{m}}RT, \quad (6.20)\]

where

\[R = N_{\mathrm{A}}k_{\mathrm{B}} \quad (6.21)\]

is the gas constant \((R = 8.31447 \mathrm{J} \mathrm{K}^{- 1} \mathrm{mol}^{- 1})\) .

The ideal gas law \((p = nk_{\mathrm{B}}T)\) expresses the important point that the pressure of an ideal gas does not depend on the mass \(m\) of the molecules. Although more massive molecules transfer greater momentum to the container walls than light molecules, their mean velocity is lower and so they make fewer collisions with the walls. Therefore the pressure is the same for a gas of light or massive molecules; it depends only on \(n\) , the number per unit volume, and the temperature.

===== Page 79 =====

60 Pressure

## Example 6.2

What is the volume occupied by one mole of ideal gas at standard temperature and pressure (STP, defined as \(0^{\circ}\mathrm{C}\) and 1 atm)?

Solution:

At \(p = 1.01325\times 10^{5}\mathrm{Pa}\) and \(T = 273.15\mathrm{K}\) , the molar volume \(V_{\mathrm{m}}\) can be obtained from eqn 6.20 as

\[V_{\mathrm{m}} = \frac{RT}{p} = 0.022414\mathrm{m}^{3} = 22.414\mathrm{litres}. \quad (6.22)\]

## Example 6.3

What is the connection between pressure and kinetic energy density? Solution:

The kinetic energy of a gas molecule moving with speed \(v\) is

\[\frac{1}{2} mv^{2}. \quad (6.23)\]

The total kinetic energy of the molecules of a gas per unit volume, i.e., the kinetic energy density, which we will call \(u\) , is therefore given by

\[u = n\int_{0}^{\infty}\frac{1}{2} mv^{2}f(v)\mathrm{d}v = \frac{1}{2} nm\langle v^{2}\rangle , \quad (6.24)\]

so that comparing with eqn 6.15 we have that

\[p = \frac{2}{3} u. \quad (6.25)\]

### 6.3 Dalton's law

If one has a mixture of gases in thermal equilibrium, then the total pressure \(p = nk_{\mathrm{B}}T\) is simply the sum of the pressures due to each component of the mixture. We can write \(n\) as

\[n = \sum_{i}n_{i}, \quad (6.26)\]

where \(n_{i}\) is the number density of the \(i\) th species. Therefore

\[p = \left(\sum_{i}n_{i}\right)k_{\mathrm{B}}T = \sum_{i}p_{i}, \quad (6.27)\]

where \(p_{i} = n_{i}k_{\mathrm{B}}T\) is known as the partial pressure of the \(i\) th species. The observation that \(p = \sum_{i}p_{i}\) is known as Dalton's law, after the British chemist John Dalton (1766- 1844), who was a pioneer of the atomic theory.

===== Page 80 =====

1

## Example 6.4

Air is \(75.5\%\) \(\mathrm{N}_{2}\) \(23.2\%\) \(\mathrm{O}_{2}\) \(1.3\%\) Ar, and \(0.05\%\) \(\mathrm{CO}_{2}\) by mass. Calculate the partial pressure of \(\mathrm{CO}_{2}\) in air at atmospheric pressure.

Solution:

Dalton's law states that the partial pressure is proportional to the number density. The number density is proportional to the mass fraction divided by the molar mass. The molar masses of the species (in grammes) are 28 \(\mathrm{N}_{2}\) 32 \(\mathrm{O}_{2}\) 40 \(\mathrm{Ar}\) and 44 \(\mathrm{CO}_{2}\) .Hence,the partial pressure of \(\mathrm{CO}_{2}\) is

\[p\mathrm{CO}_{2} = \frac{\frac{0.05}{44}}{\frac{75.5}{28} + \frac{23.2}{32} + \frac{1.3}{40} + \frac{0.05}{44}} = 0.00033\mathrm{atm}. \quad (6.28)\]

## Chapter summary

The pressure, \(p\) , is given by

\[p = \frac{1}{3} nm\langle v^2\rangle ,\]

where \(n\) is the number of molecules per unit volume and \(m\) is the molecular mass.

This expression agrees with the ideal gas equation,

\[p = nk_{\mathrm{B}}T,\]

where \(V\) is the volume, \(T\) is the temperature and \(k_{\mathrm{B}}\) is the Boltzmann constant.

## Exercises

(6.1) What is the volume occupied by 1 mole of gas at \(10^{- 10}\) torr, the pressure inside an "ultra high vacuum" (UHV) chamber.

(6.2) Calculate \(u\) , the kinetic energy density, for air at atmospheric pressure.

(6.3) Mr Fourier sits in his living room at \(18^{\circ}\mathrm{C}\) . He de

cides he is rather cold and turns the heating up so that the temperature is \(25^{\circ}\mathrm{C}\) . What happens to the total energy of the air in his living room? [Hint: what controls the pressure in the room?]

(6.4) A diffuse cloud of neutral hydrogen atoms (known as HI) in space has a temperature of \(50\mathrm{K}\) and num

===== Page 81 =====

62 Exercises

ber density \(500\mathrm{cm}^{- 3}\) .Calculate the pressure (in Pa) and the volume (in cubic light years) occupied by the cloud if its mass is \(100M_{\odot}\) \(M_{\odot}\) is the symbol for the mass of the Sun, see Appendix A.)

(6.5) (a) Given that the number of molecules hitting unit area of a surface per second with speeds between \(v\) and \(v + \mathrm{d}v\) and angles between \(\theta\) and \(\theta +d\theta\) to the normal is

\[\frac{1}{2} v n f(v)\mathrm{d}v\sin \theta \cos \theta d\theta ,\]

show that the average value of \(\cos \theta\) for these molecules is \(\frac{2}{3}\)

(b) Using the results above, show that for a gas obeying the Maxwellian distribution (i.e., \(f(v)\propto v^{2}e^{-mv^{2} / 2k_{\mathrm{B}}T})\) the average energy of all the molecules is \(\frac{3}{2} k_{\mathrm{B}}T\) , but the average energy of those hitting the surface is \(2k_{\mathrm{B}}T\) .

(6.6) The molecules in a gas travel with different velocities. A particular molecule will have velocity \(\mathbf{v}\) and speed \(v = |\mathbf{v}|\) and will move at an angle \(\theta\) to some chosen fixed axis. We have shown that the number of molecules in a gas with speeds between \(v\) and \(v + \mathrm{d}v\) and moving at angles between \(\theta\) and \(\theta +d\theta\) to any chosen axis is given by

\[\frac{1}{2} n f(v)\mathrm{d}v\sin \theta d\theta ,\]

where \(n\) is the number of molecules per unit volume and \(f(v)\) is some function of \(v\) only. \([f(v)\) could be the Maxwellian distribution given above; however you should not assume this but rather calculate the general case.] Hence show by integration that:

(a) \(\langle u\rangle = 0\) (b) \(\langle u^{2}\rangle = \frac{1}{3}\langle v^{2}\rangle\) (c) \(\langle |u|\rangle = \frac{1}{2}\langle v\rangle\)

where \(u\) is any one Cartesian component of \(v\) ,i.e., \(v_{x}\) \(v_{y}\) or \(v_{z}\)

[Hint: You can take \(u\) as the \(z\) - component of \(\mathbf{v}\) without loss of generality. Why? Then express \(u\) in terms of \(v\) and \(\theta\) and average over \(v\) and \(\theta\) . You can use expressions such as

\[\langle v\rangle = \frac{\int_{0}^{\infty}v f(v)\mathrm{d}v}{\int_{0}^{\infty}f(v)\mathrm{d}v}\]

and similarly for \(\langle v^{2}\rangle\) . Make sure you understand why.]

(6.7) If \(v_{1}\) \(v_{2}\) \(v_{3}\) are three Cartesian components of \(\mathbf{v}\) what value do you expect for \(\langle v_{1}v_{2}\rangle\) \(\langle v_{1}v_{3}\rangle\) ,and \(\langle v_{2}v_{3}\rangle\) ?Evaluate one of them by integration to check your deduction.

(6.8) Calculate the partial pressure of \(O_{2}\) in air at atmospheric pressure.

(6.9) This question provides an alternative derivation of the formula for pressure. Without loss of generality, let us consider molecules travelling towards a wall which lies in the \(xy\) plane. The momentum change of a molecule of mass \(m\) and velocity \(\mathbf{v} = (v_{x},v_{y},v_{z})\) bouncing off the wall will be \(2mv_{x}\) . Explain why the pressure \(p\) on the wall is given by

\[p = \int_{0}^{\infty}(2mv_{x})v_{x}n g(v_{x})\mathrm{d}v_{x}, \quad (6.29)\]

where \(g(v_{x})\) is the function given in eqn 5.2. Hence show that \(p = nk_{\mathrm{B}}T\) .Using the same approach show that \(\Phi\) the number of molecules hitting unit area of the wall per second is given by

\[\Phi = \int_{0}^{\infty}v_{x}n g(v_{x})\mathrm{d}v_{x} = n\sqrt{\frac{k_{\mathrm{B}}T}{\pi m}} = \frac{1}{4} n\langle v\rangle .\]

This result will be derived using a different method in the next chapter.

===== Page 82 =====

## Robert Boyle (1627-1691)

Robert Boyle was born into wealth. His father was a self- made man of humble yeoman stock who, at the age of 22, had left England for Ireland to seek his fortune.

[Image: A portrait of Robert Boyle in 17th century dress, wearing a long curly wig.]
Fig.6.6 Robert Boyle

This his father found or, possibly more accurately, "grabbed" and through rapid land acquisition of a rather dubious nature Boyle senior became one of England's richest men and the Earl of Cork to boot. Robert was born when his father was in his sixties and was the last but one of his father's sixteen children. His father, as a new member of the aristocracy, believed

in the best education for his children, and Robert was duly packed off to Eton and then, at the age of 12, sent off for a European Grand Tour, taking in Geneva, Venice, and Florence. Boyle studied the works of Galileo, who died in Florence while Boyle was staying in the city. Meanwhile, his father was getting into a spot of bother with the Irish rebellion of 1641- 1642, resulting in the loss of the rents that kept him and his family in the manner to which they had become accustomed, and hence also causing Robert Boyle some financial difficulty. He was almost married off at this time to a wealthy heiress, but Boyle managed to escape this fate and remained unmarried for the rest of his life. His father died in 1643 and Boyle returned to England the following year, inheriting his father's Dorset estate.

However, by this time the Civil War (which had started in 1642) was in full swing and Boyle tried hard not to take sides. He kept his head down, devoting his time to study, building a chemical laboratory in his house and worked on moral and theological essays. Cromwell's defeat of the Irish in 1652 worked well for Boyle as many Irish lands were handed over to the English colonists. Financially, Boyle was now secure and ready to live the life of a gentleman. In London, he had met John Wilkins, who had founded an intellectual society, which he called "The Invisi

ble College" and which suddenly brought Boyle into contact with the leading thinkers of the day. When Wilkins was appointed Warden of Wadham College, Oxford, Boyle decided to move to Oxford and set up a laboratory there. He set up an air pump and, together with a number of talented assistants (the most famous of which was Robert Hooke, later to discover his law of springs and to observe a cell with a microscope, in addition to numerous other discoveries) Boyle and his team conducted a large number of elaborate experiments in this new vacuum. They showed that sound did not travel in a vacuum, and that flames and living organisms could not be sustained, and discovered the "spring of air", namely that compressing air resulted in its pressure increasing, and that the pressure of a gas and its volume were in inverse proportion.

Boyle was much taken with the atomistic viewpoint as described by the French philosopher Pierre Gassendi (1592- 1655), which seems particularly appropriate for someone whose work led to the path for the development of the kinetic theory of gases. His greatest legacy was in his reliance on experiment as a means of determining scientific truth. He was, however, also someone who often worked vicariously through a band of assistants, citing his weakness of health and of eyesight as a reason for failing to write his papers as he wished to and to have read other peoples' works as he ought; his writings are, however, full of criticisms of his assistants for making mistakes, failing to record data, and generally slowing down his research endeavours.

With the restoration of the monarchy in 1660, the Invisible College, which had been meeting for several years in Gresham College, London, sought the blessing of the newly crowned Charles II and became the Royal Society, which has existed ever since as a thriving scientific society. In 1680, Boyle (who had been a founding fellow of the Royal Society) was elected President of the Royal Society, but declined to hold the office, citing an unwillingness to take the necessary oaths. Boyle retained a strong Christian faith throughout his life, and prided himself on his honesty and pure seeking of the truth. In 1670, Boyle suffered a stroke but made a good recovery, staying active in research until the mid- 1680's. He died in 1691, shortly after the death of his sister Katherine to whom he had been extremely close.

===== Page 83 =====

7 Molecular effusion

7.1 Flux 64 7.2 Effusion 66 Chapter summary 69 Exercises 69

Effusion is the process by which a gas escapes from a very small hole. The empirical relation known as Graham's law of effusion [after Thomas Graham (1805- 1869)] states that the rate of effusion is inversely proportional to the square root of the mass of the effusing molecule.

Isotopes (the word means "same place") are atoms of a chemical element with the same atomic number \(Z\) (and hence number of protons in the nucleus) but different atomic weights \(A\) (and hence different number of neutrons in the nucleus).

## Example 7.1

Effusion can be used to separate different isotopes of a gas (which cannot be separated chemically). For example, in the separation of \(^{235}\mathrm{UF}_6\) and \(^{238}\mathrm{UF}_6\) the ratio of the effusion rates of the two gases is equal to

\[\sqrt{\frac{\mathrm{mass~of~}^{238}\mathrm{UF}_6}{\mathrm{mass~of~}^{235}\mathrm{UF}_6}} = \sqrt{\frac{352.0412}{348.0343}} = 1.00574, \quad (7.1)\]

which, although small, was enough for many kilogrammes of \(^{235}\mathrm{UF}_6\) to be extracted for the Manhattan project in 1945 to produce the first uranium atom bomb, which was subsequently dropped on Hiroshima.

## Example 7.2

How much faster does helium gas effuse out of a small hole than \(\mathrm{N}_2\) ? Solution:

\[\sqrt{\frac{\mathrm{mass~of~}\mathrm{N}_2}{\mathrm{mass~of~}\mathrm{He}}} = \sqrt{\frac{28}{4}} = 2.6. \quad (7.2)\]

In this chapter, we will discover where Graham's law comes from. We begin by evaluating the flux of particles hitting the inside walls of the container of a gas.

### 7.1 Flux

The concept of flux is a very important one in thermal physics. It quantifies the flow of particles or the flow of energy or even the flow of momentum. Of relevance to this chapter is the molecular flux, \(\Phi\) , which

===== Page 84 =====

1s defined to be the number of molecules striking unit area per second. Thus

\[\mathrm{molecular~flux} = \frac{\mathrm{number~of~molecules}}{\mathrm{area}\times\mathrm{time}}. \quad (7.3)\]

The units of molecular flux are therefore \(\mathrm{m}^{- 2}\mathrm{s}^{- 1}\) . We can also define heat flux using

\[\mathrm{heat~flux} = \frac{\mathrm{amount~of~heat}}{\mathrm{area}\times\mathrm{time}}. \quad (7.4)\]

The units of heat flux are therefore \(\mathrm{Jm}^{- 2}\mathrm{s}^{- 1}\) . In Section 9.1, we will also come across a flux of momentum.

Returning to the effusion problem, we note that the flux of molecules in a gas can be evaluated by integrating expression 6.13 over all \(v\) and \(\theta\) , so that

\[\begin{array}{rcl}{\Phi} & = & {\int_0^\infty \int_0^{\pi /2}v\cos \theta nf(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta}\\ {} & = & {\frac{n}{2}\int_0^\infty \mathrm{d}v vf(v)\int_0^{\pi /2}\mathrm{d}\theta \cos \theta \sin \theta} \end{array} \quad (7.5)\]

so that

\[\Phi = \frac{1}{4} n\langle v\rangle . \quad (7.6)\]

An alternative expression for \(\Phi\) can be found as follows: rearranging the ideal gas law \(p = n k_{\mathrm{B}}T\) , we can write

\[n = \frac{p}{k_{\mathrm{B}}T}, \quad (7.7)\]

and using the expression for the average speed of molecules in a gas from eqn 5.13

\[\langle v\rangle = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}}, \quad (7.8)\]

we can substitute these expressions into eqn 7.6 and obtain

\[\Phi = \frac{p}{\sqrt{2\pi m k_{\mathrm{B}}T}}. \quad (7.9)\]

Note that consideration of eqn 7.9 shows us that the effusion rate depends inversely on the square root of the mass, in agreement with Graham's law.

## Example 7.3

Calculate the particle flux from \(\mathrm{N}_{2}\) gas at STP (standard temperature and pressure, i.e., 1 atm and \(0^{\circ}\mathrm{C}\) ).

Solution:

\[\begin{array}{rl}\Phi & = \frac{1.01325\times 10^5\mathrm{Pa}}{\sqrt{2\pi\times(28\times 1.67\times 10^{-27}\mathrm{kg})\times 1.38\times 10^{-23}\mathrm{JK}^{-1}\times 273\mathrm{K}}}\\ & \approx 3\times 10^{27}\mathrm{m}^{-2}\mathrm{s}^{-1}. \end{array} \quad (7.10)\]

===== Page 85 =====

66 Molecular effusion

[Image: A box containing a gas, with a small hole in the top. Arrows show molecules effusing out of the hole.]
Fig. 7.1 A gas effuses from a small hole in its container.

[Image: A box resting on a weighing scale. The box contains liquid at the bottom and gas above it, with a small hole at the top.]
Fig. 7.2 The Knudsen method.

[Image: A graph of f(v) versus v/v_max. Two curves are shown. The solid curve is proportional to v^2 exp(-mv^2/2k_B T), the Maxwellian distribution. The dashed curve is proportional to v^3 exp(-mv^2/2k_B T), the distribution for effusing gas. The dashed curve peaks at a higher velocity.]
Fig. 7.3 The distribution function for molecular speeds (Maxwell-Boltzmann distribution) in a gas is proportional to \(v^{2}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}\) (solid line) but the gas effusing from a small hole has a distribution function that is proportional to \(v^{3}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}\) (dashed line). The distinction between the two situations occurs when counting the molecules crossing a fixed plane during some interval of time.

### 7.2 Effusion

Consider a container of gas with a small hole of area \(A\) in the side. Gas will leak (i.e., effuse) out of the hole (see Fig. 7.1). The hole is small, so that the equilibrium of gas in the container is not disturbed. The number of molecules escaping per unit time is just the number of molecules hitting the hole area in the closed box per second, so is given by \(\Phi A\) per second, where \(\Phi\) is the molecular flux. This is the effusion rate.

## Example 7.4

In the Knudsen method of measuring vapour pressure \(p\) from a liquid containing molecules of mass \(m\) at temperature \(T\) , the liquid is placed in the bottom of a container that has a small hole of area \(A\) at the top (see Fig. 7.2). The container is placed on a weighing balance and its weight \(Mg\) is measured as a function of time. In equilibrium, the effusion rate is

\[\Phi A = \frac{pA}{\sqrt{2\pi mk_{\mathrm{B}}T}}, \quad (7.11)\]

so that the rate of change of mass, \(\mathrm{d}M / \mathrm{d}t\) is given by \(- m\Phi A\) . Hence

\[p = \sqrt{\frac{2\pi k_{\mathrm{B}}T}{m}}\frac{1}{A}\left|\frac{\mathrm{d}M}{\mathrm{d}t}\right|. \quad (7.12)\]

Effusion preferentially selects faster molecules. Therefore the speed distribution of molecules effusing through the hole is not Maxwellian. This result seems paradoxical at first glance: aren't the molecules emerging from the box the same ones that were inside beforehand? How can their distribution be different?

The reason is that the faster molecules inside the box travel more quickly and have a greater probability of reaching the hole than their slower cousins. This can be expressed mathematically by noticing that the number of molecules hitting a wall (or a hole) is given by eqn 6.13 and this has an extra factor of \(v\) in it. Thus the distribution of molecules effusing through the hole in some interval of time is proportional to

\[v^{3}\mathrm{e}^{-mv^{2} / 2k_{\mathrm{B}}T}. \quad (7.13)\]

Note the extra factor of \(v\) in this expression compared with the usual Maxwell- Boltzmann distribution in eqn 5.10 (see Fig. 7.3). The molecules

===== Page 86 =====

7.2 Effusion 67

in the Maxwellian gas had an average energy of \(\frac{1}{2} m\langle v^2\rangle = \frac{3}{2} k_{\mathrm{B}}T\) , but the molecules in the effusing gas have a higher energy, as the following example will demonstrate.

## Example 7.5

What is the mean kinetic energy of gas molecules effusing out of a small hole? Solution:

\[\langle \mathrm{kinetic~energy}\rangle = \frac{1}{2} m\langle v^2\rangle\] \[= \frac{\frac{1}{2}m\int_0^\infty v^2v^3\mathrm{e}^{-\frac{1}{2}mv^2 / k_{\mathrm{B}}T}\mathrm{d}v}{\int_0^\infty v^3\mathrm{e}^{-\frac{1}{2}mv^2 / k_{\mathrm{B}}T}\mathrm{d}v\] \[= \frac{1}{2} m\left(\frac{2k_{\mathrm{B}}T}{m}\right)\frac{\int_0^\infty u^2\mathrm{e}^{-u}\mathrm{d}u}{\int_0^\infty u\mathrm{e}^{-u}\mathrm{d}u\]

where the substitution \(u = mv^2 / 2k_{\mathrm{B}}T\) has been made. Using the standard integral \(\int_0^\infty x^n\mathrm{e}^{- x}\mathrm{d}x = n!\) (see Appendix C.1), we have that

\[\langle \mathrm{kinetic~energy}\rangle = 2k_{\mathrm{B}}T. \quad (7.15)\]

This is larger by a factor of \(\frac{4}{3}\) than the mean kinetic energy of molecules in the gas. This is because effusion preferentially selects higher energy molecules.

The hole has to be small. How small? The diameter of the hole has to be much less \(^2\) than the mean free path \(\lambda\) , defined in Section 8.3.

## Example 7.6

Consider a container divided by a partition with a small hole, diameter \(D\) , containing the same gas on each side. The gas on the left- hand side has temperature \(T_{1}\) and pressure \(p_{1}\) . The gas on the right- hand side has temperature \(T_{2}\) and pressure \(p_{2}\) .

If \(D\gg \lambda\) \(p_1 = p_2\)

If \(D\ll \lambda\) , we are in the effusion regime and the system will achieve equilibrium when the molecular fluxes balance, so that

\[\Phi_{1} = \Phi_{2}, \quad (7.16)\]

so that, using eqn 7.9 we may write

\[\frac{p_1}{\sqrt{T_1}} = \frac{p_2}{\sqrt{T_2}}. \quad (7.17)\]

2This is because, as we shall see in Section 8.3, the mean free path controls the characteristic distance between collisions. If the hole is small on this scale, molecules can effuse out without the rest of the gas "noticing", i.e., without a pressure gradient developing close to the hole.

This is called the Knudsen effect, after Martin Knudsen (1871- 1949).

===== Page 87 =====

 A final example gives an approximate derivation of the flow rate of gas down a pipe at low pressures.

## Example 7.7

Estimate the mass flow rate of gas down a long pipe of length \(L\) and diameter \(D\) at very low pressures in terms of the difference in pressures \(p_1 - p_2\) between the two ends of the pipe.

Solution:

This type of flow is known as Knudsen flow. At very low pressures, molecules collide with the walls of the tube much more often than they do with each other. Let us define a coordinate \(x\) , which measures the distance along the pipe. The net flux \(\Phi (x)\) of molecules flowing down the pipe at position \(x\) can be estimated by subtracting the molecules effusing down the pipe since their last collision (roughly a distance \(D\) upstream) from the molecules effusing up the pipe since their last collision (roughly a distance \(D\) downstream). Thus

\[\Phi (x)\approx \frac{1}{4}\langle v\rangle [n(x - D) - n(x + D)], \quad (7.18)\]

where \(n(x)\) is the number density of molecules at position \(x\) . Using \(p = \frac{1}{3} nm\langle v^2\rangle\) (eqn 6.15), this can be written

\[\Phi (x)\approx \frac{3}{4m}\frac{\langle v\rangle}{\langle v^2\rangle} [p(x - D) - p(x + D)]. \quad (7.19)\]

We can write

\[p(x - D) - p(x + D)\approx -2D\frac{\mathrm{d}p}{\mathrm{d}x}, \quad (7.20)\]

but also notice that in steady state \(\Phi\) must be the same along the tube, so that

\[\frac{\mathrm{d}p}{\mathrm{d}x} = \frac{p_2 - p_1}{L}. \quad (7.21)\]

Hence the mass flow rate \(\dot{M} = m\Phi (\pi D^2 /4)\) (where \(\pi D^2 /4\) is the cross- sectional area of the pipe) is given by

\[\dot{M}\approx \frac{3}{8}\frac{\langle v\rangle}{\langle v^2\rangle}\pi D^3\frac{p_1 - p_2}{L}. \quad (7.22)\]

With eqns 5.13 and 5.14, we have that

\[\frac{\langle v\rangle^2}{\langle v^2\rangle} = \frac{8}{3\pi}, \quad (7.23)\]

and hence our estimate of the Knudsen flow rate is

\[\dot{M}\approx \frac{D^3}{\langle v\rangle}\frac{p_1 - p_2}{L}. \quad (7.24)\]

Note that the flow rate is proportional to \(D^3\) , so it is much more efficient to pump gas through wide pipes to obtain high flow rates.

===== Page 88 =====

1

## Chapter summary

The molecular flux, \(\Phi\) , is the number of molecules striking unit area per second and is given by

\[\Phi = \frac{1}{4} n\langle v\rangle .\]

This expression, together with the ideal gas equation, can be used to derive an alternative expression for the particle flux:

\[\Phi = \frac{p}{\sqrt{2\pi mk_{\mathrm{B}}T}}.\]

These expressions also govern molecular effusion through a small hole.

## Exercises

(7.1) In a vacuum chamber designed for surface- science experiments, the pressure of residual gas is kept as low as possible so that surfaces can be kept clean. The coverage of a surface by a single monolayer requires about \(10^{19}\) atoms per \(\mathrm{m}^2\) . What pressure would be needed to deposit less than one monolayer per hour from residual gas? You may assume that if a molecule hits the surface, it sticks.

(7.2) A vessel contains a monatomic gas at temperature \(T\) . Use the Maxwell- Boltzmann distribution of speeds to calculate the mean kinetic energy of the molecules.

Molecules of the gas stream through a small hole into a vacuum. A box is opened for a short time and catches some of the molecules. Neglecting the thermal capacity of the box, calculate the final temperature of the gas trapped in the box.

(7.3) A closed vessel is partially filled with liquid mercury; there is a hole of area \(10^{- 7} \mathrm{~m}^2\) above the liquid level. The vessel is placed in a region of high vacuum at \(273 \mathrm{~K}\) and after 30 days is found to be lighter by \(2.4 \times 10^{- 5} \mathrm{~kg}\) . Estimate the vapour pressure of mercury at \(273 \mathrm{~K}\) . (The relative molecular mass of mercury is 200.59. )

(7.4) Calculate the mean speed and most probable speed for a molecule of mass \(m\) which has effused out of an enclosure at temperature \(T\) . Which of the two speeds is the larger?

(7.5) A gas effuses into a vacuum through a small hole of area \(A\) . The particles are then collimated by passing through a very small circular hole of radius \(a\) , in a screen a distance \(d\) from the first hole. Show that the rate at which particles emerge from the second hole is \(\frac{1}{4} nA\langle v\rangle (a^2 /d^2)\) , where \(n\) is the particle density and \(\langle v \rangle\) is the average speed. (Assume that no collisions take place after the gas effuses through the second hole, and that \(d \gg a\) .)

(7.6) Show that if a gas were allowed to leak through a small hole into an evacuated sphere and the particles condensed where they first hit the surface they would form a uniform coating.

(7.7) An astronaut goes for a space walk and her space suit is pressurized to 1 atm. Unfortunately, a tiny piece of space dust punctures her suit and it develops a small hole of radius \(1 \mu \mathrm{m}\) . What force does she feel due to the effusing gas?

(7.8) Show that the time dependence of the pressure inside an oven (volume \(V\) ) containing hot gas (molecular mass \(m\) , temperature \(T\) ) with a small hole of area \(A\) is given by

\[p(t) = p(0)\mathrm{e}^{-t / \tau}, \quad (7.25)\]

with

\[\tau = \frac{V}{A}\sqrt{\frac{2\pi m}{k_{\mathrm{B}}T}}. \quad (7.26)\]

===== Page 89 =====

8.1 The mean collision time 70 8.2 The collision cross- section 71 8.3 The mean free path 73 Chapter summary 74 Exercises 74

It turns out that large- angle scattering dominates transport processes in most gases (described in Chapter 9) and is largely independent of energy and therefore temperature; this allows us to use a rigid- sphere model of collisions, i.e. to model atoms in a gas as billiard balls.

## The mean free path and collisions

At room temperature, the rms speed of \(\mathrm{O_2}\) or \(\mathrm{N_2}\) is about \(500~\mathrm{ms}^{- 1}\) Processes such as the diffusion of one gas into another would therefore be almost instantaneous, were it not for the occurrence of collisions between molecules. Collisions are fundamentally quantum mechanical events, but in a dilute gas, molecules spend most of their time between collisions and so we can consider them as classical billiard balls and ignore the details of what actually happens during a collision. All that we care about is that after collisions the molecules' velocities become essentially randomized. In this chapter we will model the effect of collisions in a gas and develop the concepts of a mean collision time, the collision cross- section and the mean free path.

### 8.1 The mean collision time

In this section, we aim to calculate the average time between molecular collisions. Let us consider a particular molecule moving in a gas of other similar molecules. To make things simple to start with, we suppose that the molecule under consideration is travelling at speed \(v\) and that the other molecules in the gas are stationary. This is clearly a gross over- simplification, but we will relax this assumption later. We will also attribute a collision cross- section \(\sigma\) to each molecule, which is something like the cross- sectional area of our molecule. Again, we will refine this definition later in the chapter.

In a time dt, our molecule will sweep out a volume \(\sigma v\mathrm{dt}\) . If another molecule happens to lie inside this volume, there will be a collision. With \(n\) molecules per unit volume, the probability of a collision in time dt is therefore \(n\sigma v\mathrm{dt}\) . Let us define \(P(t)\) as follows:

\[P(t) = \mathrm{the~probability~of~a~molecule~not~colliding~up~to~time~}t. \quad (8.1)\]

Elementary calculus then implies that

\[P(t + \mathrm{d}t) = P(t) + \frac{\mathrm{d}P}{\mathrm{d}t}\mathrm{d}t, \quad (8.2)\]

but \(P(t + \mathrm{d}t)\) is also the probability of a molecule not colliding up to time \(t\) multiplied by the probability of not colliding in subsequent time dt, i.e.,

\[P(t + \mathrm{d}t) = P(t)(1 - n\sigma v\mathrm{d}t). \quad (8.3)\]

===== Page 90 =====

8.2 The collision cross- section 71

Hence rearranging gives

\[\frac{1}{P}\frac{\mathrm{d}P}{\mathrm{d}t} = -n\sigma v \quad (8.4)\]

and therefore that (using \(P(0) = 1\) )

\[P(t) = \mathrm{e}^{-n\sigma vt}. \quad (8.5)\]

Now the probability of surviving without collision up to time \(t\) but then colliding in the next dt is

\[\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t. \quad (8.6)\]

We can check that this is a proper probability by integrating it,

\[\int_{0}^{\infty}\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t = 1, \quad (8.7)\]

and confirming that it is equal to unity. Here, use has been made of the integral

\[\int_{0}^{\infty}\mathrm{e}^{-x}\mathrm{d}x = 0! = 1 \quad (8.8)\]

(see Appendix C.1). We are now in a position to calculate the mean scattering time \(\tau\) , which is the average time elapsed between collisions for a given molecule. This is given by

\[\begin{array}{rcl}{\tau} & = & {\int_0^\infty t\mathrm{e}^{-n\sigma vt}n\sigma v\mathrm{d}t}\\ {} & = & {\frac{1}{n\sigma v}\int_0^\infty (n\sigma vt)\mathrm{e}^{-n\sigma vt}\mathrm{d}(n\sigma vt)}\\ {} & = & {\frac{1}{n\sigma v}\int_0^\infty xe^{-x}\mathrm{d}x} \end{array} \quad (8.9)\]

where the integral has been simplified by the substitution \(x = n\sigma vt\) . Hence we find that

\[\tau = \frac{1}{n\sigma v}, \quad (8.10)\]

where use has been made of the integral (again, see Appendix C.1)

\[\int_{0}^{\infty}x\mathrm{e}^{-x}\mathrm{d}x = 1! = 1. \quad (8.11)\]

### 8.2 The collision cross-section

In this section we will consider the factor \(\sigma\) in much more detail. To be as general as possible, we will consider two spherical molecules of radii \(a_1\) and \(a_2\) with a hard- sphere potential between them (see Fig. 8.1).

[Image: Two spheres of radii a1 and a2, touching at a point.]
Fig. 8.1 Two spherical molecules of radii \(a_1\) and \(a_2\) with a hard-sphere potential between them.

===== Page 91 =====

72 The mean free path and collisions

This implies that there is a potential energy function \(V(R)\) that depends on the relative separation \(R\) of their centres, and is given by

\[V(R) = \left\{ \begin{array}{ll}0 & R > a_1 + a_2\\ \infty & R\leq a_1 + a_2 \end{array} \right. \quad (8.12)\]

and this is sketched in Fig.8.2.

[Image: A graph of potential energy V(R) versus separation R. V(R) is zero for R > a1+a2 and infinite for R <= a1+a2.]
Fig.8.2 The hard-sphere potential \(V(R)\) .

The impact parameter \(b\) between two moving molecules is defined as the distance of closest approach that would result if the molecular trajectories were undeflected by the collision. Thus for a hard- sphere potential there is only a collision if the impact parameter \(b< a_{1}+\) \(a_{2}\) .Focus on one of these molecules (let's say the one with radius \(a_{1}\) - This is depicted in Fig.8.3. Now imagine molecules of the other type (with radius \(a_{2}\) ) nearby. A collision will only take place if the centre of these other molecules comes inside a tube of radius \(a_{1} + a_{2}\) (so that the molecule labelled A would not collide, whereas B and C would). Thus our first molecule can be considered to sweep out an imaginary tube of space of cross- sectional area \(\pi (a_{1} + a_{2})^{2}\) that defines its "personal space". The area of this tube is called the collision cross- section \(\sigma\) and is then given by

\[\sigma = \pi (a_1 + a_2)^2. \quad (8.13)\]

If \(a_{1} = a_{2} = a\) ,then

\[\sigma = \pi d^2 \quad (8.14)\]

where \(d = 2a\) is the molecular diameter.

[Image: A diagram showing a small molecule of radius a1 moving at velocity v. A tube of radius a1+a2 is swept out. Two other molecules A and B are shown. Molecule A is outside the tube and won't collide. Molecule B is inside the tube and will collide.]
Fig.8.3 A molecule sweeps out an imaginary tube of space of cross-sectional area \(\sigma = \pi (a_{1} + a_{2})^{2}\) . If the centre of another molecule enters this tube, there will be a collision.

Is the hard- sphere potential correct? It is a good approximation at lower temperatures, but progressively worsens as the temperature increases. Molecules are not really hard spheres but slightly squashy objects, and when they move at higher speeds and plough into each other with more momentum, you need more of a direct hit to cause a collision. Thus as the gas is warmed, the molecules may appear to have a smaller cross- sectional area.3

===== Page 92 =====

8.3 The mean free path

Having derived the mean collision time, it is tempting to derive the mean free path as

\[\lambda = \langle v\rangle \tau = \frac{\langle v\rangle}{n\sigma v} \quad (8.15)\]

but what should we take as \(v\) ? A first guess is to use \(\langle v\rangle\) , but that turns out to be not quite right. What has gone wrong?

Our approach to molecular scattering has been to focus on one molecule as the moving one, and think of all of the others as sitting ducks, fixed in space waiting patiently for a collision to occur. The reality is quite different: all molecules are whizzing around. We should therefore take \(v\) as the average relative velocity, i.e., \(\langle v_{\mathrm{r}}\rangle\) , where

\[\pmb {v}_{\mathrm{r}} = \pmb {v}_{1} - \pmb {v}_{2} \quad (8.16)\]

and \(\pmb{v}_{1}\) and \(\pmb{v}_{2}\) are the velocities of two molecules labelled 1 and 2. Now,

\[v_{\mathrm{r}}^{2} = v_{1}^{2} + v_{2}^{2} - 2v_{1}\cdot v_{2}, \quad (8.17)\]

so that

\[\langle v_{\mathrm{r}}^{2}\rangle = \langle v_{1}^{2}\rangle +\langle v_{2}^{2}\rangle = 2\langle v^{2}\rangle , \quad (8.18)\]

because \(\langle \pmb {v}_1\cdot \pmb {v}_2\rangle = 0\) (which follows because \(\langle \cos \theta \rangle = 0\) ). The quantity which we want is \(\langle v_{\mathrm{r}}\rangle\) , but what we have an expression for is \(\langle v_{\mathrm{r}}^{2}\rangle\) . If the probability distribution describing molecular speed is a Maxwell- Boltzmann distribution, then the error in writing \(\langle v_{\mathrm{r}}\rangle \approx \sqrt{\langle v_{\mathrm{r}}^{2}\rangle}\) is small,4 so to a reasonable degree of approximation we can write

\[\langle v_{\mathrm{r}}\rangle \approx \sqrt{\langle v_{\mathrm{r}}^{2}\rangle}\approx \sqrt{2}\langle v\rangle \quad (8.19)\]

and hence we obtain an expression for \(\lambda\) as follows:5

\[\lambda = \frac{1}{\sqrt{2}n\sigma}. \quad (8.20)\]

Substitution of \(p = n k_{\mathrm{B}}T\) yields the expression

\[\lambda = \frac{k_{\mathrm{B}}T}{\sqrt{2}p\sigma}. \quad (8.21)\]

To increase the mean free path by a certain factor, the pressure needs to be decreased by the same factor.

## Example 8.1

Calculate the mean free path for a gas of \(\mathrm{N}_{2}\) at room temperature and pressure. (For \(\mathrm{N}_{2}\) , take the molecular diameter to be \(d = 0.37 \mathrm{nm}\) .)

Solution:

The collision cross- section is \(\pi d^{2} = 4.3\times 10^{- 19}\mathrm{m}^{2}\) .We have \(p\approx 10^{5}\mathrm{Pa}\) and \(T\approx 300\mathrm{K}\) so the number density is \(n = p / k_{\mathrm{B}}T\approx 10^{5} / (1.38\times\) \(10^{- 23}\times 300)\approx 2\times 10^{25}\mathrm{m}^{- 3}\) . This leads to \(\lambda = 1 / (\sqrt{2} n\sigma) = 6.8\times 10^{- 8}\mathrm{m}\)

4Equation 7.23 implies that \(\langle v\rangle /\sqrt{\langle v^{2}\rangle} = \sqrt{\frac{8}{3\pi}} = 0.92\) so the error is less than \(10\%\)

5Although this derivation has used an approximation, it turns out that eqn 8.20 is exact. A brief version of the full derivation is given here. Consider a first class of molecules which move at velocity \(\pmb{v}\) and consider only collisions with a second class of molecules which move at velocity \(\pmb{u}\) . In a frame moving at velocity \(\pmb{u}\) , this second class of molecules are stationary and offer a total cross- section of \(n\sigma f(\pmb {u})\mathrm{d}\pmb {u}\) , where \(f(\pmb {u}) = g(u_{x})g(u_{y})g(u_{z})\) is a Maxwell- Boltzmann distribution for the vector \(\pmb {u} = (u_{x},u_{y},u_{z})\) . In unit time, the total volume swept out by these targets relative to the first class of molecules (which in this frame move at velocity \(\pmb {v} - \pmb {u}\) ) is \(|\pmb {v} - \pmb {u}|n\sigma f(\pmb {u})\mathrm{d}\pmb {u}\) . The number of encounters per second is obtained by multiplying this volume by the probability of finding one of the first class of molecules in unit volume, giving \(|\pmb {v} - \pmb {u}|n\sigma f(\pmb {u})\mathrm{d}\pmb {u}f(\pmb {v})\mathrm{d}\pmb {v}\) . The collision rate \(R\) is therefore obtained by integrating over all \(\pmb{u}\) and \(\pmb{v}\) giving

\[R = n\sigma \int \int |\pmb {v} - \pmb {u}|f(\pmb {u})\mathrm{d}\pmb {u}f(\pmb {v})\mathrm{d}\pmb {v},\]

which writing \(\pmb {x} = (\pmb {v} - \pmb {u}) / \sqrt{2}\) and \(\pmb {y} =\) \((\pmb {v} + \pmb {u}) / \sqrt{2}\) can be transformed into

\[R = n\sigma \sqrt{2}\int |\pmb {x}|f(\pmb {x})\mathrm{d}\pmb {x}\int f(\pmb {y})\mathrm{d}\pmb {y},\]

where the first integral yields \(\langle v\rangle\) and the second integral is unity. Hence \(R =\) \(n\sigma \sqrt{2}\langle v\rangle\) and the mean free path is \(\lambda =\) \(\langle v\rangle /R = 1 / (\sqrt{2} n\sigma)\)

===== Page 93 =====

 Notice that both \(\lambda\) and \(\tau\) decrease with increasing pressure at fixed temperature. Thus the frequency of collisions increases with increasing pressure.

## Chapter summary

The mean scattering time is given by

\[\tau = \frac{1}{n\sigma\langle v_t\rangle},\]

where the collision cross- section is \(\sigma = \pi d^2\) , \(d\) is the molecular diameter and \(\langle v_t \rangle \approx \sqrt{2} \langle v \rangle\) .

The mean free path is

\[\lambda = \frac{1}{\sqrt{2n\sigma}}.\]

## Exercises

(8.1) What is the mean free path of an \(\mathrm{N}_2\) molecule in an ultra- high- vacuum chamber at a pressure of \(10^{- 10}\) mbar? What is the mean collision time? The chamber has a diameter of \(0.5 \mathrm{m}\) . On average, how many collisions will the molecule make with the chamber walls compared with collisions with other molecules? If the pressure is suddenly raised to \(10^{- 6}\) mbar, how do these results change?

(8.2) (a) Show that the root mean square free path is given by \(\sqrt{2} \lambda\) where \(\lambda\) is the mean free path.

(b) What is the most probable free path length?

(c) What percentage of molecules travel a distance greater than (i) \(\lambda\) (ii) \(2\lambda\) (iii) \(5\lambda\) ?

(8.3) Show that particles hitting a plane boundary have travelled a distance \(2\lambda /3\) perpendicular to the plane since their last collision, on average.

(8.4) A diffuse cloud of neutral hydrogen atoms in space has a temperature of \(50 \mathrm{K}\) and number density \(500 \mathrm{cm}^{- 3}\) . Estimate the mean scattering time (in years) between hydrogen atoms in the cloud. Estimate the mean free path (in astronomical units). (1 astronomical unit is the Earth-Sun distance; see Appendix A for a numerical value.)

===== Page 94 =====

1

# Part III

# Transport and thermal diffusion

In the third part of this book, we use our results from the kinetic theory of gases to derive various transport properties of gases and then apply this to solving the thermal diffusion equation. This part is structured as follows:

In Chapter 9, we use the intuition developed from considering molecular collisions and the mean free path to determine various transport properties, in particular viscosity, thermal conductivity, and diffusion. These correspond to the transport of momentum, heat, and particles respectively. In Chapter 10, we derive the thermal diffusion equation, which shows how heat is transported between regions of different temperature. This equation is a differential equation and can be applied to a variety of physical situations, and we show how to solve it in certain cases of high symmetry.

===== Page 95 =====

9

## Transport properties in gases

9.1 Viscosity 76  9.2 Thermal conductivity 81  9.3 Diffusion 83  9.4 More detailed theory 86  Chapter summary 88  Further reading 88  Exercises 89

In this chapter, we wish to describe how a gas can transport momentum, energy, or particles from one place to another. The model we have used so far has been that of a gas in equilibrium, so that none of its macroscopic parameters are time- dependent. Now we consider non- equilibrium situations, but still in the steady state, i.e., so that the system parameters are time- independent, but the surroundings will be time- dependent. The phenomena we want to treat are called transport properties and we will consider

(1) Viscosity, which is the transport of momentum,
(2) Thermal conductivity, which is the transport of heat, and
(3) Diffusion, which is the transport of particles.

### 9.1 Viscosity

This proportionality was suggested by Isaac Newton and holds for many liquids and most gases, which are thus termed Newtonian fluids. NonNewtonian fluids have a viscosity that is a function of the applied shear stress.

Also used is the kinematic viscosity \(\nu\) , defined by \(\nu = \eta /\rho\) , where \(\rho\) is the density. This is useful because one often wants to compare the viscous forces with inertial forces. The unit of kinematic viscosity is \(\mathrm{m}^2 \mathrm{s}^{- 1}\) .

[Image: Two parallel plates separated by a fluid. The top plate moves with velocity u, the bottom is stationary. The velocity profile of the fluid in between is linear, with average velocity <u_x> increasing from bottom to top.]
Fig. 9.1 A fluid is sandwiched between two plates of area \(A\) which each lie in an \(xy\) plane (see text).

Viscosity is the measure of the resistance of a fluid to the deformation produced by a shear stress. For straight, parallel, and uniform flow, the shear stress between the layers is proportional to the velocity gradient in the direction perpendicular to the layers. The constant of proportionality, given the symbol \(\eta\) , is called the coefficient of viscosity, the dynamic viscosity, or simply the viscosity.

Consider the scenario in Fig. 9.1 in which a fluid is sandwiched between two plates of area \(A\) , which each lie in the \(xy\) plane. A shear stress \(\tau_{xz} = F / A\) is applied to the fluid by sliding the top plate over it at speed \(u\) while keeping the bottom plate stationary. A shear force \(F\) is applied. A velocity gradient \(\mathrm{d}\langle u_x\rangle /\mathrm{d}z\) is set up, so that \(\langle u_x \rangle = 0\) near the bottom plate and \(\langle u_x \rangle = u\) near the top plate. If the fluid is a gas, then this extra motion in the \(x\) - direction is superimposed on the Maxwell- Boltzmann motion in the \(x\) , \(y\) and \(z\) directions (and hence the use of the average \(\langle u_x \rangle\) , rather than \(u_x\) ).

The viscosity \(\eta\) is then defined by

\[\tau_{xz} = \frac{F}{A} = \eta \frac{\mathrm{d}\langle u_x\rangle}{\mathrm{d}z}. \quad (9.1)\]

The units of viscosity are \(\mathrm{Pa s} (= \mathrm{N m}^{- 2} \mathrm{s})\) . Force is rate of change of momentum, and hence transverse momentum is being transported

===== Page 96 =====

9.1 Viscosity 77

through the fluid. This is achieved because molecules travelling in the \(+z\) direction move from a layer in which \(\langle u_{x}\rangle\) is smaller to one in which \(\langle u_{x}\rangle\) is larger, and hence they transfer net momentum to that layer in the \(- x\) direction. Molecules travelling parallel to \(- z\) have the opposite effect. Hence, the shear stress \(\tau_{xz}\) is equal to the transverse momentum transported across each square metre per second, and \(\tau_{xz}\) is equal to a flux of momentum (though note that there must be a minus sign involved, because the momentum flux must be from regions of high transverse velocity to regions of low transverse velocity, which is in the opposite direction to the velocity gradient). The velocity gradient \(\partial \langle u_{x}\rangle /\partial z\) therefore drives a momentum flux \(\Pi_{z}\) , according to

\[\Pi_{z} = -\eta \frac{\partial\langle u_{x}\rangle}{\partial z}. \quad (9.2)\]

The viscosity can be calculated using kinetic theory as follows:

Recall first that we showed before in eqn 6.13 that the number of molecules hitting unit area per second is \(v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta\) . Consider molecules travelling at an angle \(\theta\) to the \(z\) - axis (see Fig. 9.2). Then molecules crossing a plane of constant \(z\) will have travelled on average a distance \(\lambda\) since their last collision, and so they will have travelled a distance \(\lambda \cos \theta\) parallel to the \(z\) - axis since their last collision. Over that distance there is an average increase in \(\langle u_{x}\rangle\) given by \((\partial \langle u_{x}\rangle /\partial z)\lambda \cos \theta\) so these upwards- travelling molecules bring an excess momentum in the \(x\) - direction given by

\[-m\left(\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\lambda \cos \theta . \quad (9.3)\]

Hence the total \(x\) - momentum transported across unit area perpendicular to \(z\) in unit time is the momentum flux \(\Pi_{z}\) given by

\[\begin{array}{rcl}\Pi_{z} & = & \int_{0}^{\infty}\int_{0}^{\pi}v\cos \theta n f(v)\mathrm{d}v\frac{1}{2}\sin \theta \mathrm{d}\theta \cdot m\left(-\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\lambda \cos \theta \\ & = & \frac{1}{2} nm\lambda \int_{0}^{\infty}v f(v)\mathrm{d}v\left(-\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\int_{0}^{\pi}\cos^{2}\theta \sin \theta \mathrm{d}\theta \\ & = & -\frac{1}{3} nm\lambda \langle v\rangle \left(\frac{\partial\langle u_{x}\rangle}{\partial z}\right). \end{array} \quad (9.4)\]

Hence the viscosity is given by

\[\eta = \frac{1}{3} nm\lambda \langle v\rangle . \quad (9.5)\]

Equation 9.5 has some important consequences.

\(\eta\) is independent of pressure.

Because \(\lambda \approx 1 / (\sqrt{2} n\sigma)\propto n^{- 1}\) , the viscosity is independent of \(n\) and hence (at constant temperature) it is independent of pressure. This is at first sight a weird result: as you increase the pressure, and hence \(n\) , you should be better at transmitting momentum

[Image: A diagram showing a molecule's velocity vector v at an angle theta to the z-axis. The molecule travels a mean free path lambda before crossing a plane. The distance travelled parallel to the z-axis is lambda cos theta.]
Fig. 9.2 Molecular velocity \(\mathbf{v}\) for molecules travelling at an angle \(\theta\) to the \(z\) -axis. These will have travelled on average a distance \(\lambda\) since their last collision, and so they will have travelled a distance \(\lambda \cos \theta\) parallel to the \(z\) -axis since their last collision.

3The negative sign is because the molecules moving in the \(+z\) direction are moving up the velocity gradient from a slower to a faster region and so bring a deficit in \(x\) - momentum if \(\left(\frac{\partial\langle u_{x}\rangle}{\partial z}\right)\) is positive. It is the same reason for the negative sign in eqn 9.2.

For this calculation, the integration over angle \(\theta\) runs from 0 to \(\pi\) , since we wish to sum over the molecules travelling in all possible directions.

===== Page 97 =====

[Image: A graph of apparent viscosity of air versus pressure. The viscosity is roughly constant over a wide range of pressure, but shows deviations at very low and very high pressures.]
Fig. 9.3 The apparent viscosity of air as a function of pressure at \(288\mathrm{K}\) . It is found to be constant over a wide range of pressure.

because you have more molecules to do it with. However, your mean free path reduces correspondingly, so that each molecule becomes less effective at transmitting momentum in such a way as to precisely cancel out the effect of having more of them. This result holds impressively well over quite a range of pressures (see Fig. 9.3) although it begins to fail at very low or very high pressures.

This result holds impressively well over quite a range of pressures (see Fig. 9.3) although it begins to fail at very low or very high pressures.

\(\eta \propto T^{1 / 2}\) Because \(\eta\) is independent of \(n\) , the only temperature dependence is from \(\langle v\rangle \propto T^{1 / 2}\) , and hence \(\eta \propto T^{1 / 2}\) . Note therefore that the viscosity of gases increases with \(T\) , which is different for most liquids, which get runnier (i.e., less viscous) when you heat them.

Substituting in \(\lambda = (\sqrt{2} n\sigma)^{- 1}\) , \(\sigma = \pi d^2\) and \(\langle v\rangle = (8k_{\mathrm{B}}T / \pi m)^{1 / 2}\) yields a more useful (though less memorable) expression for the viscosity:

\[\eta = \frac{2}{3\pi d^2}\left(\frac{mk_{\mathrm{B}}T}{\pi}\right)^{1 / 2}. \quad (9.6)\]

Equation 9.6 predicts that the viscosity will be proportional to \(\sqrt{m} /d^2\) at constant temperature. This proportionality holds very well, as shown in Fig. 9.4.

[Image: A graph of viscosity at 300 K versus sqrt(m/m_p)/d^2 for various gases. The data points follow a linear trend. The dotted line is the prediction of simple kinetic theory, and the solid line is the prediction of a more detailed theory.]
Fig. 9.4 The dependence of the viscosity of various gases on \(\sqrt{m} /d^2\) . The dotted line is the prediction of eqn 9.6. The solid line is the prediction of eqn 9.45.

Various approximations have gone into this approach, and a condition for their validity is that

\[L\gg \lambda \gg d, \quad (9.7)\]

where \(L\) is the size of the container holding the gas and \(d\) is the molecular diameter. We need \(\lambda \gg d\) (pressure not too high) so that we can neglect collisions involving more than two particles. We need \(\lambda \ll L\) (pressure not too low) so that molecules mainly collide with each other and not with the container walls. If \(\lambda\) is of the

===== Page 98 =====

 same order of magnitude or greater than \(L\) , most of a molecule's collisions will be with the container walls. Figure 9.3 indeed shows that the pressure- independence of the viscosity begins to break down when the pressure is too low or too high.

The factor of \(\frac{1}{3}\) in eqn 9.5 is not quite right, so that eqn 9.6 leads to the dotted line in Fig. 9.4. To get a precise numerical factor, you need to consider the fact that the velocity distribution is different in different layers (because of the shear stress applied) and then average over the distribution of path lengths. This will be done in Section 9.4 and leads to a prediction that gives the solid line in Fig. 9.4.

[Image: A graph of viscosity versus T^(1/2) for Ne, He, and H2. The data follow a roughly linear trend, but show some deviation, indicating the T^(1/2) dependence is not exact.]
Fig. 9.5 The temperature dependence of the viscosity of various gases. The agreement with the predicted \(T^{1 / 2}\) behaviour is satisfactory as a first approximation, but not very good in detail.

The measured temperature dependence of the viscosity of various gases broadly agrees with our prediction that \(\eta \propto \sqrt{T}\) , as shown in Fig. 9.5, but the agreement is not quite perfect. The reason for this is that the collision cross- section, \(\sigma = \pi d^{2}\) , is actually temperature- dependent. At high temperatures, molecules move faster and hence have to collide more directly to have a proper momentum- randomizing collision. We have been assuming that molecules behave as perfect hard spheres and that any collision perfectly randomizes the molecular motion, but this is not precisely true. This means that the effective molecular diameter shrinks as you increase the temperature, increasing the viscosity over and above the expected \(\sqrt{T}\) dependence. This is evident in the data presented in Fig. 9.5.

Viscosity can be measured by the damping of torsional oscillations in the apparatus shown in the box.

===== Page 99 =====

80 Transport properties in gases

## Measurement of viscosity

Maxwell developed a method for measuring the viscosity of a gas by observing the damping rate of oscillations of a disc suspended from a fixed support by a torsion fibre.

[Image: (a) A diagram of Maxwell's method. An oscillating disc is suspended between two fixed horizontal discs. (b) A diagram of the rotating-cylinder method. An inner cylinder is suspended by a torsion fibre inside an outer rotating cylinder.]
Fig.9.6 Measuring viscosity by a Maxwell's method and b the rotating-cylinder method.

It is positioned halfway between two, fixed horizontal discs and oscillates parallel to them in the gas. This is shown in Fig.9.6a with the fixed horizontal discs shaded and the oscillating disc in white. The damping of the torsional oscillations is from the viscous damping due to the gas trapped on each side of the oscillating disc between the fixed discs. The fixed discs are mounted inside a vacuum chamber in which the composition and pressure of the gas to be measured can be varied.

A very accurate method is the rotating- cylinder method, in which gas is confined between two vertical coaxial cylinders. It is shown in Fig.9.6b). The outer cylinder (inner radius \(b\) ) is rotated by a motor at a constant angular speed \(\omega_{0}\) while the inner cylinder outer radius \(a\) ) is suspended by a torsion fibre from a fixed support. The torque \(G\) on the outer cylinder is transmitted via the gas to the inner cylinder and a resulting torque on the torsion fibre. The velocity gradient \(u(r)\) is related to the angular velocity \(\omega (r)\) by \(u(r) = r\omega (r)\) and we expect that \(\omega\) varies all the way from 0 at \(r = a\) to \(\omega_{0}\) at \(r = b\) . The velocity gradient is thus

fibre. The velocity gradient \(u(r)\) is related to the angular velocity \(\omega (r)\) by \(u(r) = r\omega (r)\) and we expect that \(\omega\) varies all the way from 0 at \(r = a\) to \(\omega_{0}\) at \(r = b\) . The velocity gradient is thus

\[\frac{\mathrm{d}u}{\mathrm{d}r} = \omega +r\frac{\mathrm{d}\omega}{\mathrm{d}r}, \quad (9.8)\]

but the first term on the right- hand side simply corresponds to the velocity gradient due to rigid rotation and does not contribute to the viscous shearing stress, which is thus \(\eta \mathrm{rd}\omega /\mathrm{d}r\) . The force \(F\) on a cylindrical element of gas (of length \(l\) ) is then just this viscous stress multiplied by the area of the cylinder \(2\pi r l\) , i.e.,

\[F = 2\pi r l\eta \times r\frac{\mathrm{d}\omega}{\mathrm{d}r}, \quad (9.9)\]

and so the torque \(G = rF\) on this cylindrical element is

\[G = 2\pi r^{3}l\eta \frac{\mathrm{d}\omega}{\mathrm{d}r}. \quad (9.10)\]

In the steady state, there is no change in viscous torque from the outer to the inner cylinder (if there were, angular acceleration would be induced somewhere and the system would change) so this torque is transmitted to the suspended cylinder. Hence rearranging and integrating give

\[G\int_{a}^{b}\frac{\mathrm{d}r}{r^{3}} = 2\pi l\eta \int_{0}^{\omega_{0}}\mathrm{d}\omega = 2\pi l\eta \omega_{0}, \quad (9.11)\]

so that

\[\eta = \frac{G}{4\pi\omega l}\left(\frac{1}{a^2} -\frac{1}{b^2}\right). \quad (9.12)\]

The torque \(G\) is related to the angular deflection \(\phi\) of the inner cylinder by \(G = \alpha \phi\) . The angular deflection can be measured using a light beam reflected from a small mirror attached to the torsion fibre. The coefficient \(\alpha\) is known as the torsion constant. This can be found by measuring the period \(T\) of torsional oscillations of an object of moment of inertia \(I\) suspended from the wire, which is

\[T = 2\pi \sqrt{\frac{I}{\alpha}}. \quad (9.13)\]

Knowledge of \(I\) and \(T\) yields \(\alpha\) which can be used with the measured \(\phi\) to obtain \(G\) and hence \(\eta\) .

===== Page 100 =====

9.2 Thermal conductivity

We have defined heat as "thermal energy in transit".5 It quantifies the transfer of energy in response to a temperature gradient. The amount of heat that flows along a temperature gradient depends on the thermal conductivity of the material, which we will now define.

Thermal conductivity can be considered in one dimension using the diagram shown in Fig. 9.7. Heat flows from hot to cold, and so flows against the temperature gradient. The flow of heat can be described by a heat flux vector \(J\) , whose direction lies along the direction of flow of heat and whose magnitude is equal to the heat energy flowing per unit time per unit area (measured in \(\mathrm{J s^{- 1}m^{- 2} = W m^{- 2}}\) ). The heat flux \(J_{z}\) in the \(z\) - direction is given by

\[J_{z} = -\kappa \left(\frac{\partial T}{\partial z}\right), \quad (9.14)\]

where the negative sign is because heat flows "downhill". The constant \(\kappa\) is called the thermal conductivity of the gas. In general, in three dimensions we can write that the heat flux \(J\) is related to temperature using

\[J = -\kappa \nabla T. \quad (9.15)\]

How do molecules in a gas "carry" heat? Gas molecules have energy, and as we found in eqn 5.17 their mean translational kinetic energy \(\langle \frac{1}{2} mv^2\rangle = \frac{3}{2} k_{\mathrm{B}}T\) depends on the temperature. Therefore to increase the temperature of a gas by \(1\mathrm{K}\) , one has to increase the mean kinetic energy by \(\frac{3}{2} k_{\mathrm{B}}\) per molecule. The heat capacity \(C\) of the gas is the heat required to increase the temperature of gas by \(1\mathrm{K}\) . The heat capacity \(C_{\mathrm{molecule}}\) of a gas molecule is therefore equal to \(\frac{3}{2} k_{\mathrm{B}}\) , though we will later see that it can be larger than this if the molecule can store energy in forms other than translational kinetic energy.8

The derivation of the thermal conductivity of a gas is very similar to that for viscosity. Consider molecules travelling along the \(z\) - axis. Then molecules crossing a plane of constant \(z\) will have travelled on average a distance \(\lambda\) since their last collision, and so they will have travelled a distance \(\lambda \cos \theta\) parallel to the \(z\) - axis since their last collision. Therefore they bring a deficit of thermal energy given by

\[C_{\mathrm{molecule}}\times \Delta T = C_{\mathrm{molecule}}\frac{\partial T}{\partial z}\lambda \cos \theta , \quad (9.16)\]

where \(C_{\mathrm{molecule}}\) is the heat capacity of a single molecule. Hence the total thermal energy transported across unit area in unit time, i.e., the heat flux, is given by

\[\begin{array}{rcl}{J_z} & = & {\int_0^\infty \mathrm{d}v\int_0^\pi \left(-C_{\mathrm{molecule}}\frac{\partial T}{\partial z}\lambda \cos \theta\right)v\cos \theta nf(v)\frac{1}{2}\sin \theta \mathrm{d}\theta}\\ {} & = & {-\frac{1}{2} nC_{\mathrm{molecule}}\lambda \int_0^\infty vf(v)\mathrm{d}v\frac{\partial T}{\partial z}\int_0^\pi \cos^2\theta \sin \theta \mathrm{d}\theta}\\ {} & = & {-\frac{1}{3} nC_{\mathrm{molecule}}\lambda (v)\frac{\partial T}{\partial z}.} \end{array} \quad (9.17)\]

5See Chapter 2.

[Image: A diagram showing two horizontal lines at temperatures T2 (top) and T1 (bottom), with T1 > T2. An arrow labelled Jz points upwards, opposite to the temperature gradient vector.]
Fig. 9.7 Heat flows in the opposite direction to the temperature gradient.

\(^{6}\) Thermal conductivity has units \(\mathrm{Wm^{- 1}K^{- 1}}\) .

See Section 2.2.

\(^{8}\) Other forms include rotational kinetic energy or vibrational energy, if the gas molecules are polyatomic.

===== Page 101 =====

82 Transport properties in gases

Hence the thermal conductivity \(\kappa\) is given by

\[\kappa = \frac{1}{3} C_V\lambda \langle v\rangle , \quad (9.18)\]

where \(C_V = nC_{\mathrm{molecule}}\) is the heat capacity per unit volume (though the subscript \(V\) here refers to a temperature change at constant volume). Equation 9.18 has some important consequences.

[Image: A graph of thermal conductivity versus T^(1/2) for He, Ne, and Ar. The data follow a roughly linear trend.]
Fig.9.8 The thermal conductivity of various gases as a function of temperature. The agreement with the predicted \(T^{1 / 2}\) behaviour is satisfactory as a first approximation, but not very good in detail.

[Image: A graph of thermal conductivity versus 1/(sqrt(m)d^2) for various gases. The data follow a linear trend for noble gases, but N2 deviates slightly.]
Fig.9.9 The dependence of the thermal conductivity of various gases on \(1 / (\sqrt{m} d^2)\) . The dotted line is the prediction of eqn 9.19. The solid line is the prediction of eqn 9.46, which works very well for the monatomic noble gases, but a little less well for diatomic \(\mathrm{N}_2\) .

\(\kappa\) is independent of pressure. The argument is the same as for \(\eta\) . Because \(\lambda \approx 1 / (\sqrt{2} n\sigma)\propto n^{- 1}\) , \(\kappa\) is independent of \(n\) and hence (at constant temperature) it is independent of pressure. \(\kappa \propto T^{1 / 2}\) . The argument is also the same as for \(\eta\) . Because \(\kappa\) is independent of \(n\) , the only temperature dependence is from \(\langle v\rangle \propto \sqrt{T}\) , and hence \(\eta \propto T^{1 / 2}\) . This holds quite well for a number of gases (see Fig. 9.8). As for viscosity, substituting in \(\lambda = (\sqrt{2} n\sigma)^{- 1}\) , \(\sigma = \pi d^2\) and \(\langle v\rangle = (8k_{\mathrm{B}}T / \pi m)^{1 / 2}\) yields a more useful (though less memorable) expression for the thermal conductivity:

\(\kappa \geq \lambda \gg d\) is again the relevant condition for our treatment to hold. Equation 9.19 predicts that the thermal conductivity will be proportional to \(1 / (\sqrt{m} d^2)\) at constant temperature. This holds very well, as shown in Fig. 9.9. Thermal conductivity can be measured by various techniques; see the box.

The similarity of \(\eta\) and \(\kappa\) would suggest that

\[\frac{\kappa}{\eta} = \frac{C_{\mathrm{molecule}}}{m}. \quad (9.20)\]

The ratio \(C_{\mathrm{molecule}} / m\) is the specific heat capacity \(c_{\mathrm{V}}\) (the subscript \(V\) indicating a measurement at constant volume), so equivalently

\[\kappa = c_{\mathrm{V}}\eta . \quad (9.21)\]

However, neither of these relations hold too well. Faster molecules cross a given plane more often than slow ones. These carry more kinetic energy and therefore do carry more heat. However, they don't necessarily carry more average momentum in the \(x\) - direction. We will return to this point in Section 9.4.

===== Page 102 =====

9.3 Diffusion 83

## Measurement of thermal conductivity

The thermal conductivity \(\kappa\) can be measured using the hot- wire method. Gas fills the space between two coaxial cylinders (inner cylinder radius \(a\) outer cylinder radius \(b\) as shown in Fig.9.10.

[Image: A diagram of the hot-wire method. An inner cylinder of radius a at temperature Ta is inside an outer cylinder of radius b at temperature Tb. The space between them is filled with gas.]
Fig.9.10 The hot-wire method for measuring thermal conductivity.

The outer cylinder is connected to a constant- temperature bath of temperature \(T_{b}\) while heat is generated in the inner cylinder (the hot wire) at rate \(Q\) per unit length of the cylinder (measured in units of \(\mathrm{Wm^{- 1}}\) ).The temperature of the inner cylinder rises to \(T_{a}\) The rate \(Q\) can be connected with the radial heat flux \(J_{r}\) using

\[Q = 2\pi rJ_{r}, \quad (9.22)\]

and \(J_{r}\) itself is given by \(- \kappa \partial T / \partial r\) as in eqn 9.14. Hence

\[Q = -2\pi r\kappa \left(\frac{\partial T}{\partial r}\right), \quad (9.23)\]

and rearranging and integrating yields

\[Q\int_{a}^{b}\frac{\mathrm{d}r}{r} = -2\pi \kappa \int_{T_{a}}^{T_{b}}\mathrm{d}T, \quad (9.24)\]

and hence

\[\kappa = \frac{Q}{2\pi}\frac{\ln b / a}{T_a - T_b}. \quad (9.25)\]

Since \(Q\) is known (it is the power supplied to heat the inner cylinder) and \(T_{a}\) and \(T_{b}\) can be measured, the value of \(\kappa\) can be deduced.

An important application of this technique is in the Pirani gauge, which is commonly used in vacuum systems to measure pressure. A sensor wire is heated electrically, and the pressure of the gas is determined by measuring the current needed to keep the wire at a constant temperature. (The resistance of the wire is temperature dependent, so the temperature is estimated by measuring the resistance of the wire.) The Pirani gauge thus relies on the fact that at low pressure the thermal conductivity is a function of pressure (since the condition \(\lambda \ll L\) ,where \(L\) is a linear dimension in the gauge, is not met). In fact, a typical Pirani gauge will not work to detect pressures much above 1 mbar because, above these pressures, the thermal conductivity of the gases no longer changes with pressure. The thermal conductivity of each gas is different, so the gauge has to be calibrated for the individual gas being measured.

### 9.3 Diffusion

Consider a distribution of similar molecules, some of which are labelled (e.g., by being radioactive). Let there be \(n^{*}(z)\) of these labelled molecules per unit volume, but note that \(n^{*}\) is allowed to be a function of the \(z\) coordinate. The flux \(\Phi_{z}\) of labelled molecules parallel to the \(z\) - direction (measured in \(\mathrm{m}^{- 2}\mathrm{s}^{- 1}\) ) is10

\[\Phi_{z} = -D\left(\frac{\partial n^{*}}{\partial z}\right), \quad (9.26)\]

where \(D\) is the coefficient of self- diffusion.11Now consider a thin slab of gas of thickness dz and area \(A\) as shown in Fig.9.11. The flux into the slab is

\[A\Phi_{z}, \quad (9.27)\]

10In three dimensions, this equation is written \(\Phi = - D\nabla n^{*}\) . This is a statement of Fick's law, named after Adolf Fick (1829- 1901).

11We use the phrase self- diffusion because the molecules that are diffusing are the same (apart from being labelled) as the molecules into which they are diffusing. Later we will consider diffusion of molecules into dissimilar molecules.

===== Page 103 =====

 and the flux out of the slab is

\[A\left(\Phi_{z} + \frac{\partial\Phi_{z}}{\partial z}\mathrm{d}z\right). \quad (9.28)\]

[Image: A diagram of a thin slab of gas of thickness dz and area A. An upward arrow shows the flux into the slab, A Phi_z. A downward arrow shows the flux out of the slab, A [Phi_z + (dPhi_z/dz) dz]. The number of particles in the slab is A n* dz.]
Fig. 9.11 The fluxes into and out of a thin slab of gas of thickness \(\mathrm{d}z\) and area \(A\) .

The difference in these two fluxes must be balanced by the time- dependent changes in the number of labelled particles inside the region. Hence

\[\frac{\partial}{\partial t} (n^{*}A\mathrm{d}z) = -A\frac{\partial\Phi_{z}}{\partial z}\mathrm{d}z, \quad (9.29)\]

so that

\[\frac{\partial n^{*}}{\partial t} = -\frac{\partial\Phi_{z}}{\partial z}, \quad (9.30)\]

and hence that

\[\frac{\partial n^{*}}{\partial t} = D\frac{\partial^{2}n^{*}}{\partial z^{2}}. \quad (9.31)\]

This is the diffusion equation. A derivation of the diffusion equation in three dimensions is shown in the box.12

# Three-dimensional derivation of the diffusion equation

The total number of labelled particles that flow out of a closed surface \(S\) is given by the integral

\[\int_{S}\Phi \cdot \mathrm{d}S, \quad (9.32)\]

and this must be balanced by the rate of decrease of labelled particles inside the volume \(V\) surrounded by \(S\) , i.e.,

\[\int_{S}\Phi \cdot \mathrm{d}S = -\frac{\partial}{\partial t}\int_{V}n^{*}\mathrm{d}V. \quad (9.33)\]

The divergence theorem implies that

\[\int_{S}\Phi \cdot \mathrm{d}S = \int_{V}\nabla \cdot \Phi \mathrm{d}V, \quad (9.34)\]

and hence that

\[\nabla \cdot \Phi = -\frac{\partial n^{*}}{\partial t}. \quad (9.35)\]

Substituting in \(\Phi = - D\nabla n^{*}\) then yields the diffusion equation, which is

\[\frac{\partial n^{*}}{\partial t} = D\nabla^{2}n^{*}. \quad (9.36)\]

A kinetic theory derivation of \(D\) proceeds as follows. The excess labelled molecules hitting unit area per second is

\[\begin{array}{rcl}{\Phi_z} & = & {\int_0^\pi \mathrm{d}\theta \int_0^\infty \mathrm{d}v v\cos \theta f(v)\frac{1}{2}\sin \theta \left(-\frac{\partial n^*}{\partial z}\lambda \cos \theta\right)}\\ {} & = & {-\frac{1}{3}\lambda \langle v\rangle \frac{\partial n^*}{\partial z},} \end{array} \quad (9.37)\]

===== Page 104 =====

9.3 Diffusion 85

and hence

\[D = \frac{1}{3}\lambda \langle v\rangle . \quad (9.38)\]

This equation has some important implications:

\(D\propto p^{- 1}\) In this case, there is no factor of \(n\) , but \(\lambda \propto 1 / n\) and hence \(D\propto n^{- 1}\) and at fixed temperature \(D\propto p^{- 1}\) (this holds quite well experimentally, see Fig. 9.12). \(D\propto T^{3 / 2}\) Because \(p = nk_{\mathrm{B}}T\) and \(\langle v\rangle \propto T^{1 / 2}\) , we have that \(D\propto T^{3 / 2}\) at fixed pressure. \(D\rho = \eta\) The only difference between the formula for \(D\) and that for \(\eta\) is a factor of \(\rho = nm\) , and so

\[D\rho = \eta . \quad (9.39)\]

\(D\propto m^{- 1 / 2}d^{- 2}\) , which is the same dependence as thermal conductivity.

The less memorable formula for \(D\) is, as before, obtained by substituting in the expressions for \(\langle v\rangle\) and \(\lambda\) , yielding

\[D = \frac{2}{3\pi nd^2}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}. \quad (9.40)\]

[Image: Two graphs showing diffusion constant D versus pressure. The left graph shows D versus p, with a curve decaying as 1/p. The right graph shows D versus 1/p, with a linear trend.]
Fig. 9.12 Diffusion as a function of pressure.

This section has been about self- diffusion, where labelled atoms (or molecules) diffuse amongst unlabelled, but otherwise identical, atoms (or molecules). Experimentally, it is easier to measure the diffusion of atoms (or molecules) of one type (call them type 1, mass \(m_{1}\) , diameter \(d_{1}\) ) amongst atoms (or molecules) of another type (call them type 2, mass \(m_{2}\) , diameter \(d_{2}\) ). In this case the diffusion constant \(D_{12}\) is used which is given by eqn 9.40 with \(d\) replaced by \((d_{1} + d_{2}) / 2\) and \(m\) replaced by \(2m_{1}m_{2} / (m_{1} + m_{2})\) , so that

\[D_{12} = \frac{2}{3\pi n(\frac{1}{2}[d_1 + d_2])^2}\left(\frac{k_{\mathrm{B}}T(m_1 + m_2)}{2\pi m_1m_2}\right)^{1 / 2}. \quad (9.41)\]

===== Page 105 =====

9.4 More detailed theory

The treatment of the transport properties presented so far in this chapter has the merit that it allows one to get the basic dependences fairly straightforwardly, and gives good insight as to what is going on. However, some of the details of the predictions are not in complete agreement with experiment and it is the purpose of this section to offer a critique of this approach and see how things might be improved. This section contains more advanced material than considered in the rest of this chapter and can be skipped at first reading.

One effect, which we have ignored, is the persistence of velocity after a collision. Our assumption has been that following a collision, a molecule's velocity becomes completely randomized and is completely uncorrelated with its velocity before the collision. However, although that is the simplest approximation to take, it is not correct. After most collisions, a molecule will retain some component of its velocity in the direction of its original motion. Moreover, our treatment has implicitly assumed a Maxwellian distribution of molecular velocities and that the different components of \(\pmb{v}\) are uncorrelated with each other, so that they can be considered to be independent random variables.13 However, these components are actually partially correlated with each other and so are not independent random variables.

A further effect which becomes important at low pressure is the presence of boundaries; the details of the collisions of molecules with walls of a container can be quite important, and such collisions become more important as the pressure is reduced so that the mean free path increases.

Yet another consideration is the interconversion between the internal energy of a molecule and its translational degrees of freedom. As we will see in later chapters, the heat capacity of a molecule contains terms not only due to its translational motion ( \(C_{\mathrm{molecule}} = \frac{3}{2} k_{\mathrm{B}}\) ) but also due to its rotational and vibrational degrees of freedom. Collisions can give rise to processes where a molecule's energy can be redistributed throughout these different degrees of freedom. Thus if the molar heat capacity \(C_{V}\) can be written as the sum of two terms, \(C_{V} = C_{V}^{\prime} + C_{V}^{\prime \prime}\) , where \(C_{V}^{\prime}\) is due to translational degrees of freedom and \(C_{V}^{\prime \prime}\) is due to other degrees of freedom, then it turns out that eqn 9.21 should be amended to give

\[\kappa = \left(\frac{5}{2} C_{V}^{\prime} + C_{V}^{\prime \prime}\right)\eta . \quad (9.42)\]

The \(\frac{5}{2}\) factor reflects the correlations that exist between momentum, energy, and translational motion. The most energetic molecules are the most rapid and therefore possess longer mean free paths. This leads to Eucken's formula, which states that

\[\kappa = \frac{1}{4} (9\gamma -5)\eta C_{V}. \quad (9.43)\]

For an ideal monatomic gas \(\gamma = \frac{5}{3}\) and hence

\[\kappa = \frac{5}{2}\eta C_{V}, \quad (9.44)\]

===== Page 106 =====

9.4 More detailed theory 87

which supersedes eqn 9.21.

A more accurate treatment of the effects mentioned in this section has been performed by Chapman and Enskog (in the twentieth century); the methods used go beyond the scope of this text, but we summarize the results.

The viscosity, which was written as \(\eta = (2 / 3\pi d^2)(mk_B T / \pi)^{1 / 2}\) in eqn 9.6, should be replaced by

\[\eta = \frac{5}{16}\frac{1}{d^2}\left(\frac{mk_B T}{\pi}\right)^{1 / 2}, \quad (9.45)\]

i.e., the \(2 / 3\pi\) should be replaced by \(5 / 16\) .

The corrected formula for \(\kappa\) (which we had evaluated in eqn 9.19) can be obtained from this expression of \(\eta\) using Eucken's formula, eqn 9.43, and hence reads

\[\kappa = \frac{25}{32d^2} C_{\mathrm{molecule}}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}, \quad (9.46)\]

i.e., the \(2 / 3\pi\) should be replaced by \(25 / 32\) .

The formula for \(D\) , which appears in eqn 9.40, should now be replaced by

\[D = \frac{3}{8}\frac{1}{nd^2}\left(\frac{k_{\mathrm{B}}T}{\pi m}\right)^{1 / 2}, \quad (9.47)\]

i.e., the \(2 / 3\pi\) should be replaced by \(3 / 8\) . Similarly, eqn 9.41 should be replaced by

\[D = \frac{3}{8n(\frac{1}{2}[d_1 + d_2])^2}\left(\frac{k_{\mathrm{B}}T(m_1 + m_2)}{2\pi m_1m_2}\right)^{1 / 2}. \quad (9.48)\]

This also alters other conclusions, such as eqn 9.39, which becomes

\[D\rho = \frac{\frac{3}{3}\eta}{\frac{5}{16}} = \frac{6\eta}{5}. \quad (9.49)\]

===== Page 107 =====

88 Further reading

## Chapter summary

Viscosity, \(\eta\) , defined by \(\Pi_{z} = - \eta \partial \langle u_{x} \rangle / \partial z\) is (approximately)

\[\eta = \frac{1}{3} nm\lambda \langle v \rangle .\]

Thermal conductivity, \(\kappa\) , defined by \(J_{z} = - \kappa \partial T / \partial z\) is (approximately)

\[\kappa = \frac{1}{3} C_{V}\lambda \langle v \rangle .\]

Diffusion, \(D\) , defined by \(\Phi_{z} = - D\partial n^{*} / \partial z\) is (approximately)

\[D = \frac{1}{3}\lambda \langle v \rangle .\]

These relationships assume that

\[L\gg \lambda \gg d.\]

The results of a more detailed theory have been summarized (and serve only to alter the numerical factors at the start of each equation).

The predicted pressure, temperature, molecular mass and molecular diameter dependences are:


<table>ηκD× p0× p0× p-1× T1/2× T1/2× T3/2× m1/2d-2× m-1/2d-2× m-1/2d-2</table>

(In this table, \(\propto p^{0}\) means independent of pressure.)

## Further reading

Chapman and Cowling (1970) is the classic treatise describing the more advanced treatment of transport properties in gases.

===== Page 108 =====

9.1) Is air more viscous than water? Compare the dynamic viscosity \(\eta\) and the kinematic viscosity \(\nu = \eta /\rho\) using the following data:


<table>ρ (kg m−3)η (Pa s)Air1.317.4×10−6Water10001.0×10−3</table>

(9.2) Obtain an expression for the thermal conductivity of a gas at ordinary pressures. The thermal conductivity of argon (atomic weight 40) at STP is \(1.6 \times 10^{- 2} \mathrm{Wm}^{- 1} \mathrm{K}^{- 1}\) . Use this to calculate the mean free path in argon at STP. Express the mean free path in terms of an effective atomic radius for collisions and find the value of this radius. Solid argon has a close- packed cubic structure in which, if the atoms are regarded as hard spheres, 0.74 of the volume of the structure is filled. The density of solid argon is \(1.6 \times 10^{3} \mathrm{kg m}^{- 3}\) . Compare the effective atomic radius obtained from this information with your effective collision radius. Comment on your result.

(9.3) Define the coefficient of viscosity. Use kinetic theory to show that the coefficient of viscosity of a gas is given, with suitable approximations, by

\[\eta = K\rho \langle c\rangle \lambda\]

where \(\rho\) is the density of the gas, \(\lambda\) is the mean free path of the gas molecules, \(\langle c \rangle\) is their mean speed, and \(K\) is a number that depends on the approximations you make.

In 1660 Boyle set up a pendulum inside a vessel that was attached to a pump that could remove air from the vessel. He was surprised to find that there was no observable change in the rate of damping of the swings of the pendulum when the pump was set going. Explain his observation in terms of the above formula.

Make a rough order- of- magnitude estimate of the lower limit to the pressure that Boyle obtained; use reasonable assumptions concerning the apparatus that Boyle might have used. [The viscosity of air at atmospheric pressure and at \(293 \mathrm{K}\) is \(18.2 \mu \mathrm{N} \mathrm{s} \mathrm{m}^{- 2}\) .]

Explain why the damping is nearly independent of pressure despite the fact that fewer molecules collide with the pendulum as the pressure is reduced.

(9.4) Two plane discs, each of radius \(5 \mathrm{cm}\) are mounted coaxially with their adjacent surfaces \(1 \mathrm{mm}\) apart. They are in a chamber containing Ar gas at STP (viscosity \(2.1 \times 10^{- 5} \mathrm{Ns} \mathrm{m}^{- 2}\) ) and are free to rotate about their common axis. One of them rotates with an angular velocity of \(10 \mathrm{rad} \mathrm{s}^{- 1}\) . Find the torque that must be applied to the other to keep it stationary.

(9.5) Measurements of the viscosity, \(\eta\) of argon gas \((^{40}\mathrm{Ar})\) over a range of pressures yield the following results at two temperatures:

\[\mathrm{at} 500\mathrm{K}\quad \eta \approx 3.5\times 10^{-5}\mathrm{kg}\mathrm{m}^{-1}\mathrm{s}^{-1};\] \[\mathrm{at} 2000\mathrm{K}\quad \eta \approx 8.0\times 10^{-5}\mathrm{kg}\mathrm{m}^{-1}\mathrm{s}^{-1}.\]

The viscosity is found to be approximately independent of pressure. Discuss the extent to which these data are consistent with (i) simple kinetic theory, and (ii) the diameter of the argon atom (0.34 nm) deduced from the density of solid argon at low temperatures.

(9.6) In Section 11.3, we will define the ratio of \(C_{p}\) to \(C_{V}\) as given by the number \(\gamma\) . We will also show that \(C_{p} = C_{V} + R\) , where the heat capacities here are per mole. Show that these definitions lead to

\[C_{V} = \frac{R}{(\gamma - 1)}. \quad (9.50)\]

Starting with the formulae \(C_{V} = C_{V}^{\prime} + C_{V}^{\prime \prime}\) and \(\kappa = \left(\frac{5}{2} C_{V}^{\prime} + C_{V}^{\prime \prime}\right)\eta\) , show that if \(C_{V}^{\prime} / R = \frac{3}{2}\) , then

\[\kappa = \frac{1}{4} (9\gamma -5)\eta C_{V}, \quad (9.51)\]

which is Eucken's formula. Deduce the value of \(\gamma\) for each of the following monatomic gases measured at room temperatures.


<table>Speciesκ/(ηCV)He2.45Ne2.52Ar2.48Kr2.54Xe2.58</table>

Deduce what proportion of the heat capacity of the molecules is associated with the translational degrees of freedom for these gases. (Hint: notice the word "monatomic".)

===== Page 109 =====

10

## The thermal diffusion equation

10.1 Derivation of the thermal diffusion equation 90  10.2 The one- dimensional thermal diffusion equation 91  10.3 The steady state 94  10.4 The thermal diffusion equation for a sphere 94  10.5 Newton's law of cooling 99  10.6 The Prandtl number 100  10.7 Sources of heat 101  10.8 Particle diffusion 102  Chapter summary 103  Exercises 103

This section assumes familiarity with solving differential equations (see, e.g., Boas (1983), Riley et al. (2006)). It can be omitted at first reading.

[Image: A closed surface S encloses a volume V. Arrows labelled J point outward from the surface, representing heat flux.]
Fig. 10.1 A closed surface \(S\) encloses a volume \(V\) . The total heat flow out of \(S\) is given by \(\int_{S} \mathbf{J} \cdot \mathrm{d} \mathbf{S}\) .

In the previous chapter, we have seen how the thermal conductivity of a gas can be calculated using kinetic theory. In this chapter, we look at solving problems involving the thermal conductivity of matter using a technique developed by mathematicians in the late eighteenth and early nineteenth centuries. The key equation describes thermal diffusion, i.e., how heat appears to "diffuse" from one place to the other, and most of this chapter introduces techniques for solving this equation.

## 10.1 Derivation of the thermal diffusion equation

Recall from eqn 9.15 that the heat flux \(J\) is given by

\[\mathbf{J} = -\kappa \nabla T. \quad (10.1)\]

This equation is very similar mathematically to the equation for particle flux \(\Phi\) in eqn 9.26 which is, in three dimensions,

\[\Phi = -D\nabla n, \quad (10.2)\]

where \(D\) is the diffusion constant, and also to the flow of electrical current given by the current density \(\mathbf{J}_{e}\) defined by

\[\mathbf{J}_{e} = \sigma \mathbf{E} = -\sigma \nabla \phi , \quad (10.3)\]

where \(\sigma\) is the conductivity, \(\mathbf{E}\) is the electric field and \(\phi\) here is the electric potential. Because of this mathematical similarity, an equation that is analogous to the diffusion equation (eqn 9.36) holds in each case. We will derive the thermal diffusion equation in this section.

In fact in all these phenomena, there needs to be some account of the fact that you can't destroy energy, or particles, or charge. (We will only treat the thermal case here.) The total heat flow out of a closed surface \(S\) (as in Fig. 10.1) is given by the integral

\[\int_{S} \mathbf{J} \cdot \mathrm{d} \mathbf{S}, \quad (10.4)\]

and is a quantity with the dimension of power. It is therefore equal to the rate which the material inside the surface is losing energy. This can

===== Page 110 =====

 be expressed as the rate of change of the total thermal energy inside the volume \(V\) surrounded by the closed surface \(S\) . The thermal energy can be written as the volume integral \(\int_{V}CT\mathrm{d}V\) , where \(C\) here is the heat capacity per unit volume (measured in \(\mathrm{JK}^{- 1}\mathrm{m}^{- 3}\) ) and is equal to \(\rho c\) , where \(\rho\) is the density and \(c\) is the heat capacity per unit mass (the specific heat capacity, see Section 2.2). Hence

\[\int_{S}\mathbf{J}\cdot \mathrm{d}\mathbf{S} = -\frac{\partial}{\partial t}\int_{V}CT\mathrm{d}V. \quad (10.5)\]

We haven't worried about what the "zero" of thermal energy is; there could also be an additive, time- independent, constant in the expression for total thermal energy, but since we are going to differentiate this with respect to time to obtain the rate of change of thermal energy, it doesn't matter.

The divergence theorem implies that

\[\int_{S}\mathbf{J}\cdot \mathrm{d}\mathbf{S} = \int_{V}\nabla \cdot \mathbf{J}\mathrm{d}V, \quad (10.6)\]

and hence that

\[\nabla \cdot \mathbf{J} = -C\frac{\partial T}{\partial t}. \quad (10.7)\]

Substituting in eqn 10.1 then yields the thermal diffusion equation which is

\[\frac{\partial T}{\partial t} = D\nabla^2 T, \quad (10.8)\]

where \(D = \kappa /C\) is the thermal diffusivity. Since \(\kappa\) has units \(\mathrm{Wm}^{- 1}\mathrm{K}^{- 1}\) and \(C = \rho c\) has units \(\mathrm{JK}^{- 1}\mathrm{m}^{- 3}\) , \(D\) has units \(\mathrm{m}^2\mathrm{s}^{- 1}\) .

## 10.2 The one-dimensional thermal diffusion equation

In one dimension, this equation becomes

\[\frac{\partial T}{\partial t} = D\frac{\partial^2T}{\partial x^2}, \quad (10.9)\]

and can be solved using conventional methods.

## Example 10.1

Solution of the one- dimensional thermal diffusion equation

The one- dimensional thermal diffusion equation looks a bit like a wave equation. Therefore, one method to solve eqn 10.9 is to look for wave- like solutions of the form

\[T(x,t)\propto \exp (\mathrm{i}(kx - \omega t)), \quad (10.10)\]

where \(k = 2\pi /\lambda\) is the wave vector, \(\omega = 2\pi f\) is the angular frequency, \(\lambda\) is the wavelength and \(f\) is the frequency. Substitution of this equation into eqn 10.9 yields

\[-\mathrm{i}\omega = -Dk^2 \quad (10.11)\]

===== Page 111 =====

92 The thermal diffusion equation

and hence

\[k^{2} = \frac{\mathrm{i}\omega}{D} \quad (10.12)\]

so that

\[k = \pm (1 + \mathrm{i})\sqrt{\frac{\omega}{2D}}. \quad (10.13)\]

The spatial part of the wave, which looks like \(\exp (\mathrm{i}k x)\) , can either be of the form

\[\exp \left((\mathrm{i} - 1)\sqrt{\frac{\omega}{2D}} x\right), \quad \text{which blows up as } x \to -\infty , \quad (10.14)\]

or

\[\exp \left((-\mathrm{i} + 1)\sqrt{\frac{\omega}{2D}} x\right), \quad \text{which blows up as } x \to \infty . \quad (10.15)\]

Let us now solve a problem in which a boundary condition is applied at \(x = 0\) and a solution is desired in the region \(x > 0\) . We don't want solutions that blow up as \(x \to \infty\) and pick the first type of solution (i.e., eqn 10.14). Hence our general solution for \(x \geq 0\) can be written as

\[T(x,t) = \sum_{\omega}A(\omega)\exp (-\mathrm{i}\omega t)\exp \left((\mathrm{i} - 1)\sqrt{\frac{\omega}{2D}} x\right), \quad (10.16)\]

where we have summed over all possible frequencies. To find which frequencies are needed, we have to be specific about the boundary condition for which we want to solve.

Let us imagine that we want to solve the one- dimensional problem of the propagation of sinusoidal temperature waves into the ground. The waves could be due to the alternation of day and night (for a wave with period 1 day), or winter and summer (for a wave with period 1 year). The boundary condition can be written as

\[T(0,t) = T_0 + \Delta T\cos \Omega t. \quad (10.17)\]

This boundary condition can be rewritten

\[T(0,t) = T_0 + \frac{\Delta T}{2}\mathrm{e}^{\mathrm{i}\Omega t} + \frac{\Delta T}{2}\mathrm{e}^{-\mathrm{i}\Omega t}. \quad (10.18)\]

However, at \(x = 0\) the general solution (eqn 10.16) becomes

\[T(0,t) = \sum_{\omega}A(\omega)\exp (-\mathrm{i}\omega t). \quad (10.19)\]

Comparison of eqns 10.18 and 10.19 implies that the only non- zero values of \(A(\omega)\) are

\[A(0) = T_0,\qquad A(-\Omega) = \frac{\Delta T}{2},\qquad \mathrm{and}\qquad A(\Omega) = \frac{\Delta T}{2}. \quad (10.20)\]

Hence the solution to our problem for \(x \geq 0\) is

\[T(x,t) = T_0 + \Delta T\mathrm{e}^{-x / \delta}\cos \left(\Omega t - \frac{x}{\delta}\right), \quad (10.21)\]

===== Page 112 =====

 where

\[\delta = \sqrt{\frac{2D}{\Omega}} = \sqrt{\frac{2\kappa}{\Omega C}} \quad (10.22)\]

is known as the skin depth. The solution in eqn 10.21 is plotted in Fig. 10.2. [Note that the use of the term skin depth brings out the analogy between this effect and the skin depth that arises when electromagnetic waves are incident on a metal surface, see e.g. Griffiths (2003).] We note the following important features of this solution:

We note the following important features of this solution:

\(T\) falls off exponentially as \(\mathrm{e}^{- x / \delta}\) . There is a phase shift of \(x / \delta\) radians in the oscillations. \(\delta \propto \Omega^{- 1 / 2}\) so that faster oscillations fall off faster.

[Image: Two plots of the solution T(x,t). The top is a contour plot of x/delta versus Omega t. The bottom is a 3D surface plot of T versus x/delta and Omega t, showing exponential decay and a phase shift with depth.]
Fig. 10.2 A contour plot and a three-dimensional surface plot of eqn 10.21, showing that the temperature falls off exponentially as \(\mathrm{e}^{- x / \delta}\) . The contour plot shows that there is a phase shift in the oscillations as \(x\) increases.

===== Page 113 =====

10.3 The steady state

If the system has reached a steady state, its properties are not time- dependent. This includes the temperature, so that

\[\frac{\partial T}{\partial t} = 0. \quad (10.23)\]

Hence in this case, the thermal diffusion equation reduces to

\[\nabla^2 T = 0, \quad (10.24)\]

which is Laplace's equation. Note that the thermal diffusivity \(D = \kappa /C\) plays no role in this equation. However, there is still a heat flux \(J = - \kappa \nabla T\) and so the thermal conductivity \(\kappa\) is still relevant.

## Example 10.2

The plane \(x = 0\) is maintained at a temperature \(T_{1}\) and the plane \(x = L\) is maintained at a temperature \(T_{2}< T_{1}\) . Find the heat flux.

Solution:

The steady state implies that we must use Laplace's equation in one dimension so \(\partial^2 T / \partial x^2 = 0\) . Integrating twice and putting in the boundary conditions yields

\[T = \frac{(T_2 - T_1)x}{L} +T_1\mathrm{for}0\leq x\leq L, \quad (10.25)\]

and hence the heat flux is

\[J = -\kappa \left(\frac{\partial T}{\partial x}\right) = \frac{\kappa}{L} (T_1 - T_2). \quad (10.26)\]

The quantity \(\frac{\kappa}{L}\) is called the thermal conductance or sometimes the U value and is measured in \(\mathrm{Wm}^{- 2}\mathrm{K}^{- 1}\) . Its reciprocal \(\frac{L}{\kappa}\) is called the thermal resistance or sometimes the R value and is measured in \(\mathrm{m}^2\mathrm{KW}^{- 1}\) . The thermal resistance of duvets is measured in togs, where 1 tog is equal to \(0.1\mathrm{m}^2\mathrm{KW}^{- 1}\) .

## 10.4 The thermal diffusion equation for a sphere

Very often, heat transfer problems have spherical symmetry (e.g., the cooling of the Earth or the Sun). In this section we will show that one can also solve the (rather forbidding looking) problem of the thermal diffusion equation in a system with spherical symmetry. In spherical polar coordinates, we have in general that \(\nabla^2 T\) is given by<sup>1</sup>

===== Page 114 =====

10.4 The thermal diffusion equation for a sphere 95

\[\nabla^2 T = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right) + \frac{1}{r^2}\frac{\partial}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin \theta \frac{\partial T}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2T}{\partial\phi^2}, \quad (10.27)\]

so that if \(T\) is not a function of \(\theta\) or \(\phi\) we can write

\[\nabla^2 T = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right), \quad (10.28)\]

and hence the diffusion equation becomes

\[\frac{\partial T}{\partial t} = \frac{\kappa}{C}\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right). \quad (10.29)\]

## Example 10.3

The thermal diffusion equation for a sphere in the steady state In the steady state, \(\partial T / \partial t = 0\) and hence we need to solve

\[\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial T}{\partial r}\right) = 0. \quad (10.30)\]

Now if \(T\) is independent of \(r\) \(\partial T / \partial r = 0\) and this will be a solution. Moreover, if \(r^2 (\partial T / \partial r)\) is independent of \(r\) , this will generate another solution. Now \(r^2 (\partial T / \partial r) =\) constant implies that \(T\propto r^{- 1}\) .Hence a general solution is

\[T = A + \frac{B}{r}, \quad (10.31)\]

where \(A\) and \(B\) are constants. This should not surprise us if we know some electromagnetism, as we are solving Laplace's equation in spherical coordinates assuming spherical symmetry, and in electromagnetism the solution for the electric potential in this case is an arbitrary constant plus a Coulomb potential, proportional to \(1 / r\) .

A practical problem one often needs to solve is cooking a quantity of meat. The meat is initially at some cool temperature (the temperature of the kitchen or of the refrigerator) and it is placed into a hot oven. The skill in cooking is getting the inside up to temperature. How long does it take? The next example shows how to calculate this for the (rather artificial) example of a spherical chicken!

## Example 10.4

## The spherical chicken

A spherical chicken \(^2\) of radius \(a\) at initial temperature \(T_0\) is placed into an oven at temperature \(T_{1}\) at time \(t = 0\) see Fig.10.3).The boundary conditions are that the oven is at temperature \(T_{1}\) so that

\[T(a,t) = T_{1}, \quad (10.32)\]

===== Page 115 =====

 and the chicken is originally at temperature \(T_{0}\) , so that for \(r < a\)

\[T(r,0) = T_0. \quad (10.33)\]

[Image: A circle representing a spherical chicken of radius a at initial temperature T0. It is surrounded by a grey region representing the oven at temperature T1.]
Fig. 10.3 Initial condition of a spherical chicken of radius \(a\) at initial temperature \(T_{0}\) , which is placed into an oven at temperature \(T_{1}\) at time \(t = 0\) .

We want to obtain the temperature as a function of time at the centre of the chicken, i.e., \(T(0,t)\) .

Solution:

We will show how we can transform this to a one- dimensional diffusion equation. This is accomplished using a substitution

\[T(r,t) = T_{1} + \frac{B(r,t)}{r}, \quad (10.34)\]

where \(B(r,t)\) is now a function of \(r\) and \(t\) . This substitution is motivated by the solution to the steady- state problem in eqn 10.31 and of course means that we can write \(B\) as \(B = r(T - T_{1})\) .

We now need to work out some partial differentials:

\[\frac{\partial T}{\partial t} = \frac{1}{r}\frac{\partial B}{\partial t}, \quad (10.35)\]

\[\frac{\partial T}{\partial r} = -\frac{B}{r^2} +\frac{1}{r}\frac{\partial B}{\partial r}, \quad (10.36)\]

and hence multiplying eqn 10.36 by \(r^{2}\) we have that

\[r^{2}\frac{\partial T}{\partial r} = -B + r\frac{\partial B}{\partial r}, \quad (10.37)\]

and therefore

\[\frac{\partial}{\partial r}\left[r^{2}\frac{\partial T}{\partial r}\right] = r\frac{\partial^{2}B}{\partial r^{2}}, \quad (10.38)\]

which means that eqn 10.29 becomes

\[\frac{\partial B}{\partial t} = D\frac{\partial^{2}B}{\partial r^{2}}, \quad (10.39)\]

where \(D = \kappa /C\) . This is a one- dimensional diffusion equation and is therefore much easier to solve than the one with which we started.

The new boundary conditions can be rewritten as follows:

(1) Because \(B = r(T - T_{1})\) we have that \(B = 0\) when \(r = 0\) :

\[B(0,t) = 0; \quad (10.40)\]

(2) Because \(T = T_{1}\) at \(r = a\) we have that:

\[B(a,t) = 0; \quad (10.41)\]

(3) Because \(T = T_{0}\) at \(t = 0\) we have that (for \(r < a\) ):

\[B(r,0) = r(T_0 - T_1). \quad (10.42)\]

===== Page 116 =====

10.4 The thermal diffusion equation for a sphere 97

We look for wave- like solutions with these boundary conditions and hence are led to try

\[B = \sin (kr)\mathrm{e}^{-\mathrm{i}\omega t}, \quad (10.43)\]

and substituting this into eqn 10.39 yields

\[\mathrm{i}\omega = Dk^2. \quad (10.44)\]

The relation \(ka = n\pi\) where \(n\) is an integer fits the first two boundary conditions and hence

\[\mathrm{i}\omega = D\left(\frac{n\pi}{a}\right)^2, \quad (10.45)\]

and hence our general solution is

\[B(r,t) = \sum_{n = 1}^{\infty}A_{n}\sin \left(\frac{n\pi r}{a}\right)\mathrm{e}^{-D\left(\frac{n\pi}{a}\right)^{2}t}. \quad (10.46)\]

To find \(A_{n}\) , we need to match this solution at \(t = 0\) using our third boundary condition. Hence

\[r(T_0 - T_1) = \sum_{n = 1}^{\infty}A_n\sin \left(\frac{n\pi r}{a}\right). \quad (10.47)\]

We multiply both sides by sin \(\left(\frac{n\pi r}{a}\right)\) and integrate, so that

\[\int_0^a\sin \left(\frac{n\pi r}{a}\right)r(T_0 - T_1)\mathrm{d}r = \sum_{n = 1}^{\infty}A_n\int_0^a\sin \left(\frac{n\pi r}{a}\right)\sin \left(\frac{n\pi r}{a}\right)\mathrm{d}r. \quad (10.48)\]

The right- hand side yields \(A_{n}a / 2\) and the left- hand side can be integrated by parts. This yields

\[A_{m} = \frac{2a}{m\pi} (T_{1} - T_{0})(-1)^{m}, \quad (10.49)\]

and hence by substituting this back into eqn 10.46 we obtain

\[B(r,t) = \frac{2a}{\pi} (T_1 - T_0)\sum_{n = 1}^{\infty}\frac{(-1)^n}{n}\sin \left(\frac{n\pi r}{a}\right)\mathrm{e}^{-D(n\pi / a)^2t}. \quad (10.50)\]

Putting this back into eqn 10.34 shows that the temperature \(T(r,t)\) inside the chicken \((r\leq a)\) behaves as

\[T(r,t) = T_{1} + \frac{2a}{\pi} (T_{1} - T_{0})\sum_{n = 1}^{\infty}\frac{(-1)^{n}}{n}\frac{\sin(n\pi r / a)}{r}\mathrm{e}^{-D(n\pi / a)^{2}t}. \quad (10.51)\]

The centre of the chicken has temperature

\[T(0,t) = T_{1} + 2(T_{1} - T_{0})\sum_{n = 1}^{\infty}(-1)^{n}\mathrm{e}^{-D(n\pi / a)^{2}t}, \quad (10.52)\]

which is deduced from eqn 10.51 using the fact that as \(r \to 0\)

\[\frac{1}{r}\sin \left(\frac{n\pi r}{a}\right)\to \frac{n\pi}{a}. \quad (10.53)\]

===== Page 117 =====

[Image: A graph of temperature T versus time t for the centre of a spherical chicken. The graph shows T starting at T0, dipping slightly, and then rising asymptotically towards T1. Several curves show the sum of an increasing number of terms from the series solution.]
Fig. 10.4 The sum of the first few terms of eqn 10.52, shown together with \(T(0,t)\) evaluated from all terms (thick solid line). The sums of only the first few terms fail near \(t = 0\) and one needs more and more terms to give an accurate estimate of the temperatures as \(t\) gets closer to 0 (although this is the region where one knows what the temperature is anyway!).

The expression in eqn 10.52 (see Fig. 10.4) becomes dominated by the first exponential in the sum as time \(t\) increases, so that

\[T(0,t)\approx T_{1} - 2(T_{1} - T_{0})\mathrm{e}^{-D(\pi /a)^{2}t}, \quad (10.54)\]

[Image: A graph of cooking time t versus chicken mass m. A solid curve shows t proportional to m^(2/3). A dashed line shows a typical cookery book rule (40 minutes per kg plus 30 minutes). The two lines agree for most normal-sized chickens.]
Fig. 10.5 The cooking time for a chicken according to eqn 10.55 (solid line) and the cook's rule of 40 minutes per kg plus 30 minutes "for the pot" given in many cookery books. The two rules agree for most normal-sized chickens. [Note 1 kg is approximately 2.2 lb.]

for \(t\gg a^{2} / D\pi^{2}\) . Analogous behaviour is of course found for a warm sphere cooling in a colder environment. A cooling or warming body thus behaves like a low- pass filter, with the smallest exponent dominating at long times. The smaller the sphere, the shorter the time before it warms or cools, according to a simple exponential law.

This example shows that the cooking time \(t\) is proportional to \(a^{2}\) . It therefore scales with the surface area \(4\pi a^{2}\) and not the volume \(\frac{4}{3}\pi a^{3}\) . The mass \(m\) of the chicken is proportional to its volume (assuming the density of chickens is constant) and therefore

\[t\propto m^{2 / 3}. \quad (10.55)\]

However, cookery books give a different "law" for cooking chickens: they often quote a rule which is something like 40 minutes per kg plus 30 minutes "for the pot". This is clearly nonsense, since the pot doesn't need cooking, and the rule fails for stir- frying small pieces of chicken (which cook in seconds in a hot pan and clearly don't need 30 minutes added on). However, the two approaches give approximately the same answer for most normal- sized chickens (see Fig. 10.5).

===== Page 118 =====

10.5 Newton's law of cooling 99

## Example 10.5

The surface of a spherical animal of radius \(a\) is maintained at a temperature \(T_{0}\) by its internal metabolism. It sits in a medium of thermal conductivity \(\kappa\) which is at a lower temperature \(T_{1}\) as measured at a large distance from the animal). Assuming steady- state conditions, find the rate at which the animal loses heat.

Solution:

In the region outside the animal, \(\partial T / \partial t = 0\) and hence by eqns 10.30 and 10.31 we have that \(T(r) = A + B / r\) where \(A\) and \(B\) are constants. Since \(T(a) = T_{0}\) and \(T(r)\rightarrow T_{1}\) for \(r\rightarrow \infty\) ,we have \(A = T_{1}\) and \(B = a(T_{0}-\) \(T_{1})\) .The heat flux is radial and is given by \(J = - \kappa \partial T / \partial r = \kappa a(T_{0}-\) \(T_{1}) / r^{2}\) and so at the surface \((r = a)\) is given by \(J = \kappa (T_{0} - T_{1}) / a\) .The total amount of heat lost at the surface per second is therefore obtained by multiplying \(J\) by the surface area of the sphere, yielding \(4\pi a^{2}J =\) \(4\pi \kappa a(T_{0} - T_{1})\) .Note that the heat lost per second is proportional to \(a\) even though the heat generated by the animal presumably scales with its volume and hence with \(a^{3}\) . Therefore heat loss is much more important for small animals than for large ones.

## 10.5 Newton's law of cooling

Newton's law of cooling states that the temperature of a cooling body falls exponentially towards the temperature of its surroundings with a rate proportional to the area of contact between the body and the environment. The results of the previous section indicate that it is an approximation to reality, as a cooling sphere only cools exponentially at long times.

Newton's law of cooling is often stated as follows: the heat loss of a solid or liquid surface (a hot central- heating pipe or the exposed surface of a cup of tea) to the surrounding gas (usually air, which is free to convect the heat away) is proportional to the area of contact multiplied by the temperature difference between the solid/liquid and the gas. Mathematically, this can be expressed as an equation for the heat flux \(J\) , which is

\[J = h\Delta T, \quad (10.56)\]

where \(\Delta T\) is the temperature difference between the body and its environment and \(h\) is a vector whose direction is normal to the surface of the body and whose magnitude \(h = |h|\) is a heat transfer coefficient. In general, \(h\) depends on the temperature of the body and its surroundings and varies over the surface, so that Newton's "law" of cooling is more of an empirical relation.

The steps leading from eqn 10.56 to an exponential decay of temperature are demonstrated in the following example.

===== Page 119 =====

3 One can either have forced convection, in which fluid is driven past the cooling body by some external input of work (provided by means of a pump, fan, propulsive motion of an aircraft, etc.), or free convection, in which any external fluid motion is driven only by the temperature difference between the cooling body and the surrounding fluid. Newton's law of cooling is actually only correct for forced convection, while for free convection (which one should probably use for the example of the cooling of a cup of tea in air) the heat transfer coefficient is temperature dependent \((h \propto (\Delta T)^{1 / 4}\) for laminar flow, \(h \propto (\Delta T)^{1 / 3}\) in the turbulent regime). We examine convection in stars in more detail in Section 35.3.2.

## Example 10.6

A polystyrene cup containing tea at temperature \(T_{\mathrm{hot}}\) at \(t = 0\) stands for a while in a room with air temperature \(T_{\mathrm{air}}\) . The heat loss through the surface area \(A\) exposed to the air is, according to Newton's law of cooling, proportional to \(A(T(t) - T_{\mathrm{air}})\) , where \(T(t)\) is the temperature of the tea at time \(t\) . Ignoring the heat lost by other means, we have that

\[-C\frac{\partial T}{\partial t} = JA = hA(T - T_{\mathrm{air}}), \quad (10.57)\]

where \(J\) is the heat flux, \(C\) is the heat capacity of the cup of tea and \(h\) is a constant, so that

\[T = T_{\mathrm{air}} + (T_{\mathrm{hot}} - T_{\mathrm{air}}) \mathrm{e}^{-\lambda t} \quad (10.58)\]

where \(\lambda = Ah / C\) .

What makes these types of calculation of heat transfer so difficult is that heat transfer from bodies into their surrounding gas or liquid is often dominated by convection. \(^3\) Convection can be defined as the transfer of heat by the motion of or within a fluid (i.e., within a liquid or a gas). Convection is often driven by the fact that warmer fluid expands and rises, while colder fluid contracts and sinks; this causes currents in the fluid to be set up, which rather efficiently transfer heat. Our analysis of the thermal conductivity in a gas ignores such currents. Convection is a very complicated process and can depend on the precise details of the geometry of the surroundings. A third form of heat transfer is by thermal radiation, and this will be the subject of chapter 23.

## 10.6 The Prandtl number

How valid is it to ignore convection? It's clearly fine to ignore it in a solid, but for a fluid we need to know the relative strength of the diffusion of momentum and heat. Convection dominates if momentum diffusion dominates (because convection involves transport of the gas itself) but conduction dominates if heat diffusion dominates. We can express these two diffusivities using the kinematic viscosity \(\nu = \eta /\rho\) (with units \(\mathrm{m}^2 \mathrm{s}^{- 1}\) ) and the thermal diffusivity \(D = \kappa /\rho c_p\) (also with units \(\mathrm{m}^2 \mathrm{s}^{- 1}\) ), where \(\rho\) is the density. To examine their relative magnitudes, we define the Prandtl number as the dimensionless ratio \(\sigma_{\mathrm{p}}\) obtained by dividing \(\nu\) by \(D\) , so that

\[\sigma_{\mathrm{p}} = \frac{\nu}{D} = \frac{\eta c_{\mathrm{p}}}{\kappa}. \quad (10.59)\]

For an ideal gas, we can use \(c_{\mathrm{p}} / c_{\mathrm{V}} = \gamma = \frac{5}{3}\) , and using eqn 9.21 (which states that \(\kappa = c_{\mathrm{V}}\eta\) ) we arrive at \(\sigma_{\mathrm{p}} = \frac{5}{3}\) . However, eqn 9.21 resulted

===== Page 120 =====

10.7 Sources of heat 101

from an approximate treatment, and the corrected version is eqn 9.44 (which states that \(\kappa = \frac{5}{2}\eta c_V\) ), and hence we arrive at

\[\sigma_{\mathrm{p}} = \frac{2}{3}. \quad (10.60)\]

For many gases, the Prandtl number is found to be around this value. It is between 100 and 40000 for engine oil and around 0.015 for mercury. When \(\sigma_{\mathrm{p}} \gg 1\) , diffusion of momentum (i.e., viscosity) dominates over diffusion of heat (i.e., thermal conductivity), and convection is the dominant mode of heat transport. When \(\sigma_{\mathrm{p}} \ll 1\) the reverse is true, and thermal conduction dominates the heat transport.

## 10.7 Sources of heat

If heat is generated at a rate \(H\) per unit volume (so \(H\) is measured in \(\mathrm{Wm}^{- 3}\) ), this will add to the divergence of \(\mathbf{J}\) so that eqn 10.7 becomes

\[\nabla \cdot \mathbf{J} = -C\frac{\partial T}{\partial t} +H, \quad (10.61)\]

and hence the thermal diffusion equation becomes

\[\nabla^2 T = \frac{C}{\kappa}\frac{\partial T}{\partial t} -\frac{H}{\kappa}, \quad (10.62)\]

or equivalently

\[\frac{\partial T}{\partial t} = D\nabla^2 T + \frac{H}{C}. \quad (10.63)\]

## Example 10.7

A metallic bar of length \(L\) with both ends maintained at \(T = T_0\) passes a current, which generates heat \(H\) per unit length of the bar per second. Find the temperature at the centre of the bar in steady state.

Solution: In steady state,

\[\frac{\partial T}{\partial t} = 0, \quad (10.64)\]

and so

\[\frac{\partial^2T}{\partial x^2} = -\frac{H}{\kappa}. \quad (10.65)\]

Integrating this twice yields

\[T = \alpha x + \beta -\frac{H}{2\kappa} x^2, \quad (10.66)\]

where \(\alpha\) and \(\beta\) are constants of integration. The boundary conditions imply that

\[T - T_0 = \frac{H}{2\kappa} x(L - x), \quad (10.67)\]

so that at \(x = L / 2\) we have that the temperature is

\[T = T_0 + \frac{HL^2}{8\kappa}. \quad (10.68)\]

===== Page 121 =====

10.8 Particle diffusion

This chapter has been concerned with the diffusion of heat, but as stated at the beginning of the chapter, the same laws apply to diffusion of particles. Just as heat diffuses down a temperature gradient \(\nabla T\) from hot to cold, so particles diffuse down a concentration gradient \(\nabla n\) from high concentration to low concentration. The mathematics are analogous since the diffusion equation \(\partial n / \partial t = D\nabla^{2}n\) (with \(D\) as a diffusion constant) is essentially the same as the thermal diffusion equation \(\partial T / \partial t = D\nabla^{2}T\) (with \(D = \kappa /C\) as the thermal diffusivity). The techniques presented in this chapter can be used to solve many problems in diffusion physics.

## Example 10.8

A sphere of radius \(a\) is placed in an infinite medium containing certain particles with number density \(n_0\) . The sphere absorbs these particles with great efficiency so that the number density at distance \(r = a\) from the centre of the sphere is zero. Find the rate of absorption of the particles by the sphere.

Solution:

This problem is entirely analogous to that of Example 10.5. Using the same methods, we find

\[n(r) = n_0\left(1 - \frac{a}{r}\right) \quad (10.69)\]

outside the sphere, so that the flux \(\Phi\) at the surface is

\[\Phi = -D\left(\frac{\partial n}{\partial r}\right)_{r = a} = \frac{Dn_0}{a}, \quad (10.70)\]

and so the total rate of absorption is obtained by multiplying \(\Phi\) by the surface area of the sphere which gives

\[\mathrm{rate~of~absorption} = 4\pi an_0. \quad (10.71)\]

Notice that this rate is (again) proportional to the radius \(a\) and not to the area (or even the volume). This has important implications in biology. Bacteria absorb oxygen from their environment and this is at a maximum rate \(4\pi an_0\) (assuming them to be spherical and maximally efficient absorbers), but their consumption of oxygen scales with their volume and hence with \(a^3\) . This sets a maximum limit on the size of a bacterium, because if it is too big the bacterium will not be able to supply its internal oxygen needs. Large organisms are multicellular.

===== Page 122 =====

103

## Chapter summary

The thermal diffusion equation (in the absence of a heat source) is

\[\frac{\partial T}{\partial t} = D\nabla^2 T, \quad (10.72)\]

where \(D = \kappa /C\) is the thermal diffusivity.

"Steady state" implies that

\[\frac{\partial}{\partial t} (\mathrm{physical~quantity}) = 0. \quad (10.73)\]

If heat is generated at a rate \(H\) per unit volume per unit time, then the thermal diffusion equation becomes

\[\frac{\partial T}{\partial t} = D\nabla^2 T + \frac{H}{C}. \quad (10.74)\]

Newton's law of cooling states that the heat loss from a solid or liquid surface is proportional to the area of the surface multiplied by the temperature difference between the solid/liquid and the gas.

The particle diffusion equation is

\[\frac{\partial n}{\partial t} = D\nabla^2 n, \quad (10.75)\]

where \(D\) is the diffusion constant.

## Exercises

(10.1) One face of a thick uniform layer is subject to sinusoidal temperature variations of angular frequency \(\omega\) . Show that damped sinusoidal temperature oscillations propagate into the layer and give an expression for the decay length of the oscillation amplitude. A cellar is built underground and is covered by a ceiling, which is \(3\mathrm{m}\) thick and made of limestone. The outside temperature is subject to daily fluctuations of amplitude \(10^{\circ}\mathrm{C}\) and annual fluctuations of \(20^{\circ}\mathrm{C}\) . Estimate the magnitude of the daily and annual temperature variations within the cellar. Assuming that January is the coldest month of the year, when will the cellar's temperature be at its lowest?

[The thermal conductivity of limestone is \(1.6\mathrm{Wm}^{- 1}\mathrm{K}^{- 1}\) , and the heat capacity of limestone is \(2.5\times 10^{6}\mathrm{J}\mathrm{K}^{- 1}\mathrm{m}^{- 3}\) .]

(10.2) (a) A cylindrical wire of thermal conductivity \(\kappa\) , radius \(a\) and resistivity \(\rho\) uniformly carries a current \(I\) . The temperature of its surface is fixed at \(T_{0}\) using water cooling. Show that the temperature \(T(r)\) inside the wire at radius \(r\) is given by

\[T(r) = T_0 + \frac{\rho I^2}{4\pi^2a^4\kappa} (a^2 -r^2).\]

(b) The wire is now placed in air at temperature \(T_{\mathrm{air}}\) and the wire loses heat from its surface according to Newton's law of cooling (so that the heat flux from the surface of the wire is given by \(\alpha (T(a) - T_{\mathrm{air}})\)

===== Page 123 =====

104 Exercises

where \(\alpha\) is a constant). Find the temperature \(T(r)\)

(10.3) Show that for the problem of a spherical chicken being cooked in an oven considered in Example 10.4, the temperature \(T\) gets \(90\%\) of the way from \(T_{0}\) to \(T_{1}\) after a time \(\sim a^{2}\ln 20 / \pi^{2}D\) .

(10.4) A microprocessor has an array of metal fins attached to it, whose purpose is to remove heat generated within the processor. Each fin may be represented by a long thin cylindrical copper rod with one end attached to the processor; heat received by the rod through this end is lost to the surroundings through its sides.

Show that the temperature \(T(x,t)\) at location \(x\) along the rod at time \(t\) obeys the equation

\[\rho C_{P}\frac{\partial T}{\partial t} = \kappa \frac{\partial^{2}T}{\partial x^{2}} -\frac{2}{a} R(T),\]

where \(a\) is the radius of the rod, and \(R(T)\) is the rate of heat loss per unit area of surface at temperature \(T\) .The surroundings of the rod are at temperature \(T_{0}\) .Assume that \(R(T)\) has the form of Newton's law of cooling, namely

\[R(T) = A(T - T_{0}).\]

In the steady state:

(a) obtain an expression for \(T\) as a function of \(x\) for the case of an infinitely long rod whose hot end has temperature \(T_{\mathrm{m}}\)

(b) show that the heat that can be transported away by a long rod (with radius \(a\) ) is proportional to \(a^{3 / 2}\) provided that \(A\) is independent of \(a\)

In practice the rod is not infinitely long. What length does it need to have for the results above to be approximately valid? The radius of the rod, \(a\) is 1.5 mm.

[The thermal conductivity of copper is \(380\mathrm{Wm}^{- 1}\mathrm{K}^{- 1}\) .The cooling constant \(A =\) \(250\mathrm{Wm}^{- 2}\mathrm{K}^{- 1}\) .]

(10.5) For oscillations at frequency \(\omega\) , a viscous penetration depth \(\delta_{\mathrm{v}}\) can be defined by

\[\delta_{\mathrm{v}} = \left(\frac{2\eta}{\rho\omega}\right)^{1 / 2}, \quad (10.76)\]

analogously to the thermal penetration depth

\[\delta = \left(\frac{2\kappa}{\rho c_{\mathrm{p}}\omega}\right)^{1 / 2} \quad (10.77)\]

defined in this chapter. Show that

\[\left(\frac{\delta_{\mathrm{v}}}{\delta}\right)^{2} = \sigma_{\mathrm{p}}, \quad (10.78)\]

where \(\sigma_{\mathrm{p}}\) is the Prandtl number (see eqn 10.59).

(10.6) For thermal waves, calculate the magnitude of the group velocity. This shows that the thermal diffusion equation cannot hold exactly since the velocity of propagation can become larger than that of any particles that could carry heat through the material. We now consider a modification of the thermal diffusion equation which fixes this problem. Consider the number density \(n\) of thermal carriers in a material. In equilibrium, \(n = n_{0}\) , so that

\[\left(\frac{\partial n}{\partial t}\right) = -\pmb {\nu}\cdot \nabla n + \frac{n - n_{0}}{\tau}, \quad (10.79)\]

where \(\tau\) is a relaxation time and \(\pmb{\nu}\) is the carrier velocity. Multiply this equation by \(\omega \tau \pmb{\nu}\) ,where \(\omega\) is the energy of a carrier, and sum over all \(k\) states. Using the fact that \(\textstyle \sum_{k}n_{0}v = 0\) and \(\begin{array}{r}J = \sum_{k}\omega n v \end{array}\) and that \(|n - n_{0}|\ll n_{0}\) show that

\[\pmb {J} + \tau \frac{\mathrm{d}\pmb{J}}{\mathrm{d}t} = -\kappa \nabla T, \quad (10.80)\]

and hence the modified thermal diffusion equation becomes

\[\frac{\partial T}{\partial t} +\tau \frac{\partial^{2}T}{\partial t^{2}} = D\nabla^{2}T. \quad (10.81)\]

Show that this modified equation gives a group velocity whose magnitude remains finite. Is this modification ever necessary?

(10.7) A series of \(N\) large, flat rectangular slabs with thickness \(\Delta x_{i}\) and thermal conductivity \(\kappa_{i}\) are placed on top of one another. The top and bottom surfaces are maintained at temperature \(T_{i}\) and \(T_{f}\) respectively. Show that the heat flux \(J\) through the slabs is given by \(J = (T_{i} - T_{f}) / \sum_{i}R_{i}\) ,where \(R_{i} = \Delta x_{i} / \kappa_{i}\)

(10.8) The space between two concentric cylinders is filled with material of thermal conductivity \(\kappa\) .The inner (outer) cylinder has radius \(r_1\) \(r_2\) ) and is maintained at temperature \(T_{1}\) \(T_{2}\) ).Derive an expression for the heat flow per unit length between the cylinders.

(10.9) A pipe of radius \(R\) is maintained at a uniform temperature \(T\) .To reduce heat loss from the pipe, it is lagged by an insulating material of thermal conductivity \(\kappa\) .The lagged pipe has radius \(r > R\) .Assume that all surfaces lose heat according to Newton's law of cooling \(\pmb {J} = \pmb {h}\Delta T\) ,where \(h = |h|\) can be taken to be a constant. Show that the heat loss per unit length of pipe is inversely proportional to

\[\frac{1}{hr} +\frac{1}{\kappa}\ln \left(\frac{r}{R}\right), \quad (10.82)\]

and hence show that thin lagging doesn't reduce heat loss if \(R< \kappa /h\)

===== Page 124 =====

1

Fourier was born in Auxerre, France, the son of a tailor. He was schooled there in the Ecole Royale Militaire where he showed early mathematical promise.

[Image: A portrait of J.B.J. Fourier, a man with curly hair and wearing a high collar.]
Fig.10.6 J.B.J.Fourier

In 1787 he entered a Benedictine abbey to train for the priesthood, but the pull of science was too great and he never followed that vocation, instead becoming a teacher at his old school in Auxerre. He was also interested in politics, and unfortunately there was a lot of it around at the time; Fourier became embroiled in the Revolutionary ferment and in 1794 came close to being gull

lottened, but following Robespierre's execution by the same means, the political tide turned in Fourier's favour. He was able to study at the Ecole Normale in Paris under such luminaries as Lagrange and Laplace, and in 1795 took up a chair at the Ecole Polytechnique.

Fourier joined Napoleon on his invasion of Egypt in 1798, becoming governor of Lower Egypt in the process. There he carried out archaeological explorations and later wrote a book about Egypt (which Napoleon then edited to make the history sections more favourable to himself). Nelson's defeat of the French fleet in late 1798 rendered Fourier isolated there, but he nevertheless set up political institutions. He managed to slink back to France in 1801 to resume his academic post, but Napoleon (a hard man to refuse) sent him back to an administrative position in Grenoble where he ended up on such high- brow activities as supervising the draining of swamps and organizing the construction of a road between Grenoble and Turin. He nevertheless found enough time to work on experiments on the propagation of heat and published, in 1807, his memoir on this subject. Lagrange and Laplace criticized his mathematics (Fourier had been forced to invent new techniques to solve the problem, which we now call Fourier series, and this was fearsomely unfamiliar stuff at the time), while the notoriously difficult Biot (he of the Biot- Savart law fame) claimed that Fourier had ignored his own crucial work on the subject (Fourier had discounted it, as Biot's work on this subject was wrong). Fourier's work won him a prize, but reservations about its importance or correctness remained.

heat and published, in 1807, his memoir on this subject. Lagrange and Laplace criticized his mathematics (Fourier had been forced to invent new techniques to solve the problem, which we now call Fourier series, and this was fearsomely unfamiliar stuff at the time), while the notoriously difficult Biot (he of the Biot- Savart law fame) claimed that Fourier had ignored his own crucial work on the subject (Fourier had discounted it, as Biot's work on this subject was wrong). Fourier's work won him a prize, but reservations about its importance or correctness remained.

In 1815, Napoleon was exiled to Elba and Fourier managed to avoid Napoleon who was due to pass through Grenoble en route out of France. When Napoleon escaped, he brought an army to Grenoble and Fourier avoided him again, earning Napoleon's displeasure, but he managed to patch things up and got himself made Prefect of Rhone, a position from which he resigned as soon as he could. Following Napoleon's final defeat at Waterloo, Fourier became somewhat out of favour in political circles and was able to continue working on physics and mathematics back in Paris. In 1822 he published his Théorie analytique de chaleur (Analytical Theory of Heat) which included all his work on thermal diffusion and the use of Fourier series, a work that was to prove influential with many later thermodynamics of the nineteenth century.

In 1824, Fourier wrote an essay that pointed towards what we now call the greenhouse effect; he realised that the insulating effect of the atmosphere might increase the Earth's surface temperature. He understood the way planets lose heat via infrared radiation (though he called it "chaleur obscure"). Since so much of his scientific work had been bound up with the nature of heat (even his work on Fourier series was only performed so he could solve heat problems) he became, in his later years, somewhat obsessed by the imagined healing powers of heat. He kept his house overheated, and wore excessively warm clothes, in order to maximize the effect of the supposedly life- giving heat. He died in 1830 after falling down the stairs.

===== Page 125 =====

This page intentionally left blank

===== Page 126 =====

1

## Part IV

## The first law

In this part we are now ready to think about energy in some detail and hence introduce the first law of thermodynamics. This part is structured as follows:

In Chapter 11, we present the notion of a function of state, of which internal energy is one of the most useful. We discuss in detail the first law of thermodynamics, which states that energy is conserved and heat is a form of energy. We derive expressions for the heat capacity measured at constant volume or pressure for an ideal gas. In Chapter 12 we introduce the key concept of reversibility and discuss isothermal and adiabatic processes.

===== Page 127 =====

11 Energy

11.1 Some definitions 108 11.2 The first law of thermodynamics 110 11.3 Heat capacity 112 Chapter summary 115 Exercises 115

In this chapter we are going to focus on one of the key concepts in thermal physics, that of energy. What happens when energy is changed from one form to another? How much work can you get out of a quantity of heat? These are key questions to be answered. We are now beginning a study of thermodynamics proper, and in this chapter we will introduce the first law of thermodynamics. Before the first law, the most important concept in this chapter, we will introduce some additional ideas.

## 11.1 Some definitions

## 11.1.1 A system in thermal equilibrium

In thermodynamics, we define a system to be whatever part of the Universe we select for study. Near the system are its surroundings. We recall from Section 4.1 that a system is in thermal equilibrium when its macroscopic observables (such as its pressure or its temperature) have ceased to change with time. If you take a gas in a container, which has been held at a certain stable temperature for a considerable period of time, the gas is likely to be in thermal equilibrium. A system in thermal equilibrium having a particular set of macroscopic observables is said to be in a particular equilibrium state. If however, you suddenly apply a lot of heat to one side of the box, then initially at least, the gas is likely to be in a non- equilibrium state.

## 11.1.2 Functions of state

A system is in an equilibrium state if macroscopic observable properties have fixed, definite values, independent of "how they got there". These properties are functions of state (sometimes called variables of state). A function of state is any physical quantity that has a well- defined value for each equilibrium state of the system. Thus, in thermal equilibrium these variables of state have no time dependence. Examples are volume, pressure, temperature, and internal energy, and we will introduce a lot more in what follows. Examples of quantities that are not functions of state include the position of particle number 4325667, the total work done on a system, and the total heat put into the system. Later, we will show in detail why work and heat are not functions of state. However, the point can be understood as follows: the fact that

===== Page 128 =====

11.1 Some definitions 109

your hands are warm or cold depends on their current temperature (a function of state), independently of how you got them to that temperature. For example, you can get to the same final thermodynamic state of having warm hands by different combinations of working and heating, e.g., you can end up with warm hands by rubbing them together (using the muscles in your arms to do work on them) or putting them in a toaster \(^{1}\) (adding heat).

We now give a more mathematical treatment of what is meant by a function of state. Let the state of a system be described by parameters \(\pmb {x} = (x_{1},x_{2},\ldots)\) and let \(f(\pmb {x})\) be some function of state. [Note that this could be a very trivial function, such as \(f(\pmb {x}) = x_{1}\) , since what we've called "parameters" are themselves functions of state. But we want to allow for more complicated functions of state which might be combinations of these "parameters".] Then if the system parameters change from \(\pmb{x}_{1}\) to \(\pmb{x}_{\mathrm{f}}\) , the change in \(f\) is

\[\Delta f = \int_{x_1}^{x_{\mathrm{f}}}\mathrm{d}f = f(x_{\mathrm{f}}) - f(x_{\mathrm{i}}). \quad (11.1)\]

This only depends on the end points \(\pmb{x}_{\mathrm{i}}\) and \(\pmb{x}_{\mathrm{f}}\) . The quantity \(\mathrm{d}f\) is an exact differential (see Appendix C.7) and functions of state have exact differentials. By contrast, a quantity that is represented by an inexact differential is not a function of state. The following example illustrates these kinds of differential.

## Example 11.1

Let a system be described by two parameters, \(x\) and \(y\) . Let \(f = xy\) so that

\[\mathrm{d}f = \mathrm{d}(xy) = y\mathrm{d}x + x\mathrm{d}y. \quad (11.2)\]

Then if \((x,y)\) changes from \((0,0)\) to \((1,1)\) , the change in \(f\) is given by

\[\Delta f = \int_{(0,0)}^{(1,1)}\mathrm{d}f = [xy]_{(0,0)}^{(1,1)} = (1\times 1) - (0\times 0) = 1. \quad (11.3)\]

This answer is independent of the exact path taken (it could be any of those shown in Fig. 11.1) because \(\mathrm{d}f\) is an exact differential.

Now consider \(^{2}\mathrm{d}g = y\mathrm{d}x\) . The change in \(g\) when \((x,y)\) changes from \((0,0)\) to \((1,1)\) along the path shown in Fig. 11.1(a) is given by

\[\Delta g = \int_{(0,0)}^{(1,1)}y\mathrm{d}x = \int_{0}^{1}x\mathrm{d}x = \frac{1}{2}. \quad (11.4)\]

However when the integral is not carried out along the line \(y = x\) , but along the path shown in Fig. 11.1(b), it is given by

\[\Delta g = \int_{(0,0)}^{(1,0)}y\mathrm{d}x + \int_{(1,0)}^{(1,1)}y\mathrm{d}x = 0. \quad (11.5)\]

[Image: Three different paths (a, b, c) between the points (0,0) and (1,1) in the xy-plane.]
Fig. 11.1 Three possible paths between the points \((x,y) = (0,0)\) and \((x,y) = (1,1)\) .

We put a line through quantities such as the d in \(\mathrm{d}g\) to signify that it is an inexact differential.

===== Page 129 =====

3Note that if \(x\) is taken to be volume, \(V\) , and \(y\) is taken to be pressure, \(p\) , then the quantity \(f\) is proportional to temperature, while \(\mathrm{d}g\) is the negative of the work \(\mathrm{d}W = - p\mathrm{d}V\) . This demonstrates that temperature is a function of state and work is not.

If the integral is taken along the path shown in Fig. 11.1(c), yet another result would be obtained, but we are not going to attempt to calculate that!

Hence we find that the value of \(\Delta g\) depends on the path taken, and this is because \(\mathrm{d}g\) is an inexact differential. \(^3\)

Recall from Section 1.2 that functions of state can either be:

- extensive (proportional to system size), e.g., energy, volume, magnetization, mass, or- intensive (independent of system size), e.g., temperature, pressure, magnetic field, density, energy density.

In general one can find an equation of state that connects functions of state: for a gas this takes the form \(f(p,V,T) = 0\) . An example is the equation of state for an ideal gas, \(pV = nRT\) , which we met in eqn 1.12.

## 11.2 The first law of thermodynamics

Though the idea that heat and work are both forms of energy seems obvious to a modern physicist, the idea took some getting used to. Lavoisier had, in 1789, proposed that heat was a weightless, conserved fluid called calorico. Caloric was a fundamental element that couldn't be created or destroyed. Lavoisier's notion "explained" a number of phenomena, such as combustion (fuels have stored caloric which is released on burning). Rumford in 1798 realized that something was wrong with the caloric theory: heating could be produced by friction, and if you keep on drilling through a cannon barrel (to take the example that drew the problem to his attention) almost limitless supplies of heat can be extracted. Where does all this caloric come from? Mayer quantified this in 1842 with an elegant experiment in which he frictionally generated heat in paper pulp and measured the temperature rise. Joule \(^4\) independently performed similar experiments, but more accurately, in the period 1840- 1845 (and his results became better known so that he was able to claim the credit!) Joule let a mass tied to a string slowly descend a certain height, while the other end of the string turns a paddle wheel immersed in a certain mass of water. The turning of the paddle frictionally heats the water. After a number of descents, Joule measured the temperature rise of the water. In this way he was able to deduce the "mechanical equivalent of heat". He also measured the heat output of a resistor (which, in modern units, is equal to \(I^2 R\) , where \(I\) is the current and \(R\) the resistance). He was able to show that the same heat was produced for the same energy used, independent of the method of delivery. This implied that heat is a form of energy. Joule's experiments therefore consigned the caloric theory of heat to a footnote in history.

However, it was Mayer and later Helmholtz who elevated the experimental observations into a grand principle, which we can state as follows:

===== Page 130 =====

11.2 The first law of thermodynamics 111

## The first law of thermodynamics

Energy is conserved and heat and work are both forms of energy.

A system has an internal energy \(U\) , which is the sum of the energy of all the internal degrees of freedom that the system possesses. \(U\) is a function of state because it has a well- defined value for each equilibrium state of the system. We can change the internal energy of the system by heating it or by doing work on it. The heat \(Q\) and work \(W\) are not functions of state since they concern the manner in which energy is delivered to (or extracted from) the system. After the event of delivering energy to the system, you have no way of telling which of \(Q\) or \(W\) was added to (or subtracted from) the system by examining the system's state.

The following analogy may be helpful: your personal bank balance behaves something like the internal energy \(U\) in that it acts like a function of state of your finances; cheques and cash are like heat and work in that they both result in a change in your bank balance, but after they have been paid in, you can't tell by simply looking at the value of your bank balance by which method the money was paid in.

The change in internal energy \(U\) of a system can be written

\[\Delta U = \Delta Q + \Delta W, \quad (11.6)\]

where \(\Delta Q\) is the heat supplied to the system and \(\Delta W\) is the work done on the system. Note the convention: \(\Delta Q\) is positive for heat supplied to the system; if \(\Delta Q\) is negative, heat is extracted from the system; \(\Delta W\) is positive for work done on the system; if \(\Delta W\) is negative, the system does work on its surroundings.

We define a thermally isolated system as a system that cannot exchange heat with its surroundings. In this case we find that \(\Delta U = \Delta W\) , because no heat can pass in or out of a thermally isolated system.

For a differential change, we write eqn 11.6 as

\[\mathrm{d}U = \mathrm{d}Q + \mathrm{d}W, \quad (11.7)\]

where \(\mathrm{d}W\) and \(\mathrm{d}Q\) are inexact differentials.

The work done on stretching a wire by a distance \(\mathrm{d}x\) with a tension \(F\) is (see Fig. 11.2(a))

\[\mathrm{d}W = F\mathrm{d}x. \quad (11.8)\]

The work done by compressing a gas (pressure \(p\) , volume \(V\) ) by a piston can be calculated in a similar fashion (see Fig. 11.2(b)). In this case the force is \(F = pA\) , where \(A\) is the area of the piston, and \(\mathrm{d}Ax = -\mathrm{d}V\) , so that

\[\mathrm{d}W = -p\mathrm{d}V. \quad (11.9)\]

In this equation, the negative sign ensures that the work \(\mathrm{d}W\) done on the system is positive when \(\mathrm{d}V\) is negative, i.e., when the gas is being compressed.

[Image: (a) A wire is stretched by a force F through a distance dx. (b) A gas in a cylinder with a piston is compressed by a distance dx, corresponding to a volume change dV.]
Fig. 11.2 (a) The work done stretching a wire by a distance \(\mathrm{d}x\) is \(F\mathrm{d}x\) . (b) The work done compressing a gas is \(-p\mathrm{d}V\) .

===== Page 131 =====

 It turns out that eqn 11.9 is only strictly true for a reversible change, a point we will explain further in Section 12.1. The idea is that if the piston is not frictionless, or if you move the piston too suddenly and generate shock waves, you will need to do more work to compress the gas because more heat is dissipated in the process.

## 11.3 Heat capacity

We now want to understand in greater detail how adding heat can change the internal energy of gas. In general, the internal energy will be a function of temperature and volume, so that we can write \(U = U(T,V)\) . Hence a small change in \(U\) can be related to changes in \(T\) and \(V\) by

\[\mathrm{d}U = \left(\frac{\partial U}{\partial T}\right)_V\mathrm{d}T + \left(\frac{\partial U}{\partial V}\right)_T\mathrm{d}V. \quad (11.10)\]

Rearranging eqn 11.7 with eqn 11.9 yields

\[\mathrm{d}Q = \mathrm{d}U + p\mathrm{d}V, \quad (11.11)\]

and now using eqn 11.10 we have that

\[\mathrm{d}Q = \left(\frac{\partial U}{\partial T}\right)_V\mathrm{d}T + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\mathrm{d}V. \quad (11.12)\]

We can divide eqn 11.12 by \(\mathrm{d}T\) to obtain

\[\frac{\mathrm{d}Q}{\mathrm{d}T} = \left(\frac{\partial U}{\partial T}\right)_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\frac{\mathrm{d}V}{\mathrm{d}T}, \quad (11.13)\]

which is valid for any change in \(T\) or \(V\) . However, what we want to know is what is the amount of heat we have to add to effect a change of temperature under certain constraints. The first constraint is that of keeping the volume constant. We recall the definition of the heat capacity at constant volume \(C_V\) (see Section 2.2, eqn 2.6) as

\[C_V = \left(\frac{\partial Q}{\partial T}\right)_V. \quad (11.14)\]

From eqn 11.13, this constraint knocks out the second term and implies that

\[C_V = \left(\frac{\partial U}{\partial T}\right)_V. \quad (11.15)\]

The heat capacity at constant pressure is then, using eqns 2.7 and 11.13, given by

\[C_p = \left(\frac{\partial Q}{\partial T}\right)_p \quad (11.16)\]

\[= \left(\frac{\partial U}{\partial T}\right)_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p \quad (11.17)\]

===== Page 132 =====

1.13 Heat capacity 113

so that

\[C_p - C_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p. \quad (11.18)\]

Recall from Section 2.2 that heat capacities are measured in \(\mathrm{JK}^{- 1}\) and refer to the heat capacity of a certain quantity of gas. We will sometimes wish to talk about the heat capacity per mole of gas, or sometimes the heat capacity per mass of gas. We will use small \(c\) for the latter, known as the specific heat capacities:

\[\begin{array}{rcl}{c_V} & = & {\frac{C_V}{M}}\\ {c_p} & = & {\frac{C_p}{M},} \end{array} \quad (11.19)\]

where \(M\) is the mass of the material. Specific heat capacities are measured in \(\mathrm{JK}^{- 1}\mathrm{kg}^{- 1}\) .

## Example 11.2

## Heat capacity of an ideal monatomic gas

For an ideal monatomic gas, the internal energy \(U\) is due to the kinetic energy, and hence \(U = \frac{3}{2} RT\) per mole (see eqn 5.17; this result arises from the kinetic theory of gases). This means that \(U\) is only a function of temperature. Hence

\[\left(\frac{\partial U}{\partial V}\right)_T = 0. \quad (11.21)\]

The equation of state for 1 mole of ideal gas is

\[pV = RT, \quad (11.22)\]

so that

\[V = \frac{RT}{p}, \quad (11.23)\]

and hence

\[\left(\frac{\partial V}{\partial T}\right)_p = \frac{R}{p}, \quad (11.24)\]

and hence using eqns 11.18, 11.21 and 11.24 we have that

\[C_p - C_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p = R. \quad (11.25)\]

Because \(U = \frac{3}{2} RT\) , we therefore have that

\[C_V = \left(\frac{\partial U}{\partial T}\right)_V = \frac{3}{2} R\mathrm{~per~mole}, \quad (11.26)\]

and

\[C_p = C_V + R = \frac{5}{2} R\mathrm{~per~mole}. \quad (11.27)\]

===== Page 133 =====

5 \(\gamma\) is sometimes called the adiabatic exponent.

## Example 11.3

Is it always true that \(\mathrm{d}U = C_V\mathrm{d}T\) Solution:

No, in general eqn 11.10 and eqn 11.15 imply that

\[\mathrm{d}U = C_V\mathrm{d}T + \left(\frac{\partial U}{\partial V}\right)_T\mathrm{d}V. \quad (11.28)\]

For an ideal gas, \(\left(\frac{\partial U}{\partial V}\right)_T = 0\) (eqn 11.21) so it is true that

\[\mathrm{d}U = C_V\mathrm{d}T, \quad (11.29)\]

but for non- ideal gases, \(\left(\frac{\partial U}{\partial V}\right)_T \neq 0\) and hence \(\mathrm{d}U \neq C_V \mathrm{d}T\) .

The ratio of \(C_p\) to \(C_V\) turns out to be a very useful quantity (we will see why in the following chapter) and therefore we give it a special name. We define the adiabatic index \(^5 \gamma\) as the ratio of \(C_p\) and \(C_V\) , so that

\[\gamma = \frac{C_p}{C_V}. \quad (11.30)\]

The reason for the name will become clear in the following chapter.

## Example 11.4

What is \(\gamma\) for an ideal monatomic gas? Solution:

Using the results from the previous example \(^6\)

\[\gamma = \frac{C_p}{C_V} = \frac{C_V + R}{C_V} = 1 + \frac{R}{C_V} = \frac{5}{3}. \quad (11.31)\]

## Example 11.5

Assuming \(U = C_V T\) for an ideal gas, find (i) the internal energy per unit mass and (ii) the internal energy per unit volume.

Solution: Using the ideal gas equation \(pV = Nk_B T\) and the density \(\rho = Nm / V\) (where \(m\) is the mass of one molecule), we find that

\[\frac{p}{\rho} = \frac{k_{\mathrm{B}}T}{m}. \quad (11.32)\]

===== Page 134 =====

 Using eqn 11.31, we have that the heat capacity per mole is given by

\[C_{V} = \frac{R}{\gamma - 1}. \quad (11.33)\]

Hence, we can write that the internal energy for one mole of gas is

\[U = C_{V}T = \frac{RT}{\gamma - 1} = \frac{N_{\mathrm{A}}k_{\mathrm{B}}T}{\gamma - 1}. \quad (11.34)\]

The molar mass is \(mN_{\mathrm{A}}\) , and so dividing eqn 11.34 by the molar mass, yields \(\tilde{u}\) , the internal energy per unit mass, given by

\[\tilde{u} = \frac{p}{\rho(\gamma - 1)}. \quad (11.35)\]

Multiplying \(\tilde{u}\) by the density \(\rho\) gives \(u\) , the internal energy per unit volume, as

\[u = \rho \tilde{u} = \frac{p}{\gamma - 1}. \quad (11.36)\]

## Chapter summary

Functions of state have exact differentials.

The first law of thermodynamics states that "energy is conserved and heat is a form of energy".

\(\mathrm{d}U = \mathrm{d}W + \mathrm{d}Q\)

For a reversible change, \(\mathrm{d}W = - p\mathrm{d}V\)

\[C_{V} = \left(\frac{\partial Q}{\partial T}\right)_{V} = \left(\frac{\partial U}{\partial T}\right)_{V}.\]

\(C_{p} = \left(\frac{\partial Q}{\partial T}\right)_{P}\) and \(C_{p} - C_{V} = R\) for a mole of ideal gas.

The adiabatic index is \(\gamma = C_{p} / C_{V}\)

## Exercises

(11.1) One mole of ideal monatomic gas is confined in a cylinder by a piston and is maintained at a constant temperature \(T_{0}\) by thermal contact with a heat reservoir. The gas slowly expands from \(V_{1}\) to \(V_{2}\) while being held at the same temperature \(T_{0}\) . Why does the internal energy of the gas not

change? Calculate the work done by the gas and the heat flow into the gas.

(11.2) Show that, for an ideal gas,

\[\frac{R}{C_{V}} = \gamma -1 \quad (11.37)\]

===== Page 135 =====

116 Exercises

and

\[\frac{R}{C_p} = \frac{\gamma - 1}{\gamma}, \quad (11.38)\]

where \(C_V\) and \(C_p\) are the heat capacities per mole.

(11.3) Consider the differential

\[\mathrm{d}z = 2xy\mathrm{d}x + (x^2 +2y)\mathrm{d}y. \quad (11.39)\]

Evaluate the integral \(\int_{(x_1,y_1)}^{(x_2,y_2)}\mathrm{d}z\) along the paths consisting of straight- line segments

(i) \((x_{1},y_{1})\rightarrow (x_{2},y_{1})\) and then \((x_{2},y_{1})\rightarrow (x_{2},y_{2})\) (ii) \((x_{1},y_{1})\rightarrow (x_{1},y_{2})\) and then \((x_{1},y_{2})\rightarrow\) \((x_{2},y_{2})\)

Is dz an exact differential?

(11.4) In polar coordinates, \(x = r\cos \theta\) and \(y = r\sin \theta\) The definition of \(x\) implies that

\[\frac{\partial x}{\partial r} = \cos \theta = \frac{x}{r}. \quad (11.40)\]

But we also have \(x^{2} + y^{2} = r^{2}\) , so differentiating with respect to \(r\) gives

\[2x\frac{\partial x}{\partial r} = 2r\Rightarrow \frac{\partial x}{\partial r} = \frac{r}{x}. \quad (11.41)\]

But eqns 11.40 and 11.41 imply that

\[\frac{\partial x}{\partial r} = \frac{\partial r}{\partial x}. \quad (11.42)\]

What's gone wrong?

(11.5) In the comic song by Flanders and Swann about the laws of thermodynamics, they summarize the first law by the statement:

Heat is work and work is heat

Is that a good summary?

===== Page 136 =====

1

## Antoine Lavoisier (1743-1794)

All flammable materials contain the odourless, colourless, tasteless substance phlogiston, and the process of burning them releases this phlogiston into the air. The burned material is said to be "dephlogistonated".

[Image: A portrait of Antoine Lavoisier in 18th century dress.]
Fig.11.3 Antoine Lavoisier

That this notion is completely untrue was first shown by Antoine Lavoisier, who was born into a wealthy Parisian family. Lavoisier showed that both sulphur and phosphorous increase in weight once burned, but the weight gain was lost from the air. He demonstrated that it was oxygen that was responsible for combustion, not phlogiston, and also that oxygen was responsible for the rusting of metals (his oxygen work was helped by results communicated to him

by Joseph Priestley, and Lavoisier was a little lax in giving Priestley credit for this). Lavoisier showed

## Benjamin Thompson [Count Rumford] (1753-1814)

Thompson was born in rural Massachusetts and had an early interest in science.

[Image: A portrait of Benjamin Thompson, Count Rumford, in a red military uniform.]
Fig.11.4 Benjamin Thompson

In 1772, as a humble doctor's apprentice, he married a rich heiress, moved to Rumford, New Hampshire, and got himself appointed as a major in a local militia. He threw his lot in with the British during the American Revolution, feeding them information about the location of American forces and performing scientific work on the force of gunpowder. His British loyalties made him few friends in the land of his birth and he fled to

Britain, abandoning his wife.

text[[65, 826, 488, 889], [505, 88, 928, 283]]
He subsequently fell out with the British and moved, in 1785, to Bavaria where he worked for Elector Karl Theodor who made him a Count, and henceforth he was known as Count Rumford. He organized that hydrogen and oxygen combined to make water and also identified the concept of an element as a fundamental substance that could not be broken down into simpler constituents by chemical processes. Lavoisier combined great experimental skill (and in this, he was ably assisted by his wife) and theoretical insight and is considered a founder of modern chemistry. Unfortunately, he added to his list of elemental substances both light and caloric, his proposed fluid which carried heat. Thus while ridding science of an unnecessary mythical substance (phlogiston), he introduced another one (caloric).

Lavoisier was a tax collector and thus found himself in the firing line when the French revolution started, the fact that he ploughed his dubiously gotten gains into scientific research cutting no ice with revolutionaries. He had unfortunately made an enemy of Jean- Paul Marat, a journalist with an interest in science who in 1780 had wanted to join the French Academy of Sciences, but was blocked by Lavoisier. In 1792 Marat, now a firebrand revolutionary leader, demanded Lavoisier's death. Although Marat was himself assassinated in 1793 (while lying in his bath), Lavoisier was guillotined the following year.

the poor workhouses, established the cultivation of the potato in Bavaria and invented Rumford soup. He continued to work on science, sometimes erratically (he believed that gases and liquids were perfect insulators of heat) but sometimes brilliantly; he noticed that the drilling of metal cannon barrels produced apparently limitless amounts of heat and his subsequent understanding of the production of heat by friction allowed him to put an end to Lavoisier's caloric theory. Not content with simply destroying Lavoisier's theory, he married Lavoisier's widow in 1804, though they separated four years later (Rumford unkindly remarked that Antoine Lavoisier had been lucky to have been guillotined than to have stayed married to her!). In 1799, Rumford founded the Royal Institution of Great Britain, establishing Davy as the first lecturer (Michael Faraday was appointed there 14 years later). He also endowed a medal for the Royal Society and a chair at Harvard. Rumford was also a prolific inventor and gave the world the Rumford fireplace, the double boiler, a drip coffee pot, and, perhaps improbably, baked Alaska (though Rumford's priority on the latter invention is not universally accepted).

===== Page 137 =====

12

## Isothermal and adiabatic processes

12.1 Reversibility 118  12.2 Isothermal expansion of an ideal gas 120  12.3 Adiabatic expansion of an ideal gas 121  12.4 Adiabatic atmosphere 121  Chapter summary 123  Exercises 123

In this chapter we will apply the results of the previous chapter to illustrate some properties concerning isothermal and adiabatic expansions of gases. These results will assume that the expansions are reversible, and so the first part of this chapter explores the key concept of reversibility. This will be important for our discussion of entropy in subsequent chapters.

## 12.1 Reversibility

The laws of physics are reversible, so that if any process is allowed, then the time- reversed process can also occur. For example, if you could film the molecules in a gas bouncing off each other and the container walls, then when watching the film it would be hard to tell whether the film was being played forwards or backwards.

However, there are plenty of processes that you see in nature which seem to be irreversible. For example, consider an egg rolling off the edge of a table and smashing on the floor. Potential energy is converted into kinetic energy as the egg falls, and ultimately the energy ends up as a small amount of heat in the broken egg and the floor. The law of conservation of energy does not forbid the conversion of that heat back into kinetic energy of the reassembled egg which would then leap off the ground and back on to the table. However, this is never observed to happen. As another example, consider a battery driving a current \(I\) through a resistor with resistance \(R\) and dissipating heat \(I^{2}R\) into the environment. Again, one never finds heat being absorbed by a resistor from its environment, resulting in the generation of a spontaneous current that can used to recharge the battery.

Lots of processes are like this, in which the final outcome is some potential, chemical, or kinetic energy that gets converted into heat, which is then dissipated into the environment. As we shall see, the reason seems to be that there are lots more ways that the energy can be distributed in heat than in any other way, and this is therefore the most probable outcome. To try and understand this statistical nature of reversibility, it is helpful to consider the following example.

===== Page 138 =====

1

## Example 12.1

We return to the situation described in Example 4.1. To recap, you are given a large box containing 100 identical coins. With the lid on the box, you give it a really good long and hard shake, so that you can hear the coins flipping, rattling, and being generally tossed around. Now you open the lid and look inside the box. Some of the coins will be lying with heads facing up and some with tails facing up. We assume that each of the \(2^{100}\) possible possible configurations (the microstates) are equally likely to be found. Each of these is equally likely and so each has a probability of occurrence of approximately \(10^{- 30}\) . However, the measurement made is counting the number of heads and the number of tails (the macrostates), and the results of this measurement are not equally likely. In Example 4.1 we showed that of the \(\approx 10^{30}\) individual microstates, a large number \((\approx 4\times 10^{27})\) corresponded to 50 heads and 50 tails, but only one microstate corresponded to 100 heads and 0 tails.

Now, imagine that you had in fact carefully prepared the coins so that they were lying heads up. Following a good shake, the coins will most probably be a mixture of heads and tails. If, on the other hand, you carefully prepared a mixed arrangement of heads and tails, a good shake of the box is very unlikely to achieve a state in which all the coins lie with heads facing up. The process of shaking the box seems almost always to randomize the number of heads and tails, and this is an irreversible process.

This shows that the statistical behaviour of large systems is such as to make certain outcomes (such as a box of coins with mixed heads and tails) more likely than certain others (such as a box of coins containing coins the same way up). The statistics of large numbers therefore seems to drive many physical changes in an irreversible direction. How can we carry out a process in a reversible fashion?

The early researchers in thermodynamics wrestled with this problem, which was of enormous practical importance in the design of engines, in which you want to waste as little heat as possible to make your engine as efficient as possible. It was realized that when gases are expanded or compressed, it is possible to convert energy irreversibly into heat, and this will generally occur when we perform the expansion or the compression very fast, causing shock waves to be propagated through the gas (we will consider this effect in more detail in Chapter 32). However, it is possible to perform the expansion or compression reversibly if we do it sufficiently slowly so that the gas remains in equilibrium throughout the entire process and passes seamlessly from one equilibrium state to the next, each equilibrium state differing from the previous one by an infinitesimal change in the system parameters. Such a process is said to be quasistatic, since the process is almost in completely unchanging static equilibrium. As we shall see, heat can nevertheless be absorbed or

===== Page 139 =====

1This is an important point: reversibility does not necessarily exclude the generation of heat. However, reversibility does require the absence of friction; a vehicle braking and coming to a complete stop, converting its kinetic energy into heat through friction in the brakes, is an irreversible process.

emitted in the process, while still maintaining reversibility. In contrast, for an irreversible process, a non- zero change (rather than a sequence of infinitesimal changes) is made to the system, and therefore the system is not in equilibrium throughout the process.

An important (but given the name, perhaps not surprising) property of reversible processes is that you can run them in reverse. This fact we will use a great deal in Chapter 13. Of course, it would take an infinite amount of time for a strictly reversible process to occur, so most processes we term reversible are approximations to the "real thing".

## 12.2 Isothermal expansion of an ideal gas

In this section, we will calculate the heat change in a reversible isothermal expansion of an ideal gas. The word isothermal means "at constant temperature", and hence in an isothermal process

\[\Delta T = 0. \quad (12.1)\]

For an ideal gas, we showed in eqn 11.29 that \(\mathrm{d}U = C_V\mathrm{d}T\) , and so this means that for an isothermal change

\[\Delta U = 0, \quad (12.2)\]

since \(U\) is a function of temperature only. Equation 12.2 implies that \(\mathrm{d}U = 0\) and hence from eqn 11.7

\[\mathrm{d}W = -\mathrm{d}Q, \quad (12.3)\]

so that the work done by the gas on its surroundings as it expands is equal to the heat absorbed by the gas. We can use \(\mathrm{d}W = - p\mathrm{d}V\) (eqn 11.9), which is the correct expression for the work done in a reversible expansion. Hence the heat absorbed by the gas during an isothermal expansion from volume \(V_{1}\) to volume \(V_{2}\) of 1 mole of an ideal gas at temperature \(T\) is

\[\begin{array}{rcl}{\Delta Q} & = & {\int \mathrm{d}Q}\\ {} & {} & {}\\ {} & = & {-\int \mathrm{d}W}\\ {} & {} & {}\\ {} & = & {\int_{V_1}^{V_2}p\mathrm{d}V}\\ {} & {} & {}\\ {} & = & {\int_{V_1}^{V_{2}}\frac{RT}{V}\mathrm{d}V}\\ {} & {} & {}\\ {} & = & {RT\ln \frac{V_2}{V_1}.} \end{array} \quad (12.8)\]

For an expansion, \(V_{2} > V_{1}\) , and so \(\Delta Q > 0\) . The internal energy has stayed the same, but the volume has increased so that the energy density has gone down. The energy density and the pressure are proportional to one another, so that pressure will also have decreased.

===== Page 140 =====

12.3 Adiabatic expansion of an ideal gas

The word adiathermal means "without flow of heat". A system bounded by adiathermal walls is said to be thermally isolated. Any work done on such a system produces an adiathermal change. We define a change to be adiabatic if it is both adiathermal and reversible. In an adiabatic expansion, therefore, there is no flow of heat and we have

\[\mathrm{d}Q = 0. \quad (12.9)\]

The first law of thermodynamics therefore implies that

\[\mathrm{d}U = \mathrm{d}W. \quad (12.10)\]

For an ideal gas, \(\mathrm{d}U = C_V\mathrm{d}T\) , and using \(\mathrm{d}W = - p\mathrm{d}V\) for a reversible change, we find that, for 1 mole of ideal gas,

\[C_V\mathrm{d}T = -p\mathrm{d}V = -\frac{RT}{V}\mathrm{d}V, \quad (12.11)\]

so that

\[\ln \frac{T_2}{T_1} = -\frac{R}{C_V}\ln \frac{V_2}{V_1}. \quad (12.12)\]

Now \(C_p = C_V + R\) , and dividing this by \(C_V\) yields

\[\gamma = \frac{C_p}{C_V} = 1 + \frac{R}{C_V}, \quad (12.13)\]

and therefore \(-(R / C_V) = 1 - \gamma\) , so that eqn 12.12 becomes

\[T V^{\gamma -1} = \mathrm{constant}, \quad (12.14)\]

or equivalently (using \(pV\propto T\) for an ideal gas)

\[p^{1 - \gamma}T^{\gamma} = \mathrm{constant} \quad (12.15)\]

and

\[pV^{\gamma} = \mathrm{constant}, \quad (12.16)\]

the last equation probably being the most memorable.

Figure 12.1 shows isotherms (lines of constant temperature, as would be followed in an isothermal expansion) and adiabats (lines followed by an adiabatic expansion in which heat cannot enter or leave the system) for an ideal gas on a graph of pressure against volume. At each point, the adiabats have a steeper gradient than the isotherms, a fact we will return to in a later chapter.

## 12.4 Adiabatic atmosphere

The hydrostatic equation (eqn 4.23) expresses the additional pressure due to a thickness \(\mathrm{d}z\) of atmosphere with density \(\rho\) and is

\[\mathrm{d}p = -\rho g\mathrm{d}z. \quad (12.17)\]

===== Page 141 =====

3 Atmospheric physicists call a "bit" of air a "parcel".

[Image: A graph of p versus V showing several isotherms (solid curves) and adiabats (dashed curves). The adiabats are steeper than the isotherms.]
Fig. 12.1 Isotherms (solid lines) and adiabats (dashed lines).

Since \(p = nk_{\mathrm{B}}T\) and \(\rho = nm\) , where \(m\) is the mass of one molecule, we can write \(\rho = mp / k_{\mathrm{B}}T\) and hence

\[\frac{\mathrm{d}p}{\mathrm{d}z} = -\frac{mgp}{k_{\mathrm{B}}T}, \quad (12.18)\]

which implies that

\[T\frac{\mathrm{d}p}{p} = -\frac{mg}{k_{\mathrm{B}}}\mathrm{d}z. \quad (12.19)\]

For an isothermal atmosphere, \(T\) is a constant, and one obtains the results of Example 4.4. This assumes that the whole atmosphere is at a uniform temperature, which is unrealistic. A much better approximation (although nevertheless still an approximation to reality) is that each parcel of air \(^3\) does not exchange heat with its surroundings. This means that if a parcel of air rises, it expands adiabatically. In this case, eqn 12.19 can be solved by recalling that for an adiabatic expansion \(p^{1 - \gamma}T^{\gamma}\) is a constant (see eqn 12.15) and hence that

\[(1 - \gamma)\frac{\mathrm{d}p}{p} +\gamma \frac{\mathrm{d}T}{T} = 0. \quad (12.20)\]

Substituting this into eqn 12.19 yields

\[\frac{\mathrm{d}T}{\mathrm{d}z} = -\left(\frac{\gamma - 1}{\gamma}\right)\frac{mg}{k_{\mathrm{B}}}, \quad (12.21)\]

which is an expression relating the rate of decrease of temperature with height, predicting it to be linear. We can rewrite \((\gamma - 1) / \gamma = R / C_{p}\) and using \(R = N_{\mathrm{A}}k_{\mathrm{B}}\) and writing the molar mass \(M_{\mathrm{molar}} = N_{\mathrm{A}}m\) we can write eqn 12.21 as

\[\frac{\mathrm{d}T}{\mathrm{d}z} = -\frac{M_{\mathrm{molar}}g}{C_p}. \quad (12.22)\]

===== Page 142 =====

 The quantity \(M_{\mathrm{molarg}} / C_p\) is known as the adiabatic lapse rate. For dry air (mostly nitrogen), it comes out as \(9.7 \mathrm{K} \mathrm{km}^{- 1}\) . Experimental values in the atmosphere are closer to \(6 - 7 \mathrm{K} \mathrm{km}^{- 1}\) (partly because the atmosphere isn't dry, and latent heat effects, due to the heat needed to evaporate water droplets [and sometimes that ice crystals], are also important).

## Chapter summary

- In an isothermal expansion \(\Delta T = 0\) .- An adiabatic change is both adiathermal (no flow of heat) and reversible. In an adiabatic expansion of an ideal gas, \(pV^{\gamma}\) is constant.

## Exercises

(12.1) In an adiabatic expansion of an ideal gas, \(pV^{\gamma}\) is constant. Show also that

\[\begin{array}{rcl}{TV^{\gamma -1}} & = & {\mathrm{constant},}\\ {T} & = & {\mathrm{constant}\times p^{1 - 1 / \gamma}.} \end{array} \quad (12.24)\]

(12.2) Assume that gases behave according to a law given by \(pV = f(T)\) , where \(f(T)\) is a function of temperature. Show that this implies

\[\left(\frac{\partial p}{\partial T}\right)_V = \frac{1}{V}\frac{\mathrm{d}f}{\mathrm{d}T}, \quad (12.25)\]

Show also that

\[\left(\frac{\partial Q}{\partial V}\right)_p = C_p\left(\frac{\partial T}{\partial V}\right)_p, \quad (12.27)\]

In an adiabatic change, we have that

\[\mathrm{d}Q = \left(\frac{\partial Q}{\partial p}\right)_V\mathrm{d}p + \left(\frac{\partial Q}{\partial V}\right)_p\mathrm{d}V = 0. \quad (12.29)\]

Hence show that \(pV^{\gamma}\) is a constant.

(12.3) Explain why we can write

\[\begin{array}{rcl}{\mathrm{d}Q} & = & {C_p\mathrm{d}T + A\mathrm{d}p\quad \mathrm{and}}\\ {\mathrm{d}Q} & = & {C_V\mathrm{d}T + B\mathrm{d}V,} \end{array} \quad (12.31)\]

where \(A\) and \(B\) are constants. Subtract these equations and show that

\[(C_p - C_V)\mathrm{d}T = B\mathrm{d}V - A\mathrm{d}p, \quad (12.32)\]

and that at constant temperature

\[\left(\frac{\partial p}{\partial V}\right)_T = \frac{B}{A}. \quad (12.33)\]

In an adiabatic change, show that

\[\begin{array}{rcl}{\mathrm{d}p} & = & {-(C_p / A)\mathrm{d}T,}\\ {\mathrm{d}V} & = & {-(C_V / B)\mathrm{d}T.} \end{array} \quad (12.34)\]

Hence show that in an adiabatic change, we have that

\[\begin{array}{rcl}{\left(\frac{\partial p}{\partial V}\right)_{\mathrm{adiabatic}}} & = & {\gamma \left(\frac{\partial p}{\partial V}\right)_T,}\\ {\left(\frac{\partial V}{\partial T}\right)_{\mathrm{adiabatic}}} & = & {\frac{1}{1 - \gamma}\left(\frac{\partial V}{\partial T}\right)_p,}\\ {\left(\frac{\partial p}{\partial T}\right)_{\mathrm{adiabatic}}} & = & {\frac{\gamma}{\gamma - 1}\left(\frac{\partial p}{\partial T}\right)_V.} \end{array} \quad (12.36)\]

(12.4) Using eqn 12.36, relate the gradients of adiabats and isotherms on a \(p - V\) diagram.

===== Page 143 =====

12.5) Two thermally insulated cylinders, A and B, of equal volume, both equipped with pistons, are connected by a valve. Initially A has its piston fully withdrawn and contains a perfect monatomic gas at temperature \(T\) , while B has its piston fully inserted, and the valve is closed. Calculate the final temperature of the gas after the following operations, which each start with the same initial arrangement. The thermal capacity of the cylinders is to be ignored.

(a) The valve is fully opened and the gas slowly drawn into B by pulling out the piston B; piston A remains stationary.

(b) Piston B is fully withdrawn and the valve is opened slightly; the gas is then driven as far as it will go into B by pushing home piston A at such a rate that the pressure in A remains constant: the cylinders are in thermal contact.

12.6) In Richhardt's method of measuring \(\gamma\) , illustrated in Fig. 12.2, a ball of mass \(m\) is placed snugly inside a tube (cross- sectional area \(A\) ) connected to a container of gas (volume \(V\) ). The pressure \(p\) of the gas inside the container is slightly greater than atmospheric pressure \(p_0\) because of the downwards force of the ball, so that

\[p = p_0 + \frac{mg}{A}. \quad (12.39)\]

Show that if the ball is given a slight downwards displacement, it will undergo simple harmonic motion with period \(\tau\) given by

\[\tau = 2\pi \sqrt{\frac{mV}{\gamma pA^2}}. \quad (12.40)\]

[You may neglect friction. As the oscillations are fairly rapid, the changes in \(p\) and \(V\) that occur can be treated as occurring adiabatically.]

In Rinkel's 1929 modification of this experiment, the ball is held in position in the neck where the gas pressure \(p\) in the container is exactly equal to air pressure, and then let drop, the distance \(L\) that it falls before it starts to go up again is measured. Show that this distance is given by

\[mgL = \frac{\gamma pA^2L^2}{8V}. \quad (12.41)\]

[Image: A diagram of Richhardt's apparatus. A ball of mass m oscillates in a tube. The tube is connected to a container of gas of volume V and pressure p. The pressure outside is p0.]
Fig. 12.2 Richhardt's apparatus for measuring \(\gamma\) . A ball of mass \(m\) oscillates up and down inside a tube.

===== Page 144 =====

1

## Part V

## The second law

In this part we introduce the second law of thermodynamics and follow its consequences. This part is structured as follows:

In Chapter 13, we consider heat engines, which are cyclic processes that convert heat into work. We state various forms of the second law of thermodynamics and prove their equivalence, in particular showing that no engine can be more efficient than a Carnot engine. We also prove Clausius' theorem, which applies to any cyclic process. In Chapter 14 we show how the results from the preceding chapter lead to the concept of entropy. We derive the important equation \(\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V\) , which combines the first and second laws of thermodynamics. We also introduce the Joule expansion and use it to discuss the statistical interpretation of entropy and Maxwell's demon. There is a very deep connection between entropy and information, and we explore this in Chapter 15, briefly touching on data compression and quantum information.

===== Page 145 =====

13

## Heat engines and the second law

13.1 The second law of thermodynamics 126  13.2 The Carnot engine 127  13.3 Carnot's theorem 130  13.4 Equivalence of Clausius' and Kelvin's statements 131  13.5 Examples of heat engines 131  13.6 Heat engines running backwards 133  13.7 Clausius' theorem 134  Chapter summary 137  Further reading 137  Exercises 137

A reservoir in this context is a body, which is sufficiently large that we can consider it to have essentially infinite heat capacity. This means that you can keep sucking heat out of it, or dumping heat into it, without its temperature changing. See Section 4.6.

2The "in isolation" phrase is very important here. In a refrigerator, heat is sucked out of cold food and squirted out of the back into your warm kitchen, so that it flows in the "wrong" direction: from cold to hot. However, this process is not happening in isolation. Work is being done by the refrigerator motor and electrical power is being consumed, adding to your electricity bill.

In this chapter, we introduce the second law of thermodynamics, probably the most important and far- reaching of all concepts in thermal physics. We are going to illustrate it with an application to the theory of "heat engines", which are machines that produce work from a temperature difference between two reservoirs. It was by considering these engines that such nineteenth century physicists as Carnot, Clausius and Kelvin came to develop their different statements of the second law of thermodynamics. However, as we will see in subsequent chapters, the second law of thermodynamics has a wider applicability, affecting all types of processes in large systems and bringing insights in information theory and cosmology. In this chapter, we will begin by stating two alternative forms of the second law of thermodynamics and then discuss how these statements impact on the efficiency of heat engines.

## 13.1 The second law of thermodynamics

The second law of thermodynamics can be formulated as a statement about the direction of heat flow that occurs as a system approaches equilibrium (and hence there is a connection with the direction of the "arrow of time"). Heat is always observed to flow from a hot body to a cold body, and the reverse process, in isolation, never occurs. Therefore, following Clausius, we can state the second law of thermodynamics as follows:

Clausius' statement of the second law of thermodynamics "No process is possible whose sole result is the transfer of heat from a colder to a hotter body."

It turns out that an equivalent statement of the second law of thermodynamics can be made, concerning how easy it is to change energy between different forms, in particular between work and heat. It is very easy to convert work into heat. For example, pick up a brick of mass \(m\) and carry it up to the top of a building of height \(h\) (thus doing work on it equal to mgh) and then let it fall back to ground level by dropping it off the top (being careful not to hit passing pedestrians). All the work that you've done in carrying the brick to the top of the building will be dissi

===== Page 146 =====

 pated in heat (and a small amount of sound energy) as the brick hits the ground. However, conversion of heat into work is much harder, and in fact the complete conversion of heat into work is impossible. This point is expressed in Kelvin's statement of the second law of thermodynamics:

# Kelvin's statement of the second law of thermodynamics:

"No process is possible whose sole result is the complete conversion of heat into work."

These two statements of the second law of thermodynamics do not seem to be obviously connected, but the equivalence of these two statements will be shown in Section 13.4.

## 13.2 The Carnot engine

Kelvin's statement of the second law of thermodynamics says that you can't completely convert heat into work. However, it does not forbid some conversion of heat into work. How good a conversion from heat to work is possible? To answer this question, we have to introduce the concept of an engine. We define an engine as a system operating a cyclic process that converts heat into work. It has to be cyclic so that it can be continuously operated, producing a steady power.

[Image: A p-V diagram showing a Carnot cycle. It consists of two isotherms (AB and CD) and two adiabats (BC and DA). The cycle is traversed clockwise A -> B -> C -> D -> A.]
Fig. 13.1 A Carnot cycle consists of two reversible adiabats (BC and DA) and two reversible isotherms (AB and CD). The Carnot cycle is here shown on a \(p - V\) plot. It is operated in the direction A→B→C→D→A, i.e., clockwise around the solid curve. Heat \(Q_{\mathrm{h}}\) enters in the isotherm A→B and heat \(Q_{\ell}\) leaves in the isotherm C→D.

One such engine is the Carnot engine, which is based on a process called a Carnot cycle and which is illustrated in Fig. 13.1. An equivalent plot which is easier to sketch is shown in Fig. 13.2. The Carnot cycle consists of two reversible adiabats and two reversible isotherms for an ideal gas. The engine operates between two heat reservoirs, one at a higher temperature \(T_{\mathrm{h}}\) and one at a lower temperature \(T_{\ell}\) . Heat enters and leaves only during the reversible isotherms (because no heat can

===== Page 147 =====

[Image: A T-S diagram for a Carnot cycle. The cycle is a rectangle. The top isotherm is at T_h, the bottom isotherm at T_l. Heat Q_h enters along the top isotherm A->B. Heat Q_l leaves along the bottom isotherm D->C.]
Fig. 13.2 A Carnot cycle can be drawn on replotted axes where the isotherms are shown as horizontal lines ( \(T\) is constant for an isotherm) and the adiabats are shown as vertical lines (where the quantity \(S\) , which must be some function of \(pV^{\gamma}\) , is constant in an adiabatic expansion; in Chapter 14 we will give a physical interpretation of \(S\) ).

enter or leave during an adiabat). Heat \(Q_{\mathrm{h}}\) enters during the expansion A→B and heat \(Q_{\ell}\) leaves during the compression C→D. Because the process is cyclic, the change of internal energy (a state function) in going round the cycle is zero. Hence the work output by the engine, \(W\) , is given by

\[W = Q_{\mathrm{h}} - Q_{\ell}. \quad (13.1)\]

## Example 13.1

Find an expression for \(Q_{\mathrm{h}} / Q_{\ell}\) for an ideal gas undergoing a Carnot cycle in terms of the temperatures \(T_{\mathrm{h}}\) and \(T_{\ell}\) .

Solution:

Using the results of Section 12.2, we can write down

\[\begin{array}{rcl}{{\bf A}}&{{\bf B}:}&{{Q_{\mathrm{h}}=RT_{\mathrm{h}}\ln\frac{V_{\mathrm{B}}}{V_{\mathrm{A}}}},\\{{\bf B}}&{{\bf C}:}&{{\left(\frac{T_{\mathrm{h}}}{T_{\ell}}\right)=\left(\frac{V_{\mathrm{C}}}{V_{\mathrm{B}}}\right)^{\gamma-1}}},\\{{\bf C}}&{{\bf D}:}&{{Q_{\ell}=-RT_{\ell}\ln\frac{V_{\mathrm{D}}}{V_{\mathrm{C}}}}},\\{{\bf D}}&{{\bf A}:}&{{\left(\frac{T_{\ell}}{T_{\mathrm{h}}}\right)=\left(\frac{V_{\mathrm{A}}}{V_{\mathrm{D}}}\right)^{\gamma-1}}}. \end{array} \quad (13.5)\]

Equations 13.3 and 13.5 lead to

\[\frac{V_{\mathrm{B}}}{V_{\mathrm{A}}} = \frac{V_{\mathrm{C}}}{V_{\mathrm{D}}}, \quad (13.6)\]

and dividing eqn 13.2 by eqn 13.4 and substituting in eqn 13.6 leads to

\[\frac{Q_{\mathrm{h}}}{Q_{\ell}} = \frac{T_{\mathrm{h}}}{T_{\ell}}. \quad (13.7)\]

This is a key result. \(^3\)

===== Page 148 =====

12 The Carnot engine 129

The Carnot engine is shown schematically in Fig. 13.3. It is drawn as a machine with heat input \(Q_{\mathrm{h}}\) from a reservoir at temperature \(T_{\mathrm{h}}\) drawn as a horizontal line, and two outputs, one of work \(W\) and the other of heat \(Q_{\ell}\) , which passes into the reservoir at temperature \(T_{\ell}\) .

The concept of efficiency is important to characterize engines. It is the ratio of "what you want to achieve" to "what you have to do to achieve it". For an engine, what you want to achieve is work (to pull a train up a hill for example) and what you have to do to achieve it is to put heat in (by shovelling coal into the furnace), keeping the hot reservoir at \(T_{\mathrm{h}}\) and providing heat \(Q_{\mathrm{h}}\) for the engine. We therefore define the efficiency \(\eta\) of an engine as the ratio of the work out to the heat in. Thus

\[\eta = \frac{W}{Q_{\mathrm{h}}} \quad (13.8)\]

Note that since the work out cannot be greater than the heat in (i.e., \(W< Q_{\mathrm{h}}\) ) we must have that \(\eta < 1\) . The efficiency must be below \(100\%\) .

[Image: A schematic diagram of a Carnot engine. A circle labeled "Carnot" has an input arrow Q_h from a hot reservoir at T_h, an output arrow W for work, and an output arrow Q_l to a cold reservoir at T_l.]
Fig. 13.3 A Carnot engine shown schematically. In diagrams such as this one, the arrows are labelled with the heat and work flowing in one cycle of the engine.

## Example 13.2

For the Carnot engine, the efficiency can be calculated using eqns 13.1, 13.7, and 13.8 as follows: substituting eqn 13.1 into 13.8 yields

\[\eta_{\mathrm{Carnot}} = \frac{Q_{\mathrm{h}} - Q_{\ell}}{Q_{\mathrm{h}}}, \quad (13.9)\]

and eqn 13.7 then implies that

\[\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}} - T_{\ell}}{T_{\mathrm{h}}} = 1 - \frac{T_{\ell}}{T_{\mathrm{h}}}. \quad (13.10)\]

How does this efficiency compare to that of a real engine? It turns out that real engines are much less efficient than Carnot engines.

## Example 13.3

A power station steam turbine operates between \(T_{\mathrm{h}} \sim 800 \mathrm{~K}\) and \(T_{\ell} = 300 \mathrm{~K}\) . If it were a Carnot engine, it could achieve an efficiency of \(\eta_{\mathrm{Carnot}} = (T_{\mathrm{h}} - T_{\ell}) / T_{\mathrm{h}} \approx 60\%\) , but in fact real power stations do not achieve the maximum efficiency and figures closer to \(40\%\) are typical.

===== Page 149 =====

4This means that Carnot's theorem is, in itself, a statement of the second law of thermodynamics.

## 13.3 Carnot's theorem

The Carnot engine is in fact the most efficient engine possible! This is stated in Carnot's theorem, as follows:

## Carnot's theorem

Of all the heat engines working between two given temperatures, none is more efficient than a Carnot engine.

Remarkably, one can prove Carnot's theorem on the basis of Clausius' statement of the second law of thermodynamics. The proof follows a reductio ad absurdum argument.

[Image: A schematic diagram showing engine E connected to a Carnot engine running backwards. Engine E takes heat Q_h' from T_h, outputs work W, and rejects heat Q_l' to T_l. The Carnot engine takes work W, takes heat Q_l from T_l, and dumps heat Q_h to T_h.]
Fig. 13.4 A hypothetical engine E, which is more efficient than a Carnot engine, is connected to a Carnot engine.

Proof: Imagine that E is an engine that is more efficient than a Carnot engine (i.e., \(\eta_{\mathrm{E}} > \eta_{\mathrm{Carnot}}\) ). The Carnot engine is reversible so one can run it in reverse. Engine E, and a Carnot engine run in reverse, are connected together as shown in Fig. 13.4. Now since \(\eta_{\mathrm{E}} > \eta_{\mathrm{Carnot}}\) , we have that

\[\frac{W}{Q_{\mathrm{h}}^{\prime}} > \frac{W}{Q_{\mathrm{h}}}, \quad (13.11)\]

and so

\[Q_{\mathrm{h}} > Q_{\mathrm{h}}^{\prime}. \quad (13.12)\]

The first law of thermodynamics implies that

\[W = Q_{\mathrm{h}}^{\prime} - Q_{\mathrm{f}}^{\prime} = Q_{\mathrm{h}} - Q_{\mathrm{f}}, \quad (13.13)\]

so that

\[Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime} = Q_{\mathrm{f}} - Q_{\mathrm{f}}^{\prime}. \quad (13.14)\]

Now \(Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime}\) is positive because of eqn 13.12, and therefore so is \(Q_{\ell} - Q_{\ell}^{\prime}\) The expression \(Q_{\mathrm{h}} - Q_{\mathrm{h}}^{\prime}\) is the net amount of heat dumped into the reservoir at temperature \(T_{\mathrm{h}}\) .The expression \(Q_{\ell} - Q_{\ell}^{\prime}\) is the net amount of heat extracted from the reservoir at temperature \(T_{\ell}\) .Because both these expressions are positive, the combined system shown in Fig. 13.4 simply extracts heat from the reservoir at \(T_{\ell}\) and dumps it into the reservoir at \(T_{\mathrm{h}}\) .This violates Clausius' statement of the second law of thermodynamics, and therefore engine E cannot exist.

[Image: A schematic diagram showing a Carnot engine connected to a reversible engine R running backwards. The Carnot engine takes heat Q_h from T_h, outputs work W, and rejects heat Q_l to T_l. Engine R takes work W, takes heat Q_l' from T_l, and dumps heat Q_h' to T_h.]
Fig. 13.5 A hypothetical reversible engine R is connected to a Carnot engine.

Corollary: All reversible engines working between two temperatures have the same efficiency \(\eta_{\mathrm{Carnot}}\) .

Proof: Imagine another reversible engine R. Its efficiency \(\eta_{\mathrm{R}} \leq \eta_{\mathrm{Carnot}}\) by Carnot's theorem. We run it in reverse and connect it to a Carnot engine going forwards, as shown in Fig. 13.5. This arrangement will simply transfer heat from the cold reservoir to the hot reservoir and violates Clausius' statement of the second law of thermodynamics unless \(\eta_{\mathrm{R}} = \eta_{\mathrm{Carnot}}\) . Therefore all reversible engines have the same efficiency

\[\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}} - T_{\ell}}{T_{\mathrm{h}}}. \quad (13.15)\]

===== Page 150 =====

13.4 Equivalence of Clausius' and Kelvin's statements statements

We first prove the proposition that if a system violates Kelvin's statement of the second law of thermodynamics, it violates Clausius' statement of the second law of thermodynamics.

Proof: If a system violates Kelvin's statement of the second law of thermodynamics, one could connect it to a Carnot engine as shown in Fig. 13.6. The first law implies that

\[Q_{\mathrm{h}}^{\prime} = W \quad (13.16)\]

and that

\[Q_{\mathrm{h}} = W + Q_{\ell}. \quad (13.17)\]

The heat dumped in the reservoir at temperature \(T_{\mathrm{h}}\) is

\[Q_{\mathrm{h}} - Q_{\ell}^{\prime} = Q_{\ell}. \quad (13.18)\]

This is also equal to the heat extracted from the reservoir at temperature \(T_{\ell}\) . The combined process therefore has the net result of transferring heat \(Q_{\ell}\) from the reservoir at \(T_{\ell}\) to the reservoir at \(T_{\mathrm{h}}\) as its sole effect and thus violates Clausius' statement of the second law of thermodynamics. Therefore the Kelvin violator does not exist.

We now prove the opposite proposition, that if a system violates Clausius' statement of the second law of thermodynamics, it violates Kelvin's statement of the second law of thermodynamics.

Proof: If a system violates Clausius' statement of the second law of thermodynamics, one could connect it to a Carnot engine as shown in Fig. 13.7. The first law implies that

\[Q_{\mathrm{h}} - Q_{\ell} = W. \quad (13.19)\]

The sole effect of this process is thus to convert heat \(Q_{\mathrm{h}} - Q_{\ell}\) into work and thus violates Kelvin's statement.

We have thus shown the equivalence of Clausius' and Kelvin's statements of the second law of thermodynamics.

[Image: A schematic diagram showing a Kelvin violator connected to a Carnot engine. The Kelvin violator takes heat Q_h' and outputs work W. The Carnot engine takes work W, takes heat Q_l from T_l, and dumps heat Q_h to T_h.]
Fig. 13.6 A Kelvin violator is connected to a Carnot engine.

[Image: A schematic diagram showing a Clausius violator connected to a Carnot engine. The Clausius violator takes heat Q_l from T_l and dumps it to T_h. The Carnot engine takes heat Q_h from T_h, outputs work W, and rejects heat Q_l to T_l.]
Fig. 13.7 A Clausius violator is connected to a Carnot engine.

## 13.5 Examples of heat engines

One of the first engines to be constructed was made in the first century by Hero of Alexandria, and is sketched in Fig. 13.8(a). It consists of a hollow sphere with a pair of bent pipes projecting from it. Steam is fed via another pair of pipes and once expelled through the bent pipes causes rotational motion. Though Hero's engine convincingly converts heat into work, and thus qualifies as a bona fide heat engine, it was little more than an entertaining toy. More practical was the engine sketched in Fig. 13.8(b), which was designed by Thomas Newcomen (1664- 1729).

===== Page 151 =====

 This was one of the first practical steam engines and was used for pumping water out of mines. Steam is used to push the piston upwards. Then cold water is injected from the tank and condenses the steam, reducing the pressure in the piston. Atmospheric pressure then pushes the piston down and raises the beam on the other side of the fulcrum. The problem with Newcomen's engine was that one had then to heat up the steam chamber again before steam could be readmitted and so it was extremely inefficient. James Watt (1736- 1819) famously improved the design so that condensation took place in a separate chamber, which was connected to the steam cylinder by a pipe. This work led the foundation of the industrial revolution.

[Image: Sketches of three engines. (a) Hero's engine: a sphere with bent pipes that rotates when steam is expelled. (b) Newcomen's engine: a beam engine with a piston and a separate boiler. (c) Stirling's engine: a hot and cold cylinder arrangement driving a flywheel.]
Fig. 13.8 Sketches of (a) Hero's engine, (b) Newcomen's engine, and (c) Stirling's engine.

Another design of an engine is Stirling's engine, the brainchild of the Rev. Robert Stirling (1790- 1878), which is sketched in Fig. 13.8(c), It works purely by the repeated heating and cooling of a sealed amount of gas. In the particular engine shown in Fig. 13.8(c), the crankshaft is driven by the two pistons in an oscillatory fashion, but the \(90^{\circ}\) bend ensures that the two pistons move out of phase. The motion is driven by a temperature differential between the top and bottom surfaces of the engine. The design is very simple and contains no valves and operates at relatively low pressures. However, such an engine literally has to "warm up" to establish the temperature differential and so it is harder to regulate power output.

One of the most popular engines is the internal combustion engine used in most automobile applications. Rather than externally heating water to produce steam (as with Newcomen's and Watt's engines) or to produce a temperature differential (as with Stirling's engine), here the burning of fuel inside the engine's combustion chamber generates the high temperature and pressure necessary to produce useful work. Different fuels can be used to drive these engines, including diesel, gasoline, natural gas, and even biofuels, such as ethanol. These engines all pro

===== Page 152 =====

duce carbon dioxide, and this has important consequences for Earth's atmosphere, as we shall discuss in Chapter 37. There are many different types of internal combustion engines, including piston engines (in which pressure is converted into rotating motion using a set of pistons), combustion turbines (in which gas flow is used to spin a turbine's blades), and jet engines (in which a fast moving jet of gas is used to generate thrust).<sup>5</sup>

## 13.6 Heat engines running backwards

In this section we discuss two applications of heat engines in which the engine is run in reverse, putting in work to move heat around.

## Example 13.4

### (a) The refrigerator

The refrigerator is a heat engine that is run backwards so that you put work in and cause a heat flow from a cold reservoir to a hot reservoir (see Fig. 13.9). In this case, the cold reservoir is the food inside the refrigerator that you wish to keep cold and the hot reservoir is usually your kitchen. For a refrigerator, we must define the efficiency in a different way from the efficiency of a heat engine. This is because what you want to achieve is "heat sucked out of the contents of the refrigerator" and what you have to do to achieve it is "electrical work" from the mains electricity supply. Thus we define the efficiency of a refrigerator as

\[\eta = \frac{Q_{\ell}}{W}. \quad (13.20)\]

For a refrigerator fitted with a Carnot engine, it is then easy to show that

\[\eta_{\mathrm{Carnot}} = \frac{T_{\ell}}{T_{\mathrm{h}} - T_{\ell}}, \quad (13.21)\]

which can yield an efficiency above \(100\%\) .

### (b) The heat pump

A heat pump is essentially a refrigerator (Fig. 13.9 applies also for a heat pump), but it is utilized in a different way. It is used to pump heat from a reservoir, to a place where it is desired to add heat. For example, the reservoir could be the soil/rock several metres underground and heat could be pumped out of the reservoir into a house which needs heating. In one cycle of the engine, we want to add heat \(Q_{\mathrm{h}}\) to the house, and now \(W\) is the work we must apply (in the form of electrical work) to accomplish this. The efficiency of a heat pump is therefore defined as

\[\eta = \frac{Q_{\mathrm{h}}}{W}. \quad (13.22)\]

[Image: A schematic diagram of a heat engine running backwards (a refrigerator or heat pump). An input of work W into the engine allows heat Q_l to be taken from a cold reservoir T_l and heat Q_h to be dumped into a hot reservoir T_h.]
Fig. 13.9 A refrigerator or a heat pump. Both devices are heat engines run in reverse (i.e., reversing the arrows on the cycle shown in Fig. 13.3).

===== Page 153 =====

6However, the capital cost means that heat pumps have not become popular until recently.

Note that \(Q_{\mathrm{h}} > W\) and so \(\eta > 1\) . The efficiency is always above \(100\%\) (See Exercise 13.1. ) This shows why heat pumps are attractive for heating. It is always possible to turn work into heat with \(100\%\) efficiency (an electric fire turns electrical work into heat in this way), but a heat pump can allow you to get even more heat into your house for the same electrical work (and hence for the same electricity bill!).

For a heat pump fitted with a Carnot engine, it is easy to show that

\[\eta_{\mathrm{Carnot}} = \frac{T_{\mathrm{h}}}{T_{\mathrm{h}} - T_{\ell}}. \quad (13.23)\]

## 13.7 Clausius' theorem

Consider a Carnot cycle. In one cycle, heat \(Q_{\mathrm{h}}\) enters and heat \(Q_{\ell}\) leaves. Heat is therefore not a conserved quantity of the cycle. However, we found in eqn 13.7 that for a Carnot cycle

\[\frac{Q_{\mathrm{h}}}{Q_{\ell}} = \frac{T_{\mathrm{h}}}{T_{\ell}}, \quad (13.24)\]

7The subscript "rev" on \(\Delta Q_{\mathrm{rev}}\) is there to remind us that we are dealing with a reversible engine.

and so if we define \(\Delta Q_{\mathrm{rev}}\) as the heat entering the system at each point, we have that

\[\sum_{\mathrm{cycle}}\frac{\Delta Q_{\mathrm{rev}}}{T} = \frac{Q_{\mathrm{h}}}{T_{\mathrm{h}}} +\frac{(-Q_{\ell})}{T_{\ell}} = 0, \quad (13.25)\]

and so \(\Delta Q_{\mathrm{rev}} / T\) sums to zero around the cycle. Replacing the sum by an integral, we could write

\[\oint \frac{\mathrm{d}Q_{\mathrm{rev}}}{T} = 0 \quad (13.26)\]

for this Carnot cycle.

Our argument so far has been in terms of a Carnot cycle operating between two distinct heat reservoirs. Real engine cycles can be much more complicated than this in that their "working substance" changes temperature in a much more complicated way and, moreover, real engines do not behave perfectly reversibly. Therefore we would like to generalize our treatment so that it can be applied to a general cycle operating between a whole series of reservoirs and we would like the cycle to be either reversible or irreversible. Our general cycle is illustrated in Fig. 13.10(a). For this cycle, heat \(\mathrm{d}Q_{i}\) enters at a particular part of the cycle. At this point the system is connected to a reservoir, which is at temperature \(T_{i}\) . The total work extracted from the cycle is \(\Delta W\) , given by

\[\Delta W = \sum_{\mathrm{cycle}}\mathrm{d}Q_{i}, \quad (13.27)\]

from the first law of thermodynamics. The sum here is taken around the whole cycle, indicated schematically by the dotted circle in Fig. 13.10(a).

===== Page 154 =====

 (a)  (b)

[Image: (a) A general cycle in the p-V plane. Heat dQ_i enters from a reservoir at T_i. Work Delta W is extracted. (b) The same cycle, but the heat dQ_i is supplied via a Carnot engine C_i operating between a common reservoir at T and the reservoir at T_i.]
Fig. 13.10 (a) A general cycle in which heat \(\mathrm{d}Q_{i}\) enters in part of the cycle from a reservoir at temperature \(T_{i}\) . Work \(\Delta W\) is extracted from each cycle. (b) The same cycle, but showing the heat \(\mathrm{d}Q_{i}\) entering the reservoir at \(T_{i}\) from a reservoir at temperature \(T\) via a Carnot engine (labelled \(C_{i}\) ).

Next we imagine that the heat at each point is supplied via a Carnot engine, which is connected between a reservoir at temperature \(T\) and the reservoir at temperature \(T_{i}\) (see Fig. 13.10(b)). The reservoir at \(T\) is common for all the Carnot engines connected at all points of the cycle. Each Carnot engine produces work \(\mathrm{d}W_{i}\) , and for a Carnot engine we know that

\[\frac{\mathrm{heat~to~reservoir~at~}T_{i}}{T_{i}} = \frac{\mathrm{heat~from~reservoir~at~}T}{T}, \quad (13.28)\]

and hence

\[\frac{\mathrm{d}Q_{i}}{T_{i}} = \frac{\mathrm{d}Q_{i} + \mathrm{d}W_{i}}{T}. \quad (13.29)\]

Rearranging, we have that

\[\mathrm{d}W_{i} = \mathrm{d}Q_{i}\left(\frac{T}{T_{i}} -1\right). \quad (13.30)\]

The thermodynamic system in Fig. 13.10(b) looks at first sight to do nothing other than convert heat to work, which is not allowed according to Kelvin's statement of the second law of thermodynamics, and hence we must insist that this is not the case. Hence

\[\mathrm{total~work~produced~per~cycle} = \Delta W + \sum_{\mathrm{cycle}}\mathrm{d}W_{i}\leq 0. \quad (13.31)\]

===== Page 155 =====

 Using eqns 13.27, 13.30, and 13.31, we therefore have that

\[T\sum_{\mathrm{cycle}}\frac{\mathrm{d}Q_i}{T_i}\leq 0. \quad (13.32)\]

Since \(T > 0\) , we have that

\[\sum_{\mathrm{cycle}}\frac{\mathrm{d}Q_i}{T_i}\leq 0, \quad (13.33)\]

and replacing the sum by an integral, we can write this as

\[\oint \frac{\mathrm{d}Q}{T}\leq 0, \quad (13.34)\]

which is known as the Clausius inequality, embodied in the expression of Clausius' theorem:

Clausius' theorem For any closed cycle, \(\oint \frac{\mathrm{d}Q}{T}\leq 0\) , where equality necessarily holds for a reversible cycle.

[Image: A schematic diagram of a Carnot engine. It takes heat dQ_h from a hot reservoir C_h at T_h, outputs work dW, and rejects heat dQ_l to a cold reservoir C_l at T_l.]
Fig. 13.11 A Carnot engine shown schematically. In diagrams such as this one, the arrows are labelled with the heat and work flowing in one cycle of the engine.

## Example 13.5

Two bodies with temperature- independent heat capacities \(C_h\) and \(C_\ell\) are used as reservoirs for a Carnot heat engine (see Fig. 13.11). Derive an expression for the total work obtainable.

Solution: In an infinitesimal change we have that

\[\begin{array}{rcl}{\mathrm{d}Q_{\mathrm{h}}} & = & {-C_{\mathrm{h}}\mathrm{d}T_{\mathrm{h}}}\\ {\mathrm{d}Q_{\ell}} & = & {C_{\ell}\mathrm{d}T_{\ell},} \end{array} \quad (13.36)\]

and for a Carnot engine we have that

\[\frac{\mathrm{d}Q_{\mathrm{h}}}{T_{\mathrm{h}}} = \frac{\mathrm{d}Q_{\ell}}{T_{\ell}}, \quad (13.37)\]

and integrating gives \(\begin{array}{r}{T_{\ell}^{T_{\ell}}\frac{\mathrm{d}Q_{\ell}}{T_{\ell}} = -\int_{T_{\mathrm{h}}}^{T_{\mathrm{f}}}\frac{\mathrm{d}Q_{\mathrm{h}}}{T_{\mathrm{h}}}} \end{array}\) and hence

\[C_{\ell}\ln \frac{T_{\mathrm{f}}}{T_{\ell}} = -C_{\mathrm{h}}\ln \frac{T_{\mathrm{f}}}{T_{\mathrm{h}}}, \quad (13.38)\]

where \(T_{\mathrm{f}}\) is the final temperature of each reservoir. Thus

\[T_{\mathrm{f}}^{C_{\mathrm{h}} + C_{\ell}} = T_{\mathrm{h}}^{C_{\mathrm{h}}}T_{\ell}^{C_{\ell}}. \quad (13.39)\]

The total heat extracted from each reservoir is \(\Delta Q_{\mathrm{h}} = C_{\mathrm{h}}(T_{\mathrm{h}} - T_{\mathrm{f}})\) and \(\Delta Q_{\ell} = C_{\ell}(T_{\mathrm{f}} - T_{\ell})\) respectively and so the total work is

\[\Delta W = \Delta Q_{\mathrm{h}} - \Delta Q_{\ell} = C_{\mathrm{h}}T_{\mathrm{h}} + C_{\ell}T_{\ell} - (C_{\mathrm{h}} + C_{\ell})T_{\mathrm{f}}. \quad (13.40)\]

===== Page 156 =====

1

## Chapter summary

- No process is possible whose sole result is the transfer of heat from a colder to a hotter body. (Clausius' statement of the second law of thermodynamics)- No process is possible whose sole result is the complete conversion of heat into work. (Kelvin's statement of the second law of thermodynamics)- Of all the heat engines working between two given temperatures, none is more efficient than a Carnot engine. (Carnot's theorem)- All the above are equivalent statements of the second law of thermodynamics.- All reversible engines operating between temperatures \(T_{\mathrm{h}}\) and \(T_{\ell}\) have the efficiency of a Carnot engine: \(\eta_{\mathrm{Carnot}} = (T_{\mathrm{h}} - T_{\ell}) / T_{\mathrm{h}}\) .- For a Carnot engine:

\[\frac{Q_{\mathrm{h}}}{Q_{\ell}} = \frac{T_{\mathrm{h}}}{T_{\ell}}.\]

Clausius' theorem states that for any closed cycle, \(\oint \frac{\mathrm{d}Q}{T} \leq 0\) where equality necessarily holds for a reversible cycle.

## Further reading

An entertaining account of how steam engines really work may be found in Semmens and Goldfinch (2000). A short account of Watt's development of his engine is in Marsden (2002).

## Exercises

(13.1) A heat pump has an efficiency greater than \(100\%\) Does this violate the laws of thermodynamics? (13.2) What is the maximum possible efficiency of an engine operating between two thermal reservoirs, one at \(100^{\circ}\mathrm{C}\) and the other at \(0^{\circ}\mathrm{C}\) ? (13.3) The history of science is littered with various schemes for producing perpetual motion. A machine that does this is sometimes referred to as a perpetuum mobile, which is the Latin term for a perpetual motion machine.

A perpetual motion machine of the first kind produces more energy than it uses. A perpetual motion machine of the second kind produces exactly the same amount of energy as it uses, but it continues running forever indefinitely by converting all its waste heat back into mechanical work.

Give a critique of these two types of machine and state which laws of thermodynamics they each break, if any.

===== Page 157 =====

13.4) A possible ideal-gas cycle operates as follows: (i) from an initial state \((p_1,V_1)\) the gas is cooled at constant pressure to \((p_1,V_2)\) (ii) the gas is heated at constant volume to \((p_2,V_2)\) (iii) the gas expands adiabatically back to \((p_1,V_1)\) Assuming constant heat capacities, show that the thermal efficiency is

\[1 - \gamma \frac{(V_1 / V_2) - 1}{(p_2 / p_1) - 1}. \quad (13.41)\]

(You may quote the fact that in an adiabatic change of an ideal gas, \(pV^{\gamma}\) stays constant, where \(\gamma = c_p / c_V\) .)

[Image: A p-V diagram for the Otto cycle. It consists of two isochores (constant volume) and two adiabats. The cycle is 1->2 (isochore), 2->3 (adiabat), 3->4 (isochore), 4->1 (adiabat).]
Fig.13.12 The Otto cycle. (An isochore is a line of constant volume.)

(13.5) Show that the efficiency of the standard Otto cycle (shown in Fig.13.12) is \(1 - r^{1 - \gamma}\) , where \(r = V_1 / V_2\) is the compression ratio. The Otto cycle is the four-stroke cycle in internal combustion engines in cars, lorries, and electrical generators.

(13.6) An ideal air conditioner operating on a Carnot cycle absorbs heat \(Q_2\) from a house at temperature \(T_2\) and discharges \(Q_1\) to the outside at temperature \(T_1\) , consuming electrical energy \(E\) . Heat leakage into the house follows Newton's law,

\[Q = A[T_1 - T_2], \quad (13.42)\]

where \(A\) is a constant. Derive an expression for \(T_2\) in terms of \(T_1\) , \(E\) , and \(A\) for continuous operation when the steady state has been reached.

The air conditioner is controlled by a thermostat. The system is designed so that with the thermostat set at \(20^{\circ}C\) and outside temperature \(30^{\circ}C\) the system operates at \(30\%\) of the maximum electrical energy input. Find the highest outside temperature for which the house may be maintained inside at \(20^{\circ}C\) .

(13.7) Two identical bodies of constant heat capacity \(C_p\) at temperatures \(T_1\) and \(T_2\) respectively are used as reservoirs for a heat engine. If the bodies remain at constant pressure, show that the amount of work obtainable is

\[W = C_p(T_1 + T_2 - 2T_i), \quad (13.43)\]

where \(T_i\) is the final temperature attained by both bodies. Show that if the most efficient engine is used, then \(T_i^2 = T_1T_2\) .

(13.8) A building is maintained at a temperature \(T\) by means of an ideal heat pump, which uses a river at temperature \(T_0\) as a source of heat. The heat pump consumes power \(W\) , and the building loses heat to its surroundings at a rate \(\alpha (T - T_0)\) , where \(\alpha\) is a positive constant. Show that \(T\) is given by

\[T = T_0 + \frac{W}{2\alpha}\left(1 + \sqrt{1 + 4\alpha T_0 / W}\right). \quad (13.44)\]

(13.9) Three identical bodies of constant thermal capacity are at temperatures \(300\mathrm{K}\) , \(300\mathrm{K}\) , and \(100\mathrm{K}\) . If no work or heat is supplied from outside, what is the highest temperature to which any one of these bodies can be raised by the operation of heat engines? If you set this problem up correctly you may have to solve a cubic equation. This looks hard to solve but in fact you can deduce one of the roots [Hint: what is the highest temperature of the bodies if you do nothing to connect them?].

(13.10) In a heat engine, heat can diffuse between the hot reservoir and the cold reservoir and in Chapter 10 we showed that this takes place on a timescale which scales with the square of the linear size of the system (see Example 10.4). The mechanical timescale of an engine typically scales simply with the linear size of the engine. Explain why this means that heat engines don't work on very small scales. [This is one why reason why the "engines" powering biological systems, which have to be extremely small, are not heat engines. Instead, useful energy is extracted directly from chemical bonds. Heat engines also often run on chemical fuel but use the fuel to heat one of the reservoirs and then extract work from the temperature difference thereby generated.]

===== Page 158 =====

1

Sadi Carnot's father, Lazare Carnot (1753- 1823), was an engineer and mathematician who founded the École Polytechnique in Paris, was briefly Napoleon Bonaparte's minister of war and served as his military governor of Antwerp. After Napoleon's defeat, Lazare Carnot was forced into exile. He fled to Warsaw in 1815 and then moved to Magdeburg in Germany in 1816.

[Image: A portrait of Sadi Carnot as a young man in military uniform.]
Fig.13.13 Sadi Carnot

It was there in 1818 that he saw a steam engine, and both he and his son Sadi Carnot, who visited him there in 1821, became hooked on the problem of understanding how it worked.

Sadi Carnot had been educated as a child by his father. In 1812 he entered the École Polytechnique and studied with Poisson and Ampere. He then moved to Metz and studied military engineering,

worked for a while as a military engineer, and then moved back to Paris in 1819. There he became interested in a variety of industrial problems as well as the theory of gases. He had now become skilled in tackling various problems, but it was his visit to Magdeburg that proved crucial in bringing him the problem that was to be his life's most important work. In this, his father's influence was a significant factor in the solution to the problem. Lazare Carnot had been obsessed by the operation of machines all his life and had been particularly interested in thinking about the operation of water wheels. In a water wheel, falling water can be made to produce useful mechanical work. The water falls from a reservoir of high potential energy to a reservoir of low potential energy, and on the way down, the water turns a wheel which then drives some useful machine such as a flour mill. Lazare Carnot had thought a great deal about how you could make such systems as efficient as possible and convert as much of the potential energy of the water as possible into useful work.

the water as possible into useful work.

Sadi Carnot was struck by the analogy between such a water wheel and a steam engine, in which heat (rather than water) flows from a reservoir at high temperature to a reservoir at low temperature. Carnot's genius was that rather than focus on the details of the steam engine he decided to consider an engine in abstracted form, focusing purely on the flow of heat between two thermal reservoirs. He idealized the workings of an engine as consisting of simple gas cycles (in what we now know as a Carnot cycle) and worked out its efficiency. He realized that to be as efficient as possible, the engine had to pass slowly through a series of equilibrium states and that it therefore had to be reversible. At any stage, you could reverse its operation and send it the other way around the cycle. He was then able to use this fact to prove that all reversible heat engines operating between two temperatures had the same efficiency.

This work was summarized in his paper on the subject, Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance (Reflections on the motive power of fire and machines fitted to develop that power), which was published in 1824. Carnot's paper was favourably reviewed, but had little immediate impact. Few could see the relevance of his work, or at least see past the abstract argument and the unfamiliar notions of idealized engine cycles; his introduction, in which he praised the technical superiority of English engine designers, may not have helped win his French audience. Carnot died in 1832 during a cholera epidemic, and most of his papers were destroyed (the standard precaution following a cholera fatality). The French physicist Émile Clapeyron later noticed his work and published his own paper on it in 1834. However, it was yet another decade before the work simultaneously came to the notice of a young German student, Rudolf Clausius, and a recent graduate of Cambridge University, William Thomson (later Lord Kelvin), who would each individually make much of Carnot's ideas. In particular, Clausius patched up and modernized Carnot's arguments (which had assumed the validity of the prevailing, but subsequently discredited, caloric theory of heat) and was motivated by Carnot's ideas to introduce the concept of entropy.

===== Page 159 =====

14 Entropy

14.1 Definition of entropy 140 14.2 Irreversible change 140 14.3 The first law revisited 142 14.4 The Joule expansion 144 14.5 The statistical basis for entropy 146 14.6 The entropy of mixing 147 14.7 Maxwell's demon 149 14.8 Entropy and probability 150 Chapter summary 153 Exercises 153

In this chapter we will use the results from Chapter 13 to define a quantity called entropy and to understand how entropy changes in reversible and irreversible processes. We will also consider the statistical basis for entropy, and use this to understand the entropy of mixing, the apparent conundrum of Maxwell's demon and the connection between entropy and probability.

## 14.1 Definition of entropy

In this section, we introduce a thermodynamic definition of entropy. We begin by recalling from eqn 13.26 that \(\oint \mathrm{d}Q_{\mathrm{rev}} / T = 0\) . This means that the integral

\[\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}\]

is path independent (see Appendix C.7). Therefore the quantity \(\mathrm{d}Q_{\mathrm{rev}} / T\) is an exact differential and we can write down a new state function which we call entropy. We therefore define the entropy \(S\) by

\[\mathrm{d}S = \frac{\mathrm{d}Q_{\mathrm{rev}}}{T}, \quad (14.1)\]

so that

\[S(\mathrm{B}) - S(\mathrm{A}) = \int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}, \quad (14.2)\]

and \(S\) is a function of state. For an adiabatic process (a reversible adiathermal process) we have that

\[\mathrm{d}Q_{\mathrm{rev}} = 0. \quad (14.3)\]

Hence an adiabatic process involves no change in entropy (the process is also called isentropic).

## 14.2 Irreversible change

Entropy \(S\) is defined in terms of reversible changes of heat. Since \(S\) is a state function, then the integral of \(S\) around a closed loop is zero, so that

\[\oint \frac{\mathrm{d}Q_{\mathrm{rev}}}{T} = 0. \quad (14.4)\]

===== Page 160 =====

 Let us now consider a loop which contains an irreversible section (A→B) and a reversible section (B→A), as shown in Fig. 14.1. The Clausius inequality (eqn 13.34) implies that, integrating around this loop, we have that

\[\oint \frac{\mathrm{d}Q}{T}\leq 0. \quad (14.5)\]

Writing out the left- hand side in detail, we have that

\[\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q}{T} +\int_{\mathrm{B}}^{\mathrm{A}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}\leq 0, \quad (14.6)\]

and hence rearranging gives

\[\int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q}{T}\leq \int_{\mathrm{A}}^{\mathrm{B}}\frac{\mathrm{d}Q_{\mathrm{rev}}}{T}. \quad (14.7)\]

This is true however close A and B get to each other, so in general we can write that the change in entropy \(\mathrm{d}S\) is given by

\[\mathrm{d}S = \frac{\mathrm{d}Q_{\mathrm{rev}}}{T}\geq \frac{\mathrm{d}Q}{T}. \quad (14.8)\]

The equality in this expression is only obtained (somewhat trivially) if the process on the right- hand side is actually reversible. Note that because \(S\) is a state function, the entropy change in going from A to B is independent of the route.

Consider a thermally isolated system. In such a system \(\mathrm{d}Q = 0\) for any process, so that the above inequality becomes

\[\mathrm{d}S\geq 0. \quad (14.9)\]

This is a very important equation and is, in fact, another statement of the second law of thermodynamics. It shows that any change for this thermally isolated system always results in the entropy either staying the same (for a reversible change) or increasing (for an irreversible change). This gives us yet another statement of the second law, namely that: "the entropy of an isolated system tends to a maximum." We can tentatively apply these ideas to the Universe as a whole, under the assumption that the Universe itself is a thermally isolated system:

## Application to the Universe

Assuming that the Universe can be treated as an isolated system, the first two laws of thermodynamics become:

(1) \(U_{\mathrm{Universe}} =\) constant.
(2) \(S_{\mathrm{Universe}}\) can only increase.

The following example illustrates how the entropy of a particular system and a reservoir, as well as that of the Universe (taken to be the system plus reservoir), changes in an irreversible process.

[Image: A p-V diagram showing an irreversible path A->B and a reversible path B->A between two points A and B.]
Fig. 14.1 An irreversible and a reversible change between two points A and B in \(p - V\) parameter space.

===== Page 161 =====

142 Entropy

[Image: A graph of entropy change versus the ratio T_system / T_reservoir. The graph shows Delta S_system, Delta S_reservoir, and Delta S_Universe. Delta S_Universe is always positive or zero.]
Fig. 14.2 The entropy change in the simple process in which a small system is placed in contact with a large reservoir.

## Example 14.1

A large reservoir at temperature \(T_{\mathrm{R}}\) is placed in thermal contact with a small system at temperature \(T_{\mathrm{S}}\) . They both end up at the temperature of the reservoir, \(T_{\mathrm{R}}\) . The heat transferred from the reservoir to the system is \(\Delta Q = C(T_{\mathrm{R}} - T_{\mathrm{S}})\) , where \(C\) is the heat capacity of the system.

If \(T_{\mathrm{R}} > T_{\mathrm{S}}\) , heat is transferred from reservoir to system, the system warms and its entropy increases; the entropy of the reservoir decreases, because heat flows out of it. If \(T_{\mathrm{R}}< T_{\mathrm{S}}\) , heat is transferred from system to reservoir, the system cools and its entropy decreases; the entropy of the reservoir increases, because heat flows into it.

Let us calculate these entropy changes in detail: The entropy change in the reservoir, which has constant temperature \(T_{\mathrm{R}}\) , is

\[\Delta S_{\mathrm{reservoir}} = \int \frac{\mathrm{d}Q}{T_{\mathrm{R}}} = \frac{1}{T_{\mathrm{R}}}\int \mathrm{d}Q = \frac{\Delta Q}{T_{\mathrm{R}}} = \frac{C(T_{\mathrm{S}} - T_{\mathrm{R}})}{T_{\mathrm{R}}}, \quad (14.10)\]

while the entropy change in the system is

\[\Delta S_{\mathrm{system}} = \int \frac{\mathrm{d}Q}{T} = \int_{T_{\mathrm{S}}}^{T_{\mathrm{R}}}\frac{C\mathrm{d}T}{T} = C\ln \frac{T_{\mathrm{R}}}{T_{\mathrm{S}}}. \quad (14.11)\]

Hence, the total entropy change in the Universe is

\[\Delta S_{\mathrm{Universe}} = \Delta S_{\mathrm{system}} + \Delta S_{\mathrm{reservoir}} = C\left[\ln \frac{T_{\mathrm{R}}}{T_{\mathrm{S}}} +\frac{T_{\mathrm{S}}}{T_{\mathrm{R}}} -1\right]. \quad (14.12)\]

These expressions are plotted in Fig. 14.2 and demonstrate that even though \(\Delta S_{\mathrm{reservoir}}\) and \(\Delta S_{\mathrm{system}}\) can each be positive or negative, we always have that

\[\Delta S_{\mathrm{Universe}}\geq 0. \quad (14.13)\]

## 14.3 The first law revisited

Using our new notion of entropy, it is possible to obtain a much more elegant and useful statement of the first law of thermodynamics. We recall from eqn 11.7 that the first law is given by

\[\mathrm{d}U = \mathrm{d}Q + \mathrm{d}W. \quad (14.14)\]

Now, for a reversible change only, we have that

\[\mathrm{d}Q = T\mathrm{d}S \quad (14.15)\]

===== Page 162 =====

14.3 The first law revisited 143

and

\[\mathrm{d}W = -pdV. \quad (14.16)\]

Combining these, we find that

\[\mathrm{d}U = T\mathrm{d}S - pdV. \quad (14.17)\]

Constructing this equation, we stress, has assumed that the change is reversible. However, since all the quantities in eqn 14.17 are functions of state, and are therefore path independent, this equation holds for irreversible processes as well! For an irreversible change, \(\mathrm{d}Q \leq T \mathrm{~d}S\) and also \(\mathrm{d}W \geq - p \mathrm{~d}V\) , but with \(\mathrm{d}Q\) being smaller than for the reversible case and \(\mathrm{d}W\) being larger than for the reversible case so that \(\mathrm{d}U\) is the same whether the change is reversible or irreversible.

Therefore, we always have that:

\[\mathrm{d}U = T\mathrm{d}S - pdV. \quad (14.18)\]

This equation implies that the internal energy \(U\) changes when either \(S\) or \(V\) changes. Thus, the function \(U\) can be written in terms of the variables \(S\) and \(V\) , which are its so- called natural variables. These variables are both extensive (i.e., they scale with the size of the system).<sup>2</sup> The variables \(p\) and \(T\) are both intensive (i.e., they do not scale with the size of the system) and behave a bit like forces, since they show how the internal energy changes with respect to some parameter. In fact, since mathematically we can write \(\mathrm{d}U\) as

\[\mathrm{d}U = \left(\frac{\partial U}{\partial S}\right)_V\mathrm{d}S + \left(\frac{\partial U}{\partial V}\right)_S\mathrm{d}V, \quad (14.19)\]

we can make the identification of \(T\) and \(p\) using

\[\begin{array}{rcl}{T}&{=}&{\left(\frac{\partial U}{\partial S}\right)_V\mathrm{and}}\\ {p}&{=}&{-\left(\frac{\partial U}{\partial V}\right)_S.}\end{array} \quad (14.21)\]

The ratio of \(p\) and \(T\) can also be written in terms of the variables \(U\) , \(S\) and \(V\) , as follows:

\[\frac{p}{T} = -\left(\frac{\partial U}{\partial V}\right)_S\left(\frac{\partial S}{\partial U}\right)_V, \quad (14.22)\]

using the reciprocal theorem (see eqn C.41). Hence

\[\frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_U, \quad (14.23)\]

using the reciprocity theorem (see eqn C.42). These equations are used in the following example.

===== Page 163 =====

144 Entropy

[Image: Two systems, 1 and 2, connected by a pipe. An arrow shows that internal energy Delta U and volume Delta V can be transferred between them.]
Fig. 14.3 Two systems, 1 and 2, which are able to exchange volume and internal energy.

## Example 14.2

Consider two systems, with pressures \(p_1\) and \(p_2\) and temperatures \(T_1\) and \(T_2\) . If internal energy \(\Delta U\) is transferred from system 1 to system 2, and volume \(\Delta V\) is transferred from system 1 to system 2 (see Fig. 14.3), find the change of entropy. Show that equilibrium results when \(T_1 = T_2\) and \(p_1 = p_2\) .

Solution:

Equation 14.18 can be rewritten as

\[\mathrm{d}S = \frac{1}{T}\mathrm{d}U + \frac{p}{T}\mathrm{d}V. \quad (14.24)\]

If we now apply this to our problem, the change in entropy is then straightforwardly

\[\Delta S = \left(\frac{1}{T_1} -\frac{1}{T_2}\right)\Delta U + \left(\frac{p_1}{T_1} -\frac{p_2}{T_2}\right)\Delta V. \quad (14.25)\]

Equation 14.9 shows that the entropy always increases in any physical process. Thus, when equilibrium is achieved, the entropy will have achieved a maximum, so that \(\Delta S = 0\) . This means that the joint system cannot increase its entropy by further exchanging volume or internal energy between system 1 and system 2. \(\Delta S = 0\) can only be achieved when \(T_1 = T_2\) and \(p_1 = p_2\) .

Eqn 14.18 is an important equation that will be used a great deal in subsequent chapters. Before proceeding, we pause to summarize the most important equations in this section and state their applicability.


<table>SummarydU = dQ + dWalways truedQ = T dSonly true for reversible changesdW = -p dVonly true for reversible changesdU = T dS - p dValways trueFor irreversible changes:dQ ≤ T dS, dW ≥ -p dV</table>

## 14.4 The Joule expansion

In this section, we describe in detail an irreversible process known as the Joule expansion (see Fig. 14.4). One mole of ideal gas (pressure \(p_1\) , temperature \(T_1\) ) is confined to the left- hand side of a thermally isolated container and occupies a volume \(V_0\) . The right- hand side of the container (also volume \(V_0\) ) is evacuated. The tap between the two parts of the container is then suddenly opened and the gas fills the entire container of volume \(2V_0\) (and has new temperature \(T_{\mathrm{f}}\) and pressure \(p_{\mathrm{f}}\) ). Both

===== Page 164 =====

 containers are assumed to be thermally isolated from their surroundings. For the initial state, the ideal gas law implies that

\[p_{\mathrm{I}}V_{0} = RT_{\mathrm{I}}, \quad (14.26)\]

and for the final state that

\[p_{\mathrm{f}}(2V_{0}) = RT_{\mathrm{f}}. \quad (14.27)\]

Since the system is thermally isolated from its surroundings, \(\Delta U = 0\) Also, since \(U\) is only a function of \(T\) for an ideal gas, \(\Delta T = 0\) and hence \(T_{\mathrm{i}} = T_{\mathrm{f}}\) .This implies that \(p_{\mathrm{i}}V_{0} = p_{\mathrm{f}}(2V_{0})\) , so that the pressure halves, i.e.,

\[p_{\mathrm{f}} = \frac{p_{\mathrm{i}}}{2}. \quad (14.28)\]

It is hard to calculate directly the change of entropy of a gas in a Joule expansion along the route that it takes from its initial state to the final state. The pressure and volume of the system are undefined during the process immediately after the partition is removed since the gas is in a non- equilibrium state. However, entropy is a function of state and therefore for the purposes of the calculation, we can take another route from the initial state to the final state since changes of functions of state are independent of the route taken. Let us calculate the change in entropy for a reversible isothermal expansion of the gas from volume \(V_{0}\) to volume \(2V_{0}\) (as indicated in Fig. 14.5). Since the internal energy is constant in the isothermal expansion of an ideal gas, \(\mathrm{d}U = 0\) , and hence the new form of the first law in eqn 14.18 gives us \(T\mathrm{d}S = p\mathrm{d}V\) , so that

\[\Delta S = \int_{\mathrm{i}}^{\mathrm{f}}\mathrm{d}S = \int_{V_{0}}^{2V_{0}}\frac{p\mathrm{d}V}{T} = \int_{V_{0}}^{2V_{0}}\frac{R\mathrm{d}V}{V} = R\ln 2. \quad (14.29)\]

Since \(S\) is a function of state, this increase in entropy \(R\ln 2\) is also the change of entropy for the Joule expansion.

## Example 14.3

What is the change of entropy in the gas, surroundings, and Universe during a Joule expansion?

Solution:

Above, we have worked out \(\Delta S_{\mathrm{gas}}\) for the reversible isothermal expansion and the Joule expansion: they have to be the same. What about the surroundings and the Universe in each case?

For the reversible isothermal expansion of the gas, we deduce the change of entropy in the surroundings so that the entropy in the Universe does not increase (because we are dealing with a reversible situation).

\[\begin{array}{rcl}{\Delta S_{\mathrm{gas}}} & = & {R\ln 2,}\\ {\Delta S_{\mathrm{surroundings}}} & = & {-R\ln 2,}\\ {\Delta S_{\mathrm{Universe}}} & = & {\Delta S_{\mathrm{gas}} + \Delta S_{\mathrm{surroundings}} = 0.} \end{array} \quad (14.30)\]

[Image: (a) A container divided into two equal parts by a tap. The left part contains a gas at pressure p_i and volume V_0. The right part is evacuated. (b) After the tap is opened, the gas fills both parts, at a new pressure p_f and volume 2V_0.]
Fig. 14.4 The Joule expansion between volume \(V_{0}\) and volume \(2V_{0}\) . One mole of ideal gas (pressure \(p_{\mathrm{i}}\) , temperature \(T_{\mathrm{i}}\) ) is confined to the left-hand side of a container in a volume \(V_{0}\) . The container is thermally isolated from its surroundings. The tap between the two parts of the container is then suddenly opened and the gas fills the entire container of volume \(2V_{0}\) (and has new temperature \(T_{\mathrm{f}}\) and pressure \(p_{\mathrm{f}}\) ).

[Image: A p-V diagram showing the Joule expansion between volumes V_0 and 2V_0. The path is undefined (dotted). A reversible isothermal expansion path between the same volumes is also shown (solid curve).]
Fig. 14.5 The Joule expansion between volume \(V_{0}\) and volume \(2V_{0}\) and a reversible isothermal expansion of a gas between the same volumes. The path in the \(p - V\) plane for the Joule expansion is undefined, whereas it is well defined for the reversible isothermal expansion. In each case however, the start and end points are well defined. Since entropy is a function of state, the change in entropy for the two processes is the same, regardless of route.

===== Page 165 =====

3In other words, the method involving the least work.

Notice that the entropy of the surroundings goes down. This does not contradict the second law of thermodynamics. The entropy of something can decrease if that something is not isolated. Here the surroundings are not isolated because they are able to exchange heat with the system.

For the Joule expansion, the system is thermally isolated so that the entropy of the surroundings does not change. Hence

\[\begin{array}{rcl}{\Delta S_{\mathrm{gas}}} & = & {R\ln 2,}\\ {\Delta S_{\mathrm{surroundings}}} & = & {0,}\\ {\Delta S_{\mathrm{Universe}}} & = & {\Delta S_{\mathrm{gas}} + \Delta S_{\mathrm{surroundings}} = R\ln 2.} \end{array} \quad (14.31)\]

Once the Joule expansion has occurred, you can only put the gas back in the left- hand side by compressing it. The best3 you can do is to do this reversibly, by a reversible isothermal compression, which takes work \(\Delta W\) given (for 1 mole of gas) by

\[\Delta W = -\int_{2V_0}^{V_0}p\mathrm{d}V = -\int_{2V_0}^{V_0}\frac{RT}{V}\mathrm{d}V = RT\ln 2 = T\Delta S_{\mathrm{gas}}. \quad (14.32)\]

The increase of entropy in a Joule expansion is thus \(\Delta W / T\) .

## A paradox?

In the Joule expansion, the system is thermally isolated so no heat can be exchanged: \(\Delta Q = 0\) . Now work is done: \(\Delta W = 0\) . Hence \(\Delta U = 0\) (so for an ideal gas, \(\Delta T = 0\) ). But if \(\Delta Q = 0\) , doesn't that imply that \(\Delta S = \Delta Q / T = 0\) ?

The above reasoning is correct, until the very end: the answer to the question in the last point is NO! The equation \(\mathrm{d}Q = T\mathrm{d}S\) is only true for reversible changes. In general \(\mathrm{d}Q\leq T\mathrm{d}S\) , and here we have \(\Delta Q = 0\) and \(\Delta S = R\ln 2\) , so we have that \(\Delta Q\leq T\Delta S\) .

## 14.5 The statistical basis for entropy

We now want to show that in addition to defining entropy via thermodynamics, i.e., using \(\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}} / T\) , it is also possible to define entropy via statistics. We will motivate this as follows:

As we showed in eqn 14.20, the first law \(\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V\) implies that

\[T = \left(\frac{\partial U}{\partial S}\right)_V, \quad (14.33)\]

===== Page 166 =====

14.6 The entropy of mixing 147

or equivalently

\[\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_V. \quad (14.34)\]

Now, recall from eqn 4.7 that

\[\frac{1}{k_{\mathrm{B}}T} = \frac{\mathrm{d}\ln\Omega}{\mathrm{d}E}. \quad (14.35)\]

Comparing these last two equations motivates the identification of \(S\) with \(k_{\mathrm{B}}\ln \Omega\) , i.e.,

\[S = k_{\mathrm{B}}\ln \Omega. \quad (14.36)\]

This is the expression for the entropy of a system that is in a particular macrostate in terms of \(\Omega\) , the number of microstates associated with that macrostate. We are assuming that the system is in a particular macrostate with fixed energy, and this situation is known as the microcanonical ensemble (see Section 4.5). Later in this chapter (see Section 14.8), and also later in the book, we will generalize this result to express the entropy for more complicated situations. Nevertheless, this expression is sufficiently important that it was inscribed on Boltzmann's tombstone, although on the tombstone the symbol \(\Omega\) is written as a "W". In the following example, we will apply this expression to understanding the Joule expansion, which we introduced in Section 14.4.

See page 31.

## Example 14.4

## Joule expansion

Following a Joule expansion, each molecule can be either on the left- hand side or the right- hand side of the container. For each molecule there are therefore two ways of placing it. For one mole \((N_{\mathrm{A}}\) molecules) there are \(2^{N_{\mathrm{A}}}\) ways of placing them. The number of microstates associated with the gas being in a container twice as big as the initial volume is larger by a multiplicative factor

\[2^{N_{\mathrm{A}}}, \quad (14.37)\]

so that the additional entropy is

\[\Delta S = k_{\mathrm{B}}\ln 2^{N_{\mathrm{A}}} = k_{\mathrm{B}}N_{\mathrm{A}}\ln 2 = R\ln 2, \quad (14.38)\]

which is the same expression as written in eqn 14.29.

## 14.6 The entropy of mixing

Consider two different ideal gases (call them 1 and 2) which are in separate vessels with volumes \(xV\) and \((1 - x)V\) respectively at the same pressures \(p\) and temperatures \(T\) (see Fig. 14.6). Since the pressures and

===== Page 167 =====

[Image: Two vessels connected by a pipe with a closed tap. The left vessel contains gas 1 of volume xV. The right vessel contains gas 2 of volume (1-x)V. Both are at pressure p and temperature T.]
Fig. 14.6 Gas 1 is confined in a vessel of volume \(xV\) , while gas 2 is confined in a vessel of volume \((1 - x)V\) . Both gases are at pressure \(p\) and temperature \(T\) . Mixing occurs once the tap on the pipe connecting the two vessels is opened.

[Image: A graph of the entropy of mixing Delta S / N k_B versus x. The curve is symmetric, starting at 0 for x=0, rising to a maximum of ln 2 at x=0.5, and returning to 0 at x=1.]
Fig. 14.7 The entropy of mixing according to eqn 14.40.

temperatures are the same on each side, and since \(p = (N / V)k_{\mathrm{B}}T\) , the number of molecules of gas 1 is \(xN\) and of gas 2 is \((1 - x)N\) , where \(N\) is the total number of molecules.

If the tap on the pipe connecting the two vessels is opened, the gases will spontaneously mix, resulting in an increase in entropy, known as the entropy of mixing. As for the Joule expansion, we can imagine going from the starting state (gas 1 in the first vessel, gas 2 in the second vessel) to the final state (a homogeneous mixture of gas 1 and gas 2 distributed throughout both vessels) via a reversible route, so that we imagine a reversible expansion of gas 1 from \(xV\) into the combined volume \(V\) and a reversible expansion of gas 2 from \((1 - x)V\) into the combined volume \(V\) . For an isothermal expansion of an ideal gas, the internal energy doesn't change and hence \(T\mathrm{d}S = p\mathrm{d}V\) so that \(\mathrm{d}S = (p / T)\mathrm{d}V = Nk_{\mathrm{B}}\mathrm{d}V / V\) using the ideal gas law. This means that the entropy of mixing for our problem is

\[\Delta S = xNk_{\mathrm{B}}\int_{xV}^{V}\frac{\mathrm{d}V_{1}}{V_{1}} +(1 - x)Nk_{\mathrm{B}}\int_{(1 - x)V}^{V}\frac{\mathrm{d}V_{2}}{V_{2}} \quad (14.39)\]

and hence

\[\Delta S = -Nk_{\mathrm{B}}(x\ln x + (1 - x)\ln (1 - x)). \quad (14.40)\]

This equation is plotted in Fig. 14.7. As expected, there is no entropy increase when \(x = 0\) or \(x = 1\) . The maximum entropy change occurs when \(x = \frac{1}{2}\) , in which case \(\Delta S = Nk_{\mathrm{B}}\ln 2\) . This of course corresponds to the equilibrium state in which no further increase of entropy is possible.

This expression for \(x = \frac{1}{2}\) also admits to a very simple statistical interpretation. Before the mixing of the gases takes place, we know that gas 1 is only in the first vessel and gas 2 is only in the second vessel. After mixing, each molecule can exist in additional "microstates"; for every microstate with a molecule of gas 1 on the left there is now an additional one with a molecule of gas 1 now on the right. Therefore \(\Omega\) must be multiplied by \(2^{N}\) and hence \(S\) must increase by \(k_{\mathrm{B}}\ln 2^{N}\) , which is \(Nk_{\mathrm{B}}\ln 2\) .

This treatment has a profound consequence: distinguishability is an important concept! We have assumed that there is some tangible difference between gas 1 and gas 2, so that there is some way to label whether a particular molecule is gas 1 or gas 2. For example, if the two gases were nitrogen and oxygen, one could measure the mass of the molecules to determine which was which. But what if the two gases were actually the same? Physically, we would expect that mixing them would have no observable consequences, so there should be no increase in entropy. Thus mixing should only increase entropy if the gases really are distinguishable. We will return to this issue of distinguishability in Chapter 29.

===== Page 168 =====

14.7 Maxwell's demon

In 1867, James Clerk Maxwell came up with an intriguing puzzle via a thought experiment. This has turned out to be much more illuminating and hard to solve than he might ever have imagined. The thought experiment can be stated as follows: imagine performing a Joule expansion on a gas. A gas is initially in one chamber, which is connected via a closed tap to a second chamber containing only a vacuum (see Fig. 14.4). The tap is opened and the gas in the first chamber expands to fill both chambers. Equilibrium is established and the pressure in each chamber is now half of what it was in the first chamber at the start. The Joule expansion is formally irreversible as there is no way to get the gas back into the initial chamber without doing work. Or is there? Maxwell imagined that the tap was operated by a microscopic intelligent creature, now called Maxwell's demon, who was able to watch the individual molecules bouncing around close to the tap (see Fig. 14.8). If the demon sees a gas molecule heading from the second chamber back into the first, it quickly opens the tap and then shuts it straight away, just letting the molecule through. If it spots a gas molecule heading from the first chamber back into the second chamber, it keeps the tap closed. The demon does no work and yet it can make sure that the gas molecules in the second chamber all go back into the first chamber. Thus it creates a pressure difference between the two chambers where none existed before the demon started its mischief.

[Image: A sketch of Maxwell's demon. A box is divided into two chambers A and B by a wall with a small trap door. A small demon-like creature sits by the trap door, holding a string to open and close it. Molecules are shown moving in both chambers.]
Fig. 14.8 Maxwell's demon watches the gas molecules in chambers A and B and intelligently opens and shuts the trap door connecting the chambers. The demon is therefore able to reverse the Joule expansion and only let molecules travel from B to A, thus apparently contravening the second law of thermodynamics.

===== Page 169 =====

 Now, a similar demon could be employed to make hot molecules go the wrong way (i.e., so that heat flows the wrong way, from cold to hot - this in fact was Maxwell's original implementation of the demon), or even to sort out molecules of different types (and thus subvert the "entropy of mixing", see Section 14.6). It looks as if the demon could therefore cause entropy to decrease in a system with no consequent increase in entropy anywhere else. In short, Maxwell's demon appears to make a mockery out of the second law of thermodynamics. How on earth does it get away with it?

Many very good minds have addressed this problem. One early idea was that the demon needs to make measurements of where all the gas molecules are, and to do this would need to shine light on the molecules; thus the process of observation of the molecules might be thought to rescue us from Maxwell's demon. However, this idea turned out not to be correct as it was found to be possible, even in principle, to detect a molecule with arbitrarily little work and dissipation. Remarkably, it turns out that because a demon needs to have a memory to operate (so that it can remember where it has observed a molecule and any other results of its measurement process), this act of storing information (actually it is the act of erasing information, as we will discuss below) is associated with an increase of entropy, and this increase cancels out any decrease in entropy that the demon might be able to effect in the system. This connection between information and entropy is an extremely important insight and will be explored in Chapter 15.

The demon is in fact a type of computational device that processes and stores information about the world. It is possible to design a computational process that proceeds entirely reversibly, and therefore has no increase in entropy associated with it. However, the act of erasing information is irreversible (as anyone who has ever failed to backup their data and then had their computer crash will testify). Erasing information always has an associated increase in entropy (of \(k_{\mathrm{B}}\ln 2\) per bit, as we shall see in Chapter 15); Maxwell's demon can operate reversibly therefore, but only if it has a large enough hard disc that it doesn't ever need to clear space to continue operating. The Maxwell demon therefore beautifully illustrates the connection between entropy and information.

## 14.8 Entropy and probability

The entropy that you measure is due to the number of different states in which the system can exist, according to \(S = k_{\mathrm{B}}\ln \Omega\) (eqn 14.36). However, each state may consist of a large number of microstates that we can't directly measure. Since the system could exist in any one of those microstates, there is extra entropy associated with them. An example should make this idea clear.

===== Page 170 =====

14.8 Entropy and probability 151

## Example 14.5

A system has five possible equally likely states in which it can exist, and which of those states it occupies can be distinguished by some easy physical measurement. The entropy is therefore, using eqn 14.36,

\[S = k_{\mathrm{B}}\ln 5. \quad (14.41)\]

However, each of those five states is made up of three equally likely microstates and it is not possible to measure easily which of those microstates it is in. The extra entropy associated with these microstates is \(S_{\mathrm{micro}} = k_{\mathrm{B}}\ln 3\) . The system therefore really has \(3\times 5 = 15\) states and the total entropy is therefore \(S_{\mathrm{tot}} = k_{\mathrm{B}}\ln 15\) . This can be decomposed into

\[S_{\mathrm{tot}} = S + S_{\mathrm{micro}}. \quad (14.42)\]

Now let us suppose that a system can have \(N\) different, equally likely microstates. As usual, it is hard to measure the details of these microstates directly, but let us assume that they are there. These microstates are divided into various groups (we will call these groups macrostates) with \(n_i\) microstates contained in the ith macrostate. The macrostates are easier to distinguish using experiment because they correspond to some macroscopic, measurable property. We must have that the sum of all the microstates in each macrostate is equal to the total number of microstates, so that

\[\sum_{i}n_{i} = N. \quad (14.43)\]

The probability \(P_{i}\) of finding the system in the ith macrostate is then given by

\[P_{i} = \frac{n_{i}}{N}. \quad (14.44)\]

Equation 14.43 then implies that \(\sum P_{i} = 1\) as required. The total entropy is of course \(S_{\mathrm{tot}} = k_{\mathrm{B}}\ln N\) , though we can't measure that directly (having no information about the microstates which is easily accessible). Nevertheless, \(S_{\mathrm{tot}}\) is equal to the sum of the entropy associated with the freedom of being able to be in different macrostates, which is our measured entropy \(S\) , and the entropy \(S_{\mathrm{micro}}\) associated with it being able to be in different microstates within a macrostate. Putting this statement in an equation, we have

\[S_{\mathrm{tot}} = S + S_{\mathrm{micro}}, \quad (14.45)\]

which is identical to eqn 14.42. The entropy associated with being able to be in different microstates (the aspect we can't measure) is given by

\[S_{\mathrm{micro}} = \langle S_i\rangle = \sum_i P_i S_i, \quad (14.46)\]

===== Page 171 =====

152 Entropy

where \(S_{i} = k_{\mathrm{B}}\ln n_{i}\) is the entropy of the microstates in the ith macrostate and, to recap, \(P_{i}\) is the probability of a particular macrostate being occupied. Hence

\[\begin{array}{rcl}{S}&{=}&{S_{\mathrm{tot}}-S_{\mathrm{micro}}}\\{=}&{k_{\mathrm{B}}\left(\ln N-\sum_{i}P_{i}\ln n_{i}\right)}\\{=}&{k_{\mathrm{B}}\sum_{i}P_{i}(\ln N-\ln n_{i}),}\end{array} \quad (14.47)\]

and using \(\ln N - \ln n_{i} = - \ln (n_{i} / N) = - \ln P_{i}\) (from eqn 14.44) yields Gibbs' expression for the entropy:

\[S = -k_{\mathrm{B}}\sum_{i}P_{i}\ln P_{i}. \quad (14.48)\]

## Example 14.6

Find the entropy for a system with \(\Omega\) macrostates, each with probability \(P_{i} = 1 / \Omega\) (i.e., assuming the microcanonical ensemble).

Solution:

Using eqn 14.48, substitution of \(P_{i} = 1 / \Omega\) yields

\[S = -k_{\mathrm{B}}\sum_{i}P_{i}\ln P_{i} = -k_{\mathrm{B}}\sum_{i = 1}^{\Omega}\frac{1}{\Omega}\ln \frac{1}{\Omega} = -k_{\mathrm{B}}\ln \frac{1}{\Omega} = k_{\mathrm{B}}\ln \Omega , \quad (14.49)\]

which is the same as eqn 14.36.

A connection between the Boltzmann probability and the expression for entropy in eqn 14.48 is demonstrated in the following example.

## Example 14.7

Maximize \(S = - k_{\mathrm{B}}\sum_{i}P_{i}\ln P_{i}\) (eqn 14.48) subject to the constraints that \(\sum P_{i} = 1\) and \(\sum_{i}P_{i}E_{i} = U\) .

Solution:

6See Appendix C.13.

Use the method of Lagrange multipliers, in which we maximize

\[\frac{S}{k_{\mathrm{B}}} -\alpha \times (\mathrm{constraint} 1) - \beta \times (\mathrm{constraint} 2) \quad (14.50)\]

where \(\alpha\) and \(\beta\) are Lagrange multipliers. Thus we vary this expression with respect to one of the probabilities \(P_{j}\) and get

\[\frac{\partial}{\partial P_{j}}\left(\sum_{i} - P_{i}\ln P_{i} - \alpha P_{i} - \beta P_{i}E_{i}\right) = 0, \quad (14.51)\]

===== Page 172 =====

0

\[-\ln P_{j} - 1 - \alpha -\beta E_{j} = 0. \quad (14.52)\]

This can be rearranged to give

\[P_{j} = \frac{\mathrm{e}^{-\beta E_{j}}}{\mathrm{e}^{1 + \alpha}}, \quad (14.53)\]

so that with \(Z = \mathrm{e}^{1 + \alpha}\) we have

\[P_{j} = \frac{\mathrm{e}^{-\beta E_{j}}}{Z}, \quad (14.54)\]

which is our familiar expression for the Boltzmann probability (eqn 4.13).

## Chapter summary

Entropy is defined by \(\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}} / T\)

The entropy of an isolated system tends to a maximum.

The entropy of an isolated system attains this maximum at equilibrium.

The laws of thermodynamics can be stated as follows:

(1) \(U_{\mathrm{Universe}} =\) constant.

(2) \(S_{\mathrm{Universe}}\) can only increase.

These can be combined to give \(\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V\) , which always holds.

The statistical definition of entropy is \(S = k_{\mathrm{B}}\ln \Omega\)

The general definition of entropy, due to Gibbs, is

\[S = -k_{\mathrm{B}}\sum_{i}P_{i}\ln P_{i}.\]

## Exercises

(14.1) A mug of tea has been left to cool from \(90^{\circ}C\) to \(18^{\circ}C\) . If there is \(0.2\mathrm{kg}\) of tea in the mug, and the tea has specific heat capacity \(4200\mathrm{JK}^{- 1}\mathrm{kg}^{- 1}\) show that the entropy of the tea has decreased by \(185.7\mathrm{JK}^{- 1}\) . Comment on the sign of this result.

(14.2) In a free expansion of a perfect gas (also called Joule expansion), we know \(U\) does not change, and no work is done. However, the entropy must increase because the process is irreversible. Are

these statements compatible with the first law \(\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V?\)

(14.3) A \(10\Omega\) resistor is held at a temperature of \(300\mathrm{K}\) . A current of \(5\mathrm{A}\) is passed through the resistor for 2 minutes. Ignoring changes in the source of the current, what is the change of entropy in (a) the resistor and (b) the Universe?

(14.4) Calculate the change of entropy

===== Page 173 =====

1) of a bath containing water, initially at \(20^{\circ}\mathrm{C}\) when it is placed in thermal contact with a very large heat reservoir at \(80^{\circ}\mathrm{C}\) (b) of the reservoir when process (a) occurs, (c) of the bath and of the reservoir if the bath is brought to \(80^{\circ}\mathrm{C}\) through the operation of a Carnot engine between them.

The bath and its contents have total heat capacity \(10^{4}\mathrm{JK}^{- 1}\)

[Hint for (c): which of the heat transfers considered in parts (a) and (b) change when you use a Carnot engine, and by how much? Where does the difference in heat energy go?]

(14.5) A block of lead of heat capacity \(1\mathrm{kJ}\mathrm{K}^{- 1}\) is cooled from \(200\mathrm{K}\) to \(100\mathrm{K}\) in two ways.

(a) It is plunged into a large liquid bath at \(100\mathrm{K}\) (b) The block is first cooled to \(150\mathrm{K}\) in one liquid bath and then to \(100\mathrm{K}\) in another bath.

Calculate the entropy changes in the system comprising block plus baths in cooling from \(200\mathrm{K}\) to \(100\mathrm{K}\) in these two cases. Prove that in the limit of an infinite number of intermediate baths the total entropy change is zero.

(14.6) Calculate the changes in entropy of the Universe as a result of the following processes:

(a) A capacitor of capacitance \(1\mu \mathrm{F}\) is connected to a battery of emf. \(100\mathrm{V}\) at \(0^{\circ}\mathrm{C}\) . (NB think carefully about what happens when a capacitor is charged from a battery.)

(b) The same capacitor, after being charged to \(100\mathrm{V}\) , is discharged through a resistor at \(0^{\circ}\mathrm{C}\) .

(c) One mole of gas at \(0^{\circ}\mathrm{C}\) is expanded reversibly and isothermally to twice its initial volume.

(d) One mole of gas at \(0^{\circ}\mathrm{C}\) is expanded reversibly and adiabatically to twice its initial volume.

(e) The same expansion as in (d) is carried out by opening a valve to an evacuated container of equal volume.

(14.7) Consider \(n\) moles of a gas, initially confined within a volume \(V\) and held at temperature \(T\) . The gas

is expanded to a total volume \(\alpha V\) ,where \(\alpha\) is a constant, by (a) a reversible isothermal expansion and (b) removing a partition and allowing a free expansion into the vacuum. Both cases are illustrated in Fig. 14.9. Assuming the gas is ideal, derive an expression for the change of entropy of the gas in each case.

[Image: (a) A gas in a volume V is expanded isothermally by moving a piston to a total volume alpha V. (b) A gas in a volume V is separated by a partition from an evacuated volume (alpha-1)V. The partition is removed for a free expansion.]
Fig. 14.9 Diagram showing \(n\) moles of gas, initially confined within a volume \(V\) .

Repeat this calculation for case (a), assuming that the gas obeys the van der Waals equation of state

\[\left(p + \frac{n^{2}a}{V^{2}}\right)(V - nb) = nRT. \quad (14.55)\]

Show further that for case (b) the temperature of the van der Waals gas falls by an amount proportional to \((\alpha - 1) / \alpha\) .

(14.8) The probability of a system being in the ith microstate is

\[P_{i} = \mathrm{e}^{-\beta E_{i}} / Z, \quad (14.56)\]

where \(E_{i}\) is the energy of the ith microstate and \(\beta\) and \(Z\) are constants. Show that the entropy is given by

\[S / k_{\mathrm{B}} = \ln Z + \beta U, \quad (14.57)\]

where \(U = \sum_{i}P_{i}E_{i}\) is the internal energy.

(14.9) Use the Gibbs expression for entropy (eqn 14.48) to derive the formula for the entropy of mixing (eqn 14.40).

===== Page 174 =====

1

Robert Mayer studied medicine in Tübingen and took the somewhat unusual career route of signing up as a ship's doctor with a Dutch vessel bound for the East Indies.

[Image: A portrait of Robert Mayer, a man with glasses and a beard.]
Fig. 14.10 Robert Mayer

While letting blood from sailors in the tropics, he noticed that their venous blood was redder than observed back home and concluded that the metabolic oxidation rate in hotter climates was slower. Since a constant body temperature was required for life, the body must reduce its oxidation rate because oxidation of material from food produces internal heat. Though there was some questionable physiological reasoning in his logic, Mayer was

text[[65, 415, 488, 514], [65, 586, 488, 636]]
on to something. He had realized that energy was something that needed to be conserved in any physical process. Back in Heilbronn, Germany, Mayer set to work on a measurement of the mechanical equivalent of heat and wrote a paper in 1841, which was the first statement of the conservation of energy (though James Joule was the son of a wealthy brewer in Salford, near Manchester, England. Joule was educated at home, and his tutors included John Dalton, the father of modern atomic theory. In 1833, illness forced his father to retire, and Joule was left in charge of the family brewery. He had a passion for scientific research and set up a laboratory, working there in the early morning and late evening so that he could continue his day job. In 1840, he James Joule was the son of a wealthy brewer in Salford, near Manchester, England. Joule was educated at home, and his tutors included John Dalton, the father of modern atomic theory. In 1833, illness forced his father to retire, and Joule was left in charge of the family brewery. He had a passion for scientific research and set up a laboratory, working there in the early morning and late evening so that he could continue his day job. In 1840, he showed that the heat dissipated by an electric current \(I\) in a resistor \(R\) was proportional to \(I^{2}R\) (what we now call Joule heating). In 1846, Joule discov

[Image: A portrait of James Joule, a man with a long white beard.]
Fig. 14.11 James Joule

showed that the heat dissipated by an electric current \(I\) in a resistor \(R\) was proportional to \(I^{2}R\) (what we now call Joule heating). In 1846, Joule discov

he used the word "force"). Mayer's work predated the ideas of Joule and Helmholtz (though his experiment was not as accurate as Joule's) and his notion of the conservation of energy had a wider scope than that of Helmholtz; not only were mechanical energy and heat convertible, but his principle could be applied to tides, meteorites, solar energy, and living things. His paper was eventually published in 1842, but received little acclaim. A later more detailed paper in 1845 was rejected and he published it privately.

Mayer then went through a bit of a bad patch, to put it mildly: others began to get the credit for ideas he thought he had pioneered, three of his children died in the late 1840's and he attempted suicide in 1850, jumping out of a third- storey window, but only succeeding in permanently laming himself. In 1851 he checked into a mental institution where he received sometimes brutal treatment and was discharged in 1853, with the doctors unable to offer him any hope of a cure. In 1858, he was even referred to as being dead in a lecture by Liebig (famous for his condenser, and editor of the journal that had accepted Mayer's 1842 paper). Mayer's scientific reputation began to recover in the 1860's and he was awarded the Copley Medal of the Royal Society of London in 1871, the year after it was awarded to Joule.

ered the phenomenon of magnetostriction (by which a magnet changes its length when magnetized). However Joule's work did not impress the Royal Society and he was dismissed as a mere provincial dilettante. However, Joule was undeterred and he decided to work on the convertibility of energy and to try to measure the mechanical equivalent of heat.

In his most famous experiment he measured the increase in temperature of a thermally insulated barrel of water, stirred by a paddle wheel, which was driven by a falling weight. But this was just one of an exhaustive series of meticulously performed experiments that aimed to determine the mechanical equivalent of heat, using electrical circuits, chemical reactions, viscous heating, mechanical contraptions, and gas compression. He even attempted to measure the temperature difference between water at the top and bottom of a waterfall, an opportunity afforded to him by being in Switzerland on his honeymoon!

===== Page 175 =====

156 Biographies

Joule's obsessive industry paid off: his completely different experimental methods gave consistent results.

Part of Joule's success was in designing thermometers with unprecedented accuracy; they could measure temperature changes as small as \(1 / 200\) degrees Fahrenheit. This was necessary as the effects he was looking for tended to be small. His methods proved to be accurate and even his early measurements were within several percent of the modern accepted value of the mechanical equivalent of heat, and his 1850 experiment was within 1 percent. However, the smallness of the effect led to scepticism, particularly from the scientific establishment, who had all had proper educations, didn't spend their days making beer and knew that you couldn't measure temperature differences as tiny as Joule claimed to have observed.

However the tide began to turn in Joule's favour in the late 1840's. Helmholtz recognized Joule's contribution to the conservation of energy in his paper

of 1847. In the same year, Joule gave a talk at a British Association meeting in Oxford where Stokes, Faraday, and Thomson were in attendance. Thomson was intrigued and the two struck up a correspondence, resulting in a fruitful collaboration between the two between 1852 and 1856. They measured the temperature fall in the expansion of a gas, and discovered the Joule- Thomson effect.

Joule refused all academic appointments, preferring to work independently. Though without advanced education, Joule had excellent instincts and was an early defender of the kinetic theory of gases, and felt his way towards a kinetic theory of heat, perhaps because of his youthful exposure to Dalton's teachings. On Joule's gravestone is inscribed the number "772.55", the number of foot- pounds required to heat a pound of water by one degree Fahrenheit. It is fitting that today, mechanical and thermal energy are measured in the same unit: the Joule.

## Rudolf Clausius (1822-1888)

Rudolf Clausius studied mathematics and physics in Berlin, and was awarded his doctorate in Halle University for work on the colour of the sky.

[Image: A portrait of Rudolf Clausius, a man with dark hair and a beard.]
Fig. 14.12 Rudolf Clausius

Clausius turned his attention to the theory of heat and, in 1850, he published a paper that essentially saw him picking up the baton left by Sadi Carnot (via an 1834 paper by Emile Clapeyron) and running with it. He defined the internal energy, \(U\) of a system and wrote that the change of heat was given by \(\mathrm{d}Q = \mathrm{d}U + (1 / J)p\mathrm{d}V\) , where the factor \(J\) (the mechanical equivalent of heat) was necessary to convert mechanical energy \(p\mathrm{d}V\) into the same units as thermal energy (a conversion which in today's units is, of course, unnecessary). He also showed that in a Carnot process, the integral round a closed loop of \(f(T)\mathrm{d}Q\) was zero, where \(f(T)\) was some function of temperature.

convert mechanical energy \(p\mathrm{d}V\) into the same units as thermal energy (a conversion which in today's units is, of course, unnecessary). He also showed that in a Carnot process, the integral round a closed loop of \(f(T)\mathrm{d}Q\) was zero, where \(f(T)\) was some function of temperature.

His work brought him a professorship in Berlin, though he subsequently moved to chairs in Zurich (1855), Würzburg (1867), and Bonn (1869). In 1854,

he wrote a paper in which he stated that heat cannot of itself pass from a colder to a warmer body, a statement of the second law of thermodynamics. He also showed that his function \(f(T)\) could be written (in modern notation) as \(f(T) = 1 / T\) . In 1865 he was ready to give \(f(T)\mathrm{d}Q\) a name, defining the entropy (a word he made up to sound like "energy" but contain "trope" meaning "turning", as in the word "heliotrope", a plant which turns towards the Sun) using \(\mathrm{d}S = \mathrm{d}Q / T\) for a reversible process. He also summarized the first and second laws of thermodynamics by stating that the energy of the world is constant and its entropy tends to a maximum.

When Bismarck started the Franco- Prussian war, Clausius patriotically ran a volunteer ambulance corps of Bonn students in 1870- 1871, carrying off the wounded from battles in Vionville and Gravelotte. He was wounded in the knee, but received the Iron Cross for his efforts in 1871. He was no less zealous in defending Germany's pre- eminence in thermal physics in various priority disputes, being provoked into siding with Mayer's claim over Joule's, and in various debates with Tait, Thomson, and Maxwell. Clausius however showed little interest in the work of Boltzmann and Gibbs that aimed to understand the molecular origin of the irreversibility that he had discovered and named.

===== Page 176 =====

15

In this chapter we are going to examine the concept of information and relate it to thermodynamic entropy. At first sight, this seems a slightly crazy thing to do. What on earth do something to do with heat engines and something to do with bits and bytes have in common? It turns out that there is a very deep connection between these two concepts. To understand why, we begin our account by trying to formulate one definition of information.

## 15.1 Information and Shannon entropy

Consider the following three true statements about Isaac Newton and his birthday.1

(1) Isaac Newton's birthday falls on a particular day of the year.
(2) Isaac Newton's birthday falls in the second half of the year.
(3) Isaac Newton's birthday falls on the 25th of a month.

The first statement has, by any sensible measure, no information content. All birthdays fall on a particular day of the year. The second statement has more information content: at least we now know which half of the year his birthday is. The third statement is much more specific and has the greatest information content.2

How do we quantify information content? Well, one property we could notice is that the greater the probability of the statement being true in the absence of any prior information, the less the information content of the statement. Thus if you knew no prior information about Newton's birthday, then you would say that statement 1 has probability \(P_{1} = 1\) statement 2 has probability \(P_{2} = \frac{1}{2}\) , and statement 3 has probability \(P_{3} = \frac{12}{365}\) ; so as the probability decreases, the information content increases. Moreover, since the useful statements 2 and 3 are independent, then if you are given statements 2 and 3 together, their information contents should add. Moreover, the probability of statements 2 and 3 both being true, in the absence of prior information, is \(P_{2} \times P_{3} = \frac{6}{365}\) . Since the probability of two independent statements being true is the product of their individual probabilities, and since it is natural to assume that information content is additive, one is motivated to adopt the definition of information which was proposed by Claude Shannon (1916- 2001) as follows:

<table>15.1 Information and Shannon entropy15715.2 Information and thermodynamics15915.3 Data compression16015.4 Quantum information16215.5 Conditional and joint probabilities16515.6 Bayes&#x27; theorem165Chapter summary168Further reading168Exercises169</table>

1The statements assume that dates are expressed according to the calendar which was used in Newton's day. The Gregorian calendar was not adopted in England until 1742.

2In fact, Newton was born on December 25th, 1642. Converting this Julian calendar date to the (currently used) Gregorian calendar gives January 4th, 1643, so Newton's dates are usually given as 1643- 1727.

3We are using the fact that 1642 was not a leap year!

===== Page 177 =====

4We need \(k\) to be a positive constant so that as \(P\) goes up, \(Q\) goes down.

The information content \(Q\) of a statement is defined by

\[Q = -k\log P, \quad (15.1)\]

where \(P\) is the probability of the statement and \(k\) is a positive constant.4 If we use \(\log_2\) (log to the base 2) for the logarithm in this expression and also \(k = 1\) ,then the information \(Q\) is measured in bits. If instead we use \(\ln \equiv \log_{\mathrm{e}}\) and choose \(k = k_{\mathrm{B}}\) ,then we have a definition that, as we shall see, will match what we have found in thermodynamics. In this chapter, we will stick with the former convention since bits are a useful quantity with which to think about information.

Thus, if we have a set of statements with probability \(P_{i}\) ,with corresponding information \(Q_{i} = - k\log P_{i}\) ,then the average information content \(S\) is given by

\[S = \langle Q\rangle = \sum_{i}Q_{i}P_{i} = -k\sum_{i}P_{i}\log P_{i}. \quad (15.2)\]

The average information is called the Shannon entropy.

## Example 15.1

A fair die produces outcomes 1,2,3,4,5,and 6 with probabilities \(\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{1}{6},\frac{\mathrm{i}}{6},\frac{1}{6},\frac{\mathrm{i}}{6}\) The information associated with each outcome is \(Q = - k\log \frac{1}{6} = k\log 6\) and the average information content is then \(S = k\log 6\) .Taking \(k = 1\) and using log to the base 2 gives a Shannon entropy of 2.58 bits. A biased die produces outcomes 1,2,3,4,5,and 6 with probabilities \(\frac{1}{10},\frac{1}{10},\frac{1}{10},\frac{1}{10},\frac{\mathrm{i}}{10},\frac{1}{2}\) The information contents associated with the outcomes are \(k\log 10\) \(k\log 10\) \(k\log 10\) \(k\log 10\) \(,k\log 10\) \(k\log 10\) and \(k\log 2\) .(These are 3.32,3.32,3.32,3.32,3.32,and 1 bit respectively.) If we take \(k = 1\) again, the Shannon entropy is then \(S = k(5\times \frac{1}{10}\log 10 + \frac{1}{2}\log 2) = k(\log \sqrt{20})\) (this is 2.16 bits). This Shannon entropy is smaller than in the case of the fair die.

The Shannon entropy quantifies how much information we gain, on average, following a measurement of a particular quantity. (Another way of looking at it is to say the Shannon entropy quantifies the amount of uncertainty we have about a quantity before we measure it.) To make these ideas more concrete, let us study a simple example in which there are only two possible outcomes of a particular random process (such as the tossing of a coin, or asking the question "will it rain tomorrow?").

===== Page 178 =====

15.2 Information and thermodynamics 159

## Example 15.2

What is the Shannon entropy for a Bernoulli trial (a two- outcome random variable \(^5\) ) with probabilities \(P\) and \(1 - P\) of the two outcomes? Solution:

\[S = -\sum_{i}P_{i}\log P_{i} = -P\log P - (1 - P)\log (1 - P), \quad (15.3)\]

where we have set \(k = 1\) . This behaviour is sketched in Fig. 15.1. The Shannon entropy has a maximum when \(p = \frac{1}{2}\) (greatest uncertainty about the outcome, or greatest information gained, 1 bit, following a trial) and a minimum when \(p = 0\) or 1 (least uncertainty about the outcome, or least information gained, 0 bit, following a trial).

The information associated with each of the two possible outcomes is also shown in Fig. 15.1 as dotted lines. The information associated with the outcome having probability \(P\) is given by \(Q_{1} = -\log_{2}P\) and decreases as \(P\) increases. Clearly when this outcome is very unlikely ( \(P\) small) the information associated with getting that outcome is very large \(Q_{1}\) is many bits of information). However, such an outcome doesn't happen very often so it doesn't contribute much to the average information (i.e., to the Shannon entropy, the solid line in Fig. 15.1). When this outcome is almost certain ( \(P\) almost 1) it contributes a lot to the average information but has very little information content. For the other outcome, with probability \(1 - P\) , \(Q_{2} = -\log_{2}(1 - P)\) and the behaviour is simply a mirror image of this. The maximum average information is when \(P = 1 - P = \frac{1}{2}\) and both outcomes have 1 bit of information associated with them.

[Image: A graph of Shannon entropy S(P) in bits versus probability P. The curve is an inverted U-shape, reaching a maximum of 1 bit at P=0.5. Dotted lines show the information associated with each outcome, -log2 P and -log2 (1-P).]
5See Section 3.7

Fig. 15.1 The Shannon entropy of a Bernoulli trial (a two- outcome random variable) with probabilities of the two outcomes given by \(P\) and \(1 - P\) . The units are chosen so that the Shannon entropy is in bits. Also shown is the information associated with each outcome (dotted lines).

## 15.2 Information and thermodynamics

Remarkably, the formula for Shannon entropy in eqn 15.2 is identical (apart from whether you take your constant as \(k\) or \(k_{\mathrm{B}}\) ) to Gibbs' expression for thermodynamic entropy in eqn 14.48. This gives us a useful perspective on what thermodynamic entropy is. It is a measure of our uncertainty of a system, based on our limited knowledge of its properties and ignorance about which of its microstates it is in. In making inferences on the basis of partial information, we can assign probabilities on the basis that we maximize entropy subject to the constraints provided by what is known about the system. This is exactly what we did in Example 14.7, when we maximized the Gibbs' entropy of an isolated system subject to the constraint that the total energy \(U\) was constant; hey presto, we found that we recovered the Boltzmann probability distribution. With this viewpoint, one can begin to understand thermodynamics from an information theory viewpoint.

===== Page 179 =====

6We could equally well reset the bits to one.

However, not only does information theory apply to physical systems, but as pointed out by Rolf Landauer (1927- 1999), information itself is a physical quantity. Imagine a physical computing device which has stored \(N\) bits of information and is connected to a thermal reservoir of temperature \(T\) . The bits can be either one or zero. Now we decide to physically erase that information. Erasure must be irreversible. There must be no vestige of the original stored information left in the erased state of the system. Let us erase the information by resetting all the bits to zero.6 Then this irreversible process reduces the number of states of the system by \(\ln 2^{N}\) and hence the entropy of the system goes down by \(Nk_{\mathrm{B}}\ln 2\) , or \(k_{\mathrm{B}}\ln 2\) per bit. For the total entropy of the Universe not to decrease, the entropy of the surroundings must go up by \(k_{\mathrm{B}}\ln 2\) per bit and so we must dissipate heat in the surroundings equal to \(k_{\mathrm{B}}T\ln 2\) per bit erased.

This connection between entropy and information helps us in our understanding of Maxwell's demon discussed in Section 14.7. By performing computations about molecules and their velocities, the demon has to store information. Each bit of information is associated with entropy, as becomes clear when the demon has to free up some space on its hard disk to continue computing. The process of erasing one bit of information gives rise to an increase of entropy of \(k_{\mathrm{B}}\ln 2\) . If Maxwell's demon reverses the Joule expansion of 1 mole of gas, it might therefore seem that it has decreased the entropy of the Universe by \(N_{\mathrm{A}}k_{\mathrm{B}}\ln 2 = R\ln 2\) , but it will have had to store at least \(N_{\mathrm{A}}\) bits of information to do this. Assuming that Maxwell's demons only have on- board a storage capacity of a few hundred gigabytes, which is much less than \(N_{\mathrm{A}}\) bits, the demon will have had to erase its disk many, many times in the process of its operation, thus leading to an increase in entropy of the Universe which at least equals, and probably outweighs, the decrease of entropy of the Universe it was aiming to achieve.

If the demon is somehow fitted with a vast on- board memory so that it doesn't have to erase its memory to do the computation, then the increase in entropy of the Universe can be delayed until the demon needs to free up some memory space. Eventually, one supposes, as the demon begins to age and becomes forgetful, the Universe will reclaim all that entropy!

## 15.3 Data compression

Information must be stored, or sometimes transmitted from one place to another. It is therefore useful if it can be compressed down to its minimum possible size. This really begs the question what the actual irreducible amount of real information in a particular block of data really is; many messages, political speeches, and even sometimes book chapters, contain large amounts of extraneous padding that is not really needed. Of course, when we compress a file on a computer we often get something that is unreadable to human beings. The English language

===== Page 180 =====

 has various quirks, such as when you see a letter "q" it is almost always followed by a "u", so is that second "u" really needed when you know it is coming? A good data compression algorithm will get rid of extra things like that, plus much more besides. Hence, the question of how many bits are in a given source of data seems like a useful question for computer scientists to attempt to answer; in fact we will see it has implications for physics!

We will not prove Shannon's noiseless channel coding theorem here, but motivate it and then state it.

## Example 15.3

Let us consider the simplest case in which our data are stored in the form of the binary digits "0" and "1". Let us further suppose that the data contain "0" with probability \(P\) and "1" with probability \(1 - P\) . If \(P = \frac{1}{2}\) then our data cannot really be compressed, as each bit of data contains real information. Let us now suppose that \(P = 0.9\) so that the data contain more "0"s than "1"s. In this case, the data contain less information, and it is not hard to find a way of taking advantage of this. For example, let us read the data into our compression algorithm in pairs of bits, rather than one bit at a time, and make the following transformations:


In each of the transformations, we end on a single "0", which lets the decompression algorithm know that it can start reading the next sequence. Now, of course, although the pair of symbols "00" has been compressed to "0", saving a bit, the pair of symbols "01" has been enlarged to "110" and "11" has been even more enlarged to "110", costing one extra or two extra bits respectively. However, "00" is very likely to occur (probability 0.81) while "01" and "11" are much less likely to occur (probabilities 0.09 and 0.01 respectively), so overall we save bits using this compression scheme.

This example gives us a clue as to how to compress data more generally. The aim is to identify in a sequence of data what the typical sequences are and then efficiently code only those. When the amount of data becomes very large, then anything other than these typical sequences is very unlikely to occur. Because there are fewer typical sequences than there are sequences in general, a saving can be made. Hence, let us divide up some data into sequences of length \(n\) . Assuming the elements in the data do not depend on each other, then the

===== Page 181 =====

 probability of finding a sequence \(x_{1}, x_{2}, \ldots , x_{n}\) is

\[P(x_{1}, x_{2}, \ldots , x_{n}) = P(x_{1})P(x_{2}) \ldots P(x_{n}) \approx P^{n}P(1 - P)^{n(1 - P)}, \quad (15.4)\]

for typical sequences. Taking logarithms to base 2 of both sides gives

\[-\log_{2}P(x_{1},x_{2},\ldots ,x_{n})\approx -nP\log_{2}P - n(1 - P)\log_{2}(1 - P) = nS, \quad (15.5)\]

where \(S\) is the entropy for a Bernoulli trial with probability \(P\) . Hence

\[P(x_{1},x_{2},\ldots ,x_{n})\approx \frac{1}{2^{nS}}. \quad (15.6)\]

This shows that there are at most only \(2^{nS}\) typical sequences and hence it only requires \(nS\) bits to code them. As \(n\) becomes larger, and the typical sequences become longer, the possibility of this scheme failing becomes smaller and smaller.

A compression algorithm will take a typical sequence of \(n\) terms \(x_{1}, x_{2}, \ldots , x_{n}\) and turn them into a string of length \(nR\) . Hence, the smaller \(R\) is, the greater the compression. Shannon's noiseless channel coding theorem states that if we have a source of information with entropy \(S\) , and if \(R > S\) , then there exists a reliable compression scheme of compression factor \(R\) . Conversely, if \(R < S\) then any compression scheme will not be reliable. Thus the entropy \(S\) sets the ultimate compression limit on a set of data.

## 15.4 Quantum information

This section shows how the concept of information can be extended to quantum systems and assumes familiarity with the main results of quantum mechanics.

In this chapter we have seen that in classical systems the information content is connected with the probability. In quantum systems, these probabilities are replaced by density matrices. A density matrix is used to describe the statistical state of a quantum system, as can arise for a quantum system in thermal equilibrium at finite temperature. A summary of the main results concerning density matrices is given in the box on page 163.

For quantum systems, the information is represented by the operator \(- k \log \rho\) , where \(\rho\) is the density matrix; as before we take \(k = 1\) . Hence the average information, or entropy, would be \(\langle -\log \rho \rangle\) . This leads to the definition of the von Neumann entropy \(S\) as

\[S(\rho) = -\mathrm{Tr}(\rho \log \rho). \quad (15.7)\]

If the eigenvalues of \(\rho\) are \(\lambda_{1}, \lambda_{2} \ldots\) , then the von Neumann entropy becomes

\[S(\rho) = -\sum_{i}\lambda_{i}\log \lambda_{i}, \quad (15.8)\]

which looks like the Shannon entropy.

===== Page 182 =====

15.4 Quantum information 163

## The density matrix

If a quantum system is in one of a number of states \(|\psi_i\rangle\) with probability \(P_{i}\) , then the density matrix \(\rho\) for the system is defined by

\[\rho = \sum_{i}P_{i}|\psi_{i}\rangle \langle \psi_{i}|. \quad (15.9)\]

As an example, think of a three- state system and think of \(|\psi_{1}\rangle\) as a column vector \(\begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}\) , and hence \(\langle \psi_{1}\rangle\) as a row vector \((1,0,0)\) and similarly for \(|\psi_{2}\rangle\) \(\langle \psi_{2}|\) \(|\psi_{3}\rangle\) and \(\langle \psi_{3}|\) . Then

\[\begin{array}{rcl}{\rho} & = & {P_1\left( \begin{array}{ccc}1 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 0 \end{array} \right) + P_2\left( \begin{array}{ccc}0 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 0 \end{array} \right) + P_3\left( \begin{array}{ccc}0 & 0 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0 \end{array} \right)}\\ {} & = & {\left( \begin{array}{ccc}P_1 & 0 & 0\\ 0 & P_2 & 0\\ 0 & 0 & P_3 \end{array} \right).} \end{array} \quad (15.10)\]

This form of the density matrix looks very simple, but this is only because we have expressed it in a very simple basis.

If \(P_{j}\neq 0\) and \(P_{i\neq j} = 0\) , then the system is said to be in a pure state and \(\rho\) can be written in the simple form

\[\rho = |\psi_j\rangle \langle \psi_j|. \quad (15.11)\]

Otherwise, it is said to be in a mixed state.

One can show that the expectation value \(\langle \hat{A}\rangle\) of a quantum mechanical operator \(\hat{A}\) is equal to

\[\langle \hat{A}\rangle = \mathrm{Tr}(\hat{A}\rho). \quad (15.12)\]

One can also prove that

\[\mathrm{Tr}\rho = 1, \quad (15.13)\]

where \(\mathrm{Tr}\rho\) means the trace of the density matrix. This expresses the fact that the sum of the probabilities must equal unity, and is in fact a special case of eqn 15.12, setting \(\hat{A} = 1\) .

One can also show that \(\mathrm{Tr}\rho^2 \leq 1\) with equality if and only if the state is pure.

For a system in thermal equilibrium at temperature \(T\) , \(P_{i}\) is given by the Boltzmann factor \(\mathrm{e}^{-\beta E_{i}}\) where \(E_{i}\) is an eigenvalue of the Hamiltonian \(\hat{H}\) . The thermal density matrix \(\rho_{\mathrm{th}}\) is

\[\rho_{\mathrm{th}} = \sum_{i}\mathrm{e}^{-\beta E_{i}}|\psi_{i}\rangle \langle \psi_{i}| = \exp (-\beta \hat{H}). \quad (15.14)\]

===== Page 183 =====

8A pure state is defined in the box on page 163.

## Example 15.4

Show that the entropy of a pure state is zero. How can you maximize the entropy?

Solution:

(i) As shown in the box on page 163, the trace of the density matrix is equal to one \((\mathrm{Tr}\rho = 1)\) , and hence the sum of the eigenvalues of the density matrix is

\[\sum \lambda_{i} = 1. \quad (15.15)\]

For a pure state only one eigenvalue will be one and all the other eigenvalues will be zero, and hence \(S(\rho) = 0\) , i.e., the entropy of a pure state is zero. This is not surprising, since for a pure state there is no "uncertainty" about the state of the system.

(ii) The entropy \(S(\rho) = -\sum_{i}\lambda_{i}\log \lambda_{i}\) is maximized \(^{10}\) when \(\lambda_{i} = 1 / n\) for all \(i\) , where \(n\) is the dimension of the density matrix. In this case, the entropy is \(S(\rho) = n\times (- \frac{1}{n}\log \frac{1}{n}) = \log n\) . This corresponds to there being maximal uncertainty in its precise state.

11 An arbitary qubit can be written as \(|\psi \rangle = \alpha |0\rangle +\beta |1\rangle\) where \(|\alpha |^{2} + |\beta |^{2} = 1\) 12 Einstein called entanglement "spooky action at a distance", and used it to argue against the Copenhagen interpretation of quantum mechanics and show that quantum mechanics is incomplete.

Classical information is made up only of sequences of "0"s and "1"s (in a sense, all information can be broken down into a series of "yes/no" questions). Quantum information is composed of quantum bits (known as qubits), that are two- level quantum systems which can be represented by linear combinations \(^{11}\) of the states \(|0\rangle\) and \(|1\rangle\) . Quantum mechanical states can also be entangled with each other. The phenomenon of entanglement \(^{12}\) has no classical counterpart. Quantum information therefore also contains entangled superpositions such as \((|01\rangle +|10\rangle) / \sqrt{2}\) . Here the quantum states of two objects must be described with reference to each other; measurement of the first bit in the sequence to be a 0 forces the second bit to be 1; if the measurement of the first bit gives a 1, the second bit has to be 0; these correlations persist in an entangled quantum system even if the individual objects encoding each bit are spatially separated. Entangled systems cannot be described by pure states of the individual subsystems, and this is where entropy plays a role, as a quantifier of the degree of mixing of states. If the overall system is pure, the entropy of its subsystems can be used to measure its degree of entanglement with the other subsystems. \(^{13}\)

In this text we do not have space to provide many details about the subject of quantum information, which is a rapidly developing area of current research. Suffice it to say that the processing of information in quantum mechanical systems has some intriguing facets, which are not present in the study of classical information. Entanglement of bits is just one example. As another example, the no- cloning theorem states that it is impossible to make a copy of non- orthogonal quantum mechanical states (for classical systems, there is no physical mechanism to stop you copying information, only copyright laws). All of these features lead to the very rich structure of quantum information theory.

===== Page 184 =====

15.5 Conditional and joint probabilities

To explore some implications of information theory in more depth we need to introduce some more ideas from probability theory. Now the probability of something often depends on information about what has happened before. Whether it rains tomorrow may depend on whether it has actually rained today. This means that having the information about whether it has rained today may affect how you assign the probability of it raining tomorrow. Not having that information may lead to a different result. This allows us to define the conditional probability \(P(\mathrm{A}|\mathrm{B})\) as the probability that event A occurs given that event B has happened. We can also define the joint probability \(P(\mathrm{A}\cap \mathrm{B})\) as the probability that event A and event B both occur. The joint probability \(P(\mathrm{A}\cap \mathrm{B})\) is equal to the probability that event B occurred multiplied by the probability that A occurred, given that B did, i.e.,

\[P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{A}|\mathrm{B})P(\mathrm{B}), \quad (15.16)\]

and, equally well,

\[P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{B}|\mathrm{A})P(\mathrm{A}). \quad (15.17)\]

If A and B are independent events, then \(P(\mathrm{A}|\mathrm{B}) = P(\mathrm{A})\) (because the probability that A occurs is independent of whether B has occurred or not) and hence

\[P(\mathrm{A}\cap \mathrm{B}) = P(\mathrm{A})P(\mathrm{B}). \quad (15.18)\]

Now consider the case where there are a number of mutually exclusive events \(\mathrm{A}_i\) such that

\[\sum_{i}P(\mathrm{A}_{i}) = 1. \quad (15.19)\]

Then we can write the probability of some other event \(X\) as

\[P(X) = \sum_{i}P(X|\mathrm{A}_{i})P(\mathrm{A}_{i}). \quad (15.20)\]

In the following section, these ideas will be used to prove a very important theorem.

## 15.6 Bayes' theorem

Very often, you know that if you are given some hypothesis H you can use it to compute the probability of some outcome O assuming that hypothesis (i.e., you can compute \(P(\mathrm{O}|\mathrm{H})\) ). But what you often want to do is the reverse: you know the outcome because it has actually occurred and you want to choose an explanation out of the possible hypotheses. In other words, given the outcome you want to know the probability that the hypothesis is true. This transformation of \(P(\mathrm{O}|\mathrm{H})\) into \(P(\mathrm{H}|\mathrm{O})\) can be accomplished using Bayes' theorem. \(^{14}\) This can be stated as follows:

\[P(\mathrm{A}|\mathrm{B}) = \frac{P(\mathrm{B}|\mathrm{A})P(\mathrm{A})}{P(\mathrm{B})}. \quad (15.21)\]

===== Page 185 =====

166 Information theory

Here \(P(\mathbf{A})\) is called the prior probability, since it is the probability of A occurring without any knowledge as to the outcome of B. The quantity which you derive is \(P(\mathbf{A}|\mathbf{B})\) , the posterior probability. The proof of Bayes' theorem is very simple: one simply equates eqns 15.16 and 15.17 and rearranges.

## Example 15.5

It is known that one per cent of a group of athletes are using illegal drugs to boost their performance. The drug test is \(95\%\) accurate (and so will give a correct diagnosis \(95\%\) of the time). A particular athlete is tested and gets a positive result. Is he guilty?

Solution:

The prior probabilities are

\[\begin{array}{rcl}{P(\mathbf{D})} & = & {0.01}\\ {P(\bar{\mathbf{D}})} & = & {0.99,} \end{array} \quad (15.22)\]

where \(\bar{\mathbf{D}}\) means "taking drugs" and \(\bar{\mathbf{D}}\) means "not taking drugs". We will also define \(\mathbf{Y}\) to mean "test positive" and \(\bar{\mathbf{Y}}\) to mean "test negative". Since he tested positive, what we want to know is the probability of his guilt, which is \(P(\mathbf{D}|\mathbf{Y})\) . Because the drug test is \(95\%\) accurate, we have

\[\begin{array}{rcl}{P(\mathbf{Y}|\mathbf{D})} & = & {0.95\qquad \mathrm{(true~positive)}}\\ {P(\mathbf{Y}|\bar{\mathbf{D}})} & = & {0.05\qquad \mathrm{(false~positive)}}\\ {P(\bar{\mathbf{Y}}|\bar{\mathbf{D}})} & = & {0.95\qquad \mathrm{(true~negative)}}\\ {P(\bar{\mathbf{Y}}|\mathbf{D})} & = & {0.05\qquad \mathrm{(false~negative)}}. \end{array} \quad (15.23)\]

The probability \(P(\mathbf{Y})\) of a positive test is given by eqn 15.20 as

\[P(\mathbf{Y}) = P(\mathbf{Y}|\mathbf{D})P(\mathbf{D}) + P(\mathbf{Y}|\bar{\mathbf{D}})P(\bar{\mathbf{D}}) = 0.95\times 0.01 + 0.05\times 0.99\approx 0.06. \quad (15.24)\]

Bayes' theorem then gives

\[P(\mathbf{D}|\mathbf{Y}) = \frac{P(\mathbf{Y}|\mathbf{D})P(\mathbf{D})}{P(\mathbf{Y})} = 0.16. \quad (15.25)\]

Hence there is only a \(16\%\) probability that he took the drug. This surprising result occurs because although the test is very accurate, the case of illegal drug use in athletes is actually very rare (at least under the assumptions given in this example) and so most positive results are false positives.

The next example demonstrates very powerfully that the probabilities you assign depend very strongly on the information you are given, and sometimes in a surprising way.

===== Page 186 =====

1

## Example 15.6

Mrs Trellis (from North Wales) has two children, born three years apart. One of them is a boy. What is the probability that Mrs Trellis has a daughter? [Not all of the information given to you here is relevant!] If, instead, you had been told that "Mrs Trellis has two children and the taller of her children was a boy", would that have changed your answer? Solution:

This is another question that emphasizes the fact that probability all depends on the information you know. Some of the information you are given here is indeed irrelevant (the three years apart and the North Wales are irrelevant). The information you have is that one of the children is a boy. There are now three possibilities for the sexes of Mrs Trellis' children (in order of seniority):

(1) boy; boy,
(2) boy; girl,
(3) girl; boy.

The fourth possibility you might think of, "girl; girl", is discounted by the information that one of the children is a boy. Thus the probability that Mrs Trellis has a daughter is \(\frac{2}{3}\) [assuming of course that Mrs Trellis has a 50:50 chance of producing a male or female baby at every birth]. The reason that the answer to this question is not \(\frac{1}{2}\) is that we don't know which of Mrs Trellis' two children our initial bit of information refers to (i.e., that the child is a boy), whether it refers to the older or the younger one.

Forget older versus younger, we could distinguish between the two children in many different ways: in order of height, weight, number of freckles, etc. Thus the table of possibilities listed above could be written, not in order of seniority, but in order of height, darkness of hair, blueness of eyes, etc. So, if instead we were told that it was the taller of the children that was a boy, then amazingly that additional information changes the probabilities. All our attention is now focused on the other child, the shorter one, who can either be male or female. It's now a probability of \(\frac{1}{2}\) that the shorter child is a daughter.

Astonishingly, knowledge of the height of one of the children alters the probability of sex, even though we have assumed that height and sex are uncorrelated. If you like, we could have replaced the statement "the taller of the children was a boy" with "the child with a first name earlier in the alphabet was a boy" and that would also have the same effect! This demonstrates the important role of distinguishability in statistics, a concept that will return!

In physics, we try to make inferences about the world based on what we can measure. Those inferences are made on the basis of probability

===== Page 187 =====

15This approach was used in Example 14.7; see also Exercises 15.3 and 22.1.

16Example 14.7.

and information theory and this feeds into the Shannon entropy. When we cover the indistinguishability of particles in a gas in Chapter 21 we will find that this has real thermodynamic implications and the above example prepares us not to be surprised by this.

Furthermore, information theory provides a rationale for setting up probability distributions on the basis of partial knowledge; one simply maximizes the entropy of the distribution subject to the constraints provided by the data. This so- called maximum entropy estimate is the least biased estimate consistent with the given data.15 Thermodynamics also gives the best description of the properties of a system that has so many \((\approx 10^{23})\) particles that one cannot follow it precisely; the Boltzmann probability obtained by maximizing the Gibbs entropy16 is the least- biased estimate of the probability consistent with the constraint that a system has fixed internal energy \(U\) .

## Chapter summary

- The information \(Q\) is given by \(Q = -\ln P\) where \(P\) is the probability.- The entropy is the average information \(S = \langle Q \rangle = -\sum_{i} P_{i} \log P_{i}\) .- The quantum mechanical generalization of this is the von Neumann entropy given by \(S(\rho) = -\mathrm{Tr}(\rho \log \rho)\) where \(\rho\) is the density matrix.- Bayes' theorem relates the posterior probability (which is a conditional probability) to the prior probability.

## Further reading

The results that we have stated in this chapter concerning Shannon's coding theorems, and which we considered only for the case of Bernoulli trials, i.e., for binary outputs, can be proved for the general case. Shannon also studied communication over noisy channels, in which the presence of noise randomly flips bits with a certain probability. In this case it is also possible to show how much information can be reliably transmitted using such a channel (essentially how many times you have to "repeat" the message to get yourself "heard", though actually this is done using error- correcting codes). Further information may be found in Feynman (1996) and Mackay (2003). An excellent account of the problem of Maxwell's demon may be found in Leff and Rex (2003). Quantum information theory has become a very hot research topic in the last few years and an excellent introduction is Nielsen and Chuang (2000).

===== Page 188 =====

 Exercises

(15.1) In a typical microchip, a bit is stored by a \(5\mathrm{fF}\) capacitor using a voltage of \(3\mathrm{V}\) . Calculate the energy stored in eV per bit and compare this with the minimum heat dissipation by erasure, which is \(k_{\mathrm{B}}T\ln 2\) per bit, at room temperature.

(15.2) A particular logic gate takes two binary inputs \(A\) and \(B\) and has two binary outputs \(A^{\prime}\) and \(B^{\prime}\) . Its truth table is


<table>ABA&#x27;B&#x27;0011011010011100</table>

and the operations producing these outputs are \(A^{\prime} = \mathrm{NOT}A\) and \(B^{\prime} = \mathrm{NOT}B\) .The input has a Shannon entropy of 2 bits. Show that the output has a Shannon entropy of 2 bits.

A second logic gate has a truth table given by


<table>ABA&#x27;B&#x27;0000011010101111</table>

This can be achieved using \(A^{\prime} = A\mathrm{OR}B\) and \(B^{\prime} = A\mathrm{AND}B\) .Show that the output now has an entropy of \(\frac{3}{2}\) bits. What is the crucial difference between the two logic gates?

(15.3) Maximize the Shannon entropy \(S = - k\sum_{i}P_{i}\log P_{i}\) subject to the constraints that \(\sum P_{i} = 1\) and \(\langle f(x)\rangle = \sum P_{i}f(x_{i})\) and show that

\[\begin{array}{rcl}{P_{i}} & = & {\frac{1}{Z(\beta)}\mathrm{e}^{-\beta f(x_{i})},}\\ {Z(\beta)} & = & {\sum \mathrm{e}^{-\beta f(x_{i})},}\\ {\langle f(x)\rangle} & = & {-\frac{\mathrm{d}}{\mathrm{d}\beta}\ln Z(\beta).} \end{array} \quad (15.28)\]

(15.4) Noise in a communication channel flips bits at random with probability \(P\) .Argue that the entropy

associated with this process is

\[S = -P\log P - (1 - P)\log (1 - P). \quad (15.29)\]

It turns out that the rate \(R\) at which we can pass information along this noisy channel is \(1 - S\) .(This is an application of Shannon's noisy channel coding theorem, and a nice proof of this theorem is given on page 548 of Nielsen and Chuang (2000).)

(15.5) (a) The relative entropy measures the closeness of two probability distributions \(P\) and \(Q\) and is defined by

\[S(P||Q) = \sum P_{i}\log \left(\frac{P_{i}}{Q_{i}}\right) = -S_{p} - \sum P_{i}\log Q_{i}, \quad (15.30)\]

where \(S_{p} = - \sum P_{i}\log P_{i}\) .Show that \(S(P||Q)\geq 0\) with equality if and only if \(P_{i} = Q_{i}\) for all \(i\)

(b) If \(i\) takes \(N\) values with probability \(P_{i}\) then show that

\[S(P||Q) = -S_{P} + \log N, \quad (15.31)\]

where \(Q_{i} = 1 / N\) for all \(i\) .Hence show that

\[S_{P}\leq \log N, \quad (15.32)\]

with equality if and only if \(P_{i}\) is uniformly distributed between all \(N\) outcomes.

(15.6) In a TV game show, a contestant is shown three closed doors. Behind one of the doors is a shiny expensive sports car, but behind the other two are goats. The contestant chooses one of the doors at random (she has, after all, a one- in- three chance of winning the car). The game show host (who knows where the car is really located) flings open one of the other two doors to reveal a goat. He grins at the contestant and says: "Well done, you didn't pick the goat behind this door." (Audience applauds sycophantically.) He then adds, still grinning: "But do you want to swap and choose the other closed door or stick with your original choice?" What should she do?

===== Page 189 =====

This page intentionally left blank

===== Page 190 =====

1

## Part VI

## Thermodynamics in action

In this part we use the laws of thermodynamics developed in Part V to solve real problems in thermodynamics. Part VI is structured as follows:

In Chapter 16 we derive various functions of state, called thermodynamic potentials, in particular the enthalpy, Helmholtz function and Gibbs function, and show how they can be used to investigate thermodynamic systems under various constraints. We introduce the Maxwell relations, which allow us to relate various partial differentials in thermal physics. In Chapter 17 we show that the results derived so far can be extended straightforwardly to a variety of different thermodynamic systems other than the ideal gas. In Chapter 18 we introduce the third law of thermodynamics, which is really an addendum to the second law, and explain some of its consequences.

===== Page 191 =====

16 Thermodynamic potentials

16.1 Internal energy, \(U\) 17216.2 Enthalpy, \(H\) 17316.3 Helmholtz function, \(F\) 17416.4 Gibbs function, \(G\) 17516.5 Constraints 17616.6 Maxwell's relations 179Chapter summary 187Exercises 187

The internal energy \(U\) of a system is a function of state, which means that a system undergoes the same change in \(U\) when we move it from one equilibrium state to another, irrespective of which route we take through parameter space. This makes \(U\) a very useful quantity, though not a uniquely useful quantity. In fact, we can make a number of other functions of state, simply by adding to \(U\) various other combinations of the functions of state \(p\) , \(V\) , \(T\) , and \(S\) in such a way as to give the resulting quantity the dimensions of energy. These new functions of state are called thermodynamic potentials, and examples include \(U + TS\) , \(U - pV\) , \(U + 2pV - 3TS\) . However, most thermodynamic potentials that one could pick are really not very useful (including the ones we've just quoted as examples!) but three of them are extremely useful and are given special symbols: \(H = U + pV\) , \(F = U - TS\) and \(G = U + pV - TS\) . In this chapter, we will explore why these three quantities are so useful. First, however, we will review some properties concerning the internal energy \(U\) .

## 16.1 Internal energy, \(U\)

Let us review the results concerning the internal energy that were derived in Section 14.3. Changes in the internal energy \(U\) of a system are given by the first law of thermodynamics written in the form (eqn 14.17):

\[\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V. \quad (16.1)\]

See Section 14.3.

This equation shows that the natural variables \(^1\) to describe \(U\) are \(S\) and \(V\) , since changes in \(U\) are due to changes in \(S\) or \(V\) . Hence we write \(U = U(S,V)\) to show that \(U\) is a function of \(S\) and \(V\) . Moreover, if \(S\) and \(V\) are held constant for the system, then

\[\mathrm{d}U = 0, \quad (16.2)\]

which is the same as saying that \(U\) is a constant. Equation 16.1 implies that the temperature \(T\) can be expressed as a differential of \(U\) using

\[T = \left(\frac{\partial U}{\partial S}\right)_V, \quad (16.3)\]

and similarly the pressure \(p\) can be expressed as

\[p = -\left(\frac{\partial U}{\partial V}\right)_S. \quad (16.4)\]

===== Page 192 =====

16.2 Enthalpy, \(H\) 173

We also have that for isochoric processes (where isochoric means that \(V\) is constant),

\[\mathrm{d}U = T\mathrm{d}S, \quad (16.5)\]

and for reversible2 isochoric processes

\[\mathrm{d}U = \mathrm{d}Q_{\mathrm{rev}} = C_V\mathrm{d}T, \quad (16.6)\]

and hence

\[\Delta U = \int_{T_1}^{T_2}C_V\mathrm{d}T. \quad (16.7)\]

This is only true for systems held at constant volume; we would like to be able to extend this to systems held at constant pressure (an easier constraint to apply experimentally), and this can be achieved using the thermodynamic potential called enthalpy, which we describe next.

## 16.2 Enthalpy, \(H\)

We define the enthalpy \(H\) by

\[H = U + PV. \quad (16.8)\]

This definition together with eqn 16.1 implies that

\[\begin{array}{rcl}{\mathrm{d}H} & = & {T\mathrm{d}S - p\mathrm{d}V + p\mathrm{d}V + V\mathrm{d}p}\\ {} & = & {T\mathrm{d}S + V\mathrm{d}p.} \end{array} \quad (16.9)\]

The natural variables for \(H\) are thus \(S\) and \(p\) , and we have that \(H = H(S,p)\) . We can therefore immediately write down that for a isobaric (i.e., constant pressure) process,

\[\mathrm{d}H = T\mathrm{d}S, \quad (16.10)\]

and for a reversible isobaric process

\[\mathrm{d}H = \mathrm{d}Q_{\mathrm{rev}} = C_p\mathrm{d}T, \quad (16.11)\]

so that

\[\Delta H = \int_{T_1}^{T_2}C_p\mathrm{d}T. \quad (16.12)\]

This shows the importance of \(H\) , that for reversible isobaric processes the enthalpy represents the heat absorbed by the system.3 Isobaric conditions are relatively easy to obtain: an experiment that is open to the air in a laboratory is usually at constant pressure since pressure is provided by the atmosphere.4 We also conclude from eqn 16.9 that if both \(S\) and \(p\) are constant, we have that \(\mathrm{d}H = 0\)

Equation 16.9 also implies that

\[T = \left(\frac{\partial H}{\partial S}\right)_p, \quad (16.13)\]

2For a reversible process, \(\mathrm{d}Q = T\mathrm{d}S\) see Section 14.3.

3If you add heat to the system at constant pressure, the enthalpy \(H\) of the system goes up. If heat is provided by the system to its surroundings \(H\) goes down.

4At a given latitude, the atmosphere provides a constant pressure, small changes due to weather fronts notwithstanding.

===== Page 193 =====

174 Thermodynamic potentials

and

\[V = \left(\frac{\partial H}{\partial p}\right)_S. \quad (16.14)\]

Both \(U\) and \(H\) suffer from the drawback that one of their natural variables is the entropy \(S\) , which is not a very easy parameter to vary in a lab. It would be more convenient if we could substitute that for the temperature \(T\) , which is, of course, a much easier quantity to control and to vary. This is accomplished for both of our next two functions of state, the Helmholtz and Gibbs functions.

## 16.3 Helmholtz function, \(F\)

We define the Helmholtz function using

\[F = U - TS. \quad (16.15)\]

Hence we find that

\[\begin{array}{rcl}{\mathrm{d}F} & = & {T\mathrm{d}S - p\mathrm{d}V - T\mathrm{d}S - S\mathrm{d}T}\\ {} & = & {- S\mathrm{d}T - p\mathrm{d}V.} \end{array} \quad (16.16)\]

This implies that the natural variables for \(F\) are \(V\) and \(T\) , and we can therefore write \(F = F(T,V)\) . For an isothermal process (constant \(T\) ), we can simplify eqn 16.16 further and write that

\[\mathrm{d}F = -p\mathrm{d}V, \quad (16.17)\]

and hence

\[\Delta F = -\int_{V_1}^{V_2}pdV. \quad (16.18)\]

Hence a positive change in \(F\) represents reversible work done on the system by the surroundings, while a negative change in \(F\) represents reversible work done on the surroundings by the system. As we shall see in Section 16.5, \(F\) represents the maximum amount of work you can get out of a system at constant temperature, since the system will do work on its surroundings until its Helmholtz function reaches a minimum. Equation 16.16 implies that the entropy \(S\) can be written as

\[S = -\left(\frac{\partial F}{\partial T}\right)_V, \quad (16.19)\]

and the pressure \(p\) as

\[p = -\left(\frac{\partial F}{\partial V}\right)_T. \quad (16.20)\]

If \(T\) and \(V\) are constant, we have that \(\mathrm{d}F = 0\) and \(F\) is a constant.

===== Page 194 =====

16.4 Gibbs function, \(G\)

We define the Gibbs function using

\[G = H - TS. \quad (16.21)\]

Hence we find that

\[\begin{array}{rcl}{\mathrm{d}G} & = & {T\mathrm{d}S + V\mathrm{d}p - T\mathrm{d}S - S\mathrm{d}T}\\ {} & = & {- S\mathrm{d}T + V\mathrm{d}p,} \end{array} \quad (16.22)\]

and the natural variables of \(G\) are \(T\) and \(p\) . [Hence we can write \(G = G(T,p)\) .]

Having \(T\) and \(p\) as natural variables is particularly convenient as \(T\) and \(p\) are the easiest quantities to manipulate and control for most experimental systems. In particular, note that if \(T\) and \(p\) are constant, \(\mathrm{d}G = 0\) . Hence \(G\) is conserved in any isothermal isobaric process. \(^5\)

The expression in eqn 16.22 allows us to write down expressions for entropy and volume as follows:

\[S = -\left(\frac{\partial G}{\partial T}\right)_p \quad (16.23)\]

and

\[V = \left(\frac{\partial G}{\partial p}\right)_T. \quad (16.24)\]

\(^5\) For example, at a phase transition between two different phases (call them phase 1 and phase 2), there is phase coexistence between the two phases at the same pressure at the transition temperature. Hence the specific Gibbs functions (the Gibbs functions per unit mass) for phase 1 and phase 2 must be equal at the phase transition. This will be particularly useful for us in Chapter 28.

We have now defined the four main thermodynamic potentials, which are useful in much of thermal physics: the internal energy \(U\) , the enthalpy \(H\) , the Helmholtz function \(F\) , and the Gibbs function \(G\) . Before proceeding further, we summarize the main equations which we have used so far.


<table>Function of stateDifferentialNatural variablesFirst derivativesInternal energyUdU = TdS - pdVU = U(S, V)T = (∂U/∂S)V,EnthalpyH = U + pVdH = TdS + VdpH = H(S, p)T = (∂H/∂S)p,Helmholtz functionF = U - TSdF = -SdT - pdVF = F(T, V)S = - (∂F/∂T)V,Gibbs functionG = H - TSdG = -SdT + VdpG = G(T, p)S = - (∂G/∂T)p,</table>

Note that to derive these equations quickly, all you need to do is memorize the definitions of \(H\) , \(F\) and \(G\) and the first law in the form \(\mathrm{d}U = T\mathrm{d}S - p\mathrm{d}V\) and the rest can be written down straightforwardly.

===== Page 195 =====

6A further weakness with the “internal energy”, which will become apparent later, is that it is only for a box of gas that it is obvious what “internal” means. For a box of gas, internal energy clearly means that energy which is inside the gas, associated with the molecules in the gas. However, if the thermodynamic system is a magnetic material in a magnetic field, should “internal energy” only mean energy inside the magnetic material, or should it also include the field energy in the surroundings or associated with the coil causing the magnetic field? We return to this issue in Chapter 17.

## Example 16.1

Show that \(U = - T^{2}\left(\frac{\partial}{\partial T}\right)_{V}\frac{F}{T}\) and \(H = - T^{2}\left(\frac{\partial}{\partial T}\right)_{p}\frac{G}{T}\) .

Solution:

Using the expressions

\[S = -\left(\frac{\partial F}{\partial T}\right)_V\qquad \mathrm{and}\qquad S = -\left(\frac{\partial G}{\partial T}\right)_p,\]

we can write down

\[U = F + TS = F - T\left(\frac{\partial F}{\partial T}\right)_V = -T^2\left(\frac{\partial(F / T)}{\partial T}\right)_V \quad (16.25)\]

and

\[H = G + TS = G - T\left(\frac{\partial G}{\partial T}\right)_p = -T^2\left(\frac{\partial(G / T)}{\partial T}\right)_p. \quad (16.26)\]

These equations are known as the Gibbs- Helmholtz equations and are useful in chemical thermodynamics.

## 16.5 ConstraintsWe have seen that the thermodynamic potentials are valid functions of state and have particular properties. But we have not yet seen how they might be useful, and there might be a suspicion lurking that \(H\) , \(F\) , and \(G\) are rather artificial objects whereas \(U\) , the internal energy, is the only natural one. This is not the case, as we shall now show. However, which of these functions of state is the most useful one depends on the context of the problem, and in particular on the type of constraint that is applied to the system.

Consider a large mass sitting on the top of a cliff, near the edge. This system has the potential to provide useful work, since one could connect the mass to a pulley system, lower the mass down the cliff edge and extract mechanical work. When the mass lies at the bottom of the cliff, no more useful work can be obtained. It would be very useful to have a quantity that depends on the amount of available useful work a system can provide, and we call such a quantity the free energy. In working out what the free energy is in any particular situation, we have to remember that a system can exchange energy with its surroundings, and how it does that rather depends on what sort of constraint the surroundings apply to the system. We shall first demonstrate this using a particular case, and then proceed to the general case.

Consider first a system with fixed volume, held at a temperature \(T\) by its contact with the surroundings. If heat \(\mathrm{d}Q\) enters the system,

===== Page 196 =====

16.5 Constraints 177

the entropy \(S_{0}\) of the surroundings changes by \(\mathrm{d}S_{0} = - \mathrm{d}Q / T\) and the change in entropy of the system, \(\mathrm{d}S\) , must be such that the total change in entropy of the Universe must be greater than, or equal to, zero (i.e., \(\mathrm{d}S + \mathrm{d}S_{0}\geq 0\) ). Hence \(\mathrm{d}S - \mathrm{d}Q / T\geq 0\) and so \(T\mathrm{d}S\geq \mathrm{d}Q\) . Now by the first law, \(\mathrm{d}Q = \mathrm{d}U - \mathrm{d}W\) and so the work added to the system must satisfy

\[\mathrm{d}W\geq \mathrm{d}U - T\mathrm{d}S. \quad (16.27)\]

Now since \(T\) is fixed, \(\mathrm{d}F = \mathrm{d}(U - TS) = \mathrm{d}U - T\mathrm{d}S\) , and hence eqn 16.27 can be written

\[\mathrm{d}W\geq \mathrm{d}F. \quad (16.28)\]

What we have shown is that adding work to the system increases the system's Helmholtz function (which we may now call a Helmholtz free energy \(^7\) ). In a reversible process, \(\mathrm{d}W = \mathrm{d}F\) and the work added to the system goes directly into an increase of Helmholtz free energy. If we extract a certain amount of work from the system \((\mathrm{d}W< 0)\) , then this will be associated with at least as big a drop in the sample's Helmholtz free energy (equality only being obtained in a reversible process). Returning to our analogy, adding work to the system hauls the mass up to the top of the cliff and gives it the potential to do work in the future (adding free energy to the system), extracting work from the system occurs by letting the mass drop down the cliff and reduces its potential to provide work in the future (subtracting free energy from the system).

Another example is a quantity of oil, which stores free energy that can be released when the oil is burned. However, how that free energy is defined depends on how the oil is burned. If it burns inside a sealed drum containing only oil and air, then the combustion will take place in a fixed volume. In this case, the relevant free energy is the Helmholtz function, as above. However, if the oil is burned in the open air, then the combustion products will need to push against the atmosphere and the free energy will be the Gibbs function, \(^8\) as we shall show.

Note that if the system is mechanically isolated from its surroundings, so that no work can be applied or extracted, then \(\mathrm{d}W = 0\) and eqn 16.28 becomes

\[\mathrm{d}F\leq 0. \quad (16.29)\]

Thus any change in \(F\) will be negative. As the system settles down towards equilibrium, all processes will tend to force \(F\) downwards. Once the system has reached equilibrium, \(F\) will be constant at this minimum level. Hence equilibrium can only be achieved by minimizing \(F\) .

We now need to repeat the argument we used to justify eqns 16.28 and 16.29 for more general constraints. In general, a system is able to exchange heat with its surroundings and also, if the system's volume changes, it may do work on its surroundings. Let us now consider a system in contact with surroundings at temperature \(T_{0}\) and pressure \(p_{0}\) (see Fig. 16.1). As described above, if heat \(\mathrm{d}Q\) enters the system, the entropy change of the system satisfies \(T_{0}\mathrm{d}S\geq \mathrm{d}Q\) . In the general case, we write the first law as

\[\mathrm{d}Q = \mathrm{d}U - \mathrm{d}W - (-p_0\mathrm{d}V), \quad (16.30)\]

7 This is because useful work could be extracted back out again, and hence it is a free energy in the sense we have defined.

8 For this example, the constraint applied by the atmosphere is the fixing of pressure.

[Image: A diagram showing a system (white box) surrounded by surroundings (grey area) at temperature T0 and pressure p0.]
Fig. 16.1 A system in contact with surroundings at temperature \(T_{0}\) and pressure \(p_{0}\) .

===== Page 197 =====

178 Thermodynamic potentials

where we have explicitly separated the mechanical work \(\mathrm{d}W\) added to the system from the work \(- p_0\mathrm{d}V\) done by the surroundings due to the volume change of the system. Putting this all together gives

\[\mathrm{d}W\geq \mathrm{d}U + p_0\mathrm{d}V - T_0\mathrm{d}S. \quad (16.31)\]

We now define the availability \(A\) by

\[A = U + p_0V - T_0S, \quad (16.32)\]

and because \(p_0\) and \(T_0\) are constants, we have

\[\mathrm{d}A = \mathrm{d}U + p_0\mathrm{d}V - T_0\mathrm{d}S. \quad (16.33)\]

Hence eqn 16.31 becomes

\[\mathrm{d}W\geq \mathrm{d}A, \quad (16.34)\]

which generalizes eqn 16.28. Changes in availability provide free energy "available" for doing work. \(A\) will change its form depending on the type of constraint, as shown below. First, note that just as we found eqn 16.29 for the specific case of fixed \(V\) and \(T\) , in the general case the availability can be used to express a general minimization principle. If the system is mechanically isolated, then

\[\mathrm{d}A\leq 0, \quad (16.35)\]

which generalizes eqn 16.29. We have derived this inequality from the second law of thermodynamics. It demonstrates that changes in \(A\) are always negative. All processes will tend to force \(A\) downwards towards a minimum value. Once the system has reached equilibrium, \(A\) will be constant at this minimum level. Hence equilibrium can only be achieved by minimizing \(A\) . However, the type of equilibrium achieved depends on the nature of the constraints, as we will now show.

System thermally isolated and with fixed volume: Since no heat can enter the system and the system can do no work on its surroundings, \(\mathrm{d}U = 0\) .Hence eqn 16.33 becomes \(\mathrm{d}A = - T_0\mathrm{d}S\) and therefore \(\mathrm{d}A\leq 0\) implies that \(\mathrm{d}S\geq 0\) .Thus we must maximize \(S\) to find the equilibrium state.

System with fixed volume at constant temperature: \(\mathrm{d}A = \mathrm{d}U - T_0\mathrm{d}S\leq 0\) but the temperature is fixed, \(\mathrm{d}T = 0\) ,and so \(\mathrm{d}F = \mathrm{d}U - T_0\mathrm{d}S - S\mathrm{d}T = \mathrm{d}U - T_0\mathrm{d}S\) ,leading to

\[\mathrm{d}A = \mathrm{d}F\leq 0, \quad (16.36)\]

so we must minimize \(F\) to find the equilibrium state.9

System at constant pressure and temperature:

Eqn 16.33 gives \(\mathrm{d}A = \mathrm{d}U - T_0\mathrm{d}S + p_0\mathrm{d}V\leq 0\) .We can write dG (from the definition \(G = H - TS\) )as

\[\mathrm{d}G = \mathrm{d}U + p_0\mathrm{d}V + V\mathrm{d}p - T_0\mathrm{d}S - S\mathrm{d}T = \mathrm{d}U - T_0\mathrm{d}S + p_0\mathrm{d}V, \quad (16.37)\]

(16.37)

(16.37)

(16.37)

(16.37)

(16.37)

(16.37)

===== Page 198 =====

16.6 Maxwell's relations 179

## Example 16.2

Chemistry laboratories are usually at constant pressure. If a chemical reaction is carried out at constant pressure, then by eqn 16.11 we have

\[\Delta H = \Delta Q, \quad (16.39)\]

and hence \(\Delta H\) is the reversible heat added to the system, i.e., the heat absorbed by the reaction. (Recall that our convention is that \(\Delta Q\) is the heat entering the system, and in this case the system is the reacting chemicals.)

If \(\Delta H< 0\) the reaction is called exothermic and heat will be emitted. If \(\Delta H > 0\) the reaction is called endothermic and heat will be absorbed.

However, this does not tell you whether or not a chemical reaction will actually proceed. Usually reactions occur at constant \(T\) and \(p\) so if the system is trying to minimize its availability, then we need to consider \(\Delta G\) . The second law of thermodynamics (via eqn 16.35 and hence eqn 16.38) therefore implies that a chemical system will minimize \(G\) so that if \(\Delta G< 0\) the reaction may spontaneously occur.12

11The temperature may rise during a reaction, but if the final products cool to the original temperature, one only needs to think about the beginning and end points, since \(G\) is a function of state.

12However, one may also need to consider the kinetics of the reaction. Often a reaction has to pass via a metastable intermediate state, which may have a higher Gibbs function, so the system cannot spontaneously lower its Gibbs function without having it slightly raised first. This gives a reaction an activation energy that must be added before the reaction can proceed, even though the completion of the reaction gives you all that energy back and more.

## 16.6 Maxwell's relations

In this section, we are going to derive four equations, which are known as Maxwell's relations. These equations are very useful in solving problems in thermodynamics, since each one relates a partial differential between quantities that can be hard to measure to a partial differential between quantities that can be much easier to measure. The derivation proceeds along the following lines: a state function \(f\) is a function of variables \(x\) and \(y\) . A change in \(f\) can be written as

\[\mathrm{d}f = \left(\frac{\partial f}{\partial x}\right)_y\mathrm{d}x + \left(\frac{\partial f}{\partial y}\right)_x\mathrm{d}y. \quad (16.40)\]

Because df is an exact differential (see Appendix C.7), we have

\[\left(\frac{\partial^2f}{\partial x\partial y}\right) = \left(\frac{\partial^2f}{\partial y\partial x}\right). \quad (16.41)\]

Hence writing

\[F_{x} = \left(\frac{\partial f}{\partial x}\right)_{y}\mathrm{and}F_{y} = \left(\frac{\partial f}{\partial y}\right)_{x}, \quad (16.42)\]

we have

\[\left(\frac{\partial F_y}{\partial x}\right) = \left(\frac{\partial F_x}{\partial y}\right). \quad (16.43)\]

===== Page 199 =====

 We can now apply this idea to each of the state variables \(U\) , \(H\) , \(F\) , and \(G\) in turn.

## Example 16.3

The Maxwell relation based on \(G\) can be derived as follows. We write down an expression for \(\mathrm{d}G\) :

\[\mathrm{d}G = -S\mathrm{d}T + V\mathrm{d}p. \quad (16.44)\]

We can also write

\[\mathrm{d}G = \left(\frac{\partial G}{\partial T}\right)_p\mathrm{d}T + \left(\frac{\partial G}{\partial p}\right)_T\mathrm{d}p, \quad (16.45)\]

and hence we can write \(S = - (\partial G / \partial T)_p\) and \(V = (\partial G / \partial p)_T\) . Because \(\mathrm{d}G\) is an exact differential, we have

\[\left(\frac{\partial^2G}{\partial T\partial p}\right) = \left(\frac{\partial^2G}{\partial p\partial T}\right), \quad (16.46)\]

and hence we have the following Maxwell relation:

\[-\left(\frac{\partial S}{\partial p}\right)_T = \left(\frac{\partial V}{\partial T}\right)_p. \quad (16.47)\]

This reasoning can be applied to each of the thermodynamic potentials \(U\) , \(H\) , \(F\) , and \(G\) to yield the four Maxwell's relations:

Maxwell's relations:

\[\begin{array}{rcl}\left(\frac{\partial T}{\partial V}\right)_S & = & -\left(\frac{\partial p}{\partial S}\right)_V\\ \left(\frac{\partial T}{\partial p}\right)_S & = & \left(\frac{\partial V}{\partial S}\right)_p\\ \left(\frac{\partial S}{\partial V}\right)_T & = & \left(\frac{\partial p}{\partial T}\right)_V\\ \left(\frac{\partial S}{\partial p}\right)_T & = & -\left(\frac{\partial V}{\partial T}\right)_p \end{array} \quad (16.50)\]

We have said that Maxwell's relations relate a partial differential that corresponds to something that can be easily measured to a partial differential that cannot. For example, in eqn 16.51 the term \((\partial V / \partial T)_p\) on the right- hand side tells you how the volume changes as you increase the temperature while keeping the pressure fixed. This is related to a quantity called the isobaric expansivity \(^{13}\) and is a quantity you can easily imagine being something one could measure in a laboratory. However, the term on the left- hand side of eqn 16.51, \((\partial S / \partial p)_T\) , is much more

===== Page 200 =====

16.6 Maxwell's relations 181

mysterious and it is not obvious how a change of entropy with pressure at constant temperature could actually be measured. Fortunately, a Maxwell relation relates it to something which can be.

Maxwell's relations should not be memorized;14 rather it is better to remember how to derive them!

A more sophisticated way of deriving these equations based on Jacobians (which may not be to everybody's taste) is outlined in the box below. It has the attractive virtue of producing all four relations in one go by directly relating the work done and heat absorbed in a cyclic process, but the unfortunate vice of requiring easy familiarity with the use of Jacobian transformations.

## An alternative derivation of Maxwell's relations

The following derivation is more elegant, but requires a knowledge of Jacobians (see Appendix C.9). Consider a cyclic process that can be described in both the \(T - S\) and \(p - V\) planes. The internal energy \(U\) is a state function and therefore doesn't change in a cycle, so \(\oint \mathrm{d}U = 0\) which implies that \(\oint p\mathrm{d}V = \oint T\mathrm{d}S\) , and hence

\[\int \int \mathrm{d}p\mathrm{d}V = \int \int \mathrm{d}T\mathrm{d}S. \quad (16.52)\]

This says that the work done (the area enclosed by the cycle in the \(p - V\) plane) is equal to the heat absorbed (the area enclosed by the cycle in the \(T - S\) plane). However, one can also write

\[\int \int \mathrm{d}p\mathrm{d}V\frac{\partial(T,S)}{\partial(p,V)} = \int \int \mathrm{d}T\mathrm{d}S, \quad (16.53)\]

where \(\partial (T,S) / \partial (p,V)\) is the Jacobian of the transformation from the \(p - V\) plane to the \(T - S\) plane, and so these two equations imply that

\[\frac{\partial(T,S)}{\partial(p,V)} = 1. \quad (16.54)\]

This equation is sufficient to generate all four Maxwell relations via

\[\frac{\partial(T,S)}{\partial(x,y)} = \frac{\partial(p,V)}{\partial(x,y)}, \quad (16.55)\]

where \((x,y)\) are taken as (i) \((T,p)\) , (ii) \((T,V)\) , (iii) \((p,S)\) , and (iv) \((S,V)\) , and using the identities in Appendix C.9.

We will now give several examples of how Maxwell's relations can be used to solve problems in thermodynamics.

===== Page 201 =====

182
Thermodynamic potentials
Example 16.4
Find expressions for (∂Cp/∂p)T and (∂CV /∂V )T in terms of p, V ,
and T.
Solution:
By the definitions of CV and Cp we have that
CV =
�∂Q
∂T
�
V
= T
�∂S
∂T
�
V
(16.56)
and
Cp =
�∂Q
∂T
�
p
= T
�∂S
∂T
�
p
.
(16.57)
Now
�∂Cp
∂p
�
T
=
�
∂
∂pT
�∂S
∂T
�
p
�
T
=
T
�
∂
∂p
�∂S
∂T
�
p
�
T
=
T
�∂
∂T
�∂S
∂p
�
T
�
p
(16.58)
and therefore, using one of the Maxwell’s relations,
�∂Cp
∂p
�
T
= −T
�
∂
∂T
�∂V
∂T
�
p
�
p
= −T
�∂2V
∂T 2
�
p
.
(16.59)
Similarly
�∂CV
∂V
�
T
= T
�∂2p
∂T 2
�
V
.
(16.60)
Both the expressions in eqns 16.59 and 16.60 are zero for a perfect gas.
Before proceeding further with the examples, we will pause to list the
tools which you have at your disposal to solve these sorts of problems.
Any given problem may not require you to use all of these, but you may
have to use more than one of these “techniques”.
(1) Write down a thermodynamic potential in terms of par-
ticular variables.
If f is a function of x and y, so that f = f(x, y), you then have
immediately that
df =
�∂f
∂x
�
y
dx +
�∂f
∂y
�
x
dy.
(16.61)

===== Page 202 =====

16.6
Maxwell’s relations
183
(2) Use Maxwell’s relations to transform the partial differ-
ential you start with into a more convenient one.
Use the Maxwell’s relations in eqns 16.48–16.51.
(3) Invert a Maxwell’s relation using the reciprocal theorem.
The reciprocal theorem states that
�∂x
∂z
�
y
=
1
�∂z
∂x
�
y
,
(16.62)
and this is proved in Appendix C.6 (see eqn C.41).
(4) Combine partial differentials using the reciprocity theo-
rem.
The reciprocity theorem states that
�∂x
∂y
�
z
�∂y
∂z
�
x
�∂z
∂x
�
y
= −1,
(16.63)
which is proved in Appendix C.6 (see eqn C.42).
This can be
combined with the reciprocal theorem to write that
�∂x
∂y
�
z
= −
�∂x
∂z
�
y
�∂z
∂y
�
x
,
(16.64)
which is a very useful identity.
(5) Identify a heat capacity.
Some of the partial differentials appearing in Maxwell’s relations
relate to real, measurable properties. As we have seen in Exam-
ple 16.4, both
�∂S
∂T
�
V and
�∂S
∂T
�
p can be related to heat capacities:
CV
T
=
�∂S
∂T
�
V
and
Cp
T =
�∂S
∂T
�
p
.
(16.65)
(6) Identify a “generalized susceptibility”.
A generalized susceptibility quantifies how much a particular
variable changes when a generalized force is applied. A general-
ized force is a variable such as T or p which is a differential of
the internal energy with respect to some other parameter.15 An
15Recall that T = (∂U/∂S)V and
p = −(∂U/∂V )S.
example of a generalized susceptibility is
�∂V
∂T
�
x which, you will
recall, answers the question “keeping x constant, how much does
the volume change when you change the temperature?” It is re-
lated to the thermal expansivity at constant x, where x is pressure
or entropy. Thus the isobaric expansivity βp is defined as
βp = 1
V
�∂V
∂T
�
p
,
(16.66)
while the adiabatic expansivity βS is defined as
βS = 1
V
�∂V
∂T
�
S
.
(16.67)

===== Page 203 =====

184
Thermodynamic potentials
Expansivities measure the fractional change in volume with a change
in temperature.
Another useful generalized susceptibility is the compressibility.
This quantifies how large a fractional volume change you achieve
when you apply pressure. The isothermal compressibility κT
is defined as
κT = −1
V
�∂V
∂p
�
T
,
(16.68)
while the adiabatic compressibility κS is defined as
κS = −1
V
�∂V
∂p
�
S
.
(16.69)
Both quantities have a minus sign so that the compressibilities are
positive (this is because things get smaller when you press them,
so fractional volume changes are negative when positive pressure is
applied). None of these expansivities or compressibilities appears
directly in a Maxwell relation, but each can easily be related to
those that do using the reciprocal and reciprocity theorems.
Example 16.5
By considering S = S(T, V ), show that Cp −CV = V Tβ2
p/κT .
Solution:
Considering S = S(T, V ) allows us to write down immediately that
dS =
�∂S
∂T
�
V
dT +
�∂S
∂V
�
T
dV.
(16.70)
Differentiating this equation with respect to T at constant p yields
�∂S
∂T
�
p
=
�∂S
∂T
�
V
+
�∂S
∂V
�
T
�∂V
∂T
�
p
.
(16.71)
Now the first two terms can be replaced by Cp/T and CV /T respectively,
while use of a Maxwell’s relation and a partial differential identity (see
eqn 16.64) yields
�∂S
∂V
�
T
=
�∂p
∂T
�
V
= −
�∂p
∂V
�
T
�∂V
∂T
�
p
(16.72)
and hence using eqns 16.66 and 16.68 we have that
Cp −CV = V Tβ2
p
κT
.
(16.73)
The next example shows how to calculate the entropy of an ideal gas.

===== Page 204 =====

16.6
Maxwell’s relations
185
Example 16.6
Find the entropy of 1 mole of ideal gas.
Solution:
For one mole of ideal gas pV = RT. Consider the entropy S as a function
of volume and temperature, i.e.,
S = S(T, V ),
(16.74)
so that
dS
=
�∂S
∂T
�
V
dT +
�∂S
∂V
�
T
dV
(16.75)
=
CV
T dT +
�∂p
∂T
�
V
dV,
(16.76)
using eqn 16.50 and eqn 16.65. The ideal gas law for 1 mole, p = RT/V ,
implies that
�∂p
∂T
�
V
= R/V,
(16.77)
and hence, if we integrate eqn 16.76,
S =
�CV
T dT +
�RdV
V
.
(16.78)
If CV is not a function of temperature (which is true for an ideal gas)
simple integration yields
S = CV ln T + R ln V + constant.
(16.79)
The entropy of an ideal gas increases with increasing temperature and
increasing volume.
The final example in this chapter shows how to prove that the ratio
of the isothermal and adiabatic compressibilities, κT /κS, is equal to γ.
Example 16.7
Find the ratio of the isothermal and adiabatic compressibilities.
Solution:
This follows using straightforward manipulations of partial differentials.
To begin with, we write
κT
κS
=
1
V
�∂V
∂p
�
T
1
V
�∂V
∂p
�
S
,
(16.80)

===== Page 205 =====

186
Thermodynamic potentials
which follows from the definitions of κT and κS (eqns 16.68 and 16.69).
Then we proceed as follows:
κT
κS
=
−
�∂V
∂T
�
p
�∂T
∂p
�
V
−
�∂V
∂S
�
p
�∂S
∂p
�
V
reciprocity theorem (eqn 16.64)
=
�∂V
∂T
�
p
�∂S
∂V
�
p
�∂p
∂T
�
V
�∂S
∂p
�
V
reciprocal theorem (eqn 16.62)
=
�∂S
∂T
�
p
�∂S
∂T
�
V
simplify numerator and denominator
=
Cp/T
CV /T
=
γ.
(16.81)
We can show that this equation is correct for the case of an ideal gas as
follows. Assuming the ideal gas equation pV ∝T, we have for constant
temperature that
dp
p = −dV
V ,
(16.82)
and hence using eqn 16.68 we have
κT = 1
p.
(16.83)
For an adiabatic change p ∝V −γ and hence
dp
p = −γ dV
V ,
(16.84)
and hence using eqn 16.69 we have
κS = 1
γp.
(16.85)
This agrees with eqn 16.81 above. We note that because κT is larger
than κS (because γ > 1), the isotherms always have a smaller gradient
than the adiabats on a p–V plot (see Fig. 12.1).

===== Page 206 =====

Exercises
187
Chapter summary
• We define the following thermodynamic potentials:
U,
H = U + pV,
F = U −TS,
G = H −TS,
which are then related by the following differentials:
dU
=
TdS −pdV
dH
=
TdS + V dp
dF
=
−SdT −pdV
dG
=
−SdT + V dp
• The availability A is given by A = U + p0V −T0S, and for any
spontaneous change we have that dA ≤0.
This means that a
system in contact with a reservoir (temperature T0, pressure p0)
will minimize A which means
– minimizing U when S and V are fixed;
– minimizing H when S and p are fixed;
– minimizing F when T and V are fixed;
– minimizing G when T and p are fixed.
• Four Maxwell’s relations can be derived from the boxed equations
above, and used to solve many problems in thermodynamics.
Exercises
(16.1) (a)
Using the first law dU = TdS −pdV to pro-
vide a reminder, write down the definitions
of the four thermodynamic potentials U, H,
F, G (in terms of U, S, T, p, V ), and give
dU, dH, dF, dG in terms of T, S, p, V and
their derivatives.
(b)
Derive all the Maxwell’s relations.
(16.2) (a)
Derive the following general relations
(i)
„ ∂T
∂V
«
U
=
−1
CV
»
T
„ ∂p
∂T
«
V
−p
–
,
(ii)
„ ∂T
∂V
«
S
=
−1
CV T
„ ∂p
∂T
«
V
,
(iii)
„∂T
∂p
«
H
=
1
Cp
"
T
„∂V
∂T
«
p
−V
#
.
In each case the quantity on the left-hand
side is the appropriate thing to consider for
a particular type of expansion. State what
type of expansion each refers to.
(b)
Using these relations, verify that for an ideal
gas (∂T/∂V )U = 0 and (∂T/∂p)H = 0, and
that (∂T/∂V )S leads to the familiar relation
pV γ = constant along an isentrope (a curve
of constant entropy).
(16.3) Use the first law of thermodynamics to show that
„∂U
∂V
«
T
= Cp −CV
V βp
−p,
(16.86)
where βp is the coefficient of volume expansivity
and the other symbols have their usual meanings.

===== Page 207 =====

188
Exercises
(16.4) (a) The natural variables for U are S and V . This
means that if you know S and V , you can find
U(S, V ). Show that this also gives you simple ex-
pressions for T and p.
(b) Suppose instead that you know V , T and the
function U(T, V ) (i.e., you have expressed U in
terms of variables that are not all the natural vari-
ables of U). Show that this leads to a (much more
complicated) expression for p, namely
p
T =
Z „∂U
∂V
«
T
dT
T 2 + f(V ),
(16.87)
where f(V ) is some (unknown) function of V .
(16.5) Use thermodynamic arguments to obtain the gen-
eral result that, for any gas at temperature T, the
pressure is given by
P = T
„∂P
∂T
«
V
−
„∂U
∂V
«
T
,
(16.88)
where U is the total energy of the gas.
(16.6) Show that another expression for the entropy per
mole of an ideal gas is
S = Cp ln T −R ln p + constant.
(16.89)
(16.7) Show that the entropy of an ideal gas can be ex-
pressed as
S = CV ln
„ p
ργ
«
+ constant.
(16.90)

===== Page 208 =====

Biographies
189
Hermann von Helmholtz (1821–1894)
Since his family couldn’t afford to give him an
academic
education
in
physics,
the
seventeen-
year
old
Helmholtz
found
himself
at
a
Berlin
medical school getting a free four-year medical
education,
the
catch
being
that
he
then
had
to
serve
as
a
surgeon
in
the
Prussian
army.
Fig.
16.2
H.
von
Helmholtz
It was during his army ser-
vice that he submitted a paper
“On the conservation of force”
(his use of the word “force”
is more akin to what we call
“energy”, the two concepts be-
ing poorly differentiated at the
time).
It was a blow against
the notion of a “vital force”,
an indwelling “life source” which
was widely proposed by physiol-
ogists to explain biological sys-
tems.
Helmholtz intuited that
such a vital force was mere metaphysical speculation
and instead all physical and chemical processes in-
volved the exchange of energy from one form to an-
other, and that “all organic processes are reducible to
physics”. Thus he began a remarkable career based
on his remarkable physical insight into physiology.
In 1849 he was appointed professor of physiology
at K¨onigsberg, and six years later took up a profes-
sorship in anatomy in Bonn, moving to Heidelberg
three years later. During this period he pioneered the
application of physical and mathematical techniques
to physiology: he invented the opthalmoscope (for
looking into the eye), the opthalmometer (for mea-
suring the curvature and refractive errors in the eye)
and worked on the problem of three-colour vision; he
did pioneering research in physiological acoustics, ex-
plaining the operation of the inner ear; he also mea-
sured the speed of nerve impulses in a frog.
He even found time to make important contribu-
tions to understanding vortices in fluids.
In 1871,
he was appointed to a chair in Berlin, but this time
it was in physics; here he pursued work in elec-
trodynamics, non-Euclidean geometry and physical
chemistry. Helmholtz mentored and influenced many
highly talented students in Berlin, including Planck,
Wien, and Hertz.
Helmholtz’s scientific life was characterized by a
search for unity and clarity. He once said that “who-
ever in the pursuit of science, seeks after immediate
practical utility may rest assured that he seeks in
vain”, but there can be only few scientists in history
whose work has had the result of greater practical
utility.
William Thomson [Lord Kelvin] (1824–1907)
William Thomson was something of a prodigy:
Fig.
16.3
William
Thomson
born in Belfast, the son of a
mathematician, he studied in
Glasgow University and then
moved
to
Peterhouse,
Cam-
bridge.
By the time he had
graduated, he had written 12 re-
search papers, the first of the
661 of his career.
He became
Professor of Natural Philosophy
in the University of Glasgow at
22, a Fellow of the Royal Society
at 27, was knighted at 42, and
in 1892 became Baron Kelvin of
Largs (taking his new title from
the River Kelvin in Glasgow), an appointment that
occurred during his presidency of the Royal Society.
When he died, he was buried next to Isaac Newton
in Westminster Abbey.
Thomson made pioneering contributions in fun-
damental electromagnetism and fluid dynamics, but
also involved himself in large engineering projects.
After working out how to solve the problem of send-
ing signals down very long cables, he was involved
in laying the first transatlantic telegraph cables in
1866. In 1893, he headed an international commis-
sion to plan the design of the Niagara Falls power
station and was convinced by Nikola Tesla, somewhat
against his better judgement, to use three-phase AC
power rather than his preferred DC power transmis-
sion.
On this point he was unable to forecast the
future (which was of course AC, not DC); in simi-
lar vein, he pronounced heavier-than-air flying ma-
chines “impossible”, thought that radio had “no fu-

===== Page 209 =====

190
Biographies
ture”, and that war, as a “relic of barbarism” would
“become as obsolete as duelling”. If only.
It is his progress in thermodynamics that interests
us here.
Inspired by the meticulous thermometric
measurements of Henri Regnault, which he had ob-
served during a postgraduate stay in Paris, Thom-
son proposed an absolute temperature scale in 1848.
Thomson was also profoundly influenced by Fourier’s
theory of heat (which he had read in his teens) and
Carnot’s work via the paper of Clapeyron. These had
assumed a caloric theory of heat, which Thomson had
initially adopted, but his encounter with Joule at the
1847 British Association meeting in Oxford had sown
some seeds of doubt in caloric. After much thought,
Thomson groped his way towards his “dynamical the-
ory of heat”, which he published in 1851, a synthe-
sis of Joule and Carnot, containing a description of
the degradation of energy and speculations about the
heat death of the Universe.
He just missed a full
articulation of the concept of entropy, but grasped
the essential details of the first and second laws of
thermodynamics. His subsequent fruitful collabora-
tion with Joule led to the Joule–Thomson (or Joule–
Kelvin) effect.
Thomson also discovered many key results concern-
ing thermoelectricity. His most controversial result
was however his estimate of the age of the Earth,
based on Fourier’s thermal diffusion equation.
He
concluded that if the Earth had originally been a red-
hot globe, and had cooled to its present temperature,
its age must be about 108 years. This pleased no-
body: the Earth was too old for those who believed
in a six-thousand year old planet but too young for
Darwin’s evolution to produce the present biological
diversity. Thomson could not have known that ra-
dioactivity (undiscovered until the very end of the
nineteenth century) acts as an additional heat source
in the Earth, allowing the Earth to be nearly two
orders of magnitude older than he estimated.
His
lasting legacy however has been his new temperature
scale, so that his “absolute zero”, the lowest possible
temperature obtainable, is zero kelvin.
Josiah Willard Gibbs (1839–1903)
Willard
Gibbs
was
born
in
New
Haven
and
died
in
New
Haven,
living
his
entire
life
Fig.
16.4
J. W.
Gibbs
(a brief postdoctoral period in
France and Germany excepted)
at Yale, where he remained un-
married.
His father was also
called Josiah Willard Gibbs and
had also been a professor at
Yale, though in Sacred Litera-
ture rather than in Mathematical
Physics.
Willard Gibbs’
life was quiet and secluded, well
away from the centres of intense
scientific activity at the time,
which were all in Europe. This
gave this gentle and scholarly
man the opportunity to perform
clear-thinking, profound and in-
dependent work in chemical thermodynamics, work
which turned out to be completely revolutionary,
though this took time to be appreciated.
Willard
Gibbs’ key papers were published in a series of in-
stallments in the Transactions of the Connecticut
Academy of Sciences, which was hardly required
reading at the time; moreover his mathematical style
did not make his papers easily accessible. Maxwell
was one of the few who were very impressed.
Gibbs established the key principles of chemical
thermodynamics, defined the free energy and chem-
ical potential, completely described phase equilibria
with more than one component and championed a
geometric view of thermodynamics. Not only did he
substantially formulate thermodynamics and statis-
tical mechanics in the form we know it today, but
he also championed the use of vector calculus, in its
modern form, to describe electromagnetism (in the
face of spirited opposition from various prominent
Europeans who maintained that the only way to de-
scribe electromagnetism was using quaternions).
Gibbs didn’t interact a great deal with scientific
colleagues in other institutions; he was privately se-
cure in himself and in his ideas. One contemporary
wrote of him: “Unassuming in manner, genial and
kindly in his intercourse with his fellow men, never
showing impatience or irritation, devoid of personal
ambition of the baser sort or of the slightest desire to
exalt himself, he went far toward realizing the ideal
of the unselfish, Christian gentleman”.

===== Page 210 =====

17
Rods, bubbles, and
magnets
17.1 Elastic rod
191
17.2 Surface tension
194
17.3 Electric
and
magnetic
dipoles
195
17.4 Paramagnetism
196
Chapter summary
200
Exercises
201
In this book, we have been illustrating the development of thermody-
namics using the ideal gas as our chief example. We have written the
first law of thermodynamics as
dU = T dS −p dV,
(17.1)
and everything has followed from this. However, in this chapter we want
to show that thermodynamics can be applied to other types of system.
In general we will write the work ¯dW as
¯dW = X dx,
(17.2)
where X is some (intensive1) generalized force and x is some (extensive)
1Recall from Section 11.1.2 that inten-
sive variables are independent of the
size of the system whereas extensive
variables are proportional to the size of
the system.
generalized displacement. Examples of these are given in Table 17.1. In
this chapter we will examine only three of these examples in detail: the
elastic rod, the surface tension in a liquid and the assembly of magnetic
moments in a paramagnet.
X
x
¯dW
fluid
−p
V
−p dV
elastic rod
f
L
f dL
liquid film
γ
A
γ dA
dielectric
E
pE
−pE · dE
magnetic
B
m
−m · dB
Table 17.1 Generalized force X and generalized displacement x for various different
systems. In this table, p = pressure, V = volume, f = tension, L = length, γ = surface
tension, A = area, E = electric field, pE = electric dipole moment, B = magnetic field,
m= magnetic dipole moment.
Fig. 17.1 An elastic material of length
L and cross-sectional area A is ex-
tended a length dL by a tension df.
17.1
Elastic rod
Consider a rod with cross-sectional area A and length L, held at tem-
perature T. The rod is made from any elastic material (such as a metal

===== Page 211 =====

192
Rods, bubbles, and magnets
or rubber) and is placed under an infinitesimal tension df, which leads
to the rod extending by an infinitesimal length dL (see Fig. 17.1). We
define the isothermal Young’s modulus ET as the ratio of stress
σ = df/A to strain ϵ = dL/L, so that
ET = σ
ϵ = L
A
�∂f
∂L
�
T
.
(17.3)
The Young’s modulus ET is always a positive quantity.
There is another useful quantity that characterizes an elastic rod. We
can also define the linear expansivity at constant tension, αf, by
αf = 1
L
�∂L
∂T
�
f
,
(17.4)
which is the fractional change in length with temperature. This quantity
is positive in most elastic systems (though not rubber). If you hang a
weight onto the end of a metal wire (thus keeping the tension f in the
wire constant) and heat the wire, it will extend. This implies that αf > 0
for a metal wire. However, if you hang a weight by a piece of rubber and
supply heat, you will find that the rubber will contract, which implies
that αf < 0 for rubber.
Example 17.1
How does the tension of a wire held at constant length change with
temperature?
Solution: Our definitions of ET and αf allow us to calculate this. Using
eqn C.42, we have that
�∂f
∂T
�
L
= −
�∂f
∂L
�
T
�∂L
∂T
�
f
= −AET αf,
(17.5)
where the last step is obtained using eqns 17.3 and 17.4.
This
result
is
familiar
to
anyone
who plays a metal-stringed instrument
where αf > 0 and hence (∂f/∂T)L <
0 from eqn 17.5; hot weather causes
the strings (held at constant length) to
slacken (reduce their tension).
We are now in a position to do some thermodynamics on our elastic
system. We will rewrite the first law of thermodynamics for this case as
dU = T dS + f dL.
(17.6)
We can also obtain other thermodynamic potentials, such as the Helmholtz
function F = U −TS, so that dF = dU −T dS −S dT, and hence
dF = −S dT + f dL.
(17.7)
Equation 17.7 implies that the entropy S is
S = −
�∂F
∂T
�
L
,
(17.8)
and similarly the tension f is
f =
�∂F
∂L
�
T
.
(17.9)

===== Page 212 =====

17.1
Elastic rod
193
A Maxwell’s-relation–type-step2 then leads to an expression for the
2As in the case of a gas, the Maxwell’s
relation allows us to relate some differ-
ential of entropy (which is hard to mea-
sure experimentally, but is telling us
something fundamental about the sys-
tem) to a differential that we can mea-
sure in an experiment, here the change
in tension with temperature of a rod
held at constant length.
isothermal change in entropy on extension as
�∂S
∂L
�
T
= −
�∂f
∂T
�
L
.
(17.10)
The right-hand side of this equation was worked out in eqn 17.5, so that
�∂S
∂L
�
T
= AET αf,
(17.11)
where A is the area (presumed not to change), and so stretching the rod
(increasing L) results in an increase in entropy if αf > 0. This is like
the case of an ideal gas for which
�∂S
∂V
�
T
=
�∂p
∂T
�
V
> 0,
(17.12)
so that expanding the gas (increasing V ) results in an increase in entropy.
If the entropy of the system goes up as it is expanded isothermally, then
heat must be absorbed. For the case of the elastic rod (assuming it is
not made of rubber), extending it isothermally (and reversibly) by ΔL
would then lead to an absorption of heat ΔQ given by
ΔQ = TΔS = AET TαfΔL.
(17.13)
Why does stretching a wire increase its entropy? Let us consider the
case of a metallic wire. This contains many small crystallites, which
have low entropy. The action of stretching the wire distorts those small
crystallites, and that increases their entropy and so heat is absorbed.3
3For example, the crystallites might
distort from cubic to tetragonal sym-
metry, thus lowering the entropy.
In
addition, the stretching of the wire may
increase the volume per atom in the
wire and this also increases the entropy.
Fig.
17.2 Rubber consists of long-
chain molecules.
(a) With no force
applied, the rubber molecule is quite
coiled up and the average end-to-end
distance is short, and the entropy is
large.
This picture has been drawn
by taking each segment of the chain
to point randomly.
(b) With a force
applied (along a vertical axis in this
diagram), the molecule becomes more
aligned with the direction of the ap-
plied force, and the end-to-end distance
is large, reducing the entropy (see Ex-
ercise 17.3).
However, for rubber αf < 0, and hence an isothermal extension means
that heat is emitted. The action of stretching a piece of rubber at con-
stant temperature results in the alignment of the long rubber molecules,
reducing their entropy (see Fig. 17.2) and causing heat to be released.
Example 17.2
The internal energy U for an ideal gas does not change when it is ex-
panded isothermally. How does U change for an elastic rod when it is
extended isothermally?
Solution: The change in internal energy on isothermal extension can be
worked out from eqn 17.6 and eqn 17.11 by writing
�∂U
∂L
�
T
= T
�∂S
∂L
�
T
+ f = f + ATET αf.
(17.14)
This is the sum of a positive term expressing the energy going into the
rod by work and a term expressing the heat flow into the rod due to an
isothermal change of length. (For an ideal gas, a similar analysis applies,
but the work done by the gas and the heat that flows into it balance
perfectly, so that U does not change.)

===== Page 213 =====

194
Rods, bubbles, and magnets
17.2
Surface tension
We now consider the case of a liquid surface with surface area A. Liquid
surfaces cost energy, which is why a liquid will tend to form droplets
(or, even better, a single droplet) to minimize this surface energy. The
work needed to change the area of a liquid surface is given by
¯dW = γ dA,
(17.15)
where γ is a parameter known as the surface tension.
Fig. 17.3 A spherical droplet of liq-
uid of radius r is suspended from a thin
pipe connected to a piston, which main-
tains the pressure p of the liquid.
Consider the arrangement shown in Fig. 17.3. If the piston moves
down, work ¯dW = F dx = +p dV is done on the liquid (which is assumed
to be incompressible). The droplet radius will therefore increase by an
amount dr such that dV = 4πr2 dr, and the surface area of the droplet
will change by an amount
dA = 4π(r + dr)2 −4πr2 ≈8πr dr,
(17.16)
so that
¯dW = γ dA = 8πγr dr.
(17.17)
Equating this to ¯dW = F dx = +p dV = p · 4πr2 dr yields
p = 2γ
r .
(17.18)
The pressure p in this expression is, of course, really the pressure dif-
ference between the pressure in the liquid and the atmospheric pressure
against which the surface of the drop pushes.
Example 17.3
What is the pressure of gas inside a spherical bubble of radius r?
Solution: The bubble (see Fig. 17.4) has two surfaces, and so the pressure
pbubble of gas inside the bubble, minus the pressure p0 outside the bubble,
has to support two lots of surface tension. Hence, assuming the liquid
wall of the bubble is thin (so that the radii of inner and outer walls are
both ≈r),
Fig. 17.4 A bubble of radius r has an
inner and an outer surface.
pbubble −p0 = 4γ
r .
(17.19)
Notice that surface tension has a microscopic explanation. A molecule
in the bulk of the liquid is attracted to its nearest neighbours by inter-
molecular forces (which is what holds a liquid together), and these forces
are applied to a given molecule by its neighbours from all directions. One
can think of these forces almost as weak chemical bonds. The molecules
at the surface are only attracted by their neighbouring molecules in one
direction, back towards the bulk of the liquid, but there is no corre-
sponding attractive force out into the “wild blue yonder”. The surface

===== Page 214 =====

17.3
Electric and magnetic dipoles
195
has a higher energy than the bulk because bonds have to be broken in
order to make a surface, and γ tells you how much energy you need to
form a unit area of surface (which gives an estimate of the size of the
intermolecular forces).
We can write the first law of thermodynamics for our surface of area
A as
dU = T dS + γ dA
(17.20)
and similarly changes in the Helmholtz function can be written
dF = −S dT + γ dA,
(17.21)
which yields the Maxwell’s relation
�∂S
∂A
�
T
= −
�∂γ
∂T
�
A
.
(17.22)
Equation 17.20 implies that
�∂U
∂A
�
T
= T
�∂S
∂A
�
T
+ γ,
(17.23)
and hence using eqn 17.22, we have
�∂U
∂A
�
T
= γ −T
�∂γ
∂T
�
A
,
(17.24)
the sum of a positive term expressing the energy going into a surface
by work and a negative term expressing the heat flow into the surface
due to an isothermal change of area. Usually, the surface tension has a
temperature dependence as shown in Fig. 17.5, and hence (∂γ/∂T)A < 0,
so in fact both terms contribute a positive amount.
Heat ΔQ is given by
ΔQ = T
�∂S
∂A
�
T
ΔA = −TΔA
�∂γ
∂T
�
A
> 0,
(17.25)
and this is absorbed on isothermally stretching a surface to increase its
area by ΔA. This quantity is positive and so heat really is absorbed.
Since
�∂S
∂A
�
T is positive, this shows that the surface has an additional
entropy compared with the bulk, in addition to costing extra energy.
Fig. 17.5 Schematic diagram of the
surface tension γ of a liquid as a func-
tion of temperature. Since γ must van-
ish at the boiling temperature Tb, we
expect that (∂γ/∂T)A < 0.
17.3
Electric and magnetic dipoles
An electric dipole moment pE can interact with an electric field E. The
potential energy of the dipole in the electric field is −pE · E. If the
electric field changes, the interaction energy can change by
d(−pE · E) = −pE · dE −E · dpE.
(17.26)
There is also some stored energy in the dipole itself. An electric dipole
consists of charges +q and −q separated by a distance a, so that the

===== Page 215 =====

196
Rods, bubbles, and magnets
dipole moment has magnitude pE = qa. The force on each charge due
to the electric field has magnitude qE. A small change da in the length
a means that the dipole moment changes by dpE = q da. Modelling the
bond between the charges as a spring, the work done on this spring be-
cause of the change of length is given by the force qE times the distance
da which equals E(q da) = E dpE. In the case in which the electric field
is at an angle to the dipole moment, only the component of the elec-
tric field parallel to the dipole moment acts to stretch the spring, so in
general we can write this contribution as +E · dpE. Adding this stored
energy to the interaction energy from eqn 17.26 gives the work supplied
to the system as4
4This is the work added to the system
(where system here means the electric
dipole and its interaction with the field)
and hence is the free energy of the elec-
tric dipole. Because the energy of the
dipole in the electric field is shared be-
tween the dipole and the field (it is an
interaction energy, belonging to both
parties) it does not make sense to think
of energy that is internal to the dipole
itself, and the “system” means the in-
teracting dipole and field.
¯dW = −pE · dE.
(17.27)
Analogous arguments can be used to show that the work supplied to a
magnetic dipole is given by
¯dW = −m · dB.
(17.28)
We consider assemblies of magnetic moments in more detail in the next
section.
17.4
Paramagnetism
Consider a system of magnetic moments arranged in a lattice at temper-
ature T. We assume that the magnetic moments cannot interact with
each other. If the application of a magnetic field causes the magnetic
moments to line up, the system is said to exhibit paramagnetism. The
equivalent formulation of the first law of thermodynamics for a param-
agnet is
dU = T dS −m dB,
(17.29)
where m is the magnetic moment and B is the magnetic field.5 The
5B is often known as the magnetic
flux density or the magnetic induc-
tion, but following common usage, we
refer to B as the magnetic field; see
Blundell (2001).
The magnetic field
H (often called the magnetic field
strength) is related to B and the mag-
netization M by
B = μ0(H + M).
magnetic moment m = MV , where M is the magnetization and V is
the volume. The magnetic susceptibility χ is given by
χ = limH→0
M
H .
(17.30)
For most paramagnets χ ≪1, so that M ≪H and hence B = μ0(H +
M) ≈μ0H. This implies that we can write the magnetic susceptibility
χ as
χ ≈μ0M
B
.
(17.31)
Paramagnetic systems obey Curie’s law, which states that
Fig. 17.6 The magnetic susceptibility
for a paramagnet follows Curie’s law
which states that χ ∝1/T.
χ ∝1
T ,
(17.32)
as shown in Fig. 17.6, and hence
�∂χ
∂T
�
B
< 0,
(17.33)
a result that we shall use later.6
6Curie’s law itself is derived in Exam-
ple 20.5.

===== Page 216 =====

17.4
Paramagnetism
197
Example 17.4
Show that heat is emitted in an isothermal increase in B (a process
known as isothermal magnetization) but that temperature is reduced
for an adiabatic reduction in B (a process known as adiabatic demag-
netization).
This coupling between thermal and
magnetic properties is known as the
magnetocaloric effect.
Solution: Eqn 17.29 implies that changes in the Helmholtz function
F = U −TS follows
dF = −S dT −m dB,
(17.34)
which yields the Maxwell relation
�∂S
∂B
�
T
=
�∂m
∂T
�
B
≈V B
μ0
�∂χ
∂T
�
B
,
(17.35)
which relates the isothermal change of entropy with field at constant
temperature to a differential of the susceptibility χ.
The heat absorbed in an isothermal change of B is
ΔQ = T
�∂S
∂B
�
T
ΔB = TV B
μ0
�∂χ
∂T
�
B
ΔB < 0,
(17.36)
and since it is negative it implies that heat is actually emitted. The
change in temperature in an adiabatic change of B is
�∂T
∂B
�
S
= −
�∂T
∂S
�
B
�∂S
∂B
�
T
.
(17.37)
If we define CB = T
�∂S
∂T
�
B, the heat capacity at constant B, then
substitution of this and eqn 17.35 into eqn 17.37 yields
�∂T
∂B
�
S
= −TV B
μ0CB
�∂χ
∂T
�
B
.
(17.38)
Equation 17.33 implies that
�∂T
∂B
�
S > 0, and hence we can cool a mate-
rial using an adiabatic demagnetization, i.e., by reducing the magnetic
field on a sample while keeping it at constant entropy. This can yield
temperatures as low as a few millikelvin for electronic systems and a few
microkelvin for nuclear systems.
Let us now consider why adiabatic demagnetization results in the cool-
ing of a material from a microscopic point of view. Consider a sample of
a paramagnetic salt, which contains N independent magnetic moments.
Without a magnetic field applied, the magnetic moments will point in
random directions (because we are assuming that they do not interact
with each other) and the system will have no net magnetization. An
applied field B will, however, tend to line up the magnetic moments and
produce a magnetization. Increasing temperature reduces the magne-
tization, and increasing magnetic field increases the magnetization. At

===== Page 217 =====

198
Rods, bubbles, and magnets
very high temperature, the magnetic moments all point in random direc-
tions and the net magnetization is zero (see Fig. 17.7(a)). The thermal
energy kBT is so large that all states are equally populated, irrespective
of whether or not the state is energetically favourable. If the magnetic
moments have angular momentum quantum number J =
1
2 they can
only point parallel or antiparallel to the magnetic field: hence there are
Ω = 2N ways of arranging up and down magnetic moments. Hence the
magnetic contribution to the entropy, S, is
S = kB ln Ω = NkB ln 2.
(17.39)
In the general case of J > 1
2, Ω = (2J + 1)N and the entropy is
S = NkB ln(2J + 1).
(17.40)
At lower temperature, the entropy of the paramagnetic salt must reduce
as only the lowest energy levels are occupied, corresponding to the aver-
age alignment of the magnetic moments with the applied field increasing.
At very low temperature, all the magnetic moments will align with the
magnetic field to minimize their energy (see Fig. 17.7(b)). In this case
there is only one way of arranging the system (with all spins aligned) so
Ω = 1 and S = 0.
Fig. 17.7 (a) At high temperature, the
spins in a paramagnet are in random
directions because the thermal energy
kBT is much larger than the magnetic
energy mB.
This state has high en-
tropy.
(b) At low temperature, the
spins become aligned with the field be-
cause the thermal energy kBT is much
smaller than the magnetic energy mB.
This state has low entropy.
The procedure for magnetically cooling a sample is as follows. The
paramagnet is first cooled to a low starting temperature using liquid
helium.
The magnetic cooling then proceeds via two steps (see also
Fig. 17.8).
The first step is isothermal magnetization. The energy of a para-
magnet is reduced by alignment of the moments parallel to a magnetic
field. At a given temperature the alignment of the moments may there-
fore be enhanced by increasing the strength of an applied magnetic field.
This is performed isothermally (see Fig. 17.8, step a →b) by having the
sample thermally connected to a bath of liquid helium (the boiling point
of helium at atmospheric pressure is 4.2 K), or perhaps with the liquid
helium bath at reduced pressure so that the temperature can be less than
4.2 K. The temperature of the sample does not change and the helium
bath absorbs the heat liberated by the sample as its energy and entropy
decrease. The thermal connection is usually provided by low-pressure
helium gas in the sample chamber, which conducts heat between the
sample and the chamber walls, the chamber itself sitting inside the he-
lium bath. (The gas is often called “exchange” gas because it allows the
sample and the bath to exchange heat.)
The second step is to thermally isolate the sample from the helium
bath (by pumping away the exchange gas). The magnetic field is then
slowly reduced to zero, slowly so that the process is quasistatic and the
entropy is constant. This step is called adiabatic demagnetization
(see Fig. 17.8, step b →c) and it reduces the temperature of the system.
During adiabatic demagnetization the entropy of the sample remains
constant; the entropy of the magnetic moments increases (because the
moments randomize as the field is turned down) and this is precisely

===== Page 218 =====

17.4
Paramagnetism
199
balanced by the decrease in the entropy of the phonons (the lattice
vibrations) as the sample cools. Entropy is thus exchanged between the
phonons and the spins.
Fig. 17.8 The entropy of a paramag-
netic salt as a function of temperature
for several different applied magnetic
fields between zero and some maximum
value, which we will call Bb. Magnetic
cooling of a paramagnetic salt from
temperature Ti to Tf is accomplished as
indicated in two steps: first, isothermal
magnetization from a to b by increasing
the magnetic field from 0 to Bb at con-
stant temperature Ti; second, adiabatic
demagnetization from b to c. The S(T)
curves have been calculated assuming
J = 1
2 . A term ∝T 3 has been added
to these curves to simulate the entropy
of the lattice vibrations. The curve for
B = 0 is actually for small, but non-
zero, B to simulate the effect of a small
residual field.
There is another way of looking at adiabatic demagnetization. Con-
sider the energy levels of magnetic ions in a paramagnetic salt subjected
to an applied magnetic field. The population of magnetic ions in each en-
ergy level is given by the Boltzmann distribution, as indicated schemati-
cally in Fig. 17.9(a). The rate at which the levels decrease in population
as the energy increases is determined by the temperature T. When we
perform an isothermal magnetization (increasing the applied magnetic
field while keeping the temperature constant) we are increasing the spac-
ing between the energy levels of the paramagnetic salt [see Fig. 17.9(b)],
but the occupation of each level is determined by the same Boltzmann
distribution because the temperature T is constant. Thus the higher–
energy levels become depopulated. This depopulation is the result of
transitions between energy levels caused by interaction with the sur-
roundings, which are keeping the system at constant temperature. In
an adiabatic demagnetization, the external magnetic field is reduced to
its original value, closing up the energy levels again. However, because
the salt is now thermally isolated, no transitions between energy lev-
els are possible and the populations of each level remain the same [see
Fig. 17.9(c)]. Another way of saying this is that in an adiabatic process
the entropy S = −kB
�
i Pi ln Pi (eqn 14.48) of the system is constant,
and this expression only involves the probability Pi of occupying the ith
level, not the energy. Thus the temperature of the paramagnetic salt fol-
lowing the adiabatic demagnetization is lower because the occupancies
now correspond to a Boltzmann distribution with a lower temperature.

===== Page 219 =====

200
Rods, bubbles, and magnets
Does adiabatic demagnetization as a method of cooling have a limit?
At first sight it looks as though the entropy would be S = NkB ln(2J +1)
at B = 0 for all T > 0, and therefore with B ̸= 0, S →0 only at absolute
zero, implying that adiabatic demagnetization might be used to cool all
the way to absolute zero. However, in real paramagnetic salts there is
always some small residual internal field due to interactions between the
moments which ensures that the entropy falls prematurely towards zero
when the temperature is a little above absolute zero (see Fig. 17.8). The
size of this field puts a limit on the lowest temperature to which the
paramagnetic salt can be cooled. In certain paramagnetic salts, which
have a very small residual internal field, temperatures of a few millikelvin
can be achieved. The failure of Curie’s law as we approach T = 0 is just
one of the consequences of the third law of thermodynamics, which we
shall treat in the following chapter.
Fig. 17.9 Schematic diagram showing
the energy levels in a magnetic system
(a) initially, (b) following isothermal
magnetization, and (c) following adia-
batic demagnetization.
Chapter summary
• The first law for a gas is dU = T dS −p dV . An isothermal ex-
pansion results in S increasing (see Fig. 17.10(a)). An adiabatic
compression results in T increasing.
• The first law for an elastic rod is dU = T dS +f dL. An isothermal
extension of a metal wire results in S increasing (see Fig. 17.10(b))
but for rubber S decreases (see Fig. 17.10(c)). An adiabatic con-
traction of a metal wire results in T increasing (but for rubber T
decreases).
• The first law for a liquid surface is dU = T dS + γ dA. An isother-
mal stretching results in S increasing. An adiabatic contraction
results in T increasing.
• The first law is dU
=
T dS −m dB for a magnetic sys-
tem.
An isothermal magnetization results in S decreasing (see
Fig. 17.10(d)). An adiabatic demagnetization results in T decreas-
ing.

===== Page 220 =====

Exercises
201
Fig. 17.10 Entropy increases when (a)
a gas is expanded isothermally, (b) a
metallic rod is stretched isothermally.
Entropy decreases when (c) rubber is
stretched isothermally and (d) a para-
magnet is magnetized isothermally.
Exercises
(17.1) For an elastic rod, show that
„∂CL
∂L
«
T
= −T
„ ∂2f
∂T 2
«
L
,
(17.41)
where CL is the heat capacity at constant length
L.
(17.2) For an elastic rod, show that
„∂T
∂L
«
S
= −TAET αf
CL
.
(17.42)
For rubber, explain why this quantity is positive.
Hence explain why, if you take a rubber band that
has been under tension for some time and sud-
denly release the tension to zero, the rubber band
appears to have cooled.
(17.3) A rubber molecule can be modelled in one di-
mension as a chain consisting of a series of N =
N+ +N−links, where N+ links point in the +x di-
rection, while N−links point in the −x direction.
If the length of one link in the chain is a, show
that the length L of the chain is
L = a(N+ −N−).
(17.43)
Show further that the number of ways Ω(L) of
arranging the links to achieve a length L can be
written as
Ω(L) =
N!
N+!N−!,
(17.44)
and also that the entropy S = kB ln Ω(L) can be
written approximately as
S = NkB
»
ln 2 −
L2
2N 2a2
–
(17.45)
when L ≪Na, and hence that S decreases as L
increases.

===== Page 221 =====

202
Exercises
(17.4) The entropy S of a surface can be written as a
function of its area A and temperature T. Hence
show that
dU
=
T dS + γ dA
(17.46)
=
CA dT +
»
γ −T
„ ∂γ
∂T
«
A
–
dA.
(17.5) Consider a liquid of density ρ with molar mass M.
Explain why the number of molecules per unit area
in the surface is approximately
(ρNA/M)2/3.
(17.47)
Hence, the energy contribution per molecule to the
surface tension γ is approximately
γ/(ρNA/M)2/3.
(17.48)
Evaluate this quantity for water (surface tension
at 20 ◦C is approximately 72 mJ m−2) and express
your answer in eV. Compare your result with the
latent heat per molecule (the molar latent heat of
water is 4.4×104 J mol−1).
(17.6) For a stretched rubber band, it is observed exper-
imentally that the tension f is proportional to the
temperature T if the length L is held constant.
Show that:
(a) the internal energy U is a function of temper-
ature only;
(b) adiabatic stretching of the band results in an
increase in temperature;
(c) the band will contract if warmed while kept
under constant tension.
(17.7) A soap bubble of radius R1 and surface tension γ
is expanded at constant temperature by forcing in
air by driving in a piston containing volume Vpiston
fully home. Show that the work ΔW needed to in-
crease the bubble’s radius to R2 is
ΔW
=
p2V2 ln p2
p1 + 8πγ(R2
2 −R2
1)
+p0(V2 −V1 −Vpiston),
(17.49)
where p1 and p2 are the initial and final pressures
in the bubble, p0 is the pressure of the atmosphere
and V1 = 4
3πR3
1 and V2 = 4
3πR3
2.

===== Page 222 =====

18
The third law
18.1 Different statements of the
third law
203
18.2 Consequences
of
the
third
law
205
Chapter summary
208
Exercises
208
In Chapter 13, we presented the second law of thermodynamics in var-
ious different forms. In Chapter 14, we related this to the concept of
entropy and showed that the entropy of an isolated system always either
stays the same or increases with time. But what value does the entropy
of a system take, and how can you measure it?
One way of measuring the entropy of a system is to measure its heat
capacity.
For example, if measurements of Cp, the heat capacity at
constant pressure, are made as a function of temperature, then using
Cp = T
�∂S
∂T
�
p
,
(18.1)
we can obtain entropy S by integration, so that
S =
�Cp
T dT.
(18.2)
This is all very well, but when you integrate, you have to worry about
constants of integration. Writing eqn 18.2 as a definite integral, we have
that the entropy S(T), measured at temperature T, is
S(T) = S(T0) +
�T
T0
Cp
T dT,
(18.3)
where T0 is some different temperature (see Fig. 18.1).
Thus it seems
Fig. 18.1 A graphical representation of
eqn 18.3.
that we are only able to learn about changes in entropy, for example
as a system is warmed from T0 to T, and we are not able to obtain an
absolute measurement of entropy itself. The third law of thermodynam-
ics, presented in this chapter, gives us additional information because it
provides a value for the entropy at one particular temperature, namely
absolute zero.
18.1
Different statements of the third law
Walter H. Nernst (1864–1941) (Fig. 18.2) came up with the first state-
ment of the third law of thermodynamics after examining data on chem-
ical thermodynamics and doing experiments with electrochemical cells.
The essential conclusion he came to concerned the change in enthalpy
ΔH in a reaction (the heat of the reaction, positive if endothermic,
negative if exothermic; see Section 16.5), and the change in Gibbs’ func-
tion ΔG (that determines in which direction the reaction goes). Since

===== Page 223 =====

204
The third law
G = H −TS, we expect that
ΔG = ΔH −TΔS,
(18.4)
so that as T →0, ΔG →ΔH. Experimental data showed that this was
true, but ΔG and ΔH not only came closer together on cooling, but
they approached each other asymptotically. On the basis of the data,
Nernst also postulated that ΔS →0 as T →0. His statement of the
third law, dating from 1906, can be written as
Nernst’s statement of the third law
Near absolute zero, all reactions in a system in internal equilibrium
take place with no change in entropy.
Fig. 18.2 W. Nernst
Max Planck (1858–1947) (Fig. 18.3) added more meat to the bones of
the statement by making a further hypothesis in 1911, namely that:
Planck’s statement of the third law
The entropy of all systems in internal equilibrium is the same at ab-
solute zero, and may be taken to be zero.
Fig. 18.3 M. Planck
Planck actually made his statement only about perfect crystals. How-
ever, it is believed to be true about any system, as long as it is in internal
equilibrium (i.e., that all parts of a system are in equilibrium with each
other). There are a number of systems, such as 4He and 3He, which
are liquids even at very low temperature. Electrons in a metal can be
treated as a gas all the way down to T = 0. The third law applies to all
of these systems. However, note that the systems have to be in inter-
nal equilibrium for the third law to apply. An example of a system not
in equilibrium is a glass, which has frozen-in disorder. For a solid, the
lowest-energy phase is the perfect crystal, but the glass phase is higher
in energy and is unstable. The glass phase will eventually relax back to
the perfect crystalline phase but it may take many centuries to do this,
and possibly a time greater than the age of the Universe.1
1The idea that the glass in the windows
of very old cathedrals has flowed over
the centuries is popularly believed, but
has been debunked, see “Do Cathedral
Glasses Flow?”, E. D. Zanotto, Am. J.
Phys.
66, 392 (1998), see also E. D.
Zanotto and P. K. Gupta, Am. J. Phys.
67, 620 (1999).
Planck’s choice of zero for the entropy was further motivated by the
development of statistical mechanics, a subject we will tackle later in
this book. It suffices to say here that the statistical definition of en-
tropy, presented in eqn 14.36 (S = kB ln Ω), implies that zero entropy
is equivalent to Ω = 1. Thus at absolute zero, when a system finds its
ground state, the entropy being equal to zero implies that this ground
state is non-degenerate.
At this point, we can raise a potential objection to the third law in
Planck’s form. Consider a perfect crystal composed of N spinless atoms.
We are told by the third law that its entropy is zero. However, let us
further suppose that each atom has at its centre a nucleus with angular
momentum quantum number I. If no magnetic field is applied to this
system, then we appear to have a contradiction. The degeneracy of the

===== Page 224 =====

18.2
Consequences of the third law
205
nuclear spin is 2I + 1 and if I > 0, this will not be equal to one. How
can we reconcile this with zero entropy since the non-zero nuclear spin
implies that the entropy S of this system should be S = NkB ln(2I +1),
to however low a temperature we cool it?
The answer to this apparent contradiction is as follows: in a real sys-
tem in internal equilibrium, the individual components of the system
must be able to exchange energy with each other, i.e., to interact with
each other. Nuclear spins actually feel a tiny, but non-zero, magnetic
field due to the dipolar fields produced each other, and this lifts the de-
generacy. Another way of looking at this is to say that the interactions
give rise to collective excitations of the nuclear spins.
These collec-
tive excitations are nuclear spin waves, and the lowest-energy nuclear
spin wave, corresponding to the longest-wavelength mode, will be non-
degenerate. At sufficiently low temperatures (and this will be extremely
low!) only that long-wavelength mode will be thermally occupied and
the entropy of the nuclear spin system will be zero.
However, this example raises an important point. If we cool a crystal,
we will extract energy from the lattice and its entropy will drop towards
zero.
However, the nuclear spins will still retain their entropy until
cooled to a much lower temperature (reflecting the weaker interactions
between nuclear spins compared with the bonds between atoms in the
lattice). If we find a method of cooling the nuclei, there might still be
some residual entropy associated with the individual nucleons. All these
thermodynamic subsystems (the electrons, the nuclear spins, and the
nucleons) are very weakly coupled to each other, but their entropies are
additive.
Francis Simon (1893–1956) (Fig. 18.4) in 1937 called these
different subsystems “aspects” and formulated the third law as follows:
Simon’s statement of the third law
The contribution to the entropy of a system by each aspect of the
system which is in internal thermodynamic equilibrium tends to zero
as T →0.
Fig. 18.4 F. E. Simon
Simon’s statement is convenient because it allows us to focus on a
particular aspect of interest, knowing that its entropy will tend to zero
as T approaches 0, while ignoring the aspects that we don’t care about
and which might not lose their entropy until much closer to T = 0.
18.2
Consequences of the third law
Having provided various statements of the third law, it is time to exam-
ine some of its consequences.
• Heat capacities tend to zero as T →0
This consequence is easy to prove. Any heat capacity C given by
C = T
�∂S
∂T
�
=
�∂S
∂ln T
�
→0,
(18.5)

===== Page 225 =====

206
The third law
because as T →0, ln T →−∞and S →0. Hence C →0.
Note that this result disagrees with the classical prediction of C =
R/2 per mole per degree of freedom. (We note for future reference
that this observation emphasizes the fact that the equipartition
theorem, to be presented in Chapter 19, is a high temperature
theory and fails at low temperature.)
• Thermal expansion stops
Since S →0 as T →0, we have for example that
�∂S
∂p
�
T
→0
(18.6)
as T →0, but by a Maxwell relation, this implies that
1
V
�∂V
∂T
�
p
→0
(18.7)
and hence the isobaric expansivity βp →0.
• No gases remain ideal as T →0
The ideal monatomic gas has served us well in this book as a simple
model that allows us to obtain tractable results.
One of these
results is eqn 11.25, which states that for an ideal gas, Cp−CV = R
per mole.
However, as T →0, both Cp and CV tend to zero,
and this equation cannot be satisfied. Moreover, we expect that
CV = 3R/2 per mole, and as we have seen, this also does not
work down to absolute zero.
Yet another nail in the coffin of
the ideal gas is the expression for its entropy given in eqn 16.79
(S = CV ln T + R ln V + constant). As T →0, this equation yields
S →−∞, which is as far from zero as you can get!
Thus we see that the third law forces us to abandon the ideal gas
model when thinking about gases at low temperature. Of course,
it is at low temperature that the weak interactions between gas
molecules (blissfully neglected so far since we have modelled gas
molecules as independent entities) become more important. More
sophisticated models of gases will be considered in Chapter 26.
• Curie’s law breaks down
Curie’s law states that the susceptibility χ is proportional to 1/T
and hence χ →∞as T →0. However, the third law implies that
(∂S/∂B)T →0 and hence
�∂S
∂B
�
T
=
�∂m
∂T
�
B
= V B
μ0
�∂χ
∂T
�
B
(18.8)
must tend to zero. Thus
�
∂χ
∂T
�
→0, in disagreement with Curie’s
law. Why does it break down? You may begin to see a theme
developing: it is interactions again! Curie’s law is derived by con-
sidering magnetic moments to be entirely independent, in which
case their properties can be determined by considering only the
balance between the applied field (driving the moments to align)

===== Page 226 =====

18.2
Consequences of the third law
207
and temperature (driving the moments to randomize). The sus-
ceptibility measures their infinitesimal response to an infinitesimal
applied field; this becomes infinite when the thermal fluctuations
are removed at T = 0. However, if interactions between the mag-
netic moments are switched on, then an applied field will have
much less of an effect because the magnetic moments will already
be driven into some partially ordered state by each other.
There is a basic underlying message here: the microscopic parts
of a system can behave independently at high temperature, where
the thermal energy kBT is much larger than any interaction energy.
At low temperature, these interactions become important and all
notions of independence break down. To paraphrase (badly) the
poet John Donne:
No man is an island, and especially not as T →0.
• Unattainability of absolute zero
The final point can almost be elevated to the status of another
statement of the third law:
It is impossible to cool to T = 0 in a finite number of steps.
Fig. 18.5 The entropy as a function of
temperature for two different values of
a parameter X. Cooling is produced by
isothermal increases in X (i.e., X1 →
X2) and adiabatic decreases in X (i.e.,
X2 →X1). (a) If S does not go to 0
as T →0 it is possible to cool to ab-
solute zero in a finite number of steps.
(b) If the third law is obeyed, then it is
impossible to cool to absolute zero in a
finite number of steps.
This is messy to prove rigorously, but we can justify the argument
by reference to Fig. 18.5, which shows plots of S against T for
different values of a parameter X (which might be magnetic field,
for example). Cooling is produced by isothermal increases in X
and adiabatic decreases in X. If the third law did not hold, it
would be possible to proceed according to Fig. 18.5(a) and cool all
the way to absolute zero. However, because of the third law, the
situation is as in Fig. 18.5(b) and the number of steps needed to
get to absolute zero becomes infinite.
Before concluding this chapter, we make one remark concerning Carnot
engines. Consider a Carnot engine, operating between reservoirs with
temperatures Tℓand Th, having an efficiency η = 1−(Tℓ/Th) (eqn 13.10).
If Tℓ→0, the efficiency η tends to 1. If you operated this Carnot engine,
you would then get perfect conversion of heat into work, in violation of
Kelvin’s statement of the second law of thermodynamics. It seems at
first sight that the unattainability of absolute zero (a version of the third
law) is a simple consequence of the second law. However, there are diffi-
culties in considering a Carnot engine operating between two reservoirs,
one of which is at absolute zero. It is not clear how you can perform an
isothermal process at absolute zero, because once a system is at abso-
lute zero it is not possible to get it to change its thermodynamical state
without warming it. Thus it is generally believed that the third law is
indeed a separate postulate which is independent of the second law. The
third law points to the fact that many of our “simple” thermodynamic
models, such as the ideal gas equation and Curie’s law of paramagnets,
need substantial modification if they are to give correct predictions as

===== Page 227 =====

208
Exercises
T →0. It is therefore opportune to consider more sophisticated models
based on the microscopic properties of real systems, and that brings us
to statistical mechanics, the subject of the next part of this book.
Chapter summary
• The third law of thermodynamics can be stated in various ways:
• Nernst: Near absolute zero, all reactions in a system in internal
equilibrium take place with no change in entropy.
• Planck: The entropy of all systems in internal equilibrium is the
same at absolute zero, and may be taken to be zero.
• Simon: The contribution to the entropy of a system by each aspect
of the system which is in internal thermodynamic equilibrium tends
to zero as T →0.
• Unattainability of T = 0: it is impossible to cool to T = 0 in a
finite number of steps.
• The third law implies that heat capacities and thermal expansivi-
ties tend to zero as T →0.
• Interactions between the constituents of a system become impor-
tant as T →0, and this leads to the breakdown of the concept of
an ideal gas and also the breakdown of Curie’s law.
Exercises
(18.1) Summarize the main consequences of the third law
of thermodynamics. Explain how it casts a shadow
of doubt on some of the conclusions from various
thermodynamic models.
(18.2) Recall from eqn 16.26 that
H = G −T
„∂G
∂T
«
p
.
(18.9)
Hence show that
ΔG −ΔH = T
„∂ΔG
∂T
«
p
,
(18.10)
and explain what happens to these terms as the
temperature T →0.

===== Page 228 =====

Part VII
Statistical mechanics
In this part we introduce the subject of statistical mechanics. This is
a thermodynamic theory in which account is taken of the microscopic
properties of individual atoms or molecules analysed in a statistical fash-
ion. Statistical mechanics allows macroscopic properties to be calculated
from the statistical distribution of the microscopic behaviour of individ-
ual atoms and molecules. This part is structured as follows:
• In Chapter 19, we present the equipartition theorem, a principle
that states that the internal energy of a classical system composed
of a large number of particles in thermal equilibrium will distribute
itself evenly among each of the quadratic degrees of freedom acces-
sible to the particles of the system.
• In Chapter 20 we introduce the partition function, which encodes
all the information concerning the states of a system and their
thermal occupation. Having the partition function allows you to
calculate all the thermodynamic properties of the system.
• In Chapter 21 we calculate the partition function for an ideal gas
and use this to define the quantum concentration. We show how the
indistinguishability of molecules affects the statistical properties
and has thermodynamic consequences.
• In Chapter 22 we extend our results on partition functions to sys-
tems in which the number of particles can vary. This allows us
to define the chemical potential and introduce the grand partition
function.
• In Chapter 23, we consider the statistical mechanics of light, which
is quantized as photons, introducing black-body radiation, radiation
pressure, and the cosmic microwave background.
• In Chapter 24, we discuss the analogous behaviour of lattice vi-
brations, quantized as phonons, and introduce the Einstein model
and Debye model of the thermal properties of solids.

===== Page 229 =====

19
Equipartition of energy
19.1 Equipartition theorem
210
19.2 Applications
213
19.3 Assumptions made
215
19.4 Brownian motion
217
Chapter summary
218
Exercises
218
Before introducing the partition function in Chapter 20, which will al-
low us to calculate many different properties of thermodynamic systems
on the basis of their microscopic energy levels (which can be deduced
using quantum mechanics), we devote this chapter to the equipartition
theorem. This theorem provides a simple, classical theory of thermal
systems. It gives remarkably good answers, but only at high tempera-
ture, where the details of quantized energy levels can be safely ignored.
We will motivate and prove this theorem in the following section, and
then apply it to various physical situations in Section 19.2, demonstrat-
ing that it provides a rapid and straightforward method for deriving
heat capacities. Finally, in Section 19.3, we will critically examine the
assumptions that we have made in the derivation of the equipartition
theorem.
19.1
Equipartition theorem
Very often in physics one is faced with an energy dependence that is
quadratic in some variable.1 An example would be the kinetic energy
1We will show later in Section 19.3 that
this quadratic dependence is very com-
mon; most potential wells are approx-
imately quadratic near the bottom of
the well.
EKE of a particle with mass m and velocity v, which is given by
EKE = 1
2mv2.
(19.1)
Another example would be the potential energy EPE of a mass suspended
at one end of a spring with spring constant k and displaced by a distance
x from its equilibrium point (see Fig. 19.1). This is given by
Fig. 19.1 A mass m suspended on a
spring with spring constant k.
The
mass is displaced by a distance x from
its equilibrium or “rest” position.
EPE = 1
2kx2.
(19.2)
In fact, the total energy E of a moving mass on the end of a spring is
given by the sum of these two terms, so that
E = EKE + EPE = 1
2mv2 + 1
2kx2,
(19.3)
and, as the mass undergoes simple harmonic motion, energy is exchanged
between EKE and EPE, while the total energy remains fixed.
Let us suppose that a system whose energy has a quadratic dependence
on some variable is allowed to interact with a heat bath. It is then able
to borrow energy occasionally from its environment, or even give it back
into the environment. What mean thermal energy would it have? The

===== Page 230 =====

19.1
Equipartition theorem
211
thermal energy would be stored as kinetic or potential energy, so if a
mass on a spring is allowed to come into thermal equilibrium with its
environment, one could in principle take a very big magnifying glass
and see the mass on a spring jiggling around all by itself owing to such
thermal vibrations. How big would such vibrations be? The calculation
is quite straightforward.
Fig. 19.2 The energy E of a system is
E = αx2.
Let the energy E of a particular system be given by
E = αx2,
(19.4)
where α is some positive constant and x is some variable (see Fig. 19.2).
Let us also assume that x could in principle take any value with equal
probability. The probability P(x) of the system having a particular en-
ergy αx2 is proportional to the Boltzmann factor e−βαx2 (see eqn 4.13),
so that after normalizing, we have
P(x) =
e−βαx2
�∞
−∞e−βαx2 dx,
(19.5)
and the mean energy is
⟨E⟩
=
�∞
−∞
E P(x) dx
=
�∞
−∞αx2e−βαx2 dx
�∞
−∞e−βαx2 dx
=
1
2β
=
1
2kBT.
(19.6)
This is a really remarkable result.
It is independent of the constant
α and gives a mean energy that is proportional to temperature. The
theorem can be extended straightforwardly to the energy being the sum
of n quadratic terms, as shown in the following example.
Example 19.1
Assume that the energy E of a system can be given by the sum of n
independent quadratic terms, so that
E =
n
�
i=1
αix2
i ,
(19.7)
where αi are constants and xi are some variables. Assume also that each
xi could in principle take any value with equal probability. Calculate
the mean energy.
Solution:
The mean energy ⟨E⟩is given by
⟨E⟩=
�∞
−∞
· · ·
�∞
−∞
E P(x1, x2, . . . xn) dx1 dx2 · · · dxn.
(19.8)

===== Page 231 =====

212
Equipartition of energy
This now looks quite complicated when we substitute in the probability
as follows
⟨E⟩=
�∞
−∞· · ·
�∞
−∞
�n
�
i=1
αix2
i
�
exp
�
−β �n
j=1 αjx2
j
�
dx1dx2 · · · dxn
�∞
−∞· · ·
�∞
−∞exp
�
−β �n
j=1 αjx2
j
�
dx1dx2 · · · dxn
,
(19.9)
where i and j have been used to distinguish different sums. This ex-
pression can be simplified by recognizing that it is the sum of n similar
terms (write out the sums to convince yourself):
⟨E⟩=
n
�
i=1
�∞
−∞· · ·
�∞
−∞αix2
i exp
�
−β �n
j=1 αjx2
j
�
dx1dx2 · · · dxn
�∞
−∞· · ·
�∞
−∞exp
�
−β �n
j=1 αjx2
j
�
dx1dx2 · · · dxn
,
(19.10)
and then all but one integral cancels between the numerator and denom-
inator of each term, so that
⟨E⟩=
n
�
i=1
�∞
−∞αix2
i exp
�
−βαix2
i
�
dxi
�∞
−∞exp (−βαix2
i ) dxi
.
(19.11)
Now each term in this sum is the same as the one treated above in
eqn 19.6. Hence
⟨E⟩=
n
�
i=1
αi⟨x2
i ⟩
=
n
�
i=1
1
2kBT
=
n
2 kBT.
(19.12)
Each quadratic energy dependence of the system is called a mode of
the system (or sometimes a degree of freedom of the system). The
spring, our example at the beginning of this chapter, has two such modes.
The result of the example above shows that each mode of the system
contributes an amount of energy equal to 1
2kBT to the total mean energy
of the system. This result is the basis of the equipartition theorem,
which we state as follows:
Equipartition theorem
If the energy of a classical system is the sum of n quadratic modes,
and that system is in contact with a heat reservoir at temperature T,
the mean energy of the system is given by n × 1
2kBT.
The equipartition theorem expresses the fact that energy is “equally
partitioned” between all the separate modes of the system, each mode
having a mean energy of precisely 1
2kBT.

===== Page 232 =====

19.2
Applications
213
Example 19.2
We return to our example of a mass on a spring, whose energy is given by
the sum of two quadratic energy modes (see eqn 19.3). The equipartition
theorem then implies that the mean energy is given by
2 × 1
2kBT = kBT.
(19.13)
How big is this energy? At room temperature, kBT ≈4 × 10−21 J ≈
0.025 eV, which is a tiny energy. This energy isn’t going to set a 10 kg
mass on a stiff spring vibrating very much! However, the extraordinary
thing about the equipartition theorem is that the result holds indepen-
dently of the size of the system, so that kBT = 0.025 eV is also the mean
energy of an atom on the end of a chemical bond (which can be modelled
as a spring) at room temperature. For an atom, kBT = 0.025 eV goes a
very long way and this explains why atoms in molecules jiggle around a
lot at room temperature. We will explore this in more detail below.
19.2
Applications
We now consider four applications of the equipartition theorem.
19.2.1
Translational motion in a monatomic gas
The energy of each atom in a monatomic gas is given by
E = 1
2mv2
x + 1
2mv2
y + 1
2mv2
z,
(19.14)
where v = (vx, vy, vz) is the velocity of the atom (see Fig. 19.3). This
energy is the sum of three independent quadratic modes, and thus the
equipartition theorem gives the mean energy as
⟨E⟩= 3 × 1
2kBT = 3
2kBT.
(19.15)
This is in agreement with our earlier derivation of the mean kinetic
energy of a gas (see eqn 5.17).
Fig. 19.3 The velocity of a molecule in
a gas.
19.2.2
Rotational motion in a diatomic gas
In a diatomic gas, there is an additional possible energy source to con-
sider, namely that of rotational kinetic energy. This adds two terms to
the energy
L2
1
2I1
+ L2
2
2I2
,
(19.16)

===== Page 233 =====

214
Equipartition of energy
where L1 and L2 are the angular momenta along the two principal direc-
tions shown in Fig. 19.4 and I1 and I2 are the corresponding moments of
inertia. We do not need to worry about the direction along the diatomic
molecule’s bond, the axis labelled “3” in Fig. 19.4.
(This is because
the moment of inertia in this direction is very small (so that the corre-
sponding rotational kinetic energy is very large), so rotational modes in
this direction cannot be excited at ordinary temperature; such rotational
modes are connected with the individual molecular electronic levels and
we will therefore ignore them.)
The total energy is thus the sum of five terms, three due to transla-
tional kinetic energy and two due to rotational kinetic energy
E = 1
2mv2
x + 1
2mv2
y + 1
2mv2
z + L2
1
2I1
+ L2
2
2I2
,
(19.17)
and all of these energy modes are independent of one another. Using the
equipartition theorem, we can immediately write down the mean energy
as
⟨E⟩= 5 × 1
2kBT = 5
2kBT.
(19.18)
Fig. 19.4 Rotational motion in a di-
atomic gas.
19.2.3
Vibrational motion in a diatomic gas
If we also include the vibrational motion of the bond linking the two
atoms in our diatomic molecule, there are two additional modes to
include.
The intramolecular bond can be modelled as a spring (see
Fig. 19.5), so that the two extra energy terms are the kinetic energy due
to relative motion of the two atoms and the potential energy in the bond
(let us suppose it has spring constant k). Writing the positions of the
two atoms as r1 and r2 with respect to some fixed origin, the energy of
the atom can be written
Fig. 19.5 A diatomic molecule can be
modelled as two masses connected by a
spring.
E = 1
2mv2
x + 1
2mv2
y + 1
2mv2
z + L2
1
2I1
+ L2
2
2I2
+ 1
2μ(˙r1 −˙r2)2 + 1
2k(r1 −r2)2,
(19.19)
where μ = m1m2/(m1 + m2) is the reduced mass2 of the system. The
2See Appendix G.
equipartition theorem just cares about the number of modes in the sys-
tem, so the mean energy is simply
⟨E⟩= 7 × 1
2kBT = 7
2kBT.
(19.20)
The heat capacity of the systems described above can be obtained
by differentiating the energy with respect to temperature. The mean
energy is given by
⟨E⟩= f
2 kBT,
(19.21)
where f is the number of degrees of freedom. This equation implies that
CV per mole = f
2 R,
(19.22)

===== Page 234 =====

19.3
Assumptions made
215
and using eqn 11.27 we have
Cp per mole =
�f
2 + 1
�
R,
(19.23)
from which we may derive
γ = Cp
CV
= ( f
2 + 1)R
f
2 R
= 1 + 2
f .
(19.24)
We can summarize our results for the heat capacity of gases, per atom
or molecule, as follows:
Gas
Modes
f
⟨E⟩
γ
Monatomic
Translational only
3
3
2kB
5
3
Diatomic
Translational and rotational
5
5
2kB
7
5
Diatomic
Translational, rotational, and vibrational
7
7
2kB
9
7
19.2.4
The heat capacity of a solid
In a solid, the atoms are held rigidly in the lattice and there is no pos-
sibility of translational motion. However, the atoms can vibrate about
their mean positions. Consider a cubic solid (Fig. 19.6) in which each
atom is connected by springs (chemical bonds) to six neighbours (one
above, one below, one in front, one behind, one to the right, one to the
left). Since each spring joins two atoms, then if there are N atoms in
the solid, there are 3N springs (neglecting the surface of the solid, a
reasonable approximation if N is large). Each spring has two quadratic
modes of energy (one kinetic, one potential) and hence a mean thermal
energy equal to 2 × 1
2kBT = kBT. Hence the mean energy of the solid is
⟨E⟩= 3NkBT,
(19.25)
and the heat capacity is ∂⟨E⟩/∂T = 3NkB. Because R = NAkB, the
molar heat capacity of a solid is then expected to be 3NAkB = 3R. This
Fig. 19.6 In a cubic solid, each atom is
connected by chemical bonds, modelled
as springs, to six nearest neighbours,
two along each of the three Cartesian
axes.
Each spring is shared between
two atoms.
result agrees quite well with experiment and is known as the Dulong–
Petit rule (see Section 24.1).
19.3
Assumptions made
The equipartition theorem seems to be an extremely powerful tool for
evaluating thermal energies of systems.
However, it does have some
limitations, and to discover what these are, it is worth thinking about
the assumptions we have made in deriving it.

===== Page 235 =====

216
Equipartition of energy
• We have assumed that the parameter for which we have taken the
energy to be quadratic can take any possible value. In the deriva-
tion, the variables xi could be integrated continuously from −∞
to ∞. However, quantum mechanics insists that certain quanti-
ties can only take particular “quantized” values. For example, the
problem of a mass on a spring is shown by quantum mechanics
to have an energy spectrum that is quantized into levels given by
(n + 1
2)ℏω. When the thermal energy kBT is of the same order,
or lower than, ℏω, the approximation made by ignoring the quan-
tized nature of this energy spectrum is going to be a very bad one.
However, when kBT ≫ℏω, the quantized nature of the energy
spectrum is going to be largely irrelevant, in much the same way
that you

متأسفم، به نظر می‌رسد پاسخ قبلی من به دلیل طولانی بودن بیش از حد، در بخش‌هایی که شامل تصاویر و جداول بود با مشکل مواجه شده و قالب‌بندی Markdown (مانند جداول و برچسب‌های تصاویر) را به درستی رعایت نکرده است. این یک خطای رایج در پاسخ‌های طولانی است.

در اینجا، پاسخ را به صورت **کامل و اصلاح‌شده**، با رعایت دقیق قالب Markdown و فرمول‌نویسی LaTeX (با استفاده از `$` برای روابط درون‌خطی و `$$` برای روابط جداگانه) ارائه می‌دهم. تمام محتوا، شامل جداول، تصاویر (با برچسب `[Image]`)، و فرمول‌ها به صورت دقیق بازسازی شده است. این بار پاسخ به چند بخش تقسیم شده تا از بروز خطا در قالب‌بندی جلوگیری شود.

---

### بخش ۱: صفحه ۱ تا ۲۰ (سرفصل‌ها، مقدمه و پیش‌گفتار)

```markdown
===== Page 1 =====

# Concepts in Thermal Physics Second edition

[Image: Cover page showing three spheres. The largest is a transparent sphere with a grid of 0s and 1s on its surface. In front of it is a sphere with a red metallic piston mechanism inside. Behind them is a third small sphere showing the Earth. To the right, the equation S = -k_B ∑ P_i ln P_i is written. The authors' names are at the bottom right.]

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

0XFORDBUNIVERSITY PRESSGreat Clarendon Street, Oxford OX2 6DPOxford University Press is a department of the University of Oxford. It furthers the University's objective of excellence in research, scholarship, and education by publishing worldwide inOxford New YorkAuckland Cape Town Dar es Salaam Hong Kong KarachiKuala Lumpur Madrid Melbourne Mexico City NairobiNew Delhi Shanghai Taipei TorontoWith offices inArgentina Austria Brazil Chile Czech Republic France Greece Guatemala Hungary Italy Japan Poland Portugal SingaporeSouth Korea Switzerland Thailand Turkey Ukraine VietnamOxford is a registered trade mark of Oxford University Press in the UK and in certain other countriesPublished in the United States by Oxford University Press Inc., New York© Stephen J. Blundell and Katherine M. Blundell 2010The moral rights of the authors have been assertedDatabase right Oxford University Press (maker)First edition published in 2006Second edition published in 2010All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, without the prior permission in writing of Oxford University Press, or as expressly permitted by law, or under terms agreed with the appropriate reprographics rights organization. Enquiries concerning reproduction outside the scope of the above should be sent to the Rights Department, Oxford University Press, at the address aboveYou must not circulate this book in any other binding or cover and you must impose the same condition on any acquirerBritish Library Cataloguing in Publication DataData availableLibrary of Congress Cataloging in Publication DataData availablePrinted in Great Britainon acid- free paper byCPI Antony Rowe, Chippenham, Wilts.ISBN 978- 0- 19- 956209- 1 (Hbk.)ISBN 978- 0- 19- 956210- 7 (Pbk.)10987654321

===== Page 6 =====

1

===== Page 7 =====

This page intentionally left blank

===== Page 8 =====

 In the beginning was the Word...

(John 1:1, first century AD)

Consider sunbeams. When the sun's rays let in Pass through the darkness of a shuttered room, You will see a multitude of tiny bodies All mingling in a multitude of ways Inside the sunbeam, moving in the void, Seeming to be engaged in endless strife, Battle, and warfare, troop attacking troop, And never a respite, harried constantly, With meetings and with partings everywhere. From this you can imagine what it is For atoms to be tossed perpetually In endless motion through the mighty void.

(On the Nature of Things, Lucretius, first century BC)

... (we) have borne the burden of the work and the heat of the day. (Matthew 20:12, first century AD)

[Image: A sphere covered in a grid of squares. Each square contains a single digit, either a 0 or a 1.]

Thermal physics forms a key part of any undergraduate physics course. It includes the fundamentals of classical thermodynamics (which was founded largely in the nineteenth century and motivated by a desire to understand the conversion of heat into work using engines) and also statistical mechanics (which was founded by Boltzmann and Gibbs, and is concerned with the statistical behaviour of the underlying microstates of the system). Students often find these topics hard, and this problem is not helped by a lack of familiarity with basic concepts in mathematics, particularly in probability and statistics. Moreover, the traditional focus of thermodynamics on steam engines seems remote and largely irrelevant to a twenty- first century student. This is unfortunate since an understanding of thermal physics is crucial to almost all modern physics and to the important technological challenges which face us in this century.

The aim of this book is to provide an introduction to the key concepts in thermal physics, fleshed out with plenty of modern examples from astrophysics, atmospheric physics, laser physics, condensed matter physics and information theory. The important mathematical principles, particularly concerning probability and statistics, are expounded in some detail. This aims to make up for the material which can no longer be automatically assumed to have been covered in every school

===== Page 9 =====

 mathematics course. In addition, the appendices contain useful mathematics, such as various integrals, mathematical results and identities. There is, unfortunately, no shortcut to mastering the necessary mathematics in studying thermal physics, but the material in the appendix provides a useful aide- mémoire.

Many courses on this subject are taught historically: the kinetic theory of gases, then classical thermodynamics are taught first, with statistical mechanics taught last. In other courses, one starts with the principles of classical thermodynamics, followed then by statistical mechanics and kinetic theory is saved until the end. Although there is merit in both approaches, we have aimed at a more integrated treatment. For example, we introduce temperature using a straightforward statistical mechanical argument, rather than on the basis of a somewhat abstract Carnot engine. However, we do postpone detailed consideration of the partition function and statistical mechanics until after we have introduced the functions of state, which manipulation of the partition function so conveniently produces. We present the kinetic theory of gases fairly early on, since it provides a simple, well- defined arena in which to practise simple concepts in probability distributions. This has worked well in the course given in Oxford, but since kinetic theory is only studied at a later stage in courses in other places, we have designed the book so that the kinetic theory chapters can be omitted without causing problems; see Fig. 1.5 on page 10 for details. In addition,

متأسفم، به نظر می‌رسد پاسخ قبلی من به دلیل طولانی بودن بیش از حد، در بخش‌های خاصی از جمله صفحه 235 با خطای قطع شدن مواجه شده است.

در ادامه، پاسخ را از **صفحه 235** به صورت کامل، با رعایت دقیق قالب Markdown و فرمول‌نویسی LaTeX ارائه می‌دهم.

---

#### ادامه صفحه 235: بخش 19.3 (ادامه)

*We have assumed that the parameter for which we have taken the energy to be quadratic can take any possible value. In the deriva-
tion, the variables xi could be integrated continuously from −∞
to ∞. However, quantum mechanics insists that certain quanti-
ties can only take particular “quantized” values. For example, the
problem of a mass on a spring is shown by quantum mechanics
to have an energy spectrum that is quantized into levels given by
\((n + \frac{1}{2})\hbar\omega\). When the thermal energy \(k_B T\) is of the same order,
or lower than, \(\hbar\omega\), the approximation made by ignoring the quan-
tized nature of this energy spectrum is going to be a very bad one.
However, when \(k_B T \gg \hbar\omega\), the quantized nature of the energy
spectrum is going to be largely irrelevant, in much the same way
that you don’t notice that the different shades of grey in a news-
paper photograph are actually made up of lots of little dots if you
don’t look closely. Thus we come to an important conclusion:

The equipartition theorem is generally valid only at high temper-
ature, so that the thermal energy is larger than the energy gap
between quantized energy levels. Results based on the equipar-
tition theorem should emerge as the high-temperature limit of
more detailed theories.*

[Image: A graph of V(x) versus x, showing a potential well that is deeper and more complex than a simple quadratic, with a minimum at x=x0.]
**Fig. 19.7** \(V (x)\) is a function that is more complicated than a quadratic but has a minimum at \(x = x_0\).

*We have assumed throughout that modes are quadratic. Is that always valid? To give a concrete example, imagine that an atom moves with coordinate \(x\) in a potential well given by \(V (x)\), which is a function that might be more complicated than a quadratic (see, for example, Fig. 19.7). At absolute zero, the atom finds a potential minimum at say \(x_0\) (so that, for the usual reasons, \(\partial V/\partial x = 0\) and \(\partial^2 V/\partial x^2 > 0\) at \(x = x_0\)). At temperature \(T > 0\), the atom can explore regions away from \(x_0\) by borrowing energy of order \(k_B T\) from its environment. Near \(x_0\), the potential \(V (x)\) can be expanded$^3$ as*
$$V (x) = V (x_0) + \left(\frac{\partial V}{\partial x}\right)_{x_0} (x - x_0) + \frac{1}{2} \left(\frac{\partial^2 V}{\partial x^2}\right)_{x_0} (x - x_0)^2 + \cdots ,$$
*so that using $(\partial V/\partial x)_{x_0} = 0$, we find that the potential energy is*
$$V (x) = \text{constant} + \frac{1}{2} \left(\frac{\partial^2 V}{\partial x^2}\right)_{x_0} (x - x_0)^2 + \cdots ,$$
*which is a quadratic again. This demonstrates that the bottom of almost all potential wells tends to be approximately quadratic (this is known as the harmonic approximation).$^4$*

>$^3$Using a Taylor expansion; see Appendix B.
>$^4$The argument that the bottom of almost all potential wells tends to be approximately quadratic could fail if $(\partial^2 V/\partial x^2)_{x_0}$ turned out to be zero. This would happen if, for example, $V (x) = \alpha (x - x_0)^4$.

*If the temperature gets too high, the system will be able to access positions far away from \(x_0\) and the approximation of ignoring the higher order (cubic, quartic, etc.) terms (known as the anharmonic terms) in the Taylor expansion may become important.*

---

#### صفحه 217: بخش 19.4 (حرکت براونی)

### 19.4 Brownian motion

We close this chapter with one example in which the effect of the equipartition of energy is encountered.

**Example 19.3**
**Brownian motion**

In 1827, Robert Brown$^5$ used a microscope to observe pollen grains jiggling about in water. He was not the first to make such an observation (any small particles suspended in a fluid will do the same, and are very apparent when looking down a microscope), but this effect has come to be known as Brownian motion.

The motion is very irregular, consisting of translations and rotations, with grains moving independently, even when moving close to each other. The motion is found to be more active the smaller the particles. The motion is also found to be more active the less viscous the fluid. Brown was able to discount a “vital” explanation of the effect, i.e., that the pollen grains were somehow “alive”, but he was not able to give a correct explanation. Something resembling a modern theory of Brownian motion was proposed by Christian Wiener$^6$ in 1863, though the major breakthrough was made by Einstein in 1905.

We will postpone a full discussion of Brownian motion until Chapter 33, but using the equipartition theorem, the origin of the effect can be understood in outline. Each pollen grain (of mass \(m\)) is free to move translationally and so has mean kinetic energy $\frac{1}{2}m\langle v^2\rangle = \frac{3}{2}k_B T$. This energy is very small, as we have seen, but leads to a measurable amplitude of vibration for a small pollen grain. The amplitude of vibration is greater for smaller pollen grains because a mean kinetic energy of $\frac{3}{2}k_B T$ gives more mean square velocity \(\langle v^2\rangle\) to less massive grains. The thermally excited vibrations are resisted by viscous damping, so the motion is expected to be more pronounced in less viscous fluids.

> $^5$Robert Brown (1773–1858).
> $^6$Christian Wiener (1826–1896).

---

#### صفحه 218: خلاصه فصل و تمرینات

### Chapter summary

- The equipartition theorem states that if the energy of a system is the sum of \(n\) quadratic modes, and that the system is in contact with a heat reservoir of temperature \(T\), the mean energy of the system is given by \(n \times \frac{1}{2} k_B T\).
- The equipartition theorem is a high-temperature result and gives incorrect predictions at low temperature, where the discrete nature of the energy spectrum cannot be ignored.

### Exercises

**(19.1)** What is the mean kinetic energy in eV at room temperature of a gaseous (a) He atom, (b) Xe atom, (c) Ar atom, and (d) Kr atom. [Hint: do you have to make four separate calculations?]

**(19.2)** Comment on the following values of molar heat capacity in J K−1 mol−1, all measured at constant pressure at 298 K.

| Al | Ar | Au | Cu | He | H2 | Fe | Pb | Ne | N2 | O2 | Ag | Xe | Zn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 24.35 | 20.79 | 25.42 | 24.44 | 20.79 | 28.82 | 25.10 | 26.44 | 20.79 | 29.13 | 29.36 | 25.53 | 20.79 | 25.40 |

[Hint: express them in terms of \(R\); which of the substances is a solid and which is gaseous?]

**(19.3)** A particle at position \(\mathbf{r}\) is in a potential well \(V (\mathbf{r})\) given by
$$V (\mathbf{r}) = \frac{A}{r^n} - \frac{B}{r},$$
where \(A\) and \(B\) are positive constants and \(n > 2\). Show that the bottom of the well is approximately quadratic in \(\mathbf{r}\). Hence find the particle’s mean thermal energy at temperature \(T\) above the bottom of the well assuming the validity of the equipartition theorem in this situation.

**(19.4)** In Example 19.1, show that
$$\langle x_i^2 \rangle = \frac{k_B T}{2\alpha_i}.$$

**(19.5)** If the energy \(E\) of a system is not quadratic, but behaves like \(E = \alpha |x|\) where \(\alpha > 0\), show that the average energy is $\langle E\rangle = k_B T$.

**(19.6)** If the energy \(E\) of a system behaves like \(E = \alpha |x|^n\), where $n = 1, 2, 3 \ldots$ and \(\alpha > 0\), show that the average energy is $\langle E\rangle = \xi k_B T$, where \(\xi\) is a numerical constant.

**(19.7)** A simple pendulum with length \(\ell\) makes an angle \(\theta\) with the vertical, where \(\theta \ll 1\). Show that it oscillates with a period given by \(2\pi\sqrt{\ell/g}\). The pendulum is now placed at rest and allowed to come into equilibrium with its surroundings at temperature \(T\). Derive an expression for \(\langle \theta^2 \rangle\).

---
I understand you want the complete book in Markdown with LaTeX math. However, **I cannot generate the entire ~500-page book in a single response due to length limits**. I can provide the rest of the content chapter by chapter, starting from where we left off.

Here is the **complete content from Page 219 (Chapter 20) to Page 249**, formatted correctly with Markdown tables, LaTeX math, and `[Image]` placeholders.

---

## Chapter 20: The Partition Function

### Page 219

#### Chapter Outline

**20.1 Writing down the partition function** 220
**20.2 Obtaining the functions of state** 221
**20.3 The big idea** 228
**20.4 Combining partition functions** 228
**Chapter summary** 231
**Exercises** 232

The probability that a system is in some particular state \(\alpha\) is proportional to the Boltzmann factor \(e^{-\beta E_{\alpha}}\). We define the partition function\(^1\) \(Z\) by a sum over all the states of the Boltzmann factors, so that

$$Z = \sum_{\alpha} e^{-\beta E_{\alpha}} \tag{20.1}$$

where the sum is over all states of the system (each one labelled by \(\alpha\)). The partition function \(Z\) contains all the information about the energies of the states of the system, and the fantastic thing about the partition function is that all thermodynamical quantities can be obtained from it. It behaves like a zipped-up and compressed version of all the properties of the system; once you have \(Z\), you only have to know how to uncompress and unzip it to get functions of state like energy, entropy, Helmholtz function, or heat capacity to simply drop out. We can therefore reduce problem solving in statistical mechanics to two steps:

**Steps to solving statistical mechanics problems**

(1) Write down the partition function \(Z\). (see Section 20.1)
(2) Go through some standard procedures to obtain the functions of state you want from \(Z\). (see Section 20.2)

We will outline these two steps in the sections that follow. Before we do that, let us pause to notice an important feature about the partition function.

- The zero of energy is always somewhat arbitrary: one can always choose to measure energy with respect to a different zero, since it is only energy differences that are important. Hence the partition function is defined up to an arbitrary multiplicative constant. This seems somewhat strange, but it turns out that many physical quantities are related to the logarithm of the partition function and therefore these quantities are defined up to an additive constant (which might reflect, for example, the rest mass of particles). Other physical quantities, however, are determined by a differential of the logarithm of the partition function and therefore these quantities can be determined precisely.

> \(^1\)The partition function is given the symbol \(Z\) because the concept was first coined in German. *Zustandssumme* means “sum over states”, which is exactly what \(Z\) is. The English name “partition function” reflects the way in which \(Z\) measures how energy is “partitioned” between states of the system.

---

### Page 220

#### 20.1 Writing down the partition function

The partition function contains all the information we need to work out the thermodynamical properties of a system. In this section, we show how you can write down the partition function in the first place.

This procedure is not complicated! Writing down the partition function is nothing more than evaluating eqn 20.1 for different situations. We demonstrate this for a couple of commonly encountered and important examples.

**Example 20.1**

**(a) The two-level system (see Fig. 20.1(a))**

Let the energy of a system be either \(-\Delta/2\) or \(\Delta/2\). Then
$$Z = \sum_{\alpha} e^{-\beta E_{\alpha}} = e^{\beta\Delta/2} + e^{-\beta\Delta/2} = 2 \cosh\left(\frac{\beta\Delta}{2}\right), \tag{20.2}$$
where the final result follows from the definition of \(\cosh x \equiv \frac{1}{2}(e^x + e^{-x})\) (see Appendix B).

[Image: Two diagrams (a) and (b). (a) shows two horizontal lines representing energy levels, one at -Delta/2 and one at +Delta/2. (b) shows a ladder of evenly spaced energy levels, labelled n=0, 1, 2, ..., each with energy (n+1/2)hbar omega.]
**Fig. 20.1** Energy levels of (a) a two-level system and (b) a simple harmonic oscillator.

**(b) The simple harmonic oscillator (see Fig. 20.1(b))**

The energy of the system is \((n + \frac{1}{2})\hbar\omega\) where \(n = 0, 1, 2, \ldots\), and hence
$$Z = \sum_{\alpha} e^{-\beta E_{\alpha}} = \sum_{n=0}^{\infty} e^{-\beta(n + \frac{1}{2})\hbar\omega} = e^{-\beta\frac{1}{2}\hbar\omega} \sum_{n=0}^{\infty} e^{-n\beta\hbar\omega} = \frac{e^{-\frac{1}{2}\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}, \tag{20.3}$$
where the sum is evaluated using the standard result for the sum of an infinite geometric progression, see Appendix B. (An alternative form of this result is found by multiplying top and bottom by \(e^{\beta\frac{1}{2}\hbar\omega}\) to obtain the result \(Z = \frac{1}{2\sinh(\beta\hbar\omega/2)}\).)

Two further, slightly more complicated, examples are the set of \(N\) equally spaced energy levels and the energy levels appropriate for the rotational states of a diatomic molecule.

---

### Page 221

**Example 20.2**

**(c) The N-level system (see Fig. 20.2(c))**

Let the energy levels of a system be \(0, \hbar\omega, 2\hbar\omega, \ldots, (N-1)\hbar\omega\). Then
$$Z = \sum_{\alpha} e^{-\beta E_{\alpha}} = \sum_{j=0}^{N-1} e^{-j\beta\hbar\omega} = \frac{1 - e^{-N\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}, \tag{20.4}$$
where the sum is evaluated using the standard result for the sum of a finite geometric progression, see Appendix B.

**(d) Rotational energy levels (see Fig. 20.2(d))**

The rotational kinetic energy of a molecule with moment of inertia \(I\) is given by \(\hat{J}^2/2I\), where \(\hat{J}\) is the total angular momentum operator. The eigenvalues of \(\hat{J}^2\) are given by \(\hbar^2 J(J+1)\), where the angular momentum quantum number, \(J\), takes the values \(J = 0, 1, 2, \ldots\). The energy levels of this system are given by
$$E_J = \frac{\hbar^2}{2I} J(J+1), \tag{20.5}$$
and have degeneracy \(2J + 1\). Hence the partition function is
$$Z = \sum_{\alpha} e^{-\beta E_{\alpha}} = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\hbar^2 J(J+1)/2I}, \tag{20.6}$$
where the factor \((2J+1)\) takes into account the degeneracy of each level.

[Image: Two diagrams (c) and (d). (c) shows N discrete energy levels, equally spaced from 0 to (N-1)hbar omega. (d) shows rotational energy levels that get closer together as J increases, with degeneracies indicated.]
**Fig. 20.2** Energy levels of (c) an N-level system and (d) a rotational system.

---

#### 20.2 Obtaining the functions of state

[Image: A diagram of a sausage machine. An input labelled "Z" goes in one side, and various outputs like U, F, S, p, H, G, C_V come out the other.]
**Fig. 20.3** Given \(Z\), it takes only a turn of the handle on our “sausage machine” to produce other functions of state.

Once \(Z\) has been written down, we can place it in our mathematical sausage machine (see Fig. 20.3), which processes it and spits out fully-fledged thermodynamical functions of state. We now outline the derivations of the components of our sausage machine so that you can derive all these functions of state for any given \(Z\).

- **Internal energy \(U\)**
The internal energy \(U\) is given by
$$U = \frac{\sum_i E_i e^{-\beta E_i}}{\sum_i e^{-\beta E_i}}. \tag{20.7}$$
Now the denominator of this expression is the partition function \(Z = \sum_i e^{-\beta E_i}\), but the numerator is simply
$$-\frac{dZ}{d\beta} = \sum_i E_i e^{-\beta E_i}. \tag{20.8}$$
Thus \(U = -(1/Z)(dZ/d\beta)\), or more simply,
$$U = -\frac{d\ln Z}{d\beta}. \tag{20.9}$$
This is a useful form since \(Z\) is normally expressed in terms of \(\beta\). If you prefer things in terms of temperature \(T\), then using \(\beta = 1/k_B T\) (and hence \(d/d\beta = -k_B T^2(d/dT)\)) one obtains
$$U = k_B T^2 \frac{d\ln Z}{dT}. \tag{20.10}$$

---

### Page 222

- **Entropy \(S\)**
Since the probability \(P_j\) is given by a Boltzmann factor divided by the partition function (so that the sum of the probabilities is one, as can be shown using eqn 20.1), we have \(P_j = e^{-\beta E_j}/Z\) and hence
$$\ln P_j = -\beta E_j - \ln Z. \tag{20.11}$$
Equation 14.48 therefore gives us an expression for the entropy as follows:
$$S = -k_B \sum_i P_i \ln P_i = k_B \sum_i P_i (\beta E_i + \ln Z) = k_B (\beta U + \ln Z), \tag{20.12}$$
where we have used \(U = \sum_i P_i E_i\) and \(\sum_i P_i = 1\). Substituting the definition of \(\beta\), namely \(\beta = 1/k_B T\), into this equation gives
$$S = \frac{U}{T} + k_B \ln Z. \tag{20.13}$$

- **Helmholtz function \(F\)**
The Helmholtz function is defined via \(F = U - TS\), so using eqn 20.13 we have that
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

- **Pressure \(p\)**
The pressure can be obtained from \(F\) using eqn 16.20, so that
$$p = -\left(\frac{\partial F}{\partial V}\right)_T = k_B T \left(\frac{\partial \ln Z}{\partial V}\right)_T. \tag{20.20}$$
Having got the pressure we can then write down the enthalpy and the Gibbs function.

- **Enthalpy \(H\)**
$$H = U + pV = k_B T \left[ T \left(\frac{\partial \ln Z}{\partial T}\right)_V + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]. \tag{20.21}$$

- **Gibbs function \(G\)**
$$G = F + pV = k_B T \left[ -\ln Z + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]. \tag{20.22}$$

---

### Page 223

These relations are summarized in Table 20.1. In practice, it is easiest to remember only the relations for \(U\) and \(F\), since the others can be derived (using the relations shown in the left column of the table).

**Table 20.1** Thermodynamic quantities derived from the partition function \(Z\).

| Function of state | Statistical mechanical expression |
| :--- | :--- |
| \(U\) | \(-\frac{d\ln Z}{d\beta}\) |
| \(F\) | \(-k_B T \ln Z\) |
| \(S\) | \(= -\left(\frac{\partial F}{\partial T}\right)_V = \frac{U-F}{T} = k_B \ln Z + k_B T \left(\frac{\partial \ln Z}{\partial T}\right)_V\) |
| \(p\) | \(= -\left(\frac{\partial F}{\partial V}\right)_T = k_B T \left(\frac{\partial \ln Z}{\partial V}\right)_T\) |
| \(H\) | \(= U + pV = k_B T \left[ T \left(\frac{\partial \ln Z}{\partial T}\right)_V + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]\) |
| \(G\) | \(= F + pV = H - TS = k_B T \left[ -\ln Z + V \left(\frac{\partial \ln Z}{\partial V}\right)_T \right]\) |
| \(C_V\) | \(= \left(\frac{\partial U}{\partial T}\right)_V = k_B T \left[ 2 \left(\frac{\partial \ln Z}{\partial T}\right)_V + T \left(\frac{\partial^2 \ln Z}{\partial T^2}\right)_V \right]\) |

---

### Page 224

Now that we have described how the process works, we can set about practising this for different partition functions.

**Example 20.3**

**(a) Two-level system**
The partition function for a two-level system (whose energy is either \(-\Delta/2\) or \(\Delta/2\)) is given by eqn 20.2, which states that
$$Z = 2 \cosh\left(\frac{\beta\Delta}{2}\right). \tag{20.23}$$
Having obtained \(Z\), we can immediately compute the internal energy \(U\) and find that
$$U = -\frac{d\ln Z}{d\beta} = -\frac{\Delta}{2} \tanh\left(\frac{\beta\Delta}{2}\right). \tag{20.24}$$
Hence the heat capacity \(C_V\) is
$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = k_B \left(\frac{\beta\Delta}{2}\right)^2 \operatorname{sech}^2\left(\frac{\beta\Delta}{2}\right). \tag{20.25}$$
The Helmholtz function is
$$F = -k_B T \ln Z = -k_B T \ln\left[ 2 \cosh\left(\frac{\beta\Delta}{2}\right) \right], \tag{20.26}$$
and hence the entropy is
$$S = \frac{U - F}{T} = -\frac{\Delta}{2T} \tanh\left(\frac{\beta\Delta}{2}\right) + k_B \ln\left[ 2 \cosh\left(\frac{\beta\Delta}{2}\right) \right]. \tag{20.27}$$
These results are plotted in Fig. 20.4(a). At low temperature, the system is in the lower level and the internal energy \(U\) is \(-\Delta/2\). The entropy \(S\) is \(k_B \ln \Omega\), where \(\Omega\) is the degeneracy and hence \(\Omega = 1\) and so \(S = k_B \ln 1 = 0\). At high temperature, the two levels are each occupied with probability \(\frac{1}{2}\), \(U\) therefore tends to 0 (which is halfway between \(-\Delta/2\) and \(\Delta/2\)), and the entropy tends to \(k_B \ln 2\) as expected. The entropy rises as the temperature increases because it reflects the freedom of the system to exist in different states, and at high temperature the system has more freedom (in that it can exist in either of the two states). Conversely, cooling corresponds to a kind of “ordering” in which the system can only exist in one state (the lower), and this gives rise to a reduction in the entropy.

---

### Page 225

[Image: Three graphs, each with two columns. Column (a) shows U, S, and C_V for a two-state system. Column (b) shows U, S, and C_V for a simple harmonic oscillator.]
**Fig. 20.4** The internal energy \(U\), the entropy \(S\), and the heat capacity \(C_V\) for (a) the two-state system (with energy levels \(\pm\Delta/2\)) and (b) the simple harmonic oscillator.

The heat capacity is very small both (i) at low temperature (\(k_B T \ll \Delta\)) and (ii) at very high temperature (\(k_B T \gg \Delta\)), because changes in temperature have no effect on the internal energy when (i) the temperature is so low that only the lower level is occupied and even a small change in temperature won’t alter that, and (ii) the temperature is so high that both levels are occupied equally and a small change in temperature won’t alter this. At very low temperature, it is hard to change the energy of the system because there is not enough energy to excite transitions from the ground state and therefore the system is “stuck”. At very high temperature, it is hard to change the energy of the system because both states are equally occupied. In between, roughly around a temperature \(T \approx \Delta/k_B\), the heat capacity rises to a maximum, known as a **Schottky anomaly**\(^2\), as shown in the lowest panel of Fig. 20.4(a). This arises because at this temperature, it is possible to thermally excite transitions between the two states of the system. Note, however, that the Schottky anomaly is not a sharp peak, cusp, or spike, as might be associated with a phase transition (see Section 28.7), but is a smooth, fairly broad maximum.

> \(^2\)Walter Schottky (1886–1976).

---

### Page 226

**(b) Simple harmonic oscillator**
The partition function for the simple harmonic oscillator (from eqn 20.3) is
$$Z = \frac{e^{-\frac{1}{2}\beta\hbar\omega}}{1 - e^{-\beta\hbar\omega}}. \tag{20.28}$$
Hence (referring to Table 20.1), we find that \(U\) is given by
$$U = -\frac{d\ln Z}{d\beta} = \hbar\omega \left( \frac{1}{2} + \frac{1}{e^{\beta\hbar\omega} - 1} \right) \tag{20.29}$$
and hence that \(C_V\) is
$$C_V = \left(\frac{\partial U}{\partial T}\right)_V = k_B (\beta\hbar\omega)^2 \frac{e^{\beta\hbar\omega}}{(e^{\beta\hbar\omega} - 1)^2}. \tag{20.30}$$
At high temperature, \(\beta\hbar\omega \ll 1\) and so \((e^{\beta\hbar\omega} - 1) \approx \beta\hbar\omega\) and \(C_V \to k_B\) (the equipartition result). Similarly, \(U \to \frac{\hbar\omega}{2} + k_B T \approx k_B T\). The Helmholtz function is (referring to Table 20.1)
$$F = -k_B T \ln Z = \frac{\hbar\omega}{2} + k_B T \ln(1 - e^{-\beta\hbar\omega}), \tag{20.31}$$
and hence the entropy is (referring again to Table 20.1)
$$S = \frac{U - F}{T} = k_B \left[ \frac{\beta\hbar\omega}{e^{\beta\hbar\omega} - 1} - \ln(1 - e^{-\beta\hbar\omega}) \right]. \tag{20.32}$$
These results are plotted in Fig. 20.4(b). At absolute zero, only the lowest level is occupied, so the internal energy is \(\frac{1}{2}\hbar\omega\) and the entropy is \(k_B \ln 1 = 0\). The heat capacity is also zero. As the temperature rises, more and more energy levels in the ladder can be occupied, and \(U\) rises without limit. The entropy also rises (and follows a dependence which is approximately \(k_B \ln(k_B T/\hbar\omega)\) where \(k_B T/\hbar\omega\) is approximately the number of occupied levels). Both functions carry on rising because the ladder of energy levels increases without limit. The heat capacity rises to a plateau at \(C_V = k_B\), which is the equipartition result (see eqn 19.13).

The results for two further examples are plotted in Fig. 20.5 and are shown without derivation. The first is an \(N\)-level system and is shown in Fig. 20.5(a). At low temperature, the behaviour of the thermodynamic functions resembles that of the simple harmonic oscillator, but at higher temperature, \(U\) and \(S\) begin to saturate and \(C_V\) falls, because the system has a limited number of energy levels.

---

### Page 227

[Image: Two graphs, each with three columns. Column (a) shows U, S, and C_V for an N-level system (N=20). Column (b) shows U, S, and C_V for a rotating diatomic molecule.]
**Fig. 20.5** The internal energy \(U\), the entropy \(S\), and the heat capacity \(C_V\) for (a) the N-level system (the simulation is shown for \(N = 20\)) and (b) the rotating diatomic molecule (in this case \(\Delta = \hbar^2/2I\) where \(I\) is the moment of inertia).

Fig. 20.5(b) shows calculations for the rotating diatomic molecule. This resembles the simple harmonic oscillator at higher temperature (the heat capacity saturates at \(C_V = k_B\)) but differs at low temperature owing to the detailed difference in the structure of the energy levels. At high temperature, the heat capacity is given by the equipartition result (see eqn 19.13). This can be verified directly using the partition function, which, at high temperature, can be represented by the following integral:
$$Z = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\Delta J(J+1)} \approx \int_0^{\infty} (2J + 1)e^{-\beta\Delta J(J+1)} dJ, \tag{20.33}$$
where \(\Delta = \hbar^2/2I\). Using
$$\frac{d}{dJ} e^{-\beta\Delta J(J+1)} = -(2J + 1)\beta\Delta e^{-\beta\Delta J(J+1)},$$
we have that
$$Z = -\left[ \frac{1}{\beta\Delta} e^{-\beta\Delta J(J+1)} \right]_0^{\infty} = \frac{1}{\beta\Delta}. \tag{20.35}$$
This implies that \(U = -d\ln Z/d\beta = 1/\beta = k_B T\) and hence \(C_V = (dU/dT)_V = k_B\).

---

### Page 228

#### 20.3 The big idea

The examples above illustrate the “big idea” of statistical mechanics: you describe a system by its energy levels \(E_\alpha\) and evaluate its properties by following the prescription given by the two steps:

(1) Write down \(Z = \sum_\alpha e^{-\beta E_\alpha}\).
(2) Evaluate various functions of state using the expressions given in Table 20.1.

And that’s really all there is to it!\(^3\)

> \(^3\)Well, almost. The Schrödinger equation can only be solved for a few systems, and if you don’t know the energy levels of your system, you can’t write down \(Z\). Fortunately, there are quite a number of systems for which you can solve the Schrödinger equation, some of which we are considering in this chapter, and they describe lots and lots of important physical systems, enough to keep us going in this book!

You can understand the results by comparing the energy \(k_B T\) with the spacings between energy levels.

- If \(k_B T\) is much less than the spacing between the lowest energy level and the first excited level then the system will sit in the lowest level.
- If there are a finite set of levels and \(k_B T\) is much larger than the energy spacing between the lowest and highest levels, then each energy level will be occupied with equal probability.
- If there are an infinite ladder of levels and \(k_B T\) is much larger than the energy spacing between adjacent levels, then the mean energy rises linearly with \(T\) and one obtains a result consistent with the equipartition theorem.

---

#### 20.4 Combining partition functions

Consider the case when the energy \(E\) of a particular system depends on various independent contributions. For example, suppose it is a sum of two contributions \(a\) and \(b\), so that the energy levels are given by \(E_{i,j}\) where
$$E_{i,j} = E^{(a)}_i + E^{(b)}_j, \tag{20.36}$$
and where \(E^{(a)}_i\) is the \(i\)th level due to contribution \(a\) and \(E^{(b)}_j\) is the \(j\)th level due to contribution \(b\), so the partition function \(Z\) is
$$Z = \sum_i \sum_j e^{-\beta(E^{(a)}_i + E^{(b)}_j)} = \sum_i e^{-\beta E^{(a)}_i} \sum_j e^{-\beta E^{(b)}_j} = Z_a Z_b, \tag{20.37}$$
so that the partition functions of the independent contributions multiply. Hence also \(\ln Z = \ln Z_a + \ln Z_b\), and the effect on functions of state which depend on \(\ln Z\) is that the independent contributions add.

---

### Page 229

**Example 20.4**

(i) The partition function \(Z\) for \(N\) independent simple harmonic oscillators is given by
$$Z = Z_{\text{SHO}}^N, \tag{20.38}$$
where \(Z_{\text{SHO}} = e^{-\frac{1}{2}\beta\hbar\omega}/(1 - e^{-\beta\hbar\omega})\), from eqn 20.3, is the partition function for a single simple harmonic oscillator.

(ii) A diatomic molecule with both vibrational and rotational degrees of freedom has a partition function \(Z\) given by
$$Z = Z_{\text{vib}} Z_{\text{rot}}, \tag{20.39}$$
where \(Z_{\text{vib}}\) is the vibrational partition function \(Z_{\text{vib}} = e^{-\frac{1}{2}\beta\hbar\omega}/(1 - e^{-\beta\hbar\omega})\), from eqn 20.3, and \(Z_{\text{rot}}\) is the rotational partition function
$$Z_{\text{rot}} = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\hbar^2 J(J+1)/2I}. \tag{20.40}$$
from eqn 20.6. For a gas of diatomic molecules, we would also need a factor in the partition function corresponding to translational motion. We will derive this in the following chapter.

The final example of the chapter applies this to a simple magnetic system and allows us to derive Curie’s law.\(^4\)

> \(^4\)Curie’s law was encountered in eqn 17.32.

**Example 20.5**
**The spin-\(\frac{1}{2}\) paramagnet**

In quantum mechanics, a particle with spin angular momentum equal to \(\frac{1}{2}\), placed in a magnetic field \(B\) along the \(z\) direction, can exist in one of two eigenstates:

- \(|\uparrow\rangle\), with angular momentum parallel to the \(B\) field, and hence magnetic moment along \(z\) equal to \(-\mu_B\) (costing an energy \(+\mu_B B\)).
- \(|\downarrow\rangle\), with angular momentum antiparallel to the \(B\) field, and hence magnetic moment along \(z\) equal to \(+\mu_B\) (costing an energy \(-\mu_B B\)).

Here \(\mu_B = e\hbar/2m\) is the Bohr magneton and we have used the fact that energy = \(-\mathbf{m} \cdot \mathbf{B}\), and also that for a negatively charged particle (the electron) the angular momentum is antiparallel to the magnetic moment.

One spin-\(\frac{1}{2}\) particle thus behaves like a two-state system, with the two states having energy \(E\) given by: \(E = \mu_B B\) and \(E = -\mu_B B\). Therefore, the single-particle partition function (which we will call \(Z_1\)) is simply
$$Z_1 = e^{\beta\mu_B B} + e^{-\beta\mu_B B} = 2 \cosh(\beta\mu_B B). \tag{20.41}$$

---

### Page 230

A spin-\(\frac{1}{2}\) paramagnet is an assembly of \(N\) such particles, which are assumed to be non-interacting: thus each particle is independent and “does its own thing”. Note that although it might be energetically favourable for all the spins to line up along the magnetic field, producing a state like
\(\cdots \uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\cdots\)
such a state is not very likely: there is only one microstate associated with it. However, even though it is less energetically favourable, there are lots of microstates associated with having half of the states up and half of them down, e.g.
\(\cdots \uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\downarrow\downarrow\uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\uparrow\uparrow\uparrow\downarrow\uparrow\downarrow\uparrow\uparrow\downarrow\downarrow\downarrow\uparrow\cdots\)

The balance between energy \(U\) and entropy \(S\) is encoded in the Helmholtz function \(F = U - TS\) which shows that entropy becomes more important as \(T\) gets larger, whereas \(U\) is more relevant at low temperature.

Because the spins do not interact with each other the \(N\)-particle partition function \(Z_N\) can be obtained by multiplying \(N\) single-particle partition functions (using the result in eqn 20.37 for combining partition functions of independent systems). Therefore
$$Z_N = Z_1^N, \tag{20.42}$$
and hence \(F\) is given by
$$F = -k_B T \ln Z_N = -N k_B T \ln [2 \cosh(\beta\mu_B B)]. \tag{20.43}$$

We can work out the magnetic moment \(m\) of the paramagnet by computing
$$m = -\left(\frac{\partial F}{\partial B}\right)_T = N\mu_B \tanh(\beta\mu_B B), \tag{20.44}$$
(see Fig. 20.6) and it is worth considering this equation for a moment. Note that when \(B\) gets very big (or \(T\) gets very small), the magnetic moment tends to \(N\mu_B\), corresponding to all the magnetic moments pointing up, i.e., to a state like
\(\cdots \uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\cdots\)
On the other hand, if \(B\) is very small (or \(T\) gets very large), the magnetic moment tends to zero, corresponding to a state in which half of the magnetic moments are up and half are down, i.e., to a state like
\(\cdots \uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\downarrow\downarrow\uparrow\uparrow\downarrow\uparrow\downarrow\downarrow\uparrow\downarrow\uparrow\uparrow\uparrow\downarrow\uparrow\downarrow\uparrow\uparrow\downarrow\downarrow\downarrow\uparrow\cdots\)

We now want to calculate the magnetic susceptibility and show that it leads to what is known as Curie’s law. Here is how we do it: the magnetization \(M\) is the magnetic moment per unit volume, so writing the volume of the paramagnet as \(V\) we have
$$M = \frac{m}{V} = \frac{N\mu_B}{V} \tanh(\beta\mu_B B). \tag{20.45}$$

---

### Page 231

[Image: A 3D plot of magnetic moment m versus field B and temperature T, showing a smooth surface that saturates at high B and low T.]
**Fig. 20.6** The behaviour of the magnetic moment \(m\) as a function of field \(B\) and temperature \(T\) for a spin-\(\frac{1}{2}\) paramagnet, as given by eqn 20.44.

Magnetic susceptibility is measured in a very weak field, so we can look in the limit when \(B\) is small so that \(\beta\mu_B \ll 1\) and use \(\tanh x \approx x\) for \(x \ll 1\), and hence have that
$$M \approx \frac{N\mu_B^2 B}{V k_B T}. \tag{20.46}$$
Recall that \(B = \mu_0(H + M)\), but for a weakly magnetic material (like a paramagnet), \(M \approx \chi H\) and \(\chi \ll 1\) is the magnetic susceptibility.\(^5\) Thus we can write that
$$B \approx \mu_0(1 + \chi)H \approx \frac{\mu_0 M}{\chi}$$
and hence
$$\chi \approx \frac{\mu_0 M}{B}. \tag{20.47}$$
This implies that
$$\chi \approx \frac{N\mu_0 \mu_B^2}{V k_B T}. \tag{20.48}$$
This result obeys Curie’s law: \(\chi \propto 1/T\).

> \(^5\)See eqn 17.30.

---

### Chapter summary

- The partition function \(Z = \sum_\alpha e^{-\beta E_\alpha}\) contains the information needed to find many thermodynamic properties.
- The equations \(U = -d\ln Z/d\beta\), \(F = -k_B T \ln Z\), \(S = (U - F)/T\), \(p = -\left(\frac{\partial F}{\partial V}\right)_T\), \(H = U + pV\), \(G = H - TS\) can be used to generate the relevant thermodynamic properties from \(Z\).

---

### Page 232

### Exercises

**(20.1)** Show that at high temperature, such that \(k_B T \gg \hbar\omega\), the partition function of the simple harmonic oscillator is approximately \(Z \approx (\beta\hbar\omega)^{-1}\). Hence find \(U, C, F\), and \(S\) at high temperature. Repeat the problem for the high temperature limit of the rotational energy levels of the diatomic molecule for which \(Z \approx (\beta\hbar^2/2I)^{-1}\) (see eqn 20.35).

**(20.2)** Show that
$$\ln P_j = \beta(F - E_j). \tag{20.49}$$

**(20.3)** Show that eqn 20.29 can be rewritten as
$$U = \frac{\hbar\omega}{2} \coth\left(\frac{\beta\hbar\omega}{2}\right), \tag{20.50}$$
and eqn 20.32 can be rewritten as
$$S = k_B \left[ \frac{\hbar\omega}{2} \coth\left(\frac{\beta\hbar\omega}{2}\right) - \ln\left( 2 \sinh\left(\frac{\beta\hbar\omega}{2}\right) \right) \right]. \tag{20.51}$$

**(20.4)** Show that the zero-point energy of a simple harmonic oscillator does not contribute to its entropy or heat capacity, but does contribute to its internal energy and Helmholtz function.

**(20.5)** Show that for \(N\) non-interacting spin-\(\frac{1}{2}\) particles in a magnetic field \(B\) the energy \(U\) is given by
$$U = -N\mu_B B \tanh\left(\frac{\mu_B B}{k_B T}\right), \tag{20.52}$$
the heat capacity is given by
$$\frac{C}{N k_B} = \left(\frac{\mu_B B}{k_B T}\right)^2 \operatorname{sech}^2\left(\frac{\mu_B B}{k_B T}\right), \tag{20.53}$$
and the entropy is given by
$$\frac{S}{N k_B} = \ln\left[ 2 \cosh\left(\frac{\mu_B B}{k_B T}\right) \right] - \frac{\mu_B B}{k_B T} \tanh\left(\frac{\mu_B B}{k_B T}\right). \tag{20.54}$$

**(20.6)** A certain magnetic system contains \(n\) independent molecules per unit volume, each of which has four energy levels given by \(0, \Delta - g\mu_B B, \Delta, \Delta + g\mu_B B\) (\(g\) is a constant). Write down the partition function, compute the Helmholtz function and hence compute the magnetization \(M\). Hence show that the magnetic susceptibility \(\chi\) is given by
$$\chi = \lim_{B \to 0} \frac{\mu_0 M}{B} = \frac{2n\mu_0 g^2 \mu_B^2}{k_B T(3 + e^{\Delta/k_B T})}. \tag{20.55}$$

**(20.7)** The energy \(E\) of a system of three independent harmonic oscillators is given by
$$E = (n_x + \tfrac{1}{2})\hbar\omega + (n_y + \tfrac{1}{2})\hbar\omega + (n_z + \tfrac{1}{2})\hbar\omega. \tag{20.56}$$
Show that the partition function \(Z\) is given by
$$Z = Z_{\text{SHO}}^3, \tag{20.57}$$
where \(Z_{\text{SHO}}\) is the partition function of a simple harmonic oscillator given in eqn 20.3. Hence show that the Helmholtz function is given by
$$F = \frac{3}{2}\hbar\omega + 3k_B T \ln(1 - e^{-\beta\hbar\omega}), \tag{20.58}$$
and that the heat capacity tends to \(3k_B\) at high temperature.

**(20.8)** The internal levels of an isolated hydrogen atom are given by \(E = -R/n^2\) where \(R = 13.6\) eV. The degeneracy of each level is given by \(2n^2\).
(a) Sketch the energy levels.
(b) Show that
$$Z = \sum_{n=1}^{\infty} 2n^2 \exp\left(\frac{R}{n^2 k_B T}\right). \tag{20.59}$$
Note that when \(T \neq 0\), this expression for \(Z\) diverges. This is because of the large degeneracy of the hydrogen atom’s highly excited states. If the hydrogen atom were to be confined in a box of finite size, this would cut off the highly excited states and \(Z\) would not then diverge. By approximating \(Z\) as follows:
$$Z \approx \sum_{n=1}^{2} 2n^2 \exp\left(\frac{R}{n^2 k_B T}\right), \tag{20.60}$$
i.e., by ignoring all but the \(n=1\) and \(n=2\) states, estimate the mean energy of a hydrogen atom at 300 K.

**(20.9)** The energy of a paramagnet can be written as \(U = -\mathbf{m} \cdot \mathbf{B}\). Writing \(TS = U + F\), show that if \(B\) is varied isothermally then
$$T \delta S = -\mathbf{B} \cdot \delta \mathbf{m}. \tag{20.61}$$
[Hint: use \(\mathbf{m} = -(\partial F/\partial B)_T\).] Show that this is consistent with \(\delta U = T \delta S - \mathbf{m} \cdot \delta \mathbf{B}\) (as in eqn 17.29).

---

Here is the **complete and corrected Markdown conversion for Chapter 21 (Pages 233–243)**.

---

## Chapter 21: Statistical mechanics of an ideal gas

### Page 233

#### Chapter Outline

**21.1 Density of states** 233
**21.2 Quantum concentration** 235
**21.3 Distinguishability** 236
**21.4 Functions of state of the ideal gas** 237
**21.5 Gibbs paradox** 240
**21.6 Heat capacity of a diatomic gas** 241
**Chapter summary** 242
**Exercises** 243

The partition function is a sum over all the states of a system of the relevant Boltzmann factors. As we saw in Chapter 20, constructing the partition function is the first step to deriving all the thermodynamic properties of a system. A very important example of this technique is the ideal gas. To determine the partition function of an ideal gas, we have to know what the relevant energy levels are so that we can label the states of the system. Our first step, outlined in the following section, is to work out how many states lie in a certain energy or momentum interval, and this leads us to the density of states to be defined below.

#### 21.1 Density of states

Consider a cubical box of dimensions \(L \times L \times L\) and volume \(V = L^3\). The box is filled with gas molecules, and we want to consider the momentum states of these gas molecules. It is convenient to label each molecule (we assume that each has mass \(m\)) in the gas by its momentum \(\mathbf{p}\) divided by \(\hbar\), i.e., by its wave vector \(\mathbf{k} = \mathbf{p}/\hbar\). We assume that the molecules behave like free particles inside the box, but that they are completely confined within the walls of the box. Their wave functions are thus the solution to the Schrödinger equation for the three-dimensional particle-in-a-box problem.\(^1\) We can hence write the wave function of a molecule with wave vector \(\mathbf{k}\) as\(^2\)
$$\psi(x, y, z) = \left(\frac{2}{L}\right)^{3/2} \sin(k_x x) \sin(k_y y) \sin(k_z z). \tag{21.1}$$
The factor \((2/L)^{3/2}\) is simply to ensure that the wave function is normalized over the volume of the box, so that \(\int |\psi(x, y, z)|^2 dV = 1\). Since the molecules are confined inside the box, we want this wave function to go to zero at the boundaries of the box (the six planes \(x=0, x=L, y=0, y=L, z=0, z=L\)) and this will occur if
$$k_x = \frac{n_x \pi}{L}, \quad k_y = \frac{n_y \pi}{L}, \quad k_z = \frac{n_z \pi}{L}, \tag{21.2}$$
where \(n_x, n_y,\) and \(n_z\) are integers. We can thus label each state by this triplet of integers.

> \(^1\)We here assume familiarity with basic quantum mechanics.
> \(^2\)This wave function is a sum of plane waves travelling in opposite directions. Thus, in this treatment, \(k_x, k_y,\) and \(k_z\) can only be positive since negating any of them results in the same probability density \(|\psi(x, y, z)|^2\).

---

### Page 234

An allowed state can be represented by a point in three-dimensional \(\mathbf{k}\)-space, and these points are uniformly distributed [in each direction, points are separated by a distance \(\pi/L\), see Fig. 21.1(a)]. A single point in \(\mathbf{k}\)-space occupies a volume
$$\frac{\pi}{L} \times \frac{\pi}{L} \times \frac{\pi}{L} = \left(\frac{\pi}{L}\right)^3. \tag{21.3}$$

Let us now focus on the magnitude of the wave vector given by \(k = |\mathbf{k}|\). Allowed states with a wave vector whose magnitude lies between \(k\) and \(k + dk\) lie on one octant of a spherical shell of radius \(k\) and thickness \(dk\) (see Fig. 21.1(b)). It is just one octant since we only allow positive wave vectors in this approach. The volume of this shell is therefore
$$\frac{1}{8} \times 4\pi k^2 dk. \tag{21.4}$$

The number of allowed states with a wave vector whose magnitude lies between \(k\) and \(k + dk\) is described by the function \(g(k) dk\), where \(g(k)\) is the **density of states**. This number is then given by
$$g(k) dk = \frac{\text{volume in } \mathbf{k}\text{-space of one octant of a spherical shell}}{\text{volume in } \mathbf{k}\text{-space occupied per allowed state}}. \tag{21.5}$$
This implies that
$$g(k) dk = \frac{\frac{1}{8} \times 4\pi k^2 dk}{(\pi/L)^3} = \frac{V k^2 dk}{2\pi^2}. \tag{21.6}$$

**Example 21.1**
An alternative method of calculating eqn 21.6 is to centre the box of gas at the origin, so that it is bounded by the planes \(x = \pm L/2, y = \pm L/2\) and \(z = \pm L/2\), and to apply periodic boundary conditions.

[Image: Three diagrams (a), (b), and (c). (a) shows a grid of points in the first octant of k-space, with spacing pi/L. (b) shows one octant of a spherical shell of radius k and thickness dk. (c) shows a full sphere in k-space with spacing 2pi/L between points.]
**Fig. 21.1** (a) States in k-space are separated by \(\pi/L\). Each state occupies a volume \((\pi/L)^3\). (b) The density of states can be calculated by considering the volume in k-space between states with wave vector \(k\) and states with wave vector \(k+dk\), namely \(4\pi k^2 dk\). One octant of the sphere is shown. (c) In Example 21.1, our alternative formulation allows states in k-space to have positive or negative wave vectors and these states are separated by \(2\pi/L\). Each state now occupies a volume \((2\pi/L)^3\).

In this case, the wave function is given by
$$\psi(x, y, z) = \frac{1}{V^{1/2}} e^{i\mathbf{k}\cdot\mathbf{r}} = \frac{1}{V^{1/2}} e^{ik_x x} e^{ik_y y} e^{ik_z z}. \tag{21.7}$$
The periodic boundary conditions can now be applied:
$$\psi\left(\frac{L}{2}, y, z\right) = \psi\left(-\frac{L}{2}, y, z\right), \tag{21.8}$$
implies that
$$e^{ik_x L/2} = e^{-ik_x L/2}, \tag{21.9}$$
and hence
$$k_x = \frac{2\pi n_x}{L}, \tag{21.10}$$
where \(n_x\) is an integer. Similarly we have that
$$k_y = \frac{2n_y \pi}{L}, \quad \text{and} \quad k_z = \frac{2n_z \pi}{L}. \tag{21.11}$$

---

### Page 235

The points in \(\mathbf{k}\)-space are now spaced twice as far apart than in our earlier treatment (see Fig. 21.1(c)), but \(n_x, n_y,\) and \(n_z\) can now be positive or negative, meaning that a complete sphere of values in \(\mathbf{k}\)-space is used in this formalism. Thus the density of states is now
$$g(k) dk = \frac{\text{volume in } \mathbf{k}\text{-space of a complete spherical shell}}{\text{volume in } \mathbf{k}\text{-space occupied per allowed state}}. \tag{21.12}$$
This implies that
$$g(k) dk = \frac{4\pi k^2 dk}{(2\pi/L)^3} = \frac{V k^2 dk}{2\pi^2}, \tag{21.13}$$
as before in eqn 21.6.

Having calculated the density of states in eqn 21.6 (and identically in eqn 21.13), we are now in a position to calculate the partition function of an ideal gas.

---

#### 21.2 Quantum concentration

The single-particle partition function\(^3\) for the ideal gas is given by a generalization of eqn 20.1 in which we replace the sum by an integral. Hence we have
$$Z_1 = \int_0^{\infty} e^{-\beta E(k)} g(k) dk, \tag{21.14}$$
where the energy of a single molecule with wave vector \(\mathbf{k}\) is given by
$$E(k) = \frac{\hbar^2 k^2}{2m}. \tag{21.15}$$
Hence,
$$Z_1 = \int_0^{\infty} e^{-\beta\hbar^2 k^2/2m} \frac{V k^2 dk}{2\pi^2} = \frac{V}{\hbar^3} \left(\frac{m k_B T}{2\pi}\right)^{3/2}, \tag{21.16}$$
which can be written in the appealingly simple form
$$Z_1 = V n_Q, \quad \text{where} \quad n_Q = \frac{1}{\hbar^3} \left(\frac{m k_B T}{2\pi}\right)^{3/2}, \tag{21.17}$$
where \(n_Q\) is known as the **quantum concentration**. We can define \(\lambda_{\text{th}}\), the **thermal wavelength**, as follows:
$$\lambda_{\text{th}} = n_Q^{-1/3} = \frac{h}{\sqrt{2\pi m k_B T}}, \tag{21.18}$$
and hence we can also write
$$Z_1 = \frac{V}{\lambda_{\text{th}}^3}. \tag{21.19}$$
Equation 21.17 (and 21.19) brings out the important fact that the partition function is proportional to the volume of the system (and also proportional to temperature to the power of \(3/2\)). The importance of this will be seen in the following section.

> \(^3\)There is a distinction between the partition function associated with “single-particle states” (where we focus our attention only on a single particle in our system, assuming it has freedom to exist in any state without having to worry about not occupying a state that has already been taken by another particle) and the partition function associated with the whole system. This point will be made clear in the following section. However, we will introduce the subscript 1 at this point to remind ourselves that we are thinking about single-particle states.

---

### Page 236

#### 21.3 Distinguishability

In this section, we want to attempt to understand what happens for our gas of \(N\) molecules, moving on from considering only single–particle states to considering the \(N\)-particle state. This is a surprisingly subtle point and to see why, we study the following, much simpler, example.

**Example 21.2**
Consider a particle which can exist in two states. We model this particle as a thermodynamic system in which the energy can be either \(0\) or \(\epsilon\). The two states of the system are shown in Fig. 21.2(a) and the single-partition function is
$$Z_1 = e^0 + e^{-\beta\epsilon} = 1 + e^{-\beta\epsilon}. \tag{21.20}$$

Now consider two such particles, which behave in the same way, and let us suppose that they are **distinguishable** (for example, they might have different physical locations, or they might have some different attribute, like colour). The possible states of the combined system are shown in Fig. 21.2(b), and we have made them distinguishable in the diagram by depicting them with different symbols. In this case we can write down the two-particle partition function \(Z_2\) as a sum over those four possible states, and hence
$$Z_2 = e^0 + e^{-\beta\epsilon} + e^{-\beta\epsilon} + e^{-2\beta\epsilon}, \tag{21.21}$$
and in this case we see that
$$Z_2 = (Z_1)^2. \tag{21.22}$$
In much the same way, we could work out the \(N\)-particle partition function for \(N\) distinguishable particles and show that it is given by
$$Z_N = (Z_1)^N. \tag{21.23}$$

[Image: Three diagrams (a), (b), and (c). (a) shows a particle in one of two energy levels, 0 or epsilon. (b) shows two distinguishable particles (one circle, one square) occupying four possible states: both on 0, one on 0 and one on epsilon, one on epsilon and one on 0, both on epsilon. (c) shows two indistinguishable particles (both circles) occupying three possible states: both on 0, one on 0 and one on epsilon, both on epsilon.]
**Fig. 21.2** (a) A particle is described by a two-state system with energy \(0\) or \(\epsilon\). (b) The possible states for two such particles if they are distinguishable. (c) The possible states for two such particles if they are indistinguishable.

However, what happens if the particles are **indistinguishable**? Returning to the combination of two systems, there are now only three possible states of the combined system, as shown in Fig. 21.2(c). The partition function is now
$$Z_2 = e^0 + e^{-\beta\epsilon} + e^{-2\beta\epsilon} \neq (Z_1)^2. \tag{21.24}$$
What has happened is that \((Z_1)^2\) correctly accounts for those states in which the particles are in the same energy level, but has overcounted (by a factor of two) those states in which the particles are in different energy levels. Similarly, for \(N\) indistinguishable particles, the \(N\)-particle partition function \(Z_N \neq (Z_1)^N\) because \((Z_1)^N\) overcounts states in which all \(N\) particles are in different states by a factor of \(N!\).

---

### Page 237

Let us summarize the results of this example. If the \(N\) particles are distinguishable, then we can write the \(N\)-particle partition function \(Z_N\) as
$$Z_N = (Z_1)^N. \tag{21.25}$$
If they are indistinguishable, then it is much more complicated.\(^4\) However, we can make a rather crafty approximation, as follows. If it is possible to ignore those configurations in which two or more particles are occupying the same energy level, then we can assume exactly the same answer as the distinguishable case and so we only have to worry about the single overcounting factor, which we make when we ignore indistinguishability. If we have \(N\) particles all in different states, then that overcounting factor is \(N!\) (the number of different arrangements of \(N\) distinguishable particles on \(N\) distinct sites). Hence we can write the \(N\)-particle partition function \(Z_N\) for indistinguishable particles as
$$Z_N = \frac{(Z_1)^N}{N!}. \tag{21.26}$$
This result has assumed that it is possible to ignore those states in which two or more particles occupy the same energy level. When is this approximation possible? We will have only one particle occupying any given state if the system is in a regime when the number of available states is much larger than the number of particles. So for the ideal gas, we require that the number of thermally accessible energy levels must be much larger than the number of molecules in the gas. This occurs when \(n\), the number density of molecules, is much less than the quantum concentration \(n_Q\). Thus the condition for validity of eqn 21.26 for an ideal gas is
$$n \ll n_Q. \tag{21.27}$$

If this condition holds, the \(N\)-particle partition function for an ideal gas can be written as
$$Z_N = \frac{1}{N!} \left(\frac{V}{\lambda_{\text{th}}^3}\right)^N. \tag{21.28}$$

> \(^4\)Note that identical (and hence indistinguishable) particles can be made to be distinguishable if they are localized. The particles can then be distinguished by their physical location. Electrons in a gas are indistinguishable if there is no means of labelling which is which, but the electrons sitting in a particular magnetic orbital, one per atom of a magnetic solid, are distinguishable.

The quantum concentration \(n_Q\) is plotted in Fig. 21.3 for electrons, protons, \(N_2\) molecules, and \(C_{60}\) molecules (known as buckyballs). At room temperature, the quantum concentration of \(N_2\) molecules is much higher than the actual number density of molecules in air (\(\approx 10^{25} \text{ m}^{-3}\)) and so the approximation in eqn 21.26 is a good one. Electrons in a metal have a concentration \(\approx 10^{29} \text{ m}^{-3}\), which is larger than the quantum concentration for electrons at room temperature, so the approximation in eqn 21.26 will not work for electrons and their quantum properties have to be considered in more detail.

---

#### 21.4 Functions of state of the ideal gas

Having obtained the partition function of an ideal gas, we are now in a position to use the machinery of statistical mechanics, developed in Chapter 20, to derive all the relevant thermodynamic properties. This we do in the following example.

[Image: A plot showing the quantum concentration n_Q and thermal wavelength lambda_th as a function of temperature for electrons, protons, N2 molecules, and C60 buckyballs. The plot shows that n_Q increases with T and is larger for lighter particles.]
**Fig. 21.3** The quantum concentration \(n_Q\) and thermal wavelength \(\lambda_{\text{th}}\) for electrons, protons, \(N_2\) molecules, and buckyballs.

---

### Page 238

**Example 21.3**
The partition function for \(N\) molecules in a gas is given in eqn 21.28 by
$$Z_N = \frac{1}{N!} \left(\frac{V}{\lambda_{\text{th}}^3}\right)^N \propto (V T^{3/2})^N, \tag{21.29}$$
since \(\lambda_{\text{th}} \propto T^{-1/2}\). Hence we can write
$$\ln Z_N = N \ln V + \frac{3N}{2} \ln T + \text{constants}. \tag{21.30}$$
The internal energy \(U\) is given by
$$U = -\frac{d\ln Z_N}{d\beta} = \frac{3}{2} N k_B T, \tag{21.31}$$
so that the heat capacity is \(C_V = \frac{3}{2} N k_B\), in agreement with previous results.

---

### Page 239

The Helmholtz function is
$$F = -k_B T \ln Z_N = -k_B T N \ln V - k_B \frac{3N}{2} T \ln T - k_B T \times \text{constants}, \tag{21.32}$$
so that
$$p = -\left(\frac{\partial F}{\partial V}\right)_T = \frac{N k_B T}{V} = n k_B T, \tag{21.33}$$
which is, reassuringly, the ideal gas equation. This also gives the enthalpy \(H\) via
$$H = U + pV = \frac{5}{2} N k_B T. \tag{21.34}$$

Before proceeding to the entropy, it is going to be necessary to worry about what the constants are in eqn 21.30. Returning to eqn 21.29, we write
$$\ln Z_N = N \ln V - 3N \ln \lambda_{\text{th}} - N \ln N + N = N \ln\left(\frac{V e}{N \lambda_{\text{th}}^3}\right), \tag{21.35}$$
where we have used Stirling’s approximation, \(\ln N! \approx N \ln N - N\) (see eqn 1.17). Hence we can obtain the following expression for the Helmholtz function \(F\):
$$F = -N k_B T \ln\left(\frac{V e}{N \lambda_{\text{th}}^3}\right) = N k_B T [\ln(n \lambda_{\text{th}}^3) - 1]. \tag{21.36}$$

This allows us to derive the entropy \(S\):
$$S = \frac{U - F}{T} = \frac{3}{2} N k_B + N k_B \ln\left(\frac{V e}{N \lambda_{\text{th}}^3}\right) = N k_B \ln\left(\frac{V e^{5/2}}{N \lambda_{\text{th}}^3}\right) = N k_B \left[ \frac{5}{2} - \ln(n \lambda_{\text{th}}^3) \right], \tag{21.37}$$
and hence the entropy is expressed in terms of the thermal wavelength of the molecules. We can also derive the Gibbs function \(G\):
$$G = H - TS = \frac{5}{2} N k_B T - N k_B T \ln\left(\frac{V e^{5/2}}{N \lambda_{\text{th}}^3}\right) = N k_B T \ln(n \lambda_{\text{th}}^3). \tag{21.38}$$

---

### Page 240

[Image: Three diagrams (a), (b), and (c). (a) shows a Joule expansion of an ideal gas into a vacuum, an irreversible process. (b) shows the mixing of two different gases, which is irreversible. (c) shows the mixing of two identical gases, which is reversible.]
**Fig. 21.4** (a) Joule expansion of an ideal gas (an irreversible process). (b) Mixing of two different gases, equivalent to the Joule expansion of each of the gases (an irreversible process). (c) Mixing of two identical gases, which is clearly a reversible process – how can you tell if they have been mixed?

---

#### 21.5 Gibbs paradox

The expression for the entropy in eqn 21.37 is called the **Sackur–Tetrode equation** and can be used to demonstrate the **Gibbs paradox**.

Consider the process shown in Fig. 21.4(a), namely the Joule expansion of \(N\) molecules of an ideal gas. This is an irreversible process which halves the number density \(n\) so that the increase in entropy is given by
$$\Delta S = S_{\text{final}} - S_{\text{initial}} = N k_B \left[ \frac{5}{2} - \ln\left(\frac{n}{2} \lambda_{\text{th}}^3\right) \right] - N k_B \left[ \frac{5}{2} - \ln(n \lambda_{\text{th}}^3) \right] = N k_B \ln 2, \tag{21.39}$$
in agreement with eqn 14.29. This reflects the fact that, following the Joule expansion, we have an uncertainty about each molecule as to whether it is on the left- or right-hand side of the chamber, whereas beforehand there was no uncertainty (all molecules were on the left-hand side). Hence the uncertainty is one bit per molecule, and hence \(\Delta S/k_B = N \ln 2\).

Now consider the situation depicted in Fig. 21.4(b) in which two **different** gases are allowed to mix following the removal of a partition which separated them. This is clearly an irreversible process and is equivalent to the Joule expansion of each gas. Thus the entropy increase is
$$\Delta S = 2 N k_B \ln 2. \tag{21.40}$$

An apparently similar case is shown in Fig. 21.4(c), but this time the two gases on either side of the partition are **indistinguishable**. Removing the partition is now an eminently reversible operation so \(\Delta S = 0\). Yet, it might be argued, is it not the case that the removal of the partition simply allows the gases which were initially on either side of the partition to each undergo a Joule expansion? Surely, the change of entropy would then be \(\Delta S = 2 N k_B \ln 2\). This apparent paradox is resolved by understanding that indistinguishable really means indistinguishable! In other words, the case shown in Fig. 21.4(c) is fundamentally different from that shown in Fig. 21.4(b). Removing the partition in the case of Fig. 21.4(c) is a reversible operation since we have no way of losing information about which side of the partition certain bits of gas are; this is because all molecules of this gas look the same to us and we never had such information in the first place. Hence \(\Delta S = 0\).

Gibbs resolved this paradox himself by realizing that indistinguishability was fundamental and that all states of the system that differ only by a permutation of identical molecules should be considered as the same state. Failure to do this results in an expression for the entropy that is not extensive (see Exercise 21.2, which was the original manifestation of the Gibbs paradox).

---

#### 21.6 Heat capacity of a diatomic gas

The energy of a diatomic molecule in a gas can be written using eqn 19.19 as the sum of three translational, two rotational, and two vibrational terms, giving seven modes in total. The equipartition theorem shows that the mean energy per molecule at high temperature is therefore \(\frac{7}{2} k_B T\) (see eqn 19.20). Because the modes are independent, the partition function of a diatomic molecule, \(Z\), can be written as the product of partition functions for the translational, rotational and vibrational modes as
$$Z = Z_{\text{trans}} Z_{\text{vib}} Z_{\text{rot}}, \tag{21.41}$$
where \(Z_{\text{trans}} = V/\lambda_{\text{th}}^3\) from eqn 21.19, \(Z_{\text{vib}} = e^{-\frac{1}{2}\beta\hbar\omega}/(1 - e^{-\beta\hbar\omega})\), from eqn 20.3, and \(Z_{\text{rot}}\) is the rotational partition function
$$Z_{\text{rot}} = \sum_{\alpha} e^{-\beta E_\alpha} = \sum_{J=0}^{\infty} (2J + 1)e^{-\beta\hbar^2 J(J+1)/2I}, \tag{21.42}$$
from eqn 20.6. Thus the mean energy \(U\) of such a diatomic molecule is given by \(U = -d\ln Z/d\beta\) and is the sum of the energies of the individual modes. Similarly, the heat capacity \(C_V\) is the sum of the heat capacities of the individual modes. This gives rise to the behaviour shown in Fig. 21.5 in which the heat capacity goes through a series of plateaus:

---

### Page 242

[Image: A graph of molar heat capacity at constant volume C_V versus temperature for a diatomic gas. The curve rises in three steps: from 0 to 3/2 R at low T, then to 5/2 R at intermediate T, and finally to 7/2 R at high T.]
**Fig. 21.5** The molar heat capacity at constant volume of a diatomic gas as a function of temperature.

at any non-zero temperature, all the translational modes are excited (a failure of the ideal gas model, because \(C_V\) should go to zero as \(T \to 0\), see Chapter 18) and \(C_V = \frac{3}{2} R\) (for one mole of gas); above \(T \approx \hbar^2/2 I k_B\) the rotational modes are also excited and \(C_V\) rises to \(\frac{5}{2} R\); above \(T \approx \hbar\omega/k_B\), the vibrational modes are excited and hence \(C_V\) rises to \(\frac{7}{2} R\).

---

### Chapter summary

- For an ideal gas, the partition function can be written
$$Z = V/\lambda_{\text{th}}^3,$$
where \(\lambda_{\text{th}} = h/\sqrt{2\pi m k_B T}\) is the thermal wavelength.
- The quantum concentration \(n_Q = 1/\lambda_{\text{th}}^3\).
- The \(N\)-particle partition function is given by
$$Z_N = \frac{(Z_1)^N}{N!}$$
for indistinguishable particles in the low-density case when \(n/n_Q \ll 1\) so that \(n\lambda_{\text{th}}^3 \ll 1\).

---

### Page 243

### Exercises

**(21.1)** Show that the single-partition function \(Z_1\) of a two-dimensional gas confined in an area \(A\) is given by
$$Z_1 = \frac{A}{\lambda_{\text{th}}^2}, \tag{21.43}$$
where \(\lambda_{\text{th}} = h/\sqrt{2\pi m k_B T}\).

**(21.2)** Show that \(S\) as given by eqn 21.37 (the Sackur–Tetrode equation) is an extensive quantity, but that the entropy of a gas of distinguishable particles is given by
$$S = N k_B \left[ \frac{3}{2} - \ln(\lambda_{\text{th}}^3/V) \right], \tag{21.44}$$
and show that this quantity is not extensive. This non-extensive entropy provided the original version of the Gibbs paradox.

**(21.3)** Show that the number of states in a gas with energies below \(E_{\text{max}}\) is
$$\int_0^{\sqrt{2m E_{\text{max}}/\hbar^2}} g(k) dk = \frac{V}{6\pi^2} \left(\frac{2m E_{\text{max}}}{\hbar^2}\right)^{3/2}. \tag{21.45}$$
Putting \(E_{\text{max}} = \frac{3}{2} k_B T\), show that the number of states is \(\Xi V n_Q\) where \(\Xi\) is a numerical constant of order unity.

**(21.4)** An atom in a solid has two energy levels: a ground state of degeneracy \(g_1\) and an excited state of degeneracy \(g_2\) at an energy \(\Delta\) above the ground state. Show that the partition function \(Z_{\text{atom}}\) is
$$Z_{\text{atom}} = g_1 + g_2 e^{-\beta\Delta}. \tag{21.46}$$
Show that the heat capacity of the atom is given by
$$C = \frac{g_1 g_2 \Delta^2 e^{-\beta\Delta}}{k_B T^2 (g_1 + g_2 e^{-\beta\Delta})^2}. \tag{21.47}$$
A monatomic gas of such atoms has a partition function given by
$$Z = Z_{\text{atom}} Z_N, \tag{21.48}$$
where \(Z_N\) is the partition function due to the translational motion of the gas atoms and is given by \(Z_N = (1/N!)[V/\lambda_{\text{th}}^3]^N\). Show that the heat capacity of such as gas is
$$C = N \left[ \frac{3}{2} k_B + \frac{g_1 g_2 \Delta^2 e^{-\beta\Delta}}{k_B T^2 (g_1 + g_2 e^{-\beta\Delta})^2} \right]. \tag{21.49}$$

[Image: A graph of heat capacity of hydrogen gas versus temperature, showing a peak around 50 K and a gradual rise to a plateau at higher temperatures.]
**Fig. 21.6** The heat capacity of hydrogen gas as a function of temperature.

**(21.5)** Explain the behaviour of the experimental heat capacity (measured at constant pressure) of hydrogen (\(H_2\)) gas shown in Fig. 21.6.

**(21.6)** Show that the single–particle partition function \(Z_1\) of a gas of hydrogen atoms is given approximately by
$$Z_1 = \frac{V e^{\beta R}}{\lambda_{\text{th}}^3}, \tag{21.50}$$
where \(R = 13.6\) eV and the contribution due to excited states has been neglected.

---

Here is the **complete and corrected Markdown conversion for Chapter 22 (Pages 244–262)**.

---

## Chapter 22: The chemical potential

### Page 244

#### Chapter Outline

**22.1 A definition of the chemical potential** 244
**22.2 The meaning of the chemical potential** 245
**22.3 Grand partition function** 247
**22.4 Grand potential** 248
**22.5 Chemical potential as Gibbs function per particle** 250
**22.6 Many types of particle** 250
**22.7 Particle number conservation laws** 251
**22.8 Chemical potential and chemical reactions** 252
**22.9 Osmosis** 257
**Chapter summary** 261
**Further reading** 261
**Exercises** 262

We now want to consider systems that can exchange particles with their surroundings and we will show in this chapter that this feature leads to a new concept, known as the **chemical potential**. Differences in the chemical potential drive the flow of particles from one place to another in much the same way as differences in temperature drive the flow of heat. The chemical potential turns up in chemical reactions (hence the name) because in a reaction such as
$$2\text{H}_2 + \text{O}_2 \to 2\text{H}_2\text{O}, \tag{22.1}$$
you are changing the number of particles in your system (three molecules on the left, two on the right). However, as we shall see, the chemical potential applies to more than just chemical systems. It is connected with conservation laws, so that particles such as electrons (which are conserved) and photons (which are not) have different chemical potentials and this has consequences for their behaviour.

---

#### 22.1 A definition of the chemical potential

If you add a particle to a system, then the internal energy will change by an amount which we call the chemical potential \(\mu\). Thus the first and second laws of thermodynamics expressed in eqn 14.18 must, in the case of changing numbers of particles, be modified to contain an extra term, so that
$$dU = T dS - p dV + \mu dN, \tag{22.2}$$
where \(N\) is the number of particles in the system.\(^1\) This means that we can write an expression for \(\mu\) as a partial differential of \(U\) as follows:
$$\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}. \tag{22.3}$$
However, keeping \(S\) and \(V\) constant is a difficult constraint to apply, so it is convenient to consider other thermodynamic potentials. Equation 22.2, together with the definitions \(F = U - TS\) and \(G = U + pV - TS\), implies that
$$dF = -p dV - S dT + \mu dN, \tag{22.4}$$
$$dG = V dp - S dT + \mu dN, \tag{22.5}$$

> \(^1\)If we are dealing with discrete particles, then \(N\) is an integer and can only change by integer amounts; hence using calculus expressions like \(dN\) is a bit sloppy, but this is an indiscretion for which we may be excused if \(N\) is large. However, there exist systems such as quantum dots, which are semiconductor nanocrystals whose size is a few nanometres. Quantum dots are so small that \(\mu\) jumps discontinuously when you add one electron to the quantum dot.

---

### Page 245

and hence we can make the more useful definitions:
$$\mu = \left(\frac{\partial F}{\partial N}\right)_{V,T} \quad \text{or} \tag{22.6}$$
$$\mu = \left(\frac{\partial G}{\partial N}\right)_{p,T}. \tag{22.7}$$
The constraints of constant \(p\) and \(T\) are experimentally convenient for chemical systems and so eqn 22.7 will be particularly useful.

---

#### 22.2 The meaning of the chemical potential

What drives a system to form a particular equilibrium state? As we have seen in Chapter 14, it is the second law of thermodynamics which states that entropy always increases. The entropy of a system can be considered to be a function of \(U, V\), and \(N\), so that \(S = S(U, V, N)\). Therefore, we can immediately write down
$$dS = \left(\frac{\partial S}{\partial U}\right)_{N,V} dU + \left(\frac{\partial S}{\partial V}\right)_{N,U} dV + \left(\frac{\partial S}{\partial N}\right)_{U,V} dN. \tag{22.8}$$
Equation 22.2 implies that
$$dS = \frac{dU}{T} + \frac{p dV}{T} - \frac{\mu dN}{T}. \tag{22.9}$$
Comparison of eqn 22.8 and 22.9 implies that we can therefore make the following identifications:
$$\left(\frac{\partial S}{\partial U}\right)_{N,V} = \frac{1}{T}, \quad \left(\frac{\partial S}{\partial V}\right)_{N,U} = \frac{p}{T}, \quad \left(\frac{\partial S}{\partial N}\right)_{U,V} = -\frac{\mu}{T}. \tag{22.10}$$

Now consider two systems which are able to exchange heat or particles between them. If we write down an expression for \(dS\), then we can use the second law of thermodynamics in the form \(dS \geq 0\) to determine the equilibrium state. We repeat this analysis for two cases as follows:

- **The case of heat flow**
[Image: Two systems, 1 and 2, connected by a diathermal wall, able to exchange heat.]
**Fig. 22.1** Two systems which are able to exchange heat with each other.

Consider two systems which are able to exchange heat with each other while remaining thermally isolated from their surroundings (see Fig. 22.1). If system 1 loses internal energy \(dU\), system 2 must gain internal energy \(dU\). Thus the change of entropy is
$$dS = \left(\frac{\partial S_1}{\partial U_1}\right)_{N,V} dU_1 + \left(\frac{\partial S_2}{\partial U_2}\right)_{N,V} dU_2 = \left(\frac{\partial S_1}{\partial U_1}\right)_{N,V} (-dU) + \left(\frac{\partial S_2}{\partial U_2}\right)_{N,V} (dU) = \left(-\frac{1}{T_1} + \frac{1}{T_2}\right) dU \geq 0. \tag{22.11}$$
So \(dU > 0\), i.e., energy flows from 1 to 2, when \(T_1 > T_2\). As expected, equilibrium is found when \(T_1 = T_2\), i.e., when the temperatures of the two systems are equal.

---

### Page 246

- **The case of particle exchange**
[Image: Two systems, 1 and 2, connected by a wall permeable to particles, able to exchange particles.]
**Fig. 22.2** Two systems which are able to exchange particles with each other.

Now consider two systems which are able to exchange particles with each other, but remain isolated from their surroundings (see Fig. 22.2). If system 1 loses \(dN\) particles, system 2 must gain \(dN\) particles. Thus the change of entropy is
$$dS = \left(\frac{\partial S_1}{\partial N_1}\right)_{U,V} dN_1 + \left(\frac{\partial S_2}{\partial N_2}\right)_{U,V} dN_2 = \left(\frac{\partial S_1}{\partial N_1}\right)_{U,V} (-dN) + \left(\frac{\partial S_2}{\partial N_2}\right)_{U,V} (dN) = \left(\frac{\mu_1}{T_1} - \frac{\mu_2}{T_2}\right) dN \geq 0. \tag{22.12}$$
Assuming that \(T_1 = T_2\), we find that \(dN > 0\) (so that particles flow from 1 to 2) when \(\mu_1 > \mu_2\). Similarly, if \(\mu_2 < \mu_1\), then \(dN < 0\). Hence equilibrium is found when \(\mu_1 = \mu_2\), i.e., when the chemical potentials are the same for each system. This demonstrates that chemical potential plays a similar rôle in particle exchange as \(1/\text{temperature}\) does in heat exchange.

---

**Example 22.1**
Find the chemical potential for an ideal gas.

**Solution:**
We use eqn 22.6 (\(\mu = (\partial F/\partial N)_{V,T}\)), which relates \(\mu\) to \(F\), together with eqn 21.36, which gives an expression for \(F\), namely
$$F = N k_B T [\ln(n \lambda_{\text{th}}^3) - 1]. \tag{22.13}$$
Recalling also that \(n = N/V\), we find that
$$\mu = k_B T [\ln(n \lambda_{\text{th}}^3) - 1] + N k_B T \left(\frac{1}{N}\right), \tag{22.14}$$
and hence
$$\mu = k_B T \ln(n \lambda_{\text{th}}^3). \tag{22.15}$$
In this case, comparison with eqn 21.38 shows that \(\mu = G/N\). We will see in Section 22.5 that this property has more general applicability than just this specific case.

---

### Page 247

#### 22.3 Grand partition function

In this section we will introduce a version of the partition function we met in Chapter 20 but now generalized to include the effect of variable numbers of particle. To do this, we have to generalize the canonical ensemble we met in Chapter 4 to the case of both energy and particle exchange.

Let us write the entropy \(S\) as a function of internal energy \(U\) and particle number \(N\). Consider a small system with fixed volume \(V\) and with energy \(\epsilon\) and containing \(\mathcal{N}\) particles, connected to a reservoir with energy \(U - \epsilon\) and \(N - \mathcal{N}\) particles (see Fig. 22.3). We assume that \(U \gg \epsilon\) and \(N \gg \mathcal{N}\). Using a Taylor expansion, we can write the entropy of the reservoir as
$$S(U - \epsilon, N - \mathcal{N}) = S(U, N) - \epsilon \left(\frac{dS}{dU}\right)_{N,V} - \mathcal{N} \left(\frac{dS}{dN}\right)_{U,V}, \tag{22.16}$$
and using the differentials defined in eqn 22.10, we have that
$$S(U - \epsilon, N - \mathcal{N}) = S(U, N) - \frac{1}{T} (\epsilon - \mu\mathcal{N}). \tag{22.17}$$
The probability \(P(\epsilon, \mathcal{N})\) that the system chooses a particular macrostate is proportional to the number \(\Omega\) of microstates corresponding to that macrostate, and using \(S = k_B \ln \Omega\) we have that
$$P(\epsilon, \mathcal{N}) \propto e^{S(U-\epsilon, N-\mathcal{N})/k_B} \propto e^{\beta(\mu\mathcal{N} - \epsilon)}. \tag{22.18}$$
This is known as the **Gibbs distribution** and the situation is known as **the grand canonical ensemble**. In the case in which \(\mu = 0\), this reverts to the Boltzmann distribution (the canonical ensemble). Normalizing this distribution, we have that the probability of a state of the system with energy \(E_i\) and with \(N_i\) particles is given by
$$P_i = \frac{e^{\beta(\mu N_i - E_i)}}{\mathcal{Z}}, \tag{22.19}$$
where \(\mathcal{Z}\) is a normalization constant.

[Image: A small system with energy epsilon and N particles, connected to a large reservoir with energy U-epsilon and N-N particles.]
**Fig. 22.3** A small system with energy \(\epsilon\) and containing \(\mathcal{N}\) particles, connected to a reservoir with energy \(U - \epsilon\) and \(N - \mathcal{N}\) particles.

The normalization constant is known as the **grand partition function** \(\mathcal{Z}\), which we write as follows:
$$\mathcal{Z} = \sum_i e^{\beta(\mu N_i - E_i)}, \tag{22.20}$$
which is a sum over all states of the system. The grand partition function \(\mathcal{Z}\) can be used to derive many thermodynamic quantities, and we write down the most useful equations here without detailed proof.\(^2\)

> \(^2\)See Exercise 22.4.

$$\mathcal{N} = \sum_i N_i P_i = k_B T \left(\frac{\partial \ln \mathcal{Z}}{\partial \mu}\right)_\beta, \tag{22.21}$$
$$U = \sum_i E_i P_i = -\left(\frac{\partial \ln \mathcal{Z}}{\partial \beta}\right)_\mu + \mu N, \tag{22.22}$$
and
$$S = -k_B \sum_i P_i \ln P_i = \frac{U - \mu N + k_B T \ln \mathcal{Z}}{T}. \tag{22.23}$$

---

### Page 248

For convenience, let us summarize the various ensembles considered in statistical mechanics.

(1) **The microcanonical ensemble**: an ensemble of systems, all of which have the same fixed energy. The entropy \(S\) is related to the number of microstates by \(S = k_B \ln \Omega\), and hence by
$$\Omega = e^{\beta T S}. \tag{22.24}$$
(2) **The canonical ensemble**: an ensemble of systems, each of which can exchange its energy with a large reservoir of heat. As we shall see, this fixes (and defines) the temperature of the system. Since \(F = -k_B T \ln Z\), the partition function is given by
$$Z = e^{-\beta F}, \tag{22.25}$$
where \(F\) is the Helmholtz function.
(3) **The grand canonical ensemble**: an ensemble of systems, each of which can exchange both energy and particles with a large reservoir. This fixes the system’s temperature and chemical potential. By analogy with the canonical ensemble, we write the grand partition function as
$$\mathcal{Z} = e^{-\beta \Phi_G}, \tag{22.26}$$
where \(\Phi_G\) is the **grand potential**, which we discuss in the next section.

---

#### 22.4 Grand potential

Using eqn 22.26, we have defined a new state function, the grand potential \(\Phi_G\), by
$$\Phi_G = -k_B T \ln \mathcal{Z}. \tag{22.27}$$
Rearranging eqn 22.23, we have that
$$-k_B T \ln \mathcal{Z} = U - TS - \mu N, \tag{22.28}$$
and hence
$$\Phi_G = U - TS - \mu N = F - \mu N. \tag{22.29}$$
The grand potential has differential \(d\Phi_G\) given by
$$d\Phi_G = dF - \mu dN - N d\mu, \tag{22.30}$$
and, substituting in eqn 22.4, we therefore have
$$d\Phi_G = -S dT - p dV - N d\mu, \tag{22.31}$$
and this leads to the following equations for \(S, p\) and \(N\):
$$S = -\left(\frac{\partial \Phi_G}{\partial T}\right)_{V,\mu}, \tag{22.32}$$
$$p = -\left(\frac{\partial \Phi_G}{\partial V}\right)_{T,\mu}, \tag{22.33}$$
$$N = -\left(\frac{\partial \Phi_G}{\partial \mu}\right)_{T,V}. \tag{22.34}$$

---

### Page 249

**Example 22.2**
Find the grand potential for an ideal gas, and show that eqns 22.33 and 22.34 lead to the correct expressions for \(p\) and \(N\).

**Solution:**
Using eqns 21.36 and 22.15 we have that
$$\Phi_G = N k_B T [\ln(n \lambda_{\text{th}}^3) - 1] - N k_B T \ln(n \lambda_{\text{th}}^3) = -N k_B T, \tag{22.35}$$
and using the ideal gas equation (\(pV = N k_B T\)) this becomes
$$\Phi_G = -pV. \tag{22.36}$$
We can check that eqn 22.34 leads to the correct value of \(p\) by evaluating
$$\left(\frac{\partial \Phi_G}{\partial \mu}\right)_{T,V} = \left(\frac{\partial \Phi_G}{\partial N}\right)_{T,V} \left(\frac{\partial N}{\partial \mu}\right)_{T,V}, \tag{22.37}$$
and since \(\left(\frac{\partial \Phi_G}{\partial N}\right)_{T,V} = -k_B T\) (from eqn 22.35) and \(\left(\frac{\partial \mu}{\partial N}\right)_{T,V} = k_B T/N\) we have that
$$\left(\frac{\partial \Phi_G}{\partial \mu}\right)_{T,V} = -k_B T \times \frac{N}{k_B T} = -N, \tag{22.38}$$
justifying eqn 22.34. Similarly,\(^3\)
$$\left(\frac{\partial \Phi_G}{\partial V}\right)_{T,\mu} = -\left(\frac{\partial \Phi_G}{\partial \mu}\right)_{T,V} \left(\frac{\partial \mu}{\partial V}\right)_{T,\Phi_G} = N \left(\frac{\partial \mu}{\partial V}\right)_{T,\Phi_G} \tag{22.39}$$
and since the constraint of constant \(T\) and constant \(\Phi_G = -N k_B T\) means constant \(T\) and \(N\), and using \(N = nV\), we can use eqn 22.15 to obtain
$$\left(\frac{\partial \mu}{\partial V}\right)_{T,N} = k_B T \left(\frac{\partial \ln(N \lambda_{\text{th}}^3/V)}{\partial V}\right)_{T,N} = -\frac{k_B T}{V}, \tag{22.40}$$
and eqn 22.39 becomes
$$\left(\frac{\partial \Phi_G}{\partial V}\right)_{T,\mu} = -\frac{N k_B T}{V} = -p, \tag{22.41}$$
thus justifying eqn 22.33.

> \(^3\)Using the reciprocity theorem, with \(T\) held constant for all terms.

---

### Page 250

#### 22.5 Chemical potential as Gibbs function per particle

If we scale a system by a factor \(\lambda\), then we expect all the extensive\(^4\) variables will scale with \(\lambda\), thus
$$U \to \lambda U, \quad S \to \lambda S, \quad V \to \lambda V, \quad N \to \lambda N, \tag{22.42}$$
and writing the entropy \(S\) as a function of \(U, V\), and \(N\), we have
$$\lambda S(U, V, N) = S(\lambda U, \lambda V, \lambda N), \tag{22.43}$$
so that differentiating with respect to \(\lambda\) we have
$$S = \frac{\partial S}{\partial(\lambda U)} \frac{\partial(\lambda U)}{\partial \lambda} + \frac{\partial S}{\partial(\lambda V)} \frac{\partial(\lambda V)}{\partial \lambda} + \frac{\partial S}{\partial(\lambda N)} \frac{\partial(\lambda N)}{\partial \lambda}, \tag{22.44}$$
so that setting \(\lambda = 1\) and using eqn 22.10, we have that
$$S = \frac{U}{T} + \frac{pV}{T} - \frac{\mu N}{T}, \tag{22.45}$$
and hence
$$U - TS + pV = \mu N. \tag{22.46}$$
We recognize the left-hand side of this equation as the Gibbs function, and so we have
$$G = \mu N. \tag{22.47}$$
This gives a new interpretation for the chemical potential: by rearranging the above equation, one has that
$$\mu = \frac{G}{N}, \tag{22.48}$$
so that the chemical potential \(\mu\) can be thought of as the Gibbs function per particle.

This analysis also implies that the grand potential \(\Phi_G = F - \mu N\) can be rewritten (using eqn 22.46 and \(F = U - TS\)) as
$$\Phi_G = -pV. \tag{22.49}$$
This equation has been demonstrated to be correct for the specific example of the ideal gas (see eqn 22.36), but we have now shown that it is always correct if entropy is an extensive property.

> \(^4\)The distinction between intensive and extensive variables is discussed in Section 11.1.2.

---

#### 22.6 Many types of particle

If there is more than one type of particle, then one can generalize the treatment in Section 22.5, and write
$$dU = T dS - p dV + \sum_i \mu_i dN_i, \tag{22.50}$$
where \(N_i\) is the number of particles of species \(i\) and \(\mu_i\) is the chemical potential of species \(i\). Correspondingly, we have the equations
$$dF = -p dV - S dT + \sum_i \mu_i dN_i, \tag{22.51}$$
$$dG = V dp - S dT + \sum_i \mu_i dN_i, \tag{22.52}$$
and in particular, when the pressure and temperature are held constant we have that
$$dG = \sum_i \mu_i dN_i. \tag{22.53}$$
This generalization will be useful in our treatment of chemical reactions in Section 22.8.

---

### Page 251

#### 22.7 Particle number conservation laws

Imagine that one has a set of particles in a box in which particle number is not conserved. This means that we are free to create or destroy particles at will. There might be an energy cost associated with doing this, but provided we have energy to “pay” for the particles, no conservation laws would be broken. In this case, the system will try to minimize its availability (see Section 16.5) and if the constraints are that the box has fixed volume and fixed temperature, then the appropriate availability is the Helmholtz function\(^5\) \(F\). The system will therefore choose a number of particles \(N\) by minimizing \(F\) with respect to \(N\), i.e.,
$$\left(\frac{\partial F}{\partial N}\right)_{V,T} = 0. \tag{22.54}$$
This means that, from eqn 22.6,
$$\mu = 0. \tag{22.55}$$
We arrive at the important result that, for a set of particles with no conservation law concerning particle number, the chemical potential \(\mu\) is zero. One example of such a particle is the photon.\(^6\)

> \(^5\)If the constraints were constant pressure and temperature, we would be dealing with \(G\) not \(F\); see Section 16.5.
> \(^6\)Strictly this is only for photons in a vacuum, which the following example will assume. Photons can have a non-zero chemical potential under some circumstances. For example, if electrons and holes combine in a light-emitting diode, it may be that the chemical potential of the electrons \(\mu_e\), from the conduction band, is not balanced by the chemical potential of the holes \(\mu_h\), from the valence band, and this leads to light with a non-zero chemical potential \(\mu_\gamma = \mu_e + \mu_h\).

To understand this further, let us consider a set of particles for which particle number is a conserved quantity. Consider a gas of electrons. Electrons do have a conservation law: electron number has to be conserved, so the only way of annihilating an electron is by reacting it with a positron\(^7\) via the reaction
$$e^- + e^+ \rightleftharpoons \gamma, \tag{22.56}$$
where \(\gamma\) denotes a photon.

Thus imagine that our box contains \(N_-\) electrons and \(N_+\) positrons. We are constrained by our conservation law to fix the number \(N = N_+ - N_-\), which also serves to ensure that charge is conserved. The system is at fixed \(T\) and \(V\), and hence we should minimize \(F\) with respect to any variable, so let us choose \(N_-\) as a variable to vary. Thus
$$\left(\frac{\partial F}{\partial N_-}\right)_{V,T,N} = 0. \tag{22.57}$$
In this case, \(F\) is the sum of a term due to the Helmholtz function for the electrons and one for the positrons. Thus
$$\left(\frac{\partial F}{\partial N_-}\right)_{V,T,N_+} + \left(\frac{\partial F}{\partial N_+}\right)_{V,T,N_-} \frac{dN_+}{dN_-} = 0. \tag{22.58}$$
Now we have that
$$\left(\frac{\partial F}{\partial N_-}\right)_{V,T,N_+} = \mu_-, \tag{22.59}$$
the chemical potential of the electrons, while
$$\left(\frac{\partial F}{\partial N_+}\right)_{V,T,N_-} = \mu_+, \tag{22.60}$$
the chemical potential of the positrons. Moreover, since
$$\frac{dN_-}{dN_+} = 1, \tag{22.61}$$
we have that
$$\mu_+ + \mu_- = 0. \tag{22.62}$$
We are ignoring the chemical potential of the photons, since this is zero because photons do not have a conservation law.\(^8\)

> \(^7\)A positron \(e^+\) is an antielectron.
> \(^8\)Again, this is true for most circumstances, the photons from a light-emitting diode being a rather notable counterexample.

---

### Page 252

#### 22.8 Chemical potential and chemical reactions

We next want to consider how the chemical potential can be used to determine the equilibrium position of a chemical reaction. Before proceeding, we will prove an important result concerning the way the chemical potential of an ideal gas depends on pressure.

**Example 22.3**
Derive an expression for the dependence of the chemical potential of an ideal gas on pressure at fixed temperature.

**Solution:**
Equation 22.15 and the ideal gas equation (\(p = n k_B T\)) imply that
$$\mu = k_B T \ln\left(\frac{\lambda_{\text{th}}^3}{k_B T}\right) + k_B T \ln p. \tag{22.63}$$
It is useful to compare the chemical potential at standard temperature (298 K) and pressure (\(p^\ominus = 1 \text{ bar} = 10^5 \text{ Pa}\)), which we denote by \(\mu^\ominus\), with the chemical potential measured at some other pressure \(p\). Here the symbol \(\ominus\) denotes the value of a function measured at standard temperature and pressure. The chemical potential \(\mu(p)\) at pressure \(p\) is then given by
$$\mu(p) = \mu^\ominus + k_B T \ln \frac{p}{p^\ominus}. \tag{22.64}$$
Chemists often define their chemical potentials as the Gibbs function per mole, rather than per particle. In those units, one would have
$$\mu(p) = \mu^\ominus + RT \ln \frac{p}{p^\ominus}. \tag{22.65}$$

Another way of solving this is to use the equation for the change in Gibbs function \(dG = V dp - S dT\), which when the temperature is constant is \(dG = V dp\). This can be integrated to give
$$G(p) = G^\ominus + \int_{p^\ominus}^p V dp$$
and hence
$$G(p) = G^\ominus + n_m RT \ln \frac{p}{p^\ominus}$$
for \(n_m\) moles of gas. Equation 22.65 then follows.

We are now ready to think about a simple chemical reaction. Consider the chemical reaction
$$\text{A} \rightleftharpoons \text{B}. \tag{22.66}$$
The symbol \(\rightleftharpoons\) indicates that in this reaction it is possible to have both the forwards reaction \(\text{A} \to \text{B}\) and the backwards reaction \(\text{B} \to \text{A}\). If we have a container filled with a mixture of A and B, and we leave it to react for a while, then depending on whether \(\text{A} \to \text{B}\) is more or less important than \(\text{B} \to \text{A}\), we can determine the equilibrium concentrations of A and B. For gaseous reactions, the concentration of A (or B) is related to that species’ partial pressure\(^9\) \(p_A\) (or \(p_B\)). We define the **equilibrium constant** \(K\) as the ratio of these two partial pressures at equilibrium, i.e.,
$$K = \frac{p_B}{p_A}. \tag{22.67}$$
When \(K \ll 1\), the backwards reaction dominates and our container will be mainly filled with A. When \(K \gg 1\), the forwards reaction dominates and our container will be mainly filled with B.

The change in Gibbs function as this reaction proceeds is
$$dG = \mu_A dN_A + \mu_B dN_B. \tag{22.68}$$
However, since an increase in B is always accompanied by a corresponding decrease in A, we have that
$$dN_B = -dN_A, \tag{22.69}$$
and hence
$$dG = (\mu_B - \mu_A) dN_B. \tag{22.70}$$
Let us now denote the total molar Gibbs function\(^{10}\) difference in a reaction by the symbol \(\Delta_r G\). For a gaseous reaction, eqn 22.65 implies that
$$\Delta_r G = \Delta_r G^\ominus + RT \ln \frac{p_B}{p_A}, \tag{22.71}$$

> \(^9\)The partial pressure of a gas in a mixture is what the pressure of that gas would be if all other components suddenly vanished. Dalton’s law states that the total pressure of a mixture of gases is equal to the sum of the individual partial pressures of the gases in the mixture (see Section 6.3).
> \(^{10}\)Thus \(\Delta_r G = N_A(\mu_B - \mu_A)\). In many chemistry books it is conventional to define chemical potential as Gibbs function per mole, rather than Gibbs function per particle. Under this definition, one would have \(\Delta_r G = \mu_B - \mu_A\).

---

### Page 253

where \(\Delta_r G^\ominus\) is the difference between the molar chemical potentials of the two species. When \(\Delta_r G < 0\), the forwards reaction \(\text{A} \to \text{B}\) occurs spontaneously. When \(\Delta_r G > 0\), the backwards reaction \(\text{B} \to \text{A}\) occurs spontaneously. Equilibrium occurs when \(\Delta_r G = 0\), and substituting this into eqn 22.71 and using eqn 22.67 shows that
$$\ln K = -\frac{\Delta_r G^\ominus}{RT}. \tag{22.72}$$
Hence there is a direct relationship between the equilibrium constant of a reaction and the difference in chemical potentials (measured under standard conditions) of the product and reactant.\(^{11}\)

It is useful to generalize these ideas to the case in which the chemical reaction is a bit more complicated than \(\text{A} \rightleftharpoons \text{B}\). A general chemical reaction, with \(p\) reactants and \(q\) products, can be written in the form
$$\sum_{j=1}^p (-\nu_j) \text{A}_j \to \sum_{j=p+1}^{p+q} (+\nu_j) \text{A}_j, \tag{22.73}$$
where the \(\nu_j\) coefficients are here defined to be negative for the reactants and where \(\text{A}_j\) represents the \(j\)th substance. This can be rearranged to give
$$0 \to \sum_{j=1}^{p+q} \nu_j \text{A}_j. \tag{22.74}$$

**Example 22.4**
Equation 22.53 can be applied to chemical reactions, such as
$$\text{N}_2 + 3\text{H}_2 \to 2\text{NH}_3. \tag{22.75}$$
This can be cast into the general form of eqn 22.74 by writing
$$\nu_1 = -1, \quad \nu_2 = -3, \quad \nu_3 = 2. \tag{22.76}$$

In a chemical system in equilibrium at constant temperature and pressure we have that the Gibbs function is minimized and so eqn 22.53 gives
$$\sum_{j=1}^{p+q} \mu_j dN_j = 0, \tag{22.77}$$
where \(N_j\) is the number of molecules of type \(\text{A}_j\). To keep the reaction balanced, the \(dN_j\) must be proportional to \(\nu_j\) and hence
$$\sum_{j=1}^{p+q} \nu_j \mu_j = 0. \tag{22.78}$$
This equation is very general.

> \(^{11}\)The reactant is defined to be the chemical on the left-hand side of the reaction; the product is defined to be the chemical on the right-hand side of the reaction.

---

### Page 254

**Example 22.5**
For the chemical reaction
$$\text{N}_2 + 3\text{H}_2 \to 2\text{NH}_3,$$
eqn 22.78 implies that
$$-\mu_{\text{N}_2} - 3\mu_{\text{H}_2} + 2\mu_{\text{NH}_3} = 0. \tag{22.79}$$

One can generalize the previous definition of the equilibrium constant for a gaseous reaction in eqn 22.67 (for a simple \(\text{A} \rightleftharpoons \text{B}\) reaction) to the following expression (for our general reaction in eqn 22.74):
$$K = \prod_{j=1}^{p+q} \left(\frac{p_j}{p^\ominus}\right)^{\nu_j}. \tag{22.80}$$

**Example 22.6**
For the chemical reaction
$$\text{N}_2 + 3\text{H}_2 \to 2\text{NH}_3,$$
the equilibrium constant is
$$K = \frac{(p_{\text{NH}_3}/p^\ominus)^2}{(p_{\text{N}_2}/p^\ominus)(p_{\text{H}_2}/p^\ominus)^3} = \frac{p_{\text{NH}_3}^2 p^{\ominus 2}}{p_{\text{N}_2} p_{\text{H}_2}^3}. \tag{22.81}$$

Equilibrium, given by eqn 22.78, implies that
$$\sum_{j=1}^{p+q} \nu_j \left(\mu_j^\ominus + RT \ln \frac{p_j}{p^\ominus}\right) = 0 \tag{22.82}$$
and writing
$$\Delta_r G^\ominus = \sum_{j=1}^{p+q} \nu_j \mu_j^\ominus, \tag{22.83}$$
we have that
$$\Delta_r G^\ominus + RT \sum_{j=1}^{p+q} \nu_j \ln \frac{p_j}{p^\ominus} = 0 \tag{22.84}$$
and hence
$$\Delta_r G^\ominus + RT \ln K = 0, \tag{22.85}$$

---

### Page 255

or equivalently
$$\ln K = -\frac{\Delta_r G^\ominus}{RT}, \tag{22.86}$$
in agreement with eqn 22.72 (which was proved only for the simple reaction \(\text{A} \rightleftharpoons \text{B}\)).

Since \(\ln K = -\Delta_r G^\ominus/RT\), we have that
$$\frac{d\ln K}{dT} = -\frac{1}{R} \frac{d(\Delta_r G^\ominus/T)}{dT}, \tag{22.87}$$
and using the Gibbs–Helmholtz relation (eqn 16.26) this becomes
$$\frac{d\ln K}{dT} = \frac{\Delta_r H^\ominus}{RT^2}. \tag{22.88}$$
Note that if the reaction is exothermic under standard conditions, then \(\Delta_r H^\ominus < 0\) and hence \(K\) decreases as temperature increases. Equilibrium therefore shifts away from the products of the reaction.
If on the other hand the reaction is endothermic under standard conditions, then \(\Delta_r H^\ominus > 0\) and hence \(K\) increases as temperature increases. Equilibrium therefore shifts towards the products of the reaction.

This observation agrees with **Le Chatelier’s principle**, which states that “a system at equilibrium, when subjected to a disturbance, responds in such a way as to minimize that disturbance”. In this case an exothermic reaction produces heat and this can raise the temperature, which then slows the forwards reaction towards the products. In the case of an endothermic reaction, heat is absorbed by the reactants and this can lower the temperature which would speed up the forwards reaction towards the products.

Equation 22.88 can be written in the following form:
$$\frac{d\ln K}{d(1/T)} = -\frac{\Delta_r H^\ominus}{R}, \tag{22.89}$$
which is known as the **van ’t Hoff equation**.\(^{12}\) This implies that a graph of \(\ln K\) against \(1/T\) should yield a straight line whose gradient is \(-\Delta_r H^\ominus/R\). This fact is used in the following example.

> \(^{12}\)Jacobus Henricus van ’t Hoff (1852–1911).

---

### Page 256

**Example 22.7**
Consider the dissociation reaction of molecular hydrogen into atomic hydrogen, i.e., the reaction
$$\text{H}_2 \to \text{H}\cdot + \text{H}\cdot \tag{22.90}$$
The equilibrium constant for this reaction is plotted in Fig. 22.4. The plot of \(K\) against \(T\) emphasizes that the equilibrium for this reaction is well and truly on the left, meaning that the main constituent is \(\text{H}_2\); molecular hydrogen is only very slightly dissociated even at 2000 K. Plotting the same data as \(\ln K\) against \(1/T\) yields a straight-line graph whose gradient yields \(-\Delta H^\ominus/R\) for this reaction. For these data we find that \(\Delta H^\ominus\) is about 440 kJ mol\(^{-1}\). This is positive and hence the reaction is endothermic, which makes sense because you need to heat \(\text{H}_2\) to break the molecular bond. This corresponds to a bond enthalpy per hydrogen molecule of \((440 \text{ kJ mol}^{-1}/N_A e) \approx 4.5 \text{ eV}\).

[Image: Two graphs of data for the reaction H2 -> H + H. The left graph shows K versus T, showing K is very small even at high T. The right graph shows ln K versus 1/T, which is a straight line with a negative slope.]
**Fig. 22.4** The equilibrium constant for the reaction \(\text{H}_2 \to \text{H}\cdot + \text{H}\cdot\), as a function of temperature. The same data are plotted in two different ways.

---

### Page 257

#### 22.9 Osmosis

We have seen in Section 22.2 that differences in chemical potential can drive a flow of particles from one reservoir to another. This is driven by entropy, as the joint system finds its most likely macrostate (maximizing the entropy). This flow of particles can give rise to a force (sometimes described as an **entropic force** because it is determined by entropy, rather than energy, considerations). A good example of this is the phenomenon of **osmosis**.

[Image: Two diagrams (a) and (b). (a) shows a bath of pure solvent A surrounding a semipermeable membrane containing a solution of B in A. (b) shows the osmotic flow has caused the level of the solution in the membrane to rise above the level of the pure solvent.]
**Fig. 22.5** (a) A bath of solvent A surrounds a solution of B dissolved in A. A semipermeable membrane allows solvent to flow through it but not the solute B. (b) Osmotic flow of solvent into the solution and in equilibrium the level of the solution is higher than that of the pure solvent.

The liquid forming the main component is known as the **solvent**, while the material dissolved in it is known as the **solute**.

Consider the situation shown in Fig. 22.5(a), in which a solution of some solute is contained inside a **semipermeable membrane** which allows the smaller solvent molecules to flow through it, but not the larger solvent molecules. This is placed in a large bath of pure solvent. For example, the solvent could be water and the solute could be sugar. What is observed is that pure water is drawn through the semipermeable membrane and into the sugar solution (this is called **osmotic flow**), causing the level to rise up until equilibrium is obtained as shown in Fig. 22.5(b). The height \(h\) reached by the solution is proportional to the **osmotic pressure**, \(\Pi = \rho_{\text{solution}} g h\), the additional pressure needed to stop the osmotic flow and bring about equilibrium, and this pressure is provided by the column of solution (density \(\rho_{\text{solution}}\)).

It is osmosis that is responsible for giving cells their internal pressure and that provides the structural stability of many plants; water is absorbed into a plant’s cells and provides turgor pressure. Water in the ground seems to be “sucked up” from the roots up to the top of the plant, but no suction is involved; the water flows upwards because it is driven by osmotic pressure. The water draws small nutrients from the soil with it as it flows up into the plant, and some water evaporates from the leaves (transpiration, a process that occurs through tiny pores in the leaves, called stomata), and provides the plant with cooling. Failure to water a plant results in wilting because the turgor pressure falls; wilting can also be produced by watering with salty water, which would cause osmotic flow of water out of the plant.

Freshwater and saltwater fish are adapted for their respective environments and can be harmed by placing them in water with the wrong salinity, precisely because this upsets the osmotic balance of their cells. Amoebae swimming in fresh water have to contend with fluid continually passing through their cell’s wall, and need a pump (the contractile vacuole) to discharge water periodically and prevent bursting.

Even our own blood cells are adapted for a particular osmotic pressure. Therefore, in blood transfusions and intravenous feeding it is important that the liquid injected is **isotonic** with blood; if instead it is too concentrated, and therefore has a higher osmotic pressure than blood, it is said to be **hypertonic** and will draw water out of the blood cells, causing them to shrivel; if it is too diluted, and therefore has a lower osmotic pressure than blood, it is said to be **hypotonic** and water will flow into the blood cells, causing them to burst.

---

### Page 258

[Image: Three diagrams (a), (b), and (c). (a) shows osmotic flow into a solution from pure solvent, with pistons applying equal pressure p to both sides. (b) shows equilibrium, with the solution subjected to an additional pressure Pi. (c) shows reverse osmosis, where a pressure greater than Pi is applied to the solution, forcing solvent out.]
**Fig. 22.6** (a) Osmotic flow into a solution from pure solvent, through a semipermeable membrane. Both sides are subjected to an identical pressure \(p\), shown schematically by the pistons. (b) In equilibrium, the chemical potential of the solvent and solution are equal. This occurs when the solution is subjected to an additional pressure equal to \(\Pi\), the osmotic pressure, over and above the pressure \(p\). (c) If a pressure difference is provided that is larger than this, flow of solvent molecules from the solution to the solvent occurs (reverse osmosis).

What causes the osmotic pressure? The answer is that it is nothing more than the tendency to maximize entropy, the drive of a system to approach equilibrium because it is the most likely state of the system. Temperature gradients are equalized by the flow of heat and concentration gradients are equalized by the flow of particles. The difference in concentration between the solvent on one side of the semipermeable membrane and the other therefore drives an osmotic flow (see Fig. 22.6(a)), and its effects can only be countered by providing a pressure-driven flow in the opposite direction (and this is what happens in equilibrium, see Fig. 22.6(b)). In fact, if you apply a greater pressure to the solution than the osmotic pressure you can cause the pressure-driven flow to be larger than the osmotic flow, leading to the phenomenon of **reverse osmosis** (see Fig. 22.6(c)). This is used in some water filtration and desalination processes, whereby for example pure water can be caused to flow out of a quantity of sea water contained inside a suitable membrane by applying mechanical pressure.

The osmotic pressure is an example of an entropic force, but there are many others. In Section 17.1 we found that if you hang a weight by a piece of rubber and heat the rubber, it will contract, thus raising the weight. This is another entropic force because the contraction of the rubber that raises the weight is due to maximizing entropy (there are many more disordered configurations of the rubber molecules in which their mean random-walk length is shorter than there are in which the rubber molecules are fully extended in a long line, see Fig. 17.2).

---

### Page 259

**Example 22.8**
Find the chemical potential of a solvent A with a solute B dissolved in it. The mole fraction of the solvent is \(x_A\).

**Solution:**
Recall from eqn 22.65 that the chemical potential\(^{13}\) of a gas (let us call it a gas of molecules of A) with pressure \(p_A^*\) is given by
$$\mu_A^{*(g)} = \mu_A^\ominus + RT \ln \frac{p_A^*}{p^\ominus}, \tag{22.91}$$
where the superscript \((g)\) indicates gas and the superscript \(*\) indicates that we are dealing with a pure substance. If this is in equilibrium with the liquid form of A, then we also have
$$\mu_A^{*(\ell)} = \mu_A^\ominus + RT \ln \frac{p_A^*}{p^\ominus}, \tag{22.92}$$
where the superscript \((\ell)\) indicates liquid. Now imagine that we mix some B molecules into the liquid. The mole fraction of A, \(x_A\), is now less than one. The chemical potential of A in the liquid is now still equal to the chemical potential of A in the gas, but the gas has a different vapour pressure \(p_A\) (no asterisk because we are no longer dealing with pure substances). Thus
$$\mu_A^{(\ell)} = \mu_A^{(g)} = \mu_A^\ominus + RT \ln \frac{p_A}{p^\ominus}. \tag{22.93}$$

Equations 22.92 and 22.93 give that
$$\mu_A^{(\ell)} = \mu_A^{*(\ell)} + RT \ln \frac{p_A}{p_A^*}. \tag{22.94}$$

The vapour pressure of A in the mixed system can be estimated using **Raoult’s law**\(^{14}\), which states that \(p_A = x_A p_A^*\) (i.e., that the vapour pressure of A is proportional to its mole fraction). Hence eqn 22.94 becomes
$$\mu_A^{(g)} = \mu_A^{(\ell)} = \mu_A^{*(\ell)} + RT \ln x_A. \tag{22.95}$$
Since \(x_A < 1\), we find that \(\mu_A^{(\ell)} < \mu_A^{*(\ell)}\) and so the chemical potential of A is depressed compared to the pure case.\(^{15}\)

> \(^{13}\)We are here again using the chemistry definition of chemical potential as Gibbs function per mole.
> \(^{14}\)François-Marie Raoult (1830–1901).
> \(^{15}\)This result will be used to explain colligative properties in Section 28.6.

We can use the result in the previous example to derive an equation which is useful in describing osmosis for dilute solutions. Let us consider the equilibrium between (i) the pure solvent, A, held at pressure \(p\) (provided by the atmosphere) and (ii) the solution, which contains a small number of B molecules dissolved in solvent A, held at pressure \(p + \Pi\), where \(\Pi\) is the osmotic pressure (see Fig. 22.6(b)). As before, (i) and (ii) are separated by a semipermeable membrane which only allows passage of the solvent A molecules. Equilibrium between the A molecules implies
$$\mu_A^*(p) = \mu_A(p + \Pi), \tag{22.96}$$
or equivalently
$$\mu_A^*(p) = \mu_A^*(p + \Pi) + RT \ln x_A, \tag{22.97}$$
where the second term in this equation uses the result from eqn 22.95. The pressure dependence of \(\mu_A\) can be accounted for by remembering that \((\partial G/\partial p)_T = V\) and hence \(\mu_A^*(p+\Pi) = \mu_A^*(p) + \int_p^{p+\Pi} V_A dp\) where \(V_A\) is the partial molar volume of solvent, which we can assume is constant over this pressure range. Hence
$$\mu_A^*(p) = \mu_A^*(p) + \Pi V_A + RT \ln x_A, \tag{22.98}$$
and therefore
$$\Pi V_A = -RT \ln x_A. \tag{22.99}$$
Remembering that \(x_A + x_B = 1\) and \(x_B \ll 1\), we can write \(-\ln x_A \approx x_B\) and hence
$$\Pi V_A = RT x_B. \tag{22.100}$$
Further writing \(x_B = n_B/(n_A + n_B)\) and the total volume \(V \approx n_A V_A\) and \(n_B \ll n_A\), we have
$$\Pi V = n_B RT. \tag{22.101}$$
This equation applies only to dilute, ideal solutions.\(^{16}\) The ratio \(n_B/V\) is the concentration of the solution, expressed as the number of moles of solute per unit volume.\(^{17}\)

> \(^{16}\)In more advanced treatments, osmotic pressure can be modelled using a virial-type expression \(\Pi V = n_B RT(1 + \alpha(n_B/V) + \cdots)\), where \(\alpha\) is a constant. Measuring \(\Pi\) as a function of the mass concentration of the solute in the solution (proportional to \(n_B/V\)) can allow this constant to be determined, as well as the molar mass of the solvent and this is useful in the mass determination of macromolecules (the technique is called osmometry).
> \(^{17}\)Chemists write the concentration \(n_B/V\) using the symbol [B]. Using this notation, eqn 22.101 becomes \(\Pi = [B]RT\).

---

### Page 260

We close by trying to examine what causes the osmotic flow at a microscopic level. As shown in Fig. 22.7, although the small solvent molecules can pass through the membrane, the large solute molecules cannot. The number density of solvent molecules on the right-hand side is lower than on the left-hand side, and this concentration gradient has an effect close to the pores in the membrane (since solute molecules are excluded from this region, their centres never being able to cross to the left of the vertical dashed line). All the molecules bounce off each other and therefore momentum is transferred between molecules of all types. However, close to the membrane, the solute molecules receive a kick from the membrane only in the rightwards direction. This momentum is eventually distributed throughout all the molecules on the right-hand side of the diagram, since the small solvent molecules colliding with these solute molecules receive a net transfer of rightwards momentum. This drags solvent through the pores and causes the osmotic flow. Equilibrium is only obtained when a pressure equal to the osmotic pressure is provided on the right-hand side and causes an equal and opposite flow of solvent molecules in a leftwards direction.

---

### Page 261

It is therefore no surprise that we find an ideal-gas type expression for the osmotic pressure in eqn 22.101 since this would be the pressure exerted by the solute molecules on the semipermeable membrane, treating those molecules as an ideal gas; by Newton’s third law, that pressure is also exerted by the semipermeable membrane on the solute molecules and through collisions with the solvent leads to the rightwards osmotic flow. Only by applying an equal and opposite pressure on the right-hand side (the osmotic pressure) can equilibrium be obtained.

[Image: A microscopic view of a semipermeable membrane. Large solute molecules are confined to the right side. Small solvent molecules are on both sides and can pass through the pores. The solute molecules collide with the membrane and transfer momentum to the solvent, causing a net flow of solvent to the right.]
**Fig. 22.7** A microscopic view of osmosis. The large solute molecules are kept on one side of the semipermeable membrane and their centres are confined in the region right of the vertical dashed line (drawn a radius away from the right-hand side of the semipermeable membrane).

---

### Chapter summary

- An extra term is appropriately introduced into the combined first and second laws to give \(dU = T dS - p dV + \mu dN\), and this allows for cases in which the number of particles can vary.
- \(\mu\) is the chemical potential, which can be expressed as \(\mu = \left(\frac{\partial G}{\partial N}\right)_{p,T}\). It is also the Gibbs function per particle.
- For a system that can exchange particles with its surroundings, the chemical potential plays a similar rôle in particle exchange as temperature does in heat exchange.
- The grand partition function \(\mathcal{Z}\) is given by \(\mathcal{Z} = \sum_i e^{\beta(\mu N_i - E_i)}\).
- The grand potential is \(\Phi_G = -k_B T \ln \mathcal{Z} = U - TS - \mu N = -pV\).
- \(\mu = 0\) for particles with no conservation law.
- For a chemical reaction \(dG = \sum \mu_j dN_j = 0\) and hence \(\sum \nu_j \mu_j = 0\).
- The equilibrium constant \(K\) can be written as \(\ln K = -\Delta_r G^\ominus/RT\).
- The temperature dependence of \(K\) follows \(d\ln K/dT = \Delta_r H^\ominus/RT^2\).
- Osmosis is an example of an entropic force. An osmotic flow occurs from a solvent into a solution through a semipermeable membrane. The osmotic pressure \(\Pi\) obeys \(\Pi V = n_B RT\) where \(n_B/V\) is the concentration of the solute.

---

### Further reading

- Baierlein (2001) and Cook and Dickerson (1995) are both excellent articles concerning the nature of the chemical potential.
- Atkins and de Paulo (2006) contains a treatment of the chemical potential from the perspective of chemistry.

---

### Page 262

### Exercises

**(22.1)** Maximize the entropy \(S = -k_B \sum_i P_i \ln P_i\), where \(P_i\) is the probability of the \(i\)th level being occupied, subject to the constraints that \(\sum P_i = 1\), \(\sum P_i E_i = U\), and \(\sum P_i N_i = \mathcal{N}\) to rederive the grand canonical ensemble.

**(22.2)** The fugacity \(z\) is defined as \(z = e^{\beta\mu}\). Using eqn 22.15, show that
$$z = n \lambda_{\text{th}}^3 \tag{22.102}$$
for an ideal gas, and comment on the limits \(z \ll 1\) and \(z \gg 1\).

**(22.3)** Estimate the bond enthalpy of Br$_2$ using the data plotted in Fig. 22.8.

[Image: A plot of ln K versus 1/T for the reaction Br2 -> Br + Br. The data points fall on a straight line with a negative slope.]
**Fig. 22.8** The equilibrium constant for the reaction \(\text{Br}_2 \to \text{Br}\cdot + \text{Br}\cdot\), as a function of temperature.

**(22.4)** Derive eqns 22.21, 22.22, and 22.23.

**(22.5)** If the partition function $Z_N$ of a gas of \(N\) indistinguishable particles is given by \(Z_N = Z_1^N/N!\), where \(Z_1\) is the single–particle partition function, show that the chemical potential is given by
$$\mu = -k_B T \ln \frac{Z_1}{N}. \tag{22.103}$$

**(22.6)** (a) Consider the ionization of atomic hydrogen, governed by the equation
$$\text{H} \rightleftharpoons \text{p}^+ + \text{e}^-, \tag{22.104}$$
where \(\text{p}^+\) is a proton (equivalently a positively ionized hydrogen) and \(\text{e}^-\) is an electron. Explain why
$$\mu_{\text{H}} = \mu_{\text{p}} + \mu_{\text{e}}. \tag{22.105}$$
Using the partition function for hydrogen atoms from eqn 21.50, and using eqn 22.103, show that
$$-k_B T \ln \frac{Z_1^p}{N_p} - k_B T \ln \frac{Z_1^e}{N_e} = -k_B T \ln \frac{Z_1^H}{N_H} e^{\beta R}, \tag{22.106}$$
where $Z_1^x$ and \(N_x\) are the single–particle partition function and number of particles for species \(x\) respectively, and where \(R = 13.6\) eV. Hence show that
$$\frac{n_e n_p}{n_H} = \frac{(2\pi m_e k_B T)^{3/2}}{h^3} e^{-\beta R}, \tag{22.107}$$
where \(n_x = N_x/V\) is the number density of species \(x\), stating any approximations you make. Equation 22.107 is known as the **Saha equation**.
(b) Explain why charge neutrality implies that \(n_e = n_p\) and conservation of nucleons implies \(n_H + n_p = n\), where \(n\) is the total number density of hydrogen (neutral and ionized). Writing \(y = n_p/n\) as the degree of ionization, show that
$$\frac{y^2}{1-y} = \frac{e^{-\beta R}}{n \lambda_{\text{th}}^3}, \tag{22.108}$$
where \(\lambda_{\text{th}}\) is the thermal wavelength for the electrons. Find the degree of ionization of a cloud of atomic hydrogen at 1000 K and density \(10^{20} \text{ m}^{-3}\).
(c) Equation 22.108 shows that the degree of ionization goes up when the density \(n\) goes down. Why is that?

**(22.7)** A solution of NaCl dissolved in water, which is 0.9% by weight NaCl, is isotonic with blood. Show that the osmotic pressure of blood is nearly eight times atmospheric pressure.

---
Here is the **complete and corrected Markdown conversion for Chapter 23 (Pages 263–278)**.

---

## Chapter 23: Photons

### Page 263

#### Chapter Outline

**23.1 The classical thermodynamics of electromagnetic radiation** 264
**23.2 Spectral energy density** 265
**23.3 Kirchhoff’s law** 266
**23.4 Radiation pressure** 268
**23.5 The statistical mechanics of the photon gas** 269
**23.6 Black-body distribution** 270
**23.7 Cosmic microwave background radiation** 273
**23.8 The Einstein A and B coefficients** 274
**Chapter summary** 277
**Further reading** 277
**Exercises** 278

In this chapter, we will consider the thermodynamics of electromagnetic radiation. It was Maxwell who realized that light was an electromagnetic wave and that the speed of light, \(c\), could be expressed in terms of fundamental constants taken from the theories of electricity and magnetism. In modern notation, this relation is
$$c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}, \tag{23.1}$$
where \(\epsilon_0\) and \(\mu_0\) are the permittivity and permeability of free space respectively. Later, Planck realized that light behaved not only like a wave but also like a particle. In the language of quantum mechanics, electromagnetic waves can be quantized as a set of particles, which are known as **photons**. Each photon has an energy \(\hbar\omega\) where \(\omega = 2\pi\nu\) is the angular frequency.\(^1\) Each photon has a momentum \(\hbar\mathbf{k}\) where \(\mathbf{k}\) is the wave vector.\(^2\) The ratio of the energy to the momentum of a photon is
$$\frac{\omega}{k} = \frac{2\pi\nu \times \lambda}{2\pi} = \nu\lambda = c. \tag{23.2}$$

Electromagnetic radiation is emitted from any substance at non-zero temperature. This is known as **thermal radiation**. For objects at room temperature, you may not have noticed this effect because the frequency of the electromagnetic radiation is low and most of the emission is in the infrared region of the electromagnetic spectrum. Our eyes are only sensitive to electromagnetic radiation in the visible region. However, you may have noticed that a piece of metal in a furnace glows “red hot” so that, for such objects at higher temperature, your eyes are able to pick up some of the thermal radiation.\(^3\)

> \(^1\nu\) is the frequency. The energy can also be expressed as \(h\nu\). Recall also that \(\hbar = h/(2\pi)\).
> \(^2\)The wave vector \(\mathbf{k} = 2\pi/\lambda\) where \(\lambda\) is the wavelength.
> \(^3\)Your eyes can pick up a lot of the thermal radiation if they are assisted by infrared goggles.

This chapter is all about the properties of this thermal radiation. We will begin in Sections 23.1–23.4 by restricting ourselves to simple thermodynamics arguments to derive as much as we can about thermal radiation without going into the gory details, in much the same way as was originally done in the nineteenth century. This approach doesn’t get us the whole way, but provides a lot of insight. Then in Sections 23.5 and 23.6, we will use the more advanced statistical mechanical techniques introduced in the previous chapters to do the job properly. The final sections concern the thermal radiation that exists in the Universe as a remnant of the hot big bang and the effect of thermal radiation on the behaviour of atoms and hence the operation of the laser.

---

### Page 264

#### 23.1 The classical thermodynamics of electromagnetic radiation

In this section, we will consider the thermodynamics of electromagnetic radiation from a classical standpoint, although we will allow ourselves the post-nineteenth century luxury of considering the electromagnetic radiation to consist of a gas of photons. First we will consider the effect of a collection of photons on the surroundings that contain it. Let us consider the surroundings to be a container of volume \(V\), which in this subject is termed a “cavity”, which is held at temperature \(T\). The photons inside the cavity are in thermal equilibrium with the cavity walls, and form electromagnetic standing waves.

[Image: A diagram of a cavity, a box with walls, containing photons. The walls are diathermal, meaning they can exchange heat with the surroundings.]
**Fig. 23.1** A cavity of photons whose walls are diathermal, meaning they are in thermal contact with their surroundings, so that the temperature within may be controlled.

The walls of the cavity, shown in Fig. 23.1, are made of diathermal material (i.e., they transmit heat between the gas of photons inside the cavity and the surroundings). If \(n\) photons per unit volume comprise the gas of photons in the cavity then the **energy density** \(u\) of the gas may be written as:
$$u = \frac{U}{V} = n\hbar\omega, \tag{23.3}$$
where \(\hbar\omega\) is the mean energy of a photon. From kinetic theory (eqn 6.15), the pressure \(p\) of a gas of particles is \(\frac{1}{3}nm\langle v^2\rangle\). For photons, we replace \(\langle v^2\rangle\) in this formula by \(c^2\), the square of the speed of light. Interpreting \(mc^2\) as the energy of a photon, we then have that \(p\) is one-third of the energy density. Thus
$$p = \frac{u}{3}, \tag{23.4}$$
which is different from the expression in eqn 6.25 (\(p = 2u/3\)) from the kinetic theory of gases, a point which we will return to in Section 25.2 (see eqn 25.21).\(^4\) Equation 23.4 gives an expression for the **radiation pressure** due to the electromagnetic radiation. Also from kinetic theory (eqn 7.6), the flux \(\Phi\) of photons on the walls of their container, that is to say the number of photons striking unit area of their container per second, is given by
$$\Phi = \frac{1}{4}nc, \tag{23.5}$$
where \(c\) is the speed of light. From this, and eqn 23.3, we can write the power incident per unit area of cavity wall, due to the photons, as
$$\mathcal{F} = \hbar\omega\Phi = \frac{1}{4}uc. \tag{23.6}$$
This relation will be important as we now derive the **Stefan–Boltzmann law**, which relates the temperature of a body to the energy flux radiating from it in the form of electromagnetic radiation. We can derive this using the first law of thermodynamics in the form \(dU = T dS - p dV\) to give
$$\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial S}{\partial V}\right)_T - p = T\left(\frac{\partial p}{\partial T}\right)_V - p, \tag{23.7}$$

> \(^4\)The factor of two difference arises from writing the kinetic energy as \(mc^2\) and not as \(\frac{1}{2}m\langle v^2\rangle\), and thus reflects the difference in form between the equation for the relativistic energy of a photon and that for the kinetic energy of a non-relativistic particle.

---

### Page 265

where the last equality follows from using a Maxwell relation. The left-hand side of eqn 23.7 is simply\(^5\) the energy density \(u\). Hence, using eqn 23.7, together with eqn 23.4, we obtain
$$u = \frac{1}{3}T\left(\frac{\partial u}{\partial T}\right)_V - \frac{u}{3}. \tag{23.8}$$
Rearranging gives:
$$4u = T\left(\frac{\partial u}{\partial T}\right)_V, \tag{23.9}$$
from which follows
$$4\frac{dT}{T} = \frac{du}{u}. \tag{23.10}$$
Equation 23.10 may be integrated to give:
$$u = AT^4, \tag{23.11}$$
where \(A\) is a constant of the integration with units \(\text{J K}^{-4}\text{ m}^{-3}\). We can now use eqn 23.6 to give us the power incident\(^6\) per unit area.\(^7\)
$$\mathcal{F} = \frac{1}{4}uc = \left(\frac{1}{4}Ac\right)T^4 = \sigma T^4, \tag{23.12}$$
where the term in brackets, \(\sigma = \frac{1}{4}Ac\), is the **Stefan–Boltzmann constant**. Equation 23.12 is known as the Stefan–Boltzmann law or sometimes as Stefan’s law. For the moment, we have no idea what value the constant \(\sigma\) takes and this is something that was originally determined from experiment. In Section 23.5, using the techniques of statistical mechanics, we will derive an expression for this constant.

> \(^5\)This should be obvious since it is the definition of energy density. However, if you want to convince yourself, notice that differentiating \(U = uV\) with respect to \(V\) yields \(\left(\frac{\partial U}{\partial V}\right)_T = u + V\left(\frac{\partial u}{\partial V}\right)_T = u\), because \(\left(\frac{\partial u}{\partial V}\right)_T = 0\) since \(u\), an energy density, is independent of volume.
> \(^6\)Note that when the cavity is in equilibrium with the radiation inside it, the power incident is equal to the power emitted; hence the expression for \(\mathcal{F}\) expresses the power emitted by the surface and the power incident on the surface.
> \(^7\)The power per unit area is equal to an energy flux, sometimes called a radiative flux or irradiance, see Section 37.3.

---

#### 23.2 Spectral energy density

The energy density \(u\) of electromagnetic radiation is a quantity that tells you how many Joules are stored in a cubic metre of cavity. What we want to do now is to specify in which frequency ranges that energy is stored. All of this will fall out of the statistical mechanical treatment in Section 23.5, but we want to continue to apply a classical treatment to see how far we can get. To do this, consider two containers, each in contact with thermal reservoirs at temperature \(T\) and joined to one another by a tube, as illustrated schematically in Fig. 23.2. The system is allowed to come to equilibrium.

[Image: Two cavities at temperature T, connected by a tube. One cavity is lined with soot, the other with a mirror coating.]
**Fig. 23.2** Two cavities at temperature \(T\): one is lined with soot and the other with a mirror coating.

The thermal reservoirs are at the same temperature \(T\) and so we know from the second law of thermodynamics that there can be no net heat flow from either one of the bodies to the other. Therefore there can be no net energy flux along the tube, so that the energy flux from the soot-lined cavity along the tube from left to right must be balanced by the energy flux from the mirror-lined cavity along the tube from right to left. Equation 23.12 thus tells us that each cavity must have the same energy density \(u\). This argument can be repeated for cavities of different shape and size as well as different coatings. Hence we conclude that \(u\) is independent of shape, size, or material of the cavity. But maybe one cavity might have more energy density than the other at certain wavelengths, even if it has to have the same energy density overall? This is not the case, as we shall now prove. First, we make a definition.

- The **spectral energy density** \(u_\lambda\) is defined as follows: \(u_\lambda d\lambda\) is the energy density due to those photons which have wavelengths between \(\lambda\) and \(\lambda + d\lambda\). The total energy density is then
$$u = \int u_\lambda d\lambda. \tag{23.13}$$
Now imagine that a filter, which only allows a narrow band of radiation at wavelength \(\lambda\) to pass, is inserted at point A in Fig. 23.2 and the system is left to come to equilibrium. The same arguments listed above apply in this case: there is no net energy flux from one cavity to the other and hence the specific internal energy within a narrow wavelength range is the same for each case:
$$u_{\lambda}^{\text{soot}}(T) = u_{\lambda}^{\text{mirror}}(T). \tag{23.14}$$
This demonstrates that the spectral internal energy has no dependence on the material, shape, size, or nature of a cavity. The spectral energy density is thus a universal function of \(\lambda\) and \(T\) only.

> \(u_\lambda\) has units \(\text{J m}^{-3}\text{ m}^{-1}\). We can also define a spectral density in terms of frequency \(\nu\), so that \(u_\nu d\nu\) is the energy density due to those photons which have frequencies between \(\nu\) and \(\nu + d\nu\).

---

### Page 266

#### 23.3 Kirchhoff’s law

We now wish to discuss how well particular surfaces of a cavity will absorb or emit electromagnetic radiation of a particular frequency or wavelength. We therefore make the following additional definitions:

- The **spectral absorptivity** \(\alpha_\lambda\) is the fraction of the incident radiation that is absorbed at wavelength \(\lambda\). (\(\alpha_\lambda\) is dimensionless.)
- The **spectral emissive power** \(e_\lambda\) of a surface is a function such that \(e_\lambda d\lambda\) is the power emitted per unit area by the electromagnetic radiation having wavelengths between \(\lambda\) and \(\lambda + d\lambda\). (\(e_\lambda\) has units \(\text{W m}^{-2}\text{ m}^{-1}\).)

Using these definitions, we may now write down the form for the power per unit area absorbed by a surface, if the incident spectral energy density is \(u_\lambda d\lambda\), as follows:
$$\left(\frac{1}{4}u_\lambda d\lambda c\right) \alpha_\lambda. \tag{23.15}$$
The power per unit area emitted by a surface is given by
$$e_\lambda d\lambda. \tag{23.16}$$
In equilibrium, the expressions in eqns 23.15 and 23.16 must be equal, and hence
$$\frac{e_\lambda}{\alpha_\lambda} = \frac{c}{4} u_\lambda. \tag{23.17}$$

Equation 23.17 expresses **Kirchhoff’s law**, which states that the ratio \(e_\lambda/\alpha_\lambda\) is a universal function of \(\lambda\) and \(T\). Therefore, if you fix \(\lambda\) and \(T\), the ratio \(e_\lambda/\alpha_\lambda\) is fixed and hence \(e_\lambda \propto \alpha_\lambda\). In other words “good absorbers are good emitters” and “bad absorbers are bad emitters”.

**Example 23.1**
Dark-coloured objects which absorb most of the light that falls on them will be good at emitting thermal radiation. One has to be a bit careful here because you have to be sure about which wavelength you are talking about. A better statement of Kirchhoff’s laws would be “good absorbers at one wavelength are good emitters at the same wavelength”.

For example, a white coffee mug absorbs poorly in visible wavelengths so looks white. A black, but otherwise identical, coffee mug absorbs well in visible wavelengths so looks black. Which one is best at keeping your coffee warm? You might conclude that it is the white mug because “poor absorbers are poor emitters” and that the mug will lose less heat by thermal radiation. However, a hot mug emits radiation mainly in the infrared region of the electromagnetic spectrum,\(^8\) and so the mug being white in the visible is immaterial; what you need to know is what “colour” each mug is in the infrared, i.e., measuring their absorption spectra at infrared wavelengths will tell you about their emission properties there.

A **perfect black body** is an object that is defined to have \(\alpha_\lambda = 1\) for all \(\lambda\). Kirchhoff’s law expressed in eqn 23.17 tells us that for this maximum value of \(\alpha\), a black body is the best possible emitter. It is often useful to think of a **black-body cavity**, which is an enclosure whose walls have \(\alpha_\lambda = 1\) for all \(\lambda\) and which contains a gas of photons at the same temperature as the walls, due to emission and absorption of photons by the atoms in the walls. The gas of photons contained in the black-body cavity is known as **black-body radiation**.

**Example 23.2**
The temperature of the Earth’s surface is maintained by radiation from the Sun. By making the approximation that the Sun and the Earth behave as black bodies, show that the ratio of the Earth’s temperature to that of the Sun is given by
$$\frac{T_{\text{Earth}}}{T_{\text{Sun}}} = \sqrt{\frac{R_{\text{Sun}}}{2D}}, \tag{23.18}$$
where \(R_{\text{Sun}}\) is the radius of the Sun and the Earth–Sun separation is \(D\).

> \(^8\)See Appendix D.

---

### Page 267

**Solution:**
The Sun emits a power equal to its surface area \(4\pi R_{\text{Sun}}^2\) multiplied by \(\sigma T_{\text{Sun}}^4\). This power is known as its **luminosity** \(L\) (measured in watts):
$$L = 4\pi R_{\text{Sun}}^2 \sigma T_{\text{Sun}}^4. \tag{23.19}$$
At a distance \(D\) from the Sun, this power is uniformly distributed over a sphere with surface area \(4\pi D^2\), and the Earth is only able to “catch” this power over its projected area \(\pi R_{\text{Earth}}^2\). Thus the power incident on the Earth is
$$\text{power incident} = L \left(\frac{\pi R_{\text{Earth}}^2}{4\pi D^2}\right). \tag{23.20}$$
The power emitted by the Earth, assuming that it has a uniform temperature \(T_{\text{Earth}}\) and behaves as a black body, is simply \(\sigma T_{\text{Earth}}^4\) multiplied by the Earth’s surface area \(4\pi R_{\text{Earth}}^2\), so that
$$\text{power emitted} = 4\pi R_{\text{Earth}}^2 \sigma T_{\text{Earth}}^4. \tag{23.21}$$
Equating eqn 23.20 and eqn 23.21 yields the desired result.

Putting in the numbers \(R_{\text{Sun}} = 7 \times 10^8 \text{ m}\), \(D = 1.5 \times 10^{11} \text{ m}\), and \(T_{\text{Sun}} = 5800 \text{ K}\) yields \(T_{\text{Earth}} = 280 \text{ K}\), which is not bad given the crudeness of the assumptions.

---

### Page 268

#### 23.4 Radiation pressure

To summarize the results of the earlier sections in this chapter, for black-body radiation we have:
$$\text{power radiated per unit area} \quad \mathcal{F} = \frac{1}{4}uc = \sigma T^4, \tag{23.22}$$
$$\text{energy density in radiation} \quad u = \left(\frac{4\sigma}{c}\right) T^4, \tag{23.23}$$
$$\text{pressure on cavity walls} \quad p = \frac{u}{3} = \frac{4\sigma T^4}{3c}. \tag{23.24}$$

If, however, one is dealing with a beam of light, in which all the photons are going in the same direction (rather than in each and every direction as we have in a gas of photons) then these results need to be modified. The pressure exerted by a collimated beam of light can be calculated as follows: a cubic metre of this beam has momentum \(n\hbar\mathbf{k} = n\hbar\omega/c\), and this momentum is absorbed by a unit area of surface, normal to the beam, in a time \(1/c\). Thus the pressure is \(p = [n\hbar\omega/c]/[1/c] = n\hbar\omega = u\). A cubic metre of the beam has energy \(n\hbar\omega\), so the power \(\mathcal{F}\) incident on unit area of surface is \(\mathcal{F} = n\hbar\omega/(1/c) = uc\). Hence, we have
$$\text{power radiated per unit area} \quad \mathcal{F} = uc = \sigma T^4, \tag{23.25}$$
$$\text{energy density in radiation} \quad u = \left(\frac{\sigma}{c}\right) T^4, \tag{23.26}$$
$$\text{pressure on cavity walls} \quad p = u = \frac{\sigma T^4}{c}. \tag{23.27}$$

It is worth emphasizing that electromagnetic radiation exerts a real pressure on a surface and this can be calculated using eqn 23.24 or eqn 23.27 as appropriate. An example of a calculation of radiation pressure is given below.

**Example 23.3**
Sunlight falls on the surface of the Earth with a power per unit area equal to \(\mathcal{F} = 1370 \text{ W m}^{-2}\). Calculate the radiation pressure and compare it with atmospheric pressure.

**Solution:**
Sunlight on the Earth’s surface consists of photons all going in the same direction,\(^9\) and hence we can use
$$p = \frac{\mathcal{F}}{c} = 4.6 \mu\text{Pa}, \tag{23.28}$$
which is more than ten orders of magnitude lower than atmospheric pressure (which is \(\sim 10^5 \text{ Pa}\)).

> \(^9\)We make this approximation because the Sun is sufficiently far from the Earth, so that all the rays of light arriving on Earth are parallel.

---

### Page 269

#### 23.5 The statistical mechanics of the photon gas

Our argument so far has only used classical thermodynamics. We have been able to predict that the energy density \(u\) of a photon gas behaves as \(AT^4\) but we have been able to say nothing about the constant \(A\). It was only through the development of quantum theory that it was possible to derive what \(A\) is, and we will present this in what follows. The crucial insight is that electromagnetic waves in a cavity can be described by simple harmonic oscillators. The angular frequency \(\omega\) of each mode of oscillation is related to the wave vector \(\mathbf{k}\) by
$$\omega = ck \tag{23.29}$$
(see Fig. 23.3) and hence the density of states\(^{10}\) of electromagnetic waves as a function of wave vector \(\mathbf{k}\) is given by
$$g(\mathbf{k}) d^3k = \frac{4\pi k^2 dk}{(2\pi/L)^3} \times 2, \tag{23.30}$$
where the cavity is assumed to be a cube of volume \(V = L^3\) and the factor two corresponds to the two possible polarizations of the electromagnetic waves. Thus
$$g(k) dk = \frac{V k^2 dk}{\pi^2}, \tag{23.31}$$

[Image: A graph of angular frequency omega versus wave vector k. The relation is a straight line passing through the origin, indicating omega = ck.]
**Fig. 23.3** The relation between \(\omega\) and \(k\), for example that in eqn 23.29, is known as a dispersion relation. For light (plotted here) this relation is very simple and is called non-dispersive because both the phase velocity (\(\omega/k\)) and the group velocity (\(d\omega/dk\)) are equal.

> \(^{10}\)This treatment is similar to the analysis in Section 21.1 for the ideal gas.

---

### Page 270

and hence the density of states \(g(\omega)\), now written as a function of frequency using eqn 23.29, is
$$g(\omega) = g(k) \frac{dk}{d\omega} = \frac{g(k)}{c}, \tag{23.32}$$
and hence
$$g(\omega) d\omega = \frac{V \omega^2 d\omega}{\pi^2 c^3}. \tag{23.33}$$

We can derive \(U\) for the photon gas by using the expression for \(U\) for a single simple harmonic oscillator in eqn 20.29 to give
$$U = \int_0^\infty g(\omega) d\omega \hbar\omega \left(\frac{1}{2} + \frac{1}{e^{\beta\hbar\omega} - 1}\right). \tag{23.34}$$

This presents us with a problem since the first part of this expression, due to the sum of all the zero-point energies, diverges:
$$\int_0^\infty g(\omega) d\omega \frac{1}{2}\hbar\omega \to \infty. \tag{23.35}$$
This must correspond to the energy of the vacuum, so after swallowing hard we redefine our zero of energy so that this infinite contribution is swept conveniently under the carpet. We are therefore left with
$$U = \int_0^\infty g(\omega) d\omega \frac{\hbar\omega}{e^{\beta\hbar\omega} - 1} = \frac{V\hbar}{\pi^2 c^3} \int_0^\infty \frac{\omega^3 d\omega}{e^{\beta\hbar\omega} - 1}. \tag{23.36}$$

If we make the substitution \(x = \hbar\beta\omega\), we can rewrite this as
$$U = \frac{V\hbar}{\pi^2 c^3} \left(\frac{1}{\hbar\beta}\right)^4 \int_0^\infty \frac{x^3 dx}{e^x - 1} = \left(\frac{V \pi^2 k_B^4}{15 c^3 \hbar^3}\right) T^4, \tag{23.37}$$
and hence \(u = U/V = AT^4\). Here, use has been made of the integral
$$\int_0^\infty \frac{x^3 dx}{e^x - 1} = \zeta(4)\Gamma(4) = \frac{\pi^4}{15}, \tag{23.38}$$
which is proved in Appendix C.4 (see eqn C.25). This therefore establishes that the constant \(A = 4\sigma/c\) is given by
$$A = \frac{\pi^2 k_B^4}{15 c^3 \hbar^3}, \tag{23.39}$$
and hence the Stefan–Boltzmann constant\(^{11}\) \(\sigma\) is
$$\sigma = \frac{\pi^2 k_B^4}{60 c^2 \hbar^3} = 5.67 \times 10^{-8} \text{ W m}^{-2}\text{ K}^{-4}. \tag{23.40}$$

> \(^{11}\)If you prefer to use \(h\), rather than \(\hbar\), the Stefan–Boltzmann constant is written as \(\sigma = \frac{2\pi^5 k_B^4}{15 c^2 h^3}\).

---

### Page 271

#### 23.6 Black-body distribution

The expression in eqn 23.36 can be rewritten as
$$u = \frac{U}{V} = \int u_\omega d\omega, \tag{23.41}$$

[Image: Two graphs of the black-body distribution. (a) shows u_nu versus frequency nu for T = 200 K, 250 K, and 300 K. (b) shows u_lambda versus wavelength lambda for the same temperatures.]
**Fig. 23.4** The black-body distribution of spectral energy density, plotted for 200 K, 250 K, and 300 K as a function of (a) frequency and (b) wavelength. The upper scale shows the frequency in inverse centimetres, a unit beloved of spectroscopists.

where \(u_\omega\) is a different form of the spectral energy density (written this time as a function of angular frequency \(\omega = 2\pi\nu\)). It thus takes the form
$$u_\omega = \frac{\hbar}{\pi^2 c^3} \frac{\omega^3}{e^{\beta\hbar\omega} - 1}. \tag{23.42}$$
This spectral energy density function is known as a **black-body distribution**. We can also express this in terms of frequency \(\nu\) by writing \(u_\omega d\omega = u_\nu d\nu\), and using \(\omega = 2\pi\nu\) and hence \(d\omega/d\nu = 2\pi\). This yields
$$u_\nu = \frac{8\pi h}{c^3} \frac{\nu^3}{e^{\beta h\nu} - 1}. \tag{23.43}$$
This function is plotted in Fig. 23.4(a). Similarly, we can transform this into wavelength, by writing\(^{12}\) \(u_\nu |d\nu| = u_\lambda |d\lambda|\), and using \(\nu = c/\lambda\) and hence \(d\nu/d\lambda = -c/\lambda^2\). This yields an expression for \(u_\lambda\) as follows:
$$u_\lambda = \frac{8\pi hc}{\lambda^5} \frac{1}{e^{\beta hc/\lambda} - 1}. \tag{23.44}$$
This is shown in Fig. 23.4(b).

We note several features of this black-body distribution.

- At low frequency (i.e., long wavelength), when \(h\nu/k_B T \ll 1\), the exponential term can be written as
$$e^{\beta h\nu} \approx 1 + \frac{h\nu}{k_B T}, \tag{23.45}$$

> \(^{12}\)There are modulus signs in the expression since we are counting the energy density within either a frequency or a wavelength interval. Because \(\nu = c/\lambda\), a positive \(d\nu\) corresponds to a negative \(d\lambda\), but we do not care in which direction the interval is defined.

---

### Page 272

and hence
$$u_\nu \to \frac{8\pi k_B T \nu^2}{c^3}, \tag{23.46}$$
and equivalently
$$u_\lambda \to \frac{8\pi k_B T}{\lambda^4}. \tag{23.47}$$

These two expressions are different forms of the **Rayleigh–Jeans law**, and were derived in the nineteenth century before the advent of quantum mechanics. As that might imply, Planck’s constant \(h\) does not appear in them. These expressions are the correct limit of the black-body distribution, as shown in Fig. 23.5. They created problems at the time, because if you take the Rayleigh–Jeans form of \(u_\lambda\) and assume that it is true for all wavelengths, and then try and integrate it to get the total internal energy density \(u\), you find that
$$u = \int_0^\infty u_\lambda d\lambda = \int_0^\infty \frac{8\pi k_B T d\lambda}{\lambda^4} \to \infty. \tag{23.48}$$
This apparent divergence in \(u\) was called the **ultraviolet catastrophe**, because integrating down to small wavelengths (towards the ultraviolet) produced a divergence. In fact, such high–energy electromagnetic waves are not excited because light is quantized and it costs too much energy to produce an ultraviolet photon when the temperature is too low. Of course, using the correct black-body \(u_\lambda\) from eqn 23.44, the correct form
$$u = \int_0^\infty u_\lambda d\lambda = \frac{4\sigma}{c} T^4 \tag{23.49}$$
is obtained.

[Image: A graph of u_lambda versus lambda showing the black-body curve (solid line) and the Rayleigh-Jeans law (dashed line). The Rayleigh-Jeans law matches the black-body curve at long wavelengths but diverges at short wavelengths.]
**Fig. 23.5** The black-body energy density \(u_\lambda\) (thick solid line), together with the Rayleigh–Jeans expression, eqn 23.47 (dashed line), which is the long-wavelength limit of the black-body distribution.

- One can also define the **radiance** (or surface brightness) \(B_\nu\) as the flux of radiation per steradian (the unit of solid angle, abbreviated to sr) in a unit frequency interval. This function gives the power through an element of unit area, per unit frequency, from an element of solid angle. The units of radiance are \(\text{W m}^{-2}\text{ Hz}^{-1}\text{ sr}^{-1}\). Because there are a total of \(4\pi\) steradians, we have that\(^{13}\)
$$B_\nu(T) = \frac{c}{4\pi} u_\nu(T) = \frac{2h}{c^2} \frac{\nu^3}{e^{\beta h\nu} - 1}. \tag{23.50}$$
By analogy, \(B_\lambda\), with units \(\text{W m}^{-2}\text{ m}^{-1}\text{ sr}^{-1}\), is defined by
$$B_\lambda(T) = \frac{c}{4\pi} u_\nu(T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\beta hc/\lambda} - 1}. \tag{23.51}$$

- Wilhelm Wien\(^{14}\) found experimentally in 1896, before the advent of quantum mechanics, that the product of the temperature and the wavelength at which the maximum of the black-body distribution \(u_\lambda\) is found is a constant. This is a statement of what is known as **Wien’s law**. The constant can be given as follows:
$$\lambda_{\text{max}}T = \text{a constant}. \tag{23.52}$$

> \(^{13}\)Note that if we divide the energy density by the time taken for unit volume of photons to pass through unit area of surface, namely \(1/c\), we have the energy flux.
> \(^{14}\)His full name was Wilhelm Carl Werner Otto Fritz Franz Wien (1864–1928).

---

### Page 273

Wien’s law follows from the fact that \(\lambda_{\text{max}}\) can be determined by the condition \(du_\lambda/d\lambda = 0\), and applying this to eqn 23.44 leads to \(\beta hc/\lambda_{\text{max}} = \text{a constant}\). Hence \(\lambda_{\text{max}}T\) is a constant, which is Wien’s law. The law tells us that at room temperature, objects that are approximately black bodies will radiate the most at wavelength \(\lambda_{\text{max}} \approx 10 \mu\text{m}\), which is in the infrared region of the electromagnetic spectrum, as demonstrated in Fig. 23.4(b).

One can easily show\(^{15}\) that the maximum in \(u_\nu\) occurs at a frequency given by
$$\frac{h\nu}{k_B T} = 2.82144 \tag{23.53}$$
and the maximum in \(u_\lambda\) occurs at a wavelength given by
$$\frac{hc}{\lambda k_B T} = 4.96511. \tag{23.54}$$
This can be used to show that the product \(\lambda T\) is given by
$$\lambda T = \begin{cases} 5.1 \text{ mm K} & \text{at the maximum of } u_\nu(T), \\ 2.9 \text{ mm K} & \text{at the maximum of } u_\lambda(T). \end{cases} \tag{23.55}$$
These maxima do not occur at the same place for each distribution because one is measured per unit frequency interval and the other per unit wavelength interval, and these are different.\(^{16}\)

> \(^{15}\)See Exercise 23.2.
> \(^{16}\)The difference between \(d\nu\) and \(d\lambda\) is derived as follows. The relationship between frequency and wavelength is given by \(c = \nu\lambda\), and hence \(\nu = c/\lambda\), so that \(d\nu = -\frac{c}{\lambda^2} d\lambda\).

Figure 23.6(a) shows how the shape of the distribution changes with temperature for \(u_\nu\) and Fig. 23.6(b) for \(u_\lambda\) on log–log scales. These diagrams show how the peak of the black-body distribution lies in the optical region of the spectrum for temperatures of several thousand kelvin, but in the microwave region for a temperature of a few kelvin. This fact is very relevant for the black-body radiation in the Universe, which we describe in the following section.

---

#### 23.7 Cosmic microwave background radiation

In 1978, Penzias and Wilson of Bell Labs, New Jersey, USA won the Nobel Prize for their serendipitous discovery (in 1963–1965) of seemingly uniform microwave emission coming from all directions in the sky, which has come to be known as the **cosmic microwave background** (CMB). Remarkably, the spectral shape of this emission exhibits, to high precision, the distribution for black-body radiation of temperature 2.7 K (see Fig. 23.7) with a peak in the emission spectrum at a wavelength of about 1 mm. It is startling that the radiation is uniform, or isotropic, to better than 1 part in \(10^5\) (meaning that its spectrum and intensity are almost the same if you measure in different directions in the sky). This is one of the key pieces of evidence in favour of the hot big bang model for the origin of the Universe. It implies that there was a time when all of the Universe we see now was in thermal equilibrium.\(^{17}\)

> \(^{17}\)Note that different black-body distributions, that is multiple curves corresponding to regions at a variety of different temperatures, do not superpose to form a single black-body distribution.

---

### Page 274

[Image: Two graphs of the black-body distribution on a logarithmic scale at four different temperatures. (a) shows u_nu versus nu, with the Rayleigh-Jeans limit shown as a dotted line. (b) shows u_lambda versus lambda, also with the Rayleigh-Jeans limit shown.]
**Fig. 23.6** The black-body distribution of spectral energy density, plotted on a logarithmic scale for four different temperatures as a function of (a) frequency and (b) wavelength. The dotted lines show the Rayleigh-Jeans law (eqns 23.46 and 23.46) which are valid in the low frequency (long wavelength) limit.

We can make various inferences about the origin of the Universe from observations of the cosmic microwave background. It can be shown that the energy density of radiation in the expanding Universe falls off as the fourth power of the scale factor (which you can think of as the linear magnification factor describing the separation of a pair of marker galaxies in the Universe, a quantity that increases with cosmic time). From the Stefan–Boltzmann law, the energy density of radiation falls off as \(T^4\), so temperature and scale factor are inversely proportional to one another, so the Universe cools as it expands. Conversely, when the Universe was much younger, it was much smaller and much hotter. Extrapolating back in time, one finds that temperatures were such that physical conditions were very different. For example, it was too hot for matter to exist as atoms, and everything was ionized. Further back in cosmic time still, even quarks and hadrons, the sub-structure of protons and neutrons were thought to be dissociated.

---

#### 23.8 The Einstein A and B coefficients

If a gas of atoms is subjected to thermal radiation, the atoms can respond by making transitions between different energy levels. We can think about this effect in terms of absorption and emission of photons by the atom. The atoms are sitting in a bath of photons which we call the **radiation field** and it has an energy density \(u_\omega\) given by eqn 23.42. In this section, we will consider the effect of this radiation field on the transitions between atomic energy levels by modelling the atom as a simple two-level system. Consider the two-level system shown in Fig. 23.8, which comprises two energy levels, a lower level 1 and an upper level 2, separated by an energy \(\hbar\omega\). In the absence of the radiation field, atoms in the upper level can decay to the lower level by the process of **spontaneous emission** of a photon [Fig. 23.8(a)]. The number of atoms in the upper level, \(N_2\), is given by solving a simple differential equation
$$\frac{dN_2}{dt} = -A_{21} N_2, \tag{23.56}$$
where \(A_{21}\) is a constant. This expresses simply that the decay rate depends on the number of atoms in the upper level. The solution of this equation is
$$N_2(t) = N_2(0)e^{-t/\tau}, \tag{23.57}$$
where \(\tau \equiv 1/A_{21}\) is the natural radiative lifetime of the upper level.

[Image: Three diagrams (a), (b), and (c) showing transitions in a two-level system. (a) Spontaneous emission: a downward arrow from level 2 to level 1, with a photon emitted. (b) Absorption: an upward arrow from level 1 to level 2, with a photon absorbed. (c) Stimulated emission: a downward arrow from level 2 to level 1, with two photons emitted.]
**Fig. 23.8** Transitions for a two-level system: (a) spontaneous emission of a photon; (b) absorption of a photon; (c) stimulated emission of a photon.

In the presence of a radiation field of energy density \(u_\omega\), two further processes are possible:

- An atom in level 1 can absorb a photon of energy \(\hbar\omega\) and will end up in level 2 [Fig. 23.8(b)]. This process is called **absorption**, and will occur at a rate that is proportional both to \(u_\omega\) and to the number of atoms in level 1. Thus the rate can be written as \(N_1 B_{12} u_\omega\), where \(B_{12}\) is a constant.

---

### Page 276

- Quantum mechanics allows the reverse process to occur. Thus an atom in level 2 can emit a photon of energy \(\hbar\omega\) as a direct result of the radiation field, and the atom will end up in level 1 [Fig. 23.8(c)]. In terms of individual photons, this process involves two photons: the presence of a first photon in the radiation field (which is absorbed and then re-emitted) stimulates the emission by the atom of an additional photon. This process is called **stimulated emission**, and will occur at a rate which is proportional both to \(u_\omega\) and to the number of atoms in level 2. Thus the rate can be written as \(N_2 B_{21} u_\omega\) where \(B_{21}\) is a constant.

The constants \(A_{21}, B_{12}\) and \(B_{21}\) are called the **Einstein A and B coefficients**. To summarize, our three processes are:
(1) spontaneous emission (one photon emitted);
(2) absorption (one photon absorbed);
(3) stimulated emission (one photon absorbed, two photons emitted).

In the steady state, with all three processes occurring simultaneously, we must have
$$N_2 B_{21} u_\omega + N_2 A_{21} = N_1 B_{12} u_\omega. \tag{23.58}$$
This can be rearranged to give
$$u_\omega = \frac{A_{21}/B_{21}}{(N_1 B_{12}/N_2 B_{21}) - 1}. \tag{23.59}$$
If the system is in thermal equilibrium, then the relative populations of the two levels must be given by a Boltzmann factor, i.e.,
$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-\beta\hbar\omega}, \tag{23.60}$$
where \(g_1\) and \(g_2\) are the degeneracies of levels 1 and 2 respectively. Substitution of eqn 23.60 into eqn 23.59 yields
$$u_\omega = \frac{A_{21}/B_{21}}{(g_1 B_{12}/g_2 B_{21}) e^{\beta\hbar\omega} - 1}, \tag{23.61}$$
and comparison with eqn 23.42 yields the following relations between the Einstein A and B coefficients:
$$B_{21} = \frac{g_1}{g_2} B_{12} \quad \text{and} \quad A_{21} = \frac{\hbar\omega^3}{\pi^2 c^3} B_{21}. \tag{23.62}$$

**Example 23.4**
When will a system of atoms in a radiation field exhibit gain, i.e., produce more photons than they absorb?

**Solution:**
The atoms will produce more photons than they absorb if the rate of stimulated emission is greater than the absorption rate, and this will occur if
$$N_2 B_{21} u_\omega > N_1 B_{12} u_\omega, \tag{23.63}$$

---

### Page 277

which implies that
$$\frac{N_2}{g_2} > \frac{N_1}{g_1}. \tag{23.64}$$
This means that we need to have a **population inversion**, so that the number of atoms (“the population”) in the upper state (per degenerate level) exceeds that in the lower state. This is the principle behind the operation of the **laser** (a word that stands for light amplification by stimulated emission of radiation). However, in our two-level system such a population inversion is not possible in thermal equilibrium. For laser operation, it is necessary to have further energy levels to provide additional transitions: these can provide a mechanism to ensure that level 2 is pumped (fed by transitions from another level, keeping its population high) and that level 1 can drain away (into another lower level, so that level 1 has a low population).

---

### Chapter summary

- The power emitted per unit area of a black-body surface at temperature \(T\) is given by \(\sigma T^4\), where
$$\sigma = \frac{\pi^2 k_B^4}{60 c^2 \hbar^3} = 5.67 \times 10^{-8} \text{ W m}^{-2}\text{ K}^{-4}.$$
- Radiation pressure \(p\) due to black-body photons is equal to \(u/3\) where \(u\) is the energy density. Radiation pressure due to a collimated beam of light is equal to \(u\).
- The spectral energy density \(u_\omega\) takes the form of a black-body distribution. This form fits well to the experimentally measured form of the cosmic microwave background. It is also important in the theory of lasers.

---

### Further reading

- A discussion of lasers may be found in Foot (2004), Chapters 1 and 7.
- More information concerning the cosmic microwave background is in Liddle (2003) Chapter 10 and Carroll and Ostlie (1996) Chapter 27.

---

### Page 278

### Exercises

**(23.1)** The temperature of the Earth’s surface is maintained by radiation from the Sun. By making the approximation that the Sun is a black body, but now assuming that the Earth is a grey body with albedo \(A\) (this means that it reflects a fraction \(A\) of the incident energy), show that the ratio of the Earth’s temperature to that of the Sun is given by
$$T_{\text{Earth}} = T_{\text{Sun}} (1 - A)^{1/4} \sqrt{\frac{R_{\text{Sun}}}{2D}}, \tag{23.65}$$
where \(R_{\text{Sun}}\) is the radius of the Sun and the Earth–Sun separation is \(D\).

**(23.2)** Show that the maxima in the functions \(u_\nu\) and \(u_\lambda\) can be computed by maximizing the function \(x^\alpha/(e^x - 1)\) for \(\alpha = 3\) and \(\alpha = 5\) respectively. Show that this implies that
$$x = \alpha(1 - e^{-x}). \tag{23.66}$$
This equation can be solved by iterating
$$x_n = \alpha(1 - e^{-x_{n-1}}); \tag{23.67}$$
now show that (using an initial guess of \(x_1 = 1\)) this leads to the values given in eqns 23.53 and 23.54.

**(23.3)** The cosmic microwave background (CMB) radiation has a temperature of 2.73 K.
(a) What is the photon energy density in the Universe?
(b) Estimate the number of CMB photons that fall on the outstretched palm of your hand every second.
(c) What is the average energy due to CMB radiation that lands on your outstretched palm every second?
(d) What radiation pressure do you feel from CMB radiation?

**(23.4)** What is the ratio of the number of photons from the Sun to the number of CMB photons that irradiate your outstretched hand every second (during the daytime!)?

**(23.5)** Thermal radiation can be treated thermodynamically as a gas of photons with internal energy \(U = u(T)V\) and pressure \(p = u(T)/3\), where \(u(T)\) is the energy density. Show that:
(a) the entropy density \(s\) is given by \(s = 4p/T\);
(b) the Gibbs function \(G = 0\);
(c) the heat capacity at constant volume \(C_v = 3s\) per unit volume;
(d) the heat capacity at constant pressure, \(C_p\), is infinite. (What on earth does that mean?)

**(23.6)** Ignoring the zero-point energy, show that the partition function \(\mathcal{Z}\) for a gas of photons in volume \(V\) is given by
$$\ln \mathcal{Z} = -\frac{V}{\pi^2 c^3} \int_0^\infty \omega^2 \ln(1 - e^{-\hbar\omega\beta}) d\omega, \tag{23.68}$$
and hence, by integrating by parts, that
$$\ln \mathcal{Z} = \frac{V \pi^2 (k_B T)^3}{45 \hbar^3 c^3}. \tag{23.69}$$
Hence show that
$$F = -\frac{4\sigma V T^4}{3c}, \tag{23.70}$$
$$S = \frac{16\sigma V T^3}{3c}, \tag{23.71}$$
$$U = \frac{4\sigma V T^4}{c}, \tag{23.72}$$
$$p = \frac{4\sigma T^4}{3c}, \tag{23.73}$$
and hence that \(U = -3F\), \(pV = U/3\), and \(S = 4U/3T\).

**(23.7)** Show that the total number \(N\) of photons in black-body radiation contained in a volume \(V\) is
$$N = \int_0^\infty \frac{g(\omega) d\omega}{e^{\hbar\omega/k_B T} - 1} = \frac{2\zeta(3)}{\pi^2} \left(\frac{k_B T}{\hbar c}\right)^3 V, \tag{23.74}$$
where \(\zeta(3) = 1.20206\) is a Riemann zeta function (see Appendix C.4). Hence show that the average energy per photon is
$$\frac{U}{N} = \frac{\pi^4}{30\zeta(3)} k_B T = 2.701 k_B T, \tag{23.75}$$
and that the average entropy per photon is
$$\frac{S}{N} = \frac{2\pi^4}{45\zeta(3)} k_B = 3.602 k_B. \tag{23.76}$$
The result for the internal energy of a photon gas is therefore \(U = 2.701 N k_B T\), whereas for a classical ideal gas one obtains \(U = \frac{3}{2} N k_B T\). Why should the two results be different? Compare the expression for the entropy of a photon gas with that for an ideal gas (the Sackur–Tetrode equation); what is the physical reason for the difference?

---

Here are the **Appendices A–H** (Pages 461–484), completing the full Markdown conversion of the book.

---

## Appendix A: Fundamental constants

| Constant | Symbol | Value |
| :--- | :--- | :--- |
| Bohr radius | \(a_0\) | \(5.292 \times 10^{-11}\) m |
| speed of light in free space | \(c\) | \(2.9979 \times 10^8\) m s\(^{-1}\) |
| Electronic charge | \(e\) | \(1.6022 \times 10^{-19}\) C |
| Planck constant | \(h\) | \(6.626 \times 10^{-34}\) J s |
| \(h/2\pi =\) | \(\hbar\) | \(1.0546 \times 10^{-34}\) J s |
| Boltzmann constant | \(k_B\) | \(1.3807 \times 10^{-23}\) J K\(^{-1}\) |
| electron rest mass | \(m_e\) | \(9.109 \times 10^{-31}\) kg |
| proton rest mass | \(m_p\) | \(1.6726 \times 10^{-27}\) kg |
| Avogadro number | \(N_A\) | \(6.022 \times 10^{23}\) mol\(^{-1}\) |
| standard molar volume | | \(22.414 \times 10^{-3}\) m\(^3\) mol\(^{-1}\) |
| molar gas constant | \(R\) | \(8.314\) J mol\(^{-1}\) K\(^{-1}\) |
| fine structure constant | \(\frac{e^2}{4\pi\epsilon_0\hbar c} = \alpha\) | \((137.04)^{-1}\) |
| permittivity of free space | \(\epsilon_0\) | \(8.854 \times 10^{-12}\) F m\(^{-1}\) |
| magnetic permeability of free space | \(\mu_0\) | \(4\pi \times 10^{-7}\) H m\(^{-1}\) |
| Bohr magneton | \(\mu_B\) | \(9.274 \times 10^{-24}\) A m\(^2\) or J T\(^{-1}\) |
| nuclear magneton | \(\mu_N\) | \(5.051 \times 10^{-27}\) A m\(^2\) or J T\(^{-1}\) |
| neutron magnetic moment | \(\mu_n\) | \(-1.9130 \mu_N\) |
| proton magnetic moment | \(\mu_p\) | \(2.7928 \mu_N\) |
| Rydberg constant | \(R_\infty\) | \(1.0974 \times 10^7\) m\(^{-1}\) |
| | \(R_\infty hc\) | \(13.606\) eV |
| Stefan constant | \(\sigma\) | \(5.670 \times 10^{-8}\) W m\(^{-2}\) K\(^{-4}\) |
| gravitational constant | \(G\) | \(6.674 \times 10^{-11}\) N m\(^2\) kg\(^{-2}\) |
| mass of the Sun | \(M_\odot\) | \(1.99 \times 10^{30}\) kg |
| mass of the Earth | \(M_\oplus\) | \(5.97 \times 10^{24}\) kg |
| radius of the Sun | \(R_\odot\) | \(6.96 \times 10^8\) m |
| radius of the Earth | \(R_\oplus\) | \(6.378 \times 10^6\) m |
| 1 astronomical unit | | \(1.496 \times 10^{11}\) m |
| 1 light year | | \(9.460 \times 10^{15}\) m |
| 1 parsec | | \(3.086 \times 10^{16}\) m |
| Planck length | \(\sqrt{\frac{\hbar G}{c^3}} = l_P\) | \(1.616 \times 10^{-35}\) m |
| Planck mass | \(\sqrt{\frac{\hbar c}{G}} = m_P\) | \(2.176 \times 10^{-8}\) kg |
| Planck time | \(l_P/c = t_P\) | \(5.391 \times 10^{-44}\) s |

---

## Appendix B: Useful formulae

**(1) Trigonometry**
$$e^{i\theta} = \cos\theta + i\sin\theta$$
$$\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$$
$$\sin(\theta + \phi) = \sin\theta\cos\phi + \cos\theta\sin\phi$$
$$\cos(\theta + \phi) = \cos\theta\cos\phi - \sin\theta\sin\phi$$
$$\tan\theta = \sin\theta/\cos\theta$$
$$\cos^2\theta + \sin^2\theta = 1$$
$$\cos 2\theta = \cos^2\theta - \sin^2\theta$$
$$\sin 2\theta = 2\cos\theta\sin\theta$$

**(2) Hyperbolics**
$$\sinh x = \frac{e^x - e^{-x}}{2}$$
$$\cosh x = \frac{e^x + e^{-x}}{2}$$
$$\cosh^2 x - \sinh^2 x = 1$$
$$\cosh 2x = \cosh^2 x + \sinh^2 x$$
$$\sinh 2x = 2\cosh x\sinh x$$
$$\tanh x = \sinh x/\cosh x$$

**(3) Logarithms**
$$\log_b(xy) = \log_b(x) + \log_b(y)$$
$$\log_b(x/y) = \log_b(x) - \log_b(y)$$
$$\log_b(x) = \frac{\log_k(x)}{\log_k(b)}$$
$$\ln(x) \equiv \log_e(x) \quad \text{where } e = 2.71828182846\ldots$$

**(4) Geometric progression**
N-term series:
$$a + ar + ar^2 + \cdots + ar^{N-1} = a \sum_{n=0}^{N-1} r^n = \frac{a(1 - r^N)}{1 - r}.$$
∞-term series:
$$a + ar + ar^2 + \cdots = a \sum_{n=0}^{\infty} r^n = \frac{a}{1 - r}.$$

**(5) Taylor and Maclaurin series**
A Taylor series of a real function \(f(x)\) about a point \(x = a\) is given by
$$f(x) = f(a) + (x - a)\left(\frac{df}{dx}\right)_{x=a} + \frac{(x - a)^2}{2!}\left(\frac{d^2 f}{dx^2}\right)_{x=a} + \ldots$$
If \(a = 0\), the expansion is a Maclaurin series
$$f(x) = f(0) + x\left(\frac{df}{dx}\right)_{x=0} + \frac{x^2}{2!}\left(\frac{d^2 f}{dx^2}\right)_{x=0} + \ldots$$

**(6) Some Maclaurin series (valid for \(|x| < 1\))**
$$(1 + x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots$$
$$(1 - x)^{-1} = 1 + x + x^2 + x^3 + \cdots$$
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$
$$\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots$$
$$\tanh x = x - \frac{x^3}{3} + \frac{2x^5}{15} - \cdots$$
$$\tanh^{-1} x = x + \frac{x^3}{3} + \frac{x^5}{5} + \frac{x^7}{7} + \cdots$$
$$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$$

**(7) Integrals**
Indefinite (with \(a > 0\)):
$$\int \frac{dx}{x^2 + a^2} = \frac{1}{a}\tan^{-1}\frac{x}{a}$$
$$\int \frac{dx}{x^2 - a^2} = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|$$
$$\int \frac{dx}{\sqrt{x^2 + a^2}} = \sinh^{-1}\frac{x}{a}$$
$$\int \frac{dx}{\sqrt{x^2 - a^2}} = \begin{cases} \cosh^{-1}\frac{x}{a} & \text{if } x > a \\ -\cosh^{-1}\frac{x}{a} & \text{if } x < -a \end{cases}$$
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\frac{x}{a}$$

**(8) Vector operators**
- **grad** acts on a scalar field to produce a vector field:
$$\text{grad } \phi = \nabla\phi = \left(\frac{\partial\phi}{\partial x}, \frac{\partial\phi}{\partial y}, \frac{\partial\phi}{\partial z}\right);$$
- **div** acts on a vector field to produce a scalar field:
$$\text{div } \mathbf{A} = \nabla\cdot\mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z};$$
- **curl** acts on a vector field to produce another vector field:
$$\text{curl } \mathbf{A} = \nabla\times\mathbf{A} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\ A_x & A_y & A_z \end{vmatrix};$$
where \(\phi(\mathbf{r})\) and \(\mathbf{A}(\mathbf{r})\) are any given scalar and vector field respectively.

**(9) Vector identities:**
$$\nabla\cdot(\nabla\phi) = \nabla^2\phi$$
$$\nabla\times(\nabla\phi) = 0$$
$$\nabla\cdot(\nabla\times\mathbf{A}) = 0$$
$$\nabla\cdot(\phi\mathbf{A}) = \mathbf{A}\cdot\nabla\phi + \phi\nabla\cdot\mathbf{A}$$
$$\nabla\times(\phi\mathbf{A}) = \phi\nabla\times\mathbf{A} - \mathbf{A}\times\nabla\phi$$
$$\nabla\times(\nabla\times\mathbf{A}) = \nabla(\nabla\cdot\mathbf{A}) - \nabla^2\mathbf{A}$$
$$\nabla\cdot(\mathbf{A}\times\mathbf{B}) = \mathbf{B}\cdot\nabla\times\mathbf{A} - \mathbf{A}\cdot\nabla\times\mathbf{B}$$
$$\nabla(\mathbf{A}\cdot\mathbf{B}) = (\mathbf{A}\cdot\nabla)\mathbf{B} + (\mathbf{B}\cdot\nabla)\mathbf{A} + \mathbf{A}\times(\nabla\times\mathbf{B}) + \mathbf{B}\times(\nabla\times\mathbf{A})$$
$$\nabla\times(\mathbf{A}\times\mathbf{B}) = (\mathbf{B}\cdot\nabla)\mathbf{A} - (\mathbf{A}\cdot\nabla)\mathbf{B} + \mathbf{A}(\nabla\cdot\mathbf{B}) - \mathbf{B}(\nabla\cdot\mathbf{A})$$

These identities can be easily proved by application of the alternating tensor and use of the summation convention. The alternating tensor \(\epsilon_{ijk}\) is defined according to
$$\epsilon_{ijk} = \begin{cases} 1 & \text{if } ijk \text{ is an even permutation of } 123 \\ -1 & \text{if } ijk \text{ is an odd permutation of } 123 \\ 0 & \text{if any two of } i, j, \text{ or } k \text{ are equal} \end{cases}$$
so that the vector product can be written
$$(\mathbf{A}\times\mathbf{B})_i = \epsilon_{ijk} A_j B_k.$$
The summation convention is used here, so that twice repeated indices are assumed summed. The scalar product is then
$$\mathbf{A}\cdot\mathbf{B} = A_i B_i.$$
Use can be made of the identity
$$\epsilon_{ijk}\epsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl},$$
where \(\delta_{ij}\) is the Kronecker delta given by
$$\delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}.$$
The vector triple product is given by
$$\mathbf{A}\times(\mathbf{B}\times\mathbf{C}) = (\mathbf{A}\cdot\mathbf{C})\mathbf{B} - (\mathbf{A}\cdot\mathbf{B})\mathbf{C}.$$

**(10) Cylindrical coordinates**
$$\nabla^2\psi = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial\psi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2\psi}{\partial\phi^2} + \frac{\partial^2\psi}{\partial z^2}$$
$$\nabla\psi = \left(\frac{\partial\psi}{\partial r}, \frac{1}{r}\frac{\partial\psi}{\partial\phi}, \frac{\partial\psi}{\partial z}\right)$$

**(11) Spherical polar coordinates**
$$\nabla^2\psi = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\psi}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2}$$
$$\nabla\psi = \left(\frac{\partial\psi}{\partial r}, \frac{1}{r}\frac{\partial\psi}{\partial\theta}, \frac{1}{r\sin\theta}\frac{\partial\psi}{\partial\phi}\right)$$

---

## Appendix C: Useful mathematics

### Page 464

#### Chapter Outline

**C.1 The factorial integral** 464
**C.2 The Gaussian integral** 464
**C.3 Stirling’s formula** 467
**C.4 Riemann zeta function** 469
**C.5 The polylogarithm** 470
**C.6 Partial derivatives** 471
**C.7 Exact differentials** 472
**C.8 Volume of a hypersphere** 473
**C.9 Jacobians** 473
**C.10 The Dirac delta function** 475
**C.11 Fourier transforms** 475
**C.12 Solution of the diffusion equation** 476
**C.13 Lagrange multipliers** 477

---

#### C.1 The factorial integral

One of the most useful integrals in thermodynamics problems is the following one (which is worth memorizing):
$$n! = \int_0^\infty x^n e^{-x} dx. \tag{C.1}$$

- This integral is simple to prove by induction as follows. First, show that it is true for the case \(n = 0\). Then assume it is true for \(n = k\) and prove it is true for \(n = k + 1\). (Hint: integrate \((k + 1)! = \int_0^\infty x^{k+1} e^{-x} dx\) by parts.)
- It allows you to define the factorial of non-integer numbers. This is so useful that the integral is given a special name, the **gamma function**. The traditional definition of the gamma function is
$$\Gamma(n) = \int_0^\infty x^{n-1} e^{-x} dx \tag{C.2}$$
so that \(\Gamma(n) = (n - 1)!\), i.e., the factorial function and the gamma function are “out of step” with each other, a rather confusing feature. The gamma function is plotted in Fig. C.1 and has a surprisingly complicated structure for negative \(n\). Selected values of the gamma function are listed in Table C.1. The gamma function will appear again in later integrals.

**Table C.1** Selected values of the gamma function. Other values can be generated using \(\Gamma(z + 1) = z\Gamma(z)\).

| \(z\) | \(-\frac{3}{2}\) | \(-\frac{1}{2}\) | \(\frac{1}{2}\) | \(1\) | \(\frac{3}{2}\) | \(2\) | \(\frac{5}{2}\) | \(3\) | \(4\) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| \(\Gamma(z)\) | \(\frac{4\sqrt{\pi}}{3}\) | \(-2\sqrt{\pi}\) | \(\sqrt{\pi}\) | \(1\) | \(\frac{\sqrt{\pi}}{2}\) | \(1\) | \(\frac{3\sqrt{\pi}}{4}\) | \(2\) | \(6\) |

---

#### C.2 The Gaussian integral

The Gaussian is a function of the form \(e^{-\alpha x^2}\), and is plotted in Fig. C.2. It has a maximum at \(x = 0\) and a shape that has been likened to that of a bell. It turns up in many statistical problems, often under the name of the normal distribution. The integral of a Gaussian is another extremely useful integral:
$$\int_{-\infty}^\infty e^{-\alpha x^2} dx = \sqrt{\frac{\pi}{\alpha}}. \tag{C.3}$$

[Image: A graph of the gamma function Gamma(n), showing singularities for integer values of n <= 0. For positive, integer n, Gamma(n) = (n-1)! .]
**Fig. C.1** The gamma function \(\Gamma(n)\) showing the singularities for integer values of \(n \le 0\). For positive, integer \(n\), \(\Gamma(n) = (n - 1)!\).

[Image: A graph of a Gaussian e^{-alpha x^2}, a bell-shaped curve centered at x=0.]
**Fig. C.2** A Gaussian \(e^{-\alpha x^2}\).

- It can be proved by evaluating the two-dimensional integral
$$\int_{-\infty}^\infty dx \int_{-\infty}^\infty dy e^{-\alpha(x^2+y^2)} = \left(\int_{-\infty}^\infty dx e^{-\alpha x^2}\right) \left(\int_{-\infty}^\infty dy e^{-\alpha y^2}\right) = I^2, \tag{C.4}$$
where \(I\) is our desired integral. We can evaluate the left-hand side using polar coordinates, so that
$$I^2 = \int_0^{2\pi} d\theta \int_0^\infty dr\, r e^{-\alpha r^2}, \tag{C.5}$$
which with the substitution \(z = \alpha r^2\) (and hence \(dz = 2\alpha r dr\)) gives
$$I^2 = 2\pi \times \frac{1}{2\alpha} \int_0^\infty dz e^{-z} = \frac{\pi}{\alpha}, \tag{C.6}$$
and hence \(I = \sqrt{\pi/\alpha}\) is proved.

- Even more fun begins when we employ a cunning stratagem: we differentiate both sides of the equation with respect to \(\alpha\). Because \(x\) does not depend on \(\alpha\), this is easy to do. Hence \((d/d\alpha)e^{-\alpha x^2} = -x^2 e^{-\alpha x^2}\) and \((d/d\alpha)\sqrt{\pi/\alpha} = -\sqrt{\pi}/2\alpha^{3/2}\) so that
$$\int_{-\infty}^\infty x^2 e^{-\alpha x^2} dx = \frac{1}{2}\sqrt{\frac{\pi}{\alpha^3}}. \tag{C.7}$$

- This trick can be repeated with equal ease. Differentiating again gives
$$\int_{-\infty}^\infty x^4 e^{-\alpha x^2} dx = \frac{3}{4}\sqrt{\frac{\pi}{\alpha^5}}. \tag{C.8}$$

- Therefore we have a way of generating the integrals between \(-\infty\) and \(\infty\) of \(x^{2n} e^{-\alpha x^2}\), where \(n \ge 0\) is an integer.\(^1\) Because these functions are even, the integrals of the same functions between 0 and \(\infty\) are just half of these results:
$$\int_0^\infty e^{-\alpha x^2} dx = \frac{1}{2}\sqrt{\frac{\pi}{\alpha}},$$
$$\int_0^\infty x^2 e^{-\alpha x^2} dx = \frac{1}{4}\sqrt{\frac{\pi}{\alpha^3}},$$
$$\int_0^\infty x^4 e^{-\alpha x^2} dx = \frac{3}{8}\sqrt{\frac{\pi}{\alpha^5}}.$$

- To integrate \(x^{2n+1} e^{-\alpha x^2}\) between \(-\infty\) and \(\infty\) is easy: the functions are all odd and so the integrals are all zero. To integrate between 0 and \(\infty\), start off with \(\int_0^\infty x e^{-\alpha x^2} dx\), which can be evaluated by noticing that \(x e^{-\alpha x^2}\) is almost what you get when you differentiate \(e^{-\alpha x^2}\). All the odd powers of \(x\) can now be obtained\(^2\) by differentiating that integral with respect to \(\alpha\). Hence,
$$\int_0^\infty x e^{-\alpha x^2} dx = \frac{1}{2\alpha},$$
$$\int_0^\infty x^3 e^{-\alpha x^2} dx = \frac{1}{2\alpha^2},$$
$$\int_0^\infty x^5 e^{-\alpha x^2} dx = \frac{1}{\alpha^3}.$$

> \(^1\)A general formula is \(\int_{-\infty}^\infty x^{2n} e^{-\alpha x^2} dx = \frac{(2n)!}{n!2^{2n}} \sqrt{\frac{\pi}{\alpha^{2n+1}}}\), for integer \(n \ge 0\).
> \(^2\)Another method of getting these integrals is to make the substitution \(y = \alpha x^2\) and turn them into the factorial integrals considered above. This is all very well, but you need to know things like \((-\frac{1}{2})! = \sqrt{\pi}\) to proceed.

- A useful expression for a normalized Gaussian (one whose integral is unity) is
$$\frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x-\mu)^2/2\sigma^2}. \tag{C.9}$$
This has mean \(\langle x \rangle = \mu\) and variance \(\langle (x - \langle x \rangle)^2 \rangle = \sigma^2\).

---

### Page 467

#### C.3 Stirling’s formula

The derivation of Stirling’s formula proceeds by using the integral expression for \(n!\) in eqn C.1, namely
$$n! = \int_0^\infty x^n e^{-x} dx. \tag{C.10}$$
We will play with the right-hand side of this integral and develop an approximation for it. We notice that the integrand \(x^n e^{-x}\) consists of a function that increases with \(x\) (the function \(x^n\)) and a function that decreases with \(x\) (the function \(e^{-x}\)), and so it must have a maximum somewhere (see Fig. C.3(a)). Most of the integral is due to the bulge around this maximum, so we will try to approximate this region around the bulge. As we are eventually going to take logs of this integral, it is natural to work with the logarithm of this integrand, which we will call \(f(x)\). Hence we define the function \(f(x)\) by
$$e^{f(x)} = x^n e^{-x}. \tag{C.11}$$
This implies that \(f(x)\) is given by
$$f(x) = n\ln x - x, \tag{C.12}$$
which is sketched in Fig. C.3(b). When the integrand has a maximum, so will \(f(x)\). Hence the maximum of the integrand, and also the maximum of this function \(f(x)\), can be found using
$$\frac{df}{dx} = \frac{n}{x} - 1 = 0, \tag{C.13}$$
which implies that the maximum in \(f\) is at \(x = n\). We can differentiate again and get
$$\frac{d^2 f}{dx^2} = -\frac{n}{x^2}. \tag{C.14}$$

[Image: Two graphs. (a) shows the integrand x^n e^{-x} (solid line) with a maximum. (b) shows f(x) = -x + n ln x (solid line), which is the natural logarithm of the integrand. The dotted line is the Taylor expansion around the maximum. The curves are for n=3.]
**Fig. C.3** (a) The integrand \(x^n e^{-x}\) (solid line) contains a maximum. (b) The function \(f(x) = -x + n\ln x\) (solid line), which is the natural logarithm of the integrand. The dotted line is the Taylor expansion around the maximum (from eqn C.15). These curves have been plotted for \(n = 3\), but the ability of the Taylor expansion to model the solid line improves as \(n\) increases. Note that (b) shows the natural logarithm of the curves in (a).

Now we can perform a Taylor expansion\(^3\) around the maximum, so that
$$f(x) = f(n) + \left(\frac{df}{dx}\right)_{x=n} (x - n) + \frac{1}{2!}\left(\frac{d^2 f}{dx^2}\right)_{x=n} (x - n)^2 + \cdots = n\ln n - n + 0 \times (x - n) - \frac{1}{2}\frac{n}{n^2}(x - n)^2 + \cdots = n\ln n - n - \frac{(x - n)^2}{2n} + \cdots \tag{C.15}$$

> \(^3\)See Appendix B.

The Taylor expansion approximates \(f(x)\) by a quadratic (see the dotted line in Fig. C.3) and hence \(e^{f(x)}\) approximates to a Gaussian.\(^4\) Putting this as the integrand in eqn C.1, and removing from this integral the terms that do not depend on \(x\), we have
$$n! = e^{n\ln n - n} \int_0^\infty e^{-(x-n)^2/2n + \cdots} dx. \tag{C.16}$$

> \(^4\)See Appendix C.2.

The integral in this expression can be evaluated with the help of eqn C.3 to be
$$\int_0^\infty e^{-(x-n)^2/2n + \cdots} dx \approx \int_{-\infty}^\infty e^{-(x-n)^2/2n} dx = \sqrt{2\pi n}. \tag{C.17}$$
(Here we have used the fact that it doesn’t matter if you put the lower limit of the integral as \(-\infty\) rather than 0 since the integrand, \(e^{-(x-n)^2/2n}\), is a Gaussian centred at \(x = n\) with a width that scales as \(\sqrt{n}\) so that the contribution to the integral from the region between \(-\infty\) and 0 is vanishingly small as \(n\) becomes large.) We have that
$$n! \approx e^{n\ln n - n} \sqrt{2\pi n}, \tag{C.18}$$
and hence
$$\ln n! \approx n\ln n - n + \frac{1}{2}\ln 2\pi n, \tag{C.19}$$
which is one version of Stirling’s formula. When \(n\) is very large, this can be written
$$\ln n! \approx n\ln n - n, \tag{C.20}$$
which is another version of Stirling’s formula.

[Image: A graph of Stirling's approximation for ln n!. The dots are the exact results. The solid line is according to eqn C.19, while the dashed line is eqn C.20. The inset shows the two lines for larger values of n, demonstrating that as n becomes large, eqn C.20 becomes a very good approximation.]
**Fig. C.4** Stirling’s approximation for \(\ln n!\). The dots are the exact results. The solid line is according to eqn C.19, while the dashed line is eqn C.20. The inset shows the two lines for larger values of \(n\) and demonstrates that as \(n\) becomes large, eqn C.20 becomes a very good approximation.

---

### Page 469

The approximation in eqn C.19 is very good, as can be seen in Fig. C.4. The approximation in eqn C.20 (the dotted line in Fig. C.4) slightly underestimates the exact result when \(n\) is small, but as \(n\) becomes large (as is often the case in thermal physics problems) it becomes a very good approximation (as shown in the inset to Fig. C.4).

---

#### C.4 Riemann zeta function

The Riemann zeta function \(\zeta(s)\) is usually defined by
$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}, \tag{C.21}$$
and converges for \(s > 1\) (see Fig. C.5). For \(s = 1\) it gives a divergent series. Some useful values are listed in Table C.2.

[Image: A graph of the Riemann zeta function zeta(s) for s > 1. It decreases from infinity at s=1 and approaches 1 as s goes to infinity.]
**Fig. C.5** The Riemann zeta function \(\zeta(s)\) for \(s > 1\).

**Table C.2** Selected values of the Riemann zeta function.

| \(s\) | \(\zeta(s)\) |
| :--- | :--- |
| 1 | \(\infty\) |
| \(\frac{3}{2}\) | \(\approx 2.612\) |
| 2 | \(\pi^2/6 \approx 1.645\) |
| \(\frac{5}{2}\) | \(\approx 1.341\) |
| 3 | \(\approx 1.20206\) |
| 4 | \(\pi^4/90 \approx 1.0823\) |
| 5 | \(\approx 1.0369\) |
| 6 | \(\pi^6/945 \approx 1.017\) |

Our reason for introducing the Riemann zeta function is that it is involved in many useful integrals. One such is the Bose integral \(I_B(n)\) defined by
$$I_B(n) = \int_0^\infty \frac{dx}{e^x - 1} x^n. \tag{C.22}$$
We can evaluate this as follows:
$$I_B(n) = \int_0^\infty dx \frac{x^n e^{-x}}{1 - e^{-x}} = \int_0^\infty dx x^n \sum_{k=0}^\infty e^{-(k+1)x} = \sum_{k=0}^\infty \frac{1}{(k+1)^{n+1}} \int_0^\infty dy y^n e^{-y} = \zeta(n+1)\Gamma(n+1). \tag{C.23}$$
Thus we have that
$$I_B(n) = \int_0^\infty \frac{x^n dx}{e^x - 1} = \zeta(n+1)\Gamma(n+1). \tag{C.24}$$

So, for example,
$$\int_0^\infty \frac{x^3 dx}{e^x - 1} = \zeta(4)\Gamma(4) = \frac{\pi^4}{90} \times 3! = \frac{\pi^4}{15}. \tag{C.25}$$

Another useful integral can be derived as follows. Consider the integral
$$I = \int_0^\infty \frac{x^{n-1}}{e^{ax} - 1} dx. \tag{C.26}$$
This can be evaluated easily by making the substitution \(y = ax\), yielding
$$I = \frac{1}{a^n} \int_0^\infty \frac{y^{n-1}}{e^y - 1} dy. \tag{C.27}$$
Now, differentiating \(I\) with respect to \(a\) using eqn C.26 gives
$$\frac{dI}{da} = -\int_0^\infty \frac{x^n e^{ax}}{(e^{ax} - 1)^2} dx, \tag{C.28}$$
while using eqn C.27 yields
$$\frac{dI}{da} = -\frac{n}{a^{n+1}} \int_0^\infty \frac{y^{n-1}}{e^y - 1} dy. \tag{C.29}$$
These two expressions should be the same, and hence equating them and putting \(a = 1\) yields
$$\int_0^\infty \frac{x^n e^x}{(e^x - 1)^2} dx = n\zeta(n)\Gamma(n). \tag{C.30}$$
So, for example,
$$\int_0^\infty \frac{x^4 e^x}{(e^x - 1)^2} dx = 4\zeta(4)\Gamma(4) = 4 \times \frac{\pi^4}{90} \times 3! = \frac{4\pi^4}{15}. \tag{C.31}$$

---

#### C.5 The polylogarithm

The polylogarithm function \(\text{Li}_n(z)\) (also known as de Jonquière’s function) is defined as
$$\text{Li}_n(z) = \sum_{k=1}^\infty \frac{z^k}{k^n}, \tag{C.32}$$
where \(z\) is in the open unit disc in the complex plane, i.e., \(|z| \ll 1\). The definition over the whole complex plane follows via the process of analytic continuation. The polylogarithm is useful in the evaluation of integrals of Bose–Einstein and Fermi–Dirac distribution functions. First note that we can write
$$\frac{1}{z^{-1}e^x - 1} = \frac{z e^{-x}}{1 - z e^{-x}} = \sum_{m=0}^\infty (z e^{-x})^{m+1}, \tag{C.33}$$
i.e., as a geometric progression. Hence we can evaluate the following integral:
$$\int_0^\infty \frac{x^{n-1} dx}{z^{-1}e^x - 1} = \sum_{m=0}^\infty \int_0^\infty x^{n-1} (z e^{-x})^{m+1} dx = \sum_{m=0}^\infty \frac{z^{m+1}}{(m+1)^n} \int_0^\infty y^{n-1} e^{-y} dy = \Gamma(n) \sum_{m=0}^\infty \frac{z^{m+1}}{(m+1)^n} = \Gamma(n) \sum_{k=1}^\infty \frac{z^k}{k^n} = \Gamma(n) \text{Li}_n(z). \tag{C.34}$$

Similarly one can show that
$$\int_0^\infty \frac{x^{n-1} dx}{z^{-1}e^x + 1} = -\Gamma(n) \text{Li}_n(-z). \tag{C.35}$$

Combining these equations, one can write in general that
$$\int_0^\infty \frac{x^{n-1} dx}{z^{-1}e^x \pm 1} = \mp \Gamma(n) \text{Li}_n(\mp z). \tag{C.36}$$

Note that when \(|z| \ll 1\), only the first term in the series in eqn C.32 contributes, and
$$\text{Li}_n(z) \approx z. \tag{C.37}$$

Note also that
$$\text{Li}_n(1) = \sum_{k=1}^\infty \frac{1}{k^n} = \zeta(n), \tag{C.38}$$
where \(\zeta(n)\) is the Riemann zeta function (eqn C.21).

---

#### C.6 Partial derivatives

Consider \(x\) as a function of two variables \(y\) and \(z\). This can be written \(x = x(y, z)\), and we have that
$$dx = \left(\frac{\partial x}{\partial y}\right)_z dy + \left(\frac{\partial x}{\partial z}\right)_y dz. \tag{C.39}$$
But rearranging \(x = x(y, z)\) can lead to having \(z\) as a function of \(x\) and \(y\) so that \(z = z(x, y)\), in which case
$$dz = \left(\frac{\partial z}{\partial x}\right)_y dx + \left(\frac{\partial z}{\partial y}\right)_x dy. \tag{C.40}$$
Substituting C.40 into C.39 gives
$$dx = \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial x}\right)_y dx + \left[ \left(\frac{\partial x}{\partial y}\right)_z + \left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x \right] dy.$$

The terms multiplying \(dx\) give the **reciprocal theorem**
$$\left(\frac{\partial x}{\partial z}\right)_y = \frac{1}{\left(\frac{\partial z}{\partial x}\right)_y}, \tag{C.41}$$
and the terms multiplying \(dy\) give the **reciprocity theorem**
$$\left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1. \tag{C.42}$$
This can be combined with the reciprocal theorem to write that
$$\left(\frac{\partial x}{\partial y}\right)_z = -\left(\frac{\partial x}{\partial z}\right)_y \left(\frac{\partial z}{\partial y}\right)_x, \tag{C.43}$$
which is a very useful identity.

---

#### C.7 Exact differentials

An expression such as \(F_1(x, y) dx + F_2(x, y) dy\) is known as an **exact differential** if it can be written as the differential
$$df = \left(\frac{\partial f}{\partial x}\right) dx + \left(\frac{\partial f}{\partial y}\right) dy, \tag{C.44}$$
of a differentiable single-valued function \(f(x, y)\). This implies that
$$F_1 = \left(\frac{\partial f}{\partial x}\right), \quad F_2 = \left(\frac{\partial f}{\partial y}\right), \tag{C.45}$$
or in vector form, \(\mathbf{F} = \nabla f\). Hence the integral of an exact differential is **path independent**, so that [where 1 and 2 are shorthands for \((x_1, y_1)\) and \((x_2, y_2)\)]
$$\int_1^2 [F_1(x, y) dx + F_2(x, y) dy] = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = \int_1^2 df = f(2) - f(1), \tag{C.46}$$
and the answer depends only on the initial and final states of the system. For an **inexact differential** this is not true and knowledge of the initial and final states is not sufficient to evaluate the integral: you have to know which path was taken.

For an exact differential the integral round a closed loop is zero:
$$\oint [F_1(x, y) dx + F_2(x, y) dy] = \oint \mathbf{F} \cdot d\mathbf{r} = \oint df = 0, \tag{C.47}$$
which implies that \(\nabla \times \mathbf{F} = 0\) (by Stokes’ theorem) and hence
$$\left(\frac{\partial F_2}{\partial x}\right) = \left(\frac{\partial F_1}{\partial y}\right) \quad \text{or} \quad \left(\frac{\partial^2 f}{\partial x \partial y}\right) = \left(\frac{\partial^2 f}{\partial y \partial x}\right). \tag{C.48}$$

For thermal physics, a crucial point to remember is that functions of state have exact differentials.

---

#### C.8 Volume of a hypersphere

A hypersphere in \(D\) dimensions and with radius \(r\) is described by the equation
$$\sum_{i=1}^D x_i^2 = r^2. \tag{C.49}$$
It has volume \(V_D\) given
$$V_D = \alpha r^D, \tag{C.50}$$
where \(\alpha\) is a numerical constant which we will now determine.

Consider the integral \(I\) given by
$$I = \int_{-\infty}^\infty dx_1 \cdots \int_{-\infty}^\infty dx_D \exp\left(-\sum_{i=1}^D x_i^2\right). \tag{C.51}$$
This can be evaluated as follows:
$$I = \left(\int_{-\infty}^\infty dx e^{-x^2}\right)^D = \pi^{D/2}. \tag{C.52}$$
Alternatively, we can evaluate it in hyperspherical polars as follows:
$$I = \int_0^\infty dV_D e^{-r^2}, \tag{C.53}$$
where the volume element is given by \(dV_D = \alpha_D r^{D-1} dr\). Hence, equating eqn C.52 and eqn C.53 we have that
$$\pi^{D/2} = \alpha_D \int_0^\infty dr r^{D-1} e^{-r^2} = \alpha_D \frac{\Gamma(D/2)}{2}, \tag{C.54}$$
and hence
$$\alpha = \frac{2\pi^{D/2}}{D\Gamma(D/2)}. \tag{C.55}$$
Hence\(^5\) we obtain the volume of a hypersphere in \(D\) dimensions as
$$V_D = \frac{\pi^{D/2} r^D}{\Gamma(\frac{D}{2} + 1)}. \tag{C.56}$$

> \(^5\)Using \(\Gamma(\frac{D}{2} + 1) = \frac{D}{2}\Gamma(\frac{D}{2})\).

---

#### C.9 Jacobians

Let \(x = g(u, v)\) and \(y = h(u, v)\) be a transformation of the plane. Then the Jacobian of this transformation is
$$\frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}. \tag{C.57}$$

**Example C.1**
The Jacobian of the polar coordinate transformation \(x(r, \theta) = r\cos\theta\) and \(y(r, \theta) = r\sin\theta\) is
$$\frac{\partial(x, y)}{\partial(r, \theta)} = \begin{vmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{vmatrix} = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r. \tag{C.58}$$

If \(g\) and \(h\) have continuous partial differentials such that the Jacobian is never zero, we then have
$$\iint_R f(x, y) dx dy = \iint_S f(g(u, v), h(u, v)) \left|\frac{\partial(x, y)}{\partial(u, v)}\right| du dv. \tag{C.59}$$
So in our example, we would have
$$\iint_R f(x, y) dx dy = \iint_S f(g(r, \theta), h(r, \theta)) r dr d\theta. \tag{C.60}$$

The Jacobian of the inverse transformation is the reciprocal of the Jacobian of the original transformation.
$$\left|\frac{\partial(x, y)}{\partial(u, v)}\right| = \frac{1}{\left|\frac{\partial(u, v)}{\partial(x, y)}\right|}, \tag{C.61}$$
which is a consequence of the fact that the determinant of the inverse of a matrix is the reciprocal of the determinant of the matrix. Other useful identities are
$$\frac{\partial(x, y)}{\partial(u, v)} = -\frac{\partial(y, x)}{\partial(u, v)} = \frac{\partial(y, x)}{\partial(v, u)}, \tag{C.62}$$
$$\frac{\partial(x, y)}{\partial(x, y)} = 1, \tag{C.63}$$
$$\frac{\partial(x, y)}{\partial(x, z)} = \left(\frac{\partial y}{\partial z}\right)_x, \tag{C.64}$$
and
$$\frac{\partial(x, y)}{\partial(u, v)} = \frac{\partial(x, y)}{\partial(a, b)} \frac{\partial(a, b)}{\partial(u, v)}. \tag{C.65}$$

**Quick exercise:**
The Jacobian can be generalized to three dimensions, as
$$\frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{vmatrix}. \tag{C.66}$$
Show that for the transformation of spherical polars \(x = r\sin\theta\cos\phi\), \(y = r\sin\theta\sin\phi\), \(z = r\cos\theta\), the Jacobian is
$$\frac{\partial(x, y, z)}{\partial(r, \theta, \phi)} = r^2 \sin\theta. \tag{C.67}$$

---

#### C.10 The Dirac delta function

The Dirac delta function \(\delta(x - a)\) centred at \(x = a\) is zero for all \(x\) not equal to \(a\), but its area is 1. Hence
$$\int_{-\infty}^\infty \delta(x - a) dx = 1. \tag{C.68}$$
Because the Dirac delta function is such a narrow “spike”, integrals of the Dirac delta function multiplied by any other function \(f(x)\) are simple to evaluate:
$$\int_{-\infty}^\infty f(x)\delta(x - a) dx = f(a). \tag{C.69}$$

---

#### C.11 Fourier transforms

Consider a function \(x(t)\). Its Fourier transform is defined by
$$\tilde{x}(\omega) = \int_{-\infty}^\infty dt e^{-i\omega t} x(t). \tag{C.70}$$
The inverse transform is
$$x(t) = \frac{1}{2\pi} \int_{-\infty}^\infty d\omega e^{i\omega t} \tilde{x}(\omega). \tag{C.71}$$

We now state some useful results concerning Fourier transforms.

- The Fourier transform of a delta function \(\delta(t - t')\) is given by
$$\int_{-\infty}^\infty dt e^{-i\omega t} \delta(t - t') = e^{-i\omega t'}, \tag{C.72}$$
and putting this into the inverse transform shows that
$$\int_{-\infty}^\infty d\omega e^{i(\omega - \omega')t} = 2\pi\delta(\omega - \omega'), \tag{C.73}$$
which is an identity that will be useful later.

- The Fourier transform of \(\dot{x}(t)\) is \(i\omega\tilde{x}(\omega)\), and so differential equations can be Fourier transformed into algebraic equations.

- The Fourier transform of \(x^*(t)\) is \(\tilde{x}^*(-\omega)\).

- **Parseval’s theorem** states that
$$\int_{-\infty}^\infty dt |x(t)|^2 = \frac{1}{2\pi} \int_{-\infty}^\infty d\omega |\tilde{x}(\omega)|^2. \tag{C.74}$$

- The convolution \(h(t)\) of two functions \(f(t)\) and \(g(t)\) is defined by
$$h(t) = \int_{-\infty}^\infty dt' f(t - t') g(t'). \tag{C.75}$$
The **convolution theorem** states that the Fourier transform of \(h(t)\) is then given by the multiplication of the Fourier transforms of \(f(t)\) and \(g(t)\), i.e.,
$$\tilde{h}(\omega) = \tilde{f}(\omega)\tilde{g}(\omega). \tag{C.76}$$

- We now prove the **Wiener–Khinchin theorem** (mentioned in Section 33.6). Using the inverse Fourier transform, we can write the correlation function \(C_{xx}(t)\) as
$$C_{xx}(t) = \int_{-\infty}^\infty x^*(t')x(t' + t) dt' = \int_{-\infty}^\infty dt' \left(\frac{1}{2\pi} \int_{-\infty}^\infty d\omega' e^{i\omega' t'} \tilde{x}^*(-\omega')\right) \left(\frac{1}{2\pi} \int_{-\infty}^\infty d\omega e^{i\omega(t'+t)} \tilde{x}(\omega)\right) = \frac{1}{4\pi^2} \int_{-\infty}^\infty d\omega e^{i\omega t} \int_{-\infty}^\infty d\omega' \tilde{x}^*(-\omega')\tilde{x}(\omega) \int_{-\infty}^\infty dt' e^{i(\omega+\omega')t'} = \frac{1}{2\pi} \int_{-\infty}^\infty d\omega e^{i\omega t} \int_{-\infty}^\infty d\omega' \tilde{x}^*(-\omega')\tilde{x}(\omega)\delta(\omega + \omega') = \frac{1}{2\pi} \int_{-\infty}^\infty d\omega e^{i\omega t} \tilde{x}^*(\omega)\tilde{x}(\omega) = \frac{1}{2\pi} \int_{-\infty}^\infty d\omega e^{i\omega t} |\tilde{x}(\omega)|^2, \tag{C.77}$$
where use has been made of eqn C.73. This result is simply the inverse Fourier transform of \(|\tilde{x}(\omega)|^2\), the power spectrum of the function.

---

#### C.12 Solution of the diffusion equation

The diffusion equation
$$\frac{\partial n}{\partial t} = D \frac{\partial^2 n}{\partial x^2} \tag{C.78}$$
can be solved by Fourier transforming \(n(x, t)\) using
$$\tilde{n}(k, t) = \int_{-\infty}^\infty dx e^{-ikx} n(x, t), \tag{C.79}$$
so that
$$-ik\tilde{n}(k, t) = \int_{-\infty}^\infty dx e^{-ikx} \frac{\partial n(x, t)}{\partial x}. \tag{C.80}$$
Hence eqn C.78 becomes
$$\frac{\partial \tilde{n}(k, t)}{\partial t} = -Dk^2 \tilde{n}(k, t), \tag{C.81}$$
which is now a simple first-order differential equation whose solution is
$$\tilde{n}(k, t) = \tilde{n}(k, 0) e^{-Dk^2 t}. \tag{C.82}$$

Inverse Fourier transforming then yields
$$n(x, t) = \frac{1}{2\pi} \int_{-\infty}^\infty dk e^{ikx} e^{-Dk^2 t} \tilde{n}(k, 0). \tag{C.83}$$

In particular, if the initial distribution of \(n\) is given by
$$n(x, 0) = n_0 \delta(x), \tag{C.84}$$
then
$$\tilde{n}(k, 0) = n_0, \tag{C.85}$$
and hence
$$n(x, t) = \frac{n_0}{\sqrt{4\pi Dt}} e^{-x^2/(4Dt)}. \tag{C.86}$$

[Image: A graph of equation C.86 plotted for various values of t. At t=0, n(x,t) is a delta function at the origin. As t increases, n(x,t) becomes broader and the distribution spreads out.]
**Fig. C.6** Equation C.86 plotted for various values of \(t\). At \(t = 0\), \(n(x, t)\) is a delta function at the origin, i.e., \(n(x, 0) = n_0 \delta(x)\). As \(t\) increases, \(n(x, t)\) becomes broader and the distribution spreads out.

**Quick exercise**
Repeat this in three dimensions for the diffusion equation
$$\frac{\partial n}{\partial t} = D\nabla^2 n \tag{C.87}$$
and show that if \(n(0, t) = n_0 \delta(\mathbf{r})\) then
$$n(\mathbf{r}, t) = \frac{n_0}{\sqrt{4\pi Dt}} e^{-r^2/(4Dt)}. \tag{C.88}$$

---

#### C.13 Lagrange multipliers

[Image: A diagram illustrating the method of Lagrange multipliers. We wish to find the maximum of a function f subject to a constraint g=0. This occurs at a point P where one of the contours of f and the curve g=0 touch tangentially.]
**Fig. C.7** We wish to find the maximum of the function \(f\) subject to the constraint that \(g = 0\). This occurs at the point P at which one of the contours of \(f\) and the curve \(g = 0\) touch tangentially.

The method of Lagrange multipliers\(^6\) is used to find the extrema of a function of several variables subject to one or more constraints. Suppose we wish to maximize (or minimize) a function \(f(\mathbf{x})\) subject to the constraint \(g(\mathbf{x}) = 0\). Both \(f\) and \(g\) are functions of the \(N\) variables \(\mathbf{x} = (x_1, x_2, \ldots, x_N)\). The maximum (or minimum) will occur when one of the contours of \(f\) and the curve \(g = 0\) touch tangentially; let us call the set of points at which this occurs P (this is shown in Fig. C.7 for a two-dimensional case). Now \(\nabla f\) is a vector normal to the contours of \(f\) and \(\nabla g\) is a vector normal to the curve \(g = 0\), and these two vectors will be parallel to each other at P. Hence
$$\nabla[f + \lambda g] = 0, \tag{C.89}$$
where \(\lambda\) is a constant, called the **Lagrange multiplier**. Thus we have \(N\) equations to solve:
$$\frac{\partial F}{\partial x_k} = 0, \tag{C.90}$$
where \(F = f + \lambda g\) and \(k = 1, \ldots, N\). This allows us to find \(\lambda\) and hence identify the \((N - 2)\)-dimensional surface on which \(f\) is extremized subject to the constraint \(g = 0\).

If there are \(M\) constraints, so that for example \(g_i(\mathbf{x}) = 0\) where \(i = 1, \ldots, M\), then we solve eqn C.90 with
$$F = f + \sum_{i=1}^M \lambda_i g_i, \tag{C.91}$$
where \(\lambda_1, \ldots, \lambda_M\) are Lagrange multipliers.

> \(^6\)Joseph-Louis, Comte de Lagrange (1736–1813).

**Example C.2**
Find the ratio of the radius \(r\) to the height \(h\) of a cylinder, which maximizes its total surface area subject to the constraint that its volume is constant.

**Solution:**
The volume \(V = \pi r^2 h\) and area \(A = 2\pi rh + 2\pi r^2\), so we consider the function \(F\) given by
$$F = A + \lambda V, \tag{C.92}$$
and solve
$$\frac{\partial F}{\partial h} = 2\pi r + \lambda \pi r^2 = 0, \tag{C.93}$$
$$\frac{\partial F}{\partial r} = 2\pi h + 4\pi r + 2\lambda \pi r h = 0, \tag{C.94}$$
which yields \(\lambda = -2/r\) and hence \(h = 2r\).

---

## Appendix D: The electromagnetic spectrum

[Image: A diagram showing the electromagnetic spectrum. The energy of a photon is shown as a temperature T = E/k_B in K and as an energy E in eV. The corresponding frequency f is shown in Hz and in cm^{-1}. The cm^{-1} scale is marked with some common molecular transitions and excitations. The wavelength lambda is also shown. The diagram shows the regions of radio, microwave, infrared, optical, and ultraviolet radiation.]
**Fig. D.1** The electromagnetic spectrum. The energy of a photon is shown as a temperature \(T = E/k_B\) in K and as an energy \(E\) in eV. The corresponding frequency \(f\) is shown in Hz and, because the unit is often quoted in spectroscopy, in cm\(^{-1}\). The cm\(^{-1}\) scale is marked with some common molecular transitions and excitations (the typical ranges for molecular rotations and vibrations are shown, together with the C–H bending and stretching modes). The energy of typical \(\pi\) and \(\sigma\) bonds is also shown. The wavelength \(\lambda = c/f\) of the photon is shown (where \(c\) is the speed of light). The particular temperatures marked on the temperature scale are \(T_{\text{CMB}}\) (the temperature of the cosmic microwave background), the boiling points of liquid helium (\(^4\)He) and nitrogen (N\(_2\)), both at atmospheric pressure, and also the value of room temperature. Other abbreviations on this diagram are IR = infrared, UV = ultraviolet, R = red, G = green, V = violet. The letter H marks 13.6 eV, the magnitude of the energy of the 1s electron in hydrogen. The frequency axis also contains descriptions of the main regions of the electromagnetic spectrum: radio, microwave, infrared (both “near” and “far”), optical and UV.

---

## Appendix E: Some thermodynamical definitions

- **System** = whatever part of the Universe we select.
- **Open systems** can exchange particles with their surroundings.
- **Closed systems** cannot.
- An **isolated system** is not influenced from outside its boundaries.
- **Adiathermal** = without flow of heat. A system bounded by adiathermal walls is thermally isolated. Any work done on such a system produces adiathermal change.
- **Diathermal** walls allow flow of heat. Two systems separated by diathermal walls are said to be in thermal contact.
- **Adiabatic** = adiathermal and reversible (often used synonymously with adiathermal).
- Put a system in thermal contact with some new surroundings. Heat flows or work is done. Eventually no further change takes place: the system is said to be in a state of **thermal equilibrium**.
- A **quasistatic process** is one carried out so slowly that the system passes through a series of equilibrium states so is always in equilibrium. A process that is quasistatic and has no hysteresis is said to be **reversible**.
- **Isobaric** = at constant pressure.
- **Isochoric** = at constant volume.
- **Isenthalpic** = at constant enthalpy.
- **Isentropic** = at constant entropy.
- **Isothermal** = at constant temperature.

---

## Appendix F: Thermodynamic expansion formulae

**Table F.1** Expansion formulae for first-order partial derivatives of thermal variables. (After E. W. Dearden, *Eur. J. Phys.* **16** 76 (1995).)

| \((\partial G)\) | \(-1\) | \(-S/V\) | \(\kappa_S - \alpha V\) | \(\alpha_S - C_p/T\) | \(S(T\alpha - P\kappa)\) | \(S(T\alpha - 1)\) | \(S - P(\kappa_S - V\alpha)\) | \(-C_p + PV\alpha\) | \(-C_p\) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| \((\partial F)\) | \(-\kappa_P\) | \(-(S/V) - P\alpha\) | \(\kappa_S\) | \(\alpha_S - p\kappa C_V/T\) | \(S(T\alpha - P\kappa)\) | \(S(T\alpha - 1)\) | \(0\) | \(-P\kappa C_V\) | \(-P(\kappa C_V + V\alpha)\) |
| \((\partial H)\) | \(T\alpha - 1\) | \(C_p/V\) | \(-\kappa C_V - V\alpha\) | \(-C_p/T\) | \(P(\kappa C_V + V\alpha)\) | \(0\) | \(-C_p\) | | |
| \((\partial U)\) | \(T\alpha - p\kappa\) | \((C_p/V) - P\alpha\) | \(-\kappa C_V\) | \(-P\kappa C_V/T\) | \(0\) | | | | |
| \((\partial S)\) | \(\alpha\) | \(C_p/TV\) | \(-\kappa C_V/T\) | \(0\) | | | | | |
| \((\partial V)\) | \(\kappa\) | \(\alpha\) | \(0\) | | | | | | |
| \((\partial P)\) | \(-1/V\) | \(0\) | | | | | | | |

Table F.1 contains a listing of various partial derivatives, some of which have been derived in this book. To evaluate a partial differential, one has to take the ratio of two terms in this table using the equation
$$\left(\frac{\partial x}{\partial y}\right)_z \equiv \frac{(\partial x)_z}{(\partial y)_z}. \tag{F.1}$$
Note that \((\partial A)_B \equiv -(\partial B)_A\).

**Example F.1**
To evaluate the Joule–Kelvin coefficient:
$$\mu_{JK} = \left(\frac{\partial T}{\partial P}\right)_H = \frac{(\partial T)_H}{(\partial P)_H} = -\frac{(\partial H)_T}{(\partial H)_P} = \frac{V(T\alpha - 1)}{C_p}. \tag{F.2}$$

---

## Appendix G: Reduced mass

Consider two particles with masses \(m_1\) and \(m_2\) located at positions \(\mathbf{r}_1\) and \(\mathbf{r}_2\) and held together by a force \(\mathbf{F}(r)\) that depends only on the distance \(r = |\mathbf{r}| = |\mathbf{r}_1 - \mathbf{r}_2|\) (see Fig. G.1).

[Image: A diagram showing two particles with masses m1 and m2 at positions r1 and r2, exerting forces on one another.]
**Fig. G.1** The forces exerted by two particles on one another.

Thus we have
$$m_1\ddot{\mathbf{r}}_1 = \mathbf{F}(r), \tag{G.1}$$
$$m_2\ddot{\mathbf{r}}_2 = -\mathbf{F}(r), \tag{G.2}$$
and hence
$$\ddot{\mathbf{r}} = (m_1^{-1} + m_2^{-1}) \mathbf{F}(r), \tag{G.4}$$
which can be written
$$\mu\ddot{\mathbf{r}} = \mathbf{F}(r), \tag{G.5}$$
where \(\mu\) is the **reduced mass** given by
$$\frac{1}{\mu} = \frac{1}{m_1} + \frac{1}{m_2}, \tag{G.6}$$
or equivalently
$$\mu = \frac{m_1 m_2}{m_1 + m_2}. \tag{G.7}$$

---

## Appendix H: Glossary of main symbols

| Symbol | Meaning |
| :--- | :--- |
| \(\alpha\) | damping constant |
| \(\alpha_\lambda\) | spectral absorptivity |
| \(\beta\) | \(= 1/(k_B T)\) |
| \(\Gamma(n)\) | gamma function |
| \(\gamma\) | adiabatic index; surface tension |
| \(\delta\) | skin depth |
| \(\epsilon\) | Seebeck coefficient |
| \(\epsilon_0\) | permittivity of free space |
| \(\zeta(s)\) | Riemann zeta function |
| \(\eta\) | viscosity |
| \(\theta(x)\) | Heaviside step function |
| \(\kappa\) | thermal conductivity |
| \(\kappa_\nu\) | extinction coefficient |
| \(\Lambda\) | relativistic thermal wavelength |
| \(\lambda\) | mean free path; wavelength |
| \(\lambda_{\text{th}}\) | thermal wavelength |
| \(\mu\) | chemical potential |
| \(\mu_0\) | permeability of free space |
| \(\mu^\ominus\) | chemical potential at STP |
| \(\mu_J\) | Joule coefficient |
| \(\mu_{JK}\) | Joule–Kelvin coefficient |
| \(\nu\) | frequency |
| \(\Pi\) | momentum flux; Peltier coefficient; Osmotic pressure |
| \(\rho\) | density; resistivity |
| \(\rho_J\) | Jeans density |
| \(\Sigma\) | local entropy production |
| \(\sigma\) | standard deviation; collision cross-section; Stefan–Boltzmann constant |
| \(\sigma_p\) | Prandtl number |
| \(\tau\) | mean scattering time |
| \(\tau_{xy}\) | shear stress across \(xy\) plane |
| \(\Phi_G\) | grand potential |
| \(\Phi\) | flux |
| \(\chi\) | magnetic susceptibility |
| \(\chi(t - t')\) | response function |
| \(\chi_\nu\) | optical depth at frequency \(\nu\) |
| \(\psi(\mathbf{r})\) | wave function |
| \(\Omega\) | solid angle; potential energy; number of microstates with energy \(E\) |
| \(\omega\) | angular frequency |
| \(A\) | availability; area; albedo; Einstein coefficient |
| \(B\) | magnetic field; bulk modulus; Einstein coefficient |
| \(B_\lambda\) | radiance or surface brightness in a wavelength interval |
| \(B_\nu\) | radiance or surface brightness in a frequency interval |
| \(B_S\) | bulk modulus at constant entropy |
| \(B_T\) | bulk modulus at constant temperature |
| \(B(T)\) | virial coefficient as a function of \(T\) |
| \(C\) | heat capacity; number of chemically distinct constituents; capacitance |
| \(c\) | speed of light; specific heat capacity |
| \(D\) | coefficient of self-diffusion |
| \(E\) | electric field; energy; Fermi energy; electromotive field |
| \(e_\lambda\) | spectral emissive power |
| \(F\) | Helmholtz function; number of degrees of freedom |
| \(\mathcal{F}_\nu\) | spectral irradiance |
| \(f\) | frequency; speed distribution function; distribution function, Fermi function |
| \(G\) | gravitational constant; Gibbs function |
| \(g\) | gravitational acceleration on Earth’s surface; degeneracy; density of states |
| \(H\) | enthalpy; magnetic field strength |
| \(I\) | current; moment of inertia |
| \(I_\nu\) | spectral radiance |
| \(J\) | heat flux |
| \(J_\nu\) | source function |
| \(K\) | equilibrium constant |
| \(K_b\) | ebullioscopic constant |
| \(K_f\) | cryoscopic constant |
| \(k\) | wave vector |
| \(k_B\) | Boltzmann constant |
| \(k_F\) | Fermi wave vector |
| \(L\) | latent heat; luminosity |
| \(L_\text{edd}\) | Eddington luminosity |
| \(L_{ij}\) | kinetic coefficients |
| \(\text{Li}_n(z)\) | polylogarithm function |
| \(l_P\) | Planck length |
| \(M\) | magnetization; Mach number; mass |
| \(m\) | magnetic moment; mass of particle or system |
| \(N\) | number of particles |
| \(N_A\) | Avogadro number |
| \(n\) | number density (number per unit volume) |
| \(n_m\) | number of moles |
| \(n_Q\) | quantum concentration |
| \(P\) | number of phases present |
| \(P(x)\) | probability of \(x\) |
| \(\hat{P}_{12}\) | exchange operator |
| \(\mathcal{P}\) | Cauchy principal value |
| \(p\) | pressure |
| \(p^\ominus\) | standard pressure (1 atmosphere) |
| \(Q\) | heat |
| \(\mathbf{q}\) | phonon wave vector |
| \(R\) | gas constant; resistance |
| \(S\) | spin; entropy |
| \(T\) | temperature |
| \(T_B\) | Boyle temperature |
| \(T_b\) | temperature at boiling point |
| \(T_C\) | Curie temperature |
| \(T_c\) | critical temperature |
| \(T_F\) | Fermi temperature |
| \(t\) | time |
| \(U\) | internal energy |
| \(u\) | internal energy per unit volume |
| \(\tilde{u}\) | internal energy per unit mass |
| \(u_\lambda\) | spectral energy density |
| \(V\) | volume |
| \(v\) | speed of particle |
| \(\langle v \rangle\) | mean speed of particle |
| \(\langle v^2 \rangle\) | mean squared speed of particle |
| \(\sqrt{\langle v^2 \rangle}\) | root mean squared (rms) speed of particle |
| \(v_s\) | speed of sound |
| \(W\) | work |
| \(Z\) | partition function |
| \(Z_1\) | partition function for single-particle state |
| \(\mathcal{Z}\) | grand partition function |
| \(z\) | fugacity |
```