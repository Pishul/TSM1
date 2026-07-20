[file name]: Heat and thermodynamics by M. W. Zemansky, Richard H. Dittman
===== Page 1 =====

 SEVENTH EDITION  HEAT AND THERMODYNAMICS  MARK W. ZEMANSKY  RICHARD H. DITTMAN

===== Page 2 =====

1

===== Page 3 =====

1

===== Page 4 =====

 HEAT AND THERMODYNAMICS  An Intermediate Textbook  

Copyright ©1997, 1981, 1968, 1957, 1951, 1943, 1937 by The McGraw- Hill Companies, Inc. Copyright renewed 1979, 1971, 1965 by Mark W. Zemansky. All rights reserved. Printed in the United States of America. Except as permitted under the United States Copyright Act of 1976, no part of this publication may be reproduced or distributed in any form or by any means, or stored in a data base or retrieval system, without the prior written permission of the publisher.  

This book is printed on acid- free paper.  

1 2 3 4 5 6 7 8 9 0 FGR FGR 9 0 9 8 7 6  

ISBN 0- 07- 017059- 2  

This book was set in Times Roman by Keyword Publishing Services. The editors were Karen J. Allanson and John M. Morriss; the production supervisor was Kathryn Porzio. The cover was designed by Karen K. Quigley. Project supervision was done by Keyword Publishing Services. Quebecor Printing/Fairfield was printer and binder.  

Library of Congress Cataloging- in- Publication Data  

Zemansky, Mark Waldo (1900- 1981)  

Heat and thermodynamics: an intermediate textbook/Mark W. Zemansky, Richard H. Dittman.—7th ed. p. cm.—(International series in pure and applied physics) Includes bibliographical references and index. ISBN 0- 07- 017059- 2 1. Heat. 2. Thermodynamics. I. Dittman, Richard. II. Title. III. Series. QC254.2. Z45 1997 536—dc20 96- 28311  

http://www.mhcollege.com

===== Page 5 =====

 To Adele C. Zemansky and Maria M. Dittman

===== Page 6 =====

1

===== Page 7 =====

 MARK W. ZEMANSKY was born in New York City in 1900, graduated from City College of New York in 1921, and received his Ph.D. degree from Columbia University in 1927. In 1925 he joined the faculty of City College, where he remained until his retirement in 1967, except for further research at Princeton University from 1928 to 1930 and then at the Kaiser Wilhelm Institute in Berlin from 1930 until 1931. Zemansky wrote the first edition of Heat and Thermodynamics in 1937. In 1947 Francis W. Sears and Zemansky published the first edition of College Physics and their University Physics in 1949. During his long association with the American Association of Physics Teachers he was associate editor of the American Journal of Physics from 1941 to 1947, president of AAPT in 1951, and executive secretary from 1967 to 1970. He died in 1981.  

RICHARD H. DITTMAN was born in Sacramento, California in 1937, graduated from Santa Clara University in 1959, and received his Ph.D. degree from Notre Dame University in 1965. Following a year's research at the Fritz Haber Institute in Berlin, he joined the faculty of the University of Wisconsin in Milwaukee, where he remained. In collaboration with Glenn M. Schmieg he wrote Physics in Everyday Life in 1979. Dittman received two distinguished faculty teaching awards, one in 1971 and the other in 1989. He also served as chair of the Department of Physics and associate dean of the College of Letters and Science.

===== Page 8 =====

1

===== Page 9 =====

1 Temperature and the Zeroth Law of Thermodynamics 3 1.1 Macroscopic Point of View 3 1.2 Microscopic Point of View 4 1.3 Macroscopic vs. Microscopic Points of View 5 1.4 Scope of Thermodynamics 6 1.5 Thermal Equilibrium and the Zeroth Law 7 1.6 Concept of Temperature 10 1.7 Thermometers and Measurement of Temperature 12 1.8 Comparison of Thermometers 15 1.9 Gas Thermometer 16 1.10 Ideal- Gas Temperature 18 1.11 Celsius Temperature Scale 20 1.12 Platinum Resistance Thermometry 21 1.13 Radiation Thermometry 22 1.14 Vapor Pressure Thermometry 23 1.15 Thermocouple 23 1.16 International Temperature Scale of 1990 (ITS- 90) 24 1.17 Rankine and Fahrenheit Temperature Scales 26  

## 2 Simple Thermodynamic Systems 29  

2.1 Thermodynamic Equilibrium 29 2.2 Equation of State 31 2.3 Hydrostatic Systems 32 2.4 Mathematical Theorems 35 2.5 Stretched Wire 38 2.6 Surfaces 40 2.7 Electrochemical Cell 41 2.8 Dielectric Slab 43 2.9 Paramagnetic Rod 44 2.10 Intensive and Extensive Coordinates 46

===== Page 10 =====

3 Work 49 3.1 Work 49 3.2 Quasi- Static Process 50 3.3 Work in Changing the Volume of a Hydrostatic System 52 3.4 PV Diagram 54 3.5 Hydrostatic Work Depends on the Path 55 3.6 Calculation of \(\int P d V\) for Quasi- Static Processes 57 3.7 Work in Changing the Length of a Wire 59 3.8 Work in Changing the Area of a Surface Film 59 3.9 Work in Moving Charge with an Electrochemical Cell 60 3.10 Work in Changing the Total Polarization of a Dielectric Solid 62 3.11 Work in Changing the Total Magnetization of a Paramagnetic Solid 63 3.12 Generalized Work 66 3.13 Composite Systems 66  

4 Heat and the First Law of Thermodynamics 72 4.1 Work and Heat 72 4.2 Adiabatic Work 74 4.3 Internal- Energy Function 77 4.4 Mathematical Formulation of the First Law 78 4.5 Concept of Heat 80 4.6 Differential Form of the First Law 81 4.7 Heat Capacity and its Measurement 83 4.8 Specific Heat of Water; the Calorie 87 4.9 Equations for a Hydrostatic System 88 4.10 Quasi- Static Flow of Heat; Heat Reservoir 89 4.11 Heat Conduction 90 4.12 Thermal Conductivity and its Measurement 91 4.13 Heat Convection 93 4.14 Thermal Radiation; Blackbody 94 4.15 Kirchhoff's Law; Radiated Heat 97 4.16 Stefan- Boltzmann Law 99  

5 Ideal Gas 106 5.1 Equation of State of a Gas 106 5.2 Internal Energy of a Real Gas 108 5.3 Ideal Gas 112 5.4 Experimental Determination of Heat Capacities 114 5.5 Quasi- Static Adiabatic Process 116 5.6 Rüchhardt's Method of Measuring \(\gamma\) 118 5.7 Velocity of a Longitudinal Wave 121

===== Page 11 =====

5.8 The Microscopic Point of View 126 5.9 Kinetic Theory of the Ideal Gas 127  

## 6 The Second Law of Thermodynamics 140  

6.1 Conversion of Work into Heat and Vice Versa 140 6.2 The Gasoline Engine 142 6.3 The Diesel Engine 146 6.4 The Steam Engine 148 6.5 The Stirling Engine 150 6.6 Heat Engine; Kelvin- Planck Statement of the Second Law 153 6.7 Refrigerator; Clausius' Statement of the Second Law 154 6.8 Equivalence of the Kelvin- Planck and Clausius Statements 156 6.9 Reversibility and Irreversibility 158 6.10 External Mechanical Irreversibility 159 6.11 Internal Mechanical Irreversibility 161 6.12 External and Internal Thermal Irreversibility 161 6.13 Chemical Irreversibility 162 6.14 Conditions for Reversibility 163  

## 7 The Carnot Cycle and the Thermodynamic Temperature Scale 168  

7.1 Carnot Cycle 168 7.2 Examples of Carnot Cycles 170 7.3 Carnot Refrigerator 173 7.4 Carnot's Theorem and Corollary 174 7.5 The Thermodynamic Temperature Scale 176 7.6 Absolute Zero and Carnot Efficiency 180 7.7 Equality of Ideal- Gas and Thermodynamic Temperatures 180  

## 8 Entropy 186  

8.1 Reversible Part of the Second Law 186 8.2 Entropy 189 8.3 Principle of Carathéodory 192 8.4 Entropy of the Ideal Gas 194 8.5 TS Diagram 196 8.6 Entropy and Reversibility 198 8.7 Entropy and Irreversibility 199 8.8 Irreversible Part of the Second Law 204 8.9 Heat and Entropy in Irreversible Processes 206 8.10 Entropy and Nonequilibrium States 208

===== Page 12 =====

8.11 Principle of Increase of Entropy 210 8.12 Application of the Entropy Principle 213 8.13 Entropy and Disorder 214 8.14 Exact Differentials 217  

## 9 Pure Substances 222  

9.1 PV Diagram for a Pure Substance 222  9.2 PT Diagram for a Pure Substance; Phase Diagram 226  9.3 PVT Surface 228  9.4 Equations of State 232  9.5 Molar Heat Capacity at Constant Pressure 233  9.6 Volume Expansivity; Cubic Expansion Coefficient 236  9.7 Compressibility 239  9.8 Molar Heat Capacity at Constant Volume 243  9.9 TS Diagram for a Pure Substance 244  

## 10 Mathematical Methods 249  

10 Mathematical Methods 249  10.1 Characteristic Functions 249  10.2 Enthalpy 252  10.3 Helmholtz and Gibbs Functions 258  10.4 Two Mathematical Theorems 260  10.5 Maxwell's Relations 261  10.6 TdS Equations 263  10.7 Internal- Energy Equations 267  10.8 Heat- Capacity Equations 269  

## 11 Open Systems 277  

11.1 Joule- Thomson Expansion 277  11.2 Liquefaction of Gases by the Joule- Thomson Expansion 280  11.3 First- Order Phase Transitions; Clausius- Clapeyron Equation 286  11.4 Clausius- Clapeyron Equation and Phase Diagrams 289  11.5 Clausius- Clapeyron Equation and the Carnot Engine 292  11.6 Chemical Potential 293  11.7 Open Hydrostatic Systems in Thermodynamic Equilibrium 297

===== Page 13 =====

12 Statistical Mechanics 307 12.1 Fundamental Principles 307 12.2 Equilibrium Distribution 311 12.3 Significance of Lagrangian Multipliers \(\lambda\) and \(\beta\) 314 12.4 Partition Function for Canonical Ensemble 317 12.5 Partition Function of an Ideal Monatomic Gas 319 12.6 Equipartition of Energy 322 12.7 Distribution of Speeds in an Ideal Monatomic Gas 324 12.8 Statistical Interpretation of Work and Heat 328 12.9 Entropy and Information 330  

## 13 Thermal Properties of Solids  

13 Thermal Properties of Solids 337 13.1 Statistical Mechanics of a Nonmetallic Crystal 337 13.2 Frequency Spectrum of Crystals 342 13.3 Thermal Properties of Nonmetals 345 13.4 Thermal Properties of Metals 348  

## 14 Critical Phenomena; Higher-Order Phase Transitions 359  

14 Critical Phenomena; Higher- Order Phase Transitions 359 14.1 Critical State 359 14.2 Critical- Point Exponents of a Hydrostatic System 363 14.3 Critical- Point Exponents of a Magnetic System 368 14.4 Higher- Order Phase Transitions 372 14.5 Lambda Transitions in \(^4\mathrm{He}\) 374 14.6 Liquid and Solid Helium 378  

## 15 Chemical Equilibrium  

15 Chemical Equilibrium 386 15.1 Dalton's Law 386 15.2 Semipermeable Membrane 387 15.3 Gibbs' Theorem 388 15.4 Entropy of a Mixture of Inert Ideal Gases 390 15.5 Gibbs Function of a Mixture of Inert Ideal Gases 392 15.6 Chemical Equilibrium 393 15.7 Thermodynamic Description of Nonequilibrium States 395 15.8 Conditions for Chemical Equilibrium 397 15.9 Condition for Mechanical Stability 398 15.10 Thermodynamic Equations for a Phase 400 15.11 Chemical Potentials 403 15.12 Degree of Reaction 404 15.13 Equation of Reaction Equilibrium 407

===== Page 14 =====

16 Ideal- Gas Reactions 413 16.1 Law of Mass Action 413 16.2 Experimental Determination of Equilibrium Constants 414 16.3 Heat of Reaction 417 16.4 Nernst's Equation 420 16.5 Affinity 423 16.6 Displacement of Equilibrium 426 16.7 Heat Capacity of Reacting Gases in Equilibrium 428  

## 17 Heterogeneous Systems  

17 Heterogeneous Systems 433 17.1 Thermodynamic Equations for a Heterogeneous System 433 17.2 Phase Rule without Chemical Reaction 435 17.3 Simple Applications of the Phase Rule 439 17.4 Phase Rule with Chemical Reaction 443 17.5 Determination of the Number of Components 447 17.6 Displacement of Equilibrium 450  

## Appendices  

A Physical Constants 459 B Method of Lagrangian Multipliers 460 C Evaluation of the Integral \(\int_{0}^{\infty} e^{- ax^{2}} dx\) 462 D Riemann Zeta Functions 464 E Thermodynamic Definitions and Formulas 466  

Bibliography 471 Answers to Selected Problems 473 Index 477

===== Page 15 =====

 Mark Zemansky wrote the first five editions of Heat and Thermodynamics and we collaborated on the sixth edition. In this edition, Zemansky's pedagogical philosophy and style were my guide for making revisions. True to his tradition, the primary emphasis is placed on the thermodynamic (macroscopic) study of temperature, energy, and entropy, while recognizing that equations of state, temperature variations of specific heats, and valuable insight come from the statistical mechanical (microscopic) approach. Methods of measurement are explained throughout the book and actual data are given in graphs and tables. Mathematical theorems beyond elementary partial differentiation are derived and explained at the places where they are needed.  

The sequence of topics in this edition is identical to the last edition and generally follows all previous editions, but changes were made to keep the book up to date or to assist the student. Listed below are the significant additions or changes:  

- replacement of the symbol \(\theta\) for ideal-gas temperatures by the symbol \(T\) for absolute temperatures in the first chapter, before the two quantities are proven equal using the second law;- inclusion of the International Temperature Scale of 1990, which defined the practical temperature scale down to \(0.65 \mathrm{~K}\) and eliminated the thermocouple as a primary standard thermometer;- determination of the universal gas constant \(R\) from speed of sound measurements; this became the new standard in 1986 and eliminated the method based on the ideal-gas law;- expression of the thermal efficiencies of internal-combustion engines in terms of temperature rather than compression and expansion ratios, thus providing a better preparation for the Carnot engine;- replacement of the axiomatic presentation of the second law of thermodynamics, according to Carathéodory, with the method of Carnot, Clausius, Kelvin, and Planck using cycles in a reversible heat engine;- extension of the phase diagram for \(\mathrm{H}_{2} \mathrm{O}\) to include two very-high-pressure polymorphs of ice;- use of Legendre transformations to organize the thermodynamic potentials for closed systems — internal energy, enthalpy, Helmholtz function, and Gibbs function;- introduction of four thermodynamic potentials for open systems — grand function, Guggenheim function, Hill function, and Ray function — which greatly assist in the transition from thermodynamics to statistical mechanics.  

Data and references were updated when appropriate.

===== Page 16 =====

 No book can be written without the advice of others. It is a great pleasure to acknowledge the assistance of Henry J. Graben, David L. Hogenboom, Charles Kaufman, J. M. Marcano, Mark McKenna, Richmond B. McQuistan, Sue Nicholls (of Keyword Publishing Services), Dorn W. Peterson, George Rainey, John Ray, James E. Rutledge, Glenn Schmieg, Dale Snider, Leslie Spanel, and Anna Topal.  

Richard H. Dittman

===== Page 17 =====

1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 1 1 1 1 7 1 1 1 1 1 1 1 1 1 8 1 1 1 1 1 1 1 1 1 9 1 1 1 1 1 1 1 1 1 10 1 1 1 1 1 1 1 1 1 11 1 1 1 1 1 1 1 1 1 12 1 1 1 1 1 1 1 1 1 13 1 1 1 1 1 1 1 1 1 14 1 1 1 1 1 1 1 1 1 15 1 1 1 1 1 1 1 1 1 16 1 1 1 1 1 1 1 1 1 17 1 1 1 1 1 1 1 1 1 18 1 1 1 1 1 1 1 1 1 19 1 1 1 1 1 1 1 1 1 20 1 1 1 1 1 1 1 1 1 21 1 1 1 1 1 1 1 1 1 22 1 1 1 1 1 1 1 1 1 23 1 1 1 1 1 1 1 1 1 24 1 1 1 1 1 1 1 1 1 25 1 1 1 1 1 1 1 1 1 26 1 1 1 1 1 1 1 1 1 27 1 1 1 1 1 1 1 1 1 28 1 1 1 1 1 1 1 1 1 29 1 1 1 1 1 1 1 1 1 30 1 1 1 1 1 1 1 1 1 31 1 1 1 1 1 1 1 1 1 32 1 1 1 1 1 1 1 1 1 33 1 1 1 1 1 1 1 1 1 34 1 1 1 1 1 1 1 1 1 35 1 1 1 1 1 1 1 1 1 36 1 1 1 1 1 1 1 1 1 37 1 1 1 1 1 1 1 1 1 38 1 1 1 1 1 1 1 1 1 39 1 1 1 1 1 1 1 1 1 40 1 1 1 1 1 1 1 1 1 41 1 1 1 1 1 1 1 1 1 42 1 1 1 1 1 1 1 1 1 43 1 1 1 1 1 1 1 1 1 44 1 1 1 1 1 1 1 1 1 45 1 1 1 1 1 1 1 1 1 46 1 1 1 1 1 1 1 1 1 47 1 1 1 1 1 1 1 1 1 48 1 1 1 1 1 1 1 1 1 49 1 1 1 1 1 1 1 1 1 50 1 1 1 1 1 1 1 1 1 51 1 1 1 1 1 1 1 1 1 52 1 1 1 1 1 1 1 1 1 53 1 1 1 1 1 1 1 1 1 54 1 1 1 1 1 1 1 1 1 55 1 1 1 1 1 1 1 1 1 56 1 1 1 1 1 1 1 1 1 57 1 1 1 1 1 1 1 1 1 58 1 1 1 1 1 1 1 1 1 59 1 1 1 1 1 1 1 1 1 60 1 1 1 1 1 1 1 1 1 61 1 1 1 1 1 1 1 1 1 62 1 1 1 1 1 1 1 1 1 63 1 1 1 1 1 1 1 1 1 64 1 1 1 1 1 1 1 1 1 65 1 1 1 1 1 1 1 1 1 66 1 1 1 1 1 1 1 1 1 67 1 1 1 1 1 1 1 1 1 68 1 1 1 1 1 1 1 1 1 69 1 1 1 1 1 1 1 1 1 70 1 1 1 1 1 1 1 1 1 71 1 1 1 1 1 1 1 1 1 72 1 1 1 1 1 1 1 1 1 73 1 1 1 1 1 1 1 1 1 74 1 1 1 1 1 1 1 1 1 75 1 1 1 1 1 1 1 1 1 76 1 1 1 1 1 1 1 1 1 77 1 1 1 1 1 1 1 1 1 78 1 1 1 1 1 1 1 1 1 79 1 1 1 1 1 1 1 1 1 80 1 1 1 1 1 1 1 1 1 81 1 1 1 1 1 1 1 1 1 82 1 1 1 1 1 1 1 1 1 83 1 1 1 1 1 1 1 1 1 84 1 1 1 1 1 1 1 1 1 85 1 1 1 1 1 1 1 1 1 86 1 1 1 1 1 1 1 1 1 87 1 1 1 1 1 1 1 1 1 88 1 1 1 1 1 1 1 1 1 89 1 1 1 1 1 1 1 1 1 90 1 1 1 1 1 1 1 1 1 91 1 1 1 1 1 1 1 1 1 92 1 1 1 1 1 1 1 1 1 93 1 1 1 1 1 1 1 1 1 94 1 1 1 1 1 1 1 1 1 95 1 1 1 1 1 1 1 1 1 96 1 1 1 1 1 1 1 1 1 97 1 1 1 1 1 1 1 1 1 98 1 1 1 1 1 1 1 1 1 99 1 1 1 1 1 1 1 1 1 100 1 1 1 1 1 1 1 1 1 101 1 1 1 1 1 1 1 1 1 102 1 1 1 1 1 1 1 1 1 103 1 1 1 1 1 1 1 1 1 104 1 1 1 1 1 1 1 1 1 105 1 1 1 1 1 1 1 1 1 106 1 1 1 1 1 1 1 1 1 107 1 1 1 1 1 1 1 1 1 108 1 1 1 1 1 1 1 1 1 109 1 1 1 1 1 1 1 1 1 110 1 1 1 1 1 1 1 1 1 111 1 1 1 1 1 1 1 1 1 112 1 1 1 1 1 1 1 1 1 113 1 1 1 1 1 1 1 1 1 114 1 1 1 1 1 1 1 1 1 115 1 1 1 1 1 1 1 1 1 116 1 1 1 1 1 1 1 1 1 117 1 1 1 1 1 1 1 1 1 118 1 1 1 1 1 1 1 1 1 119 1 1 1 1 1 1 1 1 1 120 1 1 1 1 1 1 1 1 1 121 1 1 1 1 1 1 1 1 1 122 1 1 1 1 1 1 1 1 1 123 1 1 1 1 1 1 1 1 1 124 1 1 1 1 1 1 1 1 1 125 1 1 1 1 1 1 1 1 1 126 1 1 1 1 1 1 1 1 1 127 1 1 1 1 1 1 1 1 1 128 1 1 1 1 1 1 1 1 1 129 1 1 1 1 1 1 1 1 1 130 1 1 1 1 1 1 1 1 1 131 1 1 1 1 1 1 1 1 1 132 1 1 1 1 1 1 1 1 1 133 1 1 1 1 1 1 1 1 1 134 1 1 1 1 1 1 1 1 1 135 1 1 1 1 1 1 1 1 1 136 1 1 1 1 1 1 1 1 1 137 1 1 1 1 1 1 1 1 1 138 1 1 1 1 1 1 1 1 1 139 1 1 1 1 1 1 1 1 1 140 1 1 1 1 1 1 1 1 1 141 1 1 1 1 1 1 1 1 1 142 1 1 1 1 1 1 1 1 1 143 1 1 1 1 1 1 1 1 1 144 1 1 1 1 1 1 1 1 1 145 1 1 1 1 1 1 1 1 1 146 1 1 1 1 1 1 1 1 1 147 1 1 1 1 1 1 1 1 1 148 1 1 1 1 1 1 1 1 1 149 1 1 1 1 1 1 1 1 1 150 1 1 1 1 1 1 1 1 1 151 1 1 1 1 1 1 1 1 1 152 1 1 1 1 1 1 1 1 1 153 1 1 1 1 1 1 1 1 1 154 1 1 1 1 1 1 1 1 1 

===== Page 18 =====

1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 3 1 1 1 1 1 1 1 1 1 1 4 1 1 1 1 1 1 1 1 1 5 1 1 1 1 1 1 1 1 1 6 1 1 1 1 1 1 1 1 1 7 1 1 1 1 1 1 1 1 1 8 1 1 1 1 1 1 1 1 1 9 1 1 1 1 1 1 1 1 1 10 1 1 1 1 1 1 1 1 1 11 1 1 1 1 1 1 1 1 1 12 1 1 1 1 1 1 1 1 1 13 1 1 1 1 1 1 1 1 1 14 1 1 1 1 1 1 1 1 1 15 1 1 1 1 1 1 1 1 1 16 1 1 1 1 1 1 1 1 1 17 1 1 1 1 1 1 1 1 1 18 1 1 1 1 1 1 1 1 1 19 1 1 1 1 1 1 1 1 1 20 1 1 1 1 1 1 1 1 1 21 1 1 1 1 1 1 1 1 1 22 1 1 1 1 1 1 1 1 1 23 1 1 1 1 1 1 1 1 1 24 1 1 1 1 1 1 1 1 1 25 1 1 1 1 1 1 1 1 1 26 1 1 1 1 1 1 1 1 1 27 1 1 1 1 1 1 1 1 1 28 1 1 1 1 1 1 1 1 1 29 1 1 1 1 1 1 1 1 1 30 1 1 1 1 1 1 1 1 1 31 1 1 1 1 1 1 1 1 1 32 1 1 1 1 1 1 1 1 1 33 1 1 1 1 1 1 1 1 1 34 1 1 1 1 1 1 1 1 1 35 1 1 1 1 1 1 1 1 1 36 1 1 1 1 1 1 1 1 1 37 1 1 1 1 1 1 1 1 1 38 1 1 1 1 1 1 1 1 1 39 1 1 1 1 1 1 1 1 1 40 1 1 1 1 1 1 1 1 1 41 1 1 1 1 1 1 1 1 1 42 1 1 1 1 1 1 1 1 1 43 1 1 1 1 1 1 1 1 1 44 1 1 1 1 1 1 1 1 1 45 1 1 1 1 1 1 1 1 1 46 1 1 1 1 1 1 1 1 1 47 1 1 1 1 1 1 1 1 1 48 1 1 1 1 1 1 1 1 1 49 1 1 1 1 1 1 1 1 1 50 1 1 1 1 1 1 1 1 1 51 1 1 1 1 1 1 1 1 1 52 1 1 1 1 1 1 1 1 1 53 1 1 1 1 1 1 1 1 1 54 1 1 1 1 1 1 1 1 1 55 1 1 1 1 1 1 1 1 1 56 1 1 1 1 1 1 1 1 1 57 1 1 1 1 1 1 1 1 1 58 1 1 1 1 1 1 1 1 1 59 1 1 1 1 1 1 1 1 1 60 1 1 1 1 1 1 1 1 1 61 1 1 1 1 1 1 1 1 1 62 1 1 1 1 1 1 1 1 1 63 1 1 1 1 1 1 1 1 1 64 1 1 1 1 1 1 1 1 1 65 1 1 1 1 1 1 1 1 1 
===== Page 23 =====

 FUNDAMENTAL CONCEPTS

===== Page 24 =====

1

===== Page 25 =====

1.1 MACROSCOPIC POINT OF VIEW  

The study of any special branch of natural science starts with a separation of a restricted region of space or a finite portion of matter from its surroundings by means of a closed surface called the boundary. The region within the arbitrary boundary and on which the attention is focused is called the system, and everything outside the system that has a direct bearing on the system's behavior is known as the surroundings, which could be another system. If no matter crosses the boundary, then the system is closed; but if there is an exchange of matter between system and surroundings, then the system is open.  

When a system has been chosen, the next step is to describe it in terms of quantities related to the behavior of the system or its interactions with the surroundings, or both. There are, in general, two points of view that may be adopted: the macroscopic point of view and the microscopic point of view. The macroscopic point of view considers variables or characteristics of a system at approximately the human scale, or larger; whereas the microscopic point of view considers variables or characteristics of a system at approximately the molecular scale, or smaller.  

Let us take as a system the contents in a cylinder of an automobile engine. A chemical analysis would show a mixture of hydrocarbons and air before being ignited, and after the mixture has been ignited there would be combustion products describable in terms of new chemical compounds. A statement of the amounts of these chemicals describes both the mass and the composition of the system. At any moment, the system can be described further by specifying the volume, which varies as the piston moves in the cylinder. The volume can be easily measured and, in the laboratory, is recorded automatically by means of a device coupled to the piston. Another quantity that is indispen

===== Page 26 =====

4 PART I: Fundamental Concepts  

sable in the description of our system is the pressure of the gases in the cylinder. After ignition of the mixture, the pressure is large; after the expulsion of the combustion products, the pressure is small. In the laboratory, a pressure gauge may be used to measure and record the changes of pressure as the engine operates. Finally, there is one more quantity without which we should have no adequate description of the operation of the engine. This quantity is the temperature, and, as we shall see, in many instances it can be measured just as simply as the other quantities.  

We have described the contents in a cylinder of an automobile engine by specifying the quantities of mass, composition, volume, pressure, and temperature. These quantities refer to the large- scale characteristics, or aggregate properties, of the system and provide a macroscopic description. The quantities are, therefore, called macroscopic coordinates. For a system other than a gas, such as a paramagnetic salt, the different quantities must be specified to provide a macroscopic description of the system; but macroscopic coordinates, in general, have the following properties in common:  

1. They involve no special assumptions concerning the structure of matter, fields, or radiation. 
2. They are few in number needed to describe the system. 
3. They are fundamental, as suggested more or less directly by our sensory perceptions. 
4. They can, in general, be directly measured.  

In short, a macroscopic description of a system involves the specification of a few fundamental measurable properties of a system. Thermodynamics, then, is the branch of natural science that deals with the macroscopic properties or characteristics of nature and always includes the macroscopic coordinate of temperature for every system. The presence of temperature distinguishes thermodynamics from other macroscopic branches of science, such as geometrical optics, mechanics, or electricity and magnetism.  

### 1.2 MICROSCOPIC POINT OF VIEW  

The microscopic point of view is the result of the tremendous progress of molecular, atomic, and nuclear science during the past hundred years. From this point of view, a system is considered to consist of an enormous number \(N\) of particles, each of which is capable of existing in a set of states whose energies are \(\epsilon_{1}, \epsilon_{2}, \ldots\) . The particles are assumed to interact with one another by means of collisions or by forces caused by fields. The system of particles may be imagined to be isolated or, in some cases, may be considered to be embedded in a set of similar systems, or ensemble of systems. The mathematics of probability is applied, and the equilibrium state of the system is assumed to be the state of highest probability. The fundamental problem is to find the

===== Page 27 =====

1: Temperature and the Zeroth Law of Thermodynamics 5  

number of particles in each of the microscopic energy states (known as the populations of the states) when equilibrium is reached. Statistical mechanics, then, is the branch of natural science that deals with the microscopic characteristics of nature.  

Since statistical mechanics will be treated at some length in Chap. 12, it is not necessary to pursue the matter further at this point. It is evident, however, that a microscopic description of a system involves the following properties:  

1. Assumptions are made concerning the structure of matter, fields, or radiation. 
2. Many quantities must be specified to describe the system. 
3. These quantities specified are not usually suggested by our sensory perceptions, but rather by our mathematical models. 
4. They cannot be directly measured, but must be calculated.  

In short, a microscopic description of a system involves various assumptions about the internal structure of the system and then calculations of system- wide characteristics.  

### 1.3 MACROSCOPIC VS. MICROSCOPIC POINTS OF VIEW  

Although it might seem that the two points of view are hopelessly different and incompatible, both points of view, applied to the same system, must lead to the same conclusion. The two points of view are reconciled because the few directly measurable properties whose specification constitutes the macroscopic description are really averages, over a period of time, of a large number of microscopic characteristics. For example, the macroscopic quantity, pressure, is the average rate of change of linear momentum due to the large number of molecular collisions made on a unit of area. Pressure, however, is a property that is perceived by our senses. We feel the effects of pressure. Pressure was experienced, measured, and used long before there was reason to believe in the existence of molecular impacts. If molecular theory is changed, for example, by incorporating the results of chaos, the concept of pressure will still remain and be understood by all normal human beings. The few measurable macroscopic properties are as sure as our senses. They will remain unchanged as long as our senses remain the same and are not deceived. Herein lies an important distinction between the macroscopic and microscopic points of view. The microscopic point of view, however, goes much further than our senses and many direct experiments. It assumes the structure of microscopic particles, their motion, their energy states, their interactions, etc., and then calculates measurable quantities. The microscopic point of view has changed several times, and we can never be sure that the assumptions are justified until we have compared some deduction made on the basis of these assumptions with a similar deduction based on the experimentally proven macroscopic

===== Page 28 =====

6 PART I: Fundamental Concepts  

point of view. In other words, when we seek to understand the physical reality of a result of a microscopic calculation, we look to the macroscopic point of view for guidance.  

Throughout its history, the study of thermodynamics has always looked for general laws, relationships, and procedures for understanding macroscopic temperature- dependent phenomena. Because it makes no assumptions about the microscopic structure of matter, thermodynamics has not been disproved as the various specific microscopic classical and quantum models of matter have been incorporated into statistical mechanics.  

### 1.4 SCOPE OF THERMODYNAMICS  

It has been emphasized that a description of the large- scale characteristics of a system by means of a few of its measurable properties, suggested more or less directly by our sensory perceptions, constitutes a macroscopic description. Such descriptions are the historic starting point of all investigations in all branches of natural science. For example, in dealing with the mechanics of a rigid body, we adopt the macroscopic point of view in that only the external aspects of the rigid body are considered. The position of its center of mass is specified with reference to coordinate axes at a particular time. Position and time and a combination of both, such as velocity, constitute some of the macroscopic quantities used in classical mechanics and are called mechanical coordinates. The mechanical coordinates serve to determine the potential and the kinetic energy of the rigid body with reference to the coordinate axes, namely, the kinetic and the potential energy of the body as a whole. These two types of energy constitute the external, or mechanical, energy of the rigid body. It is the purpose of mechanics to find such relations between the position coordinates and the time as are consistent with Newton's laws of motion.  

In thermodynamics, however, the attention is directed to the interior of a system. A macroscopic point of view is adopted, and emphasis is placed on those macroscopic quantities which have a bearing on the internal state of a system. It is the function of experiment to determine the quantities that are appropriate for a description of such an internal state. Macroscopic quantities, including temperature, having a bearing on the internal state of a system are called thermodynamic coordinates. Such coordinates serve to determine the internal energy of a system. It is the purpose of thermodynamics to find, among the thermodynamic coordinates, general relations that are consistent with the fundamental laws of thermodynamics.  

A system that may be described in terms of thermodynamic coordinates is called a thermodynamic system. In engineering, the important thermodynamic systems are a gas, such as air; a vapor, such as steam; a mixture, such as gasoline vapor and air; and a vapor in contact with its liquid, such as liquid and vaporized freon. Chemical thermodynamics deals with these systems and, in addition, with reactions, surface films, and electric cells. Physical thermo

===== Page 29 =====

1.5 THERMAL EQUILIBRIUM AND THE ZEROTH LAW  

We have seen that a macroscopic description of a gaseous mixture may be given by specifying such quantities as the composition, the mass, the pressure, and the volume. The last quantity specified in Sec. 1.1 was temperature, for which you have an intuitive understanding and some familiarity. This section begins the analytic development of the quantity, temperature. Experiment shows that, for a given composition and for a constant mass and temperature, many different values of pressure and volume are possible for a gas. If the pressure is kept constant, the volume may vary over a wide range of values, and vice versa. In other words, the pressure and the volume are independent coordinates but are related in a simple equation, namely, Boyle's law.  

More recently, experiment has shown that, for a wire of constant mass, the tension and the length are independent coordinates, whereas, in the case of a surface film, the surface tension and the area may be varied independently. Some systems that, at first sight, seem quite complicated, such as an electric cell with two different electrodes and an electrolyte, may still be described with the aid of only two independent coordinates. On the other hand, some thermodynamic systems composed of a number of homogeneous parts require the specification of two independent coordinates for each homogeneous part. Details of various thermodynamic systems and their thermodynamic coordinates will be given in Chap. 2. For the present, to simplify our discussion, we shall deal only with systems of constant mass and composition, each requiring only one pair of independent coordinates for its description. This involves no essential loss of generality and results in a considerable saving of words. In referring to any unspecified system, we shall use the symbols \(X\) and \(Y\) for the pair of independent coordinates, where the symbol \(X\) refers to a generalized force (for instance, the pressure of a gas) and \(Y\) refers to a generalized displacement (for instance, the volume of a gas).  

A state of a system in which the coordinates \(X\) and \(Y\) have definite values that remain constant so long as the external conditions are unchanged is called an equilibrium state. Experiment shows that the existence of an equilibrium state in one system depends on the proximity of other systems and on the nature of the boundary or wall separating the different systems. Walls are said to be either adiabatic or diathermic in ideal cases. If a wall is adiabatic [see Fig. 1- 1(a)], an equilibrium state for system \(A\) may coexist with any equilibrium state of system \(B\) for all attainable values of the four quantities, \(X\) , \(Y\) and \(X^{\prime}\) , \(Y^{\prime}\) — provided only that the wall is able to withstand the stress associated with the difference between the two sets of coordinates. Thick layers of wood, concrete, asbestos, felt, or polystyrene, as well as dewars, are, in this order, increasingly better experimental approximations to ideal adiabatic walls.

===== Page 30 =====

8 PART I: Fundamental Concepts  

\[
 \begin{array}{c}
 \text{SYSTEM }A \\
 \text{All values of } \\
 Y, X \text{ possible}
 \end{array}
 \qquad
 \begin{array}{|c|}
 \hline
 \text{Adiabatic} \\
 \text{wall} \\
 \hline
 \end{array}
 \qquad
 \begin{array}{c}
 \text{SYSTEM }B \\
 \text{All values of } \\
 Y', X' \text{ possible}
 \end{array}
\]
\[
 \text{(a)}
\]
\[
 \begin{array}{c}
 \text{SYSTEM }A \\
 \text{Only restricted } \\
 \text{values of } Y, X \\
 \text{possible}
 \end{array}
 \qquad
 \begin{array}{|c|}
 \hline
 \text{Diathermic} \\
 \text{wall} \\
 \hline
 \end{array}
 \qquad
 \begin{array}{c}
 \text{SYSTEM }B \\
 \text{Only restricted } \\
 \text{values of } Y', X' \\
 \text{possible}
 \end{array}
\]
\[
 \text{(b)}
\]
**FIGURE 1-1** Properties of (a) adiabatic and (b) diathermic walls.  

If the two systems are separated by a diathermic wall [see Fig. 1- 1(b)], the values of \(X\) , \(Y\) and \(X^{\prime}\) , \(Y^{\prime}\) will change spontaneously until an equilibrium state of the combined system is attained. The two systems are then said to be in thermal equilibrium with each other. The most common experimental diathermic wall is a thin metallic sheet. Thermal equilibrium is the state achieved by two (or more) systems, characterized by restricted values of the coordinates of the systems, after they have been in communication with each other through a diathermic wall. Unlike the diathermic wall, an adiabatic wall prevents two systems from communicating with each other and coming to thermal equilibrium with each other. Although we have not yet defined the concept of heat, it may be said that a diathermic wall is a boundary through which heat is communicated from one system to another system, yet remains closed to the transport of matter. An ideal adiabatic wall does not communicate heat.  

Imagine two systems \(A\) and \(B\) , separated from each other by an adiabatic wall but each in contact simultaneously with a third system \(C\) through diathermic walls, the whole assembly being surrounded by an adiabatic wall as shown in Fig. 1- 2(a). Experiment shows that the two systems will come to thermal equilibrium with the third system. No further change will occur if the adiabatic wall separating \(A\) and \(B\) is then replaced by a diathermic wall, as well as if the diathermic wall separating \(C\) from both \(A\) and \(B\) is also replaced by an adiabatic wall [Fig. 1- 2(b)]. If, instead of allowing both systems \(A\) and \(B\) to come to equilibrium with \(C\) at the same time, we first establish equilibrium between \(A\) and \(C\) and later establish equilibrium between \(B\) and \(C\) (the state of system \(C\) being the same in both cases); then, when \(A\) and \(B\) are brought into communication through a diathermic wall, they will be found to be in thermal equilibrium with each other. We shall use the expression "two systems are in thermal equilibrium" to mean also that the two systems are in states such that, if the two were connected through a diathermic wall, the combined system would be in thermal equilibrium.

===== Page 31 =====

\[
 \begin{array}{c}
 \text{FIGURE 1- 2} \\
 \text{The zeroth law of thermodynamics. (Adiabatic walls are designated by diagonal shading; diathermic walls, by heavy lines.)}
 \end{array}
\]
\[
 \begin{array}{ccc}
 \text{SYSTEM} & & \text{SYSTEM} \\
 C & & C \\
 \begin{array}{|c|}
 \hline
 \\
 \\
 \\
 \hline
 \end{array} & \begin{array}{|c|}
 \hline
 \text{SYSTEM} \\
 A \\
 \\
 \hline
 \end{array} & \begin{array}{|c|}
 \hline
 \text{SYSTEM} \\
 B \\
 \\
 \hline
 \end{array} \\
 \begin{array}{c}
 \text{If } A \text{ and } B \text{ are each in} \\
 \text{thermal equilibrium with } C, \text{ then} \\
 \text{(a)}
 \end{array} & & \begin{array}{c}
 A \text{ and } B \text{ are in thermal} \\
 \text{equilibrium with each other} \\
 \text{(b)}
 \end{array}
 \end{array}
\]
**FIGURE 1-2** The zeroth law of thermodynamics. (Adiabatic walls are designated by diagonal shading; diathermic walls, by heavy lines.)  

These experimental facts may then be stated concisely in the following transitive relation: Two systems in thermal equilibrium with a third are in thermal equilibrium with each other. As suggested by Ralph Fowler, this postulate of transitive thermal equilibrium has been numbered the zeroth law of thermodynamics, which establishes the basis for the concept of temperature and for the use of thermometers.  

The postulate of thermal equilibrium is numbered the zeroth law, rather than the first law, because of the historical development in the understanding of the logical order of the laws of thermodynamics. The first law of thermodynamics, which establishes the conservation of energy, including heat, was clearly formulated in 1848 by Hermann Helmholtz and William Thomson (later Lord Kelvin) using experimental data gathered by James Prescott Joule (1843- 1849) and insight provided by Julius Mayer (1842). The second law of thermodynamics was postulated earlier (1824) in Sadi Carnot's study of the working of steam engines. Logically, Carnot's principle must follow the first law if his principle is expressed as a restriction on the means by which energy can be communicated while still being conserved. As the postulates of thermodynamics were developed further, it was realized by Fowler (1931) that thermal equilibrium had to be defined before the first law could be stated. Unable to renumber the two previously established laws of thermodynamics, he was forced to adopt zero as the number of his law. It is unlikely that future developments will raise the possibility of the "minus first" law of thermodynamics.

===== Page 32 =====

1.6 CONCEPT OF TEMPERATURE  

The concept of temperature is r in interpretations and levels of abstraction. In its anthropomorphic understanding, temperature is a measure of the hotness of a given macroscopic object, as felt by the human body. Even though coldness is commonly used to express some temperatures, we prefer to avoid the word "coldness" for reasons provided by statistical mechanics. In the microscopic point of view, temperature is associated with the agitation, vibration, or motion of the object's constituent particles. Accordingly, coldness means "less hotness." To avoid ambiguity, it is suggested that the word "coldness" be avoided and let the concept of temperature be understood as the degree of hotness of an object above zero hotness.  

A scientific understanding of the concept of temperature builds upon thermal equilibrium, established in the zeroth law of thermodynamics. Consider a system \(A\) in the state \(X_{1}\) , \(Y_{1}\) in thermal equilibrium with another system \(B\) in the state \(X_{1}^{\prime}\) , \(Y_{1}^{\prime}\) . If system \(A\) is removed and its state changed, there will be found a second state \(X_{2}\) , \(Y_{2}\) that is in thermal equilibrium with the original state \(X_{1}^{\prime}\) , \(Y_{1}^{\prime}\) of system \(B\) . Experiment shows that there exists a whole set of states — \(X_{1}\) , \(Y_{1}\) ; \(X_{2}\) , \(Y_{2}\) ; \(X_{3}\) , \(Y_{3}\) — any one of which is in thermal equilibrium with this same state \(X_{1}^{\prime}\) , \(Y_{1}^{\prime}\) of system \(B\) , and all of which, by the zeroth law, are in thermal equilibrium with one another. We shall suppose that all such states, when plotted on an \(X - Y\) diagram, lie on a curve such as I in Fig. 1- 3, which we shall call an isotherm. An isotherm is the locus of all points representing states in which a system is in thermal equilibrium with one state of another system. We make no assumption as to the continuity of the isotherm, although experiments on simple systems indicate usually that at least a portion of an isotherm is a continuous curve.  

\[
 \begin{array}{c}
 \text{SYSTEM } A \\
 \begin{array}{cc}
 Y & \\
 & \begin{array}{c}
 \text{III} \\
 \text{II} \\
 \text{I}
 \end{array} \\
 \text{Y}_1,\text{X}_1 & \begin{array}{c}
 \bullet \\
 \text{Y}_2,\text{X}_2 \bullet \\
 \bullet \text{Y}_3,\text{X}_3
 \end{array}
 \end{array} \\
 X
 \end{array}
 \]
**FIGURE 1-3** Isotherms of two different systems.  

\[
 \begin{array}{c}
 \text{SYSTEM } B \\
 \begin{array}{cc}
 Y' & \\
 & \begin{array}{c}
 \text{III}' \\
 \text{II}' \\
 \text{I}'
 \end{array} \\
 & \begin{array}{c}
 \bullet \text{Y}_1',\text{X}_1' \\
 \text{Y}_2',\text{X}_2' \bullet \\
 \bullet \text{Y}_3',\text{X}_3'
 \end{array}
 \end{array} \\
 X'
 \end{array}
\]

===== Page 33 =====

1: Temperature and the Zeroth Law of Thermodynamics 11  

Similarly, with regard to system \(B\) , we find a set of states — \(X_{1}^{\prime}\) , \(Y_{1}^{\prime}\) ; \(X_{2}^{\prime}\) , \(Y_{2}^{\prime}\) ; \(X_{3}^{\prime}\) , \(Y_{3}^{\prime}\) — all of which are in thermal equilibrium with one state \((X_{1}, Y_{1})\) of system \(A\) , and, therefore, in thermal equilibrium with one another. These states are plotted on the \(X^{\prime} - Y^{\prime}\) diagram of Fig. 1- 3 and lie on the isotherm \(I^{\prime}\) . From the zeroth law, it follows that all the states on isotherm \(I\) of system \(A\) are in thermal equilibrium with all the states on isotherm \(I^{\prime}\) of system \(B\) . We shall call curves \(I\) and \(I^{\prime}\) corresponding isotherms of the two systems.  

If the experiments just outlined are repeated with different starting conditions, another set of states of system \(A\) lying on curve \(II\) may be found, every one of which is in thermal equilibrium with every state of system \(B\) lying on curve \(II^{\prime}\) . In this way, a family of isotherms \(I\) , \(II\) , \(III\) , etc., of system \(A\) and a corresponding family \(I^{\prime}\) , \(II^{\prime}\) , \(III^{\prime}\) , etc., of system \(B\) may be found. Furthermore, by repeated applications of the zeroth law, corresponding isotherms of still other systems \(C\) , \(D\) , etc., may be obtained.  

All states of corresponding isotherms of all systems have something in common, namely, that they are in thermal equilibrium with one another. The systems themselves, in these states, may be said to possess a property that ensures their being in thermal equilibrium with one another. We call this property temperature. The temperature of a system is a property that determines whether or not a system is in thermal equilibrium with other systems.  

The scalar character of temperature may be established on the basis of the zeroth law of thermodynamics. For systems \(A\) and \(B\) to be in thermal equilibrium, all the information that is needed is that both \(A\) and \(B\) are in thermal equilibrium with \(C\) . This is not true, for instance, for mechanical equilibrium of elastic crystalline solids; the tensor character of the stresses found in two crystalline bodies means that the two bodies need not necessarily be in mechanical equilibrium with each other just because each is in mechanical equilibrium with a third body.  

Since temperature is a scalar quantity, the temperature of all systems in thermal equilibrium may be represented by a number. The establishment of a temperature scale is merely the adoption of a set of rules for assigning one number to a set of corresponding isotherms, and a different number to a different set of corresponding isotherms. Once this is done, the necessary and sufficient condition for thermal equilibrium between two systems is that they have the same temperature. Also, when the temperatures are different, we may be sure that the systems are not in thermal equilibrium.  

To determine whether or not two beakers of water are in equilibrium, it is not necessary to bring them into contact by means of a diathermic wall and see if their properties change with time. Rather, an unmarked glass capillary tube filled with mercury (system \(A\) ) is inserted into the first beaker (system \(B\) ) and, shortly, some property of this device, such as the height of the mercury column, comes to rest. Then, by definition, the device has the same temperature as the water in the first beaker. The procedure is repeated with the other beaker of water (system \(C\) ). If the heights of the mercury columns are the same, then the temperatures of \(B\) and \(C\) are equal. Furthermore, experiment shows that if the two beakers are now brought into contact, there are no

===== Page 34 =====

12 PART I: Fundamental Concepts  

changes in their properties. Notice that the mercury- filled glass capillary tube requires no scale; the requirement is only that the height of the mercury in the two tests must be the same. Such a device is a thermoscope, which indicates only equality of temperature for the corresponding isotherms of the systems. In order to assign a numerical value to the temperature, we perform experiments on a standard system.  

### 1.7 THERMOMETERS AND MEASUREMENT OF TEMPERATURE  

To establish an empirical temperature scale, we select some system with coordinates \(X\) and \(Y\) as a standard, which we call a thermometer, and adopt a set of rules for assigning a numerical value to the temperature associated with each of its isotherms. To every other system in thermal equilibrium with the thermometer, we assign the same number for the temperature. The simplest procedure is to choose any convenient path in the \(X - Y\) plane, such as that shown in Fig. 1- 4 by the dashed line \(Y = Y_{1}\) , which intersects the isotherms at points each of which has the same \(Y\) - coordinate but a different \(X\) - coordinate. The temperature associated with each isotherm is then taken to be a convenient function of the \(X\) at this intersection point. The coordinate \(X\) is called the thermometric property, and the form of the thermometric function \(\theta (X)\)  

\[
 \begin{array}{c}
 \text{isotherm at the temperature of the} \\
 \text{triple point of water}
 \end{array}
\]
\[
 Y=Y_1
\]
\[
 X_{TP}
\]
**FIGURE 1-4** Setting up a temperature scale involves assignment of numerical values to the isotherms of an arbitrarily chosen standard system (the thermometer).

===== Page 35 =====

 determines the empirical temperature scale. There are many different kinds of thermometer, each with its own thermometric property, and six modern thermometers are shown in Table 1.1  

Let \(X\) stand for any one of the thermometric properties listed in Table 1.1, and let us decide arbitrarily to define the temperature scale so that the empirical temperature \(\theta\) is directly proportional to \(X\) . The arbitrary choice of a linear function maintains the temperature scale first used in the historic mercury- in- glass thermometer. Thus, the temperature common to the thermometer and to all systems in thermal equilibrium with it can be given by the thermometric function,  

\[
 \theta (X) = aX\qquad (\mathrm{constant}~Y), \quad (1.1)
\]

where \(a\) is an arbitrary constant. Notice that as the coordinate \(X\) approaches zero, the temperature also approaches zero, because there is no arbitrary constant added to the function. In effect, the linear function in Eq. (1.1) also defines an absolute temperature scale, such as the Kelvin scale or the Rankine scale.  

It should be noted further that different empirical temperature scales usually result when this arbitrary relation is applied to different kinds of thermometers and even when it is applied to different systems of the same kind, such as constant volume hydrogen or nitrogen thermometers. One must thus ultimately select, either arbitrarily or in some rational way, one kind of thermometer, such as a constant- volume gas thermometer, and one particular system, such as hydrogen gas, to serve as the standard thermometric instrument, which is how the first international temperature scale was established in 1887. But regardless of what standard is chosen, the value of the coefficient \(a\) in Eq. (1.1) must be established; only then does one have a numerical relation between the empirical temperature \(\theta (X)\) and the thermometric property \(X\) .  

Equation (1.1) applies, in general, to a thermometer placed in contact with a system whose temperature \(\theta (X)\) is to be measured. Therefore, it applies when the thermometer is placed in contact with an arbitrarily chosen standard system in a reproducible state; such a state of an arbitrarily chosen standard  

TABLE 1.1 Thermometers and thermometric properties   

| Thermometer | Thermometric property | Symbol |
| :--- | :--- | :--- |
| Gas (const. volume) | Pressure | \(P\) |
| Platinum resistance (const. tension) | Electric resistance | \(R'\) |
| Thermocouple (const. tension) | Thermal emf | \(\mathcal{C}\) |
| Helium vapor (saturated) | Pressure | \(P\) |
| Paramagnetic salt | Magnetic susceptibility | \(X\) |
| Blackbody radiation | Radiant exitance | \(\mathcal{E}_{bb}\) |

===== Page 36 =====

14 PART I: Fundamental Concepts  

system is called a fixed point, that is, fixed temperature. The fixed point provides a reference temperature for the determination of temperature scales.  

Before 1954, the international metric temperature scale was the Celsius scale, which was based on the temperature interval between two fixed points: (1) the temperature at which pure ice coexisted in equilibrium with air- saturated water at standard atmospheric pressure (the ice point); and (2) the temperature of equilibrium between pure water and pure steam at standard atmospheric pressure (the steam point). The temperature interval between these two fixed points was assigned 100 "degrees" (of hotness), abbreviated as \(100^{\circ}\mathrm{C}\) . Hundreds of attempts were made all over the world to measure the temperature of the ice point with great accuracy — without much success. The main difficulty was achieving equilibrium between air- saturated water and pure ice. When ice melts, it surrounds itself with pure water that prevents intimate contact between ice and air- saturated water. Attempts to measure the steam point also present problems, because the temperature of the steam point is very sensitive to pressure.  

In 1954, a single fixed point was chosen as the basis for a new international temperature scale, the Kelvin scale. The state in which ice, liquid water, and water vapor coexist in equilibrium, a state known as the triple point of water, provides the standard reference temperature. The temperature of the triple point of water, which can be very accurately and reproducibly measured, was assigned the value 273.16 kelvin, corresponding to \(0.01^{\circ}\mathrm{C}\) , in order to maintain the magnitude of a unit of temperature. Notice that the word "degree" has been dropped from the Kelvin scale, so the triple- point temperature is abbreviated as 273.16 K.  

We can now solve Eq. (1.1) for the coefficient \(a\) :  

\[
 a = \frac{273.16\mathrm{K}}{X_{TP}}, \quad (1.2)
\]

where the subscript \(TP\) identifies the property value \(X_{TP}\) explicitly with the triple- point temperature. In view of Eq. (1.2), the general Eq. (1.1) may be written  

\[
 \theta (X) = 273.16\mathrm{K}\frac{X}{X_{TP}}\qquad (\mathrm{constant}Y). \quad (1.3)
\]

The temperature of the triple point of water is the standard fixed point of thermometry. To achieve the triple point, one distills water of the highest purity and of substantially the same isotopic composition of ocean water into a vessel depicted schematically in Fig. 1- 5. When all air has been removed, the vessel is sealed off. With the aid of a freezing mixture in the inner well, a layer of ice is formed around the well. When the freezing mixture is replaced by a thermometer bulb, a thin layer of ice is melted nearby. So long as the solid, liquid, and vapor phases coexist in equilibrium, the system is at the triple point.

===== Page 37 =====

1.8 COMPARISON OF THERMOMETERS  

Applying the principles outlined in the preceding paragraphs to the first three thermometers listed in Table 1.1, we have three different ways of measuring temperature. Thus, for a gas at constant volume,  

\[
 \theta (P) = 273.16\mathrm{K}\frac{P}{P_{TP}}\qquad (\mathrm{constant}V); \quad (1.4)
\]

for a platinum wire resistor,  

\[
 \theta (R^{\prime}) = 273.16\mathrm{K}\frac{R^{\prime}}{R_{TP}^{\prime}};
\]

and for a thermocouple,  

\[
 \theta (\mathcal{C}) = 273.16\mathrm{K}\frac{\mathcal{C}}{\mathcal{C}_{TP}}.
\]

Now, imagine a series of tests in which the temperature of a given system is measured simultaneously with each of the three thermometers. Such a comparison is shown in Table 1.2, where the constant- volume gas thermometer is used at high pressure and low pressure. The letters NBP stand for the normal boiling point, by which the word normal specifies that the temperature at which a liquid boils occurs at standard atmospheric pressure (101,325 Pa or \(14.7\mathrm{lb} / \mathrm{in}^2\) ). Similarly, the letters NMP stand for the normal melting point,

===== Page 38 =====

16 PART I: Fundamental Concepts  

TABLE 1.2 Comparison of thermometers   

| Fixed point | Copper-constantan thermometer | | Platinum resistance thermometer | | Constant-volume H₂ thermometer | | Constant-volume H₂ thermometer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | \(\delta\), mV | \(\theta(\delta)\) | \(R'\), \(\Omega\) | \(\theta(R')\) | \(P\), kPa | \(\theta(P)\) | \(P\), kPa |
| N₂ (NBP) | 0.733 | 2.0 | 1.965 | 4.5 | 184 | 73 | 2979 |
| O₂ (NBP) | 0.954 | 1.5 | 2.506 | 9.5 | 216 | 86 | 3390 |
| CO₂ (NSP) | 3.52 | 154 | 6.65 | 185 | 486 | 193 | 73196 |
| H₂O (TP) | 6.26 | 273 | 9.832 | 273 | 68 | 273 | 101273 |
| H₂O (NBP) | 10.05 | 440 | 13.65 | 380 | 942 | 374 | 139374 |
| Sn (NMP) | 17.50 | 762 | 18.56 | 516 | 1287 | 510 | 187505 |

NSP for the normal sublimation point, and TP for the triple point, the temperature at which the solid, liquid, and vapor coexist in thermal equilibrium. The numerical values are not meant to be exact, and 273.16 has been written simply 273.  

If one compares the \(\theta\) columns in Table 1.2, it may be seen that at any fixed point, except the triple point of water, which is the arbitrarily chosen reference temperature for all thermometers, the thermometers disagree. Even the two hydrogen thermometers disagree slightly, but the variation among gas thermometers may be greatly reduced by using low pressures, so that a gas thermometer has been chosen as the standard thermometer to define the empirical temperature scale for temperatures not too far from ambient temperatures. At extremely low temperatures or extremely high temperatures, there are other standard thermometers. Within its operating range, the advantage of the gas thermometer is a well- understood equation of state, which permits the identification and elimination of sources of error.  

## 1.9 GAS THERMOMETER  

A simplified schematic diagram of a constant- volume gas thermometer is shown in Fig. 1- 6. The materials, construction, and dimensions differ in the various laboratories throughout the world where these instruments are used and depend on the nature of the gas and the temperature range for which the thermometer is intended. The gas is contained in the glass bulb \(B\) , which communicates with the mercury column \(M\) through a capillary. The volume of the gas is kept constant by adjusting the height of the mercury column \(M\) until the mercury level just touches the tip of a small pointer (indicial point) in the space above \(M\) , known as the dead space or nuisance volume. The mercury column \(M\) is adjusted by raising or lowering the reservoir. The pressure in the system equals atmospheric pressure plus the difference in height \(h\) between the

===== Page 39 =====

\[
 \begin{array}{c}
 \text{FIGURE 1- 6} \\
 \text{Simplified constant- volume gas thermometer. Mercury reservoir is raised or lowered so that the meniscus at the left always touches the indicial point. Bulb pressure equals } h \text{ plus atmospheric pressure.}
 \end{array}
\]
\[
 \begin{array}{c}
 \text{Capillary} \\
 \text{Bulb } B \\
 \text{Indicial point} \\
 M \\
 h \\
 \text{Mercury reservoir} \\
 M' \\
 \text{Mercury reservoir} \\
 \end{array}
\]

the two mercury columns \(M\) and \(M^{\prime}\) and is measured twice: when the bulb is surrounded by the system whose temperature is to be measured, and when it is surrounded by water at the triple point.  

The various values of the pressure must be corrected to take account of many sources of error, such as:  

1. The gas present in the dead space (and in any other nuisance volumes) is at a temperature different from that in the bulb.  
2. The gas in the capillary connecting the bulb with the manometer has a temperature gradient; that is, it is not at a uniform temperature.  
3. The bulb, capillary, and nuisance volumes undergo changes of volume when the temperature and pressure change.  
4. A pressure gradient exists in the capillary when the diameter of the capillary is comparable to the mean free path of the gas particles.  
5. Some gas is adsorbed on the walls of the bulb and capillary; the lower the temperature, the greater the adsorption.  
6. There are effects due to temperature and compressibility of the mercury in the manometer.

===== Page 40 =====

18 PART I: Fundamental Concepts  

Improvements and alternative ways of measuring pressure have been incorporated into the design of gas thermometers, so these errors can be estimated and eliminated from the data. As a result, the behavior of real gases approaches the behavior of the ideal gas in limiting conditions.  

## 1.10 IDEAL-GAS TEMPERATURE  

In the nineteenth century, no thermometer compared in effectiveness with the gas thermometer. It was officially adopted by the International Committee on Weights and Measures in 1887 as the standard thermometer to replace the mercury- in- glass thermometer. The theoretical basis for gas thermometry became the well- understood relationship between pressure, volume, and temperature embodied in the ideal- gas law, namely,  

\[
 PV = nRT, \quad (1.5)
\]

where \(P\) is the pressure of the system of gas, \(V\) is the volume of gas, \(n\) is the number of moles of gas, and \(R\) is the molar gas constant. The temperature \(T\) is the theoretical thermodynamic temperature. In this section, we show the experiment that yields reproducible and accurate empirical temperatures \(\theta\) . Greek letter theta \((\theta)\) indicates the real- gas temperature and \(T\) the thermodynamic ideal- gas temperature. In Sec. 7.7, we will justify the identification of the ideal- gas temperature with the thermodynamic temperature. The ideal- gas temperature is found using a constant- volume gas thermometer. Applying Eq. (1.5) initially to the gas at the assigned temperature of \(273.16 \mathrm{~K}\) and then to the gas at the unknown empirical temperature, one obtains the proportion  

\[
 \frac{P}{P_{TP}} = \frac{\theta}{273.16 \mathrm{~K}}, \quad (1.6)
\]

or  

\[
 \theta = 273.16 \mathrm{~K} \frac{P}{P_{TP}} \quad (\mathrm{constant} V). \quad (1.6)
\]

It is no coincidence that Eq. (1.6) is the same as Eq. (1.4). The Kelvin temperature scale and gas thermometers evolved together.  

Consider measuring the ideal- gas temperature at the normal boiling point (NBP) of water (the steam point). An amount of gas is introduced into the bulb of a constant- volume gas thermometer, and one measures \(P_{TP}\) when the bulb of the constant- volume thermometer is inserted in the triple- point cell shown in Fig. 1- 5. Suppose that \(P_{TP}\) is equal to \(120 \mathrm{kPa}\) . Keeping the volume \(V\) constant, carry out the following procedures:  

1. Surround the bulb with steam at standard atmospheric pressure, measure the gas pressure \(P_{NBP}\) , and calculate the empirical temperature \(\theta\) using Eq. (1.6),

===== Page 41 =====

2. Remove some of the gas so that \(P_{TP}\) has a smaller measured value, say, \(60 \mathrm{kPa}\) . Measure the new value of \(P_{NBP}\) and calculate a new value,  

\[
 \theta (P_{NBP}) = 273.16\mathrm{K}\frac{P_{NBP}}{60}.
\]

3. Continue reducing the amount of gas in the bulb so that \(P_{TP}\) and \(P_{NBP}\) have smaller and smaller values, \(P_{TP}\) having values of, say, \(40 \mathrm{kPa}\) , \(20 \mathrm{kPa}\) , etc. At each value of \(P_{TP}\) , calculate the corresponding \(\theta (P_{NBP})\) .  

4. Plot \(\theta (P_{NBP})\) against \(P_{TP}\) and extrapolate the resulting curve to the axis where \(P_{TP} = 0\) . Read from the graph,  

\[
 \lim_{P_{TP}\to 0}\theta (P_{NBP}).
\]

The results of a series of tests of this sort are plotted in Fig. 1- 7 for three different gases in order to measure \(\theta (P)\) for the normal boiling point of water. The graph conveys the information that, although the readings of a constant- volume gas thermometer depend upon the nature of the gas at ordinary values of \(P_{NBP}\) , all gases indicate the same temperature as \(P_{TP}\) is lowered and made to approach zero.  

Therefore, we define the ideal- gas temperature \(T\) by the equation  

\[
 T = 273.16\mathrm{K}\lim_{P_{TP}\to 0}\left(\frac{P}{P_{TP}}\right)\qquad (\mathrm{constant}V). \quad (1.7)
\]

Although the ideal- gas temperature scale is independent of the properties of any one particular gas, it still depends on the properties of gases in general. Helium is the most useful gas for thermometric purposes for two reasons. At high temperatures helium does not diffuse through platinum, whereas hydrogen does. Furthermore, helium becomes a liquid at a temperature lower than any other gas, and, therefore, a helium thermometer may be used to measure temperatures lower than those which can be measured with any other gas thermometer.  

The lowest ideal- gas temperature that can be measured with a constant- volume gas thermometer is about \(2.6 \mathrm{K}\) , provided that low- pressure \(^3\mathrm{He}\) is used. The temperature \(T = 0\) remains as yet undefined by means of thermometry. In Chap. 7, the Kelvin temperature scale, which is independent of the properties of any particular substance, will be developed from the second law of thermodynamics. It will be shown that, in the temperature region in which a gas thermometer may be used, the ideal- gas scale and the Kelvin thermodynamic scale are identical. In anticipation of this result, we write K after an ideal- gas temperature. It will also be shown in Chap. 7 how the absolute zero of temperature is defined on the Kelvin scale. It should be remarked that the statement, found in some textbooks of elementary science, that at absolute zero all

===== Page 42 =====

20 PART I: Fundamental Concepts  

\[
 \theta(P) \text{ } \rightarrow \quad 373.60 \quad 373.50 \quad 373.40 \quad 373.30 \quad 373.20 \quad 373.10 \quad 0 \quad 20 \quad 40 \quad 60 \quad 80 \quad 100 \quad 120 \quad P_{TP}, \text{ kPa}
\]
\[
 \begin{array}{c}
 \text{N}_2 \\
 \text{H}_2 \\
 \text{He}
 \end{array}
\]
\[
 T (\text{steam}) = 373.124 \text{ K}
\]
**FIGURE 1-7**  
Readings of a constant- volume gas thermometer for the temperature of steam (NBP of water) when different gases are used at various arbitrary values of \(P_{TP}\) . (Limiting value obtained from R. L. Rusby, R. P. Hudson, M. Durieux, J. F. Schooley, P. P. M. Steur, and C. A. Swenson: Metrologia, vol. 28, pp. 9- 18, 1991. )  

atomic motion ceases is erroneous. First, such a statement involves an assumption connecting the purely macroscopic concept of temperature and the microscopic concept of atomic motion. If we want thermodynamics to be general, this is precisely the sort of assumption that must be avoided. Second, when it is necessary in statistical mechanics to correlate temperature to atomic or molecular motion, it is found that classical statistical mechanics must be modified with the aid of quantum mechanics and that, when this modification is carried out, the particles of a substance at absolute zero have a finite amount of residual vibrational energy, known as the zero- point energy.  

### 1.11 CELSIUS TEMPERATURE SCALE  

The Celsius temperature scale, named after the Swedish astronomer Anders Celsius, was the international temperature scale prior to the introduction of the Kelvin scale in 1954. The Kelvin temperature scale is based upon a degree of the same magnitude as that of the Celsius scale; the fixed point was shifted from the ice point of water (273.15 K) to the triple point of water, which was defined to be \(0.01^{\circ}C\) above the ice point of water, that is 273.16 K. In effect, the numerical values of the normal freezing point of water and the normal boiling point of water were left to be determined by experiment, rather than being defined fixed temperatures. So, if \(\theta\) denotes the Celsius temperature, the relationship between the Celsius scale and the Kelvin scale is simply

===== Page 43 =====

1: Temperature and the Zeroth Law of Thermodynamics 21  

\[
 \theta (\mathrm{{^\circ C}}) = T(\mathrm{{K}}) - 273.15. \quad (1.8)
\]

For example, the Celsius temperature \(\theta_{NBP}\) at which water boils at standard atmospheric pressure is  

\[
 \theta_{NBP} = T_{NBP} - 273.15,
\]

and reading \(T_{NBP}\) from Fig. 1- 7,  

\[
 \theta_{NBP} = 373.124 - 273.15 = 99.974^{\circ}\mathrm{C}.
\]

It should not be surprising that the normal boiling point of water is no longer exactly \(100^{\circ}\mathrm{C}\) . The only Celsius temperature that is fixed by definition after 1954 is that of the triple point of water. All other temperatures must be measured with respect to the triple point of water as the result of making the Kelvin scale the international standard for thermodynamic temperatures.  

### 1.12 PLATINUM RESISTANCE THERMOMETRY  

Although gas thermometers could provide thermodynamic temperatures, they are cumbersome and unsuited for many applications. A more practical thermometer is the platinum resistance thermometer, which is much more reproducible, simpler to use, and generally provides a greater range of operation than the gas thermometer. The platinum resistance thermometer is secondary to the gas thermometer, because any expression that describes the electrical resistance as a function of temperature contains unknown, temperature- dependent terms that we cannot calculate from first principles.  

When the resistance thermometer is in the form of a long, fine wire, it is usually wound around a thin frame constructed so as to avoid excessive strains when the wire contracts upon cooling. In special circumstances, the wire may be wound on or embedded in the material whose temperature is to be measured. In the very low- temperature range, resistance thermometers often consist of small carbon- composition radio resistors or a germanium crystal, doped with arsenic and sealed in a helium- filled capsule. These may be bonded to the surface of the substance whose temperature is to be measured or placed in a hole drilled for that purpose.  

Resistance measuring circuits may be divided into two groups: potentiometric types, in which at balance there is exactly zero direct current flowing in the voltage leads; and bridge circuits, in which at balance a negligible alternating current flows. Until the late 1960s, bridge circuits had no application in setting temperature standards. Since then, two factors have altered this situation. First, there is the development of the inductive voltage- divider, or ratio transformer, in bridge circuits. Second, there is the improvement in electronics, which has produced lock- in amplifiers of high sensitivity and excellent signal- to- noise characteristics. Elaborate self- balancing systems have also become available.

===== Page 44 =====

22 PART I: Fundamental Concepts  

The platinum resistance thermometer may be used for very accurate work within the range 13.8033 to 1234.93 K \((- 259.3467\) to \(961.78^{\circ}C)\) . The calibration of the instrument involves the measurement of \(R^{\prime}(T)\) at various known defining temperatures and the representation of the results by an empirical formula. In a restricted range, the following quadratic equation is often used:  

\[
 R^{\prime}(T) = R_{TP}^{\prime}(1 + aT + bT^{2}), \quad (1.9)
\]

where \(R^{\prime}(T)\) is the resistance of the platinum wire at the temperature \(T\) , \(R_{TP}^{\prime}\) is the resistance of the platinum wire when it is surrounded by water at the triple point, and \(a\) and \(b\) are constants. In order to avoid the need for precise absolute measurements of resistance, the calibration of thermometers is always in terms of the ratio \(R^{\prime}(T) / R_{TP}^{\prime}\) , known as \(W(T)\) . Thus, in effect, resistivities are measured rather than resistances. Another advantage is that \(W(T)\) is relatively insensitive to the effects of strain or contamination of the wire.  

### 1.13 RADIATION THERMOMETRY  

Optical pyrometry, radiation pyrometry, infrared pyrometry, and spectral or total- radiation pyrometry are some of the methods of thermometry based on the measurement of thermal radiation, or so- called blackbody radiation.  

In radiation thermometry, in contrast to resistance thermometry, we make use of a well- established equation, the Planck radiation law, which relates thermodynamic temperature to the measured spectral radiance. The thermal radiation existing inside a closed cavity (blackbody radiation) depends only on the temperature of the walls and not at all upon their shape or composition, provided that the cavity dimensions are much larger than the wavelengths of the thermal radiation. The radiation escaping from a small hole in the cavity is perturbed by the presence of the hole. By careful design, this perturbation can be made negligibly small, so that equilibrium blackbody radiation is available for measurement. Thus, in principle, thermodynamic temperature may be measured very precisely by means of radiation thermometry.  

Radiation thermometers called pyrometers were developed for measuring high temperatures (greater than approximately \(1100^{\circ}C\) ), and they have the advantage that they are noncontact thermometers. Optical pyrometers measure temperatures of objects by comparing the visible radiation from the hot objects over a narrow wavelength band with the radiation from a standard, preferably using a photoelectric detector for measurements rather than the human eye. Corrections for the emissivity of the source must be made to determine the temperature. Total- radiation pyrometers measure the whole spectrum of electromagnetic waves, including infrared radiated by the object, in order to determine the temperature. Total- radiation pyrometers are less

===== Page 45 =====

 accurate than optical pyrometers but can measure much lower temperatures, including the triple point of water!  

### 1.14 VAPOR PRESSURE THERMOMETRY  

Saturation vapor pressure thermometry is commonly used for the measurement of temperature in the range between 0.3 and \(5.2\mathrm{K}\) , because of the sensitivity and convenience of this type of measurement. The thermometric substance is the vapor in equilibrium with the liquid of either of the two isotopes of helium: \(^3\mathrm{He}\) or \(^4\mathrm{He}\) . Helium vapor pressure is the thermometric parameter, because it depends only on a physical property of a pure element and can be reproduced at any time, it requires no interpolation device, and it is relatively easy to measure with sufficient precision over much of the temperature range.  

The range of practical usefulness of the \(^4\mathrm{He}\) vapor pressure scale is from approximately \(1.0\mathrm{K}\) (because of the small variation of pressure with temperature and complications due to superfluid behavior) to \(5.2\mathrm{K}\) (because the liquid does not exist above this temperature: the critical point). The range for the \(^3\mathrm{He}\) scale is from approximately \(0.30\mathrm{K}\) (because the pressure is inconveniently small to measure) to \(3.32\mathrm{K}\) (the critical point).  

### 1.15 THERMOCOUPLE  

A schematic diagram of a thermocouple is shown in Fig. 1- 8, where the temperature to be measured is located at the test junction. The thermal electromotive force (emf) is generated at the point where wire \(A\) and wire \(B\) are joined. The two thermocouple wires are connected to copper wires located at the reference junction, which is maintained at the temperature of melting ice.  

A thermocouple is calibrated by measuring the thermal emf at the test junction at various known temperatures, the reference junction being kept at \(0^{\circ}\mathrm{C}\) . The results of such measurements on most thermocouples can usually be represented by a cubic equation, as follows:  

\[
 \mathcal{C} = c_0 + c_1\theta +c_2\theta^2 +c_3\theta^3,
\]

where \(\mathcal{C}\) is the thermal emf, and the constants \(c_0,c_1,c_2\) ,and \(c_{3}\) are different for each thermocouple. Within a restricted range of temperature, a quadratic equation is often sufficient. The temperature range of a thermocouple depends upon the materials of which it is composed. The type K thermocouple, made of a chromel wire ( \(90\%\) Ni and \(10\%\) Cr) and an alumel wire ( \(95\%\) Ni, \(2\%\) Al, \(2\%\) Mn, and \(1\%\) Si) has a temperature range of \(- 270\) to \(1372^{\circ}\mathrm{C}\) .  

The advantage of a thermocouple is that it quite rapidly comes to thermal equilibrium with the system whose temperature is to be measured, because its

===== Page 46 =====

24 PART I: Fundamental Concepts  

\[
 \begin{array}{c}
 \text{Test} \\
 \text{junction}
 \end{array}
 \qquad
 \begin{array}{c}
 \text{Wire } A \\
 \text{Wire } B
 \end{array}
 \qquad
 \begin{array}{c}
 \text{Reference junction}
 \end{array}
 \qquad
 \begin{array}{c}
 \text{Copper wire}
 \end{array}
 \qquad
 \begin{array}{c}
 \text{Copper wire}
 \end{array}
\]
**FIGURE 1-8** Thermocouple of wires \(A\) and \(B\) with a reference junction, consisting of two junctions with copper wires, ready to be connected to a measuring or monitoring circuit.  

mass is small. Furthermore, the emf of the thermocouple is adaptable to electrical circuits, which monitor and control temperatures in many industrial, commercial, and residential furnaces, ovens, and cooling units. The disadvantage, as far as scientific temperature measurement is concerned, is that the imprecision is about \(0.2 \mathrm{~K}\) , which is five to ten times larger than the imprecision of the platinum resistance thermometer at higher temperatures. Therefore, the thermocouple is no longer a standard thermometer used in the International Temperature Scale of 1990.  

### 1.16 INTERNATIONAL TEMPERATURE SCALE OF 1990 (ITS-90)  

The International Committee of Weights and Measures is concerned with two temperature scales: the first is the theoretical thermodynamic scale; the second is, at any given time, the current practical temperature scale. The use of a constant- volume gas thermometer for routine calibrations or for the usual measurement of thermodynamic temperature is impractical. In 1927, the first international practical temperature scale was adopted to provide the means for easy and rapid calibration of scientific and industrial instruments. The practical temperature scale was revised or amended in 1948, 1960, 1968, 1976, and 1990.  

The International Temperature Scale of 1990 (ITS- 90) consists of a set of defining fixed points measured with the primary gas thermometer, and a set of procedures for interpolation between the fixed points using secondary thermometers. Although ITS- 90 is not intended to supplant the Kelvin thermo

===== Page 47 =====

 dynamic scale, it is constructed so as to provide a very close approximation to it; the differences between the practical temperature scale \(T_{90}\) and the Kelvin thermodynamic temperature scale \(T\) are within the limits of accuracy of measurement attained in 1990.  

The accurate measurement of temperature with a gas thermometer requires years of painstaking laboratory work and mathematical computation and, when completed, becomes an international event. Such work is published in the journal Metrologia and eventually is listed in tables of physical constants. The temperatures of the equilibrium states of a number of materials have been measured, and the results are tabulated in Table 1.3.  

The lower temperature limit of ITS- 90 is \(0.65\mathrm{K}\) . Below this temperature, the scale is undefined in terms of a standardized thermometer, but research continues in order to select a reference thermometer from competing instruments. Various intervals of temperature on ITS- 90 and secondary thermometers are established, as follows:  

1. From 0.65 to 5.0 K. Between 0.65 and \(3.2\mathrm{K}\) , the ITS-90 is defined by the vapor pressure-temperature relations of \(^3\mathrm{He}\) , and between 1.25 and  

TABLE 1.3 Defining fixed points of ITS-90  

| Material† | Equilibrium state§ | \(T_{90}\) (K) | \(t_{90}\) (°C) |
| :--- | :--- | :--- | :--- |
| \(^3\)He and \(^4\)He | VP | 3 to 5 | -270.15 to -268.15 |
| e-H₂ | TP | 13.8033 | -259.3467 |
| e-H₂ (or He) | VP (or CVGT) | ≈ 17 | ≈ 256.15 |
| e-H₂ (or He) | VP (or CVGT) | ≃ 20.3 | ≈ 252.85 |
| Ne | TP | 24.5561 | -248.5939 |
| O₂ | TP | 54.3584 | -218.7916 |
| Ar | TP | 83.8058 | -189.3442 |
| Hg | TP | 234.3156 | -38.8344 |
| H₂O | TP | 273.16 | 0.01 |
| Ga | NMP | 302.9146 | 29.7646 |
| In | NFP | 429.7485 | 156.5985 |
| Sn | NFP | 505.078 | 231.928 |
| Zn | NFP | 692.677 | 419.527 |
| Al | NFP | 933.473 | 660.323 |
| Ag | NFP | 1234.93 | 961.78 |
| Au | NFP | 1337.33 | 1064.18 |
| Cu | NFP | 1357.77 | 1084.62 |

†H. Preston-Thomas: Metrologia, vol. 27, pp. 3-10, 1990.  
‡e-H₂ indicates equilibrium hydrogen, that is, hydrogen with the equilibrium distribution of its ortho and para states. Normal hydrogen at room temperature contains 25 percent para-hydrogen and 75 percent ortho-hydrogen.  
§VP indicates vapor pressure point; CVGT indicates constant-volume gas thermometer point; TP indicates triple point (equilibrium temperature at which the solid, liquid, and vapor phases coexist); NFP indicates normal freezing point, and NMP indicates normal melting point (the NFP and NMP are equilibrium temperatures at which the solid and liquid phases coexist under a pressure of 101,325Pa, 1 standard atmosphere). The isotopic composition is that naturally occurring.

===== Page 48 =====

2.1768 K (the \(\lambda\) -point) and between 2.1768 and \(5.0 \mathrm{~K}\) by the vapor pressure- temperature relations of \(^{4} \mathrm{He}\) .  

2. From 3.0 to 24.5561 K. Between 3.0 and 24.5561 K, the ITS-90 is defined by the \(^{3} \mathrm{He}\) or \(^{4} \mathrm{He}\) constant- volume gas thermometer.  

3. From 13.8033 to 1234.93 K. Between 13.8033 and 1234.93 K (-259.3467 to \(961.78^{\circ} \mathrm{C}\) ), the ITS-90 is defined by resistance ratios \(W(T)\) of platinum resistance thermometers using the specified fixed points given in Table 1.3 and by reference functions and deviation functions of resistance ratios between the fixed points. Eleven subranges have been established to accommodate a variety of necessary measurements.  

4. Above 1234.93 K. At temperatures above 1234.93 K (961.78°C), ITS-90 is defined by an optical pyrometer using the ratio of spectral concentrations of the radiance of a blackbody as calculated using Planck's radiation law. Only one reference temperature is required for the pyrometer: the freezing point of gold, the freezing point of silver, or the freezing point of copper.  

Before ITS- 90 was adopted, the thermocouple was the standardized thermometer for the upper temperatures. It was removed due to insufficient accuracy. The range of the platinum resistance thermometer has been extended upward to its present limit, and the optical pyrometer is the new standardized thermometer for the highest temperatures.  

### 1.17 RANKINE AND FAHRENHEIT TEMPERATURE SCALES  

Two temperature scales commonly used by engineers in the United States are based on a unit interval of temperature equal to five- ninths the size of a unit interval of temperature on the Kelvin and Celsius scales. By definition, the Rankine scale, named after the English engineer, is an absolute scale and is based solely on the temperature of the triple point of water. The Rankine scale, which does not use the word "degree," is related to the Kelvin temperature scale by the equation  

\[
 T(\mathbf{R}) = \frac{9}{5} T(\mathbf{K}). \quad (1.10)
\]

The Fahrenheit scale, named after the German instrument maker, is defined in relation to the Rankine scale by the equation  

\[
 \theta (\mathrm{{^\circ}F}) = T(\mathrm{{R}}) - 459.67. \quad (1.11)
\]

Thus, at the ice point, where the Kelvin temperature is 273.15, the Rankine temperature is \((9 / 5)(273.15) = 491.67 \mathrm{~R}\) . Hence, the Fahrenheit temperature is  

\[
 \theta (\mathrm{{^\circ}F}) = 491.67 - 459.67 = 32.00^{\circ}\mathrm{F}.
\]

===== Page 49 =====

1.1. In the table below, a number in the top row represents the pressure of a gas in the bulb of a constant- volume gas thermometer (corrected for dead space, thermal expansion of bulb, etc.) when the bulb is immersed in a water triple- point cell. The bottom row represents the corresponding readings of pressure when the bulb is surrounded by a material at a constant unknown temperature. Calculate the ideal- gas temperature \(T\) of this material. (Use five significant figures.)  

\[
 P_{TP},\mathrm{kPa} \quad 133.32 \quad 99.992 \quad 66.661 \quad 33.331
\]
\[
 P,\mathrm{kPa} \quad 204.69 \quad 153.54 \quad 102.37 \quad 51.190
\]

1.2. The limiting value of the ratio of pressures of a gas at the steam point and at the triple point of water when the gas is kept at constant volume is found to be 1.365954. What is the ideal- gas temperature of the steam point to six significant figures?  

1.3. The resistance \(R^{\prime}\) of a particular carbon resistor obeys the equation  

\[
 \sqrt{\frac{\log R^{\prime}}{T}} = a + b\log R^{\prime},
\]

where \(a = - 1.16\) and \(b = 0.675\)  

(a) In a liquid helium cryostat, the resistance is found to be exactly \(1000\Omega\) (ohms). What is the temperature? 
(b) Make a log-log graph of \(R^{\prime}\) against \(T\) in the resistance range from 1000 to 30,000 \(\Omega\) .  

1.4. The resistance of a doped germanium crystal obeys the equation  

\[
 \log R^{\prime} = 4.697 - 3.917\log T.
\]

(a) In a liquid helium cryostat, the resistance is measured to be \(218\Omega\) . What is the temperature?  

(b) Make a log-log graph of \(R^{\prime}\) against \(T\) from 200 to 30,000 \(\Omega\) .  

1.5. The resistance of a platinum wire is found to be \(11.000\Omega\) at the ice point, \(15.247\Omega\) at the steam point, and \(28.887\Omega\) at the sulfur point. Find the constants \(a\) and \(b\) in the equation  

\[
 R^{\prime} = R_{0}^{\prime}(1 + a\theta +b\theta^{2}),
\]

and plot \(R^{\prime}\) against Celsius temperature \(\theta\) in the range from 0 to \(660^{\circ}C\) .  

1.6. When the ice point \(i\) and the steam point \(s\) were chosen as fixed points with 100 degrees between them in the original Celsius scale, the ideal- gas temperature of the ice point was written  

\[
 \theta_{i} = \frac{100}{r_{s} - 1},
\]

===== Page 50 =====

28 PART I: Fundamental Concepts  

where \(r_{s} = \lim \left(P_{s} / P_{i}\right)\) at constant \(V\) .  

(a) Show that the fractional error in \(T_{i}\) produced by an error in \(r_{s}\) is very nearly 3.73 times the fractional error in \(r_{s}\) , or  

\[
 \frac{dT_{i}}{T_{i}} = 3.73\frac{d r_{s}}{r_{s}}.
\]

(b) Any ideal-gas temperature may be written  

\[
 T = T_{i}r,
\]

where \(r = \lim \left(P / P_{i}\right)\) at constant \(V\) . Show that the fractional error in \(T\) is  

\[
 \frac{dT}{T} = \frac{d r}{r} +3.73\frac{d r_{s}}{r_{s}}
\]

(c) Now that the single fixed point of the ideal-gas temperature is a universal constant, show that the fractional error in \(T\) is  

\[
 \frac{dT}{T} = \frac{d r}{r},
\]

where \(r = \lim \left(P / P_{TP}\right)\) at constant \(V\) .  

1.7. The length of the mercury column in the old- fashioned mercury- in- glass thermometer is \(15.00\mathrm{cm}\) when the thermometer is in contact with water at its triple point. Consider the length of the mercury column as the thermometric property \(X\) and let \(\theta\) be the empirical temperature determined by this thermometer.  

(a) Calculate the empirical temperature when the length of the mercury column is \(19.00\mathrm{cm}\) . 
(b) If \(X\) can be measured with a precision of \(0.01\mathrm{cm}\) , can this thermometer distinguish between the normal freezing point of water and the triple point of water?  

1.8. The Rankine temperature scale assigns a numerical value of exactly \(491.67\mathrm{R}\) to the triple point of water. The ratio of two temperatures is defined as the limiting ratio, as \(P_{TP}\rightarrow 0\) , of the corresponding pressures of a gas kept at constant volume.  

(a) Find the best experimental value of the normal boiling point of water on this scale.  

(b) Find the temperature interval between the freezing point and the boiling point.  

1.9. What is the temperature on the Fahrenheit scale of the normal boiling point of \(\mathrm{H}_{2}\mathrm{O}\) , if this temperature is \(99.974^{\circ}\mathrm{C}\) ? (Use five significant figures.)

===== Page 51 =====

2.1 THERMODYNAMIC EQUILIBRIUM  

Suppose that experiments have been performed on a thermodynamic system and that the coordinates necessary and sufficient for a macroscopic description have been determined. When these coordinates change in any way whatsoever, either spontaneously or by virtue of outside influence, the system is said to undergo a change of state. When a system is not influenced in any way by its surroundings, it is said to be isolated. In practical applications of thermodynamics, isolated systems are of little importance. We usually have to deal with a system that is influenced in some way by its surroundings. In general, the surroundings may exert forces on the system or provide contact between the system and a body at some definite temperature. When the state of a system changes, interactions usually take place between the system and its surroundings.  

When there is no unbalanced force or torque in the interior of a system and also none between a system and its surroundings, the system is said to be in a state of mechanical equilibrium. When these conditions are not satisfied, either the system alone or both the system and its surroundings will undergo a change of state, which will cease only when mechanical equilibrium is restored.  

When a system in mechanical equilibrium does not tend to undergo a spontaneous change of internal structure, such as a chemical reaction, or a transfer of matter from one part of the system to another, such as diffusion or solution, however slow, then it is said to be in a state of chemical equilibrium.

===== Page 52 =====

30 PART I: Fundamental Concepts  

A system not in chemical equilibrium undergoes a change of state that, in some cases, is exceedingly slow. The change ceases when chemical equilibrium is reached.  

Thermal equilibrium exists when there is no spontaneous change in the coordinates of a system in mechanical and chemical equilibrium when it is separated from its surroundings by diathermic walls. In other words, there is no exchange of heat between the system and its surroundings. In thermal equilibrium, all parts of a system are at the same temperature, and this temperature is the same as that of the surroundings. When these conditions are not satisfied, a change of state will take place until thermal equilibrium is reached.  

When the conditions for all three types of equilibrium are satisfied, the system is said to be in a state of thermodynamic equilibrium; in this condition, it is apparent that there will be no tendency whatever for any change of state, either of the system or of the surroundings, to occur. States of thermodynamic equilibrium can be described in terms of macroscopic coordinates that do not involve the time, that is, in terms of thermodynamic coordinates. Thermodynamics does not attempt to deal with any problem involving the rate at which a process takes place. The investigation of problems involving the time dependence of changes of state is carried out in other branches of science, as in the kinetic theory of gases, hydrodynamics, and chemical kinetics.  

When the conditions for any one of the three types of equilibrium that constitute thermodynamic equilibrium are not satisfied, the system is said to be in a nonequilibrium state. Thus, when there is an unbalanced force or torque in the interior of a system, or between a system and its surroundings, the following phenomena may take place: acceleration, turbulence, eddies, waves, etc. While such phenomena are in progress, a system passes through nonequilibrium states. If an attempt is made to give a macroscopic description of any one of these nonequilibrium states, it is found that the pressure varies from one part of a system to another. There is no single pressure that refers to the system as a whole. Similarly, in the case of a system at a different temperature from its surroundings, a nonuniform temperature distribution is set up and there is no single temperature that refers to the system as a whole. Therefore, we conclude that when the conditions for mechanical and thermal equilibrium are not satisfied, the states traversed by a system cannot be described in terms of thermodynamic coordinates referring to the system as a whole.  

It must not be concluded, however, that we are entirely helpless in dealing with such nonequilibrium states. If we divide the system into a large number of small mass elements, then thermodynamic coordinates may be found in terms of which a macroscopic description of each mass element may be approximated. There are also special methods for dealing with systems in mechanical and thermal equilibrium but not in chemical equilibrium. All these special methods will be considered later. At present, we shall deal exclusively with systems in thermodynamic equilibrium.

===== Page 53 =====

2.2 EQUATION OF STATE  

Imagine, for the sake of simplicity, a constant mass of gas, that is, a closed system, in a vessel so equipped that the pressure, volume, and temperature may be easily measured. If
===== Page 89 =====

 FIGURE 3-8 (a) A composite system composed of two cylinders separated from each other by a rigid diathermic wall. The two gas- filled chambers may be connected to a series of different heat reservoirs that hold the composite system at the same temperature as the reservoir. The thermodynamic coordinates are \(P, V, P', V'\), and \(T\). (b) A graph of the independent coordinates \(V, V'\), and \(T\).  

ensures that both parts have the same temperature. There are five thermodynamic coordinates \((P, V, P', V',\) and \(T)\) and two equations of state, one for each of the simple systems. Consequently, only three of the five coordinates are independent. In any small displacement of each piston, the work is  

\[
\mathrm{d}W = -P d V - P' d V'.
\]

The most convenient diagram to use in demonstrating the features of this system is a three- dimensional diagram with \(T, V,\) and \(V^{\prime}\) plotted along rectangular axes, as shown in Fig. 3- 8(b). A typical isothermal process would be a curve on a plane such as the one marked for constant temperature \((T = \mathrm{const.})\) . A curve on a plane for constant volume, such as that marked \(V = \mathrm{const.}\) , would represent a process in which no work is done by the lefthand part. The points \(a\) and \(b\) lie on a vertical line, every point of which refers to a constant \(V\) and \(V^{\prime}\) . Therefore, the straight line \(ab\) represents a process in which no work is done by the composite system.  

Two simple systems do not have to be separated spatially by a diathermic wall in order to have two equations of state and a common temperature. Consider an ideal paramagnetic gas, such as oxygen at low pressures, as depicted schematically in Fig. 3- 9(a). The oxygen may have its pressure \(P\) and volume \(V\) varied with the aid of a piston- cylinder combination, and it is immersed in a magnetic field, which may be changed by varying the current in the surrounding solenoid. The gas is kept at a uniform temperature \(T\) . The coordinates are \(P, V, \mu_0 \mathcal{H}, \mathcal{M}\) , and \(T\) , only three of which are independent because of the two equations of state: the ideal- gas equation \(PV = nRT\) and

===== Page 90 =====

68 PART I: Fundamental Concepts  

FIGURE 3-9 (a) A composite system composed of gas that is also paramagnetic. The gas may be connected to different heat reservoirs that hold the composite system at the same temperature as the reservoir. The thermodynamic coordinates are \(P, V, \mu_0 \mathcal{H}, \mathcal{M},\) and \(T\) . (b) A graph of the independent coordinates \(V, \mathcal{M},\) and \(T\) .  

Curie's law \(\mathcal{M} = C_{\mathcal{C}} \mathcal{H} / T\) . Since the work done in any infinitesimal process is  

\[
\mathrm{d}W = -P d V + \mu_0 \mathcal{H} d \mathcal{M},
\]

the most convenient independent coordinates are \(T, V,\) and \(\mathcal{M},\) which are plotted along rectangular axes in Fig. 3- 9(b). Any vertical line would represent a process in which no work is done.  

In general, a five- coordinate system using \(Y, X, Y', X',\) and \(T\) as coordinates has work expressed as  

\[
\mathrm{d}W = Y d X + Y' d X'.
\]

The most convenient coordinates of this system are \(T, X,\) and \(X'\) .  

## PROBLEMS  

3.1. A thin-walled metal container of volume \(V\) contains a gas at high pressure. Connected to the container is a capillary tube and stopcock. When the stopcock is opened slightly, the gas leaks slowly into a cylinder equipped with a nonleaking, frictionless piston, where the pressure remains constant at the atmospheric value \(P_0\) . (a) Show that, after as much gas as possible has leaked out, an amount of work  

\[
W = -P_0(V_0 - V)
\]

 has been done, where \(V_{0}\) is the volume of the gas at atmospheric pressure and temperature.  

(b) How much work would be done if the gas leaked directly into the atmosphere?  

3.2. (a) Show that the work done by an ideal gas during the quasi- static, isothermal expansion from an initial pressure \(P_{i}\) to a final pressure \(P_{f}\) is given by  

\[
W = nRT\ln \frac{P_{f}}{P_{i}}.
\]

(b) Calculate the work done when the pressure of 1 mol of an ideal gas is decreased quasi-statically from 20 to 1 atm, the temperature remaining constant at \(20^{\circ}\mathrm{C}\) \((R = 8.31\mathrm{J / mol}\cdot \mathrm{deg})\) .  

3.3. An adiabatic chamber with rigid walls consists of two compartments, one containing a gas and the other evacuated; the partition between the two compartments is suddenly removed. Is the work done during an infinitesimal portion of this process (called an adiabatic free expansion) equal to \(P d V\) ?  

3.4. (a) Calculate the work done upon expansion of 1 mol of gas quasi- statically and isothermally from volume \(v_{i}\) to a volume \(v_{f}\) , when the equation of state is  

\[
\left(P + \frac{a}{v^{2}}\right)\left(v - b\right) = RT,
\]

where \(a\) and \(b\) are the van der Waals constants.  

(b) If \(a = 1.4\times 10^{9}\mathrm{N}\cdot \mathrm{m}^{4} / \mathrm{mol}\) and \(b = 3.2\times 10^{-5}\mathrm{m}^{3} / \mathrm{mol}\) , how much work is done when the gas expands from a volume of 10 liters to a volume of 22.4 liters at \(20^{\circ}\mathrm{C}\) ?  

3.5. During a quasi- static expansion of a gas in an adiabatic container, the pressure at any moment is given by the equation  

\[
P V^{\gamma} = K,
\]

where \(\gamma\) and \(K\) are constants. Show that the work done in expanding from a state \((P_{i},V_{i})\) to a state \((P_{f},V_{f})\) is  

\[
W = -\frac{P_{i}V_{i} - P_{f}V_{f}}{\gamma - 1}.
\]

If the initial pressure and volume are \(10^{6}\mathrm{Pa}\) and \(10^{- 3}\mathrm{m}^{3}\) , respectively, and the final values are \(2\times 10^{5}\mathrm{Pa}\) and \(3.16\times 10^{- 3}\mathrm{m}^{3}\) , respectively, how much work is done on a gas having \(\gamma = 1.4?\)  

3.6. A stationary vertical cylinder, closed at the top, contains a gas whose volume may be changed with the aid of a heavy, frictionless piston of weight \(w\) .  

(a) How much work is done by the external force in compressing the gas by an amount \(d V\) by raising the piston a distance \(d y\) ?  

(b) If this device is used as part of an engine, what expression is appropriate to calculate the net work delivered to or received from the surroundings?  

(c) If this device is used only to produce temperature changes of the gas, what expression for work would be appropriate?

===== Page 92 =====

3.7. The pressure on \(100\mathrm{g}\) of nickel is increased quasi- statically and isothermally from 0 to \(500\mathrm{atm}\) . Assuming the density and isothermal compressibility to remain constant at values of \(8.90\times 10^{3}\mathrm{kg / m^{3}}\) and \(6.75\times 10^{- 12}\mathrm{Pa}^{- 1}\) , respectively, calculate the work.  

3.8. (a) The tension in a wire is increased quasi- statically and isothermally from \(\mathcal{F}_{i}\) to \(\mathcal{F}_{f}\) . If the length, cross- sectional area, and isothermal Young's modulus of the wire remain practically constant, show that the work done is  

\[
W = \frac{L}{2AT}\left(\mathcal{F}_{f}^{2} - \mathcal{F}_{i}^{2}\right).
\]

(b) The tension in a copper wire \(1\mathrm{m}\) long and \(0.001\mathrm{cm}^{2}\) in area is increased quasi- statically and isothermally at \(20^{\circ}\mathrm{C}\) from 10 to \(100\mathrm{N}\) . How much work is done if the isothermal Young's modulus at \(20^{\circ}\mathrm{C}\) is \(1.23\times 10^{11}\mathrm{N / m^{2}}\) ?  

3.9. The equation of state of an ideal elastic substance is  

\[
\mathcal{F} = KT\left(\frac{L}{L_0} -\frac{L_0^2}{L^2}\right),
\]

where \(K\) is a constant and \(L_{0}\) (the value of \(L\) at zero tension) is a function of temperature only. Calculate the work necessary to compress the substance from \(L = L_{0}\) to \(L = L_{0} / 2\) quasi- statically and isothermally.  

3.10. Show that the work required to blow a spherical soap bubble of radius \(r\) in an isothermal, quasi- static process in the atmosphere is equal to \(8\pi \gamma r^{2}\) .  

3.11. An electrochemical cell, in which the reaction  

\[
\mathrm{Cu} + \mathrm{Hg}_{2}\mathrm{SO}_{4}\rightarrow 2\mathrm{Hg} + \mathrm{CuSO}_{4}
\]

takes place, is connected to a motor having a back emf only slightly smaller than the emf of the cell. The emf of this cell is given by Eq. (2.14), with \(\mathcal{E}_{20} = 0.3497\mathrm{V}\) , \(\alpha = - 6.35\times 10^{- 4}\mathrm{V / deg}\) , \(\beta = - 2.4\times 10^{- 6}\mathrm{V / deg}^{2}\) , and \(\gamma = 0\) . If the cell is kept at a constant temperature of \(25^{\circ}\mathrm{C}\) and \(0.1\mathrm{mol}\) of copper reacts, then how much work is done on the motor?  

3.12. A dielectric has an equation of state \(\mathcal{P} = \chi EV\) , where \(\chi\) is a function of temperature only. Show that the work done in an isothermal, quasi- static change of state is given by  

\[
W = \frac{1}{2V\chi}\left(\mathcal{P}_{f}^{2} - \mathcal{P}_{i}^{2}\right) = \frac{V\chi}{2}\left(E_{f}^{2} - E_{i}^{2}\right).
\]

3.13. Prove that the work done during a quasi- static isothermal change of state of a paramagnetic substance obeying Curie's law is given by  

\[
W = \frac{\mu_{0}T}{2C_{C}}\left(\mathcal{H}_{f}^{2} - \mathcal{H}_{i}^{2}\right) = \frac{\mu_{0}C_{C}}{2T}\left(\mathcal{H}_{f}^{2} - \mathcal{H}_{i}^{2}\right),
\]

where \(C_{C}\) is the Curie constant.  

3.14. A volume of \(200\mathrm{cm}^{3}\) of a paramagnetic substance is maintained at constant temperature. The magnetic field is increased quasi- statically and isothermally from 0 to

===== Page 93 =====

10 \(^{6}\mathrm{A / m}\) . Assume the Curie law to hold and the Curie constant per unit volume to be \(1.885\mathrm{K / m^{3}}\) .  

(a) How much work would have to be done if no material were present?  

(b) How much work is done to change the total magnetization of the material when the temperature is \(300\mathrm{K}\) and when it is \(1\mathrm{K}\) ?  

(c) How much work is done to change the total magnetization by the generator supplying the current?

===== Page 94 =====

4.1 WORK AND HEAT  

It was shown in Chap. 3 how a system could be transferred from an initial to a final state by means of a quasi- static process and how the work done during the process could be calculated. There are, however, other means of changing the state of a system that do not necessarily involve the performance of work. Consider the four processes shown in Fig. 4- 1, which involve closed systems, where a closed system is a system in which no matter passes between the system and surroundings. In Fig. 4- 1(a), the system is a composite one consisting of water and a paddle wheel, which is caused to rotate and churn the water by means of a falling weight. As a result, the temperature of the water rises from room temperature to a slightly higher temperature. In Fig. 4- 1(b), the water and the resistor constitute the composite system, the electric current in the resistor being maintained by a generator turned by means of a falling weight. Again, the temperature of the water rises. In both cases, the state of the system is caused to change; and since the agency for changing the state of the system is a falling weight, both processes involve the performance of work.  

In Figs. 4- 1(c) and 4- 1(d), however, the situation is quite different. The system in both these cases is water in a diathermic container. In Fig. 4- 1(c), the system is in contact with the burning gases at a high temperature; whereas, in Fig. 4- 1(d), the system is near but not in contact with a lamp whose temperature is much higher than that of the water. In both cases, the system is caused to change, but in neither case can the agency of change be described by mechanical means.

===== Page 95 =====

 FIGURE 4- 1  

Distinction between work and heat: (a) and (b) show work being done on the system by means of a falling body, whereas (c) and (d) show heat entering the system from a hotter substance.  

The results of placing two systems at different temperatures together is one of our most familiar sensory experiences. It is well known that the final temperature reached by both systems is intermediate between the two starting temperatures. Up to the beginning of the nineteenth century, such phenomena, which comprise the subject of calorimetry, were explained by postulating the existence of a substance termed caloric, or, more commonly, heat, a supposed elastic fluid found in every body. It was believed that a body at a high temperature contained much caloric and that one at a low temperature had only a little caloric. When the two bodies were brought together, the body rich in caloric lost some to the other, and, thus, the final temperature of the two bodies was intermediate. Although we now know that heat is not a fluid whose total amount remains constant, nevertheless, there is a grain of truth in the idea that the changes occurring in Figs. 4- 1(c) and 4- 1(d) are the result of the transfer of "something" from the body at the higher temperature to the one at the lower temperature, and this "something" we call heat. Therefore, we adopt as a calorimetric definition the following: heat is that which is transferred between a system and its surroundings by virtue of a temperature difference only. Whether heat is a fluid or a form of energy cannot be decided

===== Page 96 =====

74 PART I: Fundamental Concepts  

yet, but it will be shown in Secs. 4.4 and 4.5 that heat is a form of energy. It is obvious that an adiabatic wall, commonly called a heat insulator, is impervious to heat; whereas a diathermic wall, commonly called a heat conductor, transmits heat. Notice that an adiabatic wall prevents heating from occurring, just as a rigid wall prevents the performance of work in a hydrostatic system from occurring; similarly, a diathermic wall allows heating to occur, just as a movable (or deformable) wall allows the performance of work to occur.  

It is important to observe that the decision as to whether a particular change of state is the result of work or heat requires first an unequivocal answer to these questions: "What is the system?" and "What are the surroundings?" For example, in Fig. 4- 1(b), if the resistor is regarded as the system and the water as the surroundings, then there is a process of heating done by the hotter resistor by virtue of the difference in temperature between the resistor and the water. Also, if a small part of the water is regarded as the system, with the rest of the water being the hotter surroundings, then, again, there is a process of heating. Regarding, however, the composite system comprising both the water and the resistor, we find that the surroundings do not contain any object whose temperature differs from that of the system, and, hence, no heating occurs between this composite system and its surroundings.  

### 4.2 ADIABATIC WORK  

When a closed system is completely surrounded by an adiabatic boundary, the system may still be coupled to the surroundings so that work may be done. Four examples of different systems experiencing the process of working in an adiabatic container, so- called adiabatic work, are shown in Fig. 4- 2. It was a series of experiments using a paddle wheel, like the one in Fig. 4- 1(a), that established the important fact that the state of a system may be caused to change from a given initial state to the same final state by the performance of adiabatic work only.  

Mechanical systems are not easily controlled in changing the state of a system, so let us consider a composite electrical system composed of a resistor immersed in water. The initial state \(i\) is characterized by the thermodynamic coordinates \(P_{i} = 1\) atm and \(T_{i} = 287.7 \mathrm{~K}\) (14.5°C) and the final state \(f\) is characterized by the coordinates \(P_{f} = 1\) atm and \(T_{f} = 288.7 \mathrm{~K}\) (15.5°C), as shown in Fig. 4- 3. To cause the system to proceed from \(i\) to \(f\) along path I by the performance of adiabatic work only, it would be necessary to surround the water with an adiabatic wall, keep the water at atmospheric pressure, and maintain a current in the resistor for a suitable interval of time.  

But, path I is not the only path by which the system may be changed from \(i\) to \(f\) by the performance of adiabatic work only. We might compress the water adiabatically from \(i\) to \(a\) , then use a current in a resistor from \(a\) to \(b\) , and then expand from \(b\) to \(f\) , the whole series of processes being designated by

===== Page 97 =====

 FIGURE 4- 2 Adiabatic work for different types of systems.  

path II. Or, we might make use of a similar adiabatic path III. There are an infinite number of paths by which a system may be transferred from an initial state to a final state by the performance of adiabatic work only. Although further measurements of adiabatic work along different paths between the same two states were not made after Joule's pioneering work, indirect experiments and the validity of subsequent results indicate that the adiabatic work is the same along all such paths. The generalization of this result is a restricted statement of the first law of thermodynamics:  

If a closed system is caused to change from an initial state to a final state by adiabatic means only, then the work done on the system is the same for all adiabatic paths connecting the two states.  

Whenever a quantity is known to depend only on the initial and final states, and not on the path connecting them, an important conclusion can be drawn. Recall from mechanics that, in moving an object from one point in a gravitational field to another point, in the absence of friction, the work done

===== Page 98 =====

76 PART I: Fundamental Concepts  

FIGURE 4-3  

Changing the state of a system from the initial state \(i\) to the final state \(f\) along three different adiabatic paths.  

depends only on the positions of the two points and not on the path through which the body was moved. It was concluded that, for a conservative force, there exists a function of the space coordinates of the body whose final value minus its initial value is equal to the work done. This function was called the potential- energy function. Similarly, the work done in moving an electric charge from one point in a conservative electric field to another point is also independent of the path and, therefore, is also expressible as the value of the electric potential function at the final state minus its value at the initial state. Therefore, it follows from the restricted statement of the first law of thermodynamics that there exists a function of the coordinates of a thermodynamic system whose value at the final state minus its value at the initial state is equal to the adiabatic work in going from one state to the other. This function is known as the internal- energy function.  

Denoting the internal- energy function by \(U\) , we have  

\[
W_{i\to f}(\mathrm{adiabatic}) = U_{f} - U_{i},
\]

where the signs are such that, if positive work is done on the system, \(U_{f}\) will be greater than \(U_{i}\) . It is found by experiment that it is not always possible to take a system from an initial state \(i\) to any final state \(f\) by the performance of adiabatic work only. It will be shown later, when entropy is discussed, that if \(f\) cannot be reached in this way, then it is always possible to go from \(f\) to \(i\) by adiabatic means, in which case the change in internal energy from \(i\) to \(f\) , instead of being \(+W_{i\to f}\) , is \(-W_{f\to i}\) . The importance of Eq. (4.1) is that thermodynamic work, which is generally path- dependent, becomes path- independent for an adiabatic process.

===== Page 99 =====

4.3 INTERNAL-ENERGY FUNCTION  

The physical interpretation of the difference \(U_{f} - U_{i}\) is the increase in internal energy of the system. The equality, therefore, of the increase of internal energy and the adiabatic work expresses the law of the conservation of energy. It should be emphasized, however, that Eq. (4.1) expresses more than the law of the conservation of energy. It states that there exists an energy function, whose difference between two values is the energy change of the system.  

The internal energy is a function of as many thermodynamic coordinates as are necessary to specify the state of a system. The equilibrium states of a closed hydrostatic system, which is describable by means of three thermodynamic coordinates \(P\) , \(V\) , and \(T\) , are completely determined by only two coordinates, since the third is fixed by the equation of state. Therefore, the internal energy may be thought of as a function of only two (any two) of the three thermodynamic coordinates. This is true for each of the simple systems described in Chap. 2. It is not always possible to write the internal- energy function in simple mathematical form, especially if one deals with real materials instead of ideal ones. Very often, the exact form of the function \(U\) is unknown. It must be understood, however, that it is not necessary to know the exact form of the internal- energy function, but only that such a function exists because of the results of experiments on adiabatic work.  

If the coordinates characterizing the two states differ from each other only infinitesimally, then the change of internal energy is \(dU\) , where \(dU\) is an exact differential, since it is the differential of a state function. In other words, the integral of \(dU\) is independent of the path between the initial and final states. In the case of a hydrostatic system, if \(U\) is regarded as a function of \(T\) and \(V\) , then  

\[
dU(T,V) = \left(\frac{\partial U}{\partial T}\right)_V dT + \left(\frac{\partial U}{\partial V}\right)_T dV,
\]

or, regarding \(U\) as a different function of \(T\) and \(P\) ,  

\[
dU(T,P) = \left(\frac{\partial U}{\partial T}\right)_P dT + \left(\frac{\partial U}{\partial P}\right)_T dP.
\]

Notice that the two partial derivatives \((\partial U / \partial T)_V\) and \((\partial U / \partial T)_P\) are not equal, because the function \(U\) is not the same in both cases. The first partial derivative is a function of \(T\) and \(V\) , and the second partial derivative is a function of \(T\) and \(P\) . They are different mathematically and also have different physical meanings.

===== Page 100 =====

78 PART I: Fundamental Concepts  

FIGURE 4-4 Nonadiabatic processes.  

### 4.4 MATHEMATICAL FORMULATION OF THE FIRST LAW  

We have been considering processes during which a system undergoes a change of state through the performance of adiabatic work only. Such experiments must be performed in order to measure the change in the internal- energy function of a system, but they are not the usual processes that are carried out in the laboratory. In Fig. 4- 4, there are depicted two examples of processes involving changes of state that take place nonadiabatically; specifically, with diathermic walls. In Fig. 4- 4(a), the gas is in thermal contact with a flame whose temperature is higher than that of the gas; and, at the same time, the gas is forced to contract, so diathermic work is performed on the system. In Fig. 4- 4(b), the total magnetization of a paramagnetic solid is increased while it is in contact with liquid helium, the temperature of which is lower than that of the solid. As a matter of fact, some of the helium boils away during the magnetization.  

Let us now imagine two different experiments performed on the same closed system. In one experiment, we measure the adiabatic work necessary to change the state of the system from \(i\) to \(f\) in order to obtain \(U_{f} - U_{i}\) . In the other experiment, we cause the system to undergo the same change of state, so we have the same \(U_{f} - U_{i}\) , but the process is diathermic, and we measure the diathermic work \(W\) done. The result of all such experiments is that the nonadiabatic work \(W\) is not equal to \(U_{f} - U_{i}\) . In order that this result shall be consistent with the law of the conservation of energy, we are forced to

===== Page 101 =====

 conclude that energy has been transferred by means other than the performance of work. This energy, whose transfer between the system and its surroundings is required by the law of the conservation of energy and which has taken place only by virtue of the temperature difference between the system and its surroundings, is what we previously called heat. Therefore, we give the following as our thermodynamic definition of heat: When a closed system whose surroundings are at a different temperature and on which diathermic work may be done undergoes a process, then the energy transferred by nonmechanical means, equal to the difference between the change of internal energy and the diathermic work, is called heat. Denoting heat by \(Q\) , we have  

\[
Q = (U_{f} - U_{i}) - W(\mathrm{d i a t h e r m i c}),
\]

or  

\[
\boxed{U_{f} - U_{i} = Q + W,}
\]

where the sign convention has been adopted that \(Q\) is positive when it enters a system and negative when it leaves a system. Like internal energy and work, heat is measured in joules in the SI system. Equation (4.2) is known as the mathematical formulation of the first law of thermodynamics.  

It should be emphasized that the mathematical formulation of the first law contains three related ideas: (1) the existence of an internal- energy function; (2) the principle of the conservation of energy; (3) the definition of heat as energy in transit by virtue of a temperature difference.  

It was many years before it was understood that heat is related to energy. The first really conclusive evidence that heat could not be a fluid within a body was given by Benjamin Thompson, an American from Woburn, Massachusetts, who later became Count Rumford of Bavaria. In 1798, Rumford observed the rise in temperature of the brass chips produced during the boring of a cannon, and concluded that the process of boring was responsible for the production of heat, not some inherent caloric. One year later, the English chemist Sir Humphry Davy tried to show that two pieces of ice could be melted by rubbing them together. His idea was to show that heat is a manifestation of energy, but his experiment was highly inconclusive.  

The idea that heat is a form of energy was put forward in 1839 by M. Séguin, a French engineer. In 1842, Mayer, a German physician, discovered the equivalence of heat and work and made the first announcement of the principle of the conservation of energy (the first law of thermodynamics). No conclusive experiments were performed by either Séguin or Mayer. It remained for Joule, an Englishman with a private laboratory, in the period from 1840 to 1849, to convince the world by performing a series of admirable experiments, in which brass paddle wheels were turned steadily by slowly falling weights. Joule also performed experiments with mercury or sperm oil in place of water, and with iron paddles in place of brass paddles. He found that the performance of a definite amount of adiabatic work always produced the same change of state of the system, regardless of the material performing the work or the substance used for the system.

===== Page 102 =====

80 PART I: Fundamental Concepts  

Helmholtz, a surgeon in the Prussian army, recognized the epoch- making importance of Joule's work and wrote a brilliant paper in 1847, in which he applied Joule's ideas to the sciences of physical chemistry and physiology. William Thomson (Lord Kelvin) collaborated with Joule to refine the experiments.  

Heating is a process by which there is an exchange of energy between system and surroundings because of a difference in temperature. But what is the energy that is exchanged? The question cannot be answered until the conditions for the process of heating are determined. In any process of heating, there is always a difference in temperature across the diathermic boundary between the system and its surroundings. But, for a specific system, more conditions must be specified. For example, consider the hydrostatic system. If the diathermic boundary of a hydrostatic system is held rigid, then the volume of the system does not change and the isochoric heat transferred is simply the internal energy. If the diathermic boundary of a hydrostatic system is movable (a piston), then the pressure of the system does not change and the isobaric heat transferred is known as the enthalpy, which is another type of energy to be introduced in Chap. 10.  

### 4.5 CONCEPT OF HEAT  

Heat is either internal energy or enthalpy in transit, depending on the experimental conditions. During the process of heating, energy flows from one part of a system to another, or from one system to another, by virtue of only a temperature difference. When the flow has ceased, there is no longer any occasion to use the word heat or the symbol \(Q\) , because the process is completed. All that remains after heating has been completed is a different state of the system, that is, a new value for the internal energy or enthalpy. Consequently, it is incorrect to refer to the "heat in a body," just as it is incorrect to speak of the "work in a body." The processes of working and heating are transient activities that lead to a change of the energy found in a system. All that endures is the new state of the energy. The energy of a system cannot be separated into a mechanical part and a thermal part, just as you cannot analogously identify some water in a lake as originating from this river and other water from that rain. The river and the rain have lost their meanings, but the new water level endures.  

We have seen earlier that the work done on or by a system is not a function of the coordinates of the system, so the calculation of the work depends on the path of integration by which the system is brought from the initial to the final state. The same situation applies to the heat transferred in or out of a system. Heat \(Q\) is not a function of the thermodynamic coordinates, that is, not a state function, so the calculation of the heat depends on the path of integration. An infinitesimal amount of heat \(dQ\) , therefore, is an inexact

===== Page 103 =====

 differential and not the differential of an actual function of the thermodynamic coordinates.  

Imagine two systems: a system \(A\) in thermal contact with a system \(B\) , and the composite system is surrounded by adiabatic walls. For system \(A\) alone,  

\[
U_{f} - U_{i} = Q + W;
\]

and for system \(B\) alone,  

\[
U_{f}^{\prime} - U_{i}^{\prime} = Q^{\prime} + W^{\prime}.
\]

Adding, we get  

\[
(U_{f} + U_{f}^{\prime}) - (U_{i} + U_{i}^{\prime}) = Q + Q^{\prime} + W + W^{\prime}.
\]

Since \((U_{f} + U_{f}^{\prime}) - (U_{i} + U_{i}^{\prime})\) is the change in energy of the composite system and \(W + W^{\prime}\) is the work done on the composite system, it follows that \(Q + Q^{\prime}\) is the heat transferred to the composite system. Since the composite system is surrounded by adiabatic walls,  

\[
Q + Q^{\prime} = 0,
\]

and  

\[
Q = -Q^{\prime}. \quad (4.3)
\]

In other words, within an adiabatic boundary, the heat lost (or gained) by system \(A\) is equal to the heat gained (or lost) by system \(B\) . Equation (4.3) is the basis of calculations of the intermediate temperature after a piece of hot metal has been dropped into a sample of cold water contained in a calorimeter. One is allowed to consider the quantity of heat to be conserved within the adiabatic container, but heat is generally not a conserved quantity, as Rumford's experiments showed.  

### 4.6 DIFFERENTIAL FORM OF THE FIRST LAW  

A process involving only infinitesimal changes in the thermodynamic coordinates of a system is known as an infinitesimal process. For such a process, the general statement of the first law becomes  

\[
dU = dQ + dW. \quad (4.4)
\]

If the infinitesimal process is quasi- static, then \(dU\) and \(dW\) can be expressed in terms of thermodynamic coordinates only. An infinitesimal quasi- static process is one in which the system passes slowly from an initial equilibrium state to a neighboring equilibrium state.  

Equation (4.4) shows that the exact differential \(dU\) is the sum of two inexact differentials, \(dQ\) and \(dW\) . It is surprising that the inexactness of the right side of the equation is not found on the left side. It should be recognized that \(dU\) refers to a property within the system (internal energy), whereas \(dQ\)

===== Page 104 =====

82 PART I: Fundamental Concepts  

TABLE 4.1 The first law for simple systems   

Simple systemFirst lawU is a function of any two ofHydrostatic systemdU = dQ - PdVP, V, TStretched wiredU = dQ + JdLJ, L, TSurfacedU = dQ + γdAγ, A, TElectrochemical celldU = dQ + δdZδ, Z, TDielectric slabdU = dQ + EdPE, P, TParamagnetic roddU = dQ + μ0γdMμ0γ, M, T  

and \(\mathrm{d}W\) are not related to properties of the system; rather, they refer to the surroundings, where the surroundings interact with the system by means of processes of transferring energy. The quantity \(\mathrm{d}W\) was found in the last chapter to be expressible in terms of the product of an intensive generalized force and an extensive generalized displacement, as shown in Table 3.1. But, the quantity \(\mathrm{d}Q\) itself is not yet expressed in terms of thermodynamic (system) coordinates only. In this chapter, we begin the task of expressing heat in terms of system coordinates by introducing the quantity known as heat capacity of the system. After the second law of thermodynamics and the concept of entropy have been introduced in Chap. 8, we shall complete the discussion of heat and find that the first law can be written completely in terms of coordinates appropriate to the system only.  

For an infinitesimal quasi- static process of a hydrostatic system, the first law can be written  

\[
\mathrm{d}Q = dU + PdV, \quad (4.5)
\]

where \(U\) is a function of any two of the three thermodynamic coordinates \(P\) , \(V\) , and \(T\) . The pressure \(P\) is, of course, a function of \(V\) and \(T\) from the equation of state. Notice that for a process restricted to constant volume, \(\mathrm{d}Q = dU|_{V}\) , that is, heat is the flow of internal energy in an isochoric process. A similar equation may be written for each of the other simple systems, as shown in Table 4.1.  

To deal with more complicated systems, it is merely necessary to replace \(\mathrm{d}W\) in the first law by two or more expressions. For example, in the case of a composite system consisting of two hydrostatic parts separated by a diathermic wall, we may express \(\mathrm{d}Q\) as follows:  

\[
\mathrm{d}Q = dU + PdV + P'dV', \quad (4.6)
\]

and \(U\) is a function of three of the variables \(P\) , \(V\) , \(P'\) , \(V'\) , and \(T\) . In the case of a paramagnetic gas,  

\[
\mathrm{d}Q = dU + PdV - \mu_0\gamma \mathcal{K}d\mathcal{M}, \quad (4.7)
\]

and \(U\) is a function of three of the coordinates \(P\) , \(V\) , \(\mu_0\gamma \mathcal{K}\) , \(\mathcal{M}\) , and \(T\) .

===== Page 105 =====

4.7 HEAT CAPACITY AND ITS MEASUREMENT  

Equation (4.2) shows that the internal energy can be changed either by heat or work. As a practical matter, it is much easier to produce heat from combustion or electricity passing through a resistor than it is to produce work from falling weights or compressed springs. As a result, when systematic experiments were performed to measure the capability of a substance to store internal energy, heat rather than work was used, and the results came to be known as the heat capacity of the sample. The term "heat capacity" implies that a substance can hold heat, which is completely false. Heat is not a function of the thermodynamic state of a system; internal energy is! The proper expression should be internal energy capacity, but too much data have been gathered and too many books have been written to make this correction, so we are forced to use the oxymoron: heat capacity.  

When heat is absorbed by a system, a change of temperature may or may not take place, depending on the state of the system. For example, a material at its melting temperature experiences no change of temperature when it is heated but a material at less than its melting temperature becomes hotter. If a system experiences a change of temperature from \(T_{i}\) to \(T_{f}\) during the transfer of \(Q\) units of heat, the average heat capacity of the system is defined as the ratio:  

\[
\text{Average heat capacity} = \frac{Q}{T_{f} - T_{i}}.
\]

As both \(Q\) and \((T_{f} - T_{i})\) become smaller, this ratio approaches a limiting value, known as the heat capacity \(C\) , thus:  

\[
C = \lim_{T_{f}\to T_{i}}\frac{Q}{T_{f} - T_{i}},
\]

or, at temperature \(T_{i}\)  

\[
C = \frac{\mathrm{d}Q}{\mathrm{d}T}. \quad (4.8)
\]

where heat capacity is measured in joules per kelvin (J/K) in SI units. Notice that the right side of Eq. (4.8) is not a derivative of a function, but, rather, the ratio of two small experimental quantities \(\mathrm{d}Q\) and \(dT\) .  

In dealing with extensive quantities (see Sec. 2.10), such as volume or internal energy, the mass of the system or sample affects the magnitude of the variable. Standardization occurs when an extensive quantity is divided by the mass of an arbitrary sample, resulting in the volume per unit mass or the internal energy per unit mass. These quantities are called specific quantities, the adjective "specific" meaning "per unit mass." Heat capacity is an extensive quantity, and the "specific heat capacity," abbreviated as "specific heat," is an intensive quantity measured in joules per kilogram- kelvin (J/kg·K). When the specific heat capacities of different substances are compared, no

===== Page 106 =====

84 PART I: Fundamental Concepts  

interesting regularities appear. When, however, the heat capacities are standardized to the same amount of substance (a different mass for each different substance) called a mole, wonderful regularities (to be explained in Sec. 9.5) occur.  

A mole (abbreviated "mol") is defined as the amount of substance that contains as many elementary entities (atoms, molecules, ions, electrons, other particles) as there are atoms in \(0.012\mathrm{kg}\) of \(^{12}\mathrm{C}\) . This number of atoms of \(^{12}\mathrm{C}\) is called Avogadro's number \(N_{\mathrm{A}}\) and is equal to \(6.022\times 10^{23}\) particles per mole. If the mass of an atom is \(m\) , then the mass of a mole of atoms is \(mN_{\mathrm{A}}\) . This quantity, the molar mass, has also been called the "molecular weight." Designating the molar mass by \(M\) , we have  

\[
M = mN_{\mathrm{A}},
\]

and the number of moles \(n\) is given by  

\[
n = \frac{\text{total mass}}{M}.
\]

If \(C\) is the heat capacity of \(n\) moles, then the molar heat capacity \(c\) is given by  

\[
c = \frac{C}{n} = \frac{1}{n}\frac{\mathrm{d}Q}{\mathrm{d}T}
\]

and is measured in units of joules per mole- kelvin \((\mathrm{J / mol}\cdot \mathrm{K})\) . Both the specific heat and the molar heat capacity are expressed as lower- case \(c\) , whereas the heat capacity of an arbitrary sample is expressed as capital \(C\) . All three quantities are state functions, because they are a measure of the change of internal energy in an isochoric process.  

The heat capacity may be negative, zero, positive, or infinite, depending on the process the system undergoes during the heat transfer. Heat capacity has a definite value only for a definite process. In the case of a hydrostatic system, the ratio \(\mathrm{d}Q / dT\) has a unique value each time a measurement is made while the pressure is held constant. Under these conditions, \(C\) is called the heat capacity at constant pressure and is denoted by the symbol \(C_{P}\) , where  

\[
C_{P} = \left(\frac{\mathrm{d}Q}{\mathrm{d}T}\right)_{P}. \quad (4.9)
\]

In general, \(C_{P}\) is a function of \(P\) and \(T\) . Similarly, the heat capacity at constant volume is the result of taking data while the volume is held constant; thus,  

\[
C_{V} = \left(\frac{\mathrm{d}Q}{\mathrm{d}T}\right)_{V}, \quad (4.10)
\]

and depends on both \(V\) and \(T\) . In general, \(C_{P}\) and \(C_{V}\) are different. Both will be thoroughly discussed throughout this book. Each simple system has its own heat capacities as shown in Table 4.2.  

Each heat capacity of a simple system is a function of two variables. Within a small range of variation of these coordinates, however, the heat capacity may be regarded as practically constant. Very often, one heat capa

===== Page 107 =====

 TABLE 4.2 Heat capacities of simple systems   

Simple systemHeat capacitySymbolHydrostatic systemAt constant pressureCpAt constant volumeCVStretched wireAt constant tensionCgAt constant lengthCLSurfaceAt constant surface tensionCγAt constant areaCAElectrochemical cellAt constant emfCgAt constant chargeCgDielectric slabAt constant electric fieldCEAt constant total polarizationCpParamagnetic rodAt constant magnetic fieldCgAt constant total magnetizationCm  

city can be set equal to another without much error. Thus, the \(C_{\mathcal{K}}\) of a paramagnetic solid is in many situations very nearly equal to \(C_{P}\) .  

The measurement of the heat capacity of solids was one of the most important experimental projects of physics at the beginning of the twentieth century, because numerical values of heat capacity provide one of the most direct means of assessing the validity of the assumptions used in statistical mechanics. An electrical method of measurement of heat capacities is used almost invariably. If a resistance wire is wound around a cylindrical sample of material and if both the wire and the sample are regarded as the system, then the electrical energy dissipated in the wire is interpreted as work. When the wire is not included as part of the system, however, the energy which is dissipated within the wire and which flows into the sample by virtue of the temperature difference between the wire and the sample (however small) is designated as heat. The wire is often called a heating coil. If the current in the wire is \(I\) and the potential difference across it is \(\mathcal{E}\) , then the heat \(dQ\) that leaves the heating coil over a time \(dt\) is  

\[
\mathrm{d}Q = \mathcal{E}I\mathrm{d}t.
\]

If \(\mathcal{E}\) is measured in volts, \(I\) in amperes, and \(t\) in seconds, the heat will be expressed in joules. The shape, size, and construction of the calorimeter (the container of the system), heating coils, thermometers, etc., depend on the nature of the material to be studied and the temperature range desired. It is impossible to describe one calorimeter that suffices for all purposes.  

In modern calorimetry, particularly in the case of solids at low temperatures, the sample is suspended in a highly evacuated space by means of fine threads of nylon or some other poorly conducting material. A heating coil is wound around the sample, and a thermocouple or a resistance thermometer (platinum, carbon, or germanium, depending on the temperature range) is

===== Page 108 =====

86 PART I: Fundamental Concepts  

FIGURE 4-5 Temperature as a function of time in the measurement of heat capacity.  

placed in a small hole drilled for that purpose. The connecting wires for the heater, for the current in the thermometer, and for the potential difference across the thermometer are made very thin so as not to allow much heat to be transferred between the sample and its surroundings through the connecting wires. The temperature of the sample is measured as a function of the time; when plotted as in Fig. 4- 5, this gives the line \(AB\) , marked "foreperiod." At the time corresponding to point \(B\) , a switch is closed and a current is established in the heater at the same moment that an electronic timer is started. After a short interval of time \(\Delta t\) , the switch is opened and the timer is stopped. Then, the temperature is again measured as a function of time and is plotted as the line \(DE\) , marked "afterperiod" in Fig. 4- 5.  

As a rule, no reading of temperature or time is attempted while the timer is on, that is, from \(B\) to \(D\) . A vertical line is drawn through the center \(C\) of the line \(BD\) , and both the foreperiod and the afterperiod lines are extrapolated to this vertical line, giving the points \(F\) and \(G\) , as shown. The molar heat capacity \(c_{P}\) at the temperature corresponding to point \(C\) is then given by  

\[
c_{P} = \frac{\mathcal{E}I\Delta t}{n\Delta T}.
\]

Sometimes \(\Delta T\) is made as small as 0.001 deg. Strictly speaking, the graph shown in Fig. 4- 5 is not a graph of temperature \(T\) vs. time \(t\) , but of the resistance \(R'\) of the resistance thermometer vs. time \(t\) . Typically, the entire \(R'(t)\) curve is digitized and the molar heat capacities are calculated by computer.

===== Page 109 =====

4.8 SPECIFIC HEAT OF WATER; THE CALORIE  

When the subject of calorimetry was developed in the middle of the eighteenth century, measurements were confined to the temperature range between the freezing and boiling points of water. The unit of heat found most convenient was called the calorie (abbreviation cal) and was defined as the amount of heat required to raise the temperature by \(1^{\circ}C\) in a system of \(1\mathrm{g}\) of water. To measure the amount of heat transferred from the surroundings to the sample of water, it was necessary merely to make two measurements: the mass of water and change of temperature of the water. Later, as measurements became more precise and corrections were made, it was discovered that the heat necessary to change \(1\mathrm{g}\) of water from 0 to \(1^{\circ}C\) was different from the heat required to go from, say, 30 to \(31^{\circ}C\) . The calorie was then defined to be the heat needed to go from 14.5 to \(15.5^{\circ}C\) (the "15- degree calorie").  

The amount of work that had to be dissipated in water — either by maintaining a current in a resistor immersed in water or by churning the water in an irregular manner — per unit mass of water in going from 14.5 to \(15.5^{\circ}C\) was called the mechanical equivalent of heat, which was measured to be 4.1860 J/cal. In the 1920s, it was recognized that the measurement of this mechanical equivalent of heat was really a measurement of the specific heat of water, with the joule as the unit of heat. Since heat is a form of energy and the joule is the universal unit of energy, the calorie became superfluous. Among physicists and chemists today, the calorie has been dropped, and all thermal quantities are expressed in joules. There is no mechanical equivalent of heat, but instead there is the specific heat of water, whose temperature variation in the range of 0 to \(100^{\circ}C\) is shown in Fig. 4- 6.  

FIGURE 4-6 Specific heat of water at constant atmospheric pressure.

===== Page 110 =====

4.9 EQUATIONS FOR A HYDROSTATIC SYSTEM  

The mathematical formulation of the first law for a hydrostatic system is  

\[
\mathrm{d}Q = dU + P dV,
\]

where \(U\) is a function of any two of \(P, V\) , and \(T\) . Choosing \(T\) and \(V\) , we have  

\[
dU = \left(\frac{\partial U}{\partial T}\right)_V dT + \left(\frac{\partial U}{\partial V}\right)_T dV.
\]

Therefore, the first law becomes  

\[
\mathrm{d}Q = \left(\frac{\partial U}{\partial T}\right)_V dT + \left[\left(\frac{\partial U}{\partial V}\right)_T + P\right]dV. \quad (4.11)
\]

Dividing by \(dT\) , we get  

\[
\frac{\mathrm{d}Q}{dT} = \left(\frac{\partial U}{\partial T}\right)_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + P\right]\frac{dV}{dT}. \quad (4.12)
\]

This equation is true for any process involving any temperature change \(dT\) and any volume change \(dV\) .  

1. If \(V\) is constant, then \(dV = 0\) , and  

\[
\left(\frac{\mathrm{d}Q}{\mathrm{d}T}\right)_V = \left(\frac{\partial U}{\partial T}\right)_V.
\]

Notice that the term on the left is an experimental quantity — the measurement of a small amount of heat transferred due to a small difference in temperature between the system and the surroundings during a process in which the volume of the system is held constant. The term on the right is the derivative of the internal- energy function with respect to temperature while the variable volume is held constant during the differentiation.  

The term on the left, by definition, is the heat capacity at constant volume \(C_V\) ; therefore,  

\[
C_V = \left(\frac{\partial U}{\partial T}\right)_V. \quad (4.13)
\]

The importance of Eq. (4.13) is that an experimental quantity on the left side of the equation is related to a partial derivative of thermodynamic coordinates on the right side. For example, if \(U\) is calculated from first principles by making special assumptions about the atoms or molecules of a particular material, then one of the first methods of checking these assumptions is to differentiate \(U\) with respect to \(T\) at constant \(V\) and to compare the resulting quantity with the experimentally measured value of \(C_V\) . However, the measurement of \(C_V\) can be very difficult, because the

===== Page 111 =====

 volume must be held fixed while the temperature is being raised. Recall, in Sec. 2.4, the pressure needed to hold a sample of mercury at constant volume for a temperature increase of only \(10^{\circ} \mathrm{C}\) .  

2. If \(P\) is constant, then Eq. (4.12) becomes  

\[
\left(\frac{\mathrm{d}Q}{\mathrm{d}T}\right)_{P} = \left(\frac{\partial U}{\partial T}\right)_{V} + \left[\left(\frac{\partial U}{\partial V}\right)_{T} + P\right]\left(\frac{\partial V}{\partial T}\right)_{P}.
\]

But, by definition \(\left(\mathrm{d}Q / dT\right)_{P} = C_{P}\) and also \(\left(\partial V / \partial T\right)_{P} = V\beta\) from Eq. (2.3). Hence,  

\[
C_{P} = C_{V} + \left[\left(\frac{\partial U}{\partial V}\right)_{T} + P\right]V\beta ,
\]

or  

\[
\left(\frac{\partial U}{\partial V}\right)_{T} = \frac{C_{P} - C_{V}}{V\beta} -P. \quad (4.14)
\]

Although this equation is not important in its present form, it is a good example of an equation that relates a quantity \(\left(\partial U / \partial V\right)_{T}\) , which is ordinarily not measured, with state functions such as \(C_{P}, C_{V}\) , and \(\beta\) , which can be measured.  

## 4.10 QUASI-STATIC FLOW OF HEAT; HEAT RESERVOIR  

It was shown in Chap. 3 that a process caused by a finite unbalanced force or torque is attended by phenomena such as acceleration or turbulence, which cannot be handled by means of thermodynamic coordinates that refer to the system as a whole. A similar situation exists when there is a finite difference between the temperature of a system and that of its surroundings. A nonuniform temperature distribution is set up in the system, and the calculation of this distribution and its variation with time is in most cases an elaborate mathematical problem. During a quasi- static process, however, the difference between the temperature of a system and that of its surroundings is infinitesimal. As a result, the temperature is at any moment uniform throughout the system, and its changes are infinitely slow. The flow of heat is also infinitely slow and may be calculated in a simple manner in terms of thermodynamic coordinates referring to the system as a whole.  

Suppose that a system is in good thermal contact with a body of extremely large mass and that a quasi- static process is performed. A finite amount of heat flow during this process will not bring about an appreciable change in the temperature of the surrounding body if the mass is large enough. For example, an ice cube of ordinary size, if thrown into the ocean, will not produce a drop in temperature of the ocean. Or, another example, the flow of heat from an ordinary campfire into the air will not produce a rise of temperature of the

===== Page 112 =====

90 PART I: Fundamental Concepts  

atmosphere. The ocean and the atmosphere are approximate examples of an ideal body called a heat reservoir. A heat reservoir is a body of such a large mass that it may absorb or reject an unlimited quantity of heat without experiencing an appreciable change in temperature or in any other thermodynamic coordinate. Do not make the mistake of concluding that there is absolutely no change in the thermodynamic coordinates of a heat reservoir when a finite amount of heat flows in or out of the reservoir. There is a change in the reservoir, but an extremely small one, too small to be measured.  

Any quasi- static process of a system in contact with a heat reservoir is bound to be isothermal. To describe a quasi- static flow of heat involving a change of temperature, one could conceive of a system placed in contact successively with a series of reservoirs. Thus, we imagine a series of reservoirs ranging in temperature from \(T_{i}\) to \(T_{f}\) placed successively in contact with a system at constant pressure in such a way that the difference in temperature between the system and the reservoir with which it is in contact is infinitesimal. The flow of heat will be quasi- static and can be calculated as follows from the definition of \(C_{P}\) :  

\[
C_{P} = \left(\frac{\mathrm{d}Q}{\mathrm{d}T}\right)_{P},
\]

and, therefore, for a quasi- static isobaric process, a path of integration is prescribed, so  

\[
Q_{P} = \int_{T_{i}}^{T_{f}}C_{P}dT. \quad (4.15)
\]

For example, the heat absorbed by water from a series of reservoirs varying in temperature from \(T_{i}\) to \(T_{f}\) during a quasi- static isobaric process is calculated from Eq. (4.15). Assume \(C_{P}\) remains practically constant, integrate, and then  

\[
Q_{P} = C_{P}(T_{f} - T_{i}).
\]

For a quasi- static isochoric process, another path of integration is prescribed, so  

\[
Q_{V} = \int_{T_{i}}^{T_{f}}C_{V}dT. \quad (4.16)
\]

Similar considerations hold for other systems during quasi- static processes.  

## 4.11 HEAT CONDUCTION  

When two parts of a material substance are maintained at different temperatures and the temperature of each small volume element of the intervening substance is measured, experiment shows a continuous distribution of tem

===== Page 113 =====

 CHAPTER 4: Heat and the First Law of Thermodynamics 91  

perature. The transport of energy between neighboring volume elements by virtue of the temperature difference between them is known as heat conduction. The fundamental law of heat conduction is a generalization of the results of experiments on the linear flow of heat through a slab perpendicular to the faces. A piece of material is made in the form of a slab of thickness \(\Delta x\) and of area \(A\) . One face is maintained at the temperature \(T\) and the other at \(T + \Delta T\) . The heat \(Q\) that flows perpendicular to the faces for a time \(t\) is measured. The experiment is repeated with other slabs of the same material but with different values of \(\Delta x\) and \(A\) . The results of such experiments show that, for a given value of \(\Delta T\) , the conducted heat \(Q\) is proportional to the time and to the area. Also, for a given time and area, \(Q\) is proportional to the ratio \(\Delta T / \Delta x\) , provided that both \(\Delta T\) and \(\Delta x\) are small. These results may be written  

\[
\frac{Q}{t}\propto A\frac{\Delta T}{\Delta x},
\]

which is only approximately true when \(\Delta T\) and \(\Delta x\) are finite but which is rigorously true in the limit as \(\Delta T\) and \(\Delta x\) approach zero. If we generalize this result for an infinitesimal slab of thickness \(dx\) , across which there is a temperature difference \(dT\) , and introduce a constant of proportionality \(K\) , the fundamental law of heat conduction becomes  

\[
\frac{\mathrm{d}Q}{dt} = -KA\frac{dT}{dx}. \quad (4.17)
\]

The derivative \(dT / dx\) is called the temperature gradient. The minus sign is introduced in order that the positive direction of the flow of heat should coincide with the positive direction of \(x\) . For heat to flow in the positive direction of \(x\) , this must be the direction in which temperature \(T\) decreases. The letter \(K\) is called the thermal conductivity. A substance with a large thermal conductivity is known as a thermal conductor and one with a small value of \(K\) as a thermal insulator. It will be shown in the next section that the numerical value of \(K\) depends upon a number of factors, one of which is the temperature. Volume elements of a conducting material may, therefore, differ in thermal conductivity. If the temperature difference between parts of a substance is small, however, \(K\) can be considered practically constant throughout the substance. This simplification is usually made in practical problems.  

### 4.12 THERMAL CONDUCTIVITY AND ITS MEASUREMENT  

When the substance to be investigated is a metal, it is made into the form of a bar, and one end is heated electrically while the other end is cooled with a stream of water. The surface of the bar is thermally insulated, and the heat loss through the insulation is calculated by subtracting the rate at which heat

===== Page 114 =====

92 PART I: Fundamental Concepts  

enters the water from the rate at which electrical energy is supplied. In the case of most metals, the heat lost from the surface is very small in comparison with that which flows through the bar. The temperature is measured with suitable thermocouples at two places a distance \(L\) apart, and the equation  

\[
K = \frac{L}{A(T_1 - T_2)}\frac{\mathrm{d}Q}{\mathrm{d}t}
\]

is used to determine the average thermal conductivity within the given temperature range. If \(T_{1} - T_{2}\) is small, \(K\) is practically equal to the thermal conductivity at the mean temperature. \(K\) has units of watts per meter- kelvin \(\mathrm{(W / m\cdot K)}\) .  

When the substance to be investigated is a nonmetal, it is made into the form of a thin disk or plate, and the same general method is used. The substance is contained between two copper blocks, one of which is heated electrically and the other cooled by running water. In most cases, the rate at which heat is supplied is almost equal to the rate at which heat enters the water, showing that there is little loss of heat through the edges.  

Experiments show that the thermal conductivity of a metal is quite sensitive to impurities. The slightest trace of arsenic in copper reduces the thermal conductivity by a factor of 3. A change in internal structure brought about by continued heating or a large increase in pressure also affects the value of \(K\) . No appreciable change in the \(K\) of solids and liquids takes place, however, under moderate changes of pressure. Liquefaction always produces a decrease in the thermal conductivity, and the thermal conductivity of a liquid usually increases as the temperature is raised. Nonmetallic solids behave in a manner similar to that of liquids. At room temperature, these are poor conductors of heat; in general, the thermal conductivity decreases as the temperature is raised. In the low- temperature range, however, the behavior is quite different, as shown in Fig. 4- 7, where it may be seen that the thermal conductivity of sapphire rises to a maximum of approximately \(6000 \mathrm{W / m \cdot K}\) at \(35 \mathrm{K}\) (about 15 times the conductivity of silver at room temperature). The thermal conductivity of some metals remains quite constant over a wide temperature range. Thus, silver, copper, and gold have thermal conductivities that remain practically constant in the temperature range from 100 to \(1000 \mathrm{K}\) . As a general rule, the thermal conductivity of metals increases as the temperature is lowered, until a maximum is reached. Further reduction of temperature causes a decrease toward zero, as shown in the case of copper in Fig. 4- 7.  

Gases are by far the poorest heat conductors. At pressures above a certain value, depending on the nature of the gas and the dimensions of the containing vessel, the thermal conductivity is independent of the pressure. Under the usual laboratory conditions, this limiting pressure is considerably below atmospheric pressure. The thermal conductivity of a gas always increases as the temperature is raised, as indicated by He (gas) in Fig. 4- 7.

===== Page 115 =====

 FIGURE 4-7  Typical curves showing temperature dependence of thermal conductivity.  

### 4.13 HEAT CONVECTION  

A flow of liquid or gas that absorbs heat at one place and then moves to another place, where it mixes with a cooler portion of the fluid and rejects heat, is called a convection current. If the motion of the fluid is caused by a difference in density that accompanies a temperature difference, the phenomenon is called natural convection. If the fluid is made to move by the action of a pump or a fan, it is called forced convection.  

Consider a fluid in contact with a flat or curved wall whose temperature is higher than that of the main body of the fluid. Although the fluid may be in notion, there is a relatively thin layer of stagnant fluid next to the wall, the thickness of the layer depending upon the character of the motion of the main body of fluid. The more turbulent the motion, the thinner the layer. Heat is transferred from the wall to the fluid by a combination of conduction through the layer and convection in the fluid. Neglecting the transfer of heat by radiation (which will be taken into account in Sec. 4.15), we may define a convection

===== Page 116 =====

94 PART I: Fundamental Concepts  

coefficient \(h\) that includes the combined effect of conduction through the layer and convection in the fluid. Thus,  

\[
\frac{\mathrm{d}Q}{dt} = hA\Delta T, \quad (4.18)
\]

where \(A\) is the area of the wall, and \(\Delta T\) is the temperature difference between the surface of the wall and the main body of the fluid. The fundamental problem of heat convection is to find the value of \(h\) that is appropriate to a particular piece of equipment.  

Experiment shows that the convection coefficient depends on the following factors:  

1. Whether the wall is flat or curved. 
2. Whether the wall is horizontal or vertical. 
3. Whether the fluid in contact with the wall is a gas or a liquid. 
4. The density, viscosity, specific heat, and thermal conductivity of the fluid. 
5. Whether the speed of the fluid is small enough to give rise to laminar flow or large enough to cause turbulent flow. 
6. Whether evaporation, condensation, or formation of scale takes place.  

Since the physical properties of the fluid depend upon temperature and pressure, it is clear that the rigorous calculation of a convection coefficient appropriate to a given wall and fluid is an enormously complicated problem. Solutions of the problem for particular situations are achieved by numerical integration.  

### 4.14 THERMAL RADIATION; BLACKBODY  

Thermal radiation is important in thermometry, since it is the basis of precisely measured high temperatures above the range of gas thermometers. As an example of the effects of thermal radiation, consider placing your hand near a hot object and experiencing the warming that occurs before the object is touched. Evidently, heat is transmitted across the space between the object and the hand. That this can occur without the intervention of matter is proved by the fact that heat comes to us from the sun across 93 million miles of empty space. By conduction and convection, the transfer of heat is accomplished through the medium of matter, and heat can be transferred in this way only as far as matter extends or can itself be transported. By the process of radiation, however, heat is separated from its association with matter and can travel as radiation as far as empty space extends. Originally, the waves of radiation were called "radio waves." But, as the nature of radiation came to be understood, the term was replaced by the term "electromagnetic waves."

===== Page 117 =====

 A substance may be stimulated to emit electromagnetic radiation in a number of ways:  

1. An electric conductor carrying a high-frequency alternating current emits radio waves. 
2. Electrons oscillating in a magnetron-type tube emit microwaves. 
3. A hot solid or liquid emits thermal radiation, that is, infrared radiation. 
4. A gas experiencing an electric discharge may emit visible or ultraviolet radiation. 
5. A substance exposed to ultraviolet radiation from an external source may emit fluorescent light. 
6. A metal target bombarded by high-speed electrons emits x-rays. 
7. A substance whose atoms are radioactive may emit gamma rays.  

All these radiations are electromagnetic waves, differing only in frequency (or wavelength) in vacuum. We shall be concerned in this section only with thermal radiation, namely, the radiation emitted by a solid or a liquid by virtue of its temperature. The radiation characteristics of gases require special treatment. In this section, we shall assume that gases are transparent to thermal radiation.  

When thermal radiation is dispersed by a prism or diffraction grating, one obtains a continuous spectrum of the visible spectrum and the invisible infrared radiation. The distribution of energy among the various wavelengths is such that, at temperatures below about \(500^{\circ}\mathrm{C}\) , the energy is infrared radiation; at higher temperatures, increasingly more visible light is emitted. In general, the higher the temperature of a body, the greater the total energy emitted.  

The loss of energy due to the emission of thermal radiation may be compensated in a variety of ways. The emitting body may be a source of energy itself, such as the sun; or, there may be a constant supply of electrical energy from the surroundings, as in the case of a lamp. Energy may be supplied also by heat conduction or by the performance of work on the emitting body. In the absence of these sources of supply, the only other way in which a body may receive energy is by the absorption of radiation from its surroundings. In the case of a body that is immersed in radiation, the internal energy of the body will remain constant when the rate at which radiant energy is emitted equals the rate at which radiant energy is absorbed; in other words, the exiting radiant power equals the incident radiant power.  

Experiment shows that the radiant power leaving a body as thermal radiation depends on the temperature, on the area of the surface, and on the nature of the surface of the body. The total radiant power exiting an infinitesimal element of surface, divided by the area of that surface, is called the radiant exitance \(\mathcal{E}\) of the body (formerly, radiant emittance). For example, the radiant exitance of tungsten at \(1000\mathrm{K}\) is \(6.46\mathrm{kW / m^2}\) , at \(2000\mathrm{K}\) is \(236\mathrm{kW / m^2}\) , and at \(3000\mathrm{K}\) is \(1534\mathrm{kW / m^2}\) .

===== Page 118 =====

96 PART I: Fundamental Concepts  

When thermal radiation is incident upon a body equally from all directions, the radiation is said to be isotropic. Some of the radiation may be absorbed, some reflected, and some transmitted. In general, the incident isotropic radiation of all wavelengths that is absorbed depends on the temperature and the nature of the surface of the absorbing body. The fraction of the total incident radiant power that is absorbed is called the absorptivity. In thermal equilibrium, the processes of absorption and emission of radiant power are equal and opposite. So, the total emissivity \(\epsilon\) equal to the absorptivity, is defined as the fraction of the power provided to a real body that is emitted through a material surface as thermal radiation, where the word "total" includes all wavelengths of electromagnetic radiation. As a practical matter, it is easier to measure emissivity than absorptivity. To summarize:  

Radiant exitance \(\mathcal{E} =\) total radiant power emitted per unit area;  

and  

Total emissivity \(\epsilon =\) fraction of the total radiant power that is emitted as thermal radiation.  

The emissivity depends on both the temperature and the nature of the emitting surface. The emissive nature of surfaces is revealed by comparing emissivities at the same temperature. At \(300\mathrm{K}\) , when all bodies emit only infrared radiation, the emissivity of polished steel is 0.09, rough oxidized steel is 0.81, and ocean water is 0.96. There are some substances, such as lampblack or carbon soot, whose emissivity is very nearly unity, that is, almost an ideal emitter. For theoretical purposes, it is useful to conceive of an ideal substance capable either of absorbing all the thermal radiation falling on it or of emitting all the energy provided to it in the form of thermal radiation. Such a substance is called a blackbody. If a blackbody is indicated by the subscript \(bb\) , we have  

\[
\epsilon_{bb} = 1.
\]

A very good experimental approximation to a blackbody is provided by a cavity enclosed by high- temperature opaque walls. The interior walls, which are maintained at a uniform temperature, permit thermal radiation to pass through a hole small in comparison with the dimensions of the cavity. Any radiation entering the hole is completely absorbed by the walls after repeated reflections at the walls, with only a negligible amount eventually finding its way out the hole. This is true regardless of the composition of the materials of the interior walls.  

The radiation emitted by the interior walls is similarly absorbed or diffusely reflected a large number of times, so that the cavity is filled with isotropic blackbody radiation. Let us define the irradiance as the radiant power per unit area incident upon a surface within the cavity. Suppose a blackbody whose

===== Page 119 =====

 temperature is the same as that of the walls is introduced into the cavity. Then, denoting the irradiance by \(H, \dagger\)  

Radiant power absorbed per unit area \(= \epsilon_{bb}H = H\)  

and Radiant power emitted per unit area \(= \mathcal{E}_{bb}\)  

Since the temperature of the blackbody remains constant, the radiant power per unit area that is absorbed must equal the radiant power per unit area that is leaving; whence,  

\[
H = \mathcal{E}_{bb}, \quad (4.19)
\]

or the irradiance within a cavity whose walls are at the temperature \(T\) is equal to the radiant exitance of a blackbody at the same temperature. For this reason, the radiation enclosed within a cavity is called blackbody radiation. Such radiation, which provides standard radiation in terms of wavelengths and intensities, is a function only of temperature and is studied by allowing a small amount to escape from a small hole in the cavity. Since \(H\) is independent of the materials of which the interior walls are composed, it follows that the radiant exitance of a blackbody is a function of the temperature only.  

### 4.15 KIRCHHOFF'S LAW; RADIATED HEAT  

The radiant exitance of a non- blackbody depends as much on the nature of the surface as on the temperature, according to a simple law that we may derive as follows. Suppose that a non- blackbody at the temperature \(T\) , with radiant exitance \(\mathcal{E}\) , and emissivity \(\epsilon\) , is introduced into a cavity whose interior walls are at the same temperature and where the irradiance is \(H\) . Then,  

Radiant power absorbed per unit area \(= \epsilon H\)  

and  

Radiant power emitted per unit area \(= \mathcal{E}\) .  

Since the non- blackbody is in equilibrium,  

\[
\mathcal{E} = \epsilon H
\]

But, from Eq. (4.19), \(H = \mathcal{E}_{bb}\) ; hence,  

\[
\mathcal{E} = \epsilon \mathcal{E}_{bb}, \quad (4.20)
\]

===== Page 120 =====

98 PART I: Fundamental Concepts  

TABLE 4.3 Total emissivities of various surfaces, as compiled by Hottel (Values at intermediate temperatures may be obtained by linear interpolation)   

MaterialTemperature range, KEmissivity εPolished metals:Aluminum525-8750.039-0.057Brass525-6750.033-0.037Chromium325-8250.08-0.26Copper3750.018Iron425-12750.05-0.37Nickel300-6250.045-0.087Zinc525-6250.045-0.053Filaments:Molybdenum1025-28750.096-0.29Platinum300-14750.036-0.19Tantalum1575-32750.19-0.31Tungsten300-35750.032-0.35Other materials:Asbestos325-6250.93-0.95Ice (wet)2730.97Lampblack300-6250.95Rubber (gray)3000.86  

or the radiant exitance of any body at any temperature is equal to a fraction of the radiant exitance of a blackbody at that temperature, this fraction being the emissivity at that temperature.  

This equation, known as Kirchhoff's law and named after the German physicist, shows that the emissivity of a body may be determined experimentally by measuring the radiant exitance of the body and dividing it by the exitance of a blackbody at the same temperature. Values of the emissivity of the surfaces of various materials, measured in this way, are given in Table 4.3. It should be emphasized that the tabulated values of emissivity refer to the thermal radiation appropriate to the temperature listed in the temperature- range column. Thus, the emissivity of ice is 0.97 not for visible radiation, but for the long infrared waves associated with matter at \(0^{\circ}\mathrm{C}\) (273 K).  

It should be noticed that the word "heat" has not appeared as yet. If there is a temperature difference between a body and its surroundings, then, in a given interval of time, the body loses an amount of internal energy equal to the energy radiated minus the energy absorbed, whereas the surroundings gain an amount of internal energy equal to the energy absorbed minus the energy radiated. The gain of the surroundings equals the loss of the body. The gain or loss of internal energy of the body, equal to the difference between the energy of the thermal radiation which is absorbed and that which is radiated, is called heat. This statement is in agreement with the original definition of heat, since a gain

===== Page 121 =====

 or loss of internal energy by radiation and absorption will take place only if there is a difference in temperature between a body and its surroundings. If the two temperatures are the same, there is no net gain or loss of internal energy of either the body or its surroundings, and there is, therefore, no transfer of heat.  

Imagine a cavity whose interior walls are maintained at a constant temperature \(T_{W}\) . Suppose that a non- blackbody at a temperature \(T\) different from that of the walls is placed in the cavity. If the body is small compared with the size of the cavity, then the character of the radiation in the cavity will not be appreciably affected by the presence of the small body. Let \(H\) , as before, denote the irradiance within the cavity, and \(\mathcal{E}\) and \(\epsilon\) the radiant exitance and emissivity, respectively, of the body. Then, as before,  

Radiant power absorbed per unit area \(\epsilon H\)  

and  

Radiant power emitted per unit area \(\epsilon \mathcal{E}\)  

but now these two powers per unit area are not equal. The difference between them is the heat transferred by radiation per second per unit area. If \(\mathrm{d}Q\) is the heat transferred in time \(dt\) to the non- blackbody whose area is \(A\) , then  

\[
\frac{\mathrm{d}Q}{dt} = A(\epsilon H - \mathcal{E}), \quad (4.21)
\]

where, it must be remembered, emissivity \(\epsilon\) and exitance \(\mathcal{E}\) are functions of the temperature of the body \(T\) ; and irradiance \(H\) is a function of the temperature of the wall \(T_{W}\) ; thus,  

\[
\mathcal{E} = \epsilon (T)\mathcal{E}_{bb}(T),
\]

and  

\[
H = \mathcal{E}_{bb}(T_{W}).
\]

Hence,  

\[
\frac{\mathrm{d}Q}{dt} = A\epsilon (T)[\mathcal{E}_{bb}(T_{W}) - \mathcal{E}_{bb}(T)], \quad (4.22)
\]

or the rate at which heat is transferred by radiation is proportional to the difference between the radiant exitances of a blackbody at the two temperatures in question.  

### 4.16 STEFAN-BOLTZMANN LAW  

The first measurements of the heat transferred by radiation between a body and its surroundings were made by Tyndall. On the basis of these experiments, it was concluded by Stefan in 1879 that the heat radiated was proportional to the difference of the fourth powers of the absolute temperatures. This purely experimental result was later derived thermodynamically by Boltzmann, who showed that the radiant exitance of a blackbody at any temperature \(T\) is equal to  

\[
\mathcal{E}_{bb}(T) = \sigma T^{4}. \quad (4.23)
\]

===== Page 122 =====

100 PART I: Fundamental Concepts  

This law is now known as the Stefan- Boltzmann law, and \(\sigma\) (Greek letter sigma) is called the Stefan- Boltzmann constant.  

Referring to Eq. (4.22), we have for the heat transferred by radiation between a body at the temperature \(T\) and walls at \(T_{W}\) ,  

\[
\frac{\mathrm{d}Q}{d t} = A\epsilon \sigma (T_{W}^{4} - T^{4}), \quad (4.24)
\]

where \(\epsilon\) is a function of the temperature \(T\) .  

Two simple methods may be employed for the determination of the Stefan- Boltzmann constant:  

1. Nonequilibrium method. A blackened silver disk is placed in the center of a large blackened copper hemisphere. The silver disk is covered and shielded from radiation until the copper hemisphere achieves the temperature of condensing steam; this temperature is measured with a thermocouple. Then, the disk is uncovered, and its temperature \(T\) is measured as a function of the time \(t\) . From the resulting heating curve, the slope \(dT / dt\) is obtained. Assuming the silver disk to be a blackbody and putting \(\mathrm{d}Q = C_{P}dT\) in Eq. (4.24), where \(C_{P}\) is the heat capacity at constant pressure, we have  

\[
\frac{C_{P}dT}{dt} = A\sigma (T_{W}^{4} - T^{4});
\]

whence,  

\[
\sigma = \frac{C_{P}}{A(T_{W}^{4} - T^{4})}\frac{dT}{dt}.
\]

2. Equilibrium method. A hollow blackened copper sphere is provided with an electric heater and a thermocouple and is suspended inside a vessel whose walls are maintained at a constant temperature \(T_{W}\) . Electrical energy is supplied at a constant rate \(\mathcal{E}I\) until the sphere achieves an equilibrium temperature \(T\) at which the rate of supply of energy is equal to the rate of emission of radiation. Assuming the sphere to be a blackbody, we have, at equilibrium,  

\[
\mathcal{E}I = A\sigma (T^{4} - T_{W}^{4});
\]

whence,  

\[
\sigma = \frac{I}{4\pi r^{2}(T^{4} - T_{W}^{4})},
\]

where \(r\) is the radius of the sphere. The best measurements of the Stefan- Boltzmann constant to date have yielded the value  

\[
\sigma = 5.67051\times 10^{-8}\mathrm{W / m^{2}\cdot K^{4}}. \quad (4.25)
\]

[file content end until page 122]
===== Page 123 =====

4.1. A gas contained in a cylinder by a layer of styrofoam is quickly compressed, the temperature rising several hundred degrees. Has there been a transfer of heat? Has the "heat content" of the gas been increased?  

4.2. A combustion experiment is performed by burning a mixture of fuel and oxygen in a constant- volume container surrounded by a water bath. During the experiment, the temperature of the water rises. If the system is the mixture of fuel and oxygen:  

(a) Has heat been transferred? 
(b) Has work been done? 
(c) What is the sign of \(\Delta U?\)  

4.3. A liquid is irregularly stirred in a well- insulated container and thereby experiences a rise in temperature. If the system is the liquid:  

(a) Has heat been transferred? 
(b) Has work been done? 
(c) What is the sign of \(\Delta U?\)  

4.4. The amount of water in a lake may be increased by action of underground springs, by inflow from a river, and by rain. It may be decreased by various outflows and by evaporation.  

(a) Comment on the question: How much rain is there in the lake? 
(b) Comment on the question: How much water in the lake is due to rain? 
(c) What concept is analogous to "rain in the lake"?  

4.5. A container with rigid well- insulated walls is divided into two parts by a partition. One part contains a gas, and the other is evacuated. If the partition suddenly breaks, show that the initial and final internal energies of the gas are equal. (Note: this process is called an adiabatic free expansion.)  

4.6. When an electric current is maintained in an electrolytic cell of slightly acidic water and 1 mol of water is electrolyzed into hydrogen and oxygen, \(2F\) (faradays) of charge are transferred through a source of emf \(\mathcal{E}(1F\approx 96,500\mathrm{C / mol})\) . The energy change of the system is \(+286,500\mathrm{J}\) , and 50,000 J of heat is absorbed. What is \(\mathcal{E}\) ?  

4.7. A cylinder with rigid well- insulated walls is divided into two parts by a rigid insulating wall with a small hole in it. A frictionless, insulated piston is held against the perforated partition, thus preventing the gas that is on the other side from seeping through the hole. The gas is maintained at a pressure \(P_{i}\) by another frictionless insulated piston. Imagine both pistons to move simultaneously in such a way that, as the gas streams through the hole, the pressure remains at a constant value \(P_{i}\) on one side of the dividing wall and at a constant lower value \(P_{f}\) on the other side, until all the gas is forced through the hole. (Note: this process is called a throttling process.) Prove that  

\[
U_{i} + P_{i}V_{i} = U_{f} + P_{f}V_{f}.
\]

===== Page 124 =====

4.8. A container of volume \(V\) contains \(n\) moles of gas at high pressure. Connected to the container is a capillary tube through which the gas may leak slowly out to the atmosphere, where the pressure is \(P_{0}\) . Surrounding the container and capillary is a water bath, in which is immersed an electrical resistor. The gas is allowed to leak slowly through the capillary into the atmosphere while electrical energy is dissipated in the resistor at such a rate that the temperature of the gas, the container, the capillary, and the water is kept equal to that of the outside air. Show that, after as much gas as possible has leaked out during time interval \(t\) , the change in internal energy is  

\[
\Delta U = \mathcal{E}It - P_0(nv_0 - V),
\]

where \(v_{0}\) is the molar volume of the gas at atmospheric pressure, \(\mathcal{E}\) is the potential difference across the resistor, and \(I\) is the current in the resistor.  

4.9. A thick- walled insulated metal chamber contains \(n_{i}\) moles of helium at high pressure \(P_{i}\) . It is connected through a valve with a large, almost empty gasholder in which the pressure is maintained at a constant value \(P^{\prime}\) , very nearly atmospheric. The valve is opened slightly, and the helium flows slowly and adiabatically into the gasholder until the pressure on the two sides of the valve is equalized. Prove that  

\[
\frac{n_{f}}{n_{i}} = \frac{h^{\prime} - u_{i}}{h^{\prime} - u_{f}},
\]

where \(n_{f} =\) number of moles of helium left in the chamber,  

\(u_{i} =\) initial molar internal energy of helium in the chamber,  

\(u_{f} =\) final molar internal energy of helium in the chamber, and  

\(h^{\prime} = u^{\prime} + P^{\prime}\nu\) (where \(u^{\prime} =\) molar internal energy of helium in the gasholder;  

\(v^{\prime} =\) molar volume of helium in the gasholder).  

4.10. Regarding the internal energy of a hydrostatic system to be a function of \(T\) and \(P\) , derive the following equations:  

\[
(a)\qquad \mathrm{d}Q\Big[\Big(\frac{\partial U}{\partial T}\Big)_{P} + P\Big(\frac{\partial V}{\partial T}\Big)_{P}\Big]dT + \Big[\Big(\frac{\partial U}{\partial P}\Big)_{T} + P\Big(\frac{\partial V}{\partial P}\Big)_{T}\Big]dP.
\]
\[
(b)\qquad \Big(\frac{\partial U}{\partial T}\Big)_{P} = C_{P} - PV\beta .
\]
\[
(c)\qquad \Big(\frac{\partial U}{\partial P}\Big)_{T} = PV\kappa -(C_{P} - C_{V})\frac{\kappa}{\beta}.
\]

4.11. Taking \(U\) to be a function of \(P\) and \(V\) , derive the following equations:  

\[
(a)\qquad \mathrm{d}Q = \Big(\frac{\partial V}{\partial P}\Big)_{V}dP + \Big[\Big(\frac{\partial U}{\partial V}\Big)_{P} + P\Big]dV.
\]
\[
(b)\qquad \Big(\frac{\partial U}{\partial P}\Big)_{V} = \frac{C_{V}\kappa}{\beta}.
\]
\[
(c)\qquad \Big(\frac{\partial U}{\partial V}\Big)_{P} = \frac{C_{P}}{V\beta} -P.
\]

===== Page 125 =====

4.12. Derive the equations listed in the accompanying table.  

SystemHeat capacity at constant extensive variableHeat capacity at constant intensive variableStretched wireC_L = (∂U/∂T)_LC_γ = (∂U/∂T)_γ - J LαParamagnetic solid obeying Curie&#x27;s lawC_m = (∂U/∂T)_mC_κ = (∂U/∂T)_κ + m^2/C_c

Note: \(C_{C}\) is the Curie constant, not a heat capacity.  

4.13. Consider using the apparatus shown in Fig. 4- 1(a), known as the Joule paddle wheel, to determine the specific heat at constant atmospheric pressure. The paddle wheel is driven by a slowly falling weight, and both have a temperature of \(14.5^{\circ}\mathrm{C}\) . As a result of the work done by the \(0.427\mathrm{kg}\) mass that falls \(1.00\mathrm{m}\) , the temperature of \(1\mathrm{kg}\) of water rises \(1^{\circ}\mathrm{C}\) . Calculate \(c_{P}\) .  

4.14. One mole of a gas obeys the van der Waals equation of state:  

\[
\left(P + \frac{a}{v^2}\right)(v - b) = RT,
\]

and its molar internal energy is given by  

\[
u = cT - \frac{a}{v},
\]

where \(a\) , \(b\) , \(c\) , and \(R\) are constants. Calculate the molar heat capacities \(c_{V}\) and \(c_{P}\) .  

4.15. The equation of state for a monatomic solid is  

\[
P\nu +f(\nu) = \Gamma u,
\]

where \(\nu\) is the molar volume, \(\Gamma\) is the Grüneisen constant, and \(u\) is the molar internal energy due to lattice vibrations. Prove that  

\[
\Gamma = \frac{\beta\nu}{c\nu\kappa^{\prime}}
\]

where \(\kappa\) is the isothermal compressibility. This equation, known as the Grüneisen relation, plays an important role in solid- state theory.  

4.16. The molar heat capacity at constant pressure \(C_{P} / n\) of a gas varies with the temperature according to the equation  

\[
\frac{C_{P}}{n} = a + bT - \frac{c}{T^{2}},
\]

where \(a\) , \(b\) , and \(c\) are constants. How much heat is transferred during an isobaric process in which \(n\) moles of gas experience a temperature rise from \(T_{i}\) to \(T_{f}\) ?  

4.17. The molar heat capacity at constant volume of a metal at low temperatures varies with the temperature according to the equation

===== Page 126 =====

104 PART I: Fundamental Concepts  

\[
\frac{C_V}{n} = \left(\frac{124.8}{\Theta}\right)^3 T^3 + \gamma T,
\]

where \(\Theta\) is the Debye temperature, \(\gamma\) is a constant, and \(C_V / n\) is measured in units of \(\mathrm{mJ / mol\cdot K}\) . The first term on the left is the contribution attributable to lattice vibrations and the second term is due to the contribution of free electrons. For copper, \(\Theta\) is \(343\mathrm{K}\) and \(\gamma\) is \(0.688\mathrm{mJ / mol\cdot K^2}\) . How much heat per mole is transferred during a process in which the temperature changes from 2 to \(3\mathrm{K}\) ?  

4.18. Suppose that heat conduction occurs at a constant rate \(\mathrm{d}Q / dt\) in a hollow sphere with an inner radius \(r_1\) at temperature \(T_1\) and an outer radius \(r_2\) at temperature \(T_2\) . Show that for constant thermal conductivity \(K\) , the temperature difference between the two surfaces is given by  

\[
T_{1} - T_{2}\frac{\mathrm{d}Q / dt}{4\pi K}\left(\frac{1}{r_{2}} -\frac{1}{r_{1}}\right).
\]

4.19. Two thin concentric spherical shells of radius \(0.05\mathrm{m}\) and \(0.15\mathrm{m}\) , respectively, have their annular cavity filled with charcoal. When energy is supplied at the steady rate of \(10.8\mathrm{W}\) to a heater at the center, a temperature difference of \(50^{\circ}\mathrm{C}\) is set up between the spheres. Find the thermal conductivity of charcoal.  

4.20. The air above the surface of a freshwater lake is at a temperature \(T_{A}\) , while the water is at its freezing point \(T_{i}\) , where \(T_{A}< T_{i}\) . After a time \(t\) has elapsed, ice of thickness \(y\) has formed. Assuming that the heat, which is liberated when the water freezes, flows up through the ice by conduction and then into the air by natural convection, prove that  

\[
\frac{y}{h} +\frac{y^2}{2K} = \frac{T_i - T_A}{\rho L} t,
\]

where \(h\) is the convection coefficient per unit area and is assumed constant while ice forms, \(K\) is the thermal conductivity of ice, \(l\) is the latent heat of fusion of ice, and \(\rho\) is the density of ice. (Hint: The temperature of the upper surface is variable. Assume that the ice has a thickness \(y\) and imagine an infinitesimal thickness \(dy\) to form in time \(dt\) .)  

4.21. A solid cylindrical copper rod \(0.10\mathrm{m}\) long has one end maintained at a constant temperature of \(20\mathrm{K}\) . The other end is blackened and exposed to thermal radiation from a body at \(300\mathrm{K}\) , with no energy lost or gained through the sides of the cylinder. When equilibrium is reached, what is the temperature difference between the two ends? (Hint: Refer to Fig. 4.7. )  

4.22. A cylindrical metal can, blackened on the outside, \(0.10\mathrm{m}\) high and \(0.05\mathrm{m}\) in diameter, contains liquid \(^4\mathrm{He}\) at its normal boiling point of \(4.22\mathrm{K}\) , at which its heat of vaporization is \(20.4\mathrm{kJ / kg}\) . Completely surrounding the helium can are walls maintained at the temperature of liquid nitrogen \((77.35\mathrm{K})\) , and the intervening space is continuously evacuated to a very low pressure. How much helium is lost per hour?  

4.23. The operating temperature of a tungsten filament in an incandescent lamp is \(2460\mathrm{K}\) , and its total emissivity is 0.30. Find the surface area of the filament of a 100- W lamp.

===== Page 127 =====

4.24. A copper wire of length \(1.317\mathrm{m}\) and diameter \(3.26\times 10^{- 4}\mathrm{m}\) is blackened and placed along the axis of an evacuated glass tube. The wire is connected to a battery, a rheostat, an ammeter, and a voltmeter, and the current is increased until, at the moment the wire is about to melt, the ammeter reads \(12.8\mathrm{A}\) and the voltmeter reads \(20.2\mathrm{V}\) . Assuming that all the energy supplied was radiated and that the radiation from the glass tube is negligible, calculate the melting temperature of copper.  

4.25. The solar constant is the incident energy per unit of time on a unit area of a surface placed at right angles to a sunbeam just outside the earth's atmosphere. The value of the solar constant is \(1.37\mathrm{kW / m^2}\) . The area of a sphere with radius 93,000,000 miles is \(2.79\times 10^{23}\mathrm{m}^2\) , and the surface area of the sun is \(6.09\times 10^{18}\mathrm{m}^2\) . Assuming that the sun is a blackbody, calculate its surface temperature.  

4.26. (a) A small body with temperature \(T\) and emissivity \(\epsilon\) is placed in a large evacuated cavity with interior walls kept at temperature \(T_{W}\) . When \(T_{W} - T\) is small, show that the rate of heat transfer by radiation is  

\[
\frac{\mathrm{d}Q}{d t} = 4T_{W}^{3}A\epsilon \sigma (T_{W} - T).
\]

(b) If the body remains at constant pressure, show that the time for the temperature of the body to change from \(T_{1}\) to \(T_{2}\) is given by  

\[
t = \frac{C_{P}}{4T_{W}^{3}A\epsilon\sigma}\ln \frac{T_{W} - T_{1}}{T_{W} - T_{2}}.
\]

(c) Two small blackened spheres of identical size, one of copper and the other of aluminum, are suspended by silk threads within a large hole in a block of melting ice. It is found that it takes \(10\mathrm{min}\) for the temperature of the aluminum to drop from \(276\) to \(274\mathrm{K}\) , and \(14.2\mathrm{min}\) for the copper to drop the same interval of temperature. What is the ratio of specific heats of aluminum and copper? (The densities of Al and Cu are \(2.70\times 10^{3}\mathrm{kg / m^{3}}\) and \(8.96\times 10^{3}\mathrm{kg / m^{3}}\) at \(25^{\circ}\mathrm{C}\) respectively.)  

4.27. A blackened solid copper sphere with radius of \(0.02\mathrm{m}\) is placed in an evacuated enclosure with walls kept at \(100^{\circ}\mathrm{C}\) . In what time does its temperature change from 103 to \(102^{\circ}\mathrm{C}\) ? \((c_{P} = 0.395\mathrm{kJ / kg}\cdot \mathrm{K}; \rho = 8.96\times 10^{3}\mathrm{kg / m^{3}}\) at \(25^{\circ}\mathrm{C}\) .)  

4.28. In the case of a paramagnetic gas:  

(a) Derive the equation  

\[
\mathrm{d}Q = \left(\frac{\partial U}{\partial T}\right)_{V,\mathcal{M}}dT + \left[\left(\frac{\partial U}{\partial V}\right)_{M,T} + P\right]dV + \left[\left(\frac{\partial U}{\partial\mathcal{M}}\right)_{T,V} - \mu_{0}\mathcal{H}\right]d\mathcal{M}.
\]

(b) Derive expressions for \(C_{V,\mathcal{M}}, C_{V,\mathcal{M}}, C_{P,\mathcal{M}}\) , and \(C_{P,\mathcal{M}}\) .

===== Page 128 =====

5.1 EQUATION OF STATE OF A GAS  

It was emphasized in Chap. 1 that a gas is the best- behaved thermometric substance because of the fact that the ratio of the pressure \(P\) of a gas at any temperature to the pressure \(P_{TP}\) of the same gas at the triple point, as both \(P\) and \(P_{TP}\) approach zero, approaches a value independent of the nature of the gas. The limiting value of this ratio, multiplied by 273.16 K, was defined to be the ideal- gas temperature \(T\) of the system at whose temperature the gas exerts the pressure \(P\) . The reason for this regular behavior may be found by investigating the way in which the product \(PV\) of a gas depends on \(P\) .  

Suppose that the pressure \(P\) and the volume \(V\) of \(n\) moles of gas held at any constant temperature are measured over a wide range of values of the pressure, and the product \(Pv\) , where the molar volume \(v = V / n\) , is plotted as a function of \(P\) . Experiments of this sort were first performed by Amagat in France in 1870 and later by Holborn and Otto in Berlin and by Kamerlingh- Onnes and Keesom in Leiden. The relation between \(Pv\) and \(P\) may be expressed for a real gas by means of a power series (or virial expansion) of the form  

\[
Pv = A(I + BP + CP^2 + \dots), \quad (5.1)
\]

where \(A\) , \(B\) , \(C\) , etc., are called virial coefficients ( \(A\) being the first virial coefficient, \(B\) the second, etc.) and depend on the temperature and on the nature of the gas. In the pressure range from 0 to about 40 standard atmospheres, the relation between \(Pv\) and \(P\) is practically linear, so that only the first two terms in the expansion are significant. In general, the greater the pressure range, the larger the number of terms in the virial expansion.

===== Page 129 =====

 The remarkable property of gases that makes them so valuable in thermometry is displayed in Fig. 5- 1, where the product \(Pv\) is plotted against \(P\) for four different gases, all at the temperature of boiling water in the top graph, all at the triple point of water in the middle graph, and all at the temperature of solid \(\mathrm{CO}_{2}\) in the bottom graph. In each case, it is seen that, as the pressure approaches zero, the product \(Pv\) approaches the same value for all gases at the same temperature. It follows from this that the first virial coefficient \(A\) is independent of the nature of the gas and depends only on temperature. Thus,  

\[
\lim_{P\to 0}(Pv) = \mathbf{A} = \left\{ \begin{array}{ll}\mathrm{function~of~temperature~only,} & \mathrm{(5.2)}\\ \mathrm{independent~of~gas.} & \mathrm{(5.2)} \end{array} \right. \quad (5.2)
\]

The ideal- gas temperature \(T\) is defined in Eq. (1.7) as  

\[
T = 273.16\mathrm{K}\lim_{P_{TP}\to 0}\left(\frac{P}{P_{TP}}\right)\qquad (\mathrm{const.}V),
\]

\[
T = 273.16\mathrm{K}\lim \frac{P V / n}{P_{T P}V / n} = 273.16\mathrm{K}\frac{\lim (P\nu)}{\lim (P\nu)_{T P}},
\]

\[
\lim (P\nu) = \left[\lim (P\nu)_{T P}\right]T.
\]

The bracketed term is called the molar gas constant and is denoted by \(R\) . Thus,  

\[
R = \frac{\lim (P\nu)_{T P}}{273.16\mathrm{K}}. \quad (5.3)
\]

In 1972, Batuecas determined \(\lim (P\nu)_{0^{\circ}\mathrm{C}}\) for oxygen to be 22.4132 liter \(\cdot\) atm/ mol (2.27102 kJ/mol). Hence, the gas constant \(R\) was determined to have the value of 8.31441 J/mol \(\cdot\) K with an uncertainty of 31 parts per million in the 1973 recommendations of physical constants by the international Committee on Data for Science and Technology (CODATA). However, measurements of volume in the determination of \(R\) by the method of limiting density are beset with the problem of adsorption of gas on the walls of the container. Furthermore, the uncertainty in the normal melting temperature of ice is greater than the uncertainty of the triple- point temperature of water. For these reasons, an improved method for determining a more precise value of the molar gas constant \(R\) will be presented in Sec. 5.7.  

Finally, substituting for \(\nu\) its value \(V / n\) , we may write the equation of state of a gas in the limit of low pressures in the form  

\[
\lim (P V) = n R T, \quad (5.4)
\]

which is the experimental equation of state for the ideal gas. Since \(\lim (P\nu) = A = RT\) , Eq. (5.1) becomes  

\[
\frac{P\nu}{R T} = 1 + B P + C P^{2} + D P^{3} + \dots .
\]

The virial coefficients play an important role, not only in practical thermodynamics, but also in theoretical physics, where they are related to molecular properties. Except at very low temperatures, the virial coefficients are quite small, as shown in Table 5.1, where the virial coefficients are given for nitrogen in the temperature range 150 to \(500\mathrm{K}\) .  

### 5.2 INTERNAL ENERGY OF A REAL GAS  

Imagine a thermally insulated vessel with rigid walls, divided into two compartments by a partition. Suppose that there is a gas in one compartment and that the other contains a vacuum. If the partition is removed, the gas will undergo what is known as an adiabatic free expansion in which no work is done and no heat is transferred. From the first law, since both \(Q\) and \(W\) are zero, it follows that the internal energy remains unchanged during a free expan

===== Page 131 =====

 TABLE 5.1  Viral coefficients for nitrogen  

T, KB, 10-9 Pa-1C, 1018 Pa-2D, 1027 Pa-3150-55.13-2425-9992200-20.97-7.8055,050250-7.7922914,270300-1.8120328603501.18152-2024002.75111-9324503.5981.6-9905004.0360.7-856

sion. The question of whether or not the temperature of a gas changes during a free expansion and, if it does, of the magnitude of the temperature change has engaged the attention of scientists for about a hundred years. Starting with Joule in 1843, many attempts have been made to measure either the quantity \((\partial T / \partial V)_{U}\) , which is called the Joule coefficient, or related quantities that are all a measure, in one way or another, of the effect of an adiabatic free expansion, or as it is often called, Joule expansion.  

In order to study the free expansion of a gas and to measure \((\partial T / \partial V)_{U}\) Joule connected two vessels by a short tube and stopcock, which were immersed in a water bath. One vessel contained air at high pressure, and the other was evacuated. The temperature of the water was measured before and after the expansion, the idea being to measure indirectly the drop in temperature of the gas from the decrease in temperature of the water. Since the heat capacity of the vessels and the water was approximately 1000 times as large as the heat capacity of the air, Joule was unable to detect any temperature change of the water, although, in the light of our present knowledge, the air must have undergone a temperature decrease of several degrees. A direct measurement of the temperature change associated with a free expansion is so difficult that it is necessary to give up directly measuring the Joule coefficient \((\partial T / \partial V)_{U}\) . Instead of measuring a temperature change during a free expansion for which the internal energy is constant, consider measuring a change of internal energy for constant temperature.  

In general, the internal energy of any gas is a function of any two of the coordinates \(P\) , \(V\) , and \(T\) . The differential of \(U\) as a function of \(T\) and \(V\) is  

\[
dU = \left(\frac{\partial U}{\partial T}\right)_V dT + \left(\frac{\partial U}{\partial V}\right)_T dV.
\]

If no temperature change \((dT = 0)\) takes place in a free expansion \((dU = 0)\) then it follows that  

\[
\left(\frac{\partial U}{\partial V}\right)_T = 0;
\]

===== Page 132 =====

110 PART I: Fundamental Concepts  

or, in other words, \(U\) does not depend on \(V\) . Considering \(U\) to be a function of \(T\) and \(P\) , we have  

\[
dU = \left(\frac{\partial U}{\partial T}\right)_P dT + \left(\frac{\partial U}{\partial P}\right)_T dP.
\]

If no temperature change \((dT = 0)\) takes place in a free expansion \((dU = 0)\) , then it follows that  

\[
\left(\frac{\partial U}{\partial P}\right)_T = 0;
\]

or, in other words, \(U\) does not depend on \(P\) . Then, it is apparent that, if no temperature change takes place in a free expansion of a gas, \(U\) is independent of \(V\) and of \(P\) , and, therefore, \(U\) is a function of \(T\) only. Thus, to determine if the internal energy is a function of temperature, one must perform an experiment where the temperature is constant and measure whether either \((\partial U / \partial V)_T\) or \((\partial U / \partial P)_T\) is zero.  

Later methods of attacking the question of the temperature dependence of the internal energy of a gas involved the measurement of the quantity \((\partial u / \partial P)_T\) , where \(u\) is the molar internal energy, by having the gas undergo an isothermal expansion in which heat is transferred and work is done. The most extensive series of measurements of this kind was performed by Rossini and Frandsen in 1932 at the National Bureau of Standards. The apparatus is shown in Fig. 5- 2. A container \(B\) holds \(n\) moles of gas at a pressure \(P\) and communicates with the atmosphere through a long coil wrapped around the  

FIGURE 5- 2 Apparatus for measuring \((\partial u / \partial P)_T\) of a gas. (F. D. Rossini and M. Frandsen: Journal of Research of the National Bureau of Standards, vol. 9, pp. 733- 747, 1932. )

===== Page 133 =====

 container. The whole apparatus is immersed in a water bath whose temperature can be maintained constant at exactly the same value as that of the surrounding atmosphere.  

The experiment is performed as follows. When the valve is opened slightly, the gas flows slowly through the long coil and out into the air. At the same time, the temperature of the gas, the container, the coils, and the water is maintained constant by an electric heating coil immersed in the water. The electrical energy supplied to the water is, therefore, the heat \(Q\) absorbed by the gas during the expansion. The work done by the gas is evidently  

\[
W = -P_{0}(n\nu_{0} - V),
\]

where \(P_{0}\) is atmospheric pressure, \(\nu_{0}\) is the molar volume at atmospheric temperature and pressure, \(V\) is the volume of the container, and \(n\nu_{0}\) is larger than \(V\) .  

If \(u(P,T)\) is the molar internal- energy at pressure \(P\) and temperature \(T\) and if \(u(P_{0},T)\) is the molar internal- energy at atmospheric pressure and the same temperature, then, from the first law, the change of molar internal- energy can be expressed in terms of the measured quantities \(Q\) and \(W\) as  

\[
u(P,T) - u(P_0,T) = \frac{Q + W}{n},
\]

provided that corrections have been made to take account of the energy changes due to the contraction of the walls of the container. In this way, the change of molar internal- energy \(\Delta u\) was measured for various values of the initial pressure \(P\) at constant temperature \(T\) . The values of \(\Delta u\) were plotted against the corresponding pressure \(P\) , as shown in Fig. 5- 3. Since \(u(P_{0},T)\) is constant, the slope of the resulting curve is equal to \((\partial u / \partial P)_{T}\) at any value of \(P\) . Within the pressure range of 1 to 40 standard atmospheres, the experimental points fall on a straight line, meaning that \((\partial u / \partial P)_{T}\) has the same value at every pressure; that is, \((\partial u / \partial P)_{T}\) is independent of the pressure, depending only on the temperature. Thus,  

\[
\left(\frac{\partial u}{\partial P}\right)_{T} = f(T).
\]

Rossini and Frandsen's experiments with air, oxygen, and mixtures of oxygen and carbon dioxide led to the conclusion that the internal energy of a real gas is a function of both temperature and pressure. They found no pressure or temperature range in which the quantity \((\partial u / \partial P)_{T}\) was equal to zero. In other words, their real gases did not reach the low- pressure limit of the ideal gas.  

Their experiment has somewhat the same disadvantage as Joule's original experiment, in that the heat capacity of the gas is much smaller than that of the calorimeter and water bath. To keep the temperature of the gas constant within reasonable limits, the temperature of the water must be kept constant to within less than a thousandth of a degree. In Rossini and Frandsen's measurements, the final precision was estimated to be \(2\frac{1}{2}\) percent.

===== Page 134 =====

112 PART I: Fundamental Concepts  

FIGURE 5-3 Dependence of change of molar internal energy of a real gas on pressure, where \(P_0\) is atmospheric pressure.  

### 5.3 IDEAL GAS  

We have seen that, in the case of a real gas, only in the limit as the pressure approaches zero does the equation of state assume the simple form \(PV = nRT\) . Furthermore, the internal energy of a real gas is a function of pressure as well as temperature. It is convenient at this point to define the ideal gas whose properties, while not corresponding to those of any existing gas, are approximately those of a real gas at low pressures. By definition, the ideal gas satisfies the equations  

\[
\left[\begin{array}{c}{PV=nRT\] \[\left(\frac{\partial U}{\partial P}\right)_{T}=0}\end{array}\right]\qquad(\mathrm{ideal~gas}). \quad (5.5)
\]

The requirement that \((\partial U / \partial P)_T = 0\) may be written in other ways. Thus,  

\[
\left(\frac{\partial U}{\partial V}\right)_T = \left(\frac{\partial U}{\partial P}\right)_T\left(\frac{\partial P}{\partial V}\right)_T,
\]

and since \((\partial P / \partial V)_T = - nRT / V^2 = - P / V\) , and, therefore, is not zero, while \((\partial U / \partial P)_T\) is zero, it follows that for the ideal gas

===== Page 135 =====

5: Ideal Gas 113  

\[
\left(\frac{\partial U}{\partial V}\right)_T = 0 \quad (\text{ideal gas}). \quad (5.6)
\]

Finally, since both \((\partial U / \partial P)_T\) and \((\partial U / \partial V)_T\) are zero,  

\[
U = f(T) \text{ only}. \quad (5.7)
\]

Whether a real gas may be treated as the ideal gas depends upon the error that may be tolerated in a given calculation. A real gas at pressures below about twice standard atmospheric pressure may be treated as the ideal gas without introducing an error greater than a few percent. Even in the case of a saturated vapor in equilibrium with its liquid, the ideal- gas equation of state may be used with only a small error if the vapor pressure is low.  

For an infinitesimal quasi- static process of a hydrostatic system, the first law is  

\[
\mathrm{d}Q = dU + P dV,
\]

and the heat capacity at constant volume is given by  

\[
C_V = \left(\frac{\partial U}{\partial T}\right)_V.
\]

In the special case of the ideal gas, \(U\) is a function of \(T\) only; therefore, the partial derivative with respect to \(T\) is the same as the total derivative. Consequently,  

\[
C_V = \frac{dU}{dT},
\]

and  

\[
\mathrm{d}Q = C_V dT + P dV. \quad (5.8)
\]

Now, all equilibrium states are represented by the ideal- gas equation,  

\[
P V = n R T,
\]

and, for an infinitesimal quasi- static process,  

\[
P d V + V d P = n R d T.
\]

Substituting the above in Eq. (5.8), we get  

\[
\mathrm{d}Q = (C_V + n R) d T - V d P,
\]

and dividing by \(dT\) yields  

\[
\frac{\mathrm{d}Q}{dT} = C_V + n R - V \frac{dP}{dT}.
\]

At constant pressure, the left- hand member becomes \(C_P\) and \(dP = 0\) ; therefore,  

\[
C_P = C_V + n R \quad (\text{ideal gas}). \quad (5.9)
\]

===== Page 136 =====

114 PART I: Fundamental Concepts  

We have the result, therefore, that the heat capacity of an ideal gas at constant pressure is always larger than the heat capacity at constant volume, the difference remaining constant and equal to \(nR\) . The reason that \(C_P\) is always larger than \(C_V\) is the following: As heat is supplied to a system at constant pressure, the gas expands and works against the external pressure, which, of course, is equal to the pressure of the gas in a quasi- static process. Thus, \(C_P\) includes work of expansion, which is not found in the constant volume \(\left(\int P dV = 0\right)\) heat capacity \(C_V\) .  

Since \(U\) is a function of \(T\) only for an ideal gas, it follows that  

\[
C_V = \frac{dU}{dT} = \mathrm{a~function~of~}T\mathrm{~alone},
\]

and so  

\[
C_P = C_V + nR = \mathrm{a~function~of~}T\mathrm{~alone}.
\]

One more useful equation can be obtained. Since  

\[
\mathrm{d}Q = (C_V + nR)dT - VdP,
\]

we find  

\[
\mathrm{d}Q = C_PdT - VdP. \quad (5.10)
\]

### 5.4 EXPERIMENTAL DETERMINATION OF HEAT CAPACITIES  

The heat capacities of real gases are measured by the electrical method. To measure \(C_V\) , the gas is contained in a thin- walled steel flask with a heating wire wound around it. By maintaining an electric current in the wire, an equivalent amount of heat is supplied to the gas, and the heat capacity at constant volume is obtained by measuring the temperature rise of the gas. The same method is used to measure \(C_P\) except that, instead of confining the gas to a constant volume, the gas is allowed to flow at constant pressure through a calorimeter, where it receives electrically a known equivalent heat per unit of time. From the initial (inlet) and final (outlet) temperatures, the rate of supply of heat, and the rate of flow of gas, the value of \(C_P\) is calculated.  

The results of such measurements on gases at low pressures, that is, ideal gases, can be stated in a simple manner in terms of molar heat capacities.  

1. All ideal gases:  

(a) \(c_V\) is a function of \(T\) only.  

(b) \(c_P\) is a function of \(T\) only, and is greater than \(c_V\) .  

(c) \(c_P - c_V\) is not a function of \(T\) , but equal to \(R\) .  

(d) the ratio \(c_P / c_V = \gamma\) is a function of \(T\) only, and is greater than 1.  

2. Monatomic gases, such as He, Ne, and A, and most metallic vapors, such as the vapors of Na, Cd, and Hg:

===== Page 137 =====

1) \(c_{V}\) is constant over a wide temperature range and is very nearly equal to \(\frac{3}{2} R\) .  

(b) \(c_{P}\) is constant over a wide temperature range and is very nearly equal to \(\frac{5}{2} R\) .  

(c) the ratio \(c_{P} / c_{V} = \gamma\) is constant over a wide temperature range and is very nearly equal to \(\frac{5}{3}\) .  

3. So-called permanent diatomic gases, namely, air, \(\mathrm{H}_{2}\) , \(\mathrm{D}_{2}\) , \(\mathrm{O}_{2}\) , \(\mathrm{N}_{2}\) , \(\mathrm{NO}\) , and \(\mathrm{CO}\) :  

(a) \(c_{V}\) is constant at ordinary temperatures, being equal to about \(\frac{5}{2} R\) , and increases as the temperature is raised.  

(b) \(c_{P}\) is constant at ordinary temperatures, being equal to about \(\frac{7}{2} R\) , and increases as the temperature is raised.  

(c) the ratio \(c_{P} / c_{V} = \gamma\) is constant at ordinary temperatures, being equal to about \(\frac{7}{2}\) , and decreases as the temperature is raised.  

4. Polyatomic gases and gases that are chemically active, such as \(\mathrm{CO}_{2}\) , \(\mathrm{NH}_{3}\) , \(\mathrm{CH}_{4}\) , \(\mathrm{Cl}_{2}\) , and \(\mathrm{Br}_{2}\) :  

\(c_{P}\) , \(c_{V}\) , and \(c_{P} / c_{V}\) vary with the temperature, the variation being different for each gas.  

These experimental results indicate that the molar gas constant \(R = 8.315 \mathrm{J / mol \cdot K}\) is a natural unit with which to express the molar heat capacity of a gas. It is a very interesting consequence of theory that the universal gas constant is also the natural unit for solids. In the remainder of this book, we shall specify not the molar heat capacities themselves but the ratios \(c_{V} / R\) and \(c_{P} / R\) .  

The behavior of hydrogen gas \(\mathrm{(H_{2})}\) is quite exceptional, as shown in Fig. 5- 4. At very low temperatures, \(c_{P} / R\) drops to a value of \(\frac{5}{2}\) , appropriate to a monatomic gas, even though hydrogen is a diatomic gas. At room temperature, \(c_{P} / R\) for hydrogen has its expected value of \(\frac{7}{2}\) . For all other diatomic gases, \(c_{P} / R\) may always be written  

\[
\frac{c_{P}}{R} = \frac{7}{2} +f(T),
\]

where \(f(T)\) is often one or more functions of the type  

\[
\left(\frac{b}{T}\right)^{2}\frac{e^{b / T}}{(e^{b / T} - 1)^{2}}.
\]

Exact equations of the above type are difficult to handle and are not suitable for the practical calculations of the laboratory scientist; consequently, approximate empirical equations are used. Empirical equations for \(c_{P} / R\) of some of the most important gases, compiled by H. M. Spencer, are given in Table 5.2, within the temperature range 300 to 1500 K.

===== Page 138 =====

116 PART I: Fundamental Concepts  

FIGURE 5-4  

Experimental values of \(c_{P} / R\) for hydrogen as a function of temperature, plotted on a logarithmic scale.  

TABLE 5.2 \(c_{P} / R\) of important gases \(c_{P} / R = a + bT + cT^{2}\) (from 300 to 1500 K)   

Gasab, 10-3 K-1c, 10-6 K-2H23.495-0.1010.243O23.0681.638-0.512Cl23.8131.220-0.486Br24.2400.490-0.179N23.2470.712-0.041CO3.1920.924-0.141HCl3.3890.2180.186HBr3.3110.4810.079CO23.2065.082-1.714H2O3.6341.1950.135NH33.1163.970-0.366H2S3.2142.871-0.608CH41.7029.083-2.164

### 5.5 QUASI-STATIC ADIABATIC PROCESS  

When an ideal gas undergoes a quasi- static adiabatic process, the pressure, volume, and temperature change in a manner that is described by a relation between \(P\) and \(V\) , \(T\) and \(V\) , or \(P\) and \(T\) . In order to derive the relation between \(P\) and \(V\) , we start with Eqs. (5.8) and (5.10). Thus,

===== Page 139 =====

和  

\[
\mathrm{d}Q = C_{V}dT + P dV,
\]

\[
\mathrm{d}Q = C_{P}dT - VdP.
\]

In an adiabatic process, \(\mathrm{d}Q = 0\) , so  

\[
V d P = C_{P}d T,
\]

and  

\[
P d V = -C_{V}d T.
\]

Dividing the first equation by the second, we obtain  

\[
\frac{dP}{P} = -\frac{C_{P}}{C_{V}}\frac{dV}{V},
\]

and denoting the ratio of the heat capacities by the symbol \(\gamma\) , we have  

\[
\frac{dP}{P} = -\gamma \frac{dV}{V}.
\]

This equation cannot be integrated until we know the structure of the gas, which determines \(\gamma\) . We have seen that for monatomic gases, \(\gamma\) is constant. For diatomic and polyatomic gases, \(\gamma\) varies with the temperature; a very large change of temperature produces an appreciable change in \(\gamma\) . For example, in the case of the carbon monoxide, a temperature rise from 300 to 3000 K produces a decrease in \(\gamma\) from 1.40 to 1.29. Most adiabatic processes that we encounter do not involve such a large temperature change. Therefore, in an adiabatic process that involves only a moderate temperature change, we are entitled to neglect the small accompanying change in \(\gamma\) . Regarding \(\gamma\) , therefore, as constant, and integrating, we obtain  

\[
\ln P = -\gamma \ln V + \ln \mathrm{const.},
\]

or  

\[
P V^{\gamma} = \mathrm{const.} \quad (5.11)
\]

This equation of state holds at all equilibrium states through which the ideal gas passes during a quasi- static adiabatic process. It is important to understand that a free expansion is an adiabatic process but is not quasi- static, because the gas rushing into the vacuum passes through nonequilibrium states before finally achieving equilibrium. Therefore, Eq. (5.11) cannot be applied to the states traversed by the ideal gas during a free expansion or any adiabatic process that is not quasi- static.  

A family of curves representing quasi- static adiabatic processes may be plotted on a \(P V\) diagram by assigning different values to the constant in Eq. (5.11). The slope of any adiabatic curve is  

\[
\left(\frac{\partial P}{\partial V}\right)_{S} = -\gamma \mathrm{const.} V^{-\gamma -1}
\]

or  

\[
\left(\frac{\partial P}{\partial V}\right)_{S} = -\gamma \frac{P}{V}, \quad (5.12)
\]

where the subscript \(S\) is used to denote a reversible adiabatic process.

===== Page 140 =====

118 PART I: Fundamental Concepts  

FIGURE 5-5 The \(PVT\) surface for the ideal gas and its projection onto a \(PV\) diagram. (Isotherms are shown as dashed curves, and adiabatics as full curves.)  

Quasi- static isothermal processes are represented by a family of equilateral hyperbolas obtained by assigning different values to \(T\) in the equation \(PV = nRT\) . Since  

\[
\left(\frac{\partial P}{\partial V}\right)_T = -\frac{P}{V}, \quad (5.13)
\]

it follows that an adiabatic curve has a steeper negative slope than does an isothermal curve at the same point, since \(\gamma > 1\) .  

The isothermal curves and adiabatic curves of the ideal gas may be shown in a revealing way on a \(PVT\) surface. If \(P\) , \(V\) , and \(T\) are plotted along rectangular axes, the resulting surface is shown in Fig. 5- 5, where it may be seen that the adiabatic curves cut across the isotherms.  

### 5.6 RUCHHARDT'S METHOD OF MEASURING \(\gamma\)  

An ingenious method of measuring \(\gamma\) , developed by Rüchhardt in 1929, makes use of elementary mechanics, rather than thermodynamics. The gas is contained in a large jar of volume \(V\) . Fitted to the jar (see Fig. 5- 6) is a glass tube with an accurate bore of cross- sectional area \(A\) , into which a metal ball of mass \(m\) fits snugly like a piston. Since the gas is slightly compressed by the

===== Page 141 =====

 FIGURE 5- 6 Mechanical apparatus for measuring the ratio of heat capacities \(\gamma\) . (E. Rüchhardt: Physikalische Zeitschrift, vol. 30, pp. 58- 59, 1929. )  

steel ball in its equilibrium position, its pressure \(P\) is slightly larger than atmospheric pressure \(P_{0}\) . Thus, neglecting friction,  

\[
P = P_{0} + \frac{mg}{A}.
\]

If the ball is given a slight downward displacement and then let go, it will oscillate with a period \(\tau\) . Friction will cause the ball to come to rest eventually. Let the displacement of the ball from its equilibrium position at any moment be denoted by \(y\) , where \(y\) is positive when the ball is above the equilibrium position and negative below. A small positive displacement causes an increase in volume which is very small compared with the equilibrium volume \(V\) and which, therefore, can be denoted by \(dV\) , where  

\[
dV = yA.
\]

Similarly, a small positive displacement causes a decrease in pressure which is very small compared with the equilibrium pressure \(P\) and which, therefore, can be denoted by \(dP\) , where \(dP\) is a negative quantity. The resultant force \(F\) acting on the ball is equal to \(A dP\) if we neglect friction, or  

\[
dP = \frac{F}{A}.
\]

Notice that, when \(y\) is positive, \(dP\) is negative and, therefore, \(F\) is negative; that is, \(F\) is a restoring force.  

Now, as the ball oscillates fairly rapidly, the variations of \(P\) and \(V\) are adiabatic, because there is not enough time for appreciable heat transfer. Since the variations are also quite small, the states through which the gas passes can be considered to be approximately states of equilibrium. Therefore, we may assume that the changes of \(P\) and \(V\) represent an approximately quasi- static adiabatic process, and we may write

===== Page 142 =====

120 PART I: Fundamental Concepts  

\[
PV^{\gamma} = \mathrm{const.},
\]

and  

\[
\gamma PV^{\gamma -1}dV + V^{\gamma}dP = 0.
\]

Substituting for \(dV\) and \(dP\) , we get  

\[
F = -\frac{\gamma P A^{2}}{V} y.
\]

This equation expresses the fact that the restoring force is directly proportional to the displacement and is in the opposite direction, which is Hooke's law. This is precisely the condition for simple harmonic motion, for which the period \(\tau\) is  

\[
\tau = 2\pi \sqrt{\frac{m}{-F / y}}.
\]

Consequently,  

\[
\tau = 2\pi \sqrt{\frac{mV}{\gamma P A^{2}}},
\]

and, as a result,  

\[
\gamma = \frac{4\pi^{2}m V}{A^{2}P\tau^{2}}. \quad (5.14)
\]

The mass of the ball, the volume, the cross- sectional area of the tube, and the pressure are all known beforehand, and only the period has to be measured to obtain \(\gamma\) . The values obtained by Rüchhardt's mechanical measurements for air and for \(\mathrm{CO}_{2}\) were in good agreement with those obtained from calorimetric measurements of heat capacities.  

Rüchhardt's method involves errors due to three simplifying assumptions: (1) that the gas is ideal; (2) that there is no friction; and (3) that volume changes are strictly adiabatic. It is estimated that the second assumption is responsible for the largest error, amounting to about 3 percent.  

A modification of Rüchhardt's experiment in which accurate account is taken of the real equation of state of the gas, the friction present, and the departure from strict adiabatic conditions, was achieved by Clark and Katz in 1940. The method was adapted for an undergraduate teaching laboratory by D. G. Smith in 1979. A steel piston at the center of a cylindrical tube divides the gas into two equal parts, as shown in Fig. 5- 7. It is set in vibration at any desired frequency by external coils in which an alternating current of suitable frequency is maintained. The cylinder is kept in a horizontal position, and friction between the piston and the cylinder is reduced by balancing the weight of the piston by the attraction of an electromagnet.  

The amplitude of vibration of the piston is measured, using a microscope equipped with a micrometer eyepiece, at a number of values of the frequency of the impressed alternating current, and the resonance curve is plotted. From the resonance frequency and very elaborate calculations not involving the assumptions made by Rüchhardt, the value of \(\gamma\) is calculated. Since friction

===== Page 143 =====

 FIGURE 5-7 Resonance method of measuring the ratio of heat capacities \(\gamma\) of a real gas as a function of pressure. (A. L. Clark and L. Katz: Canadian Journal of Research, ser. A, vol. 21, pp. 1-17, 1943. )  

TABLE 5.3 Pressure variation of \(\gamma\) \(\gamma = a + bP + cP^{2})\)   

GasTemp., Kab, 10-9 Pa-1c, 10-12 Pa-2γ extrapolated to zero pressure (ideal gas)He296.251.6669-1.9701.667Ar297.351.666734.801.667H2296.551.40452.4701.405N2296.151.400621.801.401CO2303.051.285762.101.286N2O298.451.274422.20.09481.274CH4298.251.3029-10.40.04721.303  

was reduced to a great extent by the lift magnet, the corrections amounted to only about 1 percent. The authors measured \(\gamma\) at various pressures from 1 to 25 standard atmospheric pressures and expressed the results in the form of empirical equations, as shown in Table 5.3.  

### 5.7 VELOCITY OF A LONGITUDINAL WAVE  

Let us consider a gas enclosed in a cylinder and held in place by a piston exerting pressure \(P\) , as shown in the upper part of Fig. 5- 8. If a compression is produced by moving the piston to the right at constant velocity \(w_{0}\) , the wave

===== Page 144 =====

122 PART I: Fundamental Concepts  

FIGURE 5-8  

Propagation of a compression with constant velocity \(w\) through a gas caused by the motion of a piston with constant velocity \(w_{0}\) . Upper diagram at the start; lower diagram after time \(t\) .  

front of the pressure pulse will travel with a different constant velocity \(w\) , depending on properties of the gas that we shall now proceed to determine. The "free body" for Newton's second law is volume \(V\) of the gas whose initial uncompressed length is \(w t\) and whose uncompressed volume \(V = A w t\) , where \(A\) is the cross- sectional area of the cylinder. If \(\rho\) is the density of the normal or uncompressed gas, the mass of the free body is \(\rho A w t\) .  

Let us suppose that the piston shown in the lower part of Fig. 5- 8 exerts a force \(A(P + \Delta P)\) as the piston moves to the right with a constant velocity \(w_{0}\) . The compression moves with constant velocity \(w\) , so that in time \(t\) the compression has traveled a distance \(w t\) while the piston has traveled a distance \(w_{0} t\) . At time \(t\) ,  

\[
\text{Rate of increase of mass} \left\{ \begin{array}{l} \rho A w t \\ \displaystyle \frac{\rho A w t}{t} = \rho A w. \end{array} \right.
\]

The entire compressed column has a velocity \(w_{0}\) equal to that of the piston. Therefore,  

\[
\text{Rate of increase of momentum} \left\{ \begin{array}{l} \rho A w w_{0}. \\ \displaystyle \frac{\rho A w w_{0}}{t} = \rho A w w_{0}. \end{array} \right.
\]

The free body is acted on by a force \(A(P + \Delta P)\) to the right and a force \(A P\) to the left. Therefore,

===== Page 145 =====

 Unbalanced force on the \(\left\{ \begin{array}{l} \text { compressed column } \\ \text { compressed column } \end{array} \right\} = A \Delta P.\)  

From Newton's second law, the unbalanced force is equal to the rate of change of momentum,  

\[
A \Delta P = \rho A w w_{0},
\]

or  

\[
\Delta P = \rho w^{2} \frac{w_{0}}{w}.
\]

The "uncompressed free body" of volume \(V = A w t\) has undergone a compression \((- \Delta V) = A w_{0} t\) . That is,  

\[
-\frac{\Delta V}{V} = \frac{A w_{0} t}{A w t} = \frac{w_{0}}{w}.
\]

Therefore,  

\[
\Delta P = \rho w^{2}\left(-\frac{\Delta V}{V}\right),
\]

which may be written  

\[
w^{2} = \frac{-1}{\frac{\rho}{V}\left(\frac{\Delta V}{\Delta P}\right)}. \quad (5.15)
\]

This formula was first obtained by Newton, who regarded the quantity \((1 / V)(\Delta V / \Delta P)\) as the isothermal compressibility. It was shown later by Laplace that the expression is really the adiabatic compressibility. To see why this is so, let us consider a column of gas of cross section \(A\) , bounded by two planes, one at the center of a compression and the other at the center of a rarefaction, a distance \(\lambda /2\) apart, where \(\lambda\) is the wavelength. Let us suppose that the temperature at the center of the compression exceeds the temperature at the center of the rarefaction by an amount \(\Delta T\) . Then, the heat conducted a distance \(\lambda /2\) in the time \(\lambda /2 w\) (time for the wave to travel the distance \(\lambda /2\) ) is given by  

\[
\mathrm{Heat~conducted~in~the~time~for~the~}\left\{ \begin{array}{l l}{K A\frac{\Delta T}{\lambda / 2}\frac{\lambda}{2w} = K A\frac{\Delta T}{w},} \end{array} \right.
\]

where \(K\) is the thermal conductivity of the medium. The mass of material between the compression and rarefaction is \(\rho A \lambda /2\) , and the heat necessary to raise the temperature of this mass by the amount \(\Delta T\) is  

\[
\mathrm{Heat~necessary~to~raise~temperature~}\left\{ \begin{array}{l l}{\lambda\] \[\lambda\] \[\lambda} \end{array} \right\} = \rho A \frac{\lambda}{2} c_{V} \Delta T,
\]

where \(c_{V}\) is the molar heat capacity at constant volume.  

The propagation of the wave would be adiabatic if the conducted heat were much too small to raise the temperature of the mass \(\rho A \lambda /2\) by the amount \(\Delta T\) , or

===== Page 146 =====

124 PART I: Fundamental Concepts  

\[
\frac{K A\Delta T}{w}\ll \rho A\frac{\lambda}{2} c_{V}\Delta T\qquad \mathrm{(adiabatic~condition)}. \quad (adiabatic condition).
\]

This may be written  

\[
\frac{2K}{w\rho c_{V}}\ll \lambda \qquad \mathrm{(adiabatic~condition)}. \quad (adiabatic condition).
\]

The usual range of wavelengths of compressional waves is from a few centimeters to a few hundred centimeters. Let us compare these values with \(2K / w\rho c_{V}\) . Taking a gas like air as a typical case, we have, roughly,  

\[
K = 0.02\mathrm{W / m\cdot K}, w = 3\times 10^{2}\mathrm{m / s}, \rho = 1\mathrm{kg / m^{3}}, c_{V} = 0.4\mathrm{kJ / kg\cdot K},
\]

and  

\[
\frac{2K}{w\rho c_{V}} = \frac{2(0.02\mathrm{W / m\cdot K})}{(3\times 10^{2}\mathrm{m / s})(1\mathrm{kg / m^{3}})(0.4\mathrm{kJ / kg\cdot K})} = 330\times 10^{-9}\mathrm{m} = 330\mathrm{nm}
\]

In the case of a metal, \(K\) would be much larger, but this would be compensated by the much larger values of \(w\) and \(\rho\) , and the quantity \(2K / w\rho c_{V}\) would be still smaller than \(330\mathrm{nm}\) . This quantity is, therefore, seen to be so much smaller than the usual value of a wavelength of a compressional wave (330nm is the wavelength of ultraviolet light) that the adiabatic condition is well fulfilled. Therefore, we conclude that, in view of the properties of ordinary matter, the volume changes which take place under the influence of a longitudinal wave at ordinary frequencies are adiabatic, not isothermal.  

Returning now to Eq. (5.15) for the velocity of a longitudinal wave and identifying \((- 1 / V)(\Delta V / \Delta P)\) as the reversible adiabatic compressibility \(\kappa_{S}\) , we have, finally,  

\[
w^{2} = \frac{1}{\rho\kappa_{S}}. \quad (5.16)
\]

The adiabatic compressibility can be calculated for the ideal gas using Eq. (5.12); thus,  

\[
\kappa_{S} = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{S} = \frac{1}{\gamma P}.
\]

Since the density is

===== Page 147 =====

1 \(\rho = \frac{M}{\nu},\) where \(M\) is the molar mass and the \(\nu\) is the molar volume, Eq. (5.16) becomes  

\[
w^{2} = \frac{\gamma P\nu}{M},
\]

\[
w^{2} = \frac{\gamma RT}{M}. \quad (5.17)
\]

Equation (5.17) allows us to calculate \(\gamma\) from experimental measurements of \(w\) and \(T\) . For example, the speed of sound in air at \(0^{\circ}\mathrm{C}\) is about \(331~\mathrm{m / s}\) . Therefore, using the values  

\[
w = 331\mathrm{m / s}, T = 273\mathrm{K}, R = 8.31\mathrm{J / mol}\cdot \mathrm{K}, M = 0.029\mathrm{kg / mol},
\]

we get  

\[
\gamma = \frac{Mw^2}{RT} = \frac{(0.029\mathrm{kg / mol})(331\mathrm{m / s})^2}{(8.31\mathrm{J / mol}\cdot\mathrm{K})(273\mathrm{K})} = 1.40.
\]

The speed of a sound wave in a gas can be measured roughly by means of Kundt's tube. The gas is admitted to a horizontal cylinder tube, closed at one end and supplied at the other end with a movable piston capable of being set in vibration parallel to the axis of the tube. In the tube is a small amount of light powder. For a given frequency, a position of the piston can be found at which standing waves are set up. Under these conditions, small heaps of powder pile up at the nodes. The distance between any two adjacent nodes is one- half a wavelength, and the speed of the waves is the product of the frequency and the wavelength. Values of \(\gamma\) obtained by this mechanical method are in good agreement with those obtained from measurements of heat capacity.  

Much greater accuracy is achieved by replacing Kundt's tube with an acoustic interferometer, at one end of which is a source of waves such as a piezoelectric crystal and at the other end a receiver. When the distance between source and receiver is kept constant and the frequency varied, the various resonances corresponding to different numbers of antinodes are noted. The frequency of the compressional waves can be varied from audible to ultrasonic frequency, but corrections for errors due to viscosity, heat conduction, and boundary layer absorption must be applied.  

Equation (5.17) can be used to determine the molar gas constant \(R\) by plotting the square of the speed of sound as a function of pressure. Then, in

===== Page 148 =====

126 PART I: Fundamental Concepts  

the limit of zero pressure, which assures ideal- gas conditions, Eq. (5.17) becomes  

\[
R = \frac{Mw_0^2}{\gamma T}, \quad (5.18)
\]

where \(w_0^2\) is the extrapolation of the square of the speed of sound to zero pressure. In 1984, A. R. Colclough and colleagues at the National Physical Laboratory in England used an acoustic interferometer operating at the only defined temperature, namely, the triple point of water at \(273.16 \mathrm{~K}\) , to determine \(w_0^2\) for argon, a monatomic gas for which \(\gamma = \frac{5}{3}\) . The Committee on Data for Science and Technology used the value of \(w_0^2 = 94,756.75 \mathrm{~m}^2 / \mathrm{s}^2\) to calculate a new value of the molar gas constant \(R\) in its 1986 table of fundamental physical constants, namely, \(R\) equals \(8.314510 \mathrm{~J} / \mathrm{mol} \cdot \mathrm{K}\) , with an uncertainty of \(8.4\) parts per million. All the earlier data, including the 1973 recommendation based on Batuecas' measurement of \(R\) based on Eq. (5.3), were excluded in the determination of the latest value of the molar gas constant. Systematic errors were introduced by the presence of water adsorbed on the surface of the gas container, which could not be accounted for in an error analysis.  

## 5.8 THE MICROSCOPIC POINT OF VIEW  

We have emphasized that the point of view of classical thermodynamics is entirely macroscopic. Systems are described with the aid of their gross, or large- scale, properties. The first law of thermodynamics is a relation among the fundamental physical quantities of work, internal energy, and heat. When the first law is applied to a class of systems, a general relation is obtained which holds for any member of the class but which contains no quantities or properties of a particular system that would distinguish it from another. For example, Eq. (4.13),  

\[
C_V = \left(\frac{\partial U}{\partial T}\right)_V,
\]

is true for all hydrostatic systems, whether solid, liquid, or gas. It enables one to calculate \(C_V\) of a hydrostatic system, provided that one knows the internal energy as a function of \(T\) and \(V\) . The heat transferred during an isochoric process, Eq. (4.16), which is  

\[
Q_V = \int_{T_i}^{T_f} C_V dT,
\]

may be calculated once the \(C_V\) of the particular system under consideration is known as a function of \(T\) . But there is nothing in classical thermodynamics that provides detailed information concerning \(U\) or \(C_V\) .

===== Page 149 =====

 Another example of the limitation of classical thermodynamics is its inability to provide the equation of state of any desired system. To make use of any thermodynamic equation involving \(P, V, T\) , and the derivatives \((\partial P / \partial V)_{T}\) , \((\partial V / \partial T)_{P}\) , and \((\partial T / \partial P)_{V}\) , one must have an equation of state. Experimental values are very often useful, but there are occasions when it is not feasible to perform the necessary experiments. If an experiment is performed on, let us say, oxygen, the numerical constants in the equation of state of oxygen only are obtained, and no clue is at hand concerning the values of the constants for any other gas.  

To obtain detailed information concerning the thermodynamic coordinates and thermal properties of systems without having to resort to experimental measurements, we require calculations based on the properties and behavior of the particles of the system. There are two such microscopic theories: one is called kinetic theory, and the other is statistical mechanics. Both theories deal with particles, their internal and external motion, their collisions with one another and with any existing walls, and their forces of interaction. Making use of the laws of mechanics and statistics, kinetic theory concerns itself with the average motion of atoms and their collisions with walls and other objects in order to calculate the equation of state for the ideal gas. Statistical mechanics avoids the mechanical aspects of particles and deals with the energy aspects of aggregates or ensembles of particles. It relies heavily on statistics and quantum mechanics. Only equilibrium states can be handled — but in a uniform, straightforward manner, so that once the energy levels of the atom or of systems of atoms are understood, a program of calculations yields the equation of state, the energy, and other thermodynamic functions as well.  

In this chapter, we shall limit ourselves to a small part of the kinetic theory of the ideal gas. Statistical mechanics will be presented in Chap. 12.  

### 5.9 KINETIC THEORY OF THE IDEAL GAS  

The kinetic theory of gases was the result of the early nineteenth century work of Avogadro and Loschmidt, who calculated the number of atoms or molecules in a molar volume of a gas. In unpublished work, Waterston recognized that temperature is a function of the motion of the particles of a gas, but Krönig is commonly recognized as the originator of the kinetic theory of gases in 1856. In order to formulate a microscopic theory of gases, which will be limited to monatomic gases, several simplifying assumptions about the behavior of atoms of the ideal gas are made:  

1. Any small sample of gas consists of an enormous number of particles \(N\) . For any one chemical species, all atoms are identical and inert. If \(m\) is the mass of each atom, then the total mass is \(mN\) . If \(M\) denotes the molar mass

===== Page 150 =====

128 PART I: Fundamental Concepts  

in kilograms per mole (formerly called the atomic or molecular weight), then the number of moles \(n\) is given by  

\[
n = \frac{mN}{M}.
\]

The number of particles per mole of gas is called Avogadro's number \(N_{\mathrm{A}}\) where  

\[
N_{\mathrm{A}} = \frac{N}{n} = \frac{M}{m} = 6.0221\times 10^{23}\frac{\mathrm{particles}}{\mathrm{mole}}.
\]

Since a mole of ideal gas at the freezing point of water and at standard atmospheric pressure occupies a volume of \(22.4\times 10^{3}\mathrm{cm}^{3}\) , there are approximately \(3\times 10^{19}\) atoms in a volume of only \(1\mathrm{cm}^{3}\) \(3\times 10^{16}\) atoms per cubic millimeter, and even a volume as small as a cubic micrometer contains as many as \(3\times 10^{7}\) atoms.  

2. The atoms of an ideal gas are supposed to resemble small hard spheres that are in perpetual random motion. Within the temperature and pressure range of an ideal gas, the average distance between neighboring atoms is large compared with the size of an atom. The diameter of an atom is of the order of 2 or \(3\times 10^{-10}\mathrm{m}\) . Under standard conditions, the average distance between atoms is about 50 times their diameter.  

3. The atoms of an ideal gas are assumed to exert no forces of attraction or repulsion on other atoms except when they collide with one another and with a wall. Between collisions, they therefore move with uniform rectilinear motion.  

4. The portion of a wall with which an atom collides is considered to be smooth, and the collision is assumed to be perfectly elastic. If \(w\) is the speed of an atom approaching a wall, only the perpendicular component of velocity \(w_{\perp}\) is changed upon collision with the wall, from \(w_{\perp}\) to \(-w_{\perp}\) , or a total change of \(-2w_{\perp}\) .  

5. When there is no external field of force, the atoms are distributed uniformly throughout a container. The number density \(N / V\) is assumed constant, so that in any small element of volume \(dV\) there are \(dN\) atoms, where  

\[
dN = \frac{N}{V} dV.
\]

The infinitesimal \(dV\) must satisfy the same conditions in kinetic theory as in thermodynamics, namely, that it is small compared with \(V\) but large enough to make \(dN\) a large number. If, for example, a volume of \(1\mathrm{cm}^{3}\) contains \(10^{19}\) atoms, then one- millionth of a cubic centimeter would still contain \(10^{13}\) atoms and would qualify as a differential volume element.  

6. There is no preferred direction for the velocity of any atom, so that at any moment there are as many atoms moving in one direction as in another.  

7. Not all atoms have the same speed. A few atoms at any moment move slowly and a few move very rapidly, so that speeds may be considered to cover the

===== Page 151 =====

 range from zero to the speed of light. Since most atomic speeds are so far below the speed of light, no error is introduced in integrating the speed from 0 to \(\infty\) . If \(dN_{w}\) represents the number of atoms with speeds between \(w\) and \(w + dw\) , it is assumed that \(dN_{w}\) remains constant at equilibrium, even though the atoms are perpetually colliding and changing their speeds.  

Since the velocity vectors of the atoms of gas have no preferred direction, consider an arbitrary velocity vector \(w\) directed from the point \(O\) in Fig. 5- 9 to the elementary area \(dA^{\prime}\) . It is important to know how many atoms have velocity vectors in the neighborhood of \(w\) . The calculation of this quantity involves the concept of a solid angle. Taking \(O\) as the origin of polar coordinates \(r\) , \(\theta\) , and \(\phi\) , we construct a sphere of radius \(r\) . The area \(dA^{\prime}\) on the surface of this sphere, formed by two circles of latitude differing by \(d\theta\) and two circles of longitude differing by \(d\phi\) , has the magnitude  

\[
dA^{\prime} = (r d\theta)(r \sin \theta d\phi).
\]

The solid angle \(d\Omega\) , formed by lines radiating from \(O\) and touching the edge of \(dA^{\prime}\) , is by definition  

\[
d\Omega = \frac{dA^{\prime}}{r^{2}} = \frac{(r d\theta)(r \sin \theta d\phi)}{r^{2}}.
\]

or  

\[
d\Omega = \sin \theta d\theta d\phi . \quad (5.19)
\]

FIGURE 5-9 The solid angle \(d\Omega = \sin \theta d\theta d\phi\) .

===== Page 152 =====

130 PART I: Fundamental Concepts  

Since the largest area on the surface of the sphere is that of the entire sphere \(4\pi r^2\) , the maximum solid angle is \(4\pi\) sr (steradians).  

The fraction of atoms with velocity vectors in the neighborhood of \(\mathbf{w}\) will have speeds between \(w\) and \(w + dw\) and directions within the solid angle \(d\Omega\) about \(\mathbf{w}\) . If \(dN_w\) is the number of atoms with speeds between \(w\) and \(w + dw\) then the fraction of these atoms whose directions lie within the solid angle \(d\Omega\) is \(d\Omega /4\pi\) , so that the number of atoms within the speed range \(dw\) , in the \(\theta\) range of \(d\theta\) and the \(\phi\) range of \(d\phi\) , is given by  

\[
d^3 N_{w,\theta ,\phi} = dN_w\frac{d\Omega}{4\pi}, \quad (5.20)
\]

an equation expressing the fact that atomic velocities have no preferred direction.  

Now consider this group of atoms approaching a small area \(dA\) of the wall of the containing vessel. Many of these atoms will undergo collisions along the way, but if we consider only those members of the group that lie within the cylinder (Fig. 5- 10) whose side is of length \(wdt\) , where \(dt\) is such a short time interval that no collisions are made, then all the \(d^3 N_{w,\theta ,\phi}\) atoms within this cylinder will collide with \(dA\) . The volume of the cylinder \(dV\) is  

\[
dV = wdt\cos \theta dA, \quad (5.21)
\]

and if \(V\) is the total volume of the container, only the fraction \(dV / V\) of the atoms will be contained within the cylinder. Therefore the number of atoms (speed range, \(dw\) ; \(\theta\) range, \(d\theta\) ; \(\phi\) range, \(d\phi\) ) striking \(dA\) in time \(dt\) is expressed as  

\[
\mathrm{No.~of~}w,\theta ,\phi \mathrm{~atoms~striking~}dA\mathrm{~in~time~}dt = d^3 N_{w,\theta ,\phi}\frac{dV}{V}, \quad (5.22)
\]

which expresses the fact that atoms have no preferred location.  

According to our fundamental assumptions, an atomic collision is perfectly elastic. It follows, therefore, that an atom moving with speed \(w\) in a direction making an angle \(\theta\) with the normal to a wall will undergo a change only in its perpendicular component of velocity, as shown in Fig. 5- 10. Furthermore, it follows that the total change in momentum per collision is  

Change of momentum per collision \(= - 2mv\) cos \(\theta\) . (5.23)  

Total change of momentum = [No. of atoms of speed w in solid angle dOmega] [Fraction of these atoms striking dA in time dt] [Change in momentum per collision] = (dN_w / 4pi dOmega / 4pi) (dV / V) (-2mw cos theta) = (dN_w / 4pi sin theta dtheta dphi) (1/V w dt cos theta dA) (-2mw cos theta)

===== Page 153 =====

 FIGURE 5- 10 All the atoms in the cylinder of length \(w dt\) strike the area \(dA\) at the angle \(\theta\) to the normal. The perpendicular component of velocity \(w \cos \theta\) is reversed, but the parallel component \(w \sin \theta\) is unchanged.  

The change in momentum per unit time and per unit area due to collisions from all directions is the pressure \(dP_{w}\) exerted by the wall on the \(dN_{w}\) gas atoms. Reversing the sign of the momentum change, we get the pressure \(dP_{w}\) exerted by the \(dN_{w}\) atoms on the wall:  

\[
dP_{w} = mw^{2}\frac{dN_{w}}{V}\left(\frac{1}{2\pi}\int_{0}^{2\pi}d\phi \int_{0}^{\pi /2}\cos^{2}\theta \sin \theta d\theta\right). \quad (5.24)
\]

The quantity in parentheses may be integrated at sight and is found to be \(\frac{1}{3}\) , so that the total pressure due to atoms of all speeds is given by  

\[
PV = \frac{1}{3} m\int_{0}^{\infty}w^{2}dN_{w}.
\]

===== Page 154 =====

132 PART I: Fundamental Concepts  

The average of the square of the atomic speeds \(\langle w^2 \rangle\) is defined to be  

\[
\langle w^2 \rangle = \frac{1}{N} \int_0^\infty w^2 dN_w, \quad (5.25)
\]

so that we have  

\[
PV = \frac{Nm}{3} \langle w^2 \rangle . \quad (5.26)
\]

From the macroscopic point of view, at the beginning of this chapter, we saw that the experimental equation of state of the ideal gas is given by Eq. (5.4),  

\[
PV = nRT.
\]

From the microscopic point of view of the kinetic theory of the ideal gas, we found Eq. (5.26). A comparison of these two equations leads to  

\[
\frac{Nm}{3} \langle w^2 \rangle = nRT.
\]

The average kinetic energy of the gas atoms is \(\frac{1}{2} m \langle w^2 \rangle\) . Solving for \(T\) , we find  

\[
T = \frac{2N}{3nR} \left(\frac{1}{2} m \langle w^2 \rangle\right). \quad (5.27)
\]

Equation (5.27) provides an interpretation of temperature based on kinetic theory: Temperature is proportional to the average kinetic energy of the atoms in the ideal gas.  

In kinetic theory, it is assumed that atoms behave as noninteracting particles, so the potential energy of their interaction may be neglected. The only form of energy these particles may possess is translational kinetic energy. They may not possess, for example, rotational or vibrational energies. Therefore, the internal energy \(U\) of the ideal monatomic gas is the sum of the kinetic energies of all its atoms:  

\[
U = \sum_{j} \frac{1}{2} m w_j^2 = N \left(\frac{1}{2} m \langle w^2 \rangle\right).
\]

Using Eq. (5.27) to replace the kinetic energy, we obtain a calculated expression for the internal energy of a monatomic ideal gas,  

\[
U = \frac{3}{2} nRT. \quad (5.28)
\]

The interpretation of Eq. (5.28) is that the internal energy of the ideal monatomic gas, calculated from the kinetic theory of gases, is proportional to the thermodynamic temperature \(T\) only, in agreement with the experimental result expressed in Eq. (5.7). In the kinetic theory of gases, the concept of temperature is primarily a foreign element, since, in fact, the individual atoms are characterized by their speed alone. But, it is suggestive that we should

===== Page 155 =====

 define the ideal- gas temperature \(T\) in terms of the mean kinetic energy. The importance of Eq. (5.28) is that it has been derived from the laws of physics and statistics, rather than being formulated from experimental data.  

As a result of Eq. (5.28), there is an explicit calculated function for \(U(T)\) for an ideal monatomic gas. One can now calculate \(C_{V}\) from Eq. (4.13), with the result that \(C_{V} = \frac{3}{2} nR\) , that is, \(C_{V}\) is independent of temperature. From Eq. (5.9), \(C_{P}\) is also independent of temperature and, for a monatomic gas, \(C_{P} = \frac{5}{2} nR\) .  

Equation (5.28) can be rewritten using the relation of the number of particles per mole, \(n = N / N_{\mathrm{A}}\) , where \(N_{\mathrm{A}}\) is Avogadro's number; thus,  

\[
k = \frac{R}{N_{\mathrm{A}}} = 1.3807\times 10^{-23}\mathrm{J / K},
\]

where \(k\) is Boltzmann's constant, given by  

\[
U = \frac{3}{2}\frac{N}{N_{\mathrm{A}}} RT = \frac{3}{2} NkT.
\]

So, we can rewrite Eq. (5.27) for the average kinetic energy per particle,  

\[
\frac{1}{2} m\langle w^{2}\rangle = \frac{3}{2} kT. \quad (5.29)
\]

In this derivation, the average energy per atom, \(\frac{1}{2} m\langle w^{2}\rangle\) , is wholly kinetic energy of translation. This is the only kind of energy that a hard, spherical atom, uninfluenced by its neighbors or fields, can possess. Therefore, we have limited ourselves to a monatomic gas only. Diatomic and polyatomic molecules can also rotate and vibrate and may, therefore, be expected to possess energies of rotation and vibration, even though there are no forces between interacting molecules.  

It is worthwhile, at this point, to compare the symbolism used in our treatment of kinetic theory with that used in thermodynamics. This is shown in Table 5.4. The equation of state for the ideal monatomic gas has a simple form, namely,  

\[
P V = n K T. \quad (5.30)
\]

TABLE 5.4 Comparison of symbols   

ThermodynamicsKinetic theorym = Mass of systemm = Mass of particlen = Number of molesN = Number of particlesM = Mass per mole = m/n(molar mass; molecular “weight”)NA = Particles per mole = N/n(Avogadro&#x27;s number)R = Molar gas constantk = Boltzmann&#x27;s constant = R/NAV = VolumeV = Volumerho = Mass density = m/VNumber density = N/V

===== Page 156 =====

 Of course, the severe assumptions of point- mass atoms and noninteracting atoms in the earliest version of the kinetic theory of gases were recognized as shortcomings in a discussion of real gases. So, in 1881, van der Waals proposed an equation of state that accounted for the finite volume of the atoms themselves and interactions between atoms:  

\[
\left(P + \frac{n^2a}{V^2}\right)(V - nb) = nRT,
\]

where the constant \(a\) accounts for cohesive forces between atoms, thereby decreasing the measured pressure \(P\) , and \(b\) accounts for the volume occupied by the atoms themselves inside the system volume \(V\) .  

## PROBLEMS  

5.1. A stream of air moves with a speed \(w\) . Assume that a mass \(m\) of air is stopped adiabatically by an obstacle.  

(a) Prove that the rise in temperature of this mass of air is given by  

\[
\Delta T = \frac{w^2M}{5R},
\]

where \(M\) is the molar mass of air.  

(b) Calculate \(\Delta T\) when \(w = 600\) miles/h.  

(c) Apply the equation in part 
(a) to a meteor moving through a stationary atmosphere at a speed of 20 miles/s. What would happen?  

5.2. A vertical tank of length greater than \(0.76\mathrm{m}\) has its top end closed by a tightly fitting frictionless piston of negligible weight. The air inside the cylinder is at an absolute pressure of 1 atm (1 atm \(= 101,325\mathrm{Pa}\) ). The piston is depressed by pouring mercury on it slowly, so that the temperature of the air is maintained constant. What is the height of the air column when mercury starts to spill over the top of the cylinder?  

5.3. Mercury is poured into the open end of a J- shaped glass tube, which is closed at the short end, trapping air in that end. How much mercury can be poured in before the mercury overflows? Assume air to act like an ideal gas. The long and short arms are \(1\mathrm{m}\) and \(0.5\mathrm{m}\) long, respectively, and effects due to the curvature of the bottom may be neglected. Take atmospheric pressure to be \(76\mathrm{cm}\) Hg.  

5.4. A cylindrical cocktail glass \(15\mathrm{cm}\) high and \(35\mathrm{cm}^2\) in cross section contains water up to the \(10\mathrm{- cm}\) mark. A card is placed over the top and held there while the glass is inverted. When the support for the card is removed, what mass of water must leave the glass in order that the rest of the water will remain in the glass, if one neglects the weight of the card? (Caution: Try this over a sink.)  

5.5. Two bulbs containing air, one of which has a volume three times the other, are connected by a tube of negligible volume and are initially at the same temperature. To what temperature must the air in the larger bulb be raised in order that the pressure be doubled? Neglect heat conduction through the air in the connecting tube.

===== Page 157 =====

5.6. Expand the following equations in the form  

\[
P\nu = RT(I + BP + CP^{2} + \dots),
\]

and determine the second virial coefficient \(B\) in each case:  

\[
(a)\quad \left(P + \frac{a}{\nu^{2}}\right)(\nu -b) = RT\qquad \mathrm{(v a n d~}R\mathrm{~W a a l s~e q u a t i o n~o f~s t a t e).
\]
\[
(b)\quad \left(P e^{a / RT\nu}\right)(\nu -b) = RT\qquad \mathrm{(D i e t e r i c~e q u a t i o n~o f~s t a t e).
\]
\[
(c)\quad \left(P + \frac{a}{\nu^{2}T}\right)(\nu -b) = RT\qquad \mathrm{(B e r t h e l o t~e q u a t i o n~o f~s t a t e).
\]
\[
(d)\quad \left[P + \frac{a}{(\nu + c)^{2}T}\right](\nu -b) = RT\qquad \mathrm{(C l a u s i u s~e q u a t i o n~o f~s t a t e).
\]
\[
(e)\quad P\nu = RT\left(I + \frac{B^{\prime}}{\nu} +\frac{C^{\prime}}{\nu^{2}} +\dots\right)\qquad \mathrm{(a n o t h e r~t y p e~o f~v i r i a l~e x p a n s i o n).
\]

5.7. An ideal gas is contained in a cylinder equipped with a frictionless, nonleaking piston of area \(A\) . When the pressure is atmospheric \(P_{0}\) , the piston face is a distance \(l\) from the closed end. The gas is compressed by moving the piston a distance \(x\) . Calculate the spring constant \(\mathcal{F} / x\) of the gas:  

(a) Under isothermal conditions.  

(b) Under adiabatic conditions.  

(c) In what respect is a gas cushion superior to a steel spring?  

(d) Using Eq. (4.14), show that \(C_{P} - C_{V} = nR\) for the ideal gas.  

5.8. The temperature of an ideal gas in a tube of very small, constant cross- sectional area varies linearly from one end \((x = 0)\) to the other end \((x = L)\) according to the equation  

\[
T = T_{0} + \frac{T_{L} - T_{0}}{L} x.
\]

If the volume of the tube is \(V\) and the pressure \(P\) is uniform throughout the tube, show that the equation of state for \(n\) moles of gas is given by  

\[
P V = n R\frac{T_{L} - T_{0}}{\ln(T_{L} / T_{0})}.
\]

Show that, when \(T_{L} = T_{0} = T\) , the equation of state reduces to the obvious one, \(P V = n R T\) .  

5.9. Prove that the work done \(b y\) an ideal gas with constant heat capacities during a quasi- static adiabatic expansion is equal to:  

\[
W = -C_{V}(T_{i} - T_{f}).
\]
\[
W = \frac{P_{f}V_{f} - P_{i}V_{i}}{\gamma - 1}.
\]

===== Page 158 =====

136 PART I: Fundamental Concepts  

\[
W = \frac{P_{f}V_{f}}{\gamma - 1}\left[1 - \left(\frac{P_{i}}{P_{f}}\right)^{(\gamma - 1) / \gamma}\right].
\]

5.10. (a) Show that the heat transferred during an infinitesimal quasi- static process of an ideal gas can be written  

\[
\mathrm{d}Q = \frac{C_{V}}{nR} V d P + \frac{C_{P}}{nR} P d V.
\]

Applying this equation to an adiabatic process, show that \(P V^{\gamma} = \mathrm{const}\) .  

(b) An ideal gas of volume \(0.05\mathrm{ft}^3\) and pressure \(120\mathrm{lb} / \mathrm{in}^2\) undergoes a quasi-static adiabatic expansion until the pressure drops to \(15\mathrm{lb} / \mathrm{in}^2\) . Assuming \(\gamma\) to remain constant at the value 1.4, calculate the final volume. Calculate the work.  

5.11. (a) Derive the following formula for a quasi- static adiabatic process for the ideal gas, assuming \(\gamma\) to be constant:  

\[
T V^{\gamma -1} = \mathrm{const}.
\]

(b) At about \(0.1\mathrm{ms}\) after detonation of a 20-kiloton nuclear fission bomb, the "fireball" consists of a sphere of gas with a radius of about \(40\mathrm{ft}\) and a uniform temperature of \(300,000\mathrm{K}\) . Making rough assumptions, estimate the radius at a temperature of \(3000\mathrm{K}\) .  

5.12. (a) Derive the following formula for a quasi- static adiabatic process for the ideal gas, assuming \(\gamma\) to be constant:  

\[
\frac{T}{P^{(\gamma - 1) / \gamma}} = \mathrm{const}.
\]

(b) Helium \(\gamma = \frac{5}{3}\) at \(300\mathrm{K}\) and 1 atm pressure is compressed quasi-statically and adiabatically to a pressure of 5 atm. Assuming that the helium behaves like the ideal gas, calculate the final temperature.  

5.13. A horizontal, insulated cylinder contains a frictionless nonconducting piston. On each side of the piston is 54 liters of an inert monatomic ideal gas at 1 atm and \(273\mathrm{K}\) . Heat is slowly supplied to the gas on the left side until the piston has compressed the gas on the right side to \(7.59\mathrm{atm}\) .  

(a) How much work is done on the gas on the right side?  

(b) What is the final temperature of the gas on the right side?  

(c) What is the final temperature of the gas on the left side?  

(d) How much heat was added to the gas on the left side?  

5.14. An evacuated bottle with nonconducting walls is connected through a valve to a large supply of gas, where the pressure is \(P_{0}\) and the temperature is \(T_{0}\) . The valve is opened slightly, and helium flows into the bottle until the pressure inside the bottle is \(P_{0}\) . Assuming that the helium behaves like an ideal gas with constant heat capacities, show that the final temperature of the helium in the bottle is \(\gamma T_{0}\) .  

5.15. A thick- walled insulated chamber contains \(n_{i}\) moles of helium at high pressure \(P_{i}\) . It is connected through a valve with a large, almost empty container of helium at constant pressure \(P_{0}\) , very nearly atmospheric. The valve is opened slightly, and

===== Page 159 =====

 the helium flows slowly and adiabatically into the container until the pressures on the two sides of the valve are equal. Assuming the helium to behave like an ideal gas with constant heat capacities, show that:  

(a) The final temperature of the gas in the chamber is  

\[
T_{f} = T_{i}\left(\frac{P_{f}}{P_{i}}\right)^{(\gamma -1) / \gamma}.
\]

(b) The number of moles left in the chamber is  

\[
n_{f} = n_{i}\left(\frac{P_{f}}{P_{i}}\right)^{1 / \gamma}.
\]

(c) The final temperature of the gas in the container is  

\[
T_{f} = \frac{T_{i}}{\gamma}\frac{1 - P_{f} / P_{i}}{1 - (P_{f} / P_{i})^{1 / \gamma}}.
\]

(Hint: See Prob. 4.9. )  

5.16. (a) If \(y\) is the height above sea level, show that the decrease of atmospheric pressure due to a rise of \(dy\) is given by  

\[
\frac{dP}{P} = -\frac{Mg}{RT} dy,
\]

where \(M\) is the molar mass of air, \(g\) is the acceleration of gravity, and \(T\) is the temperature at the height \(y\) .  

(b) If the decrease of pressure in part (a) is due to an adiabatic expansion, show that  

\[
\frac{dP}{P} = \frac{\gamma}{\gamma - 1}\frac{dT}{T}.
\]

(c) From parts (a) and (b), using some of the numerical data of Sec. 5.7, calculate \(dT / dy\) in kelvin per kilometer.  

5.17. A steel ball of mass \(10 \mathrm{~g}\) is placed in the tube of cross- sectional area \(1 \mathrm{~cm}^{2}\) in Rüchhardt's apparatus. The tube is connected to a jar of air having a capacity of 5 liters, the pressure of the air being \(76 \mathrm{~cm} \mathrm{Hg}\) .  

(a) What is the period of vibration for the ball?  

(b) If the ball is held initially at a position where the air pressure is exactly atmospheric and then allowed to fall, how far will the ball drop before it starts to come up?  

5.18. Carbon dioxide is contained in Rüchhardt's apparatus, which has a volume of \(5270 \mathrm{~cm}^{3}\) . A ball of mass \(16.65 \mathrm{~g}\) , placed in the tube of cross- sectional area \(2.01 \mathrm{~cm}^{2}\) , vibrates with a period of \(0.834 \mathrm{~s}\) . What is \(\gamma\) when the barometer reads \(72.3 \mathrm{~cm}^{2}\) ?  

5.19. Mercury is poured into a U- tube open at both ends until the total length of mercury is \(h\) .  

(a) If the level of mercury on one side of the tube is depressed and the mercury is allowed to oscillate with small amplitude, show that, neglecting friction, the period \(\tau_{1}\) is given by  

\[
\tau_{1} = 2\pi \sqrt{\frac{h}{2g}}.
\]

===== Page 160 =====

138 PART I: Fundamental Concepts  

(b) One end of the U-tube is now closed so that the length of the entrapped air column is \(L\) , and again the mercury is caused to oscillate. Assuming friction to be negligible, the air to be ideal, and the changes of volume to be adiabatic, show that the period \(\tau_{2}\) is now  

\[
\tau_{2} = 2\pi \sqrt{\frac{h}{2g + \gamma h_{0}g / L}},
\]

where \(h_{0}\) is the height of the barometric column.  

(c) Show that  

\[
\gamma = \frac{2L}{h_{0}}\left(\frac{\tau_{1}^{2}}{\tau_{2}^{2}} -1\right).
\]

5.20. Prove that the expression for the speed of a longitudinal wave in an ideal gas may be written  

\[
w = \sqrt{\left(\frac{\partial P}{\partial\rho}\right)_{S}}.
\]

5.21. What is the speed of a longitudinal wave in argon at \(293 \mathrm{~K}\) ?  

5.22. A standing wave of frequency \(1100 \mathrm{~Hz}\) in a column of methane at \(293 \mathrm{~K}\) produces nodes that are \(20 \mathrm{~cm}\) apart. What is \(\gamma\) ?  

5.23. The speed of a longitudinal wave in a mixture of helium and neon at \(300 \mathrm{~K}\) was found to be \(758 \mathrm{~m / s}\) . What is the composition of the mixture?  

5.24 The molar mass of iodine is \(127 \mathrm{~g}\) . A standing wave in iodine vapor at \(400 \mathrm{~K}\) produces nodes that are \(6.77 \mathrm{~cm}\) apart when the frequency is \(1000 \mathrm{~Hz}\) . Is iodine vapor monatomic or diatomic?  

5.25. An open glass tube of uniform cross- section is bent into the shape of an L. One arm is immersed in a liquid of density \(\rho\) , and the other arm of length \(l\) remains in the air in a horizontal position. The tube is rotated with constant angular speed \(\omega\) about the axis of the vertical arm. Prove that the height \(y\) to which the liquid rises in the vertical arm is equal to  

\[
y = \frac{P_{0}(1 - e^{-\omega^{2}L^{2}M / 2RT})}{g\rho},
\]

where \(P_{0}\) is atmospheric pressure, \(M\) is the molar mass of air, and \(g\) is the acceleration of gravity.  

5.26. One mole of an ideal paramagnetic gas obeys Curie's law, with a Curie constant \(C_{C}\) . Assume that the internal energy \(U\) is a function of \(T\) only, so that \(dU = C_{V, \eta} dT\) , where \(C_{V, \eta}\) is a constant heat capacity.  

(a) Show that the equation of the family of adiabatic surfaces is  

\[
\frac{C_{V, \eta}}{nR} \ln T + \ln V = \frac{\mu_{0} \eta \mathcal{M}^{2}}{2n R C_{C}} + \ln A,
\]

where \(A\) is a constant for one surface.

===== Page 161 =====

5.27. The definition of the average speed of a particle in an ideal gas is  

\[
\langle w\rangle = \frac{\sum_{j}w_{j}}{N}.
\]

Prove that the number of particles striking a unit area of the wall of the container in unit time is equal to  

\[
\frac{N\langle w\rangle}{4V}.
\]

5.28. The root- mean- square speed \(w_{\mathrm{rms}}\) is defined as \(\sqrt{\langle w\rangle^{2}}\) . Show that:  

\[
w_{\mathrm{rms}} = \sqrt{\frac{3kT}{m}}.
\]

(b) \(w_{\mathrm{rms}} = \sqrt{3 / \gamma}\) times the speed of sound.

===== Page 162 =====

6.1 CONVERSION OF WORK INTO HEAT AND VICE VERSA  

When two stones are rubbed together under water, the work done against the force of friction is transformed into internal energy tending to produce a rise of temperature of the stones. As soon as the temperature of the stones rises above that of the surrounding water, however, there is heating of the water. If the mass of water is large enough, then there will be no appreciable rise of temperature, and the water can be regarded as a heat reservoir, as discussed in Sec. 4.10. Since the state of the stones is the same at the end of the process as at the beginning, the net result of the process is merely the conversion of mechanical work into heat. Similarly, when an electric current is maintained in a resistor immersed either in running water or in a very large mass of water, there is also a conversion of electrical work into heat, without any change in the thermodynamic coordinates of the wire. In general, work of any kind \(W\) may be done on a system in contact with a reservoir, causing heat \(Q\) to leave the system without altering the state of the system. The system acts merely as an intermediary. It is apparent from the first law that the work is equal to the heat, \(W = Q\) ; in other words, the transformation of work into heat is accomplished with 100 percent efficiency. Moreover, this transformation can be continued indefinitely.  

To study the opposite process, namely, the conversion of heat into work, we must also have at hand a process, or series of processes, by means of which such a conversion may continue indefinitely without involving any resulting changes in the state of the system. At first thought, it might appear that the isothermal expansion of an ideal gas might be a suitable process to consider in discussing the conversion of heat into work. In this case, there is no change of internal energy, since the temperature remains constant, and, therefore,

===== Page 163 =====

 \(Q = W\) , or heat has been converted completely into work. This process, however, involves a change of state of the gas. The volume increases and the pressure decreases until atmospheric pressure is reached, at which point the process stops. Therefore, the process of isothermal expansion cannot be used indefinitely.  

What is needed is a series of processes in which a system is brought back to its initial state, that is, a cycle. Each of the processes that constitute a cycle involves either the performance of work or a flow of heat between the system and its surroundings, which consist of a heat reservoir at a higher temperature than the system (a "high- temperature reservoir") and a heat reservoir at a lower temperature than the system (a "low- temperature reservoir"). For one complete cycle, let  

the symbol \(|Q_{H}|\) represent the heat exchanged between the high- temperature reservoir and the system; the symbol \(|Q_{L}|\) represent the heat exchanged between the low- temperature reservoir and the system; and the symbol \(|W|\) represent the work exchanged between the system and the surroundings.  

All three quantities \(|Q_{H}|\) , \(|Q_{L}|\) , and \(|W|\) , are expressed as absolute values, that is, positive numbers only. In all chapters of this book, except this chapter and the next one, the symbols \(Q\) and \(W\) are algebraic quantities that may take on positive or negative values. In these two chapters, we shall deal with engines and refrigerators, so we shall know at all times the direction of flow of \(Q\) and \(W\) and we are interested only in the absolute values of \(Q\) and \(W\) .  

If \(|Q_{H}|\) is larger than \(|Q_{L}|\) and if \(|W|\) is done by the system, then the machine that causes the system to undergo the cycle is called a heat engine. The purpose of a heat engine is to deliver work continuously to the surroundings by performing the same cycle over and over again. The net work in the cycle is the output, and the heat absorbed from the high- temperature reservoir by the system is the input. The thermal efficiency of the engine, symbolized by \(\eta\) (Greek letter eta), is defined as  

\[
\text{Thermal efficiency} = \frac{\text{work output}}{\text{heat input}},
\]

\[
\eta = \frac{|W|}{|Q_{H}|}, \quad (6.1)
\]

where \(|W|\) and \(|Q_{H}|\) are measured in joules. Applying the first law to one complete cycle, remembering that there is no change of internal energy, we get  

\[
|Q_{H}| - |Q_{L}| = |W|,
\]

and, therefore,  

\[
\eta = \frac{|Q_{H}| - |Q_{L}|}{|Q_{H}|},
\]

===== Page 164 =====

142 PART I: Fundamental Concepts  

\[
\eta = 1 - \frac{|Q_L|}{|Q_H|}. \quad (6.2)
\]

It is seen from this equation that \(\eta\) will be unity (efficiency 100 percent) if \(Q_{L}\) is zero. In other words, if an engine could be built to operate in a cycle in which there is no outflow of heat from the working substance to the low- temperature reservoir, then there would be 100 percent conversion of heat from the high- temperature reservoir into work. But, as we shall see in Sec. 6.6, there must always be an outflow of heat from an engine, so the efficiency of a heat engine is always less than 100 percent.  

The transformation of heat into work is usually accomplished, in practice, by two general types of heat engine: the internal- combustion engine, such as the gasoline engine and the diesel engine; and the external- combustion engine, such as the steam engine and the Stirling engine. In both types of heat engine, a gas or a mixture of gases is contained in the space between a cylinder, closed at one end, and a piston. The gas in the confined space is the system, which undergoes a cycle, thereby causing a reciprocating piston to impart a motion of rotation to a shaft, which acts against an opposing force. It is necessary, in all engines, that the gas in the confined space, at some time in the cycle, be raised to a high temperature and a high pressure, the pressure providing the force that performs external work. In the gasoline and diesel engines, the rapid burning of the fuel and oxygen from the air takes place in the confined space called the combustion chamber, thereby raising the temperature and pressure of the system. In the steam and Stirling engines, the increase in temperature and pressure of the gas is accomplished by high- temperature surroundings that transfer heat to the system inside the chamber.  

### 6.2 THE GASOLINE ENGINE  

In the gasoline engine, the cycle involves the performance of six processes, four of which require vertical motion of the piston and are called strokes:  

1. Intake stroke. The system is a mixture of gasoline vapor and air, which moves into the cylinder due to suction as the receding piston enlarges the accessible volume. The outside pressure is greater than the pressure in the cylinder, so the mixture is pushed into the combustion chamber.  

2. Compression stroke. The mixture of gasoline vapor and air is compressed until its pressure and temperature rise considerably. This is accomplished by the advancing piston, which decreases the volume of the combustion chamber.  

3. Combustion. Burning of the hot mixture occurs very rapidly after ignition by an electric spark. The resulting combustion products attain a very high pressure and temperature, but the volume remains unchanged during this

===== Page 165 =====

4. Power stroke. The hot combustion products expand and push the piston away, thus increasing the volume and decreasing the pressure and temperature. The system, acting through the piston, performs work on the surroundings (crankshaft, transmission, etc.).  

5. Exhaust. The combustion products at the end of the power stroke are still at a higher pressure and temperature than the surroundings. An exhaust valve allows some gas to escape until the pressure drops almost to atmospheric pressure. The piston remains essentially motionless during this process.  

6. Exhaust stroke. The piston pushes almost all the remaining combustion products out of the cylinder by exerting a pressure significantly larger than atmospheric pressure.  

In the above processes, there are several phenomena that render an exact mathematical analysis quite difficult. Among these are friction, turbulence, loss of heat by conduction, and the chemical reaction between gasoline vapor and oxygen. A drastic but useful simplification is provided by neglecting these troublesome effects. When this is done, we have an idealized gasoline engine that performs a cycle known as an Otto cycle. The cycle is named after the German engineer Nikolaus Otto for his invention in 1876, but the idea for a four- stroke engine came from the Frenchman Alphonse Beau de Rochas in 1862.  

The behavior of a gasoline engine can be approximated by assuming a set of ideal conditions as follows: (1) the working substance is at all times air, which behaves like an ideal gas with constant heat capacities; (2) all processes are quasi- static; (3) there is no friction or turbulence; (4) there is no loss of heat through the walls of the combustion chamber; and (5) the processes are reversible. These assumptions then lead to the idealized air- standard Otto cycle, which is composed of six simple processes of an ideal gas; these processes are plotted on a \(PV\) diagram in Fig. 6- 1 and described below.  

Process \(5 \rightarrow 1\) represents a quasi- static intake stroke, isobaric at atmospheric pressure. The volume of the combustion chamber varies from zero to \(V_{1}\) as the number of moles varies from zero to \(n\) , according to the equation  

\[
P_{0}V = nRT_{1},
\]

where \(P_{0}\) is atmospheric pressure and \(T_{1}\) is the temperature of the outside air.  

Process \(1 \rightarrow 2\) represents a quasi- static, adiabatic compression stroke. There is no friction, and no loss of heat through the cylinder wall. The temperature rises from the ambient \(T_{1}\) to \(T_{2}\) , according to the equation  

\[
T_{1}V_{1}^{\gamma -1} = T_{2}V_{2}^{\gamma -1},
\]

===== Page 166 =====

144 PART I: Fundamental Concepts  

FIGURE 6-1 Idealized Otto cycle for gasoline engines shown on a PV diagram.  

where \(V_{1}\) is the larger volume when the piston is at the bottom of the compression stroke and \(V_{2}\) the smaller volume when the piston is at the top. The ratio of heat capacities is assumed to be constant.  

Process \(2 \rightarrow 3\) represents a quasi- static isochoric increase of temperature and pressure of \(n\) moles of air, imagined to be brought about by an absorption of heat \(|Q_{H}|\) from a series of external high- temperature reservoirs whose temperatures range from \(T_{2}\) to \(T_{3}\) . If there were only one reservoir at the temperature \(T_{3}\) , then the flow of heat would not be quasi- static, because there would be a substantial difference in temperature between the system and the single reservoir at \(T_{3}\) . This process is meant to approximate the effect of the combustion in a gasoline engine when the piston is essentially motionless at the top of the stroke.  

Process \(3 \rightarrow 4\) represents a quasi- static adiabatic power stroke, involving a drop in temperature from \(T_{3}\) to \(T_{4}\) , according to the equation  

\[
T_{3}V_{2}^{\gamma -1} = T_{4}V_{1}^{\gamma -1},
\]

where \(V_{1}\) is larger than \(V_{2}\) . This process represents the power stroke.  

Process \(4 \rightarrow 1\) represents a quasi- static isochoric drop in temperature and pressure of \(n\) moles of air, brought about by a rejection of heat \(|Q_{L}|\) to a series of low- temperature external reservoirs ranging in temperature from \(T_{4}\) to \(T_{1}\) , where \(T_{1}\) is the temperature of the outside air. This process is meant to approximate the drop to atmospheric pressure upon opening the exhaust valve, but, in reality, the temperature does not actually drop to the temperature of the outside air as it leaves the exhaust port.  

Process \(1 \rightarrow 5\) represents a quasi- static exhaust stroke, isobaric at atmospheric pressure. The volume varies from \(V_{1}\) to zero as the number of moles of exhaust gas varies from \(n\) to zero, the temperature remaining constant at the value \(T_{1}\) .

===== Page 167 =====

 The two isobaric processes \(5 \rightarrow 1\) and \(1 \rightarrow 5\) obviously cancel each other and need not be considered further. Of the four remaining processes, only two involve a flow of heat. There is an absorption of \(|Q_H|\) units of heat at high temperatures from \(2 \rightarrow 3\) , and a rejection of \(|Q_L|\) units of heat at lower temperatures from \(4 \rightarrow 1\) , as indicated in Fig. 6- 1.  

Assuming \(C_V\) to be constant along the line \(2 \rightarrow 3\) , we find for heat entering the system,  

\[
|Q_H| = \int_{T_2}^{T_3} C_V dT = C_V(T_3 - T_2).
\]

Similarly, for process \(4 \rightarrow 1\) , we find for heat leaving the system,  

\[
|Q_L| = -\int_{T_4}^{T_1} C_V dT = C_V(T_4 - T_1).
\]

The thermal efficiency is, therefore,  

\[
\eta = 1 - \frac{|Q_L|}{|Q_H|} = 1 - \frac{T_4 - T_1}{T_3 - T_2}. \quad (6.3)
\]

The two adiabatic processes during the compression stroke and power stroke are given by  

\[
T_1V_1^{\gamma -1} = T_2V_2^{\gamma -1},
\]
\[
T_4V_1^{\gamma -1} = T_3V_2^{\gamma -1},
\]

and  

\[
T_1V_1^{\gamma -1} = T_2V_2^{\gamma -1},
\]
\[
T_4V_1^{\gamma -1} = T_3V_2^{\gamma -1},
\]

and  

Change signs and add unity to obtain  

\[
\frac{T_4 - T_1}{T_4} = \frac{T_3 - T_2}{T_3},
\]
\[
\frac{T_4 - T_1}{T_3 - T_2} = \frac{T_4}{T_3}.
\]

or  

Combine this result with Eq. (6.4) and Eq. (6.3) to obtain the thermal efficiency \(\eta\) of an idealized gasoline engine,  

\[
\eta = 1 - \frac{T_1}{T_2}, \quad (6.5)
\]

where \(T_1\) and \(T_2\) are the temperatures at the beginning and end of the compression stroke. This is the most important expression in connection with the gasoline engine. It shows that the thermal efficiency of a gasoline engine working in the Otto cycle depends on the temperature before and after compression. In a gasoline engine with temperatures \(T_1 = 300 \mathrm{~K}\) and \(T_2 = 580 \mathrm{~K}\) , the efficiency is 48 percent.

===== Page 168 =====

146 PART I: Fundamental Concepts  

This is the optimum efficiency for a gasoline engine operating in an idealized quasi- static Otto cycle for the temperatures cited. All the troublesome effects present in an actual gasoline engine, such as friction, turbulence, and heat conduction through the engine walls, are such that they make the efficiency much lower than that of the idealized Otto cycle. The actual operating thermal efficiency of a gasoline engine is in the range of 20- 30 percent.  

### 6.3 THE DIESEL ENGINE  

In the diesel engine, only air is admitted on the intake stroke. The air is compressed adiabatically until the temperature is high enough to ignite oil that is sprayed into the cylinder after the compression. The rate of supply of oil is adjusted so that combustion takes place approximately isobarically, the piston moving out during combustion. The rest of the cycle, namely, power stroke, exhaust, and exhaust stroke, is exactly the same as in the gasoline engine. The usual troublesome effects take place in the diesel engine as in the gasoline engine. Eliminating these effects by making the same assumptions as before, we are left with an idealized diesel engine that performs a cycle known as the air- standard Diesel cycle, named after Rudolf Diesel who constructed the first successful diesel engine using liquid fuel in 1897. If the line \(2 \rightarrow 3\) in Fig. 6- 1 is imagined horizontal instead of vertical, the resulting cycle is shown in Fig. 6- 2.  

The line \(2 \rightarrow 3\) in Fig. 6- 2 represents the quasi- static isobaric absorption of heat from a series of external reservoirs ranging in temperature from \(T_{2}\) to \(T_{3}\) . This process is meant to approximate the isobaric burning of the oil. All the other curves have the same meaning as in the case of the air- standard Otto cycle.  

Assuming \(C_{P}\) to be constant along the line \(2 \rightarrow 3\) , we get  

\[
|Q_{H}| = \int_{T_{2}}^{T_{3}}C_{P}dT = C_{P}(T_{3} - T_{2}),
\]

and, as in the case of the Otto cycle,  

\[
|Q_{L}| = C_{V}(T_{4} - T_{1}).
\]

Therefore, the thermal efficiency of an idealized diesel engine is given by  

\[
\eta = 1 - \frac{1}{\gamma}\frac{(T_{4} - T_{1})}{(T_{3} - T_{2})}.
\]

Notice that, unlike the thermal efficiency of the Otto cycle expressed in Eq. (6- 3), the efficiency of the Diesel cycle depends upon \(\gamma\) , the ratio of heat capacities. This expression may be transformed into

===== Page 169 =====

 FIGURE 6- 2 Idealized Diesel cycle for oil- fired engines shown on a \(PV\) diagram.  

\[
\eta = 1 - \frac{1}{\gamma}\frac{(r_{E}^{T} - 1)}{(r_{E} - 1)}\frac{T_{1}}{T_{2}}, \quad (6.6)
\]

where the expansion ratio \(r_{E}\) (also called the "cutoff ratio" in engineering) is given by  

\[
r_{E} = \frac{V_{1}}{V_{3}}
\]

and \(T_{1}\) and \(T_{2}\) are the temperatures at the beginning and end of the compression stroke, respectively. Interestingly, the efficiency of the Diesel cycle expressed in Eq. (6.6) does not depend on the compression ratio \(r_{C}\) given by  

\[
r_{C} = \frac{V_{1}}{V_{2}}.
\]

Taking, for example, \(r_{E} = 5\) , \(\gamma = 1.4\) , \(T_{1} = 300 \mathrm{~K}\) , and \(T_{2} = 990 \mathrm{~K}\) , we obtain  

\[
\eta = 1 - \frac{(5^{1.4} - 1)}{(1.4)(5 - 1)}\frac{300 \mathrm{~K}}{990 \mathrm{~K}} = 54 \text{ percent}.
\]

The thermal efficiencies of actual diesel engines are, of course, lower, for the reasons mentioned in connection with the gasoline engine, typically being in the range of 30- 35 percent.  

In the diesel engine just considered, four strokes of the piston are needed for the completion of a cycle, and only one of the four is a power stroke. Since only air is compressed in the diesel engine, it is possible to eliminate the exhaust and intake strokes and thus complete the cycle in two strokes. In the two- stroke- cycle diesel engine, every other stroke is a power stroke, and

===== Page 170 =====

148 PART I: Fundamental Concepts  

thus the power is doubled. The principle is very simple: At the conclusion of the power stroke, when the cylinder is full of combustion products, the valve opens, exhaust takes place until the combustion products are at atmospheric pressure, and, then, instead of using the piston itself to exhaust the remaining gases, fresh air is blown into the cylinder, replacing the combustion products. A blower, operated by the engine itself, is used for this purpose, and thus it accomplishes in one simple operation what formerly required two separate piston strokes.  

### 6.4 THE STEAM ENGINE  

The steam engine is historically quite important, because it was the first engine driven by heat, rather than animals, water, or wind. The initial function of the steam engine was to pump water out of mines in England. The first practical and safe steam engine, a reciprocating piston- cylinder device, was invented by Thomas Newcomen in 1712 and had the greatest impact in bringing about the Industrial Revolution. James Watt greatly improved the steam engine in 1764, and William Rankine was the first to describe the thermodynamic cycle for adiabatic steam engines in 1859. Currently, steam engines are used in electric power plants, and in nuclear- powered aircraft carriers and submarines.  

A schematic diagram of an elementary steam engine is shown in Fig. 6- 3(a). The operation of such an engine can be understood by following the pressure and volume changes of a small constant mass of water as it is conveyed from the condenser, through the boiler, into the expansion chamber, and back to the condenser. The water in the condenser is at a pressure less than atmospheric and at a temperature less than the normal boiling point. By means of a pump, it is introduced into the boiler, which is at a much higher pressure and temperature. In the boiler, the water is first heated to its boiling point and then vaporized, both processes taking place approximately at constant high pressure. The steam is then raised to a temperature greater than the normal boiling point at the same pressure. It is then allowed to flow into a cylinder, where it expands approximately adiabatically against a piston or a set of turbine blades, until its pressure and temperature drop to that of the condenser. In the condenser, finally, the steam condenses into the water at the same temperature and pressure as at the beginning, and the cycle is complete.  

In the actual operation of the steam engine, there are several processes that render an exact analysis difficult: turbulence caused by the pressure difference required to cause the flow of the steam from one part of the apparatus to another, friction, conduction of heat through the walls during expansion of the steam, and heat transfers due to a finite temperature difference between the furnace and the boiler.  

A first approximation to the discussion of the steam engine may be made by introducing some simplifying assumptions which, although in no way realizable in practice, provide at least an upper limit to the efficiency of such a

===== Page 171 =====

 FIGURE 6- 3(a) Schematic diagram of a simple steam engine.  

FIGURE 6- 3(b) PV diagram of the Rankine cycle for a steam engine. Process \(1 \rightarrow 2\) is not an isochoric compression of steam, but an adiabatic compression of water, which yields a nearly vertical line. Process \(3 \rightarrow 4\) is an adiabatic expansion of steam. For more detail, see Fig. 7- 2.

===== Page 172 =====

150 PART I: Fundamental Concepts  

plant and which define an idealized cycle, called the Rankine cycle, in terms of which the actual behavior of a steam plant may be discussed.  

In the Rankine cycle, all processes are assumed to be well behaved; complications that arise from turbulence, friction, and heat losses are thus eliminated. Starting at point 1 in Fig. 6- 3(b), we have liquid water at the temperature and pressure of the condenser. The Rankine cycle consists of the following four processes:  

\(1\rightarrow 2\) Adiabatic compression of water to the pressure of the boiler (only very small changes of temperature and volume of the liquid take place during this process). \(2\rightarrow 3\) Isobaric heating of water to the boiling point, vaporization of water into saturated steam, and superheating of steam to a temperature \(T_{H}\) higher than the boiling point. \(3\rightarrow 4\) Adiabatic expansion of superheated steam into wet steam. \(4\rightarrow 1\) Isobaric, isothermal condensation of steam into saturated water at the temperature \(T_{L}\) .  

During the process \(2\rightarrow 3\) , heat \(|Q_{H}|\) enters the system from a hot reservoir; whereas during the condensation process \(4\rightarrow 1\) , heat \(|Q_{L}|\) is rejected by the system to the atmosphere, a reservoir at \(T_{L}\) . This condensation process must exist in order to bring the system back to its initial state 1. Since heat is always rejected during the condensation of water, \(|Q_{L}|\) cannot be made equal to zero, and, therefore, the input \(|Q_{H}|\) cannot be converted completely into work. So the efficiency of the idealized steam engine is always less than 100 percent. The efficiency of historic steam locomotives was quite low, which led to the development of diesel- electric locomotives. However, the actual operating thermal efficiency of a steam power plant is in the range 30- 40 percent.  

### 6.5 THE STIRLING ENGINE  

In 1816, due to explosions of steam engines and loss of life, a minister of the Church of Scotland, named Robert Stirling, designed and patented a hot- air engine that could convert some of the energy liberated by a burning fuel into work. The Stirling engine remained useful and popular for many years in applications needing only a few horsepower, but, with the development of small internal- combustion engines, fell into disuse.  

The steps in the operation of an idealized Stirling engine are shown schematically in Fig. 6- 4(a). Two pistons, an expansion piston on the left and a compression piston on the right, are connected to the same shaft. As the shaft rotates, these pistons move out of phase, with the aid of suitable connecting linkages. The space between the two pistons is filled with a fixed amount of gas, usually hydrogen or helium, which is recycled from one cylinder to the other. The left- hand portion of the space is kept in contact with a high- tem

===== Page 173 =====

151  

FIGURE 6-4(a) Schematic diagram of the steps in the operation of an idealized Stirling engine. The numbers under each diagram refer to the processes shown in Fig. 6-4(b).  

FIGURE 6-4(b)  

PV diagram for a Stirling engine showing the heats exchanged between the system and the surroundings during the isothermal processes. During the isochoric processes, there are heats exchanged between the internal regenerator and the system, but these are not shown.  

perature reservoir (burning fuel), while the right- hand portion is in contact with a low- temperature reservoir (atmosphere). Between the two cylinders is a device \(R\) , called a regenerator, consisting of a packing of fine wire screens to form a kind of metal sponge. The regenerator serves as an internal reservoir, which exchanges heat with the gas as it passes back and forth through the regenerator.  

The Stirling cycle consists of four processes involving pressure and volume changes, plotted (as though ideal conditions existed) on the PV diagram of Fig. 6- 4(b). During process \(1 \rightarrow 2\) , the left piston remains at the top of the

===== Page 174 =====

152 PART I: Fundamental Concepts  

cylinder. Meanwhile, the right piston moves halfway up its cylinder, compressing low- temperature gas that is in contact with the low- temperature reservoir and, therefore, causing heat \(|Q_{L}|\) to leave. This is an approximately isothermal compression and is depicted as a rigorously isothermal process at the temperature \(T_{L}\) .  

For process \(2 \rightarrow 3\) , the left piston moves down and the right piston up, so that there is no change in volume occupied by the gas. However, gas is forced through the regenerator from the low- temperature side to the high- temperature side and enters the left- hand side at the higher temperature \(T_{H}\) . To raise the temperature of the gas, the regenerator supplies heat \(|Q_{R}|\) to the gas. Note that the process \(2 \rightarrow 3\) in Fig. 6- 4(b) is at constant volume.  

In process \(3 \rightarrow 4\) , the right piston remains stationary. The left piston continues moving down while in contact with the high- temperature reservoir, which causes the gas to expand approximately isothermally. Additional heat \(|Q_{H}|\) is absorbed from the outside at the temperature \(T_{H}\) .  

During process \(4 \rightarrow 1\) , both pistons move in opposite directions, thereby forcing gas through the regenerator from the high- temperature to the low- temperature side and giving up approximately the same amount of heat \(|Q_{R}|\) to the regenerator that is absorbed in the process \(2 \rightarrow 3\) , so the regenerator heats cancel each other during one cycle. This process takes place at practically constant volume.  

The net result of the Stirling cycle is the absorption of heat \(|Q_{H}|\) at the high temperature \(T_{H}\) , the rejection of heat \(|Q_{L}|\) at the low temperature \(T_{L}\) , and the delivery of work \(|W| = |Q_{H}| - |Q_{L}|\) to the surroundings, with no net heat transfer resulting from the two constant- volume processes. It must be emphasized that Fig. 6- 4(b) is based on the assumptions that the gas is ideal, no leakage of gas takes place, no heat is lost or gained through cylinder walls, no heat is conducted from the regenerator to the surroundings, and there is no friction. Even if these idealizations could be realized, in practice, there would still be some heat \(|Q_{L}|\) rejected at the lower temperature, and, therefore, all the input \(|Q_{H}|\) could not be converted into work, rendering the efficiency less than 100 percent. The actual operating thermal efficiency of Stirling engines is in the range of 35- 45 percent.  

The Stirling engine has some unique advantages compared with other heat engines. The engine can use any heat source, from heating due to radioactivity to combustion of biomass waste products. Using open- air combustion, the engine does not produce toxic exhaust. Furthermore, it operates quietly. The Stirling engine can be used in automobiles, but internal- combustion engines are already quite good for this application. An interesting application is an implantable Stirling engine for artificial heart power, which is being developed at the Joint Center for Graduate Study, University of Washington.  

A modification to the Stirling engine, called a Ringbom Stirling engine after its inventor Ossian Ringbom, uses only one reciprocating piston instead of two pistons. The regenerator or displacer oscillates between the closed end of the cylinder and the piston. As a result, the Ringbom Stirling engine is strikingly simpler than all the Stirling engines that had preceded it.

===== Page 175 =====

6.6 HEAT ENGINE; KELVIN- PLANCK STATEMENT OF THE SECOND LAW  

In the preceding sections, four different heat engines have been briefly described. There are, of course, more types of heat engines and a tremendous number of structural details, methods of increasing thermal efficiency, mathematical analyses, etc., which constitute the subject matter of engineering thermodynamics. Thermodynamics owes its origin to the project of converting heat into work and of developing the theory of operation of machines for this purpose. Therefore, it is fitting that one of the fundamental laws of thermodynamics is based upon the operation of heat engines. Reduced to its simplest terms, the important characteristics of heat- engine cycles may be summed up as follows:  

1. There is some process or series of processes during which there is an absorption of heat from an external reservoir at a higher temperature. 
2. There is some process or series of processes during which heat is rejected to an external reservoir at a lower temperature.  

This is represented schematically in Fig. 6- 5. It is a fact of experience that no heat- engine has ever been developed that converts the heat extracted from a reservoir at a higher temperature into work without rejecting some heat to a reservoir at a lower temperature. This negative statement, which is the result of everyday experience, constitutes the second law of thermodynamics and has been formulated in several ways. The original statement of William Thomson (Kelvin) is, "It is impossible by means of inanimate material agency to derive mechanical effect from any portion of matter by cooling it below the temperature of the coldest of the surrounding objects." In the words of Max Planck, originator of quantum mechanics, "It is impossible to construct an engine which, working in a complete cycle, will produce no effect other than the raising of a weight and the cooling of a heat reservoir." We may combine these statements into one equivalent statement, to which we shall refer hereafter as the Kelvin- Planck statement of the second law, thus:  

It is impossible to construct an engine that, operating in a cycle, will produce no effect other than the extraction of heat from a reservoir and the performance of an equivalent amount of work.  

If the second law were not true, it would be possible to propel a ship across the ocean by extracting heat from the ocean or to run a power plant by extracting heat from the surrounding air. Notice that neither of these "impossibilities" violates the first law of thermodynamics. After all, both the ocean and the surrounding air contain an enormous store of internal energy, part of which you might hope could be extracted in the form of a flow of heat. There is nothing in the first law to preclude the possibility of converting this heat

===== Page 176 =====

154 PART I: Fundamental Concepts  

FIGURE 6-5  
Schematic representation of the generalized heat engine.  

completely into work. The second law, therefore, is not a deduction from the first law, but stands by itself as a separate law of nature, referring to an aspect of nature different from that described by the first law. The first law denies the possibility of creating or destroying energy; the second law denies the possibility of utilizing energy in a particular way. The continuous operation of a machine that creates its own energy and thus violates the first law is called a perpetual motion machine of the first kind. The operation of a machine that utilizes the internal energy of only one heat reservoir, thus violating the second law, is called a perpetual motion machine of the second kind.  

### 6.7 REFRIGERATOR; CLAUSIUS' STATEMENT OF THE SECOND LAW  

We have seen that a heat engine is a machine that takes a working substance through a cycle in such a sequence of processes that some heat is absorbed by the system from a high- temperature heat reservoir, a smaller amount of heat is rejected to a low- temperature heat reservoir, and a net amount of work is done by the system on the surroundings. If we imagine a cycle performed in a sequence of processes opposite to that of an engine, then some heat is absorbed by the system from a heat reservoir at a low temperature, a larger amount of heat is rejected to a heat reservoir at a high temperature, and a net amount of work is done on the system by the surroundings. A machine that performs a cycle in this direction is called a refrigerator, and the working substance (system) is called a refrigerant. Refrigerators used for climate control are the air- conditioner and the heat pump. Figure 6- 6 represents a schematic diagram of a refrigerator.  

Let the following notation (all positive quantities) refer to one complete cycle:

===== Page 177 =====

1QH represents the amount of heat rejected by the refrigerant to the high- temperature reservoir;  

\(|Q_{L}|\) represents the amount of heat absorbed by the refrigerant from the low- temperature reservoir; and  

\(|W|\) represents the net work done on the refrigerant by the surroundings.  

Since the refrigerant undergoes a cycle, there is no change in internal energy, and the first law becomes  

\[
|Q_{L}| - |Q_{H}| = |W|,
\]

or  

\[
|Q_{H}| = |Q_{L}| + |W|.
\]

That is, the heat rejected to the high- temperature reservoir is larger than the heat extracted from the low- temperature reservoir by the amount of work done on the refrigerant.  

The purpose of a refrigerator is to extract as much heat \(|Q_{L}|\) as possible from the low- temperature reservoir with the expenditure of as little work \(|W|\) as possible. Work is always necessary to transfer heat from a lower- temperature reservoir to a higher- temperature reservoir, because it is a fact of nature that heat does not flow spontaneously from a lower- temperature reservoir to a higher- temperature reservoir. This negative statement leads us to the Clausius statement of the second law:  

It is impossible to construct a refrigerator that, operating in a cycle, will produce no effect other than the transfer of heat from a lower- temperature reservoir to a higher- temperature reservoir.  

At first sight, the Kelvin- Planck and the Clausius statements appear to be quite unconnected, but we shall see immediately that they are in all respects equivalent.  

FIGURE 6-6 Schematic representation of the generalized refrigerator.

===== Page 178 =====

6.8 EQUIVALENCE OF THE KELVIN- PLANCK AND CLAUSIUS STATEMENTS  

Let us adopt the following notation:  

\(K =\) truth of the Kelvin- Planck statement; \(- K =\) falsity of the Kelvin- Planck statement; \(C =\) truth of the Clausius statement; \(- C =\) falsity of the Clausius statement.  

Two propositions or statements are said to be equivalent when the truth of one implies the truth of the second, and the truth of the second implies the truth of the first. Using the symbol \(\supset\) to mean "implies" and the symbol \(\equiv\) to denote "equivalence," we wish to prove that  

\[
K\equiv C,
\]

when true statements imply each other, namely  

\[
K\supset C\qquad \mathrm{and}\qquad C\supset K.
\]

Alternatively, equivalence can be proven when false statements imply each other, namely,  

\[
-K\supset -C\qquad \mathrm{and} -C\supset -K.
\]

Thus, in order to demonstrate the equivalence of \(K\) and \(C\) , we use the latter strategy that the falsity of one statement implies the falsity of the second, and vice versa.  

1. To prove that \(-C\supset -K\) , consider a refrigerator, shown in the left side of Fig. 6-7, that requires no work to transfer \(|Q_{L}|\) units of heat from a low-temperature reservoir to a high-temperature reservoir and that, therefore, violates the Clausius statement. Suppose that a heat engine (on the right) also operates between the same two reservoirs in such a way that the same heat \(|Q_{L}|\) is delivered to the low-temperature reservoir. The engine, of course, does not violate any law, but the refrigerator and engine together constitute a self-contained machine that takes heat \(|Q_{H}| - |Q_{L}|\) from the high-temperature reservoir and converts all this heat into work without producing any change in the low-temperature reservoir. Therefore, the refrigerator and engine together constitute a violation of the Kelvin- Planck statement.  

2. To prove that \(-K\supset -C\) , consider an engine, shown on the left side of Fig. 6-8, that rejects no heat to the low-temperature reservoir and that, therefore, violates the Kelvin-Planck statement. Suppose that a refrigerator (on the right) also operates between the same two reservoirs and uses up all the work performed by the engine. The refrigerator violates no law, but the engine and refrigerator together constitute a self-contained machine that

===== Page 179 =====

 FIGURE 6-7 Proof that \(- C \supset - K\) . The refrigerator on the left is a violation of \(C\) ; the refrigerator and the heat engine acting together violate \(K\) .  

FIGURE 6-8  

Proof that \(- K \supset - C\) . The heat engine on the left is a violation of \(K\) ; the heat engine and refrigerator acting together violate \(C\) .  

transfers heat \(|Q_{L}|\) from the low- temperature reservoir to the high- temperature reservoir without producing any changes elsewhere. Therefore, the engine and refrigerator together constitute a violation of the Clausius statement.

===== Page 180 =====

 Therefore, we arrive at the conclusion that both statements of the second law are equivalent. It is a matter of choice which one is used in a particular argument.  

### 6.9 REVERSIBILITY AND IRREVERSIBILITY  

In thermodynamics, work is a macroscopic concept. The performance of work may always be described in terms of the raising or lowering of an object or the winding or unwinding of a spring, that is, by the operation of a machine that serves to increase or decrease the potential energy of a mechanical system. Imagine, for the sake of simplicity, a suspended object coupled, by means of suitable pulleys, to a system so that any work done by or on the system can be described in terms of the raising or lowering of the object. Imagine, further, a series of reservoirs which may be put in contact with the system and in terms of which any flow of heat to or from the system may be described. We shall refer to the suspended object and the series of reservoirs as the local surroundings of the system. The local surroundings are, therefore, those parts of the surroundings which interact directly with the system. Other machines and reservoirs which are accessible and which might interact with the system constitute the auxiliary surroundings of the system or, for want of a better expression, the rest of the universe. The word "universe" is used here in a very restricted technical sense, with no cosmic or celestial implications. The universe merely means a finite portion of the world consisting of the system and those surroundings which may interact with the system.  

Now, suppose that a process occurs in which: (1) the system proceeds from an initial state \(i\) to a final state \(f\) ; (2) the suspended object is lowered to an extent that \(W\) units of work are performed on the system; and (3) a transfer of heat \(|Q|\) takes place from the system to the series of reservoirs. If, at the conclusion of this process, the system may be restored to its initial state \(i\) , the object lifted to its former level, and the reservoirs caused to part with the same amount of heat \(|Q|\) , without producing any changes in any other mechanical device or reservoir in the universe, the original process is said to be reversible. In other words, a reversible process is one that is performed in such a way that, at the conclusion of the process, both the system and the local surroundings may be restored to their initial states without producing any changes in the rest of the universe. A process that does not fulfill these stringent requirements is said to be irreversible. The importance of the phrase in bold print is that all the initial states must be recoverable.  

The question immediately arises as to whether natural processes, namely, the familiar processes of nature, are reversible or not. Since dissipation is present in all real processes, it follows that all natural processes are irreversible. By considering representative types of natural processes and examining the features that are responsible for irreversibility, we shall then be able to state the conditions necessary for a process to occur reversibly.

===== Page 181 =====

6.10 EXTERNAL MECHANICAL IRREVERSIBILITY  

There is a large class of processes involving the isothermal transformation of work through a system (which remains unchanged) into internal energy of a reservoir. This type of process is depicted schematically in Fig. 6- 9 and is illustrated by the following five examples:  

1. Friction from rubbing two solids in contact with a reservoir. 
2. Irregular stirring of a viscous liquid in contact with a reservoir. 
3. Inelastic deformation of a solid in contact with a reservoir. 
4. Transfer of charge through a resistor in contact with a reservoir. 
5. Magnetic hysteresis of a material in contact with a reservoir.  

In order to restore the system and its local surroundings to their initial states without producing changes elsewhere, \(|Q|\) units of heat would have to be extracted from the reservoir and converted completely into work. Since this would involve a violation of the second law (Kelvin statement), all processes of the above type are irreversible.  

Another set of processes involves the adiabatic transformation of work into internal energy of a system. This is depicted schematically in Fig. 6- 10 and is illustrated by the following examples, similar to the preceding list:  

1. Friction from rubbing two thermally insulated solids. 
2. Irregular stirring of a viscous thermally insulated liquid. 
3. Inelastic deformation of a thermally insulated solid. 
4. Transfer of charge through a thermally insulated resistor. 
5. Magnetic hysteresis of a thermally insulated material.  

A process of this type is accompanied by a rise of temperature of the system from, say, \(T_{i}\) to \(T_{f}\) . In order to restore the system and its local surroundings to their initial states without producing changes elsewhere, the internal energy of the system would have to be decreased by extracting \(U_{f} - U_{i}\) units of heat, thus lowering the temperature from \(T_{f}\) to \(T_{i}\) , and this heat would have to be completely converted into work. Since this violates the second law, all processes of the above type are irreversible.  

The transformation of work into internal energy either of a system or of a reservoir is seen to take place through the agency of such phenomena as friction, viscosity, inelasticity, electric resistance, and magnetic hysteresis. These effects are known as dissipative effects and the work is said to be dissipated. Processes involving the dissipation of work into internal energy are said to exhibit external mechanical irreversibility. It is a matter of everyday experience that dissipative effects, particularly friction, are always present in machines. Friction, of course, may be reduced considerably by suitable lubrication, but experience has shown that it can never be completely eliminated. If friction could be eliminated, then a machine could run indefinitely without

===== Page 182 =====

160 PART I: Fundamental Concepts  

FIGURE 6-9  
Isothermal transformation of work through a system (which remains unchanged) into internal energy of a reservoir.  

FIGURE 6-10 Adiabatic transformation of work into internal energy of a system.  

violating either of the two laws of thermodynamics; that is, it would run but produce no work. The operation of a machine that has no dissipation of work and thus violates the fact that all natural processes are irreversible is called a perpetual motion machine of the third kind. Friction renders a process irreversible, since heat is produced by friction in whichever direction the process is traversed. For this reason, all the cycles discussed in this chapter are idealized by assuming frictionless processes.  

This chapter is quite unusual in its use of negative statements to formulate the fundamental second law of thermodynamics. The Kelvin- Planck statement and Clausius statement each independently and equivalently establish the second law. Furthermore

===== Page 123 =====

4.1. A gas contained in a cylinder by a layer of styrofoam is quickly compressed, the temperature rising several hundred degrees. Has there been a transfer of heat? Has the "heat content" of the gas been increased?  

4.2. A combustion experiment is performed by burning a mixture of fuel and oxygen in a constant- volume container surrounded by a water bath. During the experiment, the temperature of the water rises. If the system is the mixture of fuel and oxygen:  

(a) Has heat been transferred? 
(b) Has work been done? 
(c) What is the sign of \(\Delta U?\)  

4.3. A liquid is irregularly stirred in a well- insulated container and thereby experiences a rise in temperature. If the system is the liquid:  

(a) Has heat been transferred? 
(b) Has work been done? 
(c) What is the sign of \(\Delta U?\)  

4.4. The amount of water in a lake may be increased by action of underground springs, by inflow from a river, and by rain. It may be decreased by various outflows and by evaporation.  

(a) Comment on the question: How much rain is there in the lake? 
(b) Comment on the question: How much water in the lake is due to rain? 
(c) What concept is analogous to "rain in the lake"?  

4.5. A container with rigid well- insulated walls is divided into two parts by a partition. One part contains a gas, and the other is evacuated. If the partition suddenly breaks, show that the initial and final internal energies of the gas are equal. (Note: this process is called an adiabatic free expansion.)  

4.6. When an electric current is maintained in an electrolytic cell of slightly acidic water and 1 mol of water is electrolyzed into hydrogen and oxygen, \(2F\) (faradays) of charge are transferred through a source of emf \(\mathcal{E}(1F\approx 96,500\mathrm{C / mol})\) . The energy change of the system is \(+286,500\mathrm{J}\) , and 50,000 J of heat is absorbed. What is \(\mathcal{E}\) ?  

4.7. A cylinder with rigid well- insulated walls is divided into two parts by a rigid insulating wall with a small hole in it. A frictionless, insulated piston is held against the perforated partition, thus preventing the gas that is on the other side from seeping through the hole. The gas is maintained at a pressure \(P_{i}\) by another frictionless insulated piston. Imagine both pistons to move simultaneously in such a way that, as the gas streams through the hole, the pressure remains at a constant value \(P_{i}\) on one side of the dividing wall and at a constant lower value \(P_{f}\) on the other side, until all the gas is forced through the hole. (Note: this process is called a throttling process.) Prove that  

\[
U_{i} + P_{i}V_{i} = U_{f} + P_{f}V_{f}.
\]

===== Page 124 =====

4.8. A container of volume \(V\) contains \(n\) moles of gas at high pressure. Connected to the container is a capillary tube through which the gas may leak slowly out to the atmosphere, where the pressure is \(P_{0}\) . Surrounding the container and capillary is a water bath, in which is immersed an electrical resistor. The gas is allowed to leak slowly through the capillary into the atmosphere while electrical energy is dissipated in the resistor at such a rate that the temperature of the gas, the container, the capillary, and the water is kept equal to that of the outside air. Show that, after as much gas as possible has leaked out during time interval \(t\) , the change in internal energy is  

\[
\Delta U = \mathcal{E}It - P_0(nv_0 - V),
\]

where \(v_{0}\) is the molar volume of the gas at atmospheric pressure, \(\mathcal{E}\) is the potential difference across the resistor, and \(I\) is the current in the resistor.  

4.9. A thick- walled insulated metal chamber contains \(n_{i}\) moles of helium at high pressure \(P_{i}\) . It is connected through a valve with a large, almost empty gasholder in which the pressure is maintained at a constant value \(P^{\prime}\) , very nearly atmospheric. The valve is opened slightly, and the helium flows slowly and adiabatically into the gasholder until the pressure on the two sides of the valve is equalized. Prove that  

\[
\frac{n_{f}}{n_{i}} = \frac{h^{\prime} - u_{i}}{h^{\prime} - u_{f}},
\]

where \(n_{f} =\) number of moles of helium left in the chamber,  

\(u_{i} =\) initial molar internal energy of helium in the chamber,  

\(u_{f} =\) final molar internal energy of helium in the chamber, and  

\(h^{\prime} = u^{\prime} + P^{\prime}\nu\) (where \(u^{\prime} =\) molar internal energy of helium in the gasholder;  

\(v^{\prime} =\) molar volume of helium in the gasholder).  

4.10. Regarding the internal energy of a hydrostatic system to be a function of \(T\) and \(P\) , derive the following equations:  

\[
(a)\qquad \mathrm{d}Q = \left[\left(\frac{\partial U}{\partial T}\right)_{P} + P\left(\frac{\partial V}{\partial T}\right)_{P}\right]dT + \left[\left(\frac{\partial U}{\partial P}\right)_{T} + P\left(\frac{\partial V}{\partial P}\right)_{T}\right]dP.
\]

\[
(b)\qquad \left(\frac{\partial U}{\partial T}\right)_{P} = C_{P} - PV\beta .
\]

\[
(c)\qquad \left(\frac{\partial U}{\partial P}\right)_{T} = PV\kappa -(C_{P} - C_{V})\frac{\kappa}{\beta}.
\]

4.11. Taking \(U\) to be a function of \(P\) and \(V\) , derive the following equations:  

\[
(a)\qquad \mathrm{d}Q = \left(\frac{\partial U}{\partial P}\right)_{V}dP + \left[\left(\frac{\partial U}{\partial V}\right)_{P} + P\right]dV.
\]

\[
(b)\qquad \left(\frac{\partial U}{\partial P}\right)_{V} = \frac{C_{V}\kappa}{\beta}.
\]

\[
(c)\qquad \left(\frac{\partial U}{\partial V}\right)_{P} = \frac{C_{P}}{V\beta} -P.
\]

4.12. Derive the equations listed in the accompanying table.  

<table>SystemHeat capacity at constant extensive variableHeat capacity at constant intensive variableStretched wire\(C_L = \left(\frac{\partial U}{\partial T}\right)_L\)\(C_\gamma = \left(\frac{\partial U}{\partial T}\right)_\gamma - \mathcal{J} L\alpha\)Paramagnetic solid obeying Curie's law\(C_m = \left(\frac{\partial U}{\partial T}\right)_m\)\(C_\kappa = \left(\frac{\partial U}{\partial T}\right)_\kappa + \frac{m^2}{C_c}\)</table>

Note: \(C_{C}\) is the Curie constant, not a heat capacity.  

4.13. Consider using the apparatus shown in Fig. 4- 1(a), known as the Joule paddle wheel, to determine the specific heat at constant atmospheric pressure. The paddle wheel is driven by a slowly falling weight, and both have a temperature of \(14.5^{\circ}\mathrm{C}\) . As a result of the work done by the \(0.427\mathrm{kg}\) mass that falls \(1.00\mathrm{m}\) , the temperature of \(1\mathrm{kg}\) of water rises \(1^{\circ}\mathrm{C}\) . Calculate \(c_{P}\) .  

4.14. One mole of a gas obeys the van der Waals equation of state:  

\[
\left(P + \frac{a}{v^2}\right)(v - b) = RT,
\]

and its molar internal energy is given by  

\[
u = cT - \frac{a}{v},
\]

where \(a\) , \(b\) , \(c\) , and \(R\) are constants. Calculate the molar heat capacities \(c_{V}\) and \(c_{P}\) .  

4.15. The equation of state for a monatomic solid is  

\[
P\nu +f(\nu) = \Gamma u,
\]

where \(\nu\) is the molar volume, \(\Gamma\) is the Grüneisen constant, and \(u\) is the molar internal energy due to lattice vibrations. Prove that  

\[
\Gamma = \frac{\beta\nu}{c\nu\kappa^{\prime}}
\]

where \(\kappa\) is the isothermal compressibility. This equation, known as the Grüneisen relation, plays an important role in solid- state theory.  

4.16. The molar heat capacity at constant pressure \(C_{P} / n\) of a gas varies with the temperature according to the equation  

\[
\frac{C_{P}}{n} = a + bT - \frac{c}{T^{2}},
\]

where \(a\) , \(b\) , and \(c\) are constants. How much heat is transferred during an isobaric process in which \(n\) moles of gas experience a temperature rise from \(T_{i}\) to \(T_{f}\) ?  

4.17. The molar heat capacity at constant volume of a metal at low temperatures varies with the temperature according to the equation  

\[
\frac{C_V}{n} = \left(\frac{124.8}{\Theta}\right)^3 T^3 + \gamma T,
\]

where \(\Theta\) is the Debye temperature, \(\gamma\) is a constant, and \(C_V / n\) is measured in units of \(\mathrm{mJ / mol\cdot K}\) . The first term on the left is the contribution attributable to lattice vibrations and the second term is due to the contribution of free electrons. For copper, \(\Theta\) is \(343\mathrm{K}\) and \(\gamma\) is \(0.688\mathrm{mJ / mol\cdot K^2}\) . How much heat per mole is transferred during a process in which the temperature changes from 2 to \(3\mathrm{K}\) ?  

4.18. Suppose that heat conduction occurs at a constant rate \(\mathrm{d}Q / dt\) in a hollow sphere with an inner radius \(r_1\) at temperature \(T_1\) and an outer radius \(r_2\) at temperature \(T_2\) . Show that for constant thermal conductivity \(K\) , the temperature difference between the two surfaces is given by  

\[
T_{1} - T_{2} = \frac{\mathrm{d}Q / dt}{4\pi K}\left(\frac{1}{r_{2}} -\frac{1}{r_{1}}\right).
\]

4.19. Two thin concentric spherical shells of radius \(0.05\mathrm{m}\) and \(0.15\mathrm{m}\) , respectively, have their annular cavity filled with charcoal. When energy is supplied at the steady rate of \(10.8\mathrm{W}\) to a heater at the center, a temperature difference of \(50^{\circ}\mathrm{C}\) is set up between the spheres. Find the thermal conductivity of charcoal.  

4.20. The air above the surface of a freshwater lake is at a temperature \(T_{A}\) , while the water is at its freezing point \(T_{i}\) , where \(T_{A}< T_{i}\) . After a time \(t\) has elapsed, ice of thickness \(y\) has formed. Assuming that the heat, which is liberated when the water freezes, flows up through the ice by conduction and then into the air by natural convection, prove that  

\[
\frac{y}{h} +\frac{y^2}{2K} = \frac{T_i - T_A}{\rho L} t,
\]

where \(h\) is the convection coefficient per unit area and is assumed constant while ice forms, \(K\) is the thermal conductivity of ice, \(l\) is the latent heat of fusion of ice, and \(\rho\) is the density of ice. (Hint: The temperature of the upper surface is variable. Assume that the ice has a thickness \(y\) and imagine an infinitesimal thickness \(dy\) to form in time \(dt\).)  

4.21. A solid cylindrical copper rod \(0.10\mathrm{m}\) long has one end maintained at a constant temperature of \(20\mathrm{K}\) . The other end is blackened and exposed to thermal radiation from a body at \(300\mathrm{K}\) , with no energy lost or gained through the sides of the cylinder. When equilibrium is reached, what is the temperature difference between the two ends? (Hint: Refer to Fig. 4.7. )  

4.22. A cylindrical metal can, blackened on the outside, \(0.10\mathrm{m}\) high and \(0.05\mathrm{m}\) in diameter, contains liquid \(^4\mathrm{He}\) at its normal boiling point of \(4.22\mathrm{K}\) , at which its heat of vaporization is \(20.4\mathrm{kJ / kg}\) . Completely surrounding the helium can are walls maintained at the temperature of liquid nitrogen \((77.35\mathrm{K})\) , and the intervening space is continuously evacuated to a very low pressure. How much helium is lost per hour?  

4.23. The operating temperature of a tungsten filament in an incandescent lamp is \(2460\mathrm{K}\) , and its total emissivity is 0.30. Find the surface area of the filament of a 100- W lamp.  

4.24. A copper wire of length \(1.317\mathrm{m}\) and diameter \(3.26\times 10^{- 4}\mathrm{m}\) is blackened and placed along the axis of an evacuated glass tube. The wire is connected to a battery, a rheostat, an ammeter, and a voltmeter, and the current is increased until, at the moment the wire is about to melt, the ammeter reads \(12.8\mathrm{A}\) and the voltmeter reads \(20.2\mathrm{V}\) . Assuming that all the energy supplied was radiated and that the radiation from the glass tube is negligible, calculate the melting temperature of copper.  

4.25. The solar constant is the incident energy per unit of time on a unit area of a surface placed at right angles to a sunbeam just outside the earth's atmosphere. The value of the solar constant is \(1.37\mathrm{kW / m^2}\) . The area of a sphere with radius 93,000,000 miles is \(2.79\times 10^{23}\mathrm{m}^2\) , and the surface area of the sun is \(6.09\times 10^{18}\mathrm{m}^2\) . Assuming that the sun is a blackbody, calculate its surface temperature.  

4.26. (a) A small body with temperature \(T\) and emissivity \(\epsilon\) is placed in a large evacuated cavity with interior walls kept at temperature \(T_{W}\) . When \(T_{W} - T\) is small, show that the rate of heat transfer by radiation is  

\[
\frac{\mathrm{d}Q}{d t} = 4T_{W}^{3}A\epsilon \sigma (T_{W} - T).
\]

(b) If the body remains at constant pressure, show that the time for the temperature of the body to change from \(T_{1}\) to \(T_{2}\) is given by  

\[
t = \frac{C_{P}}{4T_{W}^{3}A\epsilon\sigma}\ln \frac{T_{W} - T_{1}}{T_{W} - T_{2}}.
\]

(c) Two small blackened spheres of identical size, one of copper and the other of aluminum, are suspended by silk threads within a large hole in a block of melting ice. It is found that it takes \(10\mathrm{min}\) for the temperature of the aluminum to drop from \(276\) to \(274\mathrm{K}\) , and \(14.2\mathrm{min}\) for the copper to drop the same interval of temperature. What is the ratio of specific heats of aluminum and copper? (The densities of Al and Cu are \(2.70\times 10^{3}\mathrm{kg / m^{3}}\) and \(8.96\times 10^{3}\mathrm{kg / m^{3}}\) at \(25^{\circ}\mathrm{C}\) respectively.)  

4.27. A blackened solid copper sphere with radius of \(0.02\mathrm{m}\) is placed in an evacuated enclosure with walls kept at \(100^{\circ}\mathrm{C}\) . In what time does its temperature change from 103 to \(102^{\circ}\mathrm{C}\) ? \((c_{P} = 0.395\mathrm{kJ / kg}\cdot \mathrm{K}; \rho = 8.96\times 10^{3}\mathrm{kg / m^{3}}\) at \(25^{\circ}\mathrm{C}\) .)  

4.28. In the case of a paramagnetic gas:  

(a) Derive the equation  

\[
\mathrm{d}Q = \left(\frac{\partial U}{\partial T}\right)_{V,\mathcal{M}}dT + \left[\left(\frac{\partial U}{\partial V}\right)_{M,T} + P\right]dV + \left[\left(\frac{\partial U}{\partial\mathcal{M}}\right)_{T,V} - \mu_{0}\mathcal{H}\right]d\mathcal{M}.
\]

(b) Derive expressions for \(C_{V,\mathcal{M}}, C_{V,\mathcal{M}}, C_{P,\mathcal{M}}\) , and \(C_{P,\mathcal{M}}\) .

===== Page 128 =====

5.1 EQUATION OF STATE OF A GAS  

It was emphasized in Chap. 1 that a gas is the best- behaved thermometric substance because of the fact that the ratio of the pressure \(P\) of a gas at any temperature to the pressure \(P_{TP}\) of the same gas at the triple point, as both \(P\) and \(P_{TP}\) approach zero, approaches a value independent of the nature of the gas. The limiting value of this ratio, multiplied by 273.16 K, was defined to be the ideal- gas temperature \(T\) of the system at whose temperature the gas exerts the pressure \(P\) . The reason for this regular behavior may be found by investigating the way in which the product \(PV\) of a gas depends on \(P\) .  

Suppose that the pressure \(P\) and the volume \(V\) of \(n\) moles of gas held at any constant temperature are measured over a wide range of values of the pressure, and the product \(Pv\) , where the molar volume \(v = V / n\) , is plotted as a function of \(P\) . Experiments of this sort were first performed by Amagat in France in 1870 and later by Holborn and Otto in Berlin and by Kamerlingh- Onnes and Keesom in Leiden. The relation between \(Pv\) and \(P\) may be expressed for a real gas by means of a power series (or virial expansion) of the form  

\[
Pv = A(1 + BP + CP^2 + \dots), \quad (5.1)
\]

where \(A\) , \(B\) , \(C\) , etc., are called virial coefficients ( \(A\) being the first virial coefficient, \(B\) the second, etc.) and depend on the temperature and on the nature of the gas. In the pressure range from 0 to about 40 standard atmospheres, the relation between \(Pv\) and \(P\) is practically linear, so that only the first two terms in the expansion are significant. In general, the greater the pressure range, the larger the number of terms in the virial expansion.
===== Page 129 =====

 The remarkable property of gases that makes them so valuable in thermometry is displayed in Fig. 5- 1, where the product \(Pv\) is plotted against \(P\) for four different gases, all at the temperature of boiling water in the top graph, all at the triple point of water in the middle graph, and all at the temperature of solid \(\mathrm{CO}_{2}\) in the bottom graph. In each case, it is seen that, as the pressure approaches zero, the product \(Pv\) approaches the same value for all gases at the same temperature. It follows from this that the first virial coefficient \(A\) is independent of the nature of the gas and depends only on temperature. Thus,  

\[
\lim_{P\to 0}(Pv) = \mathbf{A} = \left\{ \begin{array}{ll}\mathrm{function~of~temperature~only,} & \mathrm{(5.2)}\\ \mathrm{independent~of~gas.} & \mathrm{(5.2)} \end{array} \right. \quad (5.2)
\]

The ideal- gas temperature \(T\) is defined in Eq. (1.7) as  

\[
T = 273.16\mathrm{K}\lim_{P_{TP}\to 0}\left(\frac{P}{P_{TP}}\right)\qquad (\mathrm{const.}V),
\]

\[
T = 273.16\mathrm{K}\lim \frac{P V / n}{P_{T P}V / n} = 273.16\mathrm{K}\frac{\lim (P\nu)}{\lim (P\nu)_{T P}},
\]

\[
\lim (P\nu) = \left[\lim (P\nu)_{T P}\right]T.
\]

The bracketed term is called the molar gas constant and is denoted by \(R\) . Thus,  

\[
R = \frac{\lim (P\nu)_{T P}}{273.16\mathrm{K}}. \quad (5.3)
\]

In 1972, Batuecas determined \(\lim (P\nu)_{0^{\circ}\mathrm{C}}\) for oxygen to be 22.4132 liter \(\cdot\) atm/ mol (2.27102 kJ/mol). Hence, the gas constant \(R\) was determined to have the value of 8.31441 J/mol \(\cdot\) K with an uncertainty of 31 parts per million in the 1973 recommendations of physical constants by the international Committee on Data for Science and Technology (CODATA). However, measurements of volume in the determination of \(R\) by the method of limiting density are beset with the problem of adsorption of gas on the walls of the container. Furthermore, the uncertainty in the normal melting temperature of ice is greater than the uncertainty of the triple- point temperature of water. For these reasons, an improved method for determining a more precise value of the molar gas constant \(R\) will be presented in Sec. 5.7.  

Finally, substituting for \(\nu\) its value \(V / n\) , we may write the equation of state of a gas in the limit of low pressures in the form  

\[
\lim (P V) = n R T, \quad (5.4)
\]

which is the experimental equation of state for the ideal gas. Since \(\lim (P\nu) = A = RT\) , Eq. (5.1) becomes  

\[
\frac{P\nu}{R T} = 1 + B P + C P^{2} + D P^{3} + \dots .
\]

The virial coefficients play an important role, not only in practical thermodynamics, but also in theoretical physics, where they are related to molecular properties. Except at very low temperatures, the virial coefficients are quite small, as shown in Table 5.1, where the virial coefficients are given for nitrogen in the temperature range 150 to \(500\mathrm{K}\) .  

### 5.2 INTERNAL ENERGY OF A REAL GAS  

Imagine a thermally insulated vessel with rigid walls, divided into two compartments by a partition. Suppose that there is a gas in one compartment and that the other contains a vacuum. If the partition is removed, the gas will undergo what is known as an adiabatic free expansion in which no work is done and no heat is transferred. From the first law, since both \(Q\) and \(W\) are zero, it follows that the internal energy remains unchanged during a free expan

===== Page 131 =====

 TABLE 5.1  Viral coefficients for nitrogen  

| T, K | B, \(10^{-9}\) Pa\(^{-1}\) | C, \(10^{18}\) Pa\(^{-2}\) | D, \(10^{27}\) Pa\(^{-3}\) |
| :--- | :--- | :--- | :--- |
| 150 | -55.13 | -2425 | -999 |
| 200 | -20.97 | -7.805 | 55,050 |
| 250 | -7.792 | 291 | 14,270 |
| 300 | -1.812 | 203 | 2860 |
| 350 | 1.18 | 152 | -202 |
| 400 | 2.75 | 111 | -93 |
| 450 | 3.59 | 81.6 | -99 |
| 500 | 4.03 | 60.7 | -856 |

sion. The question of whether or not the temperature of a gas changes during a free expansion and, if it does, of the magnitude of the temperature change has engaged the attention of scientists for about a hundred years. Starting with Joule in 1843, many attempts have been made to measure either the quantity \((\partial T / \partial V)_{U}\) , which is called the Joule coefficient, or related quantities that are all a measure, in one way or another, of the effect of an adiabatic free expansion, or as it is often called, Joule expansion.  

In order to study the free expansion of a gas and to measure \((\partial T / \partial V)_{U}\) Joule connected two vessels by a short tube and stopcock, which were immersed in a water bath. One vessel contained air at high pressure, and the other was evacuated. The temperature of the water was measured before and after the expansion, the idea being to measure indirectly the drop in temperature of the gas from the decrease in temperature of the water. Since the heat capacity of the vessels and the water was approximately 1000 times as large as the heat capacity of the air, Joule was unable to detect any temperature change of the water, although, in the light of our present knowledge, the air must have undergone a temperature decrease of several degrees. A direct measurement of the temperature change associated with a free expansion is so difficult that it is necessary to give up directly measuring the Joule coefficient \((\partial T / \partial V)_{U}\) . Instead of measuring a temperature change during a free expansion for which the internal energy is constant, consider measuring a change of internal energy for constant temperature.  

In general, the internal energy of any gas is a function of any two of the coordinates \(P\) , \(V\) , and \(T\) . The differential of \(U\) as a function of \(T\) and \(V\) is  

\[
dU = \left(\frac{\partial U}{\partial T}\right)_V dT + \left(\frac{\partial U}{\partial V}\right)_T dV.
\]

If no temperature change \((dT = 0)\) takes place in a free expansion \((dU = 0)\) then it follows that  

\[
\left(\frac{\partial U}{\partial V}\right)_T = 0;
\]

===== Page 132 =====

110 PART I: Fundamental Concepts  

or, in other words, \(U\) does not depend on \(V\) . Considering \(U\) to be a function of \(T\) and \(P\) , we have  

\[
dU = \left(\frac{\partial U}{\partial T}\right)_P dT + \left(\frac{\partial U}{\partial P}\right)_T dP.
\]

If no temperature change \((dT = 0)\) takes place in a free expansion \((dU = 0)\) , then it follows that  

\[
\left(\frac{\partial U}{\partial P}\right)_T = 0;
\]

or, in other words, \(U\) does not depend on \(P\) . Then, it is apparent that, if no temperature change takes place in a free expansion of a gas, \(U\) is independent of \(V\) and of \(P\) , and, therefore, \(U\) is a function of \(T\) only. Thus, to determine if the internal energy is a function of temperature, one must perform an experiment where the temperature is constant and measure whether either \((\partial U / \partial V)_T\) or \((\partial U / \partial P)_T\) is zero.  

Later methods of attacking the question of the temperature dependence of the internal energy of a gas involved the measurement of the quantity \((\partial u / \partial P)_T\) , where \(u\) is the molar internal energy, by having the gas undergo an isothermal expansion in which heat is transferred and work is done. The most extensive series of measurements of this kind was performed by Rossini and Frandsen in 1932 at the National Bureau of Standards. The apparatus is shown in Fig. 5- 2. A container \(B\) holds \(n\) moles of gas at a pressure \(P\) and communicates with the atmosphere through a long coil wrapped around the  

FIGURE 5- 2 Apparatus for measuring \((\partial u / \partial P)_T\) of a gas. (F. D. Rossini and M. Frandsen: Journal of Research of the National Bureau of Standards, vol. 9, pp. 733- 747, 1932. )

===== Page 133 =====

 container. The whole apparatus is immersed in a water bath whose temperature can be maintained constant at exactly the same value as that of the surrounding atmosphere.  

The experiment is performed as follows. When the valve is opened slightly, the gas flows slowly through the long coil and out into the air. At the same time, the temperature of the gas, the container, the coils, and the water is maintained constant by an electric heating coil immersed in the water. The electrical energy supplied to the water is, therefore, the heat \(Q\) absorbed by the gas during the expansion. The work done by the gas is evidently  

\[
W = -P_{0}(n\nu_{0} - V),
\]

where \(P_{0}\) is atmospheric pressure, \(\nu_{0}\) is the molar volume at atmospheric temperature and pressure, \(V\) is the volume of the container, and \(n\nu_{0}\) is larger than \(V\) .  

If \(u(P,T)\) is the molar internal- energy at pressure \(P\) and temperature \(T\) and if \(u(P_{0},T)\) is the molar internal- energy at atmospheric pressure and the same temperature, then, from the first law, the change of molar internal- energy can be expressed in terms of the measured quantities \(Q\) and \(W\) as  

\[
u(P,T) - u(P_0,T) = \frac{Q + W}{n},
\]

provided that corrections have been made to take account of the energy changes due to the contraction of the walls of the container. In this way, the change of molar internal- energy \(\Delta u\) was measured for various values of the initial pressure \(P\) at constant temperature \(T\) . The values of \(\Delta u\) were plotted against the corresponding pressure \(P\) , as shown in Fig. 5- 3. Since \(u(P_{0},T)\) is constant, the slope of the resulting curve is equal to \((\partial u / \partial P)_{T}\) at any value of \(P\) . Within the pressure range of 1 to 40 standard atmospheres, the experimental points fall on a straight line, meaning that \((\partial u / \partial P)_{T}\) has the same value at every pressure; that is, \((\partial u / \partial P)_{T}\) is independent of the pressure, depending only on the temperature. Thus,  

\[
\left(\frac{\partial u}{\partial P}\right)_{T} = f(T).
\]

Rossini and Frandsen's experiments with air, oxygen, and mixtures of oxygen and carbon dioxide led to the conclusion that the internal energy of a real gas is a function of both temperature and pressure. They found no pressure or temperature range in which the quantity \((\partial u / \partial P)_{T}\) was equal to zero. In other words, their real gases did not reach the low- pressure limit of the ideal gas.  

Their experiment has somewhat the same disadvantage as Joule's original experiment, in that the heat capacity of the gas is much smaller than that of the calorimeter and water bath. To keep the temperature of the gas constant within reasonable limits, the temperature of the water must be kept constant to within less than a thousandth of a degree. In Rossini and Frandsen's measurements, the final precision was estimated to be \(2\frac{1}{2}\) percent.

===== Page 134 =====

112 PART I: Fundamental Concepts  

FIGURE 5-3 Dependence of change of molar internal energy of a real gas on pressure, where \(P_0\) is atmospheric pressure.  

### 5.3 IDEAL GAS  

We have seen that, in the case of a real gas, only in the limit as the pressure approaches zero does the equation of state assume the simple form \(PV = nRT\) . Furthermore, the internal energy of a real gas is a function of pressure as well as temperature. It is convenient at this point to define the ideal gas whose properties, while not corresponding to those of any existing gas, are approximately those of a real gas at low pressures. By definition, the ideal gas satisfies the equations  

\[
\left[\begin{array}{c}{PV=nRT\] \[\left(\frac{\partial U}{\partial P}\right)_{T}=0}\end{array}\right]\qquad(\mathrm{ideal~gas}). \quad (5.5)
\]

The requirement that \((\partial U / \partial P)_T = 0\) may be written in other ways. Thus,  

\[
\left(\frac{\partial U}{\partial V}\right)_T = \left(\frac{\partial U}{\partial P}\right)_T\left(\frac{\partial P}{\partial V}\right)_T,
\]

and since \((\partial P / \partial V)_T = - nRT / V^2 = - P / V\) , and, therefore, is not zero, while \((\partial U / \partial P)_T\) is zero, it follows that for the ideal gas

===== Page 135 =====

5: Ideal Gas 113  

\[
\left(\frac{\partial U}{\partial V}\right)_T = 0 \quad (\text{ideal gas}). \quad (5.6)
\]

Finally, since both \((\partial U / \partial P)_T\) and \((\partial U / \partial V)_T\) are zero,  

\[
U = f(T) \text{ only}. \quad (5.7)
\]

Whether a real gas may be treated as the ideal gas depends upon the error that may be tolerated in a given calculation. A real gas at pressures below about twice standard atmospheric pressure may be treated as the ideal gas without introducing an error greater than a few percent. Even in the case of a saturated vapor in equilibrium with its liquid, the ideal- gas equation of state may be used with only a small error if the vapor pressure is low.  

For an infinitesimal quasi- static process of a hydrostatic system, the first law is  

\[
\mathrm{d}Q = dU + P dV,
\]

and the heat capacity at constant volume is given by  

\[
C_V = \left(\frac{\partial U}{\partial T}\right)_V.
\]

In the special case of the ideal gas, \(U\) is a function of \(T\) only; therefore, the partial derivative with respect to \(T\) is the same as the total derivative. Consequently,  

\[
C_V = \frac{dU}{dT},
\]

and  

\[
\mathrm{d}Q = C_V dT + P dV. \quad (5.8)
\]

Now, all equilibrium states are represented by the ideal- gas equation,  

\[
P V = n R T,
\]

and, for an infinitesimal quasi- static process,  

\[
P d V + V d P = n R d T.
\]

Substituting the above in Eq. (5.8), we get  

\[
\mathrm{d}Q = (C_V + n R) d T - V d P,
\]

and dividing by \(dT\) yields  

\[
\frac{\mathrm{d}Q}{dT} = C_V + n R - V \frac{dP}{dT}.
\]

At constant pressure, the left- hand member becomes \(C_P\) and \(dP = 0\) ; therefore,  

\[
C_P = C_V + n R \quad (\text{ideal gas}). \quad (5.9)
\]

===== Page 136 =====

114 PART I: Fundamental Concepts  

We have the result, therefore, that the heat capacity of an ideal gas at constant pressure is always larger than the heat capacity at constant volume, the difference remaining constant and equal to \(nR\) . The reason that \(C_P\) is always larger than \(C_V\) is the following: As heat is supplied to a system at constant pressure, the gas expands and works against the external pressure, which, of course, is equal to the pressure of the gas in a quasi- static process. Thus, \(C_P\) includes work of expansion, which is not found in the constant volume \(\left(\int P dV = 0\right)\) heat capacity \(C_V\) .  

Since \(U\) is a function of \(T\) only for an ideal gas, it follows that  

\[
C_V = \frac{dU}{dT} = \mathrm{a~function~of~}T\mathrm{~alone},
\]

and so  

\[
C_P = C_V + nR = \mathrm{a~function~of~}T\mathrm{~alone}.
\]

One more useful equation can be obtained. Since  

\[
\mathrm{d}Q = (C_V + nR)dT - VdP,
\]

we find  

\[
\mathrm{d}Q = C_PdT - VdP. \quad (5.10)
\]

### 5.4 EXPERIMENTAL DETERMINATION OF HEAT CAPACITIES  

The heat capacities of real gases are measured by the electrical method. To measure \(C_V\) , the gas is contained in a thin- walled steel flask with a heating wire wound around it. By maintaining an electric current in the wire, an equivalent amount of heat is supplied to the gas, and the heat capacity at constant volume is obtained by measuring the temperature rise of the gas. The same method is used to measure \(C_P\) except that, instead of confining the gas to a constant volume, the gas is allowed to flow at constant pressure through a calorimeter, where it receives electrically a known equivalent heat per unit of time. From the initial (inlet) and final (outlet) temperatures, the rate of supply of heat, and the rate of flow of gas, the value of \(C_P\) is calculated.  

The results of such measurements on gases at low pressures, that is, ideal gases, can be stated in a simple manner in terms of molar heat capacities.  

1. All ideal gases:  

(a) \(c_V\) is a function of \(T\) only.  

(b) \(c_P\) is a function of \(T\) only, and is greater than \(c_V\) .  

(c) \(c_P - c_V\) is not a function of \(T\) , but equal to \(R\) .  

(d) the ratio \(c_P / c_V = \gamma\) is a function of \(T\) only, and is greater than 1.  

2. Monatomic gases, such as He, Ne, and A, and most metallic vapors, such as the vapors of Na, Cd, and Hg:

===== Page 137 =====

(a) \(c_{V}\) is constant over a wide temperature range and is very nearly equal to \(\frac{3}{2} R\) .  

(b) \(c_{P}\) is constant over a wide temperature range and is very nearly equal to \(\frac{5}{2} R\) .  

(c) the ratio \(c_{P} / c_{V} = \gamma\) is constant over a wide temperature range and is very nearly equal to \(\frac{5}{3}\) .  

3. So-called permanent diatomic gases, namely, air, \(\mathrm{H}_{2}\) , \(\mathrm{D}_{2}\) , \(\mathrm{O}_{2}\) , \(\mathrm{N}_{2}\) , \(\mathrm{NO}\) , and \(\mathrm{CO}\) :  

(a) \(c_{V}\) is constant at ordinary temperatures, being equal to about \(\frac{5}{2} R\) , and increases as the temperature is raised.  

(b) \(c_{P}\) is constant at ordinary temperatures, being equal to about \(\frac{7}{2} R\) , and increases as the temperature is raised.  

(c) the ratio \(c_{P} / c_{V} = \gamma\) is constant at ordinary temperatures, being equal to about \(\frac{7}{5}\) , and decreases as the temperature is raised.  

4. Polyatomic gases and gases that are chemically active, such as \(\mathrm{CO}_{2}\) , \(\mathrm{NH}_{3}\) , \(\mathrm{CH}_{4}\) , \(\mathrm{Cl}_{2}\) , and \(\mathrm{Br}_{2}\) :  

\(c_{P}\) , \(c_{V}\) , and \(c_{P} / c_{V}\) vary with the temperature, the variation being different for each gas.  

These experimental results indicate that the molar gas constant \(R = 8.315 \mathrm{J / mol \cdot K}\) is a natural unit with which to express the molar heat capacity of a gas. It is a very interesting consequence of theory that the universal gas constant is also the natural unit for solids. In the remainder of this book, we shall specify not the molar heat capacities themselves but the ratios \(c_{V} / R\) and \(c_{P} / R\) .  

The behavior of hydrogen gas \(\mathrm{(H_{2})}\) is quite exceptional, as shown in Fig. 5- 4. At very low temperatures, \(c_{P} / R\) drops to a value of \(\frac{5}{2}\) , appropriate to a monatomic gas, even though hydrogen is a diatomic gas. At room temperature, \(c_{P} / R\) for hydrogen has its expected value of \(\frac{7}{2}\) . For all other diatomic gases, \(c_{P} / R\) may always be written  

\[
\frac{c_{P}}{R} = \frac{7}{2} +f(T),
\]

where \(f(T)\) is often one or more functions of the type  

\[
\left(\frac{b}{T}\right)^{2}\frac{e^{b / T}}{(e^{b / T} - 1)^{2}}.
\]

Exact equations of the above type are difficult to handle and are not suitable for the practical calculations of the laboratory scientist; consequently, approximate empirical equations are used. Empirical equations for \(c_{P} / R\) of some of the most important gases, compiled by H. M. Spencer, are given in Table 5.2, within the temperature range 300 to 1500 K.

===== Page 138 =====

116 PART I: Fundamental Concepts  

FIGURE 5-4  

Experimental values of \(c_{P} / R\) for hydrogen as a function of temperature, plotted on a logarithmic scale.  

TABLE 5.2 \(c_{P} / R\) of important gases \(c_{P} / R = a + bT + cT^{2}\) (from 300 to 1500 K)   

| Gas | a | b, \(10^{-3}\) K\(^{-1}\) | c, \(10^{-6}\) K\(^{-2}\) |
| :--- | :--- | :--- | :--- |
| H\(_2\) | 3.495 | -0.101 | 0.243 |
| O\(_2\) | 3.068 | 1.638 | -0.512 |
| Cl\(_2\) | 3.813 | 1.220 | -0.486 |
| Br\(_2\) | 4.240 | 0.490 | -0.179 |
| N\(_2\) | 3.247 | 0.712 | -0.041 |
| CO | 3.192 | 0.924 | -0.141 |
| HCl | 3.389 | 0.218 | 0.186 |
| HBr | 3.311 | 0.481 | 0.079 |
| CO\(_2\) | 3.206 | 5.082 | -1.714 |
| H\(_2\)O | 3.634 | 1.195 | 0.135 |
| NH\(_3\) | 3.116 | 3.970 | -0.366 |
| H\(_2\)S | 3.214 | 2.871 | -0.608 |
| CH\(_4\) | 1.702 | 9.083 | -2.164 |

### 5.5 QUASI-STATIC ADIABATIC PROCESS  

When an ideal gas undergoes a quasi- static adiabatic process, the pressure, volume, and temperature change in a manner that is described by a relation between \(P\) and \(V\) , \(T\) and \(V\) , or \(P\) and \(T\) . In order to derive the relation between \(P\) and \(V\) , we start with Eqs. (5.8) and (5.10). Thus,

===== Page 139 =====

and  

\[
\mathrm{d}Q = C_{V}dT + P dV,
\]

\[
\mathrm{d}Q = C_{P}dT - VdP.
\]

In an adiabatic process, \(\mathrm{d}Q = 0\) , so  

\[
V d P = C_{P}d T,
\]

and  

\[
P d V = -C_{V}d T.
\]

Dividing the first equation by the second, we obtain  

\[
\frac{dP}{P} = -\frac{C_{P}}{C_{V}}\frac{dV}{V},
\]

and denoting the ratio of the heat capacities by the symbol \(\gamma\) , we have  

\[
\frac{dP}{P} = -\gamma \frac{dV}{V}.
\]

This equation cannot be integrated until we know the structure of the gas, which determines \(\gamma\) . We have seen that for monatomic gases, \(\gamma\) is constant. For diatomic and polyatomic gases, \(\gamma\) varies with the temperature; a very large change of temperature produces an appreciable change in \(\gamma\) . For example, in the case of the carbon monoxide, a temperature rise from 300 to 3000 K produces a decrease in \(\gamma\) from 1.40 to 1.29. Most adiabatic processes that we encounter do not involve such a large temperature change. Therefore, in an adiabatic process that involves only a moderate temperature change, we are entitled to neglect the small accompanying change in \(\gamma\) . Regarding \(\gamma\) , therefore, as constant, and integrating, we obtain  

\[
\ln P = -\gamma \ln V + \ln \mathrm{const.},
\]

or  

\[
P V^{\gamma} = \mathrm{const.} \quad (5.11)
\]

This equation of state holds at all equilibrium states through which the ideal gas passes during a quasi- static adiabatic process. It is important to understand that a free expansion is an adiabatic process but is not quasi- static, because the gas rushing into the vacuum passes through nonequilibrium states before finally achieving equilibrium. Therefore, Eq. (5.11) cannot be applied to the states traversed by the ideal gas during a free expansion or any adiabatic process that is not quasi- static.  

A family of curves representing quasi- static adiabatic processes may be plotted on a \(P V\) diagram by assigning different values to the constant in Eq. (5.11). The slope of any adiabatic curve is  

\[
\left(\frac{\partial P}{\partial V}\right)_{S} = -\gamma \mathrm{const.} V^{-\gamma -1}
\]

or  

\[
\left(\frac{\partial P}{\partial V}\right)_{S} = -\gamma \frac{P}{V}, \quad (5.12)
\]

where the subscript \(S\) is used to denote a reversible adiabatic process.
===== Page 140 =====

118 PART I: Fundamental Concepts  

FIGURE 5-5 The \(PVT\) surface for the ideal gas and its projection onto a \(PV\) diagram. (Isotherms are shown as dashed curves, and adiabatics as full curves.)  

Quasi- static isothermal processes are represented by a family of equilateral hyperbolas obtained by assigning different values to \(T\) in the equation \(PV = nRT\) . Since  

\[
\left(\frac{\partial P}{\partial V}\right)_T = -\frac{P}{V}, \quad (5.13)
\]

it follows that an adiabatic curve has a steeper negative slope than does an isothermal curve at the same point, since \(\gamma > 1\) .  

The isothermal curves and adiabatic curves of the ideal gas may be shown in a revealing way on a \(PVT\) surface. If \(P\) , \(V\) , and \(T\) are plotted along rectangular axes, the resulting surface is shown in Fig. 5- 5, where it may be seen that the adiabatic curves cut across the isotherms.  

### 5.6 RUCHHARDT'S METHOD OF MEASURING \(\gamma\)  

An ingenious method of measuring \(\gamma\) , developed by Rüchhardt in 1929, makes use of elementary mechanics, rather than thermodynamics. The gas is contained in a large jar of volume \(V\) . Fitted to the jar (see Fig. 5- 6) is a glass tube with an accurate bore of cross- sectional area \(A\) , into which a metal ball of mass \(m\) fits snugly like a piston. Since the gas is slightly compressed by the

===== Page 141 =====

 FIGURE 5- 6 Mechanical apparatus for measuring the ratio of heat capacities \(\gamma\) . (E. Rüchhardt: Physikalische Zeitschrift, vol. 30, pp. 58- 59, 1929. )  

steel ball in its equilibrium position, its pressure \(P\) is slightly larger than atmospheric pressure \(P_{0}\) . Thus, neglecting friction,  

\[
P = P_{0} + \frac{mg}{A}.
\]

If the ball is given a slight downward displacement and then let go, it will oscillate with a period \(\tau\) . Friction will cause the ball to come to rest eventually. Let the displacement of the ball from its equilibrium position at any moment be denoted by \(y\) , where \(y\) is positive when the ball is above the equilibrium position and negative below. A small positive displacement causes an increase in volume which is very small compared with the equilibrium volume \(V\) and which, therefore, can be denoted by \(dV\) , where  

\[
dV = yA.
\]

Similarly, a small positive displacement causes a decrease in pressure which is very small compared with the equilibrium pressure \(P\) and which, therefore, can be denoted by \(dP\) , where \(dP\) is a negative quantity. The resultant force \(F\) acting on the ball is equal to \(A dP\) if we neglect friction, or  

\[
dP = \frac{F}{A}.
\]

Notice that, when \(y\) is positive, \(dP\) is negative and, therefore, \(F\) is negative; that is, \(F\) is a restoring force.  

Now, as the ball oscillates fairly rapidly, the variations of \(P\) and \(V\) are adiabatic, because there is not enough time for appreciable heat transfer. Since the variations are also quite small, the states through which the gas passes can be considered to be approximately states of equilibrium. Therefore, we may assume that the changes of \(P\) and \(V\) represent an approximately quasi- static adiabatic process, and we may write

===== Page 142 =====

120 PART I: Fundamental Concepts  

\[
PV^{\gamma} = \mathrm{const.},
\]

and  

\[
\gamma PV^{\gamma -1}dV + V^{\gamma}dP = 0.
\]

Substituting for \(dV\) and \(dP\) , we get  

\[
F = -\frac{\gamma P A^{2}}{V} y.
\]

This equation expresses the fact that the restoring force is directly proportional to the displacement and is in the opposite direction, which is Hooke's law. This is precisely the condition for simple harmonic motion, for which the period \(\tau\) is  

\[
\tau = 2\pi \sqrt{\frac{m}{-F / y}}.
\]

Consequently,  

\[
\tau = 2\pi \sqrt{\frac{mV}{\gamma P A^{2}}},
\]

and, as a result,  

\[
\gamma = \frac{4\pi^{2}m V}{A^{2}P\tau^{2}}. \quad (5.14)
\]

The mass of the ball, the volume, the cross- sectional area of the tube, and the pressure are all known beforehand, and only the period has to be measured to obtain \(\gamma\) . The values obtained by Rüchhardt's mechanical measurements for air and for \(\mathrm{CO}_{2}\) were in good agreement with those obtained from calorimetric measurements of heat capacities.  

Rüchhardt's method involves errors due to three simplifying assumptions: (1) that the gas is ideal; (2) that there is no friction; and (3) that volume changes are strictly adiabatic. It is estimated that the second assumption is responsible for the largest error, amounting to about 3 percent.  

A modification of Rüchhardt's experiment in which accurate account is taken of the real equation of state of the gas, the friction present, and the departure from strict adiabatic conditions, was achieved by Clark and Katz in 1940. The method was adapted for an undergraduate teaching laboratory by D. G. Smith in 1979. A steel piston at the center of a cylindrical tube divides the gas into two equal parts, as shown in Fig. 5- 7. It is set in vibration at any desired frequency by external coils in which an alternating current of suitable frequency is maintained. The cylinder is kept in a horizontal position, and friction between the piston and the cylinder is reduced by balancing the weight of the piston by the attraction of an electromagnet.  

The amplitude of vibration of the piston is measured, using a microscope equipped with a micrometer eyepiece, at a number of values of the frequency of the impressed alternating current, and the resonance curve is plotted. From the resonance frequency and very elaborate calculations not involving the assumptions made by Rüchhardt, the value of \(\gamma\) is calculated. Since friction

===== Page 143 =====

 FIGURE 5-7 Resonance method of measuring the ratio of heat capacities \(\gamma\) of a real gas as a function of pressure. (A. L. Clark and L. Katz: Canadian Journal of Research, ser. A, vol. 21, pp. 1-17, 1943. )  

TABLE 5.3 Pressure variation of \(\gamma\) \(\gamma = a + bP + cP^{2})\)   

| Gas | Temp., K | a | b, \(10^{-9}\) Pa\(^{-1}\) | c, \(10^{-12}\) Pa\(^{-2}\) | \(\gamma\) extrapolated to zero pressure (ideal gas) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| He | 296.25 | 1.6669 | -1.97 | 0 | 1.667 |
| Ar | 297.35 | 1.6667 | 3.48 | 0 | 1.667 |
| H\(_2\) | 296.55 | 1.4045 | 2.47 | 0 | 1.405 |
| N\(_2\) | 296.15 | 1.4006 | 21.80 | 0 | 1.401 |
| CO\(_2\) | 303.05 | 1.2857 | 62.10 | 0 | 1.286 |
| N\(_2\)O | 298.45 | 1.2744 | 22.20 | 0.0948 | 1.274 |
| CH\(_4\) | 298.25 | 1.3029 | -10.40 | 0.0472 | 1.303 |

was reduced to a great extent by the lift magnet, the corrections amounted to only about 1 percent. The authors measured \(\gamma\) at various pressures from 1 to 25 standard atmospheric pressures and expressed the results in the form of empirical equations, as shown in Table 5.3.  

### 5.7 VELOCITY OF A LONGITUDINAL WAVE  

Let us consider a gas enclosed in a cylinder and held in place by a piston exerting pressure \(P\) , as shown in the upper part of Fig. 5- 8. If a compression is produced by moving the piston to the right at constant velocity \(w_{0}\) , the wave

===== Page 144 =====

122 PART I: Fundamental Concepts  

FIGURE 5-8  

Propagation of a compression with constant velocity \(w\) through a gas caused by the motion of a piston with constant velocity \(w_{0}\) . Upper diagram at the start; lower diagram after time \(t\) .  

front of the pressure pulse will travel with a different constant velocity \(w\) , depending on properties of the gas that we shall now proceed to determine. The "free body" for Newton's second law is volume \(V\) of the gas whose initial uncompressed length is \(w t\) and whose uncompressed volume \(V = A w t\) , where \(A\) is the cross- sectional area of the cylinder. If \(\rho\) is the density of the normal or uncompressed gas, the mass of the free body is \(\rho A w t\) .  

Let us suppose that the piston shown in the lower part of Fig. 5- 8 exerts a force \(A(P + \Delta P)\) as the piston moves to the right with a constant velocity \(w_{0}\) . The compression moves with constant velocity \(w\) , so that in time \(t\) the compression has traveled a distance \(w t\) while the piston has traveled a distance \(w_{0} t\) . At time \(t\) ,  

\[
\text{Rate of increase of mass} \left\{ \begin{array}{l} \rho A w t \\ \displaystyle \frac{\rho A w t}{t} = \rho A w. \end{array} \right.
\]

The entire compressed column has a velocity \(w_{0}\) equal to that of the piston. Therefore,  

\[
\text{Rate of increase of momentum} \left\{ \begin{array}{l} \rho A w w_{0}. \\ \displaystyle \frac{\rho A w w_{0}}{t} = \rho A w w_{0}. \end{array} \right.
\]

The free body is acted on by a force \(A(P + \Delta P)\) to the right and a force \(A P\) to the left. Therefore,

===== Page 145 =====

 Unbalanced force on the \(\left\{ \begin{array}{l} \text { compressed column } \\ \text { compressed column } \end{array} \right\} = A \Delta P.\)  

From Newton's second law, the unbalanced force is equal to the rate of change of momentum,  

\[
A \Delta P = \rho A w w_{0},
\]

or  

\[
\Delta P = \rho w^{2} \frac{w_{0}}{w}.
\]

The "uncompressed free body" of volume \(V = A w t\) has undergone a compression \((- \Delta V) = A w_{0} t\) . That is,  

\[
-\frac{\Delta V}{V} = \frac{A w_{0} t}{A w t} = \frac{w_{0}}{w}.
\]

Therefore,  

\[
\Delta P = \rho w^{2}\left(-\frac{\Delta V}{V}\right),
\]

which may be written  

\[
w^{2} = \frac{-1}{\frac{\rho}{V}\left(\frac{\Delta V}{\Delta P}\right)}. \quad (5.15)
\]

This formula was first obtained by Newton, who regarded the quantity \((1 / V)(\Delta V / \Delta P)\) as the isothermal compressibility. It was shown later by Laplace that the expression is really the adiabatic compressibility. To see why this is so, let us consider a column of gas of cross section \(A\) , bounded by two planes, one at the center of a compression and the other at the center of a rarefaction, a distance \(\lambda /2\) apart, where \(\lambda\) is the wavelength. Let us suppose that the temperature at the center of the compression exceeds the temperature at the center of the rarefaction by an amount \(\Delta T\) . Then, the heat conducted a distance \(\lambda /2\) in the time \(\lambda /2 w\) (time for the wave to travel the distance \(\lambda /2\) ) is given by  

\[
\text{Heat conducted in the time for the } \left\{ \begin{array}{l l}{K A\frac{\Delta T}{\lambda / 2}\frac{\lambda}{2w} = K A\frac{\Delta T}{w},} \end{array} \right.
\]

where \(K\) is the thermal conductivity of the medium. The mass of material between the compression and rarefaction is \(\rho A \lambda /2\) , and the heat necessary to raise the temperature of this mass by the amount \(\Delta T\) is  

\[
\text{Heat necessary to raise temperature } \left\{ \begin{array}{l l}{\lambda\] \[\lambda\] \[\lambda} \end{array} \right\} = \rho A \frac{\lambda}{2} c_{V} \Delta T,
\]

where \(c_{V}\) is the molar heat capacity at constant volume.  

The propagation of the wave would be adiabatic if the conducted heat were much too small to raise the temperature of the mass \(\rho A \lambda /2\) by the amount \(\Delta T\) , or

===== Page 146 =====

124 PART I: Fundamental Concepts  

\[
\frac{K A\Delta T}{w}\ll \rho A\frac{\lambda}{2} c_{V}\Delta T\qquad \mathrm{(adiabatic~condition)}.
\]

This may be written  

\[
\frac{2K}{w\rho c_{V}}\ll \lambda \qquad \mathrm{(adiabatic~condition)}.
\]

The usual range of wavelengths of compressional waves is from a few centimeters to a few hundred centimeters. Let us compare these values with \(2K / w\rho c_{V}\) . Taking a gas like air as a typical case, we have, roughly,  

\[
K = 0.02\mathrm{W / m\cdot K},
\]
\[
w = 3\times 10^{2}\mathrm{m / s},
\]
\[
\rho = 1\mathrm{kg / m^{3}},
\]
\[
c_{V} = 0.4\mathrm{kJ / kg\cdot K},
\]

and  

\[
\frac{2K}{w\rho c_{V}} = \frac{2(0.02\mathrm{W / m\cdot K})}{(3\times 10^{2}\mathrm{m / s})(1\mathrm{kg / m^{3}})(0.4\mathrm{kJ / kg\cdot K})}
\]
\[
= 330\times 10^{-9}\mathrm{m}
\]
\[
= 330\mathrm{nm}
\]

In the case of a metal, \(K\) would be much larger, but this would be compensated by the much larger values of \(w\) and \(\rho\) , and the quantity \(2K / w\rho c_{V}\) would be still smaller than \(330\mathrm{nm}\) . This quantity is, therefore, seen to be so much smaller than the usual value of a wavelength of a compressional wave (330nm is the wavelength of ultraviolet light) that the adiabatic condition is well fulfilled. Therefore, we conclude that, in view of the properties of ordinary matter, the volume changes which take place under the influence of a longitudinal wave at ordinary frequencies are adiabatic, not isothermal.  

Returning now to Eq. (5.15) for the velocity of a longitudinal wave and identifying \((- 1 / V)(\Delta V / \Delta P)\) as the reversible adiabatic compressibility \(\kappa_{S}\) , we have, finally,  

\[
w^{2} = \frac{1}{\rho\kappa_{S}}. \quad (5.16)
\]

The adiabatic compressibility can be calculated for the ideal gas using Eq. (5.12); thus,  

\[
\kappa_{S} = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{S} = \frac{1}{\gamma P}.
\]

Since the density is

===== Page 147 =====

\[
\rho = \frac{M}{\nu},
\]

where \(M\) is the molar mass and the \(\nu\) is the molar volume, Eq. (5.16) becomes  

\[
w^{2} = \frac{\gamma P\nu}{M},
\]

\[
w^{2} = \frac{\gamma RT}{M}. \quad (5.17)
\]

Equation (5.17) allows us to calculate \(\gamma\) from experimental measurements of \(w\) and \(T\) . For example, the speed of sound in air at \(0^{\circ}\mathrm{C}\) is about \(331~\mathrm{m / s}\) . Therefore, using the values  

\[
w = 331\mathrm{m / s}
\]
\[
T = 273\mathrm{K},
\]
\[
R = 8.31\mathrm{J / mol}\cdot \mathrm{K},
\]
\[
M = 0.029\mathrm{kg / mol},
\]

we get  

\[
\gamma = \frac{Mw^2}{RT}
\]
\[
= \frac{(0.029\mathrm{kg / mol})(331\mathrm{m / s})^2}{(8.31\mathrm{J / mol}\cdot\mathrm{K})(273\mathrm{K})}
\]
\[
= 1.40.
\]

The speed of a sound wave in a gas can be measured roughly by means of Kundt's tube. The gas is admitted to a horizontal cylinder tube, closed at one end and supplied at the other end with a movable piston capable of being set in vibration parallel to the axis of the tube. In the tube is a small amount of light powder. For a given frequency, a position of the piston can be found at which standing waves are set up. Under these conditions, small heaps of powder pile up at the nodes. The distance between any two adjacent nodes is one- half a wavelength, and the speed of the waves is the product of the frequency and the wavelength. Values of \(\gamma\) obtained by this mechanical method are in good agreement with those obtained from measurements of heat capacity.  

Much greater accuracy is achieved by replacing Kundt's tube with an acoustic interferometer, at one end of which is a source of waves such as a piezoelectric crystal and at the other end a receiver. When the distance between source and receiver is kept constant and the frequency varied, the various resonances corresponding to different numbers of antinodes are noted. The frequency of the compressional waves can be varied from audible to ultrasonic frequency, but corrections for errors due to viscosity, heat conduction, and boundary layer absorption must be applied.  

Equation (5.17) can be used to determine the molar gas constant \(R\) by plotting the square of the speed of sound as a function of pressure. Then, in

===== Page 148 =====

126 PART I: Fundamental Concepts  

the limit of zero pressure, which assures ideal- gas conditions, Eq. (5.17) becomes  

\[
R = \frac{Mw_0^2}{\gamma T}, \quad (5.18)
\]

where \(w_0^2\) is the extrapolation of the square of the speed of sound to zero pressure. In 1984, A. R. Colclough and colleagues at the National Physical Laboratory in England used an acoustic interferometer operating at the only defined temperature, namely, the triple point of water at \(273.16 \mathrm{~K}\) , to determine \(w_0^2\) for argon, a monatomic gas for which \(\gamma = \frac{5}{3}\) . The Committee on Data for Science and Technology used the value of \(w_0^2 = 94,756.75 \mathrm{~m}^2 / \mathrm{s}^2\) to calculate a new value of the molar gas constant \(R\) in its 1986 table of fundamental physical constants, namely, \(R\) equals \(8.314510 \mathrm{~J} / \mathrm{mol} \cdot \mathrm{K}\) , with an uncertainty of \(8.4\) parts per million. All the earlier data, including the 1973 recommendation based on Batuecas' measurement of \(R\) based on Eq. (5.3), were excluded in the determination of the latest value of the molar gas constant. Systematic errors were introduced by the presence of water adsorbed on the surface of the gas container, which could not be accounted for in an error analysis.  

## 5.8 THE MICROSCOPIC POINT OF VIEW  

We have emphasized that the point of view of classical thermodynamics is entirely macroscopic. Systems are described with the aid of their gross, or large- scale, properties. The first law of thermodynamics is a relation among the fundamental physical quantities of work, internal energy, and heat. When the first law is applied to a class of systems, a general relation is obtained which holds for any member of the class but which contains no quantities or properties of a particular system that would distinguish it from another. For example, Eq. (4.13),  

\[
C_V = \left(\frac{\partial U}{\partial T}\right)_V,
\]

is true for all hydrostatic systems, whether solid, liquid, or gas. It enables one to calculate \(C_V\) of a hydrostatic system, provided that one knows the internal energy as a function of \(T\) and \(V\) . The heat transferred during an isochoric process, Eq. (4.16), which is  

\[
Q_V = \int_{T_i}^{T_f} C_V dT,
\]

may be calculated once the \(C_V\) of the particular system under consideration is known as a function of \(T\) . But there is nothing in classical thermodynamics that provides detailed information concerning \(U\) or \(C_V\) .

===== Page 149 =====

 Another example of the limitation of classical thermodynamics is its inability to provide the equation of state of any desired system. To make use of any thermodynamic equation involving \(P, V, T\) , and the derivatives \((\partial P / \partial V)_{T}\) , \((\partial V / \partial T)_{P}\) , and \((\partial T / \partial P)_{V}\) , one must have an equation of state. Experimental values are very often useful, but there are occasions when it is not feasible to perform the necessary experiments. If an experiment is performed on, let us say, oxygen, the numerical constants in the equation of state of oxygen only are obtained, and no clue is at hand concerning the values of the constants for any other gas.  

To obtain detailed information concerning the thermodynamic coordinates and thermal properties of systems without having to resort to experimental measurements, we require calculations based on the properties and behavior of the particles of the system. There are two such microscopic theories: one is called kinetic theory, and the other is statistical mechanics. Both theories deal with particles, their internal and external motion, their collisions with one another and with any existing walls, and their forces of interaction. Making use of the laws of mechanics and statistics, kinetic theory concerns itself with the average motion of atoms and their collisions with walls and other objects in order to calculate the equation of state for the ideal gas. Statistical mechanics avoids the mechanical aspects of particles and deals with the energy aspects of aggregates or ensembles of particles. It relies heavily on statistics and quantum mechanics. Only equilibrium states can be handled — but in a uniform, straightforward manner, so that once the energy levels of the atom or of systems of atoms are understood, a program of calculations yields the equation of state, the energy, and other thermodynamic functions as well.  

In this chapter, we shall limit ourselves to a small part of the kinetic theory of the ideal gas. Statistical mechanics will be presented in Chap. 12.  

### 5.9 KINETIC THEORY OF THE IDEAL GAS  

The kinetic theory of gases was the result of the early nineteenth century work of Avogadro and Loschmidt, who calculated the number of atoms or molecules in a molar volume of a gas. In unpublished work, Waterston recognized that temperature is a function of the motion of the particles of a gas, but Krönig is commonly recognized as the originator of the kinetic theory of gases in 1856. In order to formulate a microscopic theory of gases, which will be limited to monatomic gases, several simplifying assumptions about the behavior of atoms of the ideal gas are made:  

1. Any small sample of gas consists of an enormous number of particles \(N\) . For any one chemical species, all atoms are identical and inert. If \(m\) is the mass of each atom, then the total mass is \(mN\) . If \(M\) denotes the molar mass

===== Page 150 =====

128 PART I: Fundamental Concepts  

in kilograms per mole (formerly called the atomic or molecular weight), then the number of moles \(n\) is given by  

\[
n = \frac{mN}{M}.
\]

The number of particles per mole of gas is called Avogadro's number \(N_{\mathrm{A}}\) where  

\[
N_{\mathrm{A}} = \frac{N}{n} = \frac{M}{m} = 6.0221\times 10^{23}\frac{\mathrm{particles}}{\mathrm{mole}}.
\]

Since a mole of ideal gas at the freezing point of water and at standard atmospheric pressure occupies a volume of \(22.4\times 10^{3}\mathrm{cm}^{3}\) , there are approximately \(3\times 10^{19}\) atoms in a volume of only \(1\mathrm{cm}^{3}\) \(3\times 10^{16}\) atoms per cubic millimeter, and even a volume as small as a cubic micrometer contains as many as \(3\times 10^{7}\) atoms.  

2. The atoms of an ideal gas are supposed to resemble small hard spheres that are in perpetual random motion. Within the temperature and pressure range of an ideal gas, the average distance between neighboring atoms is large compared with the size of an atom. The diameter of an atom is of the order of 2 or \(3\times 10^{-10}\mathrm{m}\) . Under standard conditions, the average distance between atoms is about 50 times their diameter.  

3. The atoms of an ideal gas are assumed to exert no forces of attraction or repulsion on other atoms except when they collide with one another and with a wall. Between collisions, they therefore move with uniform rectilinear motion.  

4. The portion of a wall with which an atom collides is considered to be smooth, and the collision is assumed to be perfectly elastic. If \(w\) is the speed of an atom approaching a wall, only the perpendicular component of velocity \(w_{\perp}\) is changed upon collision with the wall, from \(w_{\perp}\) to \(-w_{\perp}\) , or a total change of \(-2w_{\perp}\) .  

5. When there is no external field of force, the atoms are distributed uniformly throughout a container. The number density \(N / V\) is assumed constant, so that in any small element of volume \(dV\) there are \(dN\) atoms, where  

\[
dN = \frac{N}{V} dV.
\]

The infinitesimal \(dV\) must satisfy the same conditions in kinetic theory as in thermodynamics, namely, that it is small compared with \(V\) but large enough to make \(dN\) a large number. If, for example, a volume of \(1\mathrm{cm}^{3}\) contains \(10^{19}\) atoms, then one- millionth of a cubic centimeter would still contain \(10^{13}\) atoms and would qualify as a differential volume element.  

6. There is no preferred direction for the velocity of any atom, so that at any moment there are as many atoms moving in one direction as in another.  

7. Not all atoms have the same speed. A few atoms at any moment move slowly and a few move very rapidly, so that speeds may be considered to cover the

===== Page 151 =====

 range from zero to the speed of light. Since most atomic speeds are so far below the speed of light, no error is introduced in integrating the speed from 0 to \(\infty\) . If \(dN_{w}\) represents the number of atoms with speeds between \(w\) and \(w + dw\) , it is assumed that \(dN_{w}\) remains constant at equilibrium, even though the atoms are perpetually colliding and changing their speeds.  

Since the velocity vectors of the atoms of gas have no preferred direction, consider an arbitrary velocity vector \(w\) directed from the point \(O\) in Fig. 5- 9 to the elementary area \(dA^{\prime}\) . It is important to know how many atoms have velocity vectors in the neighborhood of \(w\) . The calculation of this quantity involves the concept of a solid angle. Taking \(O\) as the origin of polar coordinates \(r\) , \(\theta\) , and \(\phi\) , we construct a sphere of radius \(r\) . The area \(dA^{\prime}\) on the surface of this sphere, formed by two circles of latitude differing by \(d\theta\) and two circles of longitude differing by \(d\phi\) , has the magnitude  

\[
dA^{\prime} = (r d\theta)(r \sin \theta d\phi).
\]

The solid angle \(d\Omega\) , formed by lines radiating from \(O\) and touching the edge of \(dA^{\prime}\) , is by definition  

\[
d\Omega = \frac{dA^{\prime}}{r^{2}} = \frac{(r d\theta)(r \sin \theta d\phi)}{r^{2}}.
\]

or  

\[
d\Omega = \sin \theta d\theta d\phi . \quad (5.19)
\]

FIGURE 5-9 The solid angle \(d\Omega = \sin \theta d\theta d\phi\) .
===== Page 162 =====
6.1 CONVERSION OF WORK INTO HEAT AND VICE VERSA  
When two stones are rubbed together under water, the work done against the force of friction is transformed into internal energy tending to produce a rise of temperature of the stones. As soon as the temperature of the stones rises above that of the surrounding water, however, there is heating of the water. If the mass of water is large enough, then there will be no appreciable rise of temperature, and the water can be regarded as a heat reservoir, as discussed in Sec. 4.10. Since the state of the stones is the same at the end of the process as at the beginning, the net result of the process is merely the conversion of mechanical work into heat. Similarly, when an electric current is maintained in a resistor immersed either in running water or in a very large mass of water, there is also a conversion of electrical work into heat, without any change in the thermodynamic coordinates of the wire. In general, work of any kind \(W\) may be done on a system in contact with a reservoir, causing heat \(Q\) to leave the system without altering the state of the system. The system acts merely as an intermediary. It is apparent from the first law that the work is equal to the heat, \(W = Q\) ; in other words, the transformation of work into heat is accomplished with 100 percent efficiency. Moreover, this transformation can be continued indefinitely.  
To study the opposite process, namely, the conversion of heat into work, we must also have at hand a process, or series of processes, by means of which such a conversion may continue indefinitely without involving any resulting changes in the state of the system. At first thought, it might appear that the isothermal expansion of an ideal gas might be a suitable process to consider in discussing the conversion of heat into work. In this case, there is no change of internal energy, since the temperature remains constant, and, therefore,
===== Page 163 =====
 \(Q = W\) , or heat has been converted completely into work. This process, however, involves a change of state of the gas. The volume increases and the pressure decreases until atmospheric pressure is reached, at which point the process stops. Therefore, the process of isothermal expansion cannot be used indefinitely.  
What is needed is a series of processes in which a system is brought back to its initial state, that is, a cycle. Each of the processes that constitute a cycle involves either the performance of work or a flow of heat between the system and its surroundings, which consist of a heat reservoir at a higher temperature than the system (a "high- temperature reservoir") and a heat reservoir at a lower temperature than the system (a "low- temperature reservoir"). For one complete cycle, let  
the symbol \(|Q_{H}|\) represent the heat exchanged between the high- temperature reservoir and the system; the symbol \(|Q_{L}|\) represent the heat exchanged between the low- temperature reservoir and the system; and the symbol \(|W|\) represent the work exchanged between the system and the surroundings.  
All three quantities \(|Q_{H}|\) , \(|Q_{L}|\) , and \(|W|\) , are expressed as absolute values, that is, positive numbers only. In all chapters of this book, except this chapter and the next one, the symbols \(Q\) and \(W\) are algebraic quantities that may take on positive or negative values. In these two chapters, we shall deal with engines and refrigerators, so we shall know at all times the direction of flow of \(Q\) and \(W\) and we are interested only in the absolute values of \(Q\) and \(W\) .  
If \(|Q_{H}|\) is larger than \(|Q_{L}|\) and if \(|W|\) is done by the system, then the machine that causes the system to undergo the cycle is called a heat engine. The purpose of a heat engine is to deliver work continuously to the surroundings by performing the same cycle over and over again. The net work in the cycle is the output, and the heat absorbed from the high- temperature reservoir by the system is the input. The thermal efficiency of the engine, symbolized by \(\eta\) (Greek letter eta), is defined as  
\[
\text{Thermal efficiency} = \frac{\text{work output}}{\text{heat input}},
\]
\[
\eta = \frac{|W|}{|Q_{H}|}, \quad (6.1)
\]
where \(|W|\) and \(|Q_{H}|\) are measured in joules. Applying the first law to one complete cycle, remembering that there is no change of internal energy, we get  
\[
|Q_{H}| - |Q_{L}| = |W|,
\]
and, therefore,  
\[
\eta = \frac{|Q_{H}| - |Q_{L}|}{|Q_{H}|},
\]
===== Page 164 =====
142 PART I: Fundamental Concepts  
\[
\eta = 1 - \frac{|Q_L|}{|Q_H|}. \quad (6.2)
\]
It is seen from this equation that \(\eta\) will be unity (efficiency 100 percent) if \(Q_{L}\) is zero. In other words, if an engine could be built to operate in a cycle in which there is no outflow of heat from the working substance to the low- temperature reservoir, then there would be 100 percent conversion of heat from the high- temperature reservoir into work. But, as we shall see in Sec. 6.6, there must always be an outflow of heat from an engine, so the efficiency of a heat engine is always less than 100 percent.  
The transformation of heat into work is usually accomplished, in practice, by two general types of heat engine: the internal- combustion engine, such as the gasoline engine and the diesel engine; and the external- combustion engine, such as the steam engine and the Stirling engine. In both types of heat engine, a gas or a mixture of gases is contained in the space between a cylinder, closed at one end, and a piston. The gas in the confined space is the system, which undergoes a cycle, thereby causing a reciprocating piston to impart a motion of rotation to a shaft, which acts against an opposing force. It is necessary, in all engines, that the gas in the confined space, at some time in the cycle, be raised to a high temperature and a high pressure, the pressure providing the force that performs external work. In the gasoline and diesel engines, the rapid burning of the fuel and oxygen from the air takes place in the confined space called the combustion chamber, thereby raising the temperature and pressure of the system. In the steam and Stirling engines, the increase in temperature and pressure of the gas is accomplished by high- temperature surroundings that transfer heat to the system inside the chamber.  
### 6.2 THE GASOLINE ENGINE  
In the gasoline engine, the cycle involves the performance of six processes, four of which require vertical motion of the piston and are called strokes:  
1. Intake stroke. The system is a mixture of gasoline vapor and air, which moves into the cylinder due to suction as the receding piston enlarges the accessible volume. The outside pressure is greater than the pressure in the cylinder, so the mixture is pushed into the combustion chamber.  
2. Compression stroke. The mixture of gasoline vapor and air is compressed until its pressure and temperature rise considerably. This is accomplished by the advancing piston, which decreases the volume of the combustion chamber.  
3. Combustion. Burning of the hot mixture occurs very rapidly after ignition by an electric spark. The resulting combustion products attain a very high pressure and temperature, but the volume remains unchanged during this
===== Page 165 =====
4. Power stroke. The hot combustion products expand and push the piston away, thus increasing the volume and decreasing the pressure and temperature. The system, acting through the piston, performs work on the surroundings (crankshaft, transmission, etc.).  
5. Exhaust. The combustion products at the end of the power stroke are still at a higher pressure and temperature than the surroundings. An exhaust valve allows some gas to escape until the pressure drops almost to atmospheric pressure. The piston remains essentially motionless during this process.  
6. Exhaust stroke. The piston pushes almost all the remaining combustion products out of the cylinder by exerting a pressure significantly larger than atmospheric pressure.  
In the above processes, there are several phenomena that render an exact mathematical analysis quite difficult. Among these are friction, turbulence, loss of heat by conduction, and the chemical reaction between gasoline vapor and oxygen. A drastic but useful simplification is provided by neglecting these troublesome effects. When this is done, we have an idealized gasoline engine that performs a cycle known as an Otto cycle. The cycle is named after the German engineer Nikolaus Otto for his invention in 1876, but the idea for a four- stroke engine came from the Frenchman Alphonse Beau de Rochas in 1862.  
The behavior of a gasoline engine can be approximated by assuming a set of ideal conditions as follows: (1) the working substance is at all times air, which behaves like an ideal gas with constant heat capacities; (2) all processes are quasi- static; (3) there is no friction or turbulence; (4) there is no loss of heat through the walls of the combustion chamber; and (5) the processes are reversible. These assumptions then lead to the idealized air- standard Otto cycle, which is composed of six simple processes of an ideal gas; these processes are plotted on a \(PV\) diagram in Fig. 6- 1 and described below.  
Process \(5 \rightarrow 1\) represents a quasi- static intake stroke, isobaric at atmospheric pressure. The volume of the combustion chamber varies from zero to \(V_{1}\) as the number of moles varies from zero to \(n\) , according to the equation  
\[
P_{0}V = nRT_{1},
\]
where \(P_{0}\) is atmospheric pressure and \(T_{1}\) is the temperature of the outside air.  
Process \(1 \rightarrow 2\) represents a quasi- static, adiabatic compression stroke. There is no friction, and no loss of heat through the cylinder wall. The temperature rises from the ambient \(T_{1}\) to \(T_{2}\) , according to the equation  
\[
T_{1}V_{1}^{\gamma -1} = T_{2}V_{2}^{\gamma -1},
\]
===== Page 166 =====
144 PART I: Fundamental Concepts  
FIGURE 6-1 Idealized Otto cycle for gasoline engines shown on a PV diagram.  
where \(V_{1}\) is the larger volume when the piston is at the bottom of the compression stroke and \(V_{2}\) the smaller volume when the piston is at the top. The ratio of heat capacities is assumed to be constant.  
Process \(2 \rightarrow 3\) represents a quasi- static isochoric increase of temperature and pressure of \(n\) moles of air, imagined to be brought about by an absorption of heat \(|Q_{H}|\) from a series of external high- temperature reservoirs whose temperatures range from \(T_{2}\) to \(T_{3}\) . If there were only one reservoir at the temperature \(T_{3}\) , then the flow of heat would not be quasi- static, because there would be a substantial difference in temperature between the system and the single reservoir at \(T_{3}\) . This process is meant to approximate the effect of the combustion in a gasoline engine when the piston is essentially motionless at the top of the stroke.  
Process \(3 \rightarrow 4\) represents a quasi- static adiabatic power stroke, involving a drop in temperature from \(T_{3}\) to \(T_{4}\) , according to the equation  
\[
T_{3}V_{2}^{\gamma -1} = T_{4}V_{1}^{\gamma -1},
\]
where \(V_{1}\) is larger than \(V_{2}\) . This process represents the power stroke.  
Process \(4 \rightarrow 1\) represents a quasi- static isochoric drop in temperature and pressure of \(n\) moles of air, brought about by a rejection of heat \(|Q_{L}|\) to a series of low- temperature external reservoirs ranging in temperature from \(T_{4}\) to \(T_{1}\) , where \(T_{1}\) is the temperature of the outside air. This process is meant to approximate the drop to atmospheric pressure upon opening the exhaust valve, but, in reality, the temperature does not actually drop to the temperature of the outside air as it leaves the exhaust port.  
Process \(1 \rightarrow 5\) represents a quasi- static exhaust stroke, isobaric at atmospheric pressure. The volume varies from \(V_{1}\) to zero as the number of moles of exhaust gas varies from \(n\) to zero, the temperature remaining constant at the value \(T_{1}\) .
===== Page 167 =====
 The two isobaric processes \(5 \rightarrow 1\) and \(1 \rightarrow 5\) obviously cancel each other and need not be considered further. Of the four remaining processes, only two involve a flow of heat. There is an absorption of \(|Q_H|\) units of heat at high temperatures from \(2 \rightarrow 3\) , and a rejection of \(|Q_L|\) units of heat at lower temperatures from \(4 \rightarrow 1\) , as indicated in Fig. 6- 1.  
Assuming \(C_V\) to be constant along the line \(2 \rightarrow 3\) , we find for heat entering the system,  
\[
|Q_H| = \int_{T_2}^{T_3} C_V dT = C_V(T_3 - T_2).
\]
Similarly, for process \(4 \rightarrow 1\) , we find for heat leaving the system,  
\[
|Q_L| = -\int_{T_4}^{T_1} C_V dT = C_V(T_4 - T_1).
\]
The thermal efficiency is, therefore,  
\[
\eta = 1 - \frac{|Q_L|}{|Q_H|} = 1 - \frac{T_4 - T_1}{T_3 - T_2}. \quad (6.3)
\]
The two adiabatic processes during the compression stroke and power stroke are given by  
\[
\begin{array}{l}{T_1V_1^{\gamma -1} = T_2V_2^{\gamma -1},}\\ {T_4V_1^{\gamma -1} = T_3V_2^{\gamma -1},} \end{array} \quad (6.4)
\]
and  
Change signs and add unity to obtain  
\[
\frac{T_4 - T_1}{T_4} = \frac{T_3 - T_2}{T_3},
\]
\[
\frac{T_4 - T_1}{T_3 - T_2} = \frac{T_4}{T_3}.
\]
or  
Combine this result with Eq. (6.4) and Eq. (6.3) to obtain the thermal efficiency \(\eta\) of an idealized gasoline engine,  
\[
\eta = 1 - \frac{T_1}{T_2}, \quad (6.5)
\]
where \(T_1\) and \(T_2\) are the temperatures at the beginning and end of the compression stroke. This is the most important expression in connection with the gasoline engine. It shows that the thermal efficiency of a gasoline engine working in the Otto cycle depends on the temperature before and after compression. In a gasoline engine with temperatures \(T_1 = 300 \mathrm{~K}\) and \(T_2 = 580 \mathrm{~K}\) , the efficiency is 48 percent.
===== Page 168 =====
146 PART I: Fundamental Concepts  
This is the optimum efficiency for a gasoline engine operating in an idealized quasi- static Otto cycle for the temperatures cited. All the troublesome effects present in an actual gasoline engine, such as friction, turbulence, and heat conduction through the engine walls, are such that they make the efficiency much lower than that of the idealized Otto cycle. The actual operating thermal efficiency of a gasoline engine is in the range of 20- 30 percent.  
### 6.3 THE DIESEL ENGINE  
In the diesel engine, only air is admitted on the intake stroke. The air is compressed adiabatically until the temperature is high enough to ignite oil that is sprayed into the cylinder after the compression. The rate of supply of oil is adjusted so that combustion takes place approximately isobarically, the piston moving out during combustion. The rest of the cycle, namely, power stroke, exhaust, and exhaust stroke, is exactly the same as in the gasoline engine. The usual troublesome effects take place in the diesel engine as in the gasoline engine. Eliminating these effects by making the same assumptions as before, we are left with an idealized diesel engine that performs a cycle known as the air- standard Diesel cycle, named after Rudolf Diesel who constructed the first successful diesel engine using liquid fuel in 1897. If the line \(2 \rightarrow 3\) in Fig. 6- 1 is imagined horizontal instead of vertical, the resulting cycle is shown in Fig. 6- 2.  
The line \(2 \rightarrow 3\) in Fig. 6- 2 represents the quasi- static isobaric absorption of heat from a series of external reservoirs ranging in temperature from \(T_{2}\) to \(T_{3}\) . This process is meant to approximate the isobaric burning of the oil. All the other curves have the same meaning as in the case of the air- standard Otto cycle.  
Assuming \(C_{P}\) to be constant along the line \(2 \rightarrow 3\) , we get  
\[
|Q_{H}| = \int_{T_{2}}^{T_{3}}C_{P}dT = C_{P}(T_{3} - T_{2}),
\]
and, as in the case of the Otto cycle,  
\[
|Q_{L}| = C_{V}(T_{4} - T_{1}).
\]
Therefore, the thermal efficiency of an idealized diesel engine is given by  
\[
\eta = 1 - \frac{1}{\gamma}\frac{(T_{4} - T_{1})}{(T_{3} - T_{2})}.
\]
Notice that, unlike the thermal efficiency of the Otto cycle expressed in Eq. (6- 3), the efficiency of the Diesel cycle depends upon \(\gamma\) , the ratio of heat capacities. This expression may be transformed into
===== Page 169 =====
 FIGURE 6- 2 Idealized Diesel cycle for oil- fired engines shown on a \(PV\) diagram.  
\[
\eta = 1 - \frac{1}{\gamma}\frac{(r_{E}^{T} - 1)}{(r_{E} - 1)}\frac{T_{1}}{T_{2}}, \quad (6.6)
\]
where the expansion ratio \(r_{E}\) (also called the "cutoff ratio" in engineering) is given by  
\[
r_{E} = \frac{V_{1}}{V_{3}}
\]
and \(T_{1}\) and \(T_{2}\) are the temperatures at the beginning and end of the compression stroke, respectively. Interestingly, the efficiency of the Diesel cycle expressed in Eq. (6.6) does not depend on the compression ratio \(r_{C}\) given by  
\[
r_{C} = \frac{V_{1}}{V_{2}}.
\]
Taking, for example, \(r_{E} = 5\) , \(\gamma = 1.4\) , \(T_{1} = 300 \mathrm{~K}\) , and \(T_{2} = 990 \mathrm{~K}\) , we obtain  
\[
\eta = 1 - \frac{(5^{1.4} - 1)}{(1.4)(5 - 1)}\frac{300 \mathrm{~K}}{990 \mathrm{~K}}
\]
\[
= 54 \mathrm{~percent}.
\]
The thermal efficiencies of actual diesel engines are, of course, lower, for the reasons mentioned in connection with the gasoline engine, typically being in the range of 30- 35 percent.  
In the diesel engine just considered, four strokes of the piston are needed for the completion of a cycle, and only one of the four is a power stroke. Since only air is compressed in the diesel engine, it is possible to eliminate the exhaust and intake strokes and thus complete the cycle in two strokes. In the two- stroke- cycle diesel engine, every other stroke is a power stroke, and
===== Page 170 =====
148 PART I: Fundamental Concepts  
thus the power is doubled. The principle is very simple: At the conclusion of the power stroke, when the cylinder is full of combustion products, the valve opens, exhaust takes place until the combustion products are at atmospheric pressure, and, then, instead of using the piston itself to exhaust the remaining gases, fresh air is blown into the cylinder, replacing the combustion products. A blower, operated by the engine itself, is used for this purpose, and thus it accomplishes in one simple operation what formerly required two separate piston strokes.  
### 6.4 THE STEAM ENGINE  
The steam engine is historically quite important, because it was the first engine driven by heat, rather than animals, water, or wind. The initial function of the steam engine was to pump water out of mines in England. The first practical and safe steam engine, a reciprocating piston- cylinder device, was invented by Thomas Newcomen in 1712 and had the greatest impact in bringing about the Industrial Revolution. James Watt greatly improved the steam engine in 1764, and William Rankine was the first to describe the thermodynamic cycle for adiabatic steam engines in 1859. Currently, steam engines are used in electric power plants, and in nuclear- powered aircraft carriers and submarines.  
A schematic diagram of an elementary steam engine is shown in Fig. 6- 3(a). The operation of such an engine can be understood by following the pressure and volume changes of a small constant mass of water as it is conveyed from the condenser, through the boiler, into the expansion chamber, and back to the condenser. The water in the condenser is at a pressure less than atmospheric and at a temperature less than the normal boiling point. By means of a pump, it is introduced into the boiler, which is at a much higher pressure and temperature. In the boiler, the water is first heated to its boiling point and then vaporized, both processes taking place approximately at constant high pressure. The steam is then raised to a temperature greater than the normal boiling point at the same pressure. It is then allowed to flow into a cylinder, where it expands approximately adiabatically against a piston or a set of turbine blades, until its pressure and temperature drop to that of the condenser. In the condenser, finally, the steam condenses into the water at the same temperature and pressure as at the beginning, and the cycle is complete.  
In the actual operation of the steam engine, there are several processes that render an exact analysis difficult: turbulence caused by the pressure difference required to cause the flow of the steam from one part of the apparatus to another, friction, conduction of heat through the walls during expansion of the steam, and heat transfers due to a finite temperature difference between the furnace and the boiler.  
A first approximation to the discussion of the steam engine may be made by introducing some simplifying assumptions which, although in no way realizable in practice, provide at least an upper limit to the efficiency of such a
===== Page 171 =====
 FIGURE 6- 3(a) Schematic diagram of a simple steam engine.  
FIGURE 6- 3(b) PV diagram of the Rankine cycle for a steam engine. Process \(1 \rightarrow 2\) is not an isochoric compression of steam, but an adiabatic compression of water, which yields a nearly vertical line. Process \(3 \rightarrow 4\) is an adiabatic expansion of steam. For more detail, see Fig. 7- 2.
===== Page 172 =====
150 PART I: Fundamental Concepts  
plant and which define an idealized cycle, called the Rankine cycle, in terms of which the actual behavior of a steam plant may be discussed.  
In the Rankine cycle, all processes are assumed to be well behaved; complications that arise from turbulence, friction, and heat losses are thus eliminated. Starting at point 1 in Fig. 6- 3(b), we have liquid water at the temperature and pressure of the condenser. The Rankine cycle consists of the following four processes:  
\(1\rightarrow 2\) Adiabatic compression of water to the pressure of the boiler (only very small changes of temperature and volume of the liquid take place during this process). \(2\rightarrow 3\) Isobaric heating of water to the boiling point, vaporization of water into saturated steam, and superheating of steam to a temperature \(T_{H}\) higher than the boiling point. \(3\rightarrow 4\) Adiabatic expansion of superheated steam into wet steam. \(4\rightarrow 1\) Isobaric, isothermal condensation of steam into saturated water at the temperature \(T_{L}\) .  
During the process \(2\rightarrow 3\) , heat \(|Q_{H}|\) enters the system from a hot reservoir; whereas during the condensation process \(4\rightarrow 1\) , heat \(|Q_{L}|\) is rejected by the system to the atmosphere, a reservoir at \(T_{L}\) . This condensation process must exist in order to bring the system back to its initial state 1. Since heat is always rejected during the condensation of water, \(|Q_{L}|\) cannot be made equal to zero, and, therefore, the input \(|Q_{H}|\) cannot be converted completely into work. So the efficiency of the idealized steam engine is always less than 100 percent. The efficiency of historic steam locomotives was quite low, which led to the development of diesel- electric locomotives. However, the actual operating thermal efficiency of a steam power plant is in the range 30- 40 percent.  
### 6.5 THE STIRLING ENGINE  
In 1816, due to explosions of steam engines and loss of life, a minister of the Church of Scotland, named Robert Stirling, designed and patented a hot- air engine that could convert some of the energy liberated by a burning fuel into work. The Stirling engine remained useful and popular for many years in applications needing only a few horsepower, but, with the development of small internal- combustion engines, fell into disuse.  
The steps in the operation of an idealized Stirling engine are shown schematically in Fig. 6- 4(a). Two pistons, an expansion piston on the left and a compression piston on the right, are connected to the same shaft. As the shaft rotates, these pistons move out of phase, with the aid of suitable connecting linkages. The space between the two pistons is filled with a fixed amount of gas, usually hydrogen or helium, which is recycled from one cylinder to the other. The left- hand portion of the space is kept in contact with a high- tem
===== Page 173 =====
151  
FIGURE 6-4(a) Schematic diagram of the steps in the operation of an idealized Stirling engine. The numbers under each diagram refer to the processes shown in Fig. 6-4(b).  
FIGURE 6-4(b)  
PV diagram for a Stirling engine showing the heats exchanged between the system and the surroundings during the isothermal processes. During the isochoric processes, there are heats exchanged between the internal regenerator and the system, but these are not shown.  
perature reservoir (burning fuel), while the right- hand portion is in contact with a low- temperature reservoir (atmosphere). Between the two cylinders is a device \(R\) , called a regenerator, consisting of a packing of fine wire screens to form a kind of metal sponge. The regenerator serves as an internal reservoir, which exchanges heat with the gas as it passes back and forth through the regenerator.  
The Stirling cycle consists of four processes involving pressure and volume changes, plotted (as though ideal conditions existed) on the PV diagram of Fig. 6- 4(b). During process \(1 \rightarrow 2\) , the left piston remains at the top of the
===== Page 174 =====
152 PART I: Fundamental Concepts  
cylinder. Meanwhile, the right piston moves halfway up its cylinder, compressing low- temperature gas that is in contact with the low- temperature reservoir and, therefore, causing heat \(|Q_{L}|\) to leave. This is an approximately isothermal compression and is depicted as a rigorously isothermal process at the temperature \(T_{L}\) .  
For process \(2 \rightarrow 3\) , the left piston moves down and the right piston up, so that there is no change in volume occupied by the gas. However, gas is forced through the regenerator from the low- temperature side to the high- temperature side and enters the left- hand side at the higher temperature \(T_{H}\) . To raise the temperature of the gas, the regenerator supplies heat \(|Q_{R}|\) to the gas. Note that the process \(2 \rightarrow 3\) in Fig. 6- 4(b) is at constant volume.  
In process \(3 \rightarrow 4\) , the right piston remains stationary. The left piston continues moving down while in contact with the high- temperature reservoir, which causes the gas to expand approximately isothermally. Additional heat \(|Q_{H}|\) is absorbed from the outside at the temperature \(T_{H}\) .  
During process \(4 \rightarrow 1\) , both pistons move in opposite directions, thereby forcing gas through the regenerator from the high- temperature to the low- temperature side and giving up approximately the same amount of heat \(|Q_{R}|\) to the regenerator that is absorbed in the process \(2 \rightarrow 3\) , so the regenerator heats cancel each other during one cycle. This process takes place at practically constant volume.  
The net result of the Stirling cycle is the absorption of heat \(|Q_{H}|\) at the high temperature \(T_{H}\) , the rejection of heat \(|Q_{L}|\) at the low temperature \(T_{L}\) , and the delivery of work \(|W| = |Q_{H}| - |Q_{L}|\) to the surroundings, with no net heat transfer resulting from the two constant- volume processes. It must be emphasized that Fig. 6- 4(b) is based on the assumptions that the gas is ideal, no leakage of gas takes place, no heat is lost or gained through cylinder walls, no heat is conducted from the regenerator to the surroundings, and there is no friction. Even if these idealizations could be realized, in practice, there would still be some heat \(|Q_{L}|\) rejected at the lower temperature, and, therefore, all the input \(|Q_{H}|\) could not be converted into work, rendering the efficiency less than 100 percent. The actual operating thermal efficiency of Stirling engines is in the range of 35- 45 percent.  
The Stirling engine has some unique advantages compared with other heat engines. The engine can use any heat source, from heating due to radioactivity to combustion of biomass waste products. Using open- air combustion, the engine does not produce toxic exhaust. Furthermore, it operates quietly. The Stirling engine can be used in automobiles, but internal- combustion engines are already quite good for this application. An interesting application is an implantable Stirling engine for artificial heart power, which is being developed at the Joint Center for Graduate Study, University of Washington.  
A modification to the Stirling engine, called a Ringbom Stirling engine after its inventor Ossian Ringbom, uses only one reciprocating piston instead of two pistons. The regenerator or displacer oscillates between the closed end of the cylinder and the piston. As a result, the Ringbom Stirling engine is strikingly simpler than all the Stirling engines that had preceded it.
===== Page 175 =====
6.6 HEAT ENGINE; KELVIN- PLANCK STATEMENT OF THE SECOND LAW  
In the preceding sections, four different heat engines have been briefly described. There are, of course, more types of heat engines and a tremendous number of structural details, methods of increasing thermal efficiency, mathematical analyses, etc., which constitute the subject matter of engineering thermodynamics. Thermodynamics owes its origin to the project of converting heat into work and of developing the theory of operation of machines for this purpose. Therefore, it is fitting that one of the fundamental laws of thermodynamics is based upon the operation of heat engines. Reduced to its simplest terms, the important characteristics of heat- engine cycles may be summed up as follows:  
1. There is some process or series of processes during which there is an absorption of heat from an external reservoir at a higher temperature. 
2. There is some process or series of processes during which heat is rejected to an external reservoir at a lower temperature.  
This is represented schematically in Fig. 6- 5. It is a fact of experience that no heat- engine has ever been developed that converts the heat extracted from a reservoir at a higher temperature into work without rejecting some heat to a reservoir at a lower temperature. This negative statement, which is the result of everyday experience, constitutes the second law of thermodynamics and has been formulated in several ways. The original statement of William Thomson (Kelvin) is, "It is impossible by means of inanimate material agency to derive mechanical effect from any portion of matter by cooling it below the temperature of the coldest of the surrounding objects." In the words of Max Planck, originator of quantum mechanics, "It is impossible to construct an engine which, working in a complete cycle, will produce no effect other than the raising of a weight and the cooling of a heat reservoir." We may combine these statements into one equivalent statement, to which we shall refer hereafter as the Kelvin- Planck statement of the second law, thus:  
It is impossible to construct an engine that, operating in a cycle, will produce no effect other than the extraction of heat from a reservoir and the performance of an equivalent amount of work.  
If the second law were not true, it would be possible to propel a ship across the ocean by extracting heat from the ocean or to run a power plant by extracting heat from the surrounding air. Notice that neither of these "impossibilities" violates the first law of thermodynamics. After all, both the ocean and the surrounding air contain an enormous store of internal energy, part of which you might hope could be extracted in the form of a flow of heat. There is nothing in the first law to preclude the possibility of converting this heat
===== Page 176 =====
154 PART I: Fundamental Concepts  
FIGURE 6-5 Schematic representation of the generalized heat engine.  
completely into work. The second law, therefore, is not a deduction from the first law, but stands by itself as a separate law of nature, referring to an aspect of nature different from that described by the first law. The first law denies the possibility of creating or destroying energy; the second law denies the possibility of utilizing energy in a particular way. The continuous operation of a machine that creates its own energy and thus violates the first law is called a perpetual motion machine of the first kind. The operation of a machine that utilizes the internal energy of only one heat reservoir, thus violating the second law, is called a perpetual motion machine of the second kind.  
### 6.7 REFRIGERATOR; CLAUSIUS' STATEMENT OF THE SECOND LAW  
We have seen that a heat engine is a machine that takes a working substance through a cycle in such a sequence of processes that some heat is absorbed by the system from a high- temperature heat reservoir, a smaller amount of heat is rejected to a low- temperature heat reservoir, and a net amount of work is done by the system on the surroundings. If we imagine a cycle performed in a sequence of processes opposite to that of an engine, then some heat is absorbed by the system from a heat reservoir at a low temperature, a larger amount of heat is rejected to a heat reservoir at a high temperature, and a net amount of work is done on the system by the surroundings. A machine that performs a cycle in this direction is called a refrigerator, and the working substance (system) is called a refrigerant. Refrigerators used for climate control are the air- conditioner and the heat pump. Figure 6- 6 represents a schematic diagram of a refrigerator.  
Let the following notation (all positive quantities) refer to one complete cycle:
===== Page 177 =====
\(|Q_H|\) represents the amount of heat rejected by the refrigerant to the high- temperature reservoir;  
\(|Q_L|\) represents the amount of heat absorbed by the refrigerant from the low- temperature reservoir; and  
\(|W|\) represents the net work done on the refrigerant by the surroundings.  
Since the refrigerant undergoes a cycle, there is no change in internal energy, and the first law becomes  
\[|Q_L| - |Q_H| = |W|,\]  
or  
\[|Q_H| = |Q_L| + |W|.\]  
That is, the heat rejected to the high- temperature reservoir is larger than the heat extracted from the low- temperature reservoir by the amount of work done on the refrigerant.  
The purpose of a refrigerator is to extract as much heat \(|Q_L|\) as possible from the low- temperature reservoir with the expenditure of as little work \(|W|\) as possible. Work is always necessary to transfer heat from a lower- temperature reservoir to a higher- temperature reservoir, because it is a fact of nature that heat does not flow spontaneously from a lower- temperature reservoir to a higher- temperature reservoir. This negative statement leads us to the Clausius statement of the second law:  
It is impossible to construct a refrigerator that, operating in a cycle, will produce no effect other than the transfer of heat from a lower- temperature reservoir to a higher- temperature reservoir.  
At first sight, the Kelvin- Planck and the Clausius statements appear to be quite unconnected, but we shall see immediately that they are in all respects equivalent.  
**FIGURE 6-6**  
Schematic representation of the generalized refrigerator.  
===== Page 178 =====
### 6.8 EQUIVALENCE OF THE KELVIN- PLANCK AND CLAUSIUS STATEMENTS  
Let us adopt the following notation:  
\(K =\) truth of the Kelvin- Planck statement;  
\(- K =\) falsity of the Kelvin- Planck statement;  
\(C =\) truth of the Clausius statement;  
\(- C =\) falsity of the Clausius statement.  
Two propositions or statements are said to be equivalent when the truth of one implies the truth of the second, and the truth of the second implies the truth of the first. Using the symbol \(\supset\) to mean "implies" and the symbol \(\equiv\) to denote "equivalence," we wish to prove that  
\[K\equiv C,\]  
when true statements imply each other, namely  
\[K\supset C\qquad \mathrm{and}\qquad C\supset K.\]  
Alternatively, equivalence can be proven when false statements imply each other, namely,  
\[-K\supset -C\qquad \mathrm{and} -C\supset -K.\]  
Thus, in order to demonstrate the equivalence of \(K\) and \(C\) , we use the latter strategy that the falsity of one statement implies the falsity of the second, and vice versa.  
1. To prove that \(-C\supset -K\) , consider a refrigerator, shown in the left side of Fig. 6-7, that requires no work to transfer \(|Q_L|\) units of heat from a low-temperature reservoir to a high-temperature reservoir and that, therefore, violates the Clausius statement. Suppose that a heat engine (on the right) also operates between the same two reservoirs in such a way that the same heat \(|Q_L|\) is delivered to the low-temperature reservoir. The engine, of course, does not violate any law, but the refrigerator and engine together constitute a self-contained machine that takes heat \(|Q_H| - |Q_L|\) from the high-temperature reservoir and converts all this heat into work without producing any change in the low-temperature reservoir. Therefore, the refrigerator and engine together constitute a violation of the Kelvin- Planck statement.  
2. To prove that \(-K\supset -C\) , consider an engine, shown on the left side of Fig. 6-8, that rejects no heat to the low-temperature reservoir and that, therefore, violates the Kelvin-Planck statement. Suppose that a refrigerator (on the right) also operates between the same two reservoirs and uses up all the work performed by the engine. The refrigerator violates no law, but the engine and refrigerator together constitute a self-contained machine that
===== Page 179 =====
**FIGURE 6-7** Proof that \(- C \supset - K\) . The refrigerator on the left is a violation of \(C\) ; the refrigerator and the heat engine acting together violate \(K\) .  
**FIGURE 6-8**  
Proof that \(- K \supset - C\) . The heat engine on the left is a violation of \(K\) ; the heat engine and refrigerator acting together violate \(C\) .  
transfers heat \(|Q_L|\) from the low- temperature reservoir to the high- temperature reservoir without producing any changes elsewhere. Therefore, the engine and refrigerator together constitute a violation of the Clausius statement.
===== Page 180 =====
Therefore, we arrive at the conclusion that both statements of the second law are equivalent. It is a matter of choice which one is used in a particular argument.  
### 6.9 REVERSIBILITY AND IRREVERSIBILITY  
In thermodynamics, work is a macroscopic concept. The performance of work may always be described in terms of the raising or lowering of an object or the winding or unwinding of a spring, that is, by the operation of a machine that serves to increase or decrease the potential energy of a mechanical system. Imagine, for the sake of simplicity, a suspended object coupled, by means of suitable pulleys, to a system so that any work done by or on the system can be described in terms of the raising or lowering of the object. Imagine, further, a series of reservoirs which may be put in contact with the system and in terms of which any flow of heat to or from the system may be described. We shall refer to the suspended object and the series of reservoirs as the local surroundings of the system. The local surroundings are, therefore, those parts of the surroundings which interact directly with the system. Other machines and reservoirs which are accessible and which might interact with the system constitute the auxiliary surroundings of the system or, for want of a better expression, the rest of the universe. The word "universe" is used here in a very restricted technical sense, with no cosmic or celestial implications. The universe merely means a finite portion of the world consisting of the system and those surroundings which may interact with the system.  
Now, suppose that a process occurs in which: (1) the system proceeds from an initial state \(i\) to a final state \(f\) ; (2) the suspended object is lowered to an extent that \(W\) units of work are performed on the system; and (3) a transfer of heat \(|Q|\) takes place from the system to the series of reservoirs. If, at the conclusion of this process, the system may be restored to its initial state \(i\) , the object lifted to its former level, and the reservoirs caused to part with the same amount of heat \(|Q|\) , without producing any changes in any other mechanical device or reservoir in the universe, the original process is said to be reversible. In other words, a reversible process is one that is performed in such a way that, at the conclusion of the process, both the system and the local surroundings may be restored to their initial states without producing any changes in the rest of the universe. A process that does not fulfill these stringent requirements is said to be irreversible. The importance of the phrase in bold print is that all the initial states must be recoverable.  
The question immediately arises as to whether natural processes, namely, the familiar processes of nature, are reversible or not. Since dissipation is present in all real processes, it follows that all natural processes are irreversible. By considering representative types of natural processes and examining the features that are responsible for irreversibility, we shall then be able to state the conditions necessary for a process to occur reversibly.
===== Page 181 =====
### 6.10 EXTERNAL MECHANICAL IRREVERSIBILITY  
There is a large class of processes involving the isothermal transformation of work through a system (which remains unchanged) into internal energy of a reservoir. This type of process is depicted schematically in Fig. 6- 9 and is illustrated by the following five examples:  
1. Friction from rubbing two solids in contact with a reservoir. 
2. Irregular stirring of a viscous liquid in contact with a reservoir. 
3. Inelastic deformation of a solid in contact with a reservoir. 
4. Transfer of charge through a resistor in contact with a reservoir. 
5. Magnetic hysteresis of a material in contact with a reservoir.  
In order to restore the system and its local surroundings to their initial states without producing changes elsewhere, \(|Q|\) units of heat would have to be extracted from the reservoir and converted completely into work. Since this would involve a violation of the second law (Kelvin statement), all processes of the above type are irreversible.  
Another set of processes involves the adiabatic transformation of work into internal energy of a system. This is depicted schematically in Fig. 6- 10 and is illustrated by the following examples, similar to the preceding list:  
6. Friction from rubbing two thermally insulated solids. 
7. Irregular stirring of a viscous thermally insulated liquid. 
8. Inelastic deformation of a thermally insulated solid. 
9. Transfer of charge through a thermally insulated resistor. 
10. Magnetic hysteresis of a thermally insulated material.  
A process of this type is accompanied by a rise of temperature of the system from, say, \(T_{i}\) to \(T_{f}\) . In order to restore the system and its local surroundings to their initial states without producing changes elsewhere, the internal energy of the system would have to be decreased by extracting \(U_{f} - U_{i}\) units of heat, thus lowering the temperature from \(T_{f}\) to \(T_{i}\) , and this heat would have to be completely converted into work. Since this violates the second law, all processes of the above type are irreversible.  
The transformation of work into internal energy either of a system or of a reservoir is seen to take place through the agency of such phenomena as friction, viscosity, inelasticity, electric resistance, and magnetic hysteresis. These effects are known as dissipative effects and the work is said to be dissipated. Processes involving the dissipation of work into internal energy are said to exhibit external mechanical irreversibility. It is a matter of everyday experience that dissipative effects, particularly friction, are always present in machines. Friction, of course, may be reduced considerably by suitable lubrication, but experience has shown that it can never be completely eliminated. If friction could be eliminated, then a machine could run indefinitely without
===== Page 182 =====
**FIGURE 6-9**  
Isothermal transformation of work through a system (which remains unchanged) into internal energy of a reservoir.  
**FIGURE 6-10** Adiabatic transformation of work into internal energy of a system.  
violating either of the two laws of thermodynamics; that is, it would run but produce no work. The operation of a machine that has no dissipation of work and thus violates the fact that all natural processes are irreversible is called a perpetual motion machine of the third kind. Friction renders a process irreversible, since heat is produced by friction in whichever direction the process is traversed. For this reason, all the cycles discussed in this chapter are idealized by assuming frictionless processes.  
This chapter is quite unusual in its use of negative statements to formulate the fundamental second law of thermodynamics. The Kelvin- Planck statement and Clausius statement each independently and equivalently establish the second law. Furthermore, the impossibility of creating three kinds of perpetual motion machines may be used to formulate the first and second laws of thermodynamics and the definition of reversibility. If we were to state the very broad laws of thermodynamics in a positive sense, then, in principle, it would require a very large number of experiments to verify the laws. On the other hand, by stating at least the second law in a negative sense, it is asserted that if a single, well- substantiated violation of the statement can be found, then the law is not valid. As a matter of fact, within their range of applicability, no violation of the laws of thermodynamics has been found.
===== Page 183 =====
### 6.11 INTERNAL MECHANICAL IRREVERSIBILITY  
The following very important natural processes involve the transformation of internal energy of a system into mechanical energy and then back into internal energy again:  
1. Ideal gas rushing into a vacuum (free expansion, i.e., Joule expansion). 
2. Gas flowing through a porous plug (throttling process, i.e., Joule-Thomson expansion). 
3. Snapping of a stretched wire after it is cut. 
4. Collapse of a soap film after it is punctured.  
We shall prove the irreversibility of only the first process.  
During a free expansion, no interactions take place, and hence there are no local surroundings. The only effect produced is a change of state of an ideal gas from a volume \(V_{i}\) and temperature \(T\) to a larger volume \(V_{f}\) at the same temperature \(T\) . To restore the gas to its initial state, it would have to be compressed isothermally to the volume \(V_{i}\) . If the compression were performed quasi- statically and there were no friction between the piston and cylinder, an amount of work \(W\) would have to be done by some outside mechanical device, and an equal amount of heat would have to flow out of the gas into a reservoir at the temperature \(T\) . If the mechanical device and the reservoir are to be left unchanged, the heat would have to be extracted from the reservoir and converted completely into work. Since this last step is impossible, the process is irreversible.  
In a free expansion, immediately after the valve is opened, there is a transformation of some of the internal energy into kinetic energy of "mass motion" or "streaming," and then this kinetic energy is dissipated through viscosity into internal energy again. Similarly, when a stretched wire is cut, there is first a transformation of internal energy into kinetic energy of irregular motion and of vibration, and then the dissipation of this energy through inelasticity into internal energy again. In all the processes, the first energy transformation takes place as a result of mechanical instability, and the second by virtue of some dissipative effect. A process of this sort is said to exhibit internal mechanical irreversibility.  
### 6.12 EXTERNAL AND INTERNAL THERMAL IRREVERSIBILITY  
Consider the following processes involving a transfer of heat between a system and a reservoir by virtue of a finite temperature difference:  
1. Conduction or radiation of heat from a system to a cooler reservoir.
===== Page 184 =====
2. Conduction or radiation of heat through a system (which remains unchanged) from a hot reservoir to a cooler one.  
If, at the conclusion of such a process, one attempts to restore both the system and its local surroundings to their initial states without producing changes elsewhere, heat would have to be transferred by means of a self- acting device from a cooler to a hotter body. Since this violates the second law (Clausius statement), all processes of this type are irreversible. Such processes are said to exhibit external thermal irreversibility.  
A process involving a transfer of heat between parts of the same system, because of nonuniform temperatures, is also obviously irreversible by virtue of the Clausius statement of the second law. Such a process is said to exhibit internal thermal irreversibility.  
### 6.13 CHEMICAL IRREVERSIBILITY  
Some of the most interesting processes that go on in nature involve a spontaneous change of internal structure, chemical composition, density, crystal form, etc. Some important examples follow.  
Formation of new chemical compounds:  
1. All chemical reactions.  
Mixing of two different substances:  
2. Diffusion of two dissimilar inert ideal gases.  
3. Mixing of alcohol and water.  
Sudden change of phase:  
4. Freezing of supercooled liquid.  
5. Condensation of supersaturated vapor.  
Transport of matter between phases in contact:  
6. Solution of solid in water.  
7. Osmosis.  
Such processes are by far the most difficult to handle and must, as a rule, be treated by special methods. Such methods constitute what is known as chemical thermodynamics and are discussed in Chaps. 15, 16, and 17. It can be shown that the diffusion of two dissimilar inert ideal gases is equivalent to two independent free expansions. Since a free expansion is irreversible, it follows that diffusion is irreversible. At present, the statement that the other processes described above are irreversible is stated without proof. Processes that involve a spontaneous change of chemical structure, density, phase, etc., are said to exhibit chemical irreversibility.
===== Page 185 =====
### 6.14 CONDITIONS FOR REVERSIBILITY  
Most processes that occur in nature are included among the general types of process listed in the preceding sections. Living processes, such as cell division, tissue growth, etc., are no exception. If one takes into account all the interactions that accompany living processes, such processes are irreversible. It is a direct consequence of the second law of thermodynamics that all natural spontaneous processes are irreversible.  
A careful inspection of the various types of natural process shows that all involve one or both of the following features:  
1. The conditions for mechanical, thermal, or chemical equilibrium, namely, thermodynamic equilibrium, are not satisfied. 
2. Dissipative effects, such as friction, viscosity, inelasticity, electric resistance, and magnetic hysteresis, are present.  
For a process to be reversible, it must not possess these features. If a process is performed quasi- statically, the system passes through states of thermodynamic equilibrium, which may be traversed just as well in one direction as in the opposite direction. If there are no dissipative effects, all the work done by the system during the performance of a process in one direction can be returned to the system during the reverse process. We are led, therefore, to the conclusion that a process will be reversible when: (1) it is performed quasi- statically; and (2) it is not accompanied by any dissipative effects.  
Since it is impossible to satisfy these two conditions perfectly, it is obvious that a reversible process is purely an ideal abstraction, extremely useful for theoretical calculations (as we shall see) but quite devoid of reality. In this sense, the assumption of a reversible process in thermodynamics resembles the assumptions made so often in mechanics, such as those which refer to weightless strings, frictionless pulleys, and point masses.  
A heat reservoir is defined as a body of very large mass capable of absorbing or rejecting an unlimited supply of heat without suffering appreciable changes in its thermodynamic coordinates. The changes that do take place are so very slow and so minute that dissipative actions never develop. Therefore, when heat enters or leaves a reservoir, the changes that take place in the reservoir are the same as those which would take place if the same quantity of heat were transferred reversibly.  
It is possible, in the laboratory, to approximate the conditions necessary for the performance of reversible processes. For example, if a gas is confined in a cylinder equipped with a well- lubricated piston and is allowed to expand very slowly against an opposing force, provided either by an object suspended from a frictionless pulley or by an elastic spring, the gas undergoes an approximately reversible process. Similar considerations apply to a wire and to a surface.
===== Page 186 =====
164 PART I: Fundamental Concepts  
A reversible transfer of charge from one electrode to the other electrode of an electrochemical cell (battery) may be imagined as follows. Suppose that a motor whose coils have a negligible resistance is caused to rotate until its back emf is only slightly different from the emf of the cell. Suppose further that the motor is coupled either to an object suspended from a frictionless pulley or to an elastic spring. If neither the cell itself nor the connecting wires to the motor have appreciable resistance, a reversible transfer of charge takes place.  
In order to arrive at conclusions concerning the equilibrium states of thermodynamic systems, it is often necessary to invoke some sort of process in which the system passes through these states. To assume the process is quasi- static only, often is not sufficient; if dissipative effects are present, there may be heat flows or internal energy changes of neighboring systems (envelopes, containers, and surroundings) that limit the validity of the argument. In order to ensure that equilibrium states of the system only are considered, without having to take account of the effect of dissipated work in the system itself or in some other neighboring body, it is useful to invoke the concept of a reversible process, even though this assumption may at times seem a bit drastic. Notice that a quasi- static process is reversible only when dissipative effects are not present; otherwise, the quasi- static process with dissipative effects is irreversible. Thus, the processes in all four idealized cycles introduced in this chapter were assumed to be quasi- static without dissipation, that is, reversible.  
Thermodynamics is by no means unique in introducing concepts using idealized systems. Mechanics deals with point masses and elastic collisions; electricity deals with wires having no resistance and batteries having constant voltages; quantum mechanics solves the hydrogen atom with coulombic interactions. A subject with idealized conditions is introduced for three reasons. First, the problems can be solved in simple, analytical forms. Next, the results are the optimum that can be achieved and serve as limiting cases. And, finally, the solutions to the ideal situations serve as the basis for approximation or perturbation methods in dealing with real situations as complications are introduced.  
## PROBLEMS  
6.1. Show that the thermal efficiency of an ideal Otto cycle is given by  
\[\eta = 1 - \frac{1}{\eta^{\gamma - 1}},\]  
where the ratio \(r = V_{1} / V_{2}\) is called either the compression ratio or the expansion ratio for a gasoline engine. In practice, \(r\) cannot be made greater than about 10, because if \(r\) is larger, then the rise in temperature upon compression of the mixture of gasoline and air is great enough to cause combustion before the discharge of the spark. This is called preignition. Take \(r\) equal to 9 and \(\gamma\) equal to approximately 1.3 (because it is a mixture) and calculate the thermal efficiency.
===== Page 187 =====
6.2. Show that the thermal efficiency of an ideal Diesel cycle is given by  
\[\eta = 1 - \frac{1}{\gamma}\frac{(1 / r_E)^{\gamma} - (1 / r_C)^{\gamma}}{(1 / r_E) - (1 / r_C)},\]  
where the ratio \(r_{C} = V_{1} / V_{2}\) is called the compression ratio and the ratio \(r_{E} = V_{3} / V_{2}\) is called the expansion ratio for a diesel engine. The compression ratio of a diesel engine is much larger than that of a gasoline engine, because there is no preignition as only air is being compressed. Take \(r_{C} = 20\) , \(r_{E} = 5\) , and \(\gamma = 1.4\) and calculate the thermal efficiency.  
6.3. Figure P6-1 represents a simplified \(P V\) diagram of the Joule ideal- gas cycle. All processes are quasi- static, and \(C_{P}\) is constant. Prove that the thermal efficiency of an engine performing this cycle is  
\[\eta = 1 - \left(\frac{P_{1}}{P_{2}}\right)^{(\gamma - 1) / \gamma}.\]  
**FIGURE P6-1** Joule ideal-gas cycle.  
6.4. Figure P6-2 represents a simplified \(P V\) diagram of the Sargent ideal- gas cycle. All processes are quasi- static, and the heat capacities are constant. Prove that the thermal efficiency of an engine performing this cycle is  
\[\eta = 1 - \gamma \frac{T_{4} - T_{1}}{T_{3} - T_{2}}.\]  
6.5. Figure P6- 3 represents an imaginary ideal- gas cycle. Assuming constant heat capacities, show that the thermal efficiency is  
\[\eta = 1 - \gamma \frac{(V_{1} / V_{2}) - 1}{(P_{3} / P_{2}) - 1}.\]
===== Page 188 =====
166 PART I: Fundamental Concepts  
**FIGURE P6-2**  
Sargent ideal- gas cycle.  
**FIGURE P6-3**  
Imaginary ideal- gas cycle.  
6.6. An imaginary ideal- gas engine operates in a cycle, which forms a rectangle with sides parallel to the axes of a \(PV\) diagram. Call \(P_{1}\) and \(P_{2}\) the lower and higher pressures, respectively; call \(V_{1}\) and \(V_{2}\) the lower and higher volumes, respectively.  
(a) Calculate the work done in one cycle.  
(b) Indicate which parts of the cycle involve heat flow into the gas, and calculate the amount of heat flowing into the gas in one cycle. (Assume constant heat capacities.)  
(c) Show that the efficiency of this engine is  
\[\eta = \frac{\gamma - 1}{\gamma P_{2} - P_{1}} +\frac{V_{1}}{V_{2} - V_{1}}.\]
===== Page 189 =====
6.7. A vessel contains \(10^{- 3} \mathrm{~m}^{3}\) of helium gas at \(3 \mathrm{~K}\) and \(10^{3} \mathrm{~Pa}\) . Take the zero of internal energy of helium to be at this state.  
(a) The temperature is raised at constant volume to \(300 \mathrm{~K}\) . Assuming helium to behave like an ideal monatomic gas, how much heat is absorbed, and what is the internal energy of the helium? Can this energy be regarded as the result of heating or working?  
(b) The helium is now expanded adiabatically to \(3 \mathrm{~K}\) . How much work is done, and what is the new internal energy? Has heat been converted to work without compensation, thus violating the second law?  
(c) The helium is now compressed isothermally to its original volume. What are the quantities of heat and work in this process? What is the thermal efficiency of the cycle? Plot the cycle on a \(PV\) diagram.  
6.8. In the tropics, the water near the surface is warmer than the deep water. Would an engine operating between these two levels violate the second law? Why?  
6.9. Would a nuclear power plant violate either the first law or the second law of thermodynamics? Explain.  
6.10. A storage battery is connected to a motor, which is used to lift a weight. The battery remains at constant temperature by receiving heat from the outside air. Is this a violation of the second law? Why?  
6.11. A convenient measure of the performance of a refrigerator is expressed by the coefficient of performance \(\omega\) , which is the ratio of the heat extracted from the low- temperature reservoir to the work done on the refrigerant. Unlike the thermal efficiency \(\eta\) , \(\omega\) may be considerably larger than unity. Derive an expression for the heat rejected to the high- temperature reservoir. Such a refrigerator is called a "heat pump" and can warm a house in winter by refrigerating the ground, outside air, or water supplied in the mains. Assume a value of 5 for the coefficient of performance and comment on the effectiveness of a heat pump.  
6.12. There are many paramagnetic solids that have internal energies which depend only on temperature, like an ideal gas. In an isothermal decrease of the magnetic field, heat is absorbed from one reservoir and converted completely into work. Is this a violation of the second law? Explain.  
6.13. Prove that it is impossible for two reversible adiabatics to intersect. (Hint: Assume that they do intersect and complete the cycle with an isothermal. Show that the performance of this cycle violates the second law.)
===== Page 190 =====
### 7.1 CARNOT CYCLE  
During a part of the cycle performed by the working substance in an engine, some heat is absorbed from a hotter reservoir; during another part of the cycle, a smaller amount of heat is rejected to a cooler reservoir. Therefore, the engine is said to operate between these two reservoirs. Since it is a fact of experience that some heat is always rejected to the cooler reservoir, the efficiency of an actual engine is never 100 percent. If we assume that we have at our disposal two reservoirs at given temperatures, it is important to answer the following questions: (1) What is the maximum thermal efficiency that can be achieved by an engine operating between these two reservoirs, inasmuch as 100 percent efficiency is not allowed by the second law? (2) What are the characteristics of such an engine? (3) Of what effect is the nature of the working substance?  
The importance of these questions was recognized by Nicolas Léonard Sadi Carnot, a brilliant young French engineer who, in 1824, before the first law of thermodynamics was firmly established, described in a paper entitled "Réflexions sur la Puissance Motrice du Feu" ("Reflections on the Motive Power of Fire") an ideal engine operating in a particularly simple cycle known today as the Carnot cycle.  
In describing and explaining the behavior of the idealized heat engine, Carnot made use of three terms: feu, chaleur, and calorique. By feu, he meant fire or flame, and, when the word is so translated, no misconceptions arise. Carnot gave, however, no definitions for chaleur and calorique, but in a footnote stated that they had the same meaning. If both of these words are translated as heat, then Carnot's reasoning is contrary to the first law of thermodynamics. There is, however, some evidence that, in spite of the unfor
===== Page 191 =====
1. A reversible adiabatic process is performed in such a direction that the temperature rises to that of the high- temperature reservoir, \(T_H\) .  
2. The working substance is maintained in contact with the reservoir at \(T_H\) , and a reversible isothermal process is performed in such a direction and to such an extent that heat \(|Q_H|\) is absorbed from the reservoir.  
3. A reversible adiabatic process is performed in a direction opposite to process 1 until the temperature drops to that of the low- temperature reservoir, \(T_L\) .  
4. The working substance is maintained in contact with the reservoir at \(T_L\) , and a reversible isothermal process is performed in a direction opposite to process 2 until the working substance and the surroundings are in their initial states. During this process, heat \(|Q_L|\) is rejected to the low- temperature reservoir.  
An engine operating in a Carnot cycle is called a Carnot engine. A Carnot engine operates between two reservoirs in a particularly simple way. All the absorbed heat enters the system at a constant high temperature, namely, that of the hotter reservoir. Also, all the rejected heat leaves the system at a constant low temperature, that of the cooler reservoir. Notice that the exchange of heat in the Carnot cycle is unlike the situation for idealized real engines, which need a series of reservoirs to exchange heat during the constant- volume or constant- pressure processes in order to achieve reversibility. In the Carnot cycle, a single reservoir exchanges heat during a constant- temperature process. Since all four processes are reversible, the Carnot engine is a reversible engine.
===== Page 192 =====
### 7.2 EXAMPLES OF CARNOT CYCLES  
The simplest example of a Carnot cycle is that of a gas (not necessarily an ideal gas) depicted on a \(PV\) diagram in Fig. 7- 1. The dashed lines marked \(T_H\) and \(T_L\) are isothermal curves. The gas is initially in the state represented by the point 1. The four processes are then:  
1. Process \(1\rightarrow 2\) , reversible adiabatic compression until the temperature rises to \(T_H\) .  
2. Process \(2\rightarrow 3\) , reversible isothermal expansion until any desired point, such as 3, is reached.  
3. Process \(3\rightarrow 4\) , reversible adiabatic expansion until the temperature drops to \(T_L\) .  
4. Process \(4\rightarrow 1\) , reversible isothermal compression until the original state is reached.  
During the isothermal expansion \(2\rightarrow 3\) , heat \(|Q_H|\) is absorbed from the hotter reservoir at \(T_H\) . During the isothermal compression \(4\rightarrow 1\) , heat \(|Q_L|\) is rejected to the cooler reservoir at \(T_L\) .  
For a two- phase system, such as steam and water, the Carnot cycle has a shape quite different from a gaseous system. This is shown on a \(PV\) diagram in Fig. 7- 2. The dashed line \(L_A V_A\) denotes the isothermal and isobaric vaporization of the liquid at the higher temperature \(T_H\) ; the (dashed) line \(L_B V_B\) denotes the isothermal and isobaric condensation of the vapor at the lower temperature \(T_L\) . Any point between the dashed lines \(L\) and \(V\) represents a  
**FIGURE 7- 1** Carnot cycle of a real gas.
===== Page 193 =====
5. Process \(1 \rightarrow 2\) , reversible adiabatic compression until the temperature rises to \(T_H\) .  
6. Process \(2 \rightarrow 3\) , reversible isothermal isobaric vaporization until any arbitrary point, such as 3, is reached.  
7. Process \(3 \rightarrow 4\) , reversible adiabatic expansion until the temperature drops to \(T_L\) .  
8. Process \(4 \rightarrow 1\) , reversible isothermal isobaric condensation until the initial state is reached.  
During the isothermal vaporization \(2 \rightarrow 3\) , heat \(|Q_H|\) is absorbed from the hotter reservoir at \(T_H\) . During the isothermal condensation \(4 \rightarrow 1\) , heat \(|Q_L|\) is rejected to the cooler reservoir at \(T_L\) .  
A Carnot cycle using an electrochemical cell (acid battery) is depicted on an \(\mathcal{E}Z\) diagram in Fig. 7- 3. The (dashed) lines marked \(T_H\) and \(T_L\) represent isothermal and constant emf curves at the two temperatures of the reservoirs. The point 1 indicates that the cell is well charged. The four processes are:  
9. Process \(1 \rightarrow 2\) , reversible adiabatic flow of charge from - to + in the external circuit until the temperature rises to \(T_H\) .  
10. Process \(2 \rightarrow 3\) , reversible isothermal flow of charge from + to - in the external circuit until an arbitrary point 3 is reached.  
11. Process \(3 \rightarrow 4\) , reversible adiabatic flow of charge until the temperature drops to \(T_L\) .  
12. Process \(4 \rightarrow 1\) , reversible isothermal flow of charge until the initial state is restored.
===== Page 194 =====
172 PART I: Fundamental Concepts  
**FIGURE 7-3** Carnot cycle of an electrochemical cell.  
During the isothermal process \(2 \rightarrow 3\) , heat \(|Q_H|\) is absorbed from the hotter reservoir at \(T_H\) . During the isothermal process \(4 \rightarrow 1\) , heat \(|Q_L|\) is rejected to the cooler reservoir at \(T_L\) .  
As a last example of a Carnot cycle, that of a paramagnetic substance which obeys Curie's law is shown on an \(\mathcal{H}M\) diagram in Fig. 7- 4. The (dashed) lines \(0T_H\) and \(0T_L\) represent isothermal lines at the temperatures \(T_H\) and \(T_L\) , respectively. Starting at point 1, the four processes are:  
13. Process \(1 \rightarrow 2\) , reversible adiabatic magnetization until the temperature rises to \(T_H\) .  
14. Process \(2 \rightarrow 3\) , reversible isothermal demagnetization until an arbitrary point 3 is reached.  
15. Process \(3 \rightarrow 4\) , reversible adiabatic demagnetization until the temperature drops to \(T_L\) .  
16. Process \(4 \rightarrow 1\) , reversible isothermal magnetization until the initial state is reached.  
During the isothermal demagnetization \(2 \rightarrow 3\) , heat \(|Q_H|\) is absorbed from the hotter reservoir at \(T_H\) . During the isothermal magnetization \(4 \rightarrow 1\) , heat \(|Q_L|\) is rejected to the cooler reservoir at \(T_L\) .  
The net work done in one cycle by any Carnot engine can be adjusted to any arbitrary amount by choosing the position of the point 3, that is, by adjusting the extent of the isothermal process \(2 \rightarrow 3\) , which controls the amount of heat \(|Q_H|\) from the high- temperature reservoir. The nature of the working substance determines the thermodynamic coordinates used to plot a Carnot cycle, as well as the shape of the cycle. It will be shown, however, in the next chapter that it is possible to find two thermodynamic coordinates that
===== Page 195 =====
**FIGURE 7- 4** Carnot cycle of a paramagnetic substance.  
form a rectangle for the graph of a Carnot cycle with any working substance. Consequently, we shall represent a Carnot engine symbolically with the aid of a rectangle, as shown in Fig. 7- 5(a). The letter \(R\) inside the rectangle indicates that the Carnot cycle is a reversible cycle.  
If an engine is to operate between only two reservoirs and still operate in a reversible cycle, then it must be a Carnot engine. For example, if an Otto cycle were performed between only two reservoirs, the heat transfers in the two isochoric processes would involve finite temperature differences and, therefore, could not be reversible. Conversely, if the Otto cycle were performed reversibly, it would require a series of reservoirs, not merely two reservoirs at different temperatures. The expression "Carnot engine," therefore, means "an ideal engine operating reversibly between only two reservoirs without the need for work to be done on the system."  
### 7.3 CARNOT REFRIGERATOR  
Since a Carnot cycle consists of reversible processes, it may be performed in either direction. When it is performed in a direction opposite to that shown in the examples, it is a refrigeration cycle. A Carnot refrigerator is represented symbolically in Fig. 7- 5(b). The important feature of a Carnot refrigeration
===== Page 196 =====
174 PART I: Fundamental Concepts  
**FIGURE 7-5** Schematic representation of (a) the Carnot engine, and (b) the Carnot refrigerator.  
cycle, which distinguishes it from any general reversed engine cycle, is that the quantities \(|Q_H|,|Q_L|\) , and \(|W|\) are numerically equal to those quantities when the cycle is performed in the opposite direction. For example, exactly the same amount of heat that is absorbed by the Carnot engine from the high- temperature reservoir is rejected to the high- temperature reservoir when the cycle is reversed. This would not be the case if the cycle were irreversible, because of dissipative effects.  
### 7.4 CARNOT'S THEOREM AND COROLLARY  
We are now ready to prove Carnot's theorem, which is stated as follows: No heat engine operating between two given reservoirs can be more efficient than a Carnot engine operating between the same two reservoirs. Imagine a Carnot engine \(R\) , which is reversible, and any other engine \(I\) , which is irreversible, working between the same two reservoirs and adjusted so that they both deliver the same amount of work \(|W|\) . Thus:  
| Carnot engine \(R\) | Irreversible engine \(I\) |
| :--- | :--- |
| 1. Absorbs heat \(|Q_H|\) from the high- temperature reservoir. | 1. Absorbs heat \(|Q_H^{\prime}|\) from the high- temperature reservoir. |
| 2. Performs work \(|W|\) | 2. Performs work \(|W|\) |
| 3. Rejects heat \(Q_H| - |W|\) to the low- temperature reservoir. | 3. Rejects heat \(|Q_H^{\prime}| - |W|\) to the low- temperature reservoir. |
| 4. Efficiency \(\eta_R = |W| / |Q_H|\) | 4. Efficiency \(\eta_I = |W| / |Q_H^{\prime}|\) |
===== Page 197 =====
Let us assume that the efficiency of the engine \(I\) is greater than that of \(R\) . Thus,  
\[\eta_I > \eta_R,\]  
\[\frac{|W|}{|Q_H^{\prime}|} > \frac{|W|}{|Q_H|},\]  
\[|Q_H| > |Q_H^{\prime}|.\]  
Now let the engine \(I\) drive the Carnot engine \(R\) backward as a Carnot refrigerator. This is shown symbolically in Fig. 7- 6. The engine and the refrigerator coupled together in this way constitute a self- contained machine, since all the work needed to operate the refrigerator is supplied by the engine. The net heat extracted from the low- temperature reservoir is  
\[(|Q_H| - |W|) - (|Q_H^{\prime}| - |W|) = |Q_H| - |Q_H^{\prime}|,\]  
which is positive. The net heat delivered to the high- temperature reservoir is also \(|Q_H| - |Q_H^{\prime}|\) . Therefore, the effect of this self- contained machine is to transfer \(|Q_H| - |Q_H^{\prime}|\) units of heat from a low- temperature reservoir to a high- temperature reservoir without work being done by the surroundings. Since this device violates the second law of thermodynamics (Clausius statement), our original assumption that \(\eta_I > \eta_R\) is false and Carnot's theorem is proved. We may express this result in symbols, thus:  
\[\eta_I\leq \eta_R. \quad (7.1)\]  
The following corollary to Carnot's theorem may be easily proved: All Carnot engines operating between the same two reservoirs have the same efficiency. Consider two Carnot engines \(R_1\) and \(R_2\) , operating between the same  
**FIGURE 7-6** Irreversible engine \(I\) operating a Carnot refrigerator \(R\) .
===== Page 198 =====
176 PART I: Fundamental Concepts  
two reservoirs. If we imagine \(R_1\) driving \(R_2\) backward, then Carnot's theorem states that  
\[\eta_{R_1}\leq \eta_{R_2}.\]  
If \(R_2\) drives \(R_1\) backward, then  
\[\eta_{R_2}\leq \eta_{R_1}.\]  
But, the efficiency of the first reversible engine cannot be both less than or equal to the efficiency of the second reversible engine, as well as greater than or equal to the efficiency of the second reversible engine. Therefore, it follows that the efficiencies can only be equal:  
\[\eta_{R_1} = \eta_{R_2}. \quad (7.2)\]  
It is clear from the above result that the nature of the working substance which is undergoing the Carnot cycle has no influence on the efficiency of the Carnot engine.  
To summarize, the maximum thermal efficiency that can be achieved by a heat engine operating between two heat reservoirs at different temperatures is the efficiency of a Carnot engine operating between the same two reservoirs. The essential characteristic of a Carnot engine is that it is reversible and operates between two reservoirs, rather than two series of reservoirs. The superior efficiency of the Carnot cycle is due to its absorbing all heat at the highest temperature and rejecting all heat at the lowest temperature. Furthermore, a Carnot engine is independent of the working substance of the system.  
### 7.5 THE THERMODYNAMIC TEMPERATURE SCALE  
In Chap. 1, it was pointed out that the zeroth law of thermodynamics establishes the basis for the measurement of temperature, but an empirical temperature scale must be defined in terms of the thermometric property of a specific substance and thermometer, such as the ideal- gas temperature scale using the constant- volume gas thermometer. A temperature scale that is independent of the nature of the working substance, which is called an absolute or thermodynamic temperature scale, would be most desirable. In Sec. 7.4, it was proven that the efficiency of a Carnot cycle is independent of the working substance and depends only on temperature. The Carnot engine provides the basis for the thermodynamic temperature scale.  
A Carnot engine absorbing \(\left|Q_H\right|\) units of heat from a reservoir at a higher temperature \(T_H\) and rejecting \(\left|Q_L\right|\) units of heat to a reservoir at a lower temperature \(T_L\) has an efficiency \(\eta_R\) that is independent of the nature of the working substance. The thermal efficiency is given by Eq. (6.2), namely,
===== Page 199 =====
\[\eta_R = 1 - \frac{|Q_L|}{|Q_H|}.\]  
The efficiency depends only on the two temperatures of the reservoirs,  
\[\eta_R = \phi (T_H,T_L),\]  
where \(\phi (T_H,T_L)\) is an unknown function of the two temperatures. Rearranging the above two equations, we get  
\[\frac{|Q_H|}{|Q_L|} = \frac{1}{1 - \phi(T_H,T_L)} = f(T_H,T_L), \quad (7.3)\]  
where \(f(T_H,T_L)\) is also an unknown function of the two temperatures.  
Let us apply Eq. (7.3) to the three Carnot engines operating between the three reservoirs shown in Fig. 7- 7, where \(T_1 > T_3 > T_2\) . For engine \(R_A\) ,  
\[\frac{|Q_1|}{|Q_2|} = f(T_1,T_2).\]  
Now consider the second Carnot engine \(R_B\) and third Carnot engine \(R_C\) . Since the heat \(|Q_3|\) rejected by the second Carnot engine \(R_B\) is absorbed by the third Carnot engine \(R_C\) , both engines working together are equivalent to the first Carnot engine \(R_A\) . Thus, engine \(R_B\) absorbs the same heat \(|Q_1|\) from the reservoir at \(T_1\) that engine \(R_A\) absorbs. So, for engine \(R_B\) ,  
**FIGURE 7- 7** Schematic diagram of Carnot engines used to demonstrate the thermodynamic temperature scale.
===== Page 200 =====
178 PART I: Fundamental Concepts  
\[\frac{|Q_1|}{|Q_3|} = f(T_1, T_3).\]  
Engine \(R_A\) rejects heat \(|Q_2|\) to the low- temperature reservoir, so engine \(R_C\) must also reject heat \(|Q_2|\) to the low- temperature reservoir. Thus, for engine \(R_C\)  
\[\frac{|Q_3|}{|Q_2|} = f(T_3, T_2).\]  
Since  
\[\frac{|Q_1|}{|Q_2|} = \frac{|Q_1| / |Q_3|}{|Q_2| / |Q_3|},\]  
we have the result that  
\[f(T_{1}, T_{2}) = \frac{f(T_{1}, T_{3})}{f(T_{2}, T_{3})}. \quad (7.4)\]  
Now, the temperature \(T_3\) is arbitrarily chosen; and since it does not appear in the left- hand member of Eq. (7.4), \(T_3\) must, therefore, drop out of the ratio on the right. After it has been canceled, the numerator can be written \(\psi (T_1)\) and the denominator \(\psi (T_2)\) , where \(\psi\) is another unknown function of one temperature. Thus,  
\[\frac{|Q_1|}{|Q_2|} = \frac{\psi(T_1)}{\psi(T_2)}. \quad (7.5)\]  
The ratio on the right is defined as the ratio of two thermodynamic temperatures and is denoted by \(T_1 / T_2\) . We have, therefore, finally,  
\[\frac{|Q_1|}{|Q_2|} = \frac{T_1}{T_2}. \quad (7.6)\]  
Thus, two temperatures on the thermodynamic scale are to each other as the absolute values of the heats absorbed and rejected, respectively, by a Carnot engine operating between reservoirs at these temperatures. It is seen that the thermodynamic temperature scale is independent of the specific characteristics of any particular substance. Thus, the Carnot engine supplies the universality that is lacking in the ideal- gas temperature scale. Finally, the thermodynamic temperatures are called "absolute" temperatures, because they are independent of any material.  
Equation (7.5) is the fundamental relationship based on the second law of thermodynamics and the Carnot cycle. All that is necessary of the arbitrary function \(\psi\) is that \(\psi\) be a function of the thermodynamic temperature. Any function will do. In 1848, Kelvin was forced to choose a linear function of temperature in Eq. (7.6), because all the scientific and engineering data had been obtained from the mercury- in- glass thermometer, which is essentially linear over its useful range. As a result, on the thermodynamic scales now

---
### ==از اینجا به بعد شماره همه صفحات رو باید بعلاوه 200 کنیم 

---
===== Page 1 =====

in use (Kelvin or Rankine), the temperatures vary from \(0\) to \(+ \infty\) for ordinary systems. Kelvin recognized the asymmetry of the end- points of the linear scale and proposed, as his first choice, that \(\psi\) be a logarithmic function of the thermodynamic temperature. On the logarithmic scale, temperatures vary from \(- \infty\) to \(+ \infty\) . The advantage of the logarithmic scale is that absolute zero is far removed from the normal freezing point of water, whereas, on the linear scale, absolute zero is "only" a few hundred degrees below the ice point.

At first thought, it might seem that the ratio of two Kelvin temperatures would be impossible to measure, since a Carnot engine is an ideal engine, quite impossible to construct. The situation, however, is not as bad as it seems. The ratio of two Kelvin temperatures is the ratio of two heats that are transferred during two isothermal processes bounded by the same two adiabatic curves. The two adiabatic boundaries may be located experimentally, and the heats transferred during two isothermal "nearly reversible" processes can be measured with considerable precision. As a matter of fact, this is one of the methods used in measuring temperatures below \(1 \mathrm{~K}\) .

To complete the definition of the thermodynamic scale, we proceed to assign the arbitrary value of \(273.16 \mathrm{~K}\) to the temperature of the triple point of water \(T_{TP}\) , as in Chap. 1. Thus,

\[T_{TP} = 273.16 \mathrm{~K}.\]

For a Carnot engine operating between reservoirs at the temperatures \(T\) and \(T_{TP}\) , we have

\[\frac{|Q|}{|Q_{TP}|} = \frac{T}{T_{TP}},\]

or

\[T = 273.16 \mathrm{~K} \frac{|Q|}{|Q_{TP}|}. \quad (7.7)\]

Comparing Eq. (7.7) with the corresponding equation for the ideal- gas temperature, namely, Eq. (1.7),

\[T = 273.16 \mathrm{~K} \lim_{P_{TP} \to 0} \left(\frac{P}{P_{TP}}\right),\]

it is seen that, in the thermodynamic scale, \(|Q|\) plays the role of a "thermometric property" for a Carnot cycle, just as pressure is the thermometric property for a constant- volume gas thermometer. Heat does not, however, have the objection attached to the thermodynamic coordinate pressure of the arbitrarily chosen gas- thermometer, inasmuch as the behavior of a Carnot engine is independent of the nature of the working substance.

===== Page 2 =====

### 7.6 ABSOLUTE ZERO AND CARNOT EFFICIENCY

It follows from Eq. (7.7),

\[T = 273.16\mathrm{K}\frac{|Q|}{|Q_{TP}|},\]

that the smaller the value of \(|Q|\) , the lower the corresponding \(T\) . The smallest possible value of \(|Q|\) is zero, and the corresponding \(T\) is absolute zero. Thus, if a system undergoes a reversible isothermal process without transfer of heat, the temperature at which this process takes place is called absolute zero. In other words, at absolute zero, an isotherm and an adiabatic are identical.

It should be noticed that the definition of absolute zero holds for all substances and is, therefore, independent of the specific properties of any arbitrarily chosen substance. Furthermore, the definition is in terms of purely macroscopic concepts. No reference is made to atoms or molecules. Whether absolute zero may be achieved is a question that is left to experiment.

A Carnot engine absorbing heat \(|Q_{H}|\) from a hotter reservoir at \(T_{H}\) and rejecting heat \(|Q_{L}|\) to a cooler reservoir at \(T_{L}\) has an efficiency

\[\eta_{R} = 1 - \frac{|Q_{L}|}{|Q_{H}|}.\]

Since

\[\frac{|Q_{L}|}{|Q_{H}|} = \frac{T_{L}}{T_{H}},\]

we have the result that the efficiency of a Carnot engine can be expressed in terms of the absolute temperatures of its two heat reservoirs, namely,

\[\eta_{R} = 1 - \frac{T_{L}}{T_{H}}. \quad (7.8)\]

For a Carnot engine to have an efficiency of 100 percent, it is clear that \(T_{L}\) must be zero. Only when the lower reservoir is at absolute zero will all the heat be converted into work. Since nature does not provide us with a reservoir at absolute zero, a heat engine with 100 percent efficiency is a practical impossibility.

### 7.7 EQUALITY OF IDEAL-GAS AND THERMODYNAMIC TEMPERATURES

In Chap. 1, the ideal- gas temperature was defined in terms of the ratio of the pressure \(P\) to the pressure of the system at the triple point of water \(P_{TP}\) in the limit as \(P_{TP}\) approaches zero. In anticipation of this section, the ideal- gas temperature was given the symbol \(T\) for thermodynamic temperature, but let us return to the earlier symbol \(\theta\) and proceed to prove their equality.

A Carnot cycle of an ideal gas is depicted on a \(PV\) diagram in Fig. 7- 8. The two isothermal processes \(2 \rightarrow 3\) at temperature \(\theta_{1}\) and \(4 \rightarrow 1\) at temperature \(\theta_{2}\) are represented by equilateral hyperbolas whose equations are, respectively,

\[PV = nR\theta_{1}\]

and

\[PV = nR\theta_{2}.\]

For any infinitesimal reversible process of an ideal gas, the first law may be written

\[\mathrm{d}Q = C_{V}d\theta +P dV.\]

Applying this equation to the isothermal process \(2 \rightarrow 3\) , the heat absorbed is found to be

\[|Q_{1}| = \int_{V_{2}}^{V_{3}}P dV\] \[\qquad = nR\theta_{1}\ln \frac{V_{3}}{V_{2}}.\]

Similarly, for the isothermal process \(4 \rightarrow 1\) , the heat rejected is

\[|Q_{2}| = nR\theta_{2}\ln \frac{V_{4}}{V_{1}},\]

===== Page 3 =====

**FIGURE 7-8** Carnot cycle of an ideal gas. (Note: The processes are shown with exaggerated line segments in order to separate clearly the adiabatic curves from the isothermal curves.) The graph displays Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. The cycle consists of four points: 1, 2, 3, and 4. The isothermal curves are marked \(PV = nR\theta_{1}\) (between 2 and 3) and \(PV = nR\theta_{2}\) (between 4 and 1). The adiabatic curves are marked \(PV^{\gamma} = K_{1}\) (between 1 and 2) and \(PV^{\gamma} = K_{2}\) (between 3 and 4).

where the rejection of heat interchanged the limits of integration. Therefore,

\[\frac{|Q_1|}{|Q_2|} = \frac{\theta_1 \ln(V_3 / V_2)}{\theta_2 \ln(V_4 / V_1)}. \quad (7.9)\]

Since the process \(1 \rightarrow 2\) is adiabatic, we may write, for any infinitesimal portion,

\[-C_V d\theta = P dV,\]

\[-C_V d\theta = \frac{nR\theta}{V} dV.\]

Integrating from \(1 \rightarrow 2\) , we get

\[\frac{1}{nR} \int_{\theta_1}^{\theta_2} C_V \frac{d\theta}{\theta} = \ln \frac{V_2}{V_1}.\]

Similarly, for the adiabatic process \(3 \rightarrow 4\)

\[\frac{1}{nR} \int_{\theta_2}^{\theta_1} C_V \frac{d\theta}{\theta} = \ln \frac{V_4}{V_3}.\]

Therefore,

\[\ln \frac{V_2}{V_1} = \ln \frac{V_3}{V_4},\]

or

\[\ln \frac{V_3}{V_2} = \ln \frac{V_4}{V_1}.\]

Combining Eqs. (7.9) and (7.10), we obtain

\[\frac{|Q_1|}{|Q_2|} = \frac{\theta_1}{\theta_2}.\]

The thermodynamic temperature scale, defined by Eq. (7.6), allows us to replace the ratio of heats by the ratio of the thermodynamic temperatures to yield

\[\frac{T_1}{T_2} = \frac{\theta_1}{\theta_2}.\]

If \(\theta_1\) and \(T_1\) refer to any temperature, and \(\theta_2\) and \(T_2\) refer to the triple point of water, then the preceding equation becomes

\[\frac{\theta}{\theta_{TP}} = \frac{T}{T_{TP}}.\]

Since \(\theta_{TP} = T_{TP} = 273.16 \mathrm{~K}\) , it follows that

\[\theta = T.\]

===== Page 4 =====

182 PART I: Fundamental Concepts

### PROBLEMS

7.1. Take an ideal monatomic gas \(\left(\gamma = \frac{5}{3}\right)\) around the Carnot cycle, where \(T_{H} = 600 \mathrm{~K}\) and \(T_{L} = 300 \mathrm{~K}\) . Point 1 at the beginning of the adiabatic compression has pressure \(P_{1} = P_{0}\) (atmospheric pressure) and volume \(V_{1} = 50\) liters. Point 3 has a volume \(V_{3} = 75\) liters. The resulting Carnot cycle is shown in Fig. P7- 1. Calculate the values of volume and pressure at all four points, which have the same meaning as those in Fig. 7- 8.

**FIGURE P7-1** An accurately drawn Carnot cycle for an ideal gas with the ratio \(V_{3} / V_{1} = \frac{3}{2}\) . The graph shows Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. Four points 1, 2, 3, and 4 are marked, connected by two adiabatic curves and two isothermal curves.

7.2. Take an ideal monatomic gas \(\left(\gamma = \frac{5}{3}\right)\) around the Carnot cycle, where point 1 at the beginning of the adiabatic compression has pressure \(P_{1} = P_{0}\) (atmospheric pressure), volume \(V_{1} = 13\) liters, and temperature \(T_{1} = 300 \mathrm{~K}\) . Point 3 has pressure \(P_{3} = 2P_{0}\) and volume \(V_{3} = 26\) liters. The resulting Carnot cycle is shown in Fig. P7- 2. Calculate the values of volume and pressure at all four points, which have the same meaning as those in Fig. 7- 8.

7.3. An inventor claims to have developed an engine that takes in 100,000 Btu at a temperature of \(400 \mathrm{~K}\) , rejects 40,000 Btu at a temperature of \(200 \mathrm{~K}\) , and delivers \(15 \mathrm{kW} \cdot \mathrm{h}\) of work. Would you advise investing money to put this engine on the market?

7.4. A Carnot engine absorbs \(100 \mathrm{~J}\) of heat from a reservoir at the temperature of the normal boiling point of water and rejects heat to a reservoir at the temperature of the triple point of water. Find the heat rejected, the work done by the engine, and the thermal efficiency.

===== Page 5 =====

184 PART I: Fundamental Concepts

**FIGURE P7-2** An accurately drawn Carnot cycle for an ideal gas with the ratio \(V_{3} / V_{1} = 2\) . The graph shows Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. Four points 1, 2, 3, and 4 are marked.

7.5. Which is the more effective way to increase the thermal efficiency of a Carnot engine: to increase \(T_{H}\) , keeping \(T_{L}\) constant; or to decrease \(T_{L}\) , keeping \(T_{H}\) constant?

7.6. Imagine an irreversible engine \(I\) and a Carnot engine \(R\) operating between the same two reservoirs. Suppose that they absorb different amounts of heat from the high- temperature reservoir, perform different amounts of work, but reject the same amounts of heat to the low- temperature reservoir. Prove Carnot's theorem with the aid of the Kelvin- Planck statement of the second law.

7.7. In Sec. 7.4, suppose that engine \(I\) executes an irreversible cycle, and assume that \(\eta_{I} = \eta_{R}\) . Show that this assumption leads to a result that is inconsistent with the irreversibility of \(I\) , and, therefore, that \(\eta_{I} < \eta_{R}\) .

7.8. Draw a symbolic diagram of a set of Carnot engines with the following characteristics: Each engine absorbs the heat rejected by the preceding one at the temperature at which it was rejected, and each engine delivers the same amount of work. Show that the temperature intervals between which these engines operate are all equal.

7.9. Take a gas whose equation of state is \(P(\nu - b) = R\theta\) and whose heat capacity \(C_{V}\) is a function of \(\theta\) only through a Carnot cycle, and prove that \(\theta = T\) .

7.10. The initial state of \(0.1\mathrm{mol}\) of an ideal monatomic gas is \(P_{0} = 32\mathrm{Pa}\) and \(V_{0} = 8\mathrm{m}^{3}\) . The final state is \(P_{1} = 1\mathrm{Pa}\) and \(V_{1} = 64\mathrm{m}^{3}\) . Suppose that the gas undergoes a process along a straight line joining these two states with an equation \(P = aV + b\) , where \(a = - 31 / 56\) and \(b = 255 / 7\) . Plot this straight line to scale on a \(PV\) diagram. Calculate:

(a) Temperature \(T\) as a function of \(V\) along the straight line.

(b) The value of \(V\) at which \(T\) is a maximum.

(c) The values of \(T_{0}\) , \(T_{\mathrm{max}}\) , and \(T_{1}\) .

===== Page 6 =====

7.11. Show that the two states specified in Prob. 7.10 lie on an adiabatic curve. A cycle described by J. Willis and D. Kirwan, and called the "Sadly Cannot" cycle, is obtained by proceeding from the initial state to the final state along the straight line specified in Prob. 7.10 and back to the initial state along the adiabatic curve. Calculate:

(a) The work done on the gas during the adiabatic process.

(b) The net work done in the cycle.

(c) The net heat transferred to the gas.

(d) The thermal efficiency of the cycle.

(e) The thermal efficiency of a Carnot cycle operating between a reservoir at the maximum temperature in the cycle and a reservoir at the minimum temperature in the cycle.

7.12. A logarithmic thermodynamic temperature scale, which can be constructed to agree with the Celsius scale at \(\mathbf{NMP - H}_{2}\mathbf{O}\) and \(\mathbf{NBP - H}_{2}\mathbf{O}\) , is related to the Celsius scale by the formula

\[L = (99.974)\frac{\log T - \log 273.15}{\log 373.124 - \log 273.15},\]

where \(L\) is any temperature on the logarithmic temperature scale and \(T\) is the corresponding Kelvin temperature on the linear temperature scale. The formula reduces to

\[L = 738.08\log T - 1798.26.\]

(a) Calculate logarithmic temperatures for several representative temperatures between \(10^{-3}\mathrm{K}\) and \(15\times 10^{6}\mathrm{K}\)

(b) Consider two different temperature ranges on the linear scale that yield the same thermal efficiency for a Carnot cycle. Calculate the temperature ranges on the logarithmic scale and draw a conclusion about efficiency on the logarithmic scale.

===== Page 7 =====

## CHAPTER 8

## ENTROPY

### 8.1 REVERSIBLE PART OF THE SECOND LAW

Work diagrams in which a generalized force such as \(P\) , \(\mathcal{F}\) , \(\gamma\) , \(\mathcal{E}\) , or \(\mu_{0}\mathcal{K}\) is plotted against the corresponding generalized displacement \(V\) , \(L\) , \(A\) , \(Z\) , or \(\mathcal{M}\) have been used to indicate processes of various systems. An isothermal process or an adiabatic process is represented by a different curve on each diagram. In this chapter, it is desired to formulate general principles that apply to all systems. If we let the symbol \(Y\) denote any generalized force and the symbol \(X\) its corresponding generalized displacement, a generalized work diagram in which \(Y\) is plotted against \(X\) may be used to depict processes common to all systems and will thus be suitable for general discussions.

Consider a reversible process represented by the smooth curve \(i \to f\) on the generalized work diagram shown in Fig. 8- 1. The nature of the system is not essential. The dashed curves through \(i\) and \(f\) , respectively, represent portions of adiabatic processes. Let us draw a curve \(a \to b\) , representing an isothermal process, in such a way that the area under the smooth curve \(if\) is equal to the area under the zigzag sequence of processes, path \(iabf\) . Then, the work done in traversing both paths is the same, or

\[W_{if} = W_{iabf}.\]

From the first law,

\[Q_{if} = U_{f} - U_{i} - W_{if},\]

and

\[Q_{iabf} = U_{f} - U_{i} - W_{iabf}.\]

Therefore,

\[Q_{if} = Q_{iabf}.\]

===== Page 8 =====

**FIGURE 8-1** Generalized work diagram, where \(i \to f\) is any reversible process; \(i \to a\) is a reversible adiabatic process; \(a \to b\) is a reversible isothermal process; and \(b \to f\) is a reversible adiabatic process. The diagram shows Generalised force \(Y\) on the vertical axis and Generalized displacement \(X\) on the horizontal axis. A curve goes from point \(i\) to point \(f\). A zigzag path \(i \to a \to b \to f\) is superimposed, where \(a\) and \(b\) are marked such that the area under the smooth curve \(if\) equals the area under the zigzag path.

But, since no heat is transferred in the two adiabatic processes \(ia\) and \(bf\) , we have

\[Q_{if} = Q_{ab}. \quad (8.1)\]

If we are given, therefore, a reversible process in which the temperature may change in any manner, it is always possible to find a reversible zigzag path between the same two states, consisting of an adiabatic process followed by an isothermal process followed by an adiabatic process, such that the heat transferred during the isothermal segment is the same as that transferred during the original process.

Now, consider the smooth closed curve on the generalized work diagram shown in Fig. 8- 2. Since no two adiabatic lines can intersect (see Prob. 6.13), a number of adiabatic lines may be drawn, dividing the cycle into a number of adjacent strips. A zigzag closed path may now be drawn, consisting of alternate adiabatic and isothermal portions, such that the heat transferred during all the isothermal portions is equal to the heat transferred in the original cycle. Consider the two isothermal processes \(ab\) at the temperature \(T_{1}\) , during which heat \(Q_{1}\) is absorbed, and \(cd\) at the temperature \(T_{2}\) , during which heat \(Q_{2}\) is rejected. Since \(ab\) and \(cd\) are bounded by the same adiabatic curves, \(abcd\) is a Carnot cycle, and we may write Eq. (7.6) as

\[\frac{|Q_{1}|}{T_{1}} = \frac{|Q_{2}|}{T_{2}}.\]

For the sake of clearness and simplicity, we have been considering only the absolute values of heat entering or leaving a system, thus ignoring the sign convention introduced in Chap. 4. Let us now return to the sign convention and regard any \(Q\) as an algebraic symbol, positive for heat absorbed by a system and negative for heat rejected from a system. We may then write the equation cited above as

\[\frac{Q_1}{T_1} +\frac{Q_2}{T_2} = 0,\]

where \(Q_{1}\) is a positive number and \(Q_{2}\) is a negative number. Since the isothermal curves \(e f\) and \(g h\) are bounded by the same two adiabatic curves, \(e f g h\) is also a Carnot cycle, and

\[\frac{Q_3}{T_3} +\frac{Q_4}{T_4} = 0.\]

If a similar equation is written for each pair of isothermal curves bounded by the same two adiabatic curves and if all the equations are added, then the result obtained is that

\[\frac{Q_1}{T_1} +\frac{Q_2}{T_2} +\frac{Q_3}{T_3} +\frac{Q_4}{T_4} +\dots = 0.\]

Since no heat is transferred during the adiabatic portions of the zigzag cycle, we may write

\[\sum_{j}\frac{Q_{j}}{T_{j}} = 0, \quad (8.2)\]

===== Page 9 =====

**FIGURE 8-2** Generalized work diagram, where the smooth closed curve is a reversible cycle and the zigzag closed path is made up of alternating reversible isothermal and reversible adiabatic processes. The diagram shows Generalized force \(Y\) on the vertical axis and Generalized displacement \(X\) on the horizontal axis. A smooth closed curve is drawn. Inside it, a zigzag path is made of adiabatic segments (dashed lines) and isothermal segments (solid lines). Isothermal points \(a, b, c, d, e, f, g, h\) are marked at temperatures \(T_1, T_2, T_3\), and \(T_4\), with corresponding heats \(Q_1, Q_2, Q_3\), and \(Q_4\).

where the summation is taken over the entire zigzag cycle consisting of Carnot cycles, \(j\) in number.

Now, imagine the cycle divided into a very large number of strips by drawing a large number of adiabatic curves close together. If we connect these adiabatic curves with small isothermal curves, in the manner already described, then a zigzag path may be traced that can be made to approximate the original cycle as closely as we please. When these isothermal processes become infinitesimal, the ratio \(\mathrm{d}Q / T\) for an infinitesimal isothermal between two adjacent adiabatic curves is equal to the ratio \(\mathrm{d}Q / T\) for the infinitesimal piece of the original cycle bounded by the same two adiabatic curves. In the limit, therefore, we may write for Eq. (8.2) any reversible cycle,

\[\oint_{R}\frac{\mathrm{d}Q}{T} = 0. \quad (8.3)\]

The circle through the integral sign signifies that the integration takes place over the complete cycle, and the letter \(R\) emphasizes the fact that the equation is true only for a reversible cycle. This result, known as Clausius' theorem, is one part of Clausius' mathematical statement of the second law. The other part applicable to irreversible cycles will be presented in Sec. 8.8.

### 8.2 ENTROPY

Let an initial equilibrium state of any thermodynamic system be represented by the point \(i\) on any convenient diagram, such as the generalized work diagram of Fig. 8- 3. Denote a final equilibrium state by the point \(f\) . It is possible to take the system from \(i\) to \(f\) along any number of different reversible paths, since \(i\) and \(f\) are equilibrium states. Suppose the system is taken from \(i\) to \(f\) along the reversible path \(R_{1}\) and then back to \(i\) again along another reversible path \(R_{2}\) . The two paths form a reversible cycle, and from Clausius' theorem we may write

\[\oint_{R_{1}R_{2}}\frac{\mathrm{d}Q}{T} = 0.\]

The above integral may be expressed as the sum of two integrals, one for the path \(R_{1}\) and the other for the path \(R_{2}\) . Then, we have

\[R_{1}\int_{i}^{f}\frac{\mathrm{d}Q}{T} +\int_{R_{2}}\int_{f}^{i}\frac{\mathrm{d}Q}{T} = 0,\] \[R_{1}\int_{i}^{f}\frac{\mathrm{d}Q}{T} = -\int_{R_{2}}\int_{f}^{i}\frac{\mathrm{d}Q}{T}.\] 

or

Since \(R_{2}\) is a reversible path,

===== Page 10 =====

**FIGURE 8-3** Two reversible paths joining two equilibrium states of a system. The diagram shows Generalized force \(Y\) on the vertical axis and Generalized displacement \(X\) on the horizontal axis. Two points, \(i\) and \(f\), are shown connected by two different reversible paths \(R_1\) and \(R_2\).

\[-\int_{R_{2}}^{i}\frac{\mathrm{d}Q}{T} = \int_{R_{2}}^{f}\frac{\mathrm{d}Q}{T},\] \[\displaystyle \int_{R_{1}}^{f}\frac{\mathrm{d}Q}{T} = \int_{R_{2}}^{f}\frac{\mathrm{d}Q}{T}.\]

and, finally,

Since \(R_{1}\) and \(R_{2}\) were chosen at random and represent any two reversible paths, the above equation expresses the important fact that \(R_{i}\int_{i}^{f}\mathrm{d}Q / T\) is independent of the reversible path connecting \(i\) and \(f\) . Therefore, it follows from Eq. (8.4) that there exists a function of the thermodynamic coordinates of a system whose value at the final state minus its value at the initial state equals the integral \(R_{i}\int_{i}^{f}\mathrm{d}Q / T\) . This state function was named the entropy by Rudolf Clausius in 1865 and is denoted by \(S\) . If \(S_{i}\) is the entropy at the initial state and \(S_{f}\) the entropy at the final state, then we have a finite change of entropy \(S_{f} - S_{i}\) from state \(i\) to state \(f\) , given by

\[S_{f} - S_{i} = \int_{R_{i}}^{f}\frac{\mathrm{d}Q}{T}, \quad (8.5)\]

where the path from state \(i\) to state \(f\) is any reversible path \(R\) . Thus, the entropy change of the system between states \(i\) and \(f\) is independent of the path. This is a very remarkable result. Although the heat entering the system depends on the path between the states \(i\) and \(f\) , the entropy change does not depend on the path.

The existence of an entropy function \(S\) is deduced in the same way as that of the internal- energy function \(U\) , that is, by showing that a certain quantity is independent of choice of reversible processes connecting the initial equilibrium

===== Page 11 =====

state with the final equilibrium state. Both \(U\) and \(S\) are state functions, which means that the difference of either function evaluated at the final and initial equilibrium states is independent of the path connecting the two states. In neither function, however, does the defining equation enable us to calculate a single value of the function, only the difference of two values.

If the two equilibrium states \(i\) and \(f\) are infinitesimally near, then the integral sign may be eliminated and \(S_{f} - S_{i}\) becomes \(dS\) , an infinitesimal change of entropy of the system. Equation (8.5) then becomes

\[dS = \frac{\mathrm{d}Q_{R}}{T}, \quad (8.6)\]

where \(dS\) is an exact differential, since it is the differential of an actual function and not a small inexact quantity, such as \(\mathrm{d}Q\) or \(\mathrm{d}W\) . The subscript \(R\) to \(\mathrm{d}Q\) indicates that the preceding equation is true only if a small amount of heat \(\mathrm{d}Q\) is transferred reversibly.

When Eq. (8.6) is written in the form \(\mathrm{d}Q_{R} = T d S\) , it is seen that the difficulty of dealing with the inexact differential of heat is eliminated by substituting the product of the temperature and exact differential of the entropy. This is a major advancement in the formalism of thermodynamics, comparable to replacing \(\mathrm{d}W\) with \(- P d V\) in a hydrostatic system. Entropy \(S\) joins \(P\) , \(V\) , and \(T\) as a thermodynamic variable to be used in the development of the formalism and mathematical methods of thermodynamics.

It is instructive to calculate a unit of entropy, a joule per kelvin, in order to gain a feeling for this new variable. Consider the Joule paddle wheel apparatus shown in Fig. 8- 4. The system is a kilogram of water at room temperature \(T\) . The surroundings are the adiabatic cylindrical wall and top, the diathermic bottom in contact with a heat reservoir, also at temperature \(T\) , and the paddle wheels. A slowly falling mass \(m\) causes the paddle wheels to turn, so the portion of the boundary formed by the paddle wheels moves. The falling mass does work on the system, which tends to experience an increase in the temperature of the water. However, the diathermic bottom prevents the temperature from rising by removing energy from the system in the form of heat.

===== Page 12 =====

192 PART I: Fundamental Concepts

**FIGURE 8-4** Joule paddle wheel apparatus, an "entropy generator." A diagram shows a container with water and a paddle wheel inside, driven by a falling mass \(m\) via a pulley. The container is surrounded by adiabatic walls except for a diathermic bottom resting on a room-temperature reservoir.

The change of entropy of the reservoir \(\Delta S\) is given by

\[\Delta S = \int \frac{\mathrm{d}Q_{R}}{T} = \frac{Q}{T},\]

which is also the total change of entropy for the composite system of liquid plus reservoir, since the state of the water in the apparatus is unchanged at the end of the process. Furthermore, since the temperature of the water and the volume of the water are both unchanged, the internal energy is unchanged. Thus, the work done by the falling mass equals the heat that enters the reservoir. If the paddle wheel is driven by a mass of \(29.9 \mathrm{kg}\) (approximately \(66 \mathrm{lb}\) ) that falls \(1 \mathrm{m}\) , then the change of entropy is given by

\[\Delta S = \frac{W}{T} = \frac{(29.9 \mathrm{kg})(9.8 \mathrm{N / kg})(1 \mathrm{m})}{293 \mathrm{K}}\] \[\qquad = 1.00 \mathrm{J / K}.\]

The entropy of the mass turning the paddle wheels is not changed during the process, because no heat enters or leaves the mass. Rather, the entropy is generated by the conversion of work (done by the mass) into heat (entering the reservoir). Thus, the paddle wheel apparatus serves as an entropy generator.

### 8.3 PRINCIPLE OF CARATHÉODORY

We have arrived at the mathematical formulation of the second law by the historical method initiated by the engineer Carnot and elaborated by the physicists Kelvin and Clausius. They thought in terms of practical engines, ideal engines, and physical models. Starting with a statement expressing the impossibility of converting heat completely into work, or the impossibility of spontaneous heat flow from a low- temperature body to a high- temperature body, they conceived of the ideal Carnot engine having maximum thermal efficiency. With the aid of this ideal engine, an absolute thermodynamic temperature scale was defined, and the Clausius theorem was proved. On the basis of Clausius' theorem, the existence of an entropy function was deduced. From a mathematical point of view, this procedure is somewhat unsatisfactory. Mathematicians often prefer an "axiomatic treatment," that is, a statement of the minimum number of fundamental axioms and then a purely formal mathematical deduction from these axioms.

===== Page 13 =====

In 1909, the mathematician Carathéodory sought to find a statement of the second law which, without the aid of Carnot engines and refrigerators but only by mathematical deduction, would lead to the existence of an entropy function satisfying the equation \(\mathrm{d}Q_{R} = T \mathrm{~d}S\) . He was led to his formulation of the second law by a mathematical theorem that he proved and which may be stated in simple form† as follows.

Imagine a space of three dimensions with rectangular coordinates \(x, y, z\) . Carathéodory's theorem states that, in the neighborhood of any arbitrary point \(P_{0}\) , there are points that are not accessible from \(P_{0}\) along solution curves of the equation

\[A(x,y,z)d x + B(x,y,z)d y + C(x,y,z)d z = 0,\]

if, and only if, the equation is integrable. The equation is said to be integrable if there exist functions \(\lambda (x,y,z)\) and \(F(x,y,z)\) such that

\[A d x + B d y + C d z = \lambda d F.\]

The proof of this purely mathematical theorem is somewhat involved and it will not be given here. It holds for any number of variables.

Let us now consider how this theorem has a bearing on thermodynamics. Consider a system whose states are determined, for the sake of argument, by three thermodynamic coordinates \(x, y\) , and \(z\) . Then, the first law in differential form may be written

\[\mathrm{d}Q = A d x + B d y + C d z,\]

where \(A, B\) , and \(C\) are functions of \(x, y\) , and \(z\) . The adiabatic, reversible transitions of this system are subject to the condition

\[\mathrm{d}Q = A d x + B d y + C d z = 0.\]

Let us now take as Carathéodory's statement of the second law the following:

In the neighborhood of any arbitrary initial state \(P_{0}\) of a physical system, there exist neighboring states that are not accessible from \(P_{0}\) along quasistatic adiabatic paths.

It follows from Carathéodory's theorem that his statement of the second law is possible if, and only if, there exist functions \(T\) and \(S\) such that

\[\mathrm{d}Q = A d x + B d y + C d z = T d S.\]

Thus, by stating the second law in terms of the inaccessibility of certain states by adiabatic paths, and by using a mathematical theorem, Carathéodory deduced the existence of an entropy function and an integrating factor connected with Kelvin temperature, which reassures us of the validity of Clausius

===== Page 14 =====

194 PART I: Fundamental Concepts

theorem. The difficulty with Caratheodory's statement of the second law is that no physical intuition is developed, as is in the study of the characteristics of heat engines.

### 8.4 ENTROPY OF THE IDEAL GAS

If a system absorbs an infinitesimal amount of heat \(\mathrm{d}Q_{R}\) during a reversible process, the entropy change of the system is given by Eq. (8.6),

\[dS = \frac{\mathrm{d}Q_{R}}{T}.\]

It is interesting to notice that, although \(\mathrm{d}Q_{R}\) is an inexact differential, the ratio \(\mathrm{d}Q_{R} / T\) is exact. The reciprocal of the absolute thermodynamic temperature is, therefore, the integrating factor of \(\mathrm{d}Q_{R}\) . If \(\mathrm{d}Q_{R}\) is expressed as a sum of differentials involving thermodynamic coordinates, then, upon dividing by \(T\) , the expression may be integrated and the entropy of the system obtained. As an example of this procedure, consider one of the expressions for \(\mathrm{d}Q_{R}\) of the ideal gas, namely, Eq. (5.10),

\[\mathrm{d}Q_{R} = C_{P}dT - VdP.\]

Dividing by \(T\) , we get

\[\frac{\mathrm{d}Q_{R}}{T} = C_{P}\frac{dT}{T} -\frac{V}{T} dP,\] \[dS = C_{P}\frac{dT}{T} -nR\frac{dP}{P}. \quad (8.7)\]

Let us now calculate the entropy change \(\Delta S\) of the ideal gas between an arbitrarily chosen reference state \(r\) with coordinates \(T_{r}, P_{r}\) , and any other state with coordinates \(T, P\) . Integrating between these two states, we get

\[\Delta S = \int_{T_{r}}^{T}C_{P}\frac{dT}{T} -nR\ln \frac{P}{P_{r}}.\]

Suppose we assign to the reference state an entropy \(S_{r}\) and choose any arbitrary numerical value for this quantity. Then, an entropy \(S\) may be associated with the other state where \(S - S_{r} = \Delta S\) . To make the discussion simpler, let \(C_{P}\) be constant. Then,

\[S - S_{r} = C_{P}\ln \frac{T}{T_{r}} -nR\ln \frac{P}{P_{r}},\]

and this may be rewritten

\[S = C_{P}\ln T - nR\ln P + (S_{r} - C_{P}\ln T_{r} + nR\ln P_{r}).\]

Denoting the quantity in parentheses by the constant \(S_{0}\) , we get, finally,

===== Page 15 =====

\[S = C_{P}\ln T - nR\ln P + S_{0}. \quad (8.8)\]

Substituting for \(T\) and \(P\) thousands of different values, we may calculate thousands of corresponding values of \(S\) , which form an entropy table. Any one value from this table, taken alone, will have no meaning. The difference between two values, however, will be an actual change of entropy.

Let us investigate the meaning of the standard state entropy \(S_{0}\) by returning to Eq. (8.7),

\[dS = C_{P}\frac{dT}{T} -nR\frac{dP}{P}.\]

Again, for simplicity, assuming \(C_{P}\) to be constant, we may take the indefinite integral and obtain

\[S = C_{P}\ln T - nR\ln P + S_{0},\]

where \(S_{0}\) is the constant of integration. This result is precisely Eq. (8.8) obtained previously by taking into account the reference state. We see that, in taking the indefinite integral of \(dS\) , we do not obtain an "absolute entropy," but merely an entropy referred to an unspecified reference state whose coordinates are contained within the constant of integration. The reference state is arbitrarily chosen, usually for convenience and practicality. Thus, chemists use \(0.1\mathrm{MPa}\) and \(25^{\circ}\mathrm{C}\) (298 K) as the reference state for chemical reactions; engineers use the triple point of water for steam processes; and physicists use \(0.1\mathrm{MPa}\) and absolute zero for low- temperature calculations. Once the reference state is chosen, the constant of integration \(S_{0}\) can be evaluated and entropy tables constructed.

Let us calculate the change of entropy of the ideal gas as a function of \(T\) and \(V\) by using the expression for \(\mathrm{d}Q_{R}\) of the ideal gas, namely, Eq. (5.8). Thus,

\[\frac{\mathrm{d}Q_{R}}{T} = C_{V}\frac{dT}{T} +\frac{P}{T} dV,\] \[dS = C_{V}\frac{dT}{T} +nR\frac{dV}{V},\]

and

where \(C_{V}\) is the heat capacity at constant volume. Integrating \(dS\) , we obtain

\[S = \int C_{V}\frac{dT}{T} +nR\ln V + S_{0}. \quad (8.9)\]

In terms of the molar specific heat at constant volume \(c_{V}\) , the change of entropy of the ideal gas between an initial state and final state is given by

\[\Delta S = n\int_{i}^{f}c_{V}\frac{dT}{T} +nR\ln \frac{V_{f}}{V_{i}}. \quad (8.10)\]

Similarly, for the change of entropy of an ideal gas as a function of \(T\) and \(P\) , we use Eq. (8.7) to obtain

===== Page 16 =====

196 PART I: Fundamental Concepts

\[\Delta S = n\int_{i}^{f}c_{P}\frac{dT}{T} +nR\ln \frac{P_{f}}{P_{i}}, \quad (8.11)\]

where \(c_{P}\) is the molar specific heat at constant pressure.

### 8.5 TS DIAGRAM

For every infinitesimal amount of heat that enters a system during an infinitesimal portion of a reversible process, there is an equation

\[\mathrm{d}Q_{R} = T d S.\]

It follows, therefore, that the total amount of heat transferred in a reversible process is given by

\[Q_{R} = \int_{i}^{f}T d S.\]

This integral can be interpreted graphically as the area under a curve on a diagram in which \(T\) is plotted along the \(y\) - axis and \(S\) along the \(x\) - axis, a so- called "TS diagram." The shape of the curve on the TS diagram is determined by the kind of reversible process that the system undergoes. Obviously, an isothermal process is a horizontal line, but in the case of a reversible adiabatic process, we have

\[dS = \frac{\mathrm{d}Q_{R}}{T}.\]

Also, for an adiabatic process,

\[\mathrm{d}Q = 0.\]

So, if \(T\) is not zero, then

\[dS = 0,\]

and \(S\) is constant. Therefore, during a reversible adiabatic process, the entropy of a system remains constant, or, in other words, the system undergoes an isentropic process. An isentropic process on a \(TS\) diagram is obviously a vertical line, called an "isentrope." Also obvious is that an isothermal process on a \(TS\) diagram is a horizontal line, called an "isotherm."

It is clear that the two isothermal and the two adiabatic processes that make up any Carnot cycle form a rectangle on a \(TS\) diagram, regardless of the nature of the working substance, unlike the many shapes found in work diagrams for the heat engines in Chaps. 6 and 7. It was with this knowledge that we represented a Carnot engine symbolically as a rectangle in Figs. 7- 5 and 7- 7. Only reversible processes may be plotted on a \(TS\) diagram, because of the definition of entropy in Eq. (8.6). The \(TS\) diagram is particularly convenient

===== Page 17 =====

for representing all the idealized reversible cycles for various heat engines. The closed curve shown in Fig. 8- 5 consisting of an upper portion \(R_{1}\) and a lower portion \(R_{2}\) represents any reversible engine cycle that is not a Carnot cycle. The area under \(R_{1}\) (positive area) is equal to the positive heat \(Q_{1}\) absorbed by the system, and the area under \(R_{2}\) (negative area) is equal to the negative heat \(Q_{2}\) rejected by the system. The area inside the closed curve is, therefore, \(Q_{1} - Q_{2}\) , or \(W\) . The thermal efficiency of the engine is \(W / Q_{1}\) , which may be measured directly from the diagram.

Other processes are also plotted on a TS diagram. For a reversible isobaric process, the curve has a slope that follows from Eq. (8.7) by imposing constant pressure; thus,

\[\left(\frac{\partial T}{\partial S}\right)_{P} = \frac{T}{C_{P}}. \quad (8.12)\]

Similarly, by imposing the condition of constant volume on the equation preceding Eq. (8.9), the slope of a reversible isochoric process is given by

\[\left(\frac{\partial T}{\partial S}\right)_{V} = \frac{T}{C_{V}}. \quad (8.13)\]

The slopes given by Eqs. (8.12) and (8.13) are independent of the nature of the hydrostatic system, because the requirement of constant pressure and constant volume eliminated the equation of state of the ideal gas used in Eqs. (8.7) and

**FIGURE 8-5** An arbitrary reversible cycle on a TS diagram. The area under upper portion \(R_{1}\) equals the positive heat \(Q_{1}\) absorbed by the system; the area under lower portion \(R_{2}\) equals the negative heat \(Q_{2}\) rejected by the system. The Carnot cycle for the same system would be represented by a rectangle enclosing the closed curve. The diagram shows Temperature \(T\) on the vertical axis and Entropy \(S\) on the horizontal axis. A closed loop is drawn with an upper path \(R_1\) and a lower path \(R_2\).

===== Page 18 =====

198 PART I: Fundamental Concepts

**FIGURE 8-6** Curves representing reversible processes of a hydrostatic system on a TS diagram. The diagram shows Temperature \(T\) on the vertical axis and Entropy \(S\) on the horizontal axis. Four types of curves are shown: an isentrope (vertical line), an isochor, an isobar, and an isotherm (horizontal line).

### 8.6 ENTROPY AND REVERSIBILITY

In order to understand the physical meaning of entropy and its significance, it is necessary to study all the entropy changes that take place when a system undergoes a reversible process. If we calculate the entropy change of the system and add the calculated entropy change of the surroundings, then we obtain the sum of the entropy changes brought about by this particular process. We may call this sum the entropy change of the universe due to the process in question.

When a finite amount of heat is absorbed or rejected by a reservoir, extremely small changes in the coordinates occur in every unit of mass of the reservoir. The entropy change of a unit of mass is, therefore, very small. However, since the total mass of a reservoir is large, the total entropy change of the reservoir is finite. Suppose that a reservoir is in contact with a system and that heat \(Q\) is absorbed irreversibly by the reservoir at the temperature \(T\) . The reservoir undergoes nondissipative changes determined entirely by the quantity of heat absorbed. Exactly the same changes in the reservoir would occur if the same amount of heat \(Q\) were transferred reversibly. Hence, the entropy change of the reservoir is \(Q / T\) . Therefore, whenever a reservoir absorbs heat \(Q\) at the temperature \(T\) from any system during any kind of process, the entropy change of the reservoir is \(Q / T\) .

Consider now the entropy change of the universe that is brought about by the performance of any reversible process. The process will, in general, be accompanied by a flow of heat between a system and a set of reservoirs ranging in temperature from \(T_{i}\) to \(T_{f}\) . During any infinitesimal portion of the process, an amount of heat \(\mathrm{d}Q_{R}\) is transferred between the system and one of the reservoirs at the temperature \(T\) . If \(\mathrm{d}Q_{R}\) is absorbed by the system, then

\[dS\mathrm{~of~the~system~} = +\frac{\mathrm{d}Q_{R}}{T},\] \[dS\mathrm{~of~the~reservoir~} = -\frac{\mathrm{d}Q_{R}}{T},\]

and the entropy change of the universe, which is the sum of these two changes, is zero. If \(\mathrm{d}Q_{R}\) is rejected by the system, then, obviously,

\[dS\mathrm{~of~the~system~} = -\frac{\mathrm{d}Q_{R}}{T},\] \[dS\mathrm{~of~the~reservoir~} = +\frac{\mathrm{d}Q_{R}}{T},\]

and the entropy change of the universe is again zero. If no heat is transferred, then \(\mathrm{d}Q_{R}\) is zero. Neither the system nor the reservoir will have an entropy change, and the entropy change of the universe is still zero. Since there is no infinitesimal entropy change of the universe for any infinitesimal portion of the reversible process, then there is no entropy change for all such portions. In general, the change of entropy of the universe is zero for a reversible process. In other words, when a reversible process is performed, the entropy of the universe remains unchanged. However, all natural processes are irreversible and only ideal processes are reversible.

### 8.7 ENTROPY AND IRREVERSIBILITY

During an irreversible process, there is a different situation for the entropy change of the universe. When a system undergoes an irreversible process between an initial equilibrium state and a final equilibrium state, the irreversible process is replaced by a reversible one. This replacement is permitted when the initial and the final state of the system are equilibrium states. No integration is performed over the original irreversible path, because the path is not known. The entropy change of the system is equal to

\[S_{f} - S_{i} = \int_{R}^{f}\frac{\mathrm{d}Q}{T},\]

where \(R\) indicates any arbitrarily chosen reversible process by which the system is brought from the given initial state to the given final state of the irreversible process. When either the initial or the final state is a nonequilibrium state, special methods must be used, which will discussed in Sec. 8.10. For the

===== Page 19 =====

200 PART I: Fundamental Concepts

present, we shall limit ourselves to irreversible processes, all of which involve initial and final states of equilibrium.

### Processes exhibiting external mechanical irreversibility

(a) Examples are those processes involving the isothermal dissipation of work through a system (which remains unchanged) into internal energy of a reservoir, such as:

1. Friction from two solids in contact with a reservoir.
2. Irregular stirring of a viscous liquid in contact with a reservoir (e.g., Joule paddle wheel apparatus).
3. Inelastic deformation of a solid in contact with a reservoir.
4. Transfer of charge through a resistor in contact with a reservoir.
5. Magnetic hysteresis of a material in contact with a reservoir.

In the case of any process involving the isothermal transformation of work \(W\) done by a system into internal energy of a reservoir, there is no entropy change of the system because the thermodynamic coordinates of the system do not change, as stated in Sec. 6.10. Heat \(Q\) is absorbed by the reservoir, where \(Q = W\) from the work done on the reservoir. Since the reservoir absorbs \(+Q\) units of heat at the temperature \(T\) , the entropy change of the reservoir is \(+Q / T\) or \(+W / T\) . The entropy change of the universe is, therefore, also \(+W / T\) , which is a positive quantity.

(b) Further examples are those processes involving the adiabatic dissipation of work into internal energy of a system open to the atmosphere, such as:

1. Friction from rubbing thermally insulated liquids.
2. Irregular stirring of a viscous thermally insulated liquid.
3. Inelastic deformation of a thermally insulated solid.
4. Transfer of charge through a thermally insulated resistor.
5. Magnetic hysteresis of a thermally insulated material.

In the case of any process involving the adiabatic transformation of work \(W\) into internal energy of a system whose temperature rises from \(T_{i}\) to \(T_{f}\) at constant atmospheric pressure, there is no flow of heat to or from the surroundings, and, therefore, the entropy change of the local surroundings is zero. To calculate the entropy change of the system, the original irreversible process must be replaced by a reversible one that will take the system from the given initial state (temperature \(T_{i}\) , pressure \(P\) ) to the final state (temperature \(T_{f}\) , pressure \(P\) ). Let us replace the irreversible performance of work by a reversible isobaric flow of heat from a series of reservoirs ranging in temperature from \(T_{i}\) to \(T_{f}\) . The entropy change of the system will then be

\[S_{f} - S_{i}(\mathrm{system}) = \int_{R}^{T_{f}}\frac{\mathrm{d}Q}{T}.\]

===== Page 20 =====

201

For an isobaric process,

\[\mathrm{d}Q = C_{P}dT,\]

and, so,

\[S_{f} - S_{i}(\mathrm{system}) = \int_{T_{i}}^{T_{f}}C_{P}\frac{dT}{T}.\]

Finally, if \(C_{P}\) is assumed not to be a function of temperature, then the entropy change of the system is

\[S_{f} - S_{i}(\mathrm{system}) = C_{P}\ln \frac{T_{f}}{T_{i}}. \quad (8.14)\]

Thus, the entropy change of the universe is also \(C_{P}\ln (T_{f} / T_{i})\) , which is a positive quantity.

Processes exhibiting internal mechanical irreversibility. Examples are those processes involving the transformation of internal energy of a system enclosed by adiabatic walls into mechanical energy and then back into internal energy again, such as:

1. Ideal gas rushing into a vacuum (free expansion, i.e., Joule expansion).
2. Gas flowing through a porous plug (throttling process, i.e., Joule-Thomson expansion).
3. Snapping of a stretched wire after it is cut.
4. Collapse of a soap film after it is punctured.

In the case of a free expansion of the ideal gas, the entropy change of the local surroundings is zero, because there is no heat transfer through the adiabatic walls. In order to calculate the entropy change of the system, the free expansion must be replaced by a reversible process that will take the gas from its original state (volume \(V_{i}\) , temperature \(T\) ) to the final state (volume \(V_{f}\) , temperature \(T\) ), where temperature does not change for the ideal gas during expansion. Evidently, the most convenient reversible process to replace the irreversible process, for the purpose of calculation, is a reversible isothermal expansion at the temperature \(T\) from a volume \(V_{i}\) to the volume \(V_{f}\) . The entropy change of the system is then

\[S_{f} - S_{i}(\mathrm{system}) = \int_{R}^{V_{f}}\frac{\mathrm{d}Q}{T}.\]

For an isothermal process of the ideal gas,

\[\mathrm{d}Q_{R} = P d V,\]

and

\[\frac{\mathrm{d}Q_{R}}{T} = n R \frac{d V}{V},\]

which yields, for the entropy change of the system,

===== Page 21 =====

202 PART I: Fundamental Concepts

\[S_{f} - S_{i}(\mathrm{system}) = nR\ln \frac{V_{f}}{V_{i}}. \quad (8.15)\]

The entropy change of the universe is, therefore, \(nR\ln (V_{f} / V_{i})\) , which is a positive number.

Once again, we see that the entropy of the universe, which is the system, has increased, even though no heat entered or left the system. This result may seem puzzling, because entropy is defined in terms of the heat entering or leaving a system. The puzzle is resolved by recognizing that the free expansion of the ideal gas within an adiabatic container is not a reversible process. During an irreversible process, the entropy change of the universe, even if the process is adiabatic, is always positive.

Processes exhibiting external thermal irreversibility. Examples are those processes involving a transfer of heat by virtue of a finite temperature difference, such as:

1. Conduction or radiation of heat from a system to its cooler surroundings.
2. Conduction or radiation of heat through a system (which remains unchanged) from a hot reservoir to a cooler one.

In the case of the conduction of \(Q\) units of heat from one end to the other end of a system (which remains unchanged) from a hotter reservoir at \(T_{1}\) to a cooler reservoir at \(T_{2}\) , the following steps are obvious:

\[S_{f} - S_{i}(\mathrm{system}) = 0.\]

\[S_{f} - S_{i}(\mathrm{hotter~reservoir}) = -\frac{Q}{T_{1}}.\]

\[S_{f} - S_{i}(\mathrm{cooler~reservoir}) = +\frac{Q}{T_{2}}.\]

\[S_{f} - S_{i}(\mathrm{universe}) = \frac{Q}{T_{2}} -\frac{Q}{T_{1}}. \quad (8.16)\]

The entropy change of the universe is positive, because \(T_{2}\) is less than \(T_{1}\) .

Processes exhibiting chemical irreversibility. Examples are those processes involving a spontaneous change of internal structure, density, chemical composition, etc., such as:

1. Diffusion of two dissimilar inert ideal gases.
2. Mixing of alcohol and water.
3. Osmosis.
4. Freezing of supercooled liquid.
5. Condensation of a supersaturated vapor.
6. Dissolution of a solid in water.
7. A chemical reaction.

===== Page 22 =====

Assume that the diffusion of two dissimilar inert ideal gases is equivalent to two separate free expansions in an adiabatic enclosure with chambers of equal volume. For one of the gases, the change of entropy is given by Eq. (8.15),

\[S_{f} - S_{i} \text{(system)} = nR \ln \frac{V_{f}}{V_{i}},\]

namely,

\[S_{f} - S_{i} \text{(one gas)} = nR \ln \frac{V_{f}}{V_{i}},\]

which is a positive number, because \(V_{f} / V_{i} > 1\) . The other half of the system experiences the same entropy change. Since there is no entropy change of the reservoir, the entropy change of the universe is

\[S_{f} - S_{i} \text{(universe)} = 2nR \ln \frac{V_{f}}{V_{i}}, \quad (8.17)\]

which is a positive number. In general, the change of entropy is positive for any irreversible process. All the results of this section are summarized in Table 8.1.

**TABLE 8.1** Entropy change of the universe due to natural processes

| Type of irreversibility | Irreversible process | Entropy change of the system | Entropy change of the local surroundings | Entropy change of the universe |
| :--- | :--- | :--- | :--- | :--- |
| External mechanical irreversibility | Isothermal dissipation of work through a system into internal energy of a reservoir | 0 | \(W/T\) | \(W/T\) |
| Internal mechanical irreversibility | Adiabatic dissipation of work into internal energy of a system | \(C_P \ln T_f/T_i\) | 0 | \(C_P \ln T_f/T_i\) |
| Internal mechanical irreversibility | Free expansion of an ideal gas | \(nR \ln V_f/V_i\) | 0 | \(nR \ln V_f/V_i\) |
| External thermal irreversibility | Transfer of heat through a medium from a hotter to a cooler reservoir | 0 | \(Q/T_2 - Q/T_1\) | \(Q/T_2 - Q/T_1\) |
| Chemical irreversibility | Diffusion of two dissimilar inert ideal gases | \(2nR \ln V_f/V_i\) | 0 | \(2nR \ln V_f/V_i\) |

===== Page 23 =====

### 8.8 IRREVERSIBLE PART OF THE SECOND LAW

The first part of the second law considered only reversible processes. The second part deals with irreversible processes. Recall that for a reversible cycle, Eq. (8.3) states that

\[\oint_{R}\frac{\mathrm{d}Q}{T} = 0 \quad (\mathrm{reversible}). \quad (8.3)\]

Let us consider an irreversible cycle and calculate its closed integral. Figure 8- 7 shows a high- temperature reservoir at \(T_{1}\) supplying a small quantity of heat \(\mathrm{d}Q_{1}\) to an auxiliary reversible engine \(R\) . The purpose of \(R\) is to provide reversible heat for the irreversible engine \(I\) . Engine \(R\) rejects a small amount of heat \(\mathrm{d}Q\) at temperature \(T\) that is supplied to the irreversible engine \(I\) . Engine \(I\) does a small amount of work \(\mathrm{d}W\) during an irreversible cycle, so the combined system of engine \(R\) and engine \(I\) also performs an irreversible cycle. The net work of the combined system, according to the first law, equals \(\oint \mathrm{d}Q_{1}\) . But the net work cannot be positive, according to the Kelvin- Planck statement of the second law, since the combined system exchanges heat with a single reservoir. So, \(\oint \mathrm{d}Q_{1}\) cannot be positive. Moreover, if \(\oint \mathrm{d}Q_{1}\) equals zero, then, at the end of the cycle, engine \(I\) and its surroundings have returned to their original state. This result, however, is contrary to the irreversibility of engine \(I\) . So, we conclude,

\[\oint_{R}\mathrm{d}Q_{1}< 0; \quad (8.18)\]

that is, engine \(I\) generates heat that flows out of the system. From the definition of the thermodynamic temperature scale, Eq. (7.6), we have, in differential form for reversible engine \(R\) ,

**FIGURE 8-7** A high- temperature reservoir at temperature \(T_{1}\) supplies heat \(\mathrm{d}Q_{1}\) to an auxiliary reversible engine \(R\) . Irreversible engine \(I\) receives heat \(\mathrm{d}Q\) at temperature \(T\) , even though the system was initially at temperature \(T^{\prime}\) . The diagram shows a reservoir at \(T_1\) at the top, supplying \(\mathrm{d}Q_1\) to a reversible engine \(R\). \(R\) then supplies \(\mathrm{d}Q\) to an irreversible engine \(I\) at temperature \(T\). \(I\) does work \(\mathrm{d}W\).

===== Page 24 =====

204 PART I: Fundamental Concepts

\[\frac{\mathrm{d}Q_{1}}{T_{1}} = \frac{\mathrm{d}Q}{T},\] \[dQ_{1} = \frac{T_{1}}{T} dQ.\]

or

Substituting into Eq. (8.18), we get

\[\oint \frac{\mathrm{d}Q}{T} < 0. \quad (8.19)\]

This result is Clausius' inequality, which is valid for any cycle that is partially or wholly irreversible. If the cycle is reversible, the equality sign holds. Combining Eqs. (8.19) and (8.3), we obtain

\[\oint \frac{\mathrm{d}Q}{T} \leq 0. \quad (8.20)\]

This is the complete mathematical statement of the second law.

### 8.9 HEAT AND ENTROPY IN IRREVERSIBLE PROCESSES

In order to relate change of entropy to heat in irreversible processes, consider a cycle in which a system begins in an initial equilibrium state \(i\) , passes during an irreversible process \(I\) to a final equilibrium state \(f\) , and then returns by a reversible process \(R\) to the initial state \(i\) , as shown in Fig. 8- 8. Since entropy is a state function, its closed integral is always zero:

\[\oint dS = \int_{I}\int_{i}dS + \int_{R}\int_{f}dS = 0. \quad (8.22)\]

From Eq. (8.20) we obtain

\[\oint \frac{\mathrm{d}Q}{T} = \int_{I}\int_{i}\frac{\mathrm{d}Q}{T} +\int_{R}\int_{f}\frac{\mathrm{d}Q}{T} < 0. \quad (8.23)\]

From Eq. (8.6), the definition of entropy, we can write

**FIGURE 8-8** An irreversible process followed by a reversible process to complete an irreversible cycle. The diagram shows Temperature \(T\) on the vertical axis and Entropy \(S\) on the horizontal axis. An irreversible path \(I\) goes from point \(i\) to point \(f\) (indicated by a shaded band). A reversible path \(R\) returns from \(f\) to \(i\).

===== Page 25 =====

\[R\int_{i}^{f}\frac{\mathrm{d}Q}{T} = \int_{R}^{f}dS.\]

Subtract Eq. (8.23) from Eq. (8.22) and substitute the equation cited above; then,

\[\int_{i}^{f}d S - \int_{i}^{f}\frac{\mathrm{d}Q}{T} >0,\] \[\int_{i}^{f}d S > \int_{i}^{f}\frac{\mathrm{d}Q}{T}, \quad (8.24)\]

or

which means that the change of entropy during an irreversible process is greater than the integral of the heat divided by the temperature of the auxiliary reservoirs.

For small changes in state, Eq. (8.24) can be written

\[dS_{I} > \left(\frac{\mathrm{d}Q}{T}\right)_{I}. \quad (8.25)\]

In general, we have

\[dS\geq \frac{\mathrm{d}Q}{T}, \quad (8.26)\]

where the equality applies to reversible processes and the inequality applies to irreversible processes.

Various expressions for conditions involving entropy require careful consideration. According to the definition of entropy in Eq. (8.6),

\[dS = \frac{\mathrm{d}Q_{R}}{T},\]

the change in entropy in a reversible and adiabatic process ( \(\mathrm{d}Q_{R} = 0\) ) is zero. Thus, the term reversible adiabatic implies the term isentropic. Isentropic, however, does not necessarily imply reversible adiabatic. For an isentropic process, in general, we have

\[dS = 0.\]

Substituting Eq. (8.26) into this expression, we have

\[\frac{\mathrm{d}Q}{T}\leq 0.\]

It follows that for an isentropic process, either

\[\mathrm{d}Q = 0\qquad \mathrm{(reversible)},\]

or

\[\mathrm{d}Q< 0\qquad \mathrm{(irreversible)}.\]

Thus, reversible isentropic implies adiabatic, and isentropic adiabatic implies reversible. But, irreversible isentropic is not adiabatic ( \(\mathrm{d}Q< 0\) ) and implies that heat flows out of the system. Of course, if the process is irreversible adiabatic,

===== Page 26 =====

208 PART I: Fundamental Concepts

then it is not isentropic ( \(T\) not constant) and implies that the temperature increases. Finally, if the process is isentropic adiabatic, then it is not irreversible \((\mathrm{d}Q_{R} = 0)\) and implies that the process is reversible.

### 8.10 ENTROPY AND NONEQUILIBRIUM STATES

The calculation of the entropy changes associated with the irreversible processes discussed in Sec. 8.7 presented no special difficulties because, in all cases, the system either did not change at all (in which case, only the entropy changes of reservoirs had to be calculated) or both the initial and final states of a system were equilibrium states that could be connected by a suitable reversible process. Consider, however, the following process involving internal thermal irreversibility with equilibrium only in the final state. A thermally conducting bar has a nonuniform temperature distribution by connecting one end to a high- temperature reservoir and the other end to a low- temperature reservoir. The bar is removed from the reservoirs and is then thermally insulated with adiabatic walls at constant pressure. An internal flow of heat will finally bring the bar to a uniform temperature, so the irreversible process will be from an initial nonequilibrium state to a final equilibrium state. It is obviously impossible to replace the irreversible process with a reversible process, because the initial state is a nonequilibrium state. What meaning, therefore, may be attached to the entropy change associated with this irreversible process?

Let us consider a bar to be composed of an infinite number of infinitesimally thin slices (volume elements), each of which has a different initial temperature but all of which have the same final temperature. Suppose we imagine that all the slices are insulated from one another and all are kept at the same pressure, and then each slice is put in contact successively with a series of reservoirs ranging in temperature from the initial temperature of the particular section to the common final temperature. This model defines an infinite number of reversible isobaric processes for each slice, which may be used to take each slice of the system from its initial nonequilibrium state to its final equilibrium state. We shall now define the entropy change as the result of integrating \(\mathrm{d}Q / T\) over all of these reversible processes. In other words, in the absence of one reversible process to take the system from \(i\) to \(f\) , we conceive of an infinite number of reversible processes for each volume element.

Consider a uniform bar of length \(L\) as depicted in Fig. 8- 9. A typical volume element at \(x\) has a mass

\[d m = \rho A d x,\]

where \(\rho\) is the density and \(A\) is the cross- sectional area of the bar. The heat capacity of the volume element is

===== Page 27 =====

**FIGURE 8-9** Process exhibiting internal thermal irreversibility. A diagram shows a bar of length \(L\) with an initial temperature distribution linear from \(T_0\) at \(x=0\) to \(T_L\) at \(x=L\).

\[c_{P} d m = c_{P}\rho A d x.\]

Let us suppose that the initial temperature distribution is linear along the length of the bar, so that the volume element at \(x\) has an initial temperature

\[T_{i} = T_{0} - \frac{T_{0} - T_{L}}{L} x,\]

where the temperature is \(T_{0}\) at \(x = 0\) , and \(T_{L}\) at \(x = L\) . If no heat is lost and if we assume for the sake of simplicity that the thermal conductivity, density, and heat capacity of all volume elements remain constant, then the final temperature of the entire length of the bar will be

\[T_{f} = \frac{T_{0} + T_{L}}{2}.\]

Integrating \(\mathrm{d}Q / T\) over a reversible isobaric transfer of heat between a particular volume element and a series of reservoirs ranging in temperature from \(T_{i}\) to \(T_{f}\) , we get, for the entropy change of this one volume element,

\[S_{f} - S_{i}\mathrm{~(volume~element)~} = c_{P}\rho A d x\int_{T_{i}}^{T_{f}}\frac{d T}{T}\] \[\qquad = c_{P}\rho A d x\ln \frac{T_{f}}{T_{i}}\] \[\qquad = c_{P}\rho A d x\ln \frac{T_{f}}{{\cal T}_{0} - \frac{T_{0} - T_{L}}{L}}x\] \[\qquad = -c_{P}\rho A d x\ln \left(\frac{T_{0}}{T_{f}} -\frac{T_{0} - T_{L}}{L T_{f}} x\right).\]

Upon integrating over the whole bar, the total entropy change of the system is

\[S_{f} - S_{i}\mathrm{~(system)~} = -c_{P}\rho A\int_{0}^{L}\ln \left(\frac{T_{0}}{T_{f}} -\frac{T_{0} - T_{L}}{L T_{f}} x\right)d x,\]

which, after integration and simplification, becomes

\[S_{f} - S_{i}\mathrm{~(system)~} = C_{P}\left[1 - \ln \left(\frac{T_{L}}{T_{f}}\right) + \frac{T_{0}}{T_{0} - T_{L}}\ln \left(\frac{T_{L}}{T_{0}}\right)\right]. \quad (8.27)\]

Since the bar is enclosed by an adiabatic enclosure, there is no entropy change of the surroundings. Hence, the entropy change of the universe is also given by Eq. (8.27). In order to show that the entropy change is positive, let us take a convenient numerical case, such as \(T_{0} = 400 \mathrm{~K}\) , \(T_{L} = 200 \mathrm{~K}\) ; hence, \(T_{f} = 300 \mathrm{~K}\) . Then,

\[S_{f} - S_{i}\mathrm{~(universe)~} = C_{P}(1 - \ln \frac{2}{3} +2\ln \frac{1}{2}) = C_{P}(1 + \ln 3 - 3\ln 2)\] \[\qquad = 0.018C_{P},\]

where it is seen that entropy and heat capacity have the same units: joule per kelvin.

The same method may be used to compute the entropy change of a system during a process from an initial nonequilibrium state, characterized by a nonuniform pressure distribution, to a final equilibrium state where the pressure is uniform. Examples of such processes are given in the problems at the end of the chapter.

### 8.11 PRINCIPLE OF INCREASE OF ENTROPY

The entropy change of the universe was found to be positive for each of the irreversible processes treated so far. We are led to believe, therefore, that

===== Page 28 =====

**FIGURE 8-10** A cycle that contradicts the second law unless \(S_{f} > S_{i}\) . The diagram shows Generalized force \(Y\) on the vertical axis and Generalized displacement \(X\) on the horizontal axis. An irreversible adiabatic path goes from \(i\) to \(f\). A reversible adiabatic path goes from \(f\) to \(k\). A reversible isothermal path at \(T'\) with heat \(Q\) goes from \(k\) to \(j\), and a reversible adiabatic path returns from \(j\) to \(i\).

1. Let the initial state of the system be represented by the point \(i\) on the generalized work diagram of Fig. 8-10, and suppose that the system undergoes an irreversible adiabatic process to the state \(f\) . Then the entropy change is

\[\Delta S = S_{f} - S_{i}. \quad (8.28)\]

A temperature change may or may not have occurred in the system. Whether or not, let us cause the system to undergo a reversible adiabatic process \(f \rightarrow k\) in a sequence of steps that brings the temperature of the system to the temperature of any arbitrarily chosen reservoir, say, at \(T'\) . Then, since \(S_{f} = S_{k}\) , Eq. (8.28) becomes

\[\Delta S = S_{k} - S_{i}. \quad (8.29)\]

Now, suppose that the system is brought into contact with the reservoir at \(T'\) and the system undergoes a reversible isothermal process \(k \rightarrow j\) until its entropy is the same in state \(j\) as in the initial state \(i\) . A final reversible adiabatic process \(j \rightarrow i\) will now bring the system back to its initial state with no change of entropy; and, since \(S_{j} = S_{i}\) , Eq. (8.29) becomes

\[\Delta S = S_{k} - S_{j}. \quad (8.30)\]

The only heat transfer \(Q_{R}\) occurred in the cycle during the reversible isothermal process \(k \rightarrow j\) , where

\[Q_{R} = T^{\prime}(S_{j} - S_{k}).\]

A net amount of work \(W\) has been done in the cycle, where

\[W = Q_{R}.\]

It is clear from the second law of thermodynamics that the heat \(Q_{R}\) cannot have entered the system, that is, \(Q_{R}\) cannot be positive, for then we would have a cyclic process where the only effect would be the absorption of heat from a single reservoir and the performance of an equivalent amount of work. Therefore, \(Q_{R} \leq 0\) , and

\[T^{\prime}(S_{j} - S_{k}) \leq 0,\]

and, finally, since the process went from state \(k\) to state \(j\)

\[T^{\prime}(S_{k} - S_{j}) \geq 0.\]

However, \(T^{\prime} \geq 0\) , so

\[S_{k} - S_{j} = \Delta S \geq 0. \quad (8.31)\]

2. If we assume that the original irreversible adiabatic process occurred without any change in entropy, then it would be possible to bring the system back to \(i\) by means of one reversible adiabatic process. Moreover, since the net heat transferred in this cycle is zero, the net work would also be zero. Therefore, under these circumstances, the system and its surroundings would have been restored to their initial states without producing changes elsewhere, which implies that the original process was reversible. Since this is contrary to our original assertion that the process was irreversible, the entropy of the system cannot remain unchanged. Therefore,

\[\Delta S > 0, \quad (8.32)\]

because the entropy change could not have decreased.

3. Let us now suppose that the system is not homogeneous and not at uniform temperature and pressure and that it undergoes an irreversible adiabatic process in which mixing and chemical reaction may take place. First, we assume that the system may be subdivided into parts (each one infinitesimal, if necessary) and that it is possible to assign a definite temperature, pressure, composition, etc., to each part, so that each part shall have a definite entropy depending on its coordinates, so we may define the entropy changes of the whole system as the sum of the entropy changes of its parts. Second, if we assume that it is possible to take each part back to its initial state by means of the reversible processes described in 1 above, using the same reservoir for each part, then it follows that \(\Delta S\) of the whole system is positive.

===== Page 29 =====

It should be emphasized that we have had to make two assumptions, namely: (1) that the entropy change of a system may be defined by subdividing the system into parts and summing the entropy changes of these parts; and (2) that reversible processes may be found or imagined by which mixtures may be unmixed and reactions may be caused to proceed in the opposite direction. The justification for these assumptions rests, to a small extent, on experimental grounds. Thus, in a later chapter, there will be described a device involving semipermeable membranes whereby a mixture of two different inert ideal gases may be separated reversibly. A similar device through which a chemical reaction may be caused to proceed reversibly through any set of equilibrium states may also be conceived. Nevertheless, the main justification for these assumptions is that experiment completely agrees with the entropy principle, which states that the change of entropy of the universe increases in an irreversible process.

The behavior of the entropy of the universe as a result of any kind of process may now be represented simply:

\[\Delta S(\mathrm{universe})\geq 0,\]

where the equality sign refers to reversible processes and the inequality sign to irreversible processes. Equation (8.33) is a succinct statement of the second law of thermodynamics.

### 8.12 APPLICATION OF THE ENTROPY PRINCIPLE

We have seen that whenever irreversible processes occur, the entropy of the universe increases. In the actual operation of a machine, such as an engine or a refrigerator, it is often possible to calculate the sum of all the entropy changes. The fact that this sum is positive enables us to draw useful conclusions concerning the behavior of the machine. An important example from the field of low- temperature physics will illustrate the power and simplicity of the entropy principle. Suppose one wants to cool an object with a refrigerator to a desired low temperature, that is, to lower the temperature of a body of finite mass from the temperature \(T_{1}\) of its surroundings to any desired low temperature \(T_{2}\) . A refrigerator operating in a cycle between a reservoir at \(T_{1}\) and the body itself is utilized, and, after several complete cycles have been completed, a quantity of heat \(Q\) has been removed from the body, a quantity of work \(W\) has been supplied to the refrigerator, and a quantity of heat \(Q + W\) has been rejected to the reservoir, as shown in Fig. 8- 11. Listing the entropy changes, we have

**FIGURE 8-11** Operation of a refrigerator in lowering the temperature of a body from that of its surroundings \(T_{1}\) to any desired temperature \(T_{2}\) . The diagram shows a reservoir at \(T_1\) at the top, receiving heat \(Q+W\). A refrigerator in the middle receives work \(W\) and heat \(Q\) from a body at the bottom. The body's temperature is lowered from \(T_1\) to \(T_2\).

===== Page 30 =====

214 PART I: Fundamental Concepts

\[\Delta S \text{ of the body} = S_{2} - S_{1},\]

\[\Delta S \text{ of the refrigerant} = 0,\]

and

\[\Delta S \text{ of the reservoir} = \frac{Q + W}{T_{1}}.\]

Applying the entropy principle, we obtain

\[S_{2} - S_{1} + \frac{Q + W}{T_{1}} \geq 0.\]

Multiplying by \(T_{1}\) and transposing, we get

\[W \geq T_{1}(S_{1} - S_{2}) - Q.\]

It follows that the smallest possible value for \(W\) is

\[W(\min) = T_{1}(S_{1} - S_{2}) - Q.\]

If tables of the thermodynamic properties of the material are available, then a knowledge of the initial and final states is all that is needed to read from the tables the values of \(S_{1} - S_{2}\) and, if the body undergoes an isobaric process, the values of \(Q\) . The calculated value of \(W\) (min) is used to provide an estimate of the minimum cost of operation of the refrigerator.

### 8.13 ENTROPY AND DISORDER

When applied to an irreversible process, Eq. (8.33) is very unusual in being an inequality. Unlike most quantities in physics and chemistry, the change of entropy of the system and its surroundings is not conserved, rather, it increases. In order to appreciate the concept of entropy, let us consider various natural processes and look for insights that are consistent with calculations.

First- order phase changes are irreversible, isothermal processes that lend themselves to a descriptive discussion of entropy. For example, consider the phase change of sublimation, the transition of a solid to a vapor that occurs in dry ice. The change of entropy, which is the amount of heat absorbed during the sublimation divided by the sublimation temperature, increases as expected. But what can be said about the microscopic changes that occur when carbon dioxide molecules of dry ice escape from the solid into the vapor?

A solid is capable of supporting itself, whether in a crystalline state or amorphous state. Moreover, the material in the solid phase retains its size and shape, which means that the microscopic components (particles) of the system form a rigid structure. Simply stated, each particle retains its location in an organized structure; that is, the solid is in a state of order.

As latent heat is supplied to a solid, the process of sublimation changes the solid into a vapor with no change of temperature. A vapor has no fixed size and shape; in fact, a vapor must be placed in a closed container or it is lost. The particles in the vapor are not individually restrained into any organized structure; rather, the vapor particles are free to move independently throughout the volume of the container. In other words, the vapor is in a state of disorder, relative to its solid phase. An increase in entropy of a system can be described as an increase in the disorder of the system. Notice that the concept of disorder is relative to a reference state, just as entropy is.

The use of disorder as a synonym for entropy can be extended beyond phase transitions as the following examples show.

1. The temperature of an ideal gas does not change and heat is not added to the system during a free expansion, yet the entropy increases, as seen in Eq. (8.15). The only difference between the initial state and the final state of the ideal gas is an increase of volume, which provides the gas particles with more space for their motion. Disorder, in this case, is not linked to a structural change that provides freedom of movement, as in the case of sublimation, but, rather, more freedom of movement is provided in a larger volume.

2. When the temperature of a ferromagnetic material is raised above its Curie point, the material suddenly loses its ferromagnetism and becomes paramagnetic. In the microscopic picture, the magnetic moments of the ferromagnetic material are mostly aligned in one direction (ordered). At temperatures above the Curie point, the magnetic moments are randomly

===== Page 31 =====

216 PART I: Fundamental Concepts

oriented (disordered) to produce paramagnetic behavior. From a thermodynamic point of view, the entropy increases in the transition from ferromagnetism to paramagnetism.

3. In the case of conduction of heat through a metal bar from a high-temperature reservoir to a low-temperature reservoir, there is no change of phase, volume, or temperature of the conductor, but the entropy of the universe increases, as seen in Eq. (8.16). The internal energy becomes disordered in its passage between reservoirs, because the internal energy has been dissipated in the low-temperature reservoir and cannot be used to run a heat engine.

4. The entropy increases in an isothermal conversion of work into internal energy, which then flows into a heat reservoir, such as occurs with the Joule paddle wheel shown in Fig. 8.4. It has been emphasized that work is a macroscopic concept. Changes must be describable by macroscopic coordinates external to the system, although the internal situation may be discussed, at least in the equilibrium state. Haphazard motions of individual particles do not constitute work. Thus, during the isothermal dissipation of work into heat, the disorderly motion of the particles in the reservoir is increased. The process increases the entropy of the reservoir, since the system is unchanged.

All these examples, involving irreversible processes, show that the entropy of the universe increases. It is possible to regard all natural processes from the point of view of orderliness, and, in all cases, the result obtained is that isolated systems or systems plus surroundings experiencing irreversible processes proceed toward a state of greater disorder. The increase of entropy of the universe during natural processes is an expression of this tendency. Living processes, such as growth or decay, are natural processes that increase disorder, when both the system and surroundings are considered, but the calculation of the increase of entropy is not simple, even in idealized cases.

The concept of entropy has importance in the discussion of time, a topic usually avoided in thermodynamics. The increase of entropy (disorder) of a system and its surroundings occurs in all aging processes, whether in a living organism or in an inanimate system. There is no doubt which condition is prior in time: youth or maturity, green apple or overripe apple, structure or erosion. One condition always precedes the other; order precedes disorder. Entropy always increases during an aging process. So, in a metaphorical sense, entropy is the arrow of time. Furthermore, the arrow has only one direction: it points forward into the future. True, special relativity provides that the forward progress of time slows down when masses approach the speed of light. But, so far, there is no consensus that time can be reversed to move backward into the past.

===== Page 32 =====

### 8.14 EXACT DIFFERENTIALS

Experiment shows that internal energy is related to heat and work in the following equation,

\[dU = dW + dQ,\]

which is, of course, the first law of thermodynamics. Apart from the obvious observation that energy is conserved in all its forms, there are two other insights important for thermodynamics. First, the small quantities of heat and work are not differentials of a mathematical function; that is, they are inexact differentials. But, more importantly, the sum of two inexact differentials yields an exact differential! The mathematical problem is to convert the inexact differentials into exact differentials.

The situation for \(dW\) is solved in mechanics, where the generalized work is the product of the generalized force and the generalized displacement, as shown in Table 3.1 (p. 66). The situation for \(dQ\) is more complicated.

In order to clarify the notion of heat, the concept of temperature had first to be refined. That required a detailed discussion of thermometers, experimental temperature, and the second law of thermodynamics applied to the Carnot cycle. As a result, the concept of temperature was detached from experiment to become the theoretical absolute thermodynamic temperature. Furthermore, Clausius introduced a totally new concept based on his analysis of a reversible cycle composed of many infinitesimal Carnot cycles, namely, the concept of entropy. The union of the concepts of temperature and entropy produced a way to express the inexact differential of heat in terms of exact differentials,

\[dQ = TdS.\]

Now, the first law can be rewritten in usable mathematical form, as, for example, in a hydrostatic system,

\[dU = -PdV + TdS.\]

In some ways, the thermodynamics is complete now that the inexact differentials for work and heat have been replaced with exact differentials. The only other fundamental law in thermodynamics is the third law, which sets entropy to zero at absolute zero, rather than setting it to zero at an arbitrary state. The remainder of this book is devoted to developing more mathematical functions and methods to aid in the calculation of the thermodynamic quantities, and bringing in quantum mechanics in the calculation of statistical mechanical quantities.

===== Page 33 =====

### PROBLEMS

8.1. (a) Derive the expression for the efficiency of a Carnot engine directly from a TS diagram.

(b) Compare the efficiencies of cycles \(A\) and \(B\) of Fig. P8-1.

**FIGURE P8-1** The graph shows Temperature \(T\) on the vertical axis and Entropy \(S\) on the horizontal axis. Cycle A is a trapezoid defined by temperatures \(T_1\) and \(T_2\). Cycle B is a triangle defined by temperatures \(T_1\) and \(T_2\).

8.2. Prove that the slope on a TS diagram of:

(a) An isochoric curve is \(T / C_{V}\)

(b) An isobaric curve is \(T / C_{P}\)

8.3. Show that the partial derivatives given in Eqs. (8.12) and (8.13) are independent of the equation of state for the hydrostatic system.

8.4. Why does an isochoric curve plotted on a TS diagram have a greater slope than an isobaric curve at the same temperature?

8.5. Sketch TS diagrams for the following four ideal gas cycles: Otto; Diesel; a rectangle on a \(PV\) diagram; and a "right triangle" on a \(PV\) diagram in which the base is an isobaric, the altitude is an isochoric, and the "hypotenuse" is an adiabatic.

8.6. A current of \(10\mathrm{A}\) is maintained for 1 s in a resistor of \(25\Omega\) while the temperature of the resistor is kept constant at \(27^{\circ}C\)

(a) What is the entropy change of the resistor?

(b) What is the entropy change of the universe?

The same current is maintained for the same time in the same resistor, but now thermally insulated, with the same initial temperature. If the resistor has a mass of \(10\mathrm{g}\) and a specific heat of \(836\mathrm{J / kg}\cdot \mathrm{K}\)

(c) What is the entropy change of the resistor?

(d) What is the entropy change of the universe?

8.7. (a) One kilogram of water at \(273\mathrm{K}\) is brought into contact with a heat reservoir at \(373\mathrm{K}\) . When the water has reached \(373\mathrm{K}\) , what is the entropy change of the water, of the heat reservoir, and of the universe?

(b) If the water had been heated from 273 to \(373\mathrm{K}\) by first bringing it into contact with a reservoir at \(323\mathrm{K}\) and then with a reservoir at \(373\mathrm{K}\) , what would have been the entropy change of the universe?

===== Page 34 =====

8.8. A body of constant heat capacity \(C_{P}\) and at a temperature \(T_{i}\) is put in contact with a reservoir at a higher temperature \(T_{f}\) . The pressure remains constant while the body comes to equilibrium with the reservoir. Show that the entropy change of the universe is equal to

\[\Delta S = C_{P}[x - \ln (1 + x)],\]

where \(x = -(T_{f} - T_{i}) / T_{f}\) . Prove that the entropy change is positive.

8.9. The molar heat capacity at constant magnetic field of a paramagnetic solid at low temperatures varies with the temperature and field according to the relation

\[c_{\mathcal{H}} = \frac{B + C\mathcal{H}^{2}}{T^{2}} +D T^{2},\]

where \(B,C\) ,and \(D\) are constants. What is the entropy change of \(n\) moles of material when the temperature changes from \(T_{i}\) to \(T_{f}\) while \(\mathcal{H}\) remains constant at the value \(\mathcal{H}_{0}\)

8.10. According to Debye's law, the molar heat capacity at constant volume of a diamond varies with the temperature as follows:

\[c_{V} = 3R\frac{4\pi^{4}}{5}\left(\frac{T}{\Theta}\right)^{3}.\]

What is the entropy change in units of \(R\) of a diamond of \(1.2\mathrm{g}\) mass when it is heated at constant volume from 10 to \(350\mathrm{K}\) ? The molar mass of diamond is \(12\mathrm{g}\) ,and \(\Theta\) is \(2230\mathrm{K}\)

8.11. A thermally insulated cylinder, closed at both ends, is fitted with a frictionless heatconducting piston that divides the cylinder into two parts. Initially, the piston is clamped in the center with 1 liter of air at \(300\mathrm{K}\) and 2atm pressure on one side and 1 liter of air at \(300\mathrm{K}\) at 1 atm pressure on the other side. The piston is released and reaches equilibrium in pressure and temperature at a new position. Compute the final pressure and temperature and increase of entropy if air is assumed to be the ideal gas. What irreversible process has taken place?

8.12. An adiabatic cylinder, closed at both ends, is fitted with a frictionless adiabatic piston that divides the cylinder into two parts. Initially the pressure, volume, and temperature are the same on both sides of the piston \((P_{0},V_{0},\) and \(T_{0}\) ). The gas is ideal with \(C_{V}\) independent of temperature and \(\gamma = 1.5\) . By means of a heating coil in the gas on the left side, heat is slowly supplied to the gas on the left until the pressure reaches \(27P_{0} / 8\) . In terms of \(nR\) , \(V_{0}\) , and \(T_{0}\) :

(a) What is the final volume on the right side?
(b) What is the final temperature on the right side?
(c) What is the final temperature on the left side?
(d) How much heat must be supplied to the gas on the left side? (Note: Ignore the coil!)
(e) How much work is done on the gas on the right side?

===== Page 35 =====

8.13. Solve the problem of the uniform bar shown in Fig. 8-9 if only the hot reservoir is removed by showing that the entropy change of the universe is

\[\Delta S = C_P\left(1 + \frac{T_0 - T_L}{2T_L} -\frac{T_0}{T_0 - T_L}\ln \frac{T_o}{T_L}\right).\]

8.14. Calculate the entropy change of the universe as a result of the following processes:

(a) A copper block of \(0.4\mathrm{kg}\) mass and with heat capacity at constant pressure of \(150\mathrm{J / K}\) at \(100^{\circ}\mathrm{C}\) is placed in a lake at \(10^{\circ}\mathrm{C}\) .
(b) The same block at \(10^{\circ}\mathrm{C}\) is dropped from a height of \(100\mathrm{m}\) into the lake.
(c) Two such blocks at \(100^{\circ}\mathrm{C}\) and \(0^{\circ}\mathrm{C}\) are joined together.

8.15. What is the entropy change of the universe as a result of each of the following processes?

(a) A \(1 - \mu \mathrm{F}\) capacitor is connected to a \(100\mathrm{-V}\) electrochemical cell at \(0^{\circ}\mathrm{C}\)
(b) The same capacitor, after being charged to \(100\mathrm{V}\) , is discharged through a resistor kept at \(0^{\circ}\mathrm{C}\) .

8.16. An ideal- gas cycle suggested by A. S. Arrott of British Columbia, Canada, is shown in Fig. P8-2, where there are shown on a \(PV\) two isothermal curves intersected by an adiabatic curve, referring to 1 mol of an ideal monatomic gas. A process takes the gas from the upper intersection point \(A\) and expands it isothermally at \(600\mathrm{K}\) to a very special state \(B\) . The gas is then put in contact with a low- temperature reservoir at

**FIGURE P8-2** The zilch cycle for 1 mol of an ideal monatomic gas. (A. S. Arrott: American Journal of Physics, vol. 45, pp. 672- 673, 1977. See also R. H. Dickerson and J. Mottmann: American Journal of Physics, vol. 62, pp. 558- 562, 1994. ) The graph shows Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. Four points A, B, C, D are shown. Isotherms are at \(T_2 = 600 \mathrm{K}\) and \(T_1 = 300 \mathrm{K}\). An adiabat connects D to A. An isochor connects B to C.

===== Page 36 =====

300 K so that it cools isochorically to state \(C\) . Then, there is a further isothermal expansion from \(C\) to the lower intersection point \(D\) . The remainder of the zilch cycle is accomplished by an adiabatic compression from \(D\) back to \(A\) . The isochoric process \(BC\) is chosen to satisfy the condition that the net work in the cycle is zero.

(a) Calculate the work \(W_{DA}\) .

(b) Calculate the heat \(Q_{BC}\) .

(c) Calculate the net entropy change of the gas (not the reservoirs) and obtain the relationship

\[\frac{Q_{AB}}{600\mathrm{K}} +\frac{Q_{CD}}{300\mathrm{K}} = 8.64\frac{\mathrm{J}}{\mathrm{K}}.\]

(d) Calculate the work \(W_{AB}\) .

(e) Calculate the work \(W_{CD}\) .

(f) Calculate the net entropy change of the reservoirs.

(g) Draw the TS diagram.

8.17. (a) Prove that two isentropic curves do not intersect for systems of two independent variables.

(b) Show that isentropic curves do generally intersect for systems with more than two independent variables.

===== Page 37 =====

## CHAPTER 9

## PURE SUBSTANCES

### 9.1  P V DIAGRAM FOR A PURE SUBSTANCE

Since the triple point of water is the basis of the thermodynamic temperature scale, let us investigate pure water as an example of a pure substance. The experiment consists of measurements of \(P\) and \(V\) in states of equilibrium for \(\mathrm{H}_2\mathrm{O}\) either as a single phase or coexisting as multiple phases. The sample is placed in a cylinder, closed at one end, and contained by a piston. No mass is allowed to escape. Ovens and refrigerators control the temperature of the system. Movement of the piston provides independent control of the volume of the system. The pressure is measured by means of a manometer. A small window permits observation of the state of the sample.

If \(1\mathrm{g}\) of water at about \(94^{\circ}\mathrm{C}\) is introduced into the cylinder 2 liters in volume, from which all the air has been removed, the water will evaporate completely and the system will be in the condition known as unsaturated vapor, the pressure of the vapor being less than standard atmospheric pressure. On the \(P V\) diagram shown in Fig. 9- 1, this state is represented by the point \(A\) . If the vapor is then compressed slowly and isothermally, obviously the volume is decreasing, but more importantly the pressure will rise until the system reaches a state of saturated vapor, represented by the point \(B\) on the isotherm. If the compression is continued, condensation occurs to form droplets of water. During compression, the pressure remains constant (isobaric process) as long as the temperature remains constant. The horizontal straight- line segment \(B C\) represents the isothermal isobaric condensation of water vapor as the volume decreases, the constant pressure being called the vapor pressure. Alternately, as the volume increases, the vaporization line \(B C\) represents the isothermal isobaric evaporation of water vapor. At any point

===== Page 38 =====

**FIGURE 9-1** Isotherms of a pure substance such as \(\mathrm{H}_{2}\mathrm{O}\) . The solid phase, which would be at the bottom of the figure, is not shown. The graph shows Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. Several isotherms are drawn. A liquid saturation curve and a vapor saturation curve meet at the Critical point. Liquid phase is at high pressures, vapor phase at large volumes, and a mixture of liquid and vapor exists between the saturation curves.

between \(B\) and \(C\) , water and vapor coexist in equilibrium. At the point \(C\) , the sample is only liquid water, or saturated liquid.

In order to compress liquid water slightly, a very large increase of pressure is needed; hence, the line \(CD\) is almost vertical. At any point on the line \(CD\) , the water is said to be in the liquid phase; at any point on \(AB\) in the vapor phase; and at any point on line \(BC\) , between the two saturation curves, there is equilibrium between the liquid and the vapor phases. The curve \(ABCD\) , which is discontinuous at points \(B\) and \(C\) , is a typical isotherm of a pure substance on a \(PV\) diagram.

At other temperatures, the isotherms in the liquid- vapor region have a similar character, as shown in Fig. 9- 1. It is seen that the vaporization lines representing equilibrium between coexisting liquid and vapor phases become shorter as the temperature rises and vanish at a certain temperature called the critical temperature. The isotherm at the critical temperature is called the critical isotherm, and the point that represents the limit of the vaporization lines is called the critical point. It is seen that the critical point is a point of inflection on the critical isotherm. The pressure and volume at the critical point are known as the critical pressure and the critical volume, respectively. All points at which the liquid is saturated lie on the liquid saturation curve, and all points representing saturated vapor lie on the vapor saturation curve. The two saturation curves denoted by dashed lines meet at the critical point.

===== Page 39 =====

224 PART I: Fundamental Concepts

Above the critical point, the isotherms are continuous curves, which at large volumes and low pressures lose their inflection points and approach equilateral hyperbolas, namely, the isotherms of an ideal gas. At temperatures above the critical temperature, there is no longer any distinction between a liquid and a vapor, that is, the meniscus between the liquid and the vapor disappears. For \(\mathrm{H}_{2}\mathrm{O}\) , the critical temperature is \(647.067\mathrm{K}\) , the critical pressure is \(22.046\mathrm{MPa}\) , the critical volume for \(1\mathrm{kg}\) is \(0.00309\mathrm{m}^{3}\) , and the critical density is \(322.778\mathrm{kg} / \mathrm{m}^{3}\) .

It is clear that the critical point is a limiting point at which the specific volume of a liquid is equal to that of an equal mass of vapor, or, in other words, at which the density of the liquid equals the density of the vapor. If the densities of both liquid and vapor of \(\mathrm{H}_{2}\mathrm{O}\) are measured as functions of the temperature and the results are plotted, as in Fig. 9- 2, the critical temperature can be determined from the point where the two curves meet. At temperatures below the critical point, the liquid and vapor densities vary only slightly with the temperature and are significantly different from each other. It is interesting that at no temperature near the critical temperature is the meniscus visible between liquid and vapor. It was once thought that the disappearance of the meniscus was the criterion for the attainment of the critical point. At temperatures just below the critical point, there are two distinct phases with different densities, but they cannot be distinguished visually. Critical temperatures, pressures, and densities are given for various substances in Table 9.1. Although the critical point represents a unique temperature, it is not easily achieved or maintained; therefore, it is not used in thermometry as a reference temperature. Instead, the low- pressure triple point of water is the experimental basis of the Kelvin temperature scale.

In the \(PV\) diagram shown in Fig. 9- 1, the low- temperature region representing the solid phase at the bottom of the diagram had been omitted for the sake of clarity, but will be discussed further in the next section. Suffice it to say that there is a solid- vapor region below the liquid- vapor region in Fig. 9- 1. In the solid- vapor region of the \(PV\) diagram, the isotherms have the same general character as the vaporization lines in the liquid- vapor region. These horizontal line segments represent the isobaric transition from solid to vapor, or sublimation. There is one such line that separates the solid- vapor region below from the liquid- vapor region above. This line is associated with the coexistence of all three phases together, namely, the triple point. In the case of ordinary water, the triple point is at a unique temperature of \(273.16\mathrm{K}\) and a unique pressure of \(611.73\mathrm{Pa}\) . The line representing the isobaric isothermal triple-point states, however, extends over a wide range of specific volumes for \(1\mathrm{kg}\) , from \(1.00\times 10^{- 3}\mathrm{m}^{3}\) (saturated liquid) to \(2.06\times 10^{2}\mathrm{m}^{3}\) (saturated vapor). The triple-phase line of water will be discussed in more detail in Sec. 9.3.

When a liquid or solid equilibrates with its vapor at a given temperature, the vapor exerts a pressure that depends only on the temperature. In general, the higher the temperature, the greater the vapor pressure. As the temperature of a liquid is lowered, a state is reached at which some of the liquid starts to

===== Page 40 =====

**FIGURE 9-2** Density curves of liquid and vapor \(\mathrm{H}_{2}\mathrm{O}\) meet at the critical point \((+,\) liquid; \(\bullet\) , vapor; \(\circ\) , critical point). The graph shows Density, \(\mathrm{kg}/\mathrm{m}^3\) on the vertical axis and Temperature, \(\mathrm{K}\) on the horizontal axis. Two curves approach each other as the temperature increases, meeting at the critical point.

**TABLE 9.1** Critical data

| Substance | Temperature, K | Pressure, MPa | Density, kg/m³ |
| :--- | :--- | :--- | :--- |
| Helium-3 | 3.324 | 0.1154 | 41.3 |
| Helium-4 | 5.195 | 0.2275 | 69.64 |
| Hydrogen (normal) | 32.98 | 1.293 | 31.1 |
| Nitrogen | 126.20 | 3.390 | 313 |
| Oxygen | 154.58 | 5.043 | 436 |
| Ammonia | 405.51 | 11.35 | 236.4 |
| Carbon dioxide | 304.14 | 7.375 | 467.3 |
| Water | 647.067 | 22.046 | 322.778 |

solidify, namely, at the triple point. The temperature and the vapor pressure correspond to the state in which solid, liquid, and vapor exist together in equilibrium. At lower temperatures, only solid and vapor are present. The vapor pressure of most solids is very small.

### 9.2 PT DIAGRAM FOR A PURE SUBSTANCE; PHASE DIAGRAM

Consider a solid at a very low temperature. If the vapor pressure of a solid is measured at various temperatures until the triple point is reached, and, if the vapor pressure of the liquid is measured as the temperature of the sample is raised to the critical temperature, then the results can be plotted on a \(PT\) diagram, such as Fig. 9- 3, which is commonly called a phase diagram. If a substance at its triple point is compressed until there is no vapor left and the pressure on the resulting mixture of liquid and solid is increased, the temperature must change for equilibrium to exist between the solid and the liquid. Measurements of the pressures and temperatures of the solid coexisting with the liquid produce a third curve on the phase diagram, starting at the triple point and rising indefinitely. The data, representing the coexistence of: (1) solid and vapor, lie on the sublimation curve, which is bounded by absolute zero and the triple point; (2) solid and liquid, lie on the fusion curve, which starts at the triple point and is unbounded; (3) liquid and vapor, lie on the vaporization curve, which is bounded by the triple point and the critical point. In the particular case of water, the sublimation curve is called the frost line, the fusion curve is called the ice line, and the vaporization curve is called the steam line. The temperatures along the vaporization curve are the boiling points as a function of pressure. At the normal boiling point, the vapor pressure is standard atmospheric pressure, or 101,325 Pa. For water, the temperature of the normal boiling point is 373.124 K, as discussed in Sec. 1.11.

On Fig. 9- 3, no two- phase regions are shown, such as those found in the \(PV\) diagram in Fig. 9- 1. Rather, all the two- phase states collapse onto one of the three curves on the \(PT\) diagram. Away from the curves, there are only single- phase equilibrium states. A substance with no free surface (meniscus) and with a volume determined by that of the container is called a gas when its temperature is above the critical temperature. Otherwise, it is called a vapor. The term "vapor" is usually applied to a gas in equilibrium with its liquid (a saturated vapor) or to a gas at a temperature below its critical temperature. The properties of a vapor are the same as those of a gas, except that a vapor can be liquefied by an isothermal increase of pressure due to compression, but a gas cannot be liquefied, no matter how high the pressure. Helium, however, is unique in that its gas can be solidified under high pressure.

The slopes of the sublimation and the vaporization curves for all substances are positive. The slope of the fusion curve, however, may be positive or negative. The fusion curve of most substances has a positive slope. Water is one of the important exceptions. When an equation known as the Clausius- Clapeyron equation is derived in Chap. 11, it will be seen that any substance, such as water, which expands upon freezing, has a fusion curve with a negative slope, whereas for a substance that contracts upon freezing, such as carbon dioxide, has a fusion curve with a positive slope.

The triple point is merely the point of intersection of the sublimation, fusion, and vaporization curves. It must be understood that only on a phase diagram is the triple point represented by a point. On a \(PV\) diagram, the triple- phase state is a line. Triple- point data for common substances are given in Table 9.2.

**TABLE 9.2** Triple points of various substances

| Substance | Temperature, K | Pressure, MPa | Liquid density, kg/m³ |
| :--- | :--- | :--- | :--- |
| Hydrogen (normal) | 13.80 | 7.04 | 77 |
| Neon | 24.55 | 0.125 | 1 |
| Oxygen | 54.20 | 0.146 | 1306 |
| Nitrogen | 63.15 | 12.46 | 870 |
| Carbon dioxide | 216.65 | 0.518 | 1179 |
| Water (H2O) | 273.16 | 0.612 | 999.78 |
| Heavy water (D2O) | 276.97 | 0.661 | 1105.5 |

===== Page 41 =====

**FIGURE 9-3** Phase diagram for \(\mathrm{H}_{2}\mathrm{O}\) . The graph shows Pressure \(P\) on the vertical axis and Temperature \(T\) on the horizontal axis. Three regions are labeled Solid region, Liquid region, and Vapor region. Three curves, Sublimation curve, Fusion curve, and Vaporization curve, meet at the Triple point. The Vaporization curve ends at the Critical point.

===== Page 42 =====

228 PART I: Fundamental Concepts

The essential feature of a triple point is that three phases coexist in equilibrium. Most commonly, the three phases are solid, liquid, and vapor. However, a triple point could be defined as the state in which two different solid phases coexist with a liquid, or three different solid phases coexist. For example, an investigation of the ice line of water at low temperatures or very high pressures reveals various modifications (known as polymorphs in geophysics) in the solid phase. The polymorphs of \(\mathrm{H}_{2}\mathrm{O}\) vary in crystal structure, density, or entropy of the protons of hydrogen. Ordinary ice is denoted ice I, and polymorphs up to ice IX have been found in experiments that ranged in temperature from \(- 200\) to \(440^{\circ}\mathrm{C}\) and pressures from vacuum up to 170,000 atm (17 GPa). Equilibrium conditions among these polymorphs of ice and liquid give rise to eight stable triple points, which, including the thermometric low- pressure triple point at \(273.16\mathrm{K}\) , are listed in Table 9.3. Both ice IV and ice IX are unstable and, therefore, are not listed. Interestingly, water has the largest number of triple points for any known substance.

**TABLE 9.3** Equilibrium triple points of \(\mathbf{H}_{2}\mathbf{O}\)

| Phases in equilibrium | Temperature, K | Pressure, MPa | Temperature, °C |
| :--- | :--- | :--- | :--- |
| Ice I, liquid, vapor | 273.16 | 0.000612 | +0.01 |
| Ice I, liquid, ice III | 251.15 | 207.4 | -22.0 |
| Ice I, ice II, ice III | 238.45 | 212.8 | -34.7 |
| Ice II, ice III, ice V | 248.85 | 344.2 | -24.3 |
| Ice III, liquid, ice V | 256.15 | 346.2 | -17.0 |
| Ice V, liquid, ice VI | 273.31 | 625.7 | +0.16 |
| Ice VI, liquid, ice VII | 354.75 | 2199 | +81.6 |
| Ice VI, ice VII, ice VIII | 274 | 2077 | +1 |

### 9.3 PVT SURFACE

All the data that are represented on both the \(PV\) and the \(PT\) diagrams can be shown on one diagram if the three coordinates \(P\) , \(V\) , and \(T\) are plotted along orthogonal axes. The result is called the \(PVT\) surface. Two such surfaces are shown in Figs. 9- 4 and 9- 5, the first for a kilogram of an unusual substance like water that contracts upon melting, and the second for a kilogram of a typical substance like carbon dioxide that expands upon melting. The critical point is denoted by the letter \(C\) and the triple point by \(TP\) . The critical isotherm is marked \(T_{C}\) . These diagrams are not drawn to scale, the volume axis being considerably foreshortened. Every point on the \(PVT\) surface represents a state of equilibrium for the substance. If the \(PVT\) surface is projected on the \(PV\) plane, then the usual \(PV\) diagram is seen. Upon projecting the

===== Page 43 =====

**FIGURE 9-4** PVT surface for \(\mathrm{H}_{2}\mathrm{O}\) , which contracts while melting. The three-dimensional plot shows Pressure \(P\) , Volume \(V\) , and Temperature \(T\) axes. A solid region, liquid region, and vapor region are visible. A triple-point line and a critical point \(C\) are marked. The fusion, vaporization, and sublimation curves are shown on the front plane (PT projection).

**FIGURE 9-5** PVT surface for \(\mathrm{CO}_{2}\) , which expands while melting. The three-dimensional plot shows Pressure \(P\) , Volume \(V\) , and Temperature \(T\) axes. Solid, Liquid, Vapor, and Gas regions are visible. A triple point \(TP\), a critical point \(C\), and a critical isotherm \(T_C\) are marked.

PVT surface onto the PT plane, the entire solid- vapor region projects into the sublimation curve, the entire liquid- vapor region projects into the vaporization curve, the entire solid- liquid region projects into the fusion curve, and, finally, the triple- point line projects into the triple point on the phase diagram.

All the equilibrium triple points for a kilogram of water, as listed in Table 9.3, are shown on the PVT surface in Fig. 9- 6. Not shown are the two unstable polymorphs: ice IV, discovered by P. W. Bridgman in 1935, and ice IX, discovered by E. Whalley, J. B. R. Heath, and D. W. Davidson (Journal of Chemical Physics, vol. 48, pp. 2362- 2370) in 1968. In 1963, Kurt Vonnegut described in his novel Cat's Cradle the properties of a fictional form of ice, which he called ice IX, that supposedly was capable of crystallizing all the water in the world. The reported properties of the real ice IX are less spectacular.

Another interesting substance with unusual stable triple points is the isotope \(^4\mathrm{He}\) . The PVT surface for a kilogram of \(^4\mathrm{He}\) and the accompanying \(PT\) projection are shown in Fig. 9- 7, which reveals that \(^4\mathrm{He}\) has a number of remarkable properties. If we start at the critical point \((T_{C} = 5.2014\mathrm{K}\) , \(P_{C} = 2.2746\times 10^{5}\mathrm{Pa})\) and lower the temperature, the liquid remaining in equilibrium with its vapor, a triple point is reached (known as the lower \(\lambda\) - point) at which three different phases are in equilibrium. At the lower \(\lambda\) - point, there is no solid. Instead of solid helium, another modification of liquid helium, known as helium II, is found. The coordinates of the lower \(\lambda\) - point for the coexistence of helium I, helium II, and helium vapor are \(T = 2.1720\mathrm{K}\) and \(P = 0.050399\times 10^{5}\mathrm{Pa}\) . Further reduction of the temperature (by rapid evaporation) still does not produce the solid phase. In order to produce solid helium from either liquid I or liquid II, the pressure must be increased to over 29 atm, in which case another triple point (the upper \(\lambda\) - point at \(T = 1.7633\mathrm{K}\) , \(P = 30.13\times 10^{5}\mathrm{Pa}\) ) is reached at which both the liquids and the solid are in equilibrium. The lambda line connects the lower and upper \(\lambda\) - points and is the boundary between He I and He II. There is no triple point for solid, liquid, and vapor in \(^4\mathrm{He}\) .

The transition from liquid I to liquid II occurs at constant temperature and constant pressure with no "latent" heat and with no change of volume. Such a transition is known as a phase change of the second order and will be treated in detail in Chap. 14. When the two liquids of \(^4\mathrm{He}\) are in equilibrium, they both have the same density at a given temperature. Other properties, however, are remarkably different. For example, the thermal conductivity of liquid helium II is very much larger than that of liquid I; so much so, in fact, that a temperature gradient, which gives rise to bubbling in liquid I, does not exist in liquid II and, thus, one can tell when liquid II is formed by noting that the liquid suddenly becomes quiescent. Perhaps the most interesting property of liquid II is its remarkably low viscosity. It flows very rapidly through capillary tubes and goes through tightly packed porous materials as if through a sieve. Other interesting properties of liquid helium II are that it has a specific heat capacity at constant pressure larger than water, between the \(\lambda\) - point and approximately \(1.9\mathrm{K}\) , and a negative volume expansivity between the \(\lambda\) - point and approximately \(1.2\mathrm{K}\) .

===== Page 44 =====

**FIGURE 9-6** PVT surface for \(\mathrm{H}_{2}\mathrm{O}\) , showing all the equilibrium states. A triple line is a line parallel to the axis of specific volume. The three-dimensional plot shows Pressure, Specific volume, and Temperature. Various solid phases (Ice I to Ice VIII) and the Liquid phase are labeled. Triple lines for phase equilibria are shown.

**FIGURE 9-7** PVT surface and phase diagram for \(^{4}\mathrm{He}\) . The plot shows Pressure, Volume, and Temperature axes. The phase diagram projection shows Liquid I, Liquid II, He I, He II, Solid, Vapor, and Critical point \(C\) and Lambda line.

===== Page 45 =====

### 9.4 EQUATIONS OF STATE

It is impossible to express the complete behavior of a substance over the whole range of measured values of \(P\) , \(V\) , and \(T\) by means of one simple equation. Several equations of state, such as the ideal gas law and those found in Prob. 5.6, can be used to study the vapor phase.

Since the critical point is the limiting position on a \(P V\) diagram as the two end- points (saturated liquid and saturated vapor) on the same isotherm approach each other, it follows that the slope of the isotherm passing through the critical point (the critical isotherm) is zero, or

\[\left(\frac{\partial P}{\partial V}\right)_{T = T_{C}} = 0. \quad (9.1)\]

Also, the critical point is a point of inflection on the critical isotherm, because the isotherm is concave upward at volumes less than the critical volume and concave downward at specific volumes more than the critical volume; hence,

\[\left(\frac{\partial^{2}P}{\partial V^{2}}\right)_{T = T_{C}} = 0. \quad (9.2)\]

Equations (9.1) and (9.2), along with the equation of state itself, enable one to calculate the critical \(P\) , \(V\) , and \(T\) , denoted by \(P_{C}\) , \(V_{C}\) , and \(T_{C}\) . Consider, for example, the van der Waals equation of state, which can be written

\[P = \frac{RT}{\nu - b} -\frac{a}{\nu^{2}},\]

where \(\nu = V / n\) is the molar volume. This equation holds fairly well in the vapor region near and above the critical point. Equations (9.1) and (9.2) for molar volume yield, respectively,

\[\left(\frac{\partial P}{\partial\nu}\right)_{T = T_{C}} = -\frac{RT}{(\nu - b)^{2}} +\frac{2a}{\nu^{3}} = 0, \quad (9.3)\]

and

\[\left(\frac{\partial^{2}P}{\partial\nu^{2}}\right)_{T = T_{C}} = \frac{2RT}{(\nu - b)^{3}} -\frac{6a}{\nu^{4}} = 0. \quad (9.4)\]

Equations (9.3) and (9.4) can be rewritten as

\[\frac{2a}{\nu^{3}} = \frac{RT}{(\nu - b)^{2}},\]

and

\[\frac{3a}{\nu^{4}} = \frac{RT}{(\nu - b)^{3}}.\]

Divide the first equation by the second to obtain the critical molar volume,

\[\nu_{C} = 3b. \quad (9.5)\]

===== Page 46 =====

Substituting this value for \(\nu\) in the first of the two equations, we obtain the critical temperature,

\[T_{C} = \frac{8a}{27bR}, \quad (9.6)\]

and, finally, substitute these two values in the van der Waals equation to obtain the critical pressure,

\[P_{C} = \frac{a}{27b^{2}}. \quad (9.7)\]

It follows that for the van der Waals equation of state,

\[\begin{array}{r l} & {\frac{R T_{C}}{P_{C}\nu_{C}} = \frac{R\cdot\frac{8a}{27bR}}{\frac{a}{27b^{2}}\cdot3b}}\\ & {\qquad = 2.67.} \end{array} \quad (9.8)\]

If a substance behaved like an ideal gas at the critical point, then \(R T_{C} / P_{C}\nu_{C}\) would equal unity. If it obeys the van der Waals equation, then this ratio should equal 2.67, which would be a measure of the departure of the van der Waals gas from the ideal gas. In Table 9.4, the calculated values of \(R T_{C} / P_{C}\nu_{C}\) are listed for a number of interesting gases, and in no case is this ratio equal to 2.67, or even close. Above the critical point, at higher pressure, the van der Waals equation is fairly satisfactory and is useful in many cases. Other equations of state give better values of \(R T_{C} / P_{C}\nu_{C}\) , but are no better in describing other properties of gases.

**TABLE 9.4** Calculated values of \(R T_{C} / P_{C}\nu_{C}\)

| Substance | \(RT_c/P_c\nu_c\) |
| :--- | :--- |
| Water | 4.36 |
| Ammonia | 4.13 |
| Carbon dioxide | 3.64 |
| Oxygen | 3.49 |
| Nitrogen | 3.44 |
| Helium | 3.34 |
| Hydrogen | 3.26 |
| Van der Waals gas | 2.67 |
| Ideal gas | 1.00 |

===== Page 47 =====

### 9.5 MOLAR HEAT CAPACITY AT CONSTANT PRESSURE

Except for temperature, heat capacity is the thermal property of pure substances that is the oldest and most thoroughly investigated in thermodynamics, dating back to the pioneering work of Joseph Black in the 1760s.

The heat capacity was standardized to unit mass, that is, the specific heat was measured. Furthermore, the experiments were open to the atmosphere; hence, it was the specific heat capacity at constant pressure. Specific heat measurements at constant volume are much more difficult to perform, because the process of heating a sample causes thermal expansion, that is, a change of volume. For this reason, specific heat capacity at constant volume is usually not measured, but is calculated from other data, as we shall see later in this chapter.

The experimental measurement of heat capacity at constant pressure \(C_{P}\) has already been discussed in Sec. 4.7, and the general features of one type of calorimeter suitable for such measurements were described, as well as some details of technique. Data on the heat capacities of elements, alloys, compounds, plastics, etc., taken over as wide a temperature interval as possible, are of great importance in pure science and in engineering. Many interesting phenomena occur in the temperature range from absolute zero to about room temperature (300 K). In this temperature range, most materials are in the solid phase, which will be studied for the rest of this chapter. We shall limit ourselves to solids in the form of a cubic crystal, the simplest solid structure, either a single crystal, or a rod or powder consisting of a large number of small crystals. Furthermore, in order to facilitate comparison of different substances we shall investigate the molar heat capacity at constant pressure \(c_{P} = C_{P} / n\) , where \(C_{P}\) is the heat capacity of an arbitrary mass and \(n\) is the number of moles of the mass. In effect, the molar heat capacity measures the heat capacity of a substance having a fixed number of particles, namely, Avogadro's number.

The behavior of three different crystalline nonmetals is shown in Fig. 9- 8. (Metals exhibit a special behavior because of the effect of free electrons; such behavior will be discussed in Chap. 13. ) The molar heat capacity \(c_{P}\) of all materials approaches zero as \(T\) approaches zero. Between 25 and \(100 \mathrm{~K}\) , \(c_{P}\) rises rapidly but then bends and begins to flatten out in the neighborhood of room temperature. In none of the three crystals, however, does the \(c_{P}\) curve actually become horizontal.

In the germanium (Ge) crystal, the crystal structure is such that each lattice site is occupied by a single Ge atom, and therefore 1 mol of germanium crystal consists of \(N_{\mathrm{A}}\) vibrating particles, where \(N_{\mathrm{A}}\) is Avogadro's number. The value of \(c_{P}\) at room temperature is very nearly equal to \(3R\) , but it is still increasing with temperature. For crystals of sodium chloride (NaCl), each lattice site is occupied alternately, either by a sodium ion or by a chlorine ion in a face- centered cubic lattice. Therefore, 1 mol of NaCl consists of \(N_{\mathrm{A}}\) sodium ions in addition to \(N_{\mathrm{A}}\) chlorine ions, so that altogether there are \(2N_{\mathrm{A}}\) vibrating particles. The value of \(c_{P}\) at room temperature is very nearly equal to \(6R\) . In nickel (IV selenide) (NiSe \(_{2}\) ), the lattice sites are occupied by nickel atoms and by selenium atoms, with the center of the line joining the two selenium atoms and the nickel atom forming a face- centered cubic lattice similar to that of NaCl. In 1 mol of NiSe \(_{2}\) , there are \(3N_{\mathrm{A}}\) particles vibrating at their lattice sites, and the room- temperature value of \(c_{P}\) is very nearly equal

===== Page 48 =====

**FIGURE 9-8** The graph shows molar heat capacity \(c_P\) against temperature \(T\) for Germanium (Ge), Sodium Chloride (NaCl), and Nickel Selenide (NiSe$_2$). The \(c_P\) values approach \(3R\), \(6R\), and \(9R\) respectively at high temperatures.

to \(9R\) . In all cases, the molar heat capacity \(c_{P}\) at room temperature of exactly \(N_{\mathrm{A}}\) atoms or ions is approximately \(3R\) , about \(25\mathrm{J / mol\cdot K}\) .

The curves in Fig. 9- 8 correspond to crystals that were deliberately chosen to illustrate a regularity at room temperature. There is nothing special about the temperature \(300\mathrm{K}\) , however. Not all crystals have values of \(c_{P}\) whose rapid increase is tapering off at \(300\mathrm{K}\) . The \(c_{P}\) of diamond, for example, rises so slowly that at \(300\mathrm{K}\) it is still quite far from the value \(3R\) . A characteristic temperature, above which \(c_{P}\) is close to \(3R\) and below which \(c_{P}\) increases rapidly with temperature, is known as the Debye temperature. The crystals in Fig. 9- 8 have Debye temperatures below \(300\mathrm{K}\) , while diamond has a large Debye temperature \((2230\mathrm{K})\) , so its \(c_{P}\) is still much below \(3R\) at room temperature. Furthermore, \(c_{P}\) never approaches any value asymptotically, but continues to rise at all temperatures. The laws governing the temperature variation of molar heat capacity cannot be stated simply in terms of \(c_{P}\) . To express experimental results in a neat form, and also to appreciate the relation between experiment and theory, it is necessary to study first the temperature variation of thermal expansivity and compressibility, and then mathematical methods (see Chap. 10).

===== Page 49 =====

### 9.6 VOLUME EXPANSIVITY; CUBIC EXPANSION COEFFICIENT

The volume expansivity \(\beta = 1 / V(\partial V / \partial T)_p\) for a gas or liquid is measured directly. But, in experiments on the expansion of solids, the linear expansion coefficient \(\alpha\) , given in Chap. 2, is the quantity measured and usually reported in reference books under the heading of the elastic constants of a substance. Knowing the linear expansion coefficient \(\alpha\) , one calculates the cubic expansion coefficient \(\beta\) , which we call simply volume expansivity. To see the relationship between the two expansion coefficients, consider a solid of three rectangular dimensions \(L_{1}\) , \(L_{2}\) , and \(L_{3}\) ; then,

\[V = L_{1}L_{2}L_{3},\]

\[\left(\frac{\partial V}{\partial T}\right)_{p} = L_{2}L_{3}\left(\frac{\partial L_{1}}{\partial T}\right)_{p} + L_{1}L_{3}\left(\frac{\partial L_{2}}{\partial T}\right)_{p} + L_{1}L_{2}\left(\frac{\partial L_{3}}{\partial T}\right)_{p},\] \[\frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{p} = \frac{1}{L_{1}}\left(\frac{\partial L_{1}}{\partial T}\right)_{p} + \frac{1}{L_{2}}\left(\frac{\partial L_{2}}{\partial T}\right)_{p} + \frac{1}{L_{3}}\left(\frac{\partial L_{3}}{\partial T}\right)_{p},\]

and

\[\beta = \alpha_{1} + \alpha_{2} + \alpha_{3}, \quad (9.9)\]

where \(\alpha_{1}\) , \(\alpha_{2}\) , and \(\alpha_{3}\) are the linear expansion coefficients along the three axes, and \(\beta\) is the cubic expansion coefficient that we call the volume expansivity, or, simply, expansivity, as introduced in Chap. 2. In the case of quartz crystal, the two linear coefficients perpendicular to the \(z\) - axis are equal, so that \(\beta = 2\alpha_{\perp} + \alpha_{\parallel}\) . If the solid is isotropic, as in the case of a cubic crystal, then \(\alpha_{1} = \alpha_{2} = \alpha_{3} = \alpha\) , and

\[\beta = 3\alpha . \quad (9.10)\]

There are several absolute methods of measuring the linear expansion coefficients of solids, but the principal ones are based on the interference fringes of visible light and the variation of electric capacitance. The measurements in the 0 to \(50\mathrm{K}\) range involve much auxiliary cryogenic equipment, but the physical principles for measuring the linear expansion coefficients in any temperature range are easily understood.

The optical method uses an interferometer, shown in Fig. 9- 9 in a schematic diagram, which is a modification by Waterhouse and Yates of a Fizeau interferometer (straight fringes). Monochromatic light from a laser is reflected from mirror \(M_{1}\) onto plates \(P_{1}\) and \(P_{2}\) , which are separated by a ring or cylinder \(R\) made of the material whose linear expansion coefficient, hence, expansivity, is to be studied. The ring and plates are placed at the bottom of a cryostat, where liquid nitrogen or liquid helium is used to provide the low

===== Page 50 =====

**FIGURE 9-9** Modified version of an interferometer used to measure the linear coefficient of thermal expansion. The schematic shows a laser source, mirrors \(M_1, M_2, M_3\), plates \(P_1, P_2\), a specimen ring \(R\), and a camera \(C\).

temperatures at which measurements are often made. In Fig. 9- 9, all details of the cryostat, heater, thermometer, venting tubes, electric leads, etc., have been omitted. Interference takes place between the rays of light reflected from the bottom of \(P_{1}\) and the top of \(P_{2}\) , and a camera \(C\) is used to photograph the interference fringes. The temperature is varied slowly from, let us say, \(4 \mathrm{~K}\) up to room temperature, and the fringe system is photographed at regular intervals.

If \(N\) fringes travel across the field of view while the temperature changes from \(T_{0}\) to \(T\) , then the optical path difference has changed by \(N \lambda\) where \(\lambda\) is the wavelength of the light, and the thickness of the air space has changed by \(N \lambda / 2\) . If \(L_{0}\) is the length of the specimen at temperature \(T_{0}\) and \(L\) is the length at \(T\) , then

\[\frac{L - L_{0}}{L_{0}} = \frac{N \lambda}{2 L_{0}}.\]

If, therefore, \(N \lambda / 2 L_{0}\) is plotted against \(T\) and the slope of the resulting curve is taken at various temperatures, the linear expansion coefficient is obtained. Thus,

\[\alpha = \frac{d}{dT} \left(\frac{N \lambda}{2 L_{0}}\right).\]

In order to automate data acquisition, a photoelectric interferometer detects the movement of interference fringes by means of a photomultiplier tube. The number of fringes is automatically recorded as a function of the measured temperature of the specimen. Thus, the data are recorded in digital form suitable for calculation of linear and cubic expansion coefficients. The sensitivity \(\Delta L / L_{0}\) of this experiment is \(10^{- 7}\) .

===== Page 51 =====

In the electric method, the expansion of the specimen is communicated to one of the plates of a capacitor, the other plate being held fixed. The change in capacitance due to expansion of the sample is measured by an extremely sensitive bridge; and, in the experiments done by Carr and colleagues, this method has proved capable of sensitivities of \(2 \times 10^{- 10}\) . This method is the basis of most of the measurements of expansion coefficients at cryogenic temperatures.

The temperature dependence of the volume expansivity \(\beta\) of many substances is the same as that of NaCl, which is shown in Fig. 9- 10; namely, \(\beta\) is zero at absolute zero, rises rapidly in the interval from 0 to \(50 \mathrm{~K}\) , then bends and flattens out without actually becoming horizontal. Thus, the temperature variation of \(\beta\) is almost identical with that of \(c_{P}\) , also shown in Fig. 9- 10. Another similarity between \(\beta\) and \(c_{P}\) is the insensitivity of both quantities to

**FIGURE 9-10** Temperature variation of molar heat capacity \(c_{P}\) and volume expansivity \(\beta\) for NaCl, which are almost identical in temperature dependence. \((c_{P} \colon \mathrm{K}\) . Clusius, J. Goldmann, and A. Perlick: Zeitschrift für Naturforschung, vol. 4a, pp. 424- 432, 1949. \(\beta\) : P. P. M. Meincke and G. M. Graham: Canadian Journal of Physics, vol. 43, pp. 1853- 1866, 1965. ) The graph shows two curves, \(c_P\) and \(\beta\), which rise steeply at low temperatures and then flatten out.

===== Page 52 =====

### 9.7 COMPRESSIBILITY

Compressibility measurements are made in two different ways in order to determine compressibility under two different conditions. Installations are capable of subjecting solids to enormous hydrostatic pressures at constant temperature and capable of providing numerical values of the isothermal compressibility \(\kappa\) , where, from Chap. 2,

\[\kappa = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T, \quad (9.11)\]

which is also the reciprocal of the isothermal bulk modulus. Isothermal compressibilities, which are measured at fixed pressures up to many tens of thousands of atmospheres, are used to study phase transitions, changes of crystal structure, and other internal changes of solids and liquids, such as those of the polymorphs of ice. These are static measurements. Measurements of the speed of longitudinal waves in liquids and both longitudinal and transverse waves in solids, at atmospheric or moderate pressures, are dynamic measurements, which provide numerical values of the reversible adiabatic compressibility \(\kappa_{S}\) , which is defined as

\[\kappa_{S} = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{S}, \quad (9.12)\]

where the subscript \(S\) means isentropic, that is, adiabatic and reversible. It was shown in Chap. 5 that the speed of a longitudinal wave \(w\) in a fluid is given by

\[w = \sqrt{\frac{1}{\rho\kappa_{S}}}, \quad (9.13)\]

where \(\rho\) is the density of the fluid. Measurements of \(w\) and \(\rho\) are sufficient to provide \(\kappa_{S}\) of a fluid, but the measurement of \(\kappa_{S}\) of a crystalline solid is more difficult. For a cubic crystal, it is necessary to measure the speed of the shear wave in the [110] direction as well as that of the longitudinal wave in the [100] direction, and, from the two measurements, to calculate two different elastic constants. In the case of NaCl, these quantities are designated \(c_{11}\) and \(c_{12}\) , and it is known from the theory of elasticity that \(\kappa_{S}\) can be calculated from

\[\kappa_{S} = \frac{3}{c_{11} + 2c_{12}}. \quad (9.14)\]

===== Page 53 =====

Once the adiabatic compressibility \(\kappa_{S}\) is obtained, either from Eq. (9.13) for fluids or from Eq. (9.14) for cubic solids, the isothermal compressibility may be calculated by using two equations that will be derived in the next chapter, namely, the difference between the molar heat capacities at constant pressure and volume,

\[c_{P} - c_{V} = \frac{T\nu\beta^{2}}{\kappa}, \quad (9.15)\]

and the ratio of molar heat capacities,

\[\gamma = \frac{c_{P}}{c_{V}} = \frac{\kappa}{\kappa_{S}}. \quad (9.16)\]

Eliminating the molar heat capacity at constant volume \(c_{V}\) from Eqs. (9.15) and (9.16), we get

\[c_{P} - \frac{c_{P}\kappa_{S}}{\kappa} = \frac{T\nu\beta^{2}}{\kappa},\]

which reduces to

\[\kappa -\kappa_{S} = \frac{T\nu\beta^{2}}{c_{P}}. \quad (9.17)\]

Equation (9.17) permits the isothermal compressibility \(\kappa\) to be calculated from measured values of \(\kappa_{S}\) , \(T\) , \(\nu\) , \(\beta\) , and \(c_{P}\) .

The method of measuring wave speeds that is most suitable for crystalline solids is one that incorporates the pulse- echo technique. Short ultrasonic pulses of about \(1\mu \mathrm{s}\) duration are sent into the crystal from a transducer that emits sound waves. After reflection from an end of the crystal, the ultrasonic pulses are received by the same transducer. The pulse and the echo are observed on an oscilloscope, and the wave speed is calculated from the dimensions of the crystal and the time delay between pulse and echo. This method has a resolution of \(10^{- 5}\) in measurements of the wave speed and \(10^{- 7}\) in changes of the wave speed. Overton and Swim used this method to obtain the values of \(\kappa_{S}\) listed in Table 9.5.

The temperature variation of \(\kappa_{S}\) and \(\kappa\) of NaCl are shown in Fig. 9- 11, where it may be seen that both \(\kappa_{S}\) and \(\kappa\) , unlike \(c_{P}\) and \(\beta\) , do not approach zero as \(T\) approaches zero. From 0 to \(40\mathrm{K}\) , the adiabatic and isothermal compressibilities are nearly equal. At higher temperatures, the isothermal \(\kappa\) is larger than the adiabatic \(\kappa_{S}\) , as required by Eq. (9.17).

The speed of longitudinal waves in a liquid or a gas is usually measured with the aid of an acoustic interferometer, such as the one described in Sec. 5.7, which was used with argon gas to measure the molar gas constant \(R\) . Results of measurements of the isothermal and adiabatic compressibilities of water are listed in Table 9.6 and are shown in Fig. 9- 12. The minimum in the curve of isothermal compressibility for water at about \(50^{\circ}\mathrm{C}\) is quite anomalous. As a rule, the isothermal compressibility of most liquids increases as the temperature is raised and follows a simple exponential equation quite well:

**TABLE 9.5** Thermal properties of NaCl (Compiled by P. P. M. Meincke and G. M. Graham, Canadian Journal of Physics, vol. 43, pp. 1853-1866, 1965.)

| \(T\) K | \(c_P\), J/mol·K | \(\beta\), \(10^{-6}\) K\(^{-1}\) | \(\kappa\), \(10^{-12}\) Pa\(^{-1}\) | \(\nu\), kmol\(^{-1}\) | \(c_V\), J/mol·K | \(\kappa_S\), \(10^{-12}\) Pa\(^{-1}\) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 10 | 0.15 | 10.18 | 38.9 | 26.4 | 0.15 | 38.9 |
| 20 | 1.30 | 1.68 | 38.9 | 26.4 | 1.30 | 38.9 |
| 30 | 4.76 | 7.50 | 38.9 | 26.4 | 4.76 | 38.9 |
| 40 | 9.98 | 17.0 | 38.9 | 26.4 | 9.97 | 38.9 |
| 50 | 15.72 | 28.8 | 39.0 | 26.4 | 15.7 | 38.9 |
| 60 | 21.0 | 40.9 | 39.2 | 26.4 | 20.9 | 39.1 |
| 70 | 25.5 | 51.8 | 39.4 | 26.4 | 25.3 | 39.2 |
| 80 | 29.3 | 61.0 | 39.6 | 26.5 | 29.1 | 39.3 |
| 90 | 32.3 | 69.1 | 39.8 | 26.5 | 32.0 | 39.4 |
| 100 | 35.0 | 75.9 | 40.0 | 26.5 | 34.7 | 39.6 |
| 125 | 40.1 | 87.1 | 40.4 | 26.6 | 39.5 | 39.8 |
| 150 | 43.3 | 95.1 | 40.7 | 26.6 | 42.4 | 39.9 |
| 175 | 45.4 | 96.3 | 41.1 | 26.7 | 44.2 | 40.0 |
| 250 | 48.6 | 115 | 42.3 | 26.9 | 46.6 | 40.6 |
| 290 | 49.2 | 119 | 43.0 | 27.0 | 46.7 | 40.8 |

===== Page 54 =====

240 PART I: Fundamental Concepts

**FIGURE 9-11** Temperature variation of isothermal and adiabatic compressibilities of NaCl. (W. C. Overton and R. T. Swim: Physical Review, vol. 84, pp. 758-762, 1951.) The graph shows Isothermal \(\kappa\) and Adiabatic \(\kappa_S\) compressibilities against Temperature \(T\) in Kelvin. Both are nearly equal at low temperatures and diverge at higher temperatures, with \(\kappa\) being larger.

===== Page 55 =====

**TABLE 9.6** Thermal properties of water

| \(T\) °C | \(w\), m/s | \(\rho\), kg/m\(^3\) | \(c_P\), kJ/kg·K | \(\beta\), \(10^{-6}\) K\(^{-1}\) | \(\kappa\), \(10^{-10}\) Pa\(^{-1}\) | \(\kappa_S\), \(10^{-10}\) Pa\(^{-1}\) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 1402.4 | 999.84 | 4.217 | -67.89 | 5.088 | 5.085 |
| 10 | 1447.3 | 999.70 | 4.192 | 87.96 | 4.781 | 4.775 |
| 20 | 1482.3 | 998.21 | 4.181 | 206.80 | 4.589 | 4.559 |
| 30 | 1509.1 | 995.65 | 4.178 | 303.23 | 4.477 | 4.410 |
| 40 | 1528.8 | 992.22 | 4.178 | 385.30 | 4.424 | 4.311 |
| 50 | 1542.5 | 998.03 | 4.180 | 457.60 | 4.417 | 4.253 |
| 60 | 1550.9 | 983.20 | 4.184 | 523.07 | 4.449 | 4.228 |
| 70 | 1554.7 | 977.78 | 4.189 | 583.74 | 4.516 | 4.230 |
| 80 | 1554.4 | 971.82 | 4.196 | 641.11 | 4.614 | 4.258 |
| 90 | 1550.4 | 965.35 | 4.205 | 696.24 | 4.743 | 4.309 |
| 100 | 1543.2 | 958.40 | 4.215 | 750.30 | 4.901 | 4.381 |

**FIGURE 9-12** Isothermal and adiabatic compressibilities of water. The graph shows Isothermal \(\kappa\) and Adiabatic \(\kappa_S\) compressibilities against Temperature \(T\) in degrees Celsius. Both curves show a minimum at around 50°C.

\[\kappa = \kappa_{0}e^{aT}, \quad (9.18)\]

where \(\kappa_{0}\) and \(a\) are constants. The constant \(a\) for mercury is \(1.37 \times 10^{- 3} \mathrm{~K}^{- 1}\) .

All liquids, including water, become less compressible the more they are compressed; the reciprocal of the isothermal compressibility increases linearly with respect to the pressure; that is,

\[\frac{1}{\kappa} -\frac{1}{\kappa_{0}} = bP, \quad (9.19)\]

where \(\kappa_{0}\) is the isothermal compressibility at zero pressure, and the coefficient \(b\) is 6.7 for water and 8.2 for mercury.

===== Page 56 =====

### 9.8 MOLAR HEAT CAPACITY AT CONSTANT VOLUME

The measurement of \(c_{P}\) \(\beta\) and \(\kappa\) of crystalline solids, both metallic and nonmetallic, particularly at low temperatures, is important in the progress of solid- state theory. Our purpose, at present, is to use these measurements in conjunction with Eq. (9.15),

\[c_{P} - c_{V} = \frac{T\nu\beta^{2}}{\kappa},\]

to find the complete temperature dependence of \(c_{V}\) . All the measurements for NaCl are listed in Table 9.5, along with the calculated values of \(c_{V}\) , and both \(c_{P}\) and \(c_{V}\) are plotted as a function of \(T\) up to \(1000\mathrm{K}\) in Fig. 9- 13. Since 1 mol of NaCl consists of \(2N_{A}\) ions, the heat capacities refer to \(\frac{1}{2}\mathrm{mol}\) , or \(N_{A}\) ions.

At low temperatures, below \(100\mathrm{K}\) , \(c_{P}\) and \(c_{V}\) are practically the same. At all higher temperatures, while \(c_{P}\) continues to increase, \(c_{V}\) approaches a constant value \(3R\) , which is called the Dulong and Petit value, named after the two scientists who first observed that \(c_{P}\) came near this value at about room temperature. We see now that this value is actually approached by \(c_{V}\) and is exceeded only in special situations. The temperature dependence of \(c_{V} / 3R\) of five representative nonmetals is shown in Fig. 9- 14, where it may be seen that RbI practically reaches the Dulong and Petit value even before room temperature, whereas diamond has reached only one- fifth this value at

**FIGURE 9-13** Temperature variation of \(c_{P}\) and \(c_{V}\) of \(\frac{1}{2}\mathrm{mol}\) of NaCl. The value of \(c_{V}\) is close to \(3R\) at high temperatures. The graph shows \(c_P\) and \(c_V\) against Temperature \(T\) in Kelvin. \(c_P\) continues to increase, while \(c_V\) approaches a constant level near the \(3R\) mark.

===== Page 57 =====

**FIGURE 9-14** Temperature variation of \(c_{V} / 3R\) of nonmetals. (1 mol of diamond, \(\frac{1}{2}\) mol of RbI, NaCl, and MgO; and \(\frac{1}{3}\) mol of \(\mathrm{FeS}_{2}\) .) The graph shows \(c_V/3R\) against Temperature \(T\) in Kelvin. Curves for RbI, NaCl, FeS$_2$, MgO, and Diamond are shown. Diamond rises much more slowly than the others.

room temperature. As a matter of fact, it requires a temperature greater than \(2000\mathrm{K}\) to bring the \(c_{V}\) of diamond near \(3R\) .

Although the five curves in Fig. 9.14 differ markedly in the temperature at which \(c_{V} \rightarrow 3R\) , the curves are still very similar in shape. An experienced experimenter would be led to suspect that there existed a parameter — the Debye temperature \(\Theta\) — small for RbI and large for diamond, such that \(c_{V}\) is a universal function of the ratio \(T / \Theta\) , as we shall see in Chap. 13.

### 9.9 TS DIAGRAM FOR A PURE SUBSTANCE

The entropy of a system is a function of the thermodynamic coordinates, whose change during a process in which the system goes from an equilibrium state \(i\) to another equilibrium state \(f\) is equal to

\[S_{f} - S_{i} = \int_{R}^{f}\frac{\mathrm{d}Q}{T},\]

where the symbol \(R\) indicates that the integration is to be performed over any reversible path connecting \(i\) and \(f\) . If the two equilibrium states are infinitesimally near, then

\[\mathrm{d}Q = T d S,\] \[\frac{\mathrm{d}Q}{d T} = T \frac{d S}{d T}.\]

and

At constant pressure,

===== Page 58 =====

\[C_{P} = T\left(\frac{\partial S}{\partial T}\right)_P, \quad (9.20)\]

and, at constant volume,

\[C_{V} = T\left(\frac{\partial S}{\partial T}\right)_V. \quad (9.21)\]

The boxed equations relate partial derivatives of the state function \(S\) , \((\partial S / \partial T)_P\) and \((\partial S / \partial T)_V\) , which are also state functions, to quantities that can be measured experimentally, namely, \(C_P\) , \(C_V\) and \(T\) . For example, once the measurements of \(C_P\) are made at different temperatures, \(C_P / T\) can replace \((\partial S / \partial T)_P\) in any equation in which \((\partial S / \partial T)_P\) appears, even though, in general, the equation refers to a process in which the pressure is not constant, or to a process that is not reversible. Because \((\partial S / \partial T)_P\) is a state function of the system, \(C_P / T\) is also a state function and will change in value with changes in temperature and pressure.

If the temperature variation of \(C_V\) is known, the entropy change during an isobaric process may be calculated from the equation

\[S_{f} - S_{i} (\mathrm{isobaric}) = \int_{i}^{f} \frac{C_{P}}{T} dT.\]

Similarly, for an isochoric process,

\[S_{f} - S_{i} (\mathrm{isochoric}) = \int_{i}^{f} \frac{C_{V}}{T} dT.\]

The above equations provide a general method for calculating an entropy change but no way of calculating the absolute entropy of a system in a given state. If a set of tables is required that is to be used to obtain entropy differences and not absolute entropy, then it is a convenient procedure to choose an arbitrary standard state and to calculate the entropy change of the system from this standard state to all other states. Thus, in the case of water, the standard state is chosen to be water at its triple point at \(273.16 \mathrm{~K}\) , and all entropies for water are referred to this state.

The \(TS\) diagram for a substance such as carbon dioxide is shown in Fig. 9- 15. The segmented curve from \(A\) to \(F\) is a typical isobar representing a series of reversible isobaric processes in which solid is transformed finally into vapor. Thus,

===== Page 59 =====

**FIGURE 9-15** TS diagram for \(\mathrm{CO}_{2}\) showing isobaric process ABCDEF. The graph shows Temperature \(T\) on the vertical axis and Entropy \(S\) on the horizontal axis. The isobaric process goes from Solid (A) \(\rightarrow\) Solid and liquid (B) \(\rightarrow\) Liquid (C) \(\rightarrow\) Liquid and vapor (D) \(\rightarrow\) Vapor (E) \(\rightarrow\) Superheated vapor (F). The triple point, critical point, and regions for sublimation are also marked.

\(AB =\) isobaric heating of solid to its melting point,
\(BC =\) isobaric isothermal melting,
\(CD =\) isobaric heating of liquid to its boiling point,
\(DE =\) isobaric isothermal vaporization,
\(EF =\) isobaric heating of vapor (superheating).

The area under the line \(BC\) represents the latent heat of fusion at the particular temperature, and the area under the line \(DE\) represents the latent heat of vaporization. Similarly, the latent heat of sublimation is represented by the area under any sublimation line. It is obvious from the diagram that the latent heat of vaporization decreases as the temperature rises, and becomes zero at the critical point. At the triple point, but not in general, the latent heat of sublimation is equal to the sum of the latent heat of fusion and the latent heat of vaporization.

===== Page 60 =====

### PROBLEMS

9.1. A capsule containing a liquid is broken while inside a small vacuum chamber. Describe the behavior of the meniscus when the temperature of the system is raised under the following conditions:

(a) The volume of the chamber is much greater than the critical volume.

(b) The volume of the chamber is much less than the critical volume.

(c) The volume of the chamber is only slightly different from the critical volume.

9.2. (a) What happens when helium gas is compressed isothermally above the critical temperature? (b) If water vapor is compressed isothermally above the critical temperature, will ice I form? Is it possible that ice VII will form?

9.3. Using the Dieterici equation of state,

\[P = \frac{RT}{\nu - b} e^{-a / RT\nu},\]

show that

\[P_{C} = \frac{a}{4e^{2}b^{2}},\qquad \nu_{c} = 2b,\qquad T_{C} = \frac{a}{4R b},\]

and compare the value of \(RT_{C} / P_{C}\nu_{C}\) with the values in Table 9.4.

9.4. Using the Berthelot equation of state,

\[P = \frac{RT}{\nu - b} -\frac{a}{T\nu^{2}},\]

show that

\[P_{C} = \frac{1}{12b}\sqrt{\frac{2aR}{3b}},\qquad \nu_{C} = 3b,\qquad T_{C} = \sqrt{\frac{8a}{27bR}},\]

and compare the value of \(RT_{C} / P_{C}\nu_{C}\) with the values in Table 9.4.

9.5. If \(P,\nu ,\) and \(T\) are the pressure, molar volume, and temperature of a gas and \(P_{C},\nu_{C}\) and \(T_{C}\) are the critical pressure, critical molar volume, and critical temperature, then the reduced pressure \(P_{R}\) , the reduced molar volume \(\nu_{R}\) , and the reduced temperature \(T_{R}\) are defined as

\[P_{R} = \frac{P}{P_{C}},\qquad \nu_{R} = \frac{\nu}{\nu_{C}},\qquad T_{R} = \frac{T}{T_{C}}.\]

(a) Show that, in terms of reduced quantities, the van der Waals equation becomes

\[\left(P_{R} + \frac{3}{\nu_{R}^{2}}\right)\left(\nu_{R} - \frac{1}{3}\right) = \frac{8}{3} T_{R}.\]

When the van der Waals equation is in this form, the material constants \(a\) and \(b\) do not appear explicitly. Thus, all gases that obey the van der Waals equation may be considered in the same state when the values of \(P_{R},\nu_{R}\) , and \(T_{R}\) are the same (i.e., each gas is measured in units of its particular values of \(P_{C},\nu_{C}\) , and \(T_{C}\) ). This is the principle of corresponding states, which is a principle of universal similarity established first by van der Waals.

===== Page 61 =====

9.6. (a) The specific entropy of saturated water at \(100^{\circ}\mathrm{C}\) is \(1.307\mathrm{kJ / kg}\cdot \mathrm{deg}\) and that of saturated steam at the same temperature as \(7.355\mathrm{kJ / kg}\cdot \mathrm{deg}\) . What is the specific enthalpy of vaporization at this temperature?

(b) The specific enthalpy of saturated steam at \(100^{\circ}\mathrm{C}\) is \(2676\mathrm{kJ / kg}\) . From part (a), calculate the specific enthalpy of saturated water at this temperature.

9.7. The specific heat capacity at constant pressure of steam at atmospheric pressure is given by

\[c_{P} = a + bT + cT^{2},\]

where \(a = 1.912\mathrm{kJ / kg}\cdot \mathrm{deg}\)

\[b = 1.727\times 10^{-3}\mathrm{kJ / kg}\cdot \mathrm{deg}^{2},\]

\[c = -4.667\times 10^{-6}\mathrm{kJ / kg}\cdot \mathrm{deg}^{3}.\]

If the specific enthalpy of saturated steam at \(100^{\circ}\mathrm{C}\) is \(2676\mathrm{kJ / kg}\) , what is the specific enthalpy of superheated steam at the same pressure and a temperature of \(300^{\circ}\mathrm{C}\) ?

===== Page 62 =====

## CHAPTER 10

## MATHEMATICAL METHODS

### 10.1 CHARACTERISTIC FUNCTIONS

Often, important laws are reformulated to change variables in order to simplify the analysis of a system. For example, Newton's laws of motion can be rewritten in completely equivalent Lagrange's equations for appropriate coordinate systems in classical mechanics. The Lagrange's equations, in turn, can undergo a change of variable to produce the related Hamilton's equations that are fundamentally important in quantum mechanics. Changes of variables, known as Legendre differential transformations, yield functions that are fundamentally important in thermodynamics.

If the state of a system is described by a function of two variables \(f(x,y)\) which satisfies the equation

\[d f = u d x + v d y, \quad (10.1)\]

and we wish to change the description to one involving a new function \(g(u,y)\) satisfying a similar equation in terms of \(d u\) and \(d y\) , then it is necessary to define the Legendre transform \(g(u,y)\) as

\[g\equiv f - u x. \quad (10.2)\]

It is readily verified that \(g\) satisfies the equation

\[d g = -x d u + v d y. \quad (10.3)\]

Let us use Eq. (10.2) to define new thermodynamic state functions.

Consider the first law of thermodynamics for a hydrostatic system with heat expressed in terms of temperature and entropy, namely,

\[d U = -P d V + T d S, \quad (10.4)\]

===== Page 63 =====

where \(U\) is a function characterized by \(V\) and \(S\) . Therefore, \(U\) is convenient for situations involving changes in volume and entropy. For other situations, it is easier to work with different variables involving different functions.

Define a new characteristic function \(H\) , called enthalpy, using Eq. (10.2) to obtain

\[H\equiv U + PV. \quad (10.5)\]

Since \(U\) , \(P\) , and \(V\) are all state functions, \(H\) is also a state function. In differential form,

\[dH = VdP + TdS, \quad (10.6)\]

where \(H\) is a function characterized by \(P\) and \(S\) . Enthalpy is a convenient function for problems involving heat quantities, such as heat capacities, latent heats, and heats of reaction, when pressure is the variable being controlled.

Equation (10.4) may be rewritten as

\[dU = TdS - PdV,\]

in order to generate a characteristic function other than enthalpy, namely, the Helmholtz function \(A\) , given by the Legendre transform

\[A\equiv U - TS, \quad (10.7)\]

which is also a state function. In differential form,

\[dA = -SdT - PdV, \quad (10.8)\]

where \(A\) is a function of \(T\) and \(V\) . This function is appropriate for problems in which temperature and volume are the convenient independent variables, such as the partition function in statistical mechanics.

The last characteristic function, known as the Gibbs function \(G\) , is generated by a Legendre transformation of

\[dH = TdS + VdP,\]

that is,

\[G\equiv H - TS, \quad (10.9)\]

which is also a state function. In differential form,

\[dG = VdP - SdT, \quad (10.10)\]

where \(G\) is a function characterized by \(P\) and \(T\) . The Gibbs function is designed for problems in which pressure and temperature are the convenient independent variables, namely, phase transitions and most chemical reactions.

It is important to realize that no information is lost in the transformation from one characteristic function to another. The gain is a new function expressed in thermodynamic coordinates amenable to the experimental situation at hand. This remarkable formalism and procedure was introduced into thermodynamics during the 1870s by J. Willard Gibbs, Professor of Mathematical Physics at Yale for his entire career, but the names of the functions and their symbols were chosen by other scientists.

===== Page 64 =====

In terms of the state functions so far defined, we have written four differential equations that are formulations of the first law, namely,

\[dU = -PdV + TdS,\]
\[dH = VdP + TdS,\]
\[dA = -PdV - SdT,\]
\[dG = VdP - SdT.\]

and

\[dG = VdP - SdT.\]

These differential equations expressing \(U\) in terms of \(V\) and \(S\) , \(H\) in terms of \(P\) and \(S\) , and so forth, form a complete set of functions, based on successive Legendre transformations of the four thermodynamic variables \(P\) , \(V\) , \(T\) , and \(S\) for a hydrostatic system. The characteristic functions \(U(V, S)\) , \(H(P, S)\) , \(A(V, T)\) , and \(G(P, T)\) are known as thermodynamic potential functions, because they have the property that if the functions are expressed in terms of the appropriate thermodynamic variables, then all the thermodynamic properties of a system can be calculated by differentiation only. For instance, if the internal- energy function \(U\) is known as a function of \(V\) and \(S\) for a system, then we can calculate all the other thermodynamic properties of the system by differentiation, and no new constants or functions appear in the calculation. We may write

\[dU = \left(\frac{\partial U}{\partial V}\right)_S dV + \left(\frac{\partial U}{\partial S}\right)_V dS,\]

from which it follows, from comparison with Eq. (10.4), that

\[\left(\frac{\partial U}{\partial V}\right)_S = -P\qquad \mathrm{and}\qquad \left(\frac{\partial U}{\partial S}\right)_V = T. \quad (10.11)\]

However, if the internal- energy function \(U\) were chosen to be a function of \(V\) and \(T\) , we could not obtain the rest of the thermodynamic properties of the system without performing integrations, which introduce unknown constants of integration. For \(U\) to be classified as a thermodynamic potential function, it must be given as a function characterized by \(V\) and \(S\) .

There can be characteristic functions calculated for hydrostatic systems other than the four functions just mentioned. Any of the four differential equations could be rearranged to produce another function. For example, \(U(V, S)\) could be solved to give \(S(V, U)\) , and we could then say that \(S\) is the characteristic function for volume and internal energy, just as \(U\) is the characteristic function for volume and entropy. The choice of \(U, H, A\) , and \(G\) as the fundamental set of functions has the advantage that all four functions are energies, which, of course, are conserved.

For other simple systems, such as wires, surfaces, batteries, electrets, or paramagnets, the thermodynamic coordinates of pressure and volume are replaced by appropriate conjugate variables, as given in Table 3.1 (p. 66). But, notice that the extensive quantities simply replace volume, whereas intensive quantities replace negative pressure. For example, in Sec. 3.13, a composite system of an ideal paramagnetic gas was considered. Its four characteristic functions are:

\[\begin{array}{l}{dU = -PdV + \mu_0\mathcal{H}d\mathcal{M} + TdS,}\\ {dH = VdP - \mathcal{H}\mu_0d\mathcal{M} + TdS,}\\ {dA = -PdV + \mu_0\mathcal{H}d\mathcal{M} - SdT,} \end{array} \quad (10.12)\]

and

\[dG = VdP - \mathcal{H}\mu_0d\mathcal{M} - SdT.\]

Obviously, in a simple system of a paramagnetic solid, the terms involving the hydrostatic variables would not be present.

===== Page 65 =====

### 10.2 ENTHALPY

In discussing some of the properties of gases in Chap. 4, the sum of \(U\) and \(PV\) appeared several times (see Probs. 4.7 and 4.9). In order to investigate this sum, imagine a cylinder, thermally insulated and equipped with two adiabatic pistons on opposite sides of a porous wall that is also adiabatic, as shown in Fig. 10- 1(a). The importance of the porous wall is to permit mass to flow from one chamber to another while controlling the pressure, unlike a free expansion. The wall, shown ruled in horizontal lines, can be a porous plug, a narrow constriction, or a series of small holes. Between the left- hand piston and the wall there is a gas at a pressure \(P_{i}\) and a volume \(V_{i}\) ; since the right- hand piston against the wall prevents any gas from seeping through the porous plug, the initial state of the gas is an equilibrium state contained between the faces of the two pistons. Now, imagine that both pistons move simultaneously at different speeds to the right such that a constant higher pressure \(P_{i}\) is maintained on the left- hand side of the porous plug and a constant lower pressure \(P_{f}\) is maintained on the right- hand side. After all the gas has flowed through the porous plug, the final equilibrium state of the system is shown in Fig. 10- 1(b). There is no knowledge of the temperature of the gas in either the initial state or the final state. A throttling process is also known as a porous plug process or a Joule- Thomson expansion.

A throttling process exhibits internal mechanical irreversibility, due to friction between the gas and the walls of the pores in the plug. In other words, the gas passes through dissipative nonequilibrium states on its way from the initial equilibrium state to the final equilibrium state. These intermediate nonequilibrium states cannot be described by thermodynamic coordinates, but an interesting conclusion can be drawn about the initial and final

===== Page 66 =====

**FIGURE 10-1** Throttling process (Joule- Thomson expansion). (a) Initial state: a gas at pressure \(P_i\) and volume \(V_i\) is contained between two pistons with a porous plug. (b) Final state: gas at pressure \(P_f\) and volume \(V_f\) is on the right side of the plug.

equilibrium states, which are described by thermodynamic coordinates. From the first law,

\[(U_{f} - U_{i}) = W + Q. \quad (10.13)\]

The throttling process occurs in an adiabatic enclosure, so

\[Q = 0. \quad (10.14)\]

The net work done by the pistons on the gas causes the gas to flow across the boundary of the system enclosing the porous plug; that is,

\[W = -\int_{V_{f}}^{0}P_{f}d V - \int_{0}^{V_{i}}P_{i}d V. \quad (10.15)\]

Since both pressures remain constant on either side of the porous plug, the net work is

\[W = -(P_{f}V_{f} - P_{i}V_{i}). \quad (10.15)\]

Comparison of Eq. (10.15) with Eq. (10.13) shows that the internal energy \(U\) is different for the two equilibrium end- states of the Joule- Thomson expansion. A state function can be devised for which there is no difference in the end- states. If Eqs. (10.13), (10.14), and (10.15) are combined to obtain

\[(U_{f} - U_{i}) = -(P_{f}V_{f} - P_{i}V_{i}), \quad (10.16)\]

then

\[U_{i} + P_{i}V_{i} = U_{f} + P_{f}V_{f}. \quad (10.16)\]

Of course, the sums in Eq. (10.16) are simply the characteristic function enthalpy introduced in Eq. (10.5); that is,

\[H = U + PV. \quad (10.5)\]

===== Page 67 =====

So, Eq. (10.16) becomes

\[H_{i} = H_{f}\qquad \mathrm{(throttling~process)}\qquad \mathrm{[property~(1)]}, \quad (10.17)\]

which is the first of several experimental properties of enthalpy. Notice that in a throttling process the initial and final enthalpies are equal. One is not entitled to say that the enthalpy remains constant, since one cannot speak of the enthalpy of a system while it is passing through nonequilibrium states during this irreversible process. In plotting a throttling process on any diagram, the initial and final equilibrium states may be represented by points. The intermediate nonequilibrium states, however, cannot be plotted.

A continuous throttling process may be achieved by a pump that maintains a constant high pressure on one side of a porous wall or expansion valve, and a constant lower pressure on the other side, as shown in Fig. 10- 2. For every kilogram of fluid that undergoes the throttling process, we may write

\[h_{l} = h_{f},\]

where \(h = H / m\) indicates specific enthalpy. The continuous Joule- Thomson expansion, which is essential in the production of liquid nitrogen and other cryogenic liquids, is also used in mechanical refrigerators for attaining low temperatures in situations where liquids are unavailable or undesirable.

In order to determine other properties of enthalpy, consider the change in enthalpy that occurs when an arbitrary system undergoes any infinitesimal quasi- static process from an initial equilibrium state to a final equilibrium state. We have, from Eq. (10.5),

\[\begin{array}{r}{d H = d U + P d V + V d P;}\\ {\mathrm{d}Q = d U + P d V.} \end{array} \quad (10.18)\]

but,

\[\mathrm{d}Q = d U + P d V.\]

Therefore,

\[d H = \mathrm{d}Q + V d P. \quad (10.19)\]

**FIGURE 10-2** Apparatus for performing a continuous throttling process. The diagram shows a pump maintaining a high pressure on one side and a low pressure on the other, with a porous plug in between.

===== Page 68 =====

Dividing both sides by \(dT\) , we obtain

\[\frac{dH}{dT} = \frac{dQ}{dT} +V\frac{dP}{dT},\]

and, at constant \(P\)

\[\left(\frac{\partial H}{\partial T}\right)_P = \left(\frac{dQ}{dT}\right)_P = C_P\qquad [\mathrm{property}(2)]. \quad (10.20)\]

Equation (10.20) shows that the state function enthalpy \(H\) is related to an experimental quantity, the isobaric heat capacity, which is also a state function. Notice that \(H\) must be a function of \(T\) and \(P\) in order to perform the partial differentiation in Eq. (10.20). If \(H\) were a function of other variables, then the partial derivative would be complicated with terms in addition to the isobaric heat capacity. Furthermore, Eq. (10.20) provides a means of calculating the enthalpy from isobaric heat capacity data, namely,

\[H_{f} - H_{i} = \int_{i}^{f}C_{P}dT\qquad (\mathrm{all~processes}). \quad (10.21)\]

For an ideal gas, the isobaric heat capacity is constant and \(H_{f} - H_{i} = C_{P}(T_{f} - T_{i})\) . Enthalpy values for real vapors and gases at low pressures, with empirical temperature dependence of \(C_{P}\) , are calculated using Eq. (10.21) and the results are expressed as specific enthalpy or molar enthalpy as a function of temperature. Such data are extremely useful in experimental or practical work, even though, in theory, the characteristic function enthalpy \(H(P,S)\) is not expressly a function of temperature.

The enthalpy is related to heat, as shown in Eq. (10.19),

\[dH = dQ + VdP.\]

Thus, the change in enthalpy during an isobaric process is equal to the heat that is transferred between the system and the surroundings,

\[H_{f} - H_{i} = Q_{P}\qquad (\mathrm{isobaric})\qquad [\mathrm{property}(3)]. \quad (10.22)\]

Equation (10.22) completes the explanation of the concept of heat begun in Sec. 4.4, where the mathematical formulation of the first law was introduced and heat was explained as heat in transit due to a difference in temperature between the system and surroundings. For an isochoric (constant volume) process in a hydrostatic system, heat is the flow of internal energy; whereas for an isobaric (constant pressure) process in a hydrostatic system, heat is the flow of enthalpy. The change of enthalpy of a system during an isobaric chemical process is commonly called the "heat of reaction," but the phrase enthalpy of reaction is more informative.

If heat is added to the system during a first- order phase transition (e.g., melting, boiling, or sublimation), then the change of enthalpy of the system is called "latent heat." The word "latent" acknowledges that there is no change in temperature of the system when heating the system during a phase transition, unlike heating without a phase transition. Again, it is more informative to use the phrase latent enthalpy.

The change in enthalpy of a system undergoing a reversible adiabatic process has an interesting graphical interpretation. From the expression

\[dH = dQ + Vdp,\]

the change of enthalpy for an adiabatic process is

\[H_{f} - H_{i} = \int_{i}^{f}Vdp \qquad (\mathrm{adiabatic}) \qquad [\mathrm{property}(4)]. \quad (10.23)\]

The integral in Eq. (10.23) is represented by the area to the left of a curve for an isentropic process on a \(PV\) diagram, such as Fig. 10- 3, whereas the integral \(- \int P dV\) is represented by the area under an adiabatic curve on a \(PV\) diagram. There is a thermodynamic difference between the two integrals. The integral \(- \int P dV\) is adiabatic work, which changes the configuration of a system with constant mass by changing the volume. The integral \(\int V dP\) , known as (negative) flow- work in engineering practice, is energy that is received by a flowing gas in a region of higher pressure, perhaps from a pump or piston, and then carried to a region of lower pressure, such as in the continuous Joule- Thomson expansion.

If a pure substance undergoes an infinitesimal reversible process, then Eq. (10.19) may be written

\[dH = TdS + Vdp,\]

which, of course, is the same as Eq. (10.6). Partial differentiation yields

\[\left(\frac{\partial H}{\partial S}\right)_P = T\qquad \mathrm{and}\qquad \left(\frac{\partial H}{\partial P}\right)_S = V. \quad (10.24)\]

**FIGURE 10-3** \(PV\) diagram illustrating the difference between work and flow-work. The graph shows Pressure \(P\) on the vertical axis and Volume \(V\) on the horizontal axis. An isentropic curve from \(i\) to \(f\) is shown. The area under the curve is \(- \int P dV\), and the area to the left of the curve is \(\int V dP\).

===== Page 69 =====

The relations given in Eq. (10.24) are analogous to similar relations for internal energy given in Eq. (10.11). The properties of internal energy \(U(V, S)\) and the enthalpy \(H(P, S)\) are given in Table 10.1 for comparison of the two functions. The free expansion of a gas occurs in a rigid adiabatic container, which prevents work and heat from entering or leaving the system. Consequently, the internal energy \(U\) is unchanged; that is, \(U_i = U_f\). Notice that the system is the entire interior volume, including the chamber that was initially empty of gas. Furthermore, the gas expands irreversibly, so no statement can be made about \(U\) during the process, only at the initial and final equilibrium states.

**TABLE 10.1** Comparison of properties of \(U\) and \(H\) for a hydrostatic system

| Internal energy \(U(V,S)\) | Enthalpy \(H(P,S)\) |
| :--- | :--- |
| Free expansion (irreversible) | Throttling process (irreversible) |
| \(U_i = U_f\) | \(H_i = H_f\) |
| In general | In general |
| \(dU = \mathrm{d}Q - PdV\) | \(dH = \mathrm{d}Q + V dP\) |
| \((\partial U/\partial T)_V = C_V\) | \((\partial H/\partial T)_P = C_P\) |
| Isochoric process | Isobaric process |
| \(U_f - U_i = Q_V\) | \(H_f - H_i = Q_P\) |
| For an ideal gas | For an ideal gas |
| \(U_f - U_i = \int_i^f C_V dT\) | \(H_f - H_i = \int_i^f C_P dT\) |
| Adiabatic process | Adiabatic process |
| \(U_f - U_i = -\int_i^f P dV\) | \(H_f - H_i = \int_i^f V dP\) |
| Nearby equilibrium states | Nearby equilibrium states |
| \(dU = T dS - PdV\) | \(dH = T dS + V dP\) |
| \((\partial U/\partial S)_V = T\) | \((\partial H/\partial S)_P = T\) |
| \((\partial U/\partial V)_S = -P\) | \((\partial H/\partial P)_S = V\) |

===== Page 70 =====

### 10.3 HELMHOLTZ AND GIBBS FUNCTIONS

The Helmholtz function \(A(V,T)\) was introduced in Eq. (10.7) as another Legendre transformation of the internal- energy function \(U(V,S)\) ; that is,

\[A = U - TS.\]

For an infinitesimal reversible process, the Helmholtz function is given by Eq. (10.8),

\[dA = -PdV - SdT.\]

So, it follows:

1. For a reversible isothermal process,

\[dA = -PdV,\]

\[(A_{f} - A_{i})_{T} = -\int_{i}^{f}(PdV)_{T}. \quad (10.25)\]

Hence, the increase of the Helmholtz function during a reversible isothermal process equals the work done on the system. Alternatively, in a reversible isothermal process, the decrease in the Helmholtz function is the maximum amount of work done by the system; hence, \(A\) is sometimes called the Helmholtz free energy.

For any finite isothermal process, we may write, from Eq. (10.7),

\[\Delta A_{T} = \Delta U_{T} - T\Delta S_{T},\]

\[\Delta A_{T} = \Delta U_{T} - \Delta Q_{T} = \Delta W_{T}.\]

The decrease of the Helmholtz energy \(\Delta A_{T}\) of a system equals the maximum amount of isothermal work \(\Delta W_{T}\) that is performed by the system. The internal energy \(U_{T}\) also decreases, but the decrease \(\Delta U_{T}\) does not equal the work that the system can perform, as in the case of purely mechanical systems. In fact,

\[\Delta W_{T}\geq \Delta U\qquad \mathrm{depending~on}\qquad \Delta Q_{T}\geq 0.\]

Thermodynamic work is significantly different from mechanical work. Mechanical systems are usually considered to be reversible, whereas thermodynamic systems are only reversible in idealized cases needed for simple calculations, but are irreversible in any real, natural process.

2. For a reversible isothermal and isochoric process,

\[dA = 0,\]

and

\[A = \mathrm{const}. \quad (10.26)\]

In other words, the Helmholtz function has the same initial and final values when the initial and final temperatures and volumes are unchanged.

From the differential of the Helmholtz function,

===== Page 71 =====

\[dA = - PdV - S dT,\]

the pressure and the entropy may be calculated by performing the partial differentiations:

\[\left(\frac{\partial A}{\partial V}\right)_T = -P\qquad \mathrm{and}\qquad \left(\frac{\partial A}{\partial T}\right)_V = -S. \quad (10.27)\]

All the other thermodynamic variables can be calculated by differentiating the Helmholtz function, as shown in one of the problems at the end of the chapter.

The Gibbs function \(G(P,T)\) was introduced in Eq. (10.9) as the last Legendre transformation, that is,

\[G = H - TS.\]

For an infinitesimal reversible process,

\[dG = V dP - S dT,\]

so the volume and the entropy may then be calculated by the partial differentiations:

\[\left(\frac{\partial G}{\partial P}\right)_T = V\qquad \mathrm{and}\qquad \left(\frac{\partial G}{\partial T}\right)_P = -S. \quad (10.28)\]

In the case of a reversible isothermal and isobaric process,

\[dG = 0,\]

and

\[G = \mathrm{const}.\]

This is a particularly important result in connection with processes involving a change of phase. Sublimation, fusion, and vaporization take place isothermally and isobarically. Hence, during such processes, the Gibbs function of the system remains constant. If we denote by the symbols \(g^{\prime}, g^{\prime \prime}\) , and \(g^{\prime \prime \prime}\) , the molar Gibbs functions of a saturated solid, saturated liquid, and saturated vapor, respectively, then the equation of the fusion curve is

\[g^{\prime} = g^{\prime \prime},\]

the equation of the vaporization curve is

\[g^{\prime \prime} = g^{\prime \prime \prime},\]

and the equation of the sublimation curve is

\[g^{\prime} = g^{\prime \prime \prime}.\]

At the triple point, two equations hold simultaneously, namely,

\[g^{\prime} = g^{\prime \prime} = g^{\prime \prime \prime}. \quad (10.29)\]

All the \(g\) 's can be regarded as functions of \(P\) and \(T\) only, and hence Eq. (10.29) serves to determine the \(P\) and \(T\) of the triple point uniquely.

===== Page 72 =====

The Gibbs function is extremely important in chemistry, since chemical reactions begin and end at the same equilibrium atmospheric pressure and ambient temperature.

### 10.4 TWO MATHEMATICAL THEOREMS

THEOREM 1. If a relation exists among \(x, y\) , and \(z\) , then we may imagine \(z\) expressed as a function of \(x\) and \(y\) ; whence,

\[d z = \left(\frac{\partial z}{\partial x}\right)_{y}d x + \left(\frac{\partial z}{\partial y}\right)_{x}d y.\]

If we let

\[M = \left(\frac{\partial z}{\partial x}\right)_{y}\qquad \mathrm{and}\qquad N = \left(\frac{\partial z}{\partial y}\right)_{x},\]

then

\[d z = M d x + N d y,\]

where \(z, M\) , and \(N\) are all functions of \(x\) and \(y\) . Partially differentiating \(M\) with respect to \(y\) , and \(N\) with respect to \(x\) , we get

\[\left(\frac{\partial M}{\partial y}\right)_{x} = \frac{\partial^{2}z}{\partial x \partial y}\qquad \mathrm{and}\qquad \left(\frac{\partial N}{\partial x}\right)_{y} = \frac{\partial^{2}z}{\partial y \partial x}.\]

Since the two second derivatives of the right- hand terms are equal, it follows that

\[\left(\frac{\partial M}{\partial y}\right)_{x} = \left(\frac{\partial N}{\partial x}\right)_{y}. \quad (10.30)\]

This is known as the condition for an exact differential, and it applies to all four characteristic functions.

THEOREM 2. If a quantity \(f\) is a function of \(x, y\) , and \(z\) , and a relation exists among \(x, y\) , and \(z\) , then \(f\) may be regarded as a function of any two of \(x, y\) , and \(z\) . Similarly, any one of \(x, y\) , and \(z\) may be considered to be a function of \(f\) and one other of \(x, y\) , and \(z\) . Thus, regarding \(x\) to be a function of \(f\) and \(y\) ,

\[d x = \left(\frac{\partial x}{\partial f}\right)_{y}d f + \left(\frac{\partial x}{\partial y}\right)_{f}d y.\]

Considering \(y\) to be a function of \(f\) and \(z\) ,

\[d y = \left(\frac{\partial y}{\partial f}\right)_{z}d f + \left(\frac{\partial y}{\partial z}\right)_{f}d z.\]

Substituting this expression for \(d y\) in the preceding equation, we get

\[d x = \left[\left(\frac{\partial x}{\partial f}\right)_{y} + \left(\frac{\partial x}{\partial y}\right)_{f}\left(\frac{\partial y}{\partial f}\right)_{z}\right]d f + \left[\left(\frac{\partial x}{\partial y}\right)_{f}\left(\frac{\partial y}{\partial z}\right)_{f}\right]d z.\]

===== Page 73 =====

But, \[ dx = \left( \frac{\partial x}{\partial f} \right)_z df + \left( \frac{\partial x}{\partial z} \right)_f dz. \]

Equate the \(dz\) terms of the last two equations to obtain

\[\left(\frac{\partial x}{\partial y}\right)_f\left(\frac{\partial y}{\partial z}\right)_f = \left(\frac{\partial x}{\partial z}\right)_f,\]

that is,

\[\left[\left(\frac{\partial x}{\partial y}\right)_f\left(\frac{\partial y}{\partial z}\right)_f\left(\frac{\partial z}{\partial x}\right)_f = 1.\right] \quad (10.31)\]

Notice that Eq. (10.31) is not the same as Eq. (2.6), which is an expression involving three variables instead of four variables.

Equating the \(df\) terms, we obtain

\[\left(\frac{\partial x}{\partial f}\right)_z = \left(\frac{\partial x}{\partial f}\right)_y + \left(\frac{\partial x}{\partial y}\right)_f\left(\frac{\partial y}{\partial f}\right)_z. \quad (10.32)\]

### 10.5 MAXWELL'S RELATIONS

We have seen that the hydrostatic properties of a pure substance are conveniently represented in terms of the differentials of any of these four functions:

\[dU = -PdV + TdS,\]
\[dH = VdP + TdS,\]
\[dA = -PdV - SdT,\]
\[dG = VdP - SdT.\]

and

\[dG = VdP - SdT.\]

Since \(U\) , \(H\) , \(A\) , and \(G\) are actual functions, their differentials are exact differentials of the type

\[dz = Mdx + Ndy,\]

where \(z\) , \(M\) , and \(N\) are all functions of \(x\) and \(y\) . Apply Eq. (10.30), the condition for an exact differential, to the four exact differentials \(dU\) , \(dH\) , \(dA\) , and \(dG\) to obtain:

**FIGURE 10-4** The VAT- VUS diagram; a mnemonic device for writing the differential forms of the four thermodynamic potentials. A square diagram has vertices labeled \(V\), \(T\), \(P\), \(S\). Arrows point from \(V\) to \(P\) and from \(T\) to \(S\). Characteristic functions are placed on the sides: \(U\) between \(V\) and \(S\), \(H\) between \(P\) and \(S\), \(A\) between \(V\) and \(T\), and \(G\) between \(P\) and \(T\).

===== Page 74 =====

1. \(dU = T dS - P dV\) ; hence, \(\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V\) .

2. \(dH = T dS + V dP\) ; hence, \(\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P\) .

3. \(dA = -S dT - P dV\) ; hence, \(\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V\) .

4. \(dG = -S dT + V dP\) ; hence, \(\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P\) .

The four equations on the right are known as Maxwell's relations. These equations do not refer to a process but express relations that hold at any equilibrium state of a hydrostatic system. Of course, the reciprocals of Maxwell's relations are also valid equations.

Maxwell's relations are enormously useful, because they provide relationships between measurable quantities and those which either cannot be measured or are difficult to measure. In particular, it should be noted that pressure, volume, and temperature can be measured by experimental techniques, whereas entropy cannot be determined experimentally. By using the Maxwell relations, one can determine changes of entropy by quantities that can be measured, namely, \(P\) , \(V\) , and \(T\) in a hydrostatic system. For example, the fourth Maxwell relation,

\[\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P,\]

may be combined with the volume expansivity \(\beta\) of a pure substance in order to provide information concerning the statistical interpretation of entropy in the following way. If a substance has a positive expansivity, then \((\partial V / \partial T)_P\) is positive and the derivative \((\partial S / \partial P)_T\) is negative. If the pressure on a substance is increased isothermally and if no unusual molecular rearrangements take place (such as association or dissociation), the molecules experience a decrease in entropy and are, therefore, in a more orderly state, according to microscopic theory. In other words, our knowledge about these molecules is increased.

The four characteristic functions and associated Maxwell relations need to be remembered. A useful mnemonic device for this purpose, which is shown in Fig. 10- 4, is called a König- Born diagram, named after Max Born whose students popularized it and F. O. König who first published it. The square is also referred to as a VAT- VUS diagram because of the labels on the top and left side. A characteristic function is indicated at the midpoint of each side and its thermodynamic coordinates at the ends of the side. So, for example, the Helmholtz function \(A\) is a function of thermodynamic coordinates \(V\) and \(T\) , and the internal- energy function \(U\) is a function of thermodynamic coordinates \(V\) and \(S\) . The differential of the characteristic function for a simple system always equals the sum of two terms that include the differential of the thermodynamic coordinates. The coefficient of the differential in each term is found by connecting the arrow from the thermodynamic coordinate of the differential to its conjugate coordinate across the VAT- VUS diagram. The Maxwell relations are obtained by applying Eq. (10.30) to each of the four thermodynamic potential functions.

Consider, for example, the internal- energy function \(U(V,S)\) . The differential \(dU\) equals the sum of terms including \(dV\) and \(dS\) . The coefficient of \(dV\) is found by the arrow that connects \(V\) to \(P\) . Notice that the connection goes against the arrow, so the coefficient of \(dV\) is not \(P\) , but \(- P\) . Similarly, the coefficient of \(dS\) is found by going in the direction of the arrow that connects \(S\) to \(T\) . The VAT- VUS diagram is modified for other simple systems by replacing \(P\) and \(V\) by the appropriate intensive and extensive variables in the new system, except that \(P\) is replaced by the negative of the intensive variable.

### 10.6 TdS EQUATIONS

The entropy of a pure substance can be considered as a function of any two variables, such as \(T\) and \(V\) ; thus,

\[dS = \left(\frac{\partial S}{\partial T}\right)_V dT + \left(\frac{\partial S}{\partial V}\right)_T dV,\]

and

\[T dS = T\left(\frac{\partial S}{\partial T}\right)_V dT + T\left(\frac{\partial S}{\partial V}\right)_T dV.\]

Since \(T dS = dQ\) for a reversible isochoric process, it follows that

\[T\left(\frac{\partial S}{\partial T}\right)_V = C_V.\]

And, from Maxwell's third relation,

===== Page 75 =====

264 PART I: Fundamental Concepts

\[\left(\frac{\partial S}{\partial V}\right)_{T} = \left(\frac{\partial P}{\partial T}\right)_{V};\]

therefore,

\[T d S = C_{V} d T + T\left(\frac{\partial P}{\partial T}\right)_{V} d V. \quad (10.34)\]

We shall call Eq. (10.34) the first \(T d S\) equation. It is useful in a variety of ways. For example, 1 mol of a van der Waals gas undergoes a reversible isothermal expansion from an initial molar volume \(\nu_{i}\) to a final molar volume \(\nu_{f}\) . How much heat has been transferred?

For 1 mol,

\[T d s = c_{V} d T + T\left(\frac{\partial P}{\partial T}\right)_{V} d v,\]

where \(s, \nu\) , and \(c_{V}\) indicate molar quantities. Using the molar van der Waals equation of state,

\[P = \frac{R T}{\nu - b} -\frac{a}{\nu^{2}},\]
\[\left(\frac{\partial P}{\partial T}\right)_{V} = \frac{R}{\nu - b};\]

and

\[T d s = c_{V} d T + R T \frac{d v}{\nu - b}.\]

hence,

Since \(T\) is constant, \(c_{V} d T = 0\) ; and, since the process is reversible, \(q = \int T d s\) . Therefore,

\[q = R T \int_{\nu_{i}}^{\nu_{f}} \frac{d v}{\nu - b},\]

and, finally,

\[q = R T \ln \frac{\nu_{f} - b}{\nu_{i} - b}.\]

A second \(T d S\) equation can be derived if the entropy of a pure substance is regarded as a function of \(T\) and \(P\) ; then,

\[d S = \left(\frac{\partial S}{\partial T}\right)_{P} d T + \left(\frac{\partial S}{\partial P}\right)_{T} d P,\]

and

\[T d S = T\left(\frac{\partial S}{\partial T}\right)_{P} d T + T\left(\frac{\partial S}{\partial P}\right)_{T} d P.\]

But,

\[T\left(\frac{\partial S}{\partial T}\right)_{P} = C_{P}.\]

And, from Maxwell's fourth relation,

\[\left(\frac{\partial S}{\partial P}\right)_{T} = -\left(\frac{\partial V}{\partial T}\right)_{P};\]

===== Page 76 =====

thus,

\[T d S = C_{P}d T - T\left(\frac{\partial V}{\partial T}\right)_{P}d P. \quad (10.35)\]

Equation (10.35) is the second \(T d S\) equation, which is more useful than the first \(T d S\) equation because the partial derivative holds pressure constant rather than volume constant. A third \(T d S\) equation for hydrostatic systems will be found among the problems at the end of the chapter. Two important applications of the second \(T d S\) equation follow.

1. Reversible isothermal change of pressure. When \(T\) is constant,

\[T d S = -T\left(\frac{\partial V}{\partial T}\right)_{P}d P,\]

and

\[Q = -T\left\{\left(\frac{\partial V}{\partial T}\right)_{P}d P.\right.\]

Remembering that the volume expansivity is

\[\beta = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{P},\]

we obtain

\[Q = -T\int V\beta d P,\]

which can be integrated when the dependence of \(V\) and \(\beta\) on the pressure is known. In the case of a solid or liquid, neither \(V\) nor \(\beta\) is very sensitive to a change in pressure. For example, in the case of mercury, as the pressure is increased from zero to a thousand times atmospheric pressure at room temperature, the volume of 1 mol of mercury changes only \(\frac{1}{3}\) percent, and the volume expansivity changes about 4 percent. The volume and the expansivity of most solids and liquids behave similarly; therefore, \(V\) and \(\beta\) are assumed to be constant and are brought in front of the integral sign. We then have

\[Q = -TV\beta \int_{P_{i}}^{P_{f}}d P,\]

or

\[Q = -TV\beta (P_{f} - P_{i}).\]

It is seen from this result that, as the pressure is increased isothermally, heat will flow out if \(\beta\) is positive but that, for a substance with a negative expansivity (such as water between 0 and \(4^{\circ}C\) , or a rubber band), an isothermal increase of pressure causes an absorption of heat.

If the pressure on \(15\mathrm{cm}^{3}\) of mercury at \(20^{\circ}C\) is increased reversibly and isothermally from 0 to 1000 atm, the heat transferred will be approximately

\[Q\simeq -TV\beta P_{f},\]

where \(T = 293\mathrm{K}\) , \(V = 2\times 10^{- 5}\mathrm{m}^{3}\) , \(\beta = 1.81\times 10^{- 4}\mathrm{K}^{- 1}\) , and \(P_{f} = 1.01\times 10^{8}\mathrm{Pa}\) . Hence,

===== Page 77 =====

266 PART I: Fundamental Concepts

\[\begin{array}{r l} & {Q = -(293\mathrm{~K})(1.5\times 10^{-5}\mathrm{~m}^{3})(1.81\times 10^{-4}\mathrm{~K}^{-1})(1.01\times 10^{8}\mathrm{~Pa})}\\ & {\quad = -80.3\mathrm{~N}\cdot \mathrm{m}}\\ & {\quad = -80.3\mathrm{~J}.} \end{array} \quad (1.01\times 10^{8}\mathrm{~Pa})\]

In other words, 80.3 J of heat leaves the system in order to hold the temperature constant as the pressure is increased by an enormous amount.

It is interesting to compare the heat liberated by the system with the work done on the system during the compression,

\[W = -\int P dV;\]

and, at constant temperature,

\[W = -\int \left(\frac{\partial V}{\partial P}\right)_{T}P dP.\]

Recalling the isothermal compressibility, \(\kappa = -(1 / V)(\partial V / \partial P)_{T}\) , we get

\[W = \int_{P_{i}}^{P_{f}}V\kappa P dP.\]

The isothermal compressibility is also fairly insensitive to a change of pressure. The isothermal compressibility of mercury at room temperature changes about 2 percent as the pressure is increased from zero to a thousand times atmospheric pressure. Therefore, we may again replace \(V\) and \(\kappa\) by constant values and obtain

\[W = \frac{1}{2} V\kappa (P_{f}^{2} - P_{i}^{2})\] \[\qquad \simeq \frac{1}{2} V\kappa P_{f}^{2}.\]

For example, taking \(\kappa = 4.01\times 10^{- 11}\mathrm{Pa}^{- 1}\) for mercury, we get

\[W = \frac{1}{2} V\kappa P_{f}^{2}\] \[\qquad = \frac{1}{2} (1.5\times 10^{-5}\mathrm{m}^{3})(4.01\times 10^{-11}\mathrm{Pa}^{-1})(1.01\times 10^{8}\mathrm{Pa})^{2}\] \[\qquad = 3.07\mathrm{J}.\]

Therefore, it is seen that, if the pressure is increased from 0 to 1000 atm during a compression of \(15\mathrm{cm}^{3}\) of mercury maintained at \(20^{\circ}\mathrm{C}\) , then 80.3 J of heat flows from the system but only 3.07 J of work is performed on the system! The extra amount of energy in the form of heat comes, of course, from the store of internal energy, which has changed by an amount

\[\Delta U = Q + W\] \[\qquad = -80.3\mathrm{~J} + 3.1\mathrm{~J}\] \[\qquad = -77.2\mathrm{~J}.\]

Whereas isothermal compressibility \(\kappa\) is always a positive quantity, volume expansivity \(\beta\) may be positive or negative. In the foregoing example, \(\beta\) is

===== Page 78 =====

positive and heat flows out of the system during compression. For a substance with a negative expansivity \(\beta\) , heat is absorbed by the system and the internal energy is increased.

2. Reversible adiabatic change of pressure. Since the entropy remains constant in this process,

\[T d S = 0 = C_{P} d T - T\left(\frac{\partial V}{\partial T}\right)_{P} d P,\]

\[d T = \frac{T}{C_{P}}\left(\frac{\partial V}{\partial T}\right)_{P} d P = \frac{T V \beta}{C_{P}} d P.\]

In the case of a solid or liquid, an increase of pressure of as much as 1000 atm produces only a small temperature change. Also, experiment shows that \(C_{P}\) hardly changes, even for an increase of 10,000 atm. The equation above, when applied to a solid or a liquid, may, therefore, be written

\[\Delta T = \frac{T V \beta}{C_{P}} (P_{f} - P_{i}).\]

It is clear from the discussion above that a reversible adiabatic increase of pressure will produce an increase of temperature in any substance with a positive expansivity, and a decrease in temperature in a substance with a negative expansivity.

For example, if the pressure on \(15 \mathrm{cm}^{3}\) of mercury (specific heat \(c_{P} = 139 \mathrm{J / kg} \cdot \mathrm{K}\) and specific volume \(\nu = 7.38 \times 10^{- 5} \mathrm{m}^{3} / \mathrm{kg}\) ) at \(20^{\circ} \mathrm{C}\) is increased isentropically from 0 to 1000 atm, the temperature change will be approximately

\[\begin{array}{l}{{\Delta T\simeq\frac{T\nu\beta}{c_{P}}P_{f}}}\\ {{\qquad=\frac{(293\mathrm{K})(7.38\times10^{-5}\mathrm{m}^{3}/\mathrm{kg})(1.81\times10^{-4}\mathrm{K}^{-1})}{139\mathrm{J}/\mathrm{kg}\cdot\mathrm{K}}(1.01\times10^{8}\mathrm{Pa})}}\\ {{\qquad=2.84\mathrm{K}.}}\end{array} \quad (1.01 \times 10^{8} \mathrm{Pa})\]

In Sec. 2.4, the inverse of this example found that a \(10^{\circ} \mathrm{C}\) change in the temperature of mercury requires approximately 450 atm of pressure. The discrepancy in results arises because the earlier calculation was done at constant volume, thereby eliminating the effect of work being performed. If the system were a substance with negative \(\beta\) , then the adiabatic increase of pressure would have produced a decrease in temperature.

### 10.7 INTERNAL-ENERGY EQUATIONS

If a pure substance undergoes an infinitesimal reversible process between two equilibrium states, the change of internal energy is

===== Page 79 =====

268 PART I: Fundamental Concepts

\[dU = T dS - P dV.\]

Dividing by \(dV\) , we get

\[\frac{dU}{dV} = T\frac{dS}{dV} -P,\]

where \(U\) , \(S\) , and \(P\) are regarded as functions of \(T\) and \(V\) . If \(T\) is held constant, then the derivatives become partial derivatives, and

\[\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial S}{\partial V}\right)_T - P.\]

Using Maxwell's third relation, \((\partial S / \partial V)_T = (\partial P / \partial T)_V\) , we get

\[\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_V - P. \quad (10.36)\]

We shall call this equation the first internal- energy equation. Although holding the volume constant is difficult in an experiment, it is straightforward in an equation of state. Two examples of its usefulness follow.

1. Ideal gas:

\[P = \frac{nRT}{V},\]

\[\left(\frac{\partial P}{\partial T}\right)_V = \frac{nR}{V},\]

and

\[\left(\frac{\partial U}{\partial V}\right)_T = T\frac{nR}{V} -P = 0.\]

Therefore, \(U\) does not depend on \(V\) , but is a function of only \(T\) in an ideal gas.

2. Van der Waals gas (1 mol):

\[P = \frac{RT}{\nu - b} -\frac{1}{\nu^2},\]

\[\left(\frac{\partial P}{\partial T}\right)_V = \frac{R}{\nu - b},\]

and

\[\left(\frac{\partial u}{\partial v}\right)_T = T\frac{R}{\nu - b} -\frac{RT}{\nu - b} +\frac{a}{\nu^2} = \frac{a}{\nu^2}.\]

Consequently,

\[du = c_VdT + \frac{a}{\nu^2} dv,\]

and

\[u = \int c_VdT - \frac{a}{\nu} +\mathrm{const}.\]

It follows, therefore, that the internal energy of a van der Waals gas increases as the volume increases, with the temperature remaining constant.

===== Page 80 =====

The second internal- energy equation shows the dependence of internal energy on pressure. We start with Eq. (10.4),

\[dU = T dS - P dV,\]

and divide by \(dP\) . Then,

\[\frac{dU}{dP} = T\frac{dS}{dP} -P\frac{dV}{dP},\]

where \(U\) , \(S\) , and \(V\) are regarded as functions of \(T\) and \(P\) . If \(T\) is held constant, then the derivatives become partial derivatives, and

\[\left(\frac{\partial U}{\partial P}\right)_T = T\left(\frac{\partial S}{\partial P}\right)_T - P\left(\frac{\partial V}{\partial P}\right)_T.\]

Using Maxwell's fourth relation, \((\partial S / \partial P)_T = - (\partial V / \partial T)_P\) , we get

\[\left(\frac{\partial U}{\partial P}\right)_T = -T\left(\frac{\partial V}{\partial T}\right)_P - P\left(\frac{\partial V}{\partial P}\right)_T, \quad (10.37)\]

which is the second internal- energy equation.

### 10.8 HEAT-CAPACITY EQUATIONS

Equating the first and second \(T dS\) equations,

\[C_P dT - T\left(\frac{\partial V}{\partial T}\right)_P dP = C_V dT + T\left(\frac{\partial P}{\partial T}\right)_V dV,\]

and solving for \(dT\) , we obtain

\[dT = \frac{T\left(\frac{\partial P}{\partial T}\right)_V}{C_P - C_V} dV + \frac{T\left(\frac{\partial V}{\partial T}\right)_P}{C_P - C_V} dP.\]

But,

\[dT = \left(\frac{\partial T}{\partial V}\right)_P dV + \left(\frac{\partial T}{\partial P}\right)_V dP.\]

Therefore,

\[\left(\frac{\partial T}{\partial V}\right)_P = \frac{T\left(\frac{\partial P}{\partial T}\right)_V}{C_P - C_V},\]

and

\[\left(\frac{\partial T}{\partial P}\right)_V = \frac{T\left(\frac{\partial V}{\partial T}\right)_P}{C_P - C_V}.\]

Both of the foregoing equations yield the result that

===== Page 81 =====

270 PART I: Fundamental Concepts

\[C_{P} - C_{V} = T\left(\frac{\partial V}{\partial T}\right)_{P}\left(\frac{\partial P}{\partial T}\right)_{V}.\]

It was shown, by Eq. (2.6), that

\[\left(\frac{\partial P}{\partial T}\right)_{V} = -\left(\frac{\partial V}{\partial T}\right)_{P}\left(\frac{\partial P}{\partial V}\right)_{T},\]

and, therefore,

\[C_{P} - C_{V} = -T\left(\frac{\partial V}{\partial T}\right)_{P}^{2}\left(\frac{\partial P}{\partial V}\right)_{T}. \quad (10.38)\]

Equation (10.38) is an important equation in thermodynamics, and it shows that:

1. Since \((\partial P / \partial V)_{T}\) is always negative for all known substances and \((\partial V / \partial T)_{P}^{2}\) must be positive, then \(C_{P} - C_{V}\) can never be negative; or \(C_{P}\) can never be less than \(C_{V}\) .

2. As \(T \rightarrow 0\) , \(C_{P} \rightarrow C_{V}\) ; or, at absolute zero, the two heat capacities are equal.
3. \(C_{P} = C_{V}\) when \((\partial V / \partial T)_{P} = 0\) . For example, at \(4^{\circ} \mathrm{C}\) , the temperature at which the density of water is a maximum, \(C_{P} = C_{V}\) .

Laboratory measurements of the heat capacity of solids and liquids usually take place at constant pressure and for unit mass, and, therefore, data are reported in terms of specific heat \(c_{P}\) . It would be extremely difficult to measure, with any degree of accuracy, \(c_{V}\) of a solid or liquid, because of thermal expansion. Values of \(c_{V}\) , however, must be known for purposes of comparison with theory. The equation for the difference in the specific heats is very useful in calculating \(c_{V}\) in terms of \(c_{P}\) and other measurable quantities. Remembering that volume expansivity is

\[\beta = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{P},\]

and isothermal compressibility is

\[\kappa = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{T},\]

we may write Eq. (10.38) in the form

\[c_{P} - c_{V} = \frac{T\nu\left[\frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_{P}\right]^{2}}{-\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{T}},\]

or

\[c_{P} - c_{V} = P\frac{T\nu\beta^{2}}{\kappa}, \quad (10.39)\]

===== Page 82 =====

where \(c_{P}\) and \(c_{V}\) are molar heat capacities and \(\nu\) is the molar volume. Equation (10.39) is also useful in deriving equations for the adiabatic compressibility. From Eq. (9.16),

\[c_{P}\kappa = c_{V}\kappa_{S}.\] \[c_{P}\kappa = c_{V}\kappa_{S}.\]

Therefore,

\[c_{P} - c_{V} = c_{P} - \frac{c_{P}\kappa_{S}}{\kappa} = c_{P}\left(1 - \frac{\kappa_{S}}{\kappa}\right).\]

Comparing this expression for the heat- capacity difference with Eq. (10.39), we get

\[\frac{T\nu\beta^{2}}{\kappa} = \frac{c_{P}}{\kappa} (\kappa - \kappa_{S}),\]

and, finally,

\[\kappa - \kappa_{S} = \frac{T\nu\beta^{2}}{c_{P}}. \quad (10.42)\]

### PROBLEMS

10.1. Starting with the first Maxwell relation, derive the remaining three by using only the relations:

\[\left(\frac{\partial x}{\partial y}\right)_{z}\left(\frac{\partial y}{\partial z}\right)_{x}\left(\frac{\partial z}{\partial x}\right)_{y} = -1,\]

\[\left(\frac{\partial x}{\partial y}\right)_{f}\left(\frac{\partial y}{\partial z}\right)_{f}\left(\frac{\partial z}{\partial x}\right)_{f} = +1.\]

10.2. Show that, for an ideal gas:

\[A = \int C_{V}dT - T\int \frac{C_{V}}{T} dT - nRT\ln V - \mathrm{const.}T + \mathrm{const.}\]
\[G = \int C_{P}dT - T\int \frac{C_{P}}{T} dT + nRT\ln P - \mathrm{const.}T + \mathrm{const.}\]
\[A = \int C_{V}dT - T\int \frac{C_{V}}{T} dT - nRT\ln V - \mathrm{const.}T + \mathrm{const.}\]
\[G = \int C_{P}dT - T\int \frac{C_{P}}{T} dT + nRT\ln P - \mathrm{const.}T + \mathrm{const.}\]

(c) Apply the above equations to 1 mol of an ideal gas.

10.3. From the differential equation for the thermodynamic potential \(A(T,V)\) , derive expressions for pressure \(P\) , entropy \(S\) , internal energy \(U\) , heat capacity at constant volume \(C_{V}\) , heat capacity at constant pressure \(C_{P}\) , volume expansivity \(\beta\) , and isothermal compressibility \(\kappa\) .

10.4. Derive the following equations:

\[\begin{array}{l}{U=-T\Big(\frac{\partial A}{\partial T}\Big)_{V}=-T^{2}\Big[\frac{\partial(A/T)}{\partial T}\Big]_{V}.}\\ {C_{V}=-T\Big(\frac{\partial^{2}A}{\partial T^{2}}\Big)_{V}.}\\ {H=G-T\Big(\frac{\partial G}{\partial T}\Big)_{P}=-T^{2}\Big[\frac{\partial(G/T)}{\partial T}\Big]_{P}}\\ {C_{P}=-T\Big(\frac{\partial^{2}G}{\partial T^{2}}\Big)_{P}.}\end{array} \quad (Gibbs-Helmholtz equation)\]

10.5. Another set of characteristic functions for a single- substance system can be defined by performing the Legendre transformations on the entropy \(S(U,V)\) rather than on the internal energy \(U(V,S)\) . The thermodynamic potentials turn out to be particularly useful in statistical mechanics and the theory of irreversible thermodynamics, in contrast to equilibrium thermodynamics presented in this book.

===== Page 83 =====

10.6. From the fact that \(dV / V\) is an exact differential, derive the relation

\[\left(\frac{\partial\beta}{\partial P}\right)_{T} = -\left(\frac{\partial\kappa}{\partial T}\right)_{P}.\]

10.7. By invoking the condition for an exact differential, Eq. (10.30), demonstrate that the reversible heat \(Q_{R}\) is not a thermodynamic property.

10.8. Derive the third \(T d S\) equation,

\[T d S = C_{V}\left(\frac{\partial T}{\partial P}\right)_{V}d P + C_{P}\left(\frac{\partial T}{\partial V}\right)_{P}d V,\]

and show that the three \(T d S\) equations may be written as follows:

\[T d S = C_{V}d T + \frac{\beta T}{\kappa}d V.\]
\[T d S = C_{P}d T - V\beta T d P.\]
\[T d S = \frac{C_{V}\kappa}{\beta}d P + \frac{C_{P}}{\beta V}d V.\]

10.9. The pressure on \(500\mathrm{g}\) of copper is increased reversibly and isothermally from 0 to \(5000\mathrm{atm}\) at \(298\mathrm{K}\) . (Take the density \(\rho = 8.96\times 10^{3}\mathrm{kg / m^{3}}\) , volume expansivity \(\beta = 49.5\times 10^{- 6}\mathrm{K}^{- 1}\) , isothermal compressibility \(\kappa = 6.18\times 10^{- 12}\mathrm{Pa}^{- 1}\) , and specific heat \(c_{P} = 385\mathrm{J / kg}\cdot \mathrm{K}\) to be constant.)

(a) How much heat is transferred during the compression?

(b) How much work is done during the compression?

(c) Determine the change of internal energy.

(d) What would have been the rise of temperature if the copper had been subjected to a reversible adiabatic compression?

10.10. The pressure on \(0.2\mathrm{kg}\) of water is increased reversibly and isothermally from atmospheric pressure to \(3\times 10^{8}\mathrm{Pa}\) at \(20^{\circ}\mathrm{C}\) . (Numerical values are given in Table 9.6. )

(a) How much heat is transferred?

===== Page 84 =====

10.11. The pressure on 1 g of water is increased from 0 to \(10^{8}\) Pa reversibly and adiabatically. Calculate the temperature change when the initial temperature and other variables have the different values given in the three cases below:

| Temperature, °C | Specific volume \(v\), \(10^{-3}\) m³/kg | \(\beta\), \(10^{-6}\) K⁻¹ | \(c_P\), \(10^{-3}\) J/kg·K |
| :--- | :--- | :--- | :--- |
| 0 | 1.0002 | -68 | 4.217 |
| 50 | 1.0121 | 458 | 4.181 |
| 100 | 1.0435 | 750 | 4.217 |

10.12. A gas obeys the equation \(P(\nu - b) = RT\) , where \(b\) is constant and \(c_{V}\) is constant. Show that:

(a) \(u\) is a function of \(T\) only.

(b) \(\gamma\) is constant.

(c) A relation that holds during an adiabatic process is

\[P(\nu -b)^{\gamma} = \mathrm{const}.\]

10.13 Show that for a gas obeying the van der Waals equation \((P + a / \nu^{2})(\nu - b) = RT\) with \(c_{V}\) a function of \(T\) only, an equation for an adiabatic process is

\[T(\nu -b)^{R / c_{V}} = \mathrm{const}.\]

10.14. (a) Using the virial expansion

\[P\nu = RT(1 + BP + CP^{2} + \dots)\]

calculate \((\partial u / \partial P)_{T}\) and its limit as \(P\rightarrow 0\)

(b) Using the same expansion, calculate \((\partial P / \partial \nu)_{T}\) and its limit as \(P\rightarrow 0\)

(c) Using parts \((a)\) and \((b)\) , calculate \((\partial u / \partial \nu)_{T}\) and its limit as \(P\rightarrow 0\) . (Compare the solution with the results of Rossini and Frandsen given in Sec. 5.2. )

10.15. Show that the differentials of the three thermodynamic potentials \(U\) , \(H\) , and \(A\) may be written

\[dU = (C_{P} - PV\beta)dT + V(\kappa P - \beta T)dP,\]
\[dH = C_{P}dT + V(1 - \beta T)dP,\]
\[dA = -(PV\beta + S)dT + PV\kappa dP.\]

and

10.16. (a) Derive the equation

\[\left(\frac{\partial C_{V}}{\partial V}\right)_{T} = T\left(\frac{\partial^{2}P}{\partial T^{2}}\right)_{V}.\]

(b) Prove that \(C_{V}\) of an ideal gas is a function of \(T\) only.

(c) In the case of a gas obeying the equation of state

===== Page 85 =====

10.17. (a) Derive the equation

\[\frac{P\nu}{RT} = 1 + \frac{\beta}{\nu},\]

where \(B\) is a function of \(T\) only, show that

\[c_{V} = -\frac{RT}{\nu}\frac{d^{2}}{dT^{2}} (BT) + (c_{V})_{0},\]

where \((c_{V})_{0}\) is the value at very large volumes.

10.17. (a) Derive the equation

\[\left(\frac{\partial C_{P}}{\partial P}\right)_{T} = -T\left(\frac{\partial^{2}V}{\partial T^{2}}\right)_{P}.\]

(b) prove that \(C_{P}\) of an ideal gas is a function of \(T\) only.

(c) In the case of a gas obeying the equation of state

\[P\nu = RT + BP,\]

where \(B\) is a function of \(T\) only, show that

\[c_{P} = -T\frac{d^{2}B}{dT^{2}} P + (c_{P})_{0},\]

where \((c_{P})_{0}\) is the value at very low pressures.

10.18. In the accompanying table are listed the thermal properties of liquid neon, compiled by Gladun. Calculate the plot against temperature: (a) \(c_{V}\) , (b) \(\kappa_{S}\) , and (c) \(\gamma\) .

| \(T\), K | \(\rho\), kg/m³ | \(\beta\), \(10^{-2}\) K⁻¹ | \(\kappa\), \(10^{-8}\) Pa⁻¹ | \(c_P\), \(10^3\) J/kg·K |
| :--- | :--- | :--- | :--- | :--- |
| 25 | 1240 | 1.33 | 0.43 | 1.81 |
| 27 | 1206 | 1.46 | 0.50 | 1.86 |
| 29 | 1170 | 1.63 | 0.62 | 1.94 |
| 31 | 1131 | 1.84 | 0.79 | 2.04 |
| 33 | 1089 | 2.12 | 1.03 | 2.18 |
| 35 | 1042 | 2.52 | 1.40 | 2.36 |
| 37 | 992 | 3.14 | 2.04 | 2.63 |
| 39 | 932 | 4.24 | 3.24 | 3.07 |
| 41 | 859 | 6.86 | 6.94 | 4.06 |
| 43 | 743 | 13.10 | 21.49 | 6.41 |
| 44 | 588 | 51.90 | 96.39 | 13.4 |

10.19. Derive the following equations:

===== Page 86 =====

10.20. Derive the following equations:

10.21. (a) A measure of the result of an adiabatic Joule free expansion is provided by the Joule coefficient \(\eta = (\partial T / \partial V)_{U}\) . Show that

\[\eta = -\frac{1}{C_{V}}\left(\frac{\beta T}{\kappa} -P\right).\]

(b) A measure of the result of the Joule- Thomson expansion (adiabatic throttling process or isenthalpic expansion) is provided by the Joule- Thomson coefficient \(\mu = (\partial T / \partial P)_{H}\) . Show that

\[\mu = \frac{V}{C_{P}} (\beta T - 1).\]

10.22. The temperature of \(1\mathrm{kg}\) of mercury at \(20^{\circ}\mathrm{C}\) is increased by \(5^{\circ}\mathrm{C}\) under conditions of constant volume. How much heating is required? (Take the volume expansivity \(\beta = 1.81\times 10^{- 4}\mathrm{K}^{- 1}\) , specific heat at constant pressure \(c_{P} = 139\mathrm{J / kg}\cdot \mathrm{K}\) , isothermal compressibility \(\kappa = 3.94\times 10^{- 11}\mathrm{Pa}^{- 1}\) to be constant.)

===== Page 87 =====

## CHAPTER 11

## OPEN SYSTEMS

### 11.1 JOULE- THOMSON EXPANSION

In this chapter, we shall study the behavior of open systems by means of phase transitions. In the best- known first- order phase transitions, namely, the melting of ice and the vaporization of water, the regions of temperature and pressure are easily accessible without special apparatus. Some of the most interesting materials, however, such as nitrogen, hydrogen, and helium, whose phase transitions are well understood, exist only at low temperatures. It is important, therefore, to learn how these low temperatures are achieved and maintained. The first step is to liquefy nitrogen, which is produced by means of the Joule- Thomson expansion or, as it is also called, a throttling process, as discussed in Sec. 10.2.

In the Joule- Thomson expansion, a gas is made to undergo a continuous throttling process. By means of a pump, a constant pressure is maintained on one side of a porous plug and a constant lower pressure on the other side. The experiment is performed in the following way. The pressure \(P_{i}\) and temperature \(T_{i}\) on the high- pressure side of the plug are chosen arbitrarily. The pressure \(P_{f}\) on the other side of the plug is then set at any value less than \(P_{i}\) , and the temperature of the gas \(T_{f}\) is measured. Next, \(P_{i}\) and \(T_{i}\) are kept the same, \(P_{f}\) is changed to another value, and the corresponding \(T_{f}\) is measured. This procedure is repeated for a number of different values of \(P_{f}\) , and the corresponding \(T_{f}\) is measured in each case. The final pressure \(P_{f}\) is the independent variable of the experiment, and \(T_{f}\) is the dependent variable. The results provide a set of discrete points on a phase diagram, one point being \((P_{i}, T_{i})\) and the others being the various corresponding \(P_{f}\) 's and \(T_{f}\) 's indicated in Fig. 11- 1 by numbers (1) to (7). Although the points shown in the figure do not refer to any particular gas, they are typical of most gases. It can be seen

===== Page 88 =====

278 PART I: Fundamental Concepts

**FIGURE 11-1** Isenthalpic states of a gas undergoing the Joule- Thomson expansion. The graph shows Temperature \(T\) on the vertical axis and Pressure \(P\) on the horizontal axis. A point \(i\) is marked with a circle. Several final points \(f(1)\) through \(f(7)\) are marked with crosses.

that, if a throttling process takes place between the states \((P_{i},T_{i})\) and \((P_{f},T_{f})\) .4), there is a rise of temperature. Between \((P_{i},T_{i})\) and \((P_{f},T_{f})\) .7), however, there is a drop of temperature. In general, the temperature change of a gas upon passage through a porous plug depends on the three quantities \(P_{i}\) \(T_{i}\) , and \(P_{f}\) , and may be an increase or a decrease; or, there may be no change whatever in the temperature.

According to the discussion of enthalpy in Sec. 10.2, the eight points plotted in Fig. 11- 1 represent equilibrium states of a certain amount of the gas (say, 1 mol), for which the gas has the same molar enthalpy at the initial equilibrium state and all the final equilibrium states. All equilibrium states of the gas corresponding to this molar enthalpy must lie on some curve, and it is reasonable to assume that this curve can be obtained by drawing a smooth curve through the discrete points. Such a curve is called an isenthalpic curve. Realize that an isenthalpic curve is not the graph of a throttling process. No such graph can be drawn, because in any throttling process the intermediate irreversible states traversed by a gas cannot be described by means of thermodynamic coordinates. An isenthalpic curve is the locus of all points representing equilibrium initial and final states of the same molar enthalpy. The throttling experiment is performed to provide a few of these points, and the rest are obtained by interpolation.

The temperature \(T_{i}\) on the high- pressure side is now changed to another value, with \(P_{i}\) being kept the same. The final pressure \(P_{f}\) is again varied, and the corresponding \(T_{f}\) 's are measured. Upon plotting the new point \((P_{i},T_{i})\) and the resulting \(P_{f}\) 's and \(T_{f}\) 's, another locus of points is obtained, which determines another isenthalpic curve corresponding to a different molar enthalpy. In this way, a series of isenthalpic curves is obtained. Such a series is shown in Fig. 11- 2 for nitrogen.

The numerical value of the slope of an isenthalpic curve on a \(TP\) diagram, at any point, is called the Joule- Thomson coefficient and is denoted by \(\mu\) . Thus,

\[\mu = \left(\frac{\partial T}{\partial P}\right)_{h}, \quad (11.1)\]

===== Page 89 =====

**FIGURE 11-2** Isenthalpic curves, labeled 1- 6, and inversion curve for nitrogen. In the region below the liquid- vapor curve, the substance is in the liquid phase. The graph shows Temperature \(T\) in Kelvin on the vertical axis and Pressure \(P\) in MPa on the horizontal axis. Isenthalpic curves 1-6 and an Inversion curve are shown. Regions for Cooling and Heating are indicated, separated by the inversion curve. The liquid-vapor equilibrium curve is also shown at the bottom.

that is, the Joule- Thomson coefficient is the slope at a point on the isenthalpic expansion curve. The locus of all points at which the Joule- Thomson coefficient is zero (the locus of the maxima of the isenthalpic curves) is known as the inversion curve and is shown for nitrogen in Fig. 11- 2, as a heavy closed curve. The region inside the inversion curve, where \(\mu\) is positive, is called the region of cooling, that is, the final temperature of the gas is less than the initial temperature; whereas outside the inversion curve, where \(\mu\) is negative, it is called the region of heating, that is, the final temperature is more than the initial temperature. For example, expansion represented by movement from point (a) on Fig. 11- 2 to either (b) or (c) raises the temperature of the gas, whereas movement from points (c) or (d) to (e) lowers the temperature of the gas.

Since the Joule- Thomson coefficient involves \(T\) , \(P\) , and \(h\) , we seek a relation among the differentials of \(T\) , \(P\) , and \(h\) . In general, the difference in molar enthalpy between two neighboring equilibrium states is

\[d h = T d s + \nu d P,\]

and, according to the second \(T d s\) equation,

\[T d s = c_{P}d T - T\left(\frac{\partial\nu}{\partial T}\right)_{P}d P.\]

Substituting for \(T d s\) , we get

===== Page 90 =====

280 PART I: Fundamental Concepts

\[dh = c_{P}dT - \left[T\left(\frac{\partial\nu}{\partial T}\right)_{P} - \nu \right]dP,\]

\[dT = \frac{1}{c_{P}}\left[T\left(\frac{\partial\nu}{\partial T}\right)_{P} - \nu \right]dP + \frac{1}{c_{P}}dh.\]

Since \(\mu = (\partial T / \partial P)_{h}\)

\[\mu = \frac{1}{c_{P}}\left[T\left(\frac{\partial\nu}{\partial T}\right)_{P} - \nu \right]. \quad (11.2)\]

This is the thermodynamic equation for the Joule- Thomson coefficient. The condition for the inversion curve, \(\mu = 0\) , is met when the quantity in the brackets vanishes. It is evident that, for 1 mol of an ideal gas, the Joule- Thomson coefficient equals

\[\mu = \frac{1}{c_{P}}\left(T\frac{R}{P} -\nu\right) = 0.\]

In other words, the final temperature equals the initial temperature under all conditions for an ideal gas in the Joule- Thomson expansion. For real gases, the final temperature may be either more or less than the initial temperature. As a result of the latter possibility, the most important application of the Joule- Thomson expansion is cooling of gases and their liquefaction.

### 11.2 LIQUEFACTION OF GASES BY THE JOULE-THOMSON EXPANSION

An inspection of the isenthalpic curves and the inversion curve of Fig. 11- 2 shows that, for the Joule- Thomson expansion to give rise to cooling, the initial temperature of the gas must be below the point where the inversion curve intercepts the temperature axis, that is, below the maximum inversion temperature. Otherwise, the Joule- Thomson expansion raises the temperature of the gas. For many gases, room temperature is already below the maximum inversion temperature, so that no precooling is necessary. Thus, if air is compressed to a pressure of 200 atm and a temperature of \(52^{\circ}C\) , then, after throttling to a pressure of 1 atm, it will be cooled to \(23^{\circ}C\) . On the other hand, if helium originally at 200 atm and \(52^{\circ}C\) is throttled to 1 atm, its temperature will rise to \(64^{\circ}C\) .

Figure 11- 3 shows that, before the Joule- Thomson expansion can produce cooling in hydrogen, the hydrogen must be cooled below 200 K. Liquid nitrogen at \(77\mathrm{K}\) is used for this purpose. To produce Joule- Thomson cooling in helium, the helium needs to be cooled below \(43\mathrm{K}\) . Liquid hydrogen is sometimes used as a refrigerant, with appropriate precautions. Table 11.1 gives the

===== Page 91 =====

**FIGURE 11-3** The graph shows Temperature \(T\) in Kelvin on the vertical axis and Pressure \(P\) in MPa on the horizontal axis. Isenthalpic curves and an Inversion curve for Hydrogen are shown.

**TABLE 11.1** Maximum inversion temperatures

| Gas | Maximum inversion temperature, K |
| :--- | :--- |
| Xe | 1486 |
| CO₂ | 1275 |
| Kr | 1079 |
| Ar | 794 |
| CO | 644 |
| N₂ | 607 |
| Ne | 228 |
| H₂ | 204 |
| ⁴He | 43 |

maximum inversion temperatures of a few gases. The inversion curve for \(^4\mathrm{He}\) is shown in Fig. 11- 4.

It is clear from Figs. 11- 2, 11- 3, and 11- 4 that, once a gas has been precooled to a temperature lower than the maximum inversion temperature, the optimum pressure from which to start throttling corresponds to a point on the inversion curve. Starting at this pressure and ending at atmospheric pressure, the process produces the largest temperature drop, which may not be large enough to produce liquefaction. Consequently, the gas that has been cooled by throttling is used to cool the incoming gas, which after throttling

===== Page 92 =====

282 PART I: Fundamental Concepts

**FIGURE 11-4** Inversion curve for \(^{4}\mathrm{He}\) . The graph shows Temperature \(T\) in Kelvin on the vertical axis and Pressure \(P\) in MPa on the horizontal axis. A single curve is shown, with a point for saturated liquid marked.

becomes still cooler. After successive cooling processes, the temperature of the gas is lowered to such a temperature that, after throttling, it becomes partly liquefied. The device used for this purpose, a countercurrent heat exchanger, is shown in Fig. 11- 5.

The gas, after precooling, is sent through the middle tube of a long coil of double- walled pipe. After throttling, it flows back through the outer annular space surrounding the middle pipe. For the heat exchanger to be efficient, the temperature of the gas as it leaves must differ only slightly from the temperature at which it entered. To accomplish this, the heat exchanger must be quite long and well insulated, and the gas must flow through it with sufficient speed to cause turbulent flow, so that there is good thermal contact between the opposing streams of gas.

When the steady state is finally reached, liquid is formed at a constant rate: for every mass unit of gas supplied, a certain fraction \(y\) is liquefied, and the fraction \(1 - y\) is returned to the pump. Considering only the heat exchanger and throttling valve to be completely insulated, as shown in Fig. 11- 6, we have a process in which the molar enthalpy of 1 mol of entering gas is equal to the molar enthalpy of \(y\) units of emerging liquid plus the molar enthalpy of \(1 - y\) units of emerging gas. if

\[h_{l} = \mathrm{molar~enthalpy~of~entering~gas~at~}(T_{i},P_{i}),\]
\[h_{L} = \mathrm{molar~enthalpy~of~emerging~liquid~at~}(T_{L},P_{L}),\]

and

\(h_{f} = \mathrm{molar~enthalpy~of~emerging~gas~at~}(T_{f},P_{f}),\)

===== Page 93 =====

**FIGURE 11-5** Apparatus for the liquefaction of a gas by means of the Joule- Thomson expansion. A diagram shows a compressor, cooler, heat exchanger, and throttle valve. High-pressure and low-pressure paths are indicated.

**FIGURE 11-6** Throttling valve and heat exchanger in steady state. A diagram shows 1 mole of gas entering at \(h_i, T_i, P_i\), passing through a heat exchanger and throttle valve, and emerging as \(y\) moles of liquid and \(1-y\) moles of gas.

===== Page 94 =====

284 PART I: Fundamental Concepts

then

\[h_{i} = y h_{L} + (1 - y)h_{f},\]

or

\[y = \frac{h_{f} - h_{L}}{h_{f} - h_{L}}. \quad (11.3)\]

In the steady state, \(h_{L}\) is determined by the pressure on the liquid, which fixes the temperature, and hence is constant. The final molar enthalpy \(h_{f}\) is determined by the pressure drop in the return tube and the temperature at point \(C\) , which is only a little below that at point \(A\) ; hence, \(h_{f}\) remains constant. The initial molar enthalpy \(h_{i}\) refers to a temperature \(T_{i}\) that is fixed, but at a pressure that may be chosen at will. Therefore, the liquefied fraction \(y\) may be varied only by varying \(h_{i}\) . From Eq. (11.3), it is seen that the fraction \(y\) that is liquefied will be a maximum when \(h_{i}\) is a minimum; and, since \(h_{i}\) may be varied only by varying the pressure, \(h_{i}\) will be a minimum when

\[\left(\frac{\partial h_{i}}{\partial P}\right)_{T = T_{i}} = 0.\]

But, from Eqs. (2.6) and (11.1),

\[\left(\frac{\partial h}{\partial P}\right)_{T} = -\left(\frac{\partial h}{\partial T}\right)_{P}\left(\frac{\partial T}{\partial P}\right)_{h} = -c_{P}\mu ;\]

hence, for \(y\) to be a maximum,

\[\mu = 0\qquad \mathrm{at} T = T_{i},\]

or the point \((T_{i},P_{i})\) must lie on the inversion curve in order to maximize the fraction \(y\) of the liquid.

In the design of gas- liquefaction equipment, a TS diagram showing isobars and isenthalps is particularly useful. For example, to calculate the fraction \(y\) liquefied in the steady state, the three molar enthalpies \(h_{i}, h_{f}\) , and \(h_{L}\) may be obtained directly from such a diagram. TS diagrams for hydrogen and for helium are shown in Figs. 11- 7 and 11- 8, respectively.

The use of the Joule- Thomson expansion to produce liquefaction of gases has two advantages: (1) There are no moving parts at low temperature that would be difficult to lubricate. (2) The lower the temperature, the larger the drop in temperature for a given pressure drop, as shown by the isenthalps in Figs. 11- 2 and 11- 3. For the purpose of liquefying hydrogen and helium, however, a disadvantage is that the hydrogen must be precooled with liquid nitrogen, and the helium must be precooled with liquid hydrogen.

An approximately reversible adiabatic expansion against a piston or a turbine blade always produces a decrease in temperature, no matter what the original temperature. Therefore, if a gas like helium could be made to do external work adiabatically through the medium of an engine or a turbine, then, with the aid of a heat exchanger, the helium could be liquefied without precooling. But, this method has the disadvantage that the temperature drop on adiabatic expansion decreases as the temperature decreases.

===== Page 95 =====

286 PART I: Fundamental Concepts

A combination of both methods has been used successfully. Thus, adiabatic reversible expansion is used to achieve a temperature within the inversion curve, and then the Joule- Thomson expansion completes the liquefaction. Kapitza was the first to liquefy helium in this way, with the aid of a small expansion engine that was lubricated by the helium itself. Later, he liquefied air with the aid of a centrifugal turbine only a trifle larger than a watch.

The most significant development in the field of gas liquefaction is the Collins helium liquefier, commonly called a "closed- cycle refrigerator," in which helium undergoes adiabatic expansion in a reciprocating engine. The expanded gas is then used to cool the incoming gas in the usual countercurrent heat exchanger. When the temperature is low enough, the gas passes through a throttling valve, and Joule- Thomson cooling is used to complete the liquefaction. The unit consists of a four- stage compressor, a gasholder, a purifier, and a cryostat containing the engines and heat exchangers, Dewar flasks, vacuum pumps, and gauges.

### 11.3 FIRST-ORDER PHASE TRANSITIONS: CLAUSIUS-CLAPEYRON EQUATION

In the familiar phase transitions - melting, vaporization, and sublimation - as well as in some less familiar transitions, such as from one polymorph of ice to another, the temperature and pressure remain constant while the entropy and volume change. Consider \(n_0\) moles of material in phase \(i\) with molar entropy \(s^{(i)}\) and molar volume \(\nu^{(i)}\) . Both \(s^{(i)}\) and \(\nu^{(i)}\) are functions of \(T\) and \(P\) , and hence remain constant during the phase transition that ends with the material in phase \(f\) with molar entropy \(s^{(f)}\) and molar volume \(\nu^{(f)}\) . (The different phases are indicated by superscripts in order to reserve subscripts for specifying different states of the same phase or different substances.) Let \(x\) equal the fraction of the initial phase that has been transformed into the final phase at any moment. Then, the entropy \(S\) and the volume \(V\) of the mixture at any moment are given by

\[S = n_0(1 - x)s^{(i)} + n_0xs^{(f)},\]

and

\[V = n_0(1 - x)\nu^{(i)} + n_0x\nu^{(f)},\]

and \(S\) and \(V\) are seen to be linear functions of \(x\) .

If the phase transition takes place reversibly at constant pressure, the change of enthalpy per mole is given by

\[\Delta h = T(s^{(f)} - s^{(i)}).\]

The change in molar enthalpy, therefore, means that there is a change of molar entropy. Since

\[d g = -s d T + \nu d P,\]

===== Page 96 =====

then

\[s = -\left(\frac{\partial g}{\partial T}\right)_{P},\]

and

\[\nu = \left(\frac{\partial g}{\partial P}\right)_{T}.\]

We may characterize the familiar phase transitions by either of the following equivalent statements:

1. There are changes of molar entropy and of molar volume.

2. The first-order derivatives of the molar Gibbs function change discontinuously.

Any phase change that satisfies these requirements is known as a phase change of the first order. For such a phase change, the temperature variations of \(g, s, \nu\) , and \(c_{P}\) are shown by four graphs in Fig. 11- 9, which shows a phase change from liquid to vapor. The phase transition may be regarded as accomplished reversibly in either direction. Notice that the molar Gibbs function has a single value at the vaporization temperature, but the slope is discontinuous.

The fourth graph, showing the behavior of molar heat capacity \(c_{P}\) , is particularly significant in that the \(c_{P}\) of a mixture of two phases during the

**FIGURE 11-9** Characteristics of a first- order phase transition: (a) molar Gibbs function; (b) molar entropy; (c) molar volume; (d) molar heat capacity. The graphs show: (a) \(g\) vs \(T\), (b) \(- (\partial g/\partial T)_P\) vs \(T\), (c) \((\partial g/\partial P)_T\) vs \(T\), and (d) \(c_P\) vs \(T\). Each graph shows a discontinuity at the transition temperature.

===== Page 97 =====

phase transition is infinite. This is true because the transition occurs at constant \(T\) and \(P\) . When \(P\) is constant, \(dT = 0\) ; or when \(T\) is constant, \(dP = 0\) . Therefore,

\[c_{P} = T\left(\frac{\partial s}{\partial T}\right)_{P}\to \infty ;\qquad \beta = \frac{1}{\nu}\left(\frac{\partial\nu}{\partial T}\right)_{P}\to \infty ;\qquad \kappa = -\frac{1}{\nu}\left(\frac{\partial\nu}{\partial P}\right)_{T}\to \infty .\]

It should be noticed, however, that these statements are true only when both phases are present. As shown in Fig. 11- 9(d), the \(c_{P}\) of phase \((i)\) remains finite right up to the transition temperature. It does not "anticipate" the onset of a phase transition by starting to rise before this temperature is reached. This is always true of a first- order transition, but not of other transitions, as will be shown in Chap. 14.

The second \(T d S\) equation provides an indeterminate result when applied to a first- order phase transition. For 1 mol,

\[T d s = c_{P}d T - T\nu \beta d P,\]

where \(c_{P} = \infty\) and \(dT = 0\) ; also, \(\beta = \infty\) and \(dP = 0\) .

The first \(T d S\) equation, however, may be integrated through the phase transition. When 1 mol of substance is converted reversibly, isothermally, and is

