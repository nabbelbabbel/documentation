.. image:: scine_header.svg
      :alt: SCINE 

What is SCINE?
==============

The software for chemical interaction networks (SCINE) aims to offer developments
for 21st-century computational quantum chemistry. A central idea underpinning the design
of SCINE is the automated exploration of chemical reaction networks with interactive
steering. Reaching this goal has required new developments in many traditional branches of
quantum chemistry. SCINE is intended to provide a unifying framework for all these developments.

SCINE shoots for maximum flexiblity due to its modular design. Each module offers useful
functionality in its own right and can be used as such, but it can be enhanced by the other SCINE
modules. Currently, the following modules have been released:

- autoCAS, which automates the notorious active-orbital-space selection step in multi-configurational calculations,
- QCMaquis, which implements a second-generation density matrix renormalization group (DMRG) algorithm, that, together with the OpenMolcas project, makes multi-configurational CASSCF-type calculations with dynamical correlation for large active spaces accessible,
- ReaDuct, which offers several algorithms for the refinement of reaction paths and associated transition-state searches, and
- Sparrow, which provides a fast implementation of many semiempirical quantum chemical models.

Visit `scine.ethz.ch <https://scine.ethz.ch/>`_ to learn more about SCINE and its individual modules and about future releases.
