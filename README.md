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
of use in high energy physics, particularly the ability to initialize from eta, phi, pT, and mass instead of E, px, py, pz 
and the ability to obtain any component (in either parameterization) simply.
We will also give each four-vector a frame attribute so that we keep track of which frame a four-vector is being
measured in.

This class will be part of a "lorentz" subpackage that also contains functions that return the flat space metric tensor and 
the Levi-Civita tensor, as well as methods for boosts and rotations in 4-D.

### subpackage: event

This subpackage will be further divided into sub-subpackages for different types of events.  I anticipate lhco (for 
events that can be specified with information in LHC Olympics format) and lhe (for events that can be specified with
information in Les Houches Accord format), but there may be more at some point.  The very first step is to implement the
lhco sub-subpackage

### sub-subpackage: event.lhco

This sub-subpackage contains classes for physics_object, event, event_list, variable, cut, cut_based_analysis, and 
output_data.  I'm going to write these classes for LHCO first-- later versions may contain abstract base classes for all
of these objects that lhco, lhe, and possible other event classes inherit from.

**physics_object**: is a base class containg a four-vector object representing the momentum of the physics object.
Inheriting from it are
**photon**, **electron**, **muon**, (hadronic) **tau**, **jet**, **hadron_collider_missing_energy**, 
**lepton_collider_missing_energy**, **stable_charged_particle**

**event** an event contains a dictionary with the keys: "photons", "electrons", "muons", "taus", "jets", "b-jets",
"missing_energy", and "stable_charged_particles".  The values for these keys are lists of the appropriate physics object.
The event class also comes with a set of simple methods for obtaining components of four vectors (or actual four-vectors)
or for iterating over particles of a given type.  Some of these return a custom "PhysicsObjectNotFound" exception.  We sort 
each list by pT (descending) and enforce that there is only one missing_energy object in the event whose momenta is the sum of 
all missing_energy objects passed to the event.  (Each event can have either a hadron_collider_missing_energy object or a
lepton_collider_missing_energy_object.  The former is strictly transverse, the latter is not.)  An event can also have
additional attributes like a weight.  An event also contains variables (described below).

**event_list** is a list of events, possibly with addiitonal information (like a total cross section).  It contains a method
for giving its objects a weight (assuming uniform weights).

**variable** is an object containg an evaluate method that takes an event as input, uses only standard methods in event, 
and returns the value of the variable.  It also contains a name attribute that is used to specify the variable in cut and output_data objects.

**cut** is an object containing a variable, a threshold (which can be a numerical value or another variable), and a comparison
(>, <. >=, <=, or ==) as well as an evaluate method that returns a bool indicating whether the event is cut or not.

**cut_based_analysis** basically a set of cuts.  has an evaluate method that performs cuts on an event_list and returns an 
event_list consiting of the events that pass the cuts.

**output_data** an object that is initialized with a list of variables and an event_list and returns a dictionary where the 
keys are variable names and the associated values are lists with the value of the variable in each event in event_list.  (if 
if the variable can't be calculated for the event, it's value will be zero).  There is also a key for "weights" and the 
associated list is the event weights.


### subpackage: io

This package contains code for reading various datafiles (like lhco event files, root files, MadGraph banner files).



## License Notes

I haven't looked into the details of this yet, but I plan for this package to be open source and free to use, though I also
anticipate being the only developer, at least at first.
