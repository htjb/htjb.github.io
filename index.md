---
title: Introduction
---

I am a third year PhD student in Physics at Cavendish Astrophysics,
University of Cambridge. I work on data analysis techniques for global or sky-averaged 21-cm cosmology
as part of the
[Cm-Wave Experimental Radio Cosmology](https://cavendishcmwavecosmology.weebly.com/) group and as part of the
[REACH (Radio Experiment for the Analysis of Cosmic Hydrogen)](https://www.astro.phy.cam.ac.uk/research/research-projects/reach/reach)
collaboration under the
supervision of Dr Eloy de Lera Acedo, Dr Will Handley and Dr Anastasia Fialkov.

21-cm cosmology is a field of study which aims to track the redshifted 21-cm
emission from neutral hydrogen throughout cosmic history in an effort to
determine when the first galaxies formed and what those galaxies were like. We know
very little about the first luminous objects to form between the CMB and the current
era of the galaxies dominated by large scale structure. While probes like JWST
give us a window to distant galaxies, as far back as z=16, 21-cm cosmology can
provide statistical information about the population of galaxies over the redshift range
z = 5 - 150.

There are a number of on going and future experimental efforts in the field with future missions
planned to the far side of the Moon. While a promising probe the view to the first
galaxies is fogged by emission from our own and other galaxies, emission from our own atmosphere
and made challenging by the non-uniform responses of our instruments. I have worked on a
number of these challenges during my PhD.

I have looked  at the
modelling of Galactic and extra-galactic emission with Maximally Smooth Functions (MSFs).
MSFs have very smooth properties making them ideally suited for modelling smooth synchrotron and
free-free emission foregrounds in 21-cm experiments. They can also be used as
a tool to help identify non-smooth systematics in data sets that could be introduced by the instrument or
the environment around the telescope. I am the lead author and maintainer of the
code [maxsmooth](https://github.com/htjb/maxsmooth) which can be used to rapidly
and efficiently fit MSFs. I have demonstrated applications of this software to data
from LEDA, EDGES and SARAS2.

In addition, I have worked on novel techniques for emulating the global (or sky-averaged)
21-cm signal with neural networks. The resultant signal emulator
[globalemu](https://github.com/htjb/globalemu) is 102 times faster than the previous state of the art.
It has recently been used to model data from the SARAS instruments and will be used extensively by the
REACH collaboration for physical signal modelling in a nested sampling loop.

You can read about the application of globalemu and maxsmooth to the SARAS2 data and the resultant
constraints that we derived on the properties of the first galaxies  
[here](https://arxiv.org/abs/2201.11531). A similar work on the SARAS3 data has recently been accepted for publication
at Nature Astronomy.

More recently, I have worked on the use of Normalizing flows in a machine-learning enhanced Bayesian workflow
with the code [margarine](https://github.com/htjb/margarine).

<center><img src="{{ site.url }}/assets/portrait.jpg" width="30%" alt-text="Portrait image"></center>

<center>
<a href='https://arxiv.org/search/?searchtype=author&query=Bevins%2C+H+T+J'><img src="{{ site.url }}/assets/arxiv.png" width="10%" alt-text="arXiv Link"></a>
<a href='https://github.com/htjb'><img src="{{ site.url }}/assets/github_logo.png" width="10%" alt-text="Github Link"></a>
<a href='https://www.linkedin.com/in/harry-bevins-641a6512a/'><img src="{{ site.url }}/assets/linkedin.png" width="10%" alt-text="Linkedin Link"></a>
<a href='https://ui.adsabs.harvard.edu/search/q=author%3A%22Bevins%2C%20H.%20T.%20J.%22&sort=date%20desc%2C%20bibcode%20desc&p_=0'><img src="{{ site.url }}/assets/ads.png" width="10%" alt-text="ADS Link"></a>
<a href='https://publons.com/researcher/5239833/harry-bevins/'><img src="{{ site.url }}/assets/publons.png" width="10%" alt-text="Publons Link"></a>
</center>
