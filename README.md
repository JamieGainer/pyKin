# pyKin
Package for python particle physics analyses

The goal is to create a unified analysis framework in clean object-oriented python that can solve any problem I've run into on
the analysis side of my particle physics research or might run into in the future.  Ideally this will ultimately also meet
many other physicists needs.  My background is in phenomenology (i.e. theory rather than experiment) so while I hope this code 
may help experimentalists, I imagine that my background will strongly affect design choices, at least initially.

## Implementation Notes/ Plan

### subpackage: lorentz

I've written a lightweight tensor algebra package called einstein_tensor (JamieGainer/einstein_tensor).  Of particular
importance for pyKin is that we will build momentum four vectors the Tensor object from einstein_tensor.  We will add methods 
of use in high energy physics, particularly the ability to initialize from eta, phi, pT, and mass instead of E, px, py, pz.  

This class will be part of a "lorentz" subpackage that also contains functions that return the flat space metric tensor and 
the Levi-Civita tensor, as well as methods for boosts and rotations in 4-D.

### subpackage: event

This subpackage will be further divided into sub-subpackages for different types of events.  I anticipate lhco (for 
events that can be specified with information in LHC Olympics format) and lhe (for events that can be specified with
information in Les Houches Accord format), but there may be more at some point.  The very first step is to implement the
lhco sub-subpackage

### sub-subpackage: event.lhco

This sub-subpackage contains classes for physics_object, event, event_list, variable, cut, cut_based_analysis, and histogram_data

**physics_object**: contains a frame 

### subpackage: io

This package contains



## License Notes

I haven't looked into the details of this yet, but I plan for this package to be open source and free to use, though I also
anticipate being the only developer, at least at first.
