# GT Gas Distributor - SPARTA Simulation

3D molecular dynamics simulation of xenon gas flow through a distributor geometry.

## Xenon Gas Parameters

### Species File (species/xe.species)
- Atomic weight: 131.29 amu (Wikipedia)
- Molecular mass: 2.18E-25 kg (131.29 amu × 1.66054E-27 kg/amu)
- Monatomic noble gas: 0 rotational and vibrational degrees of freedom

### VSS Collision Model (vss/xe.vss)
Since SPARTA does not provide built-in Xenon parameters, these were estimated from another DSMC paper I found:

**Collision Diameter: 5.65e-10 m**
Couldn't find SPARTA Xenon examples, but this link https://pubs.aip.org/aip/jap/article/137/15/154701/3344208/Rarefied-xenon-flow-in-orificed-hollow-cathodes seems to have a value. Should maybe verify this; I just copied it from a random paper.

**Omega (ω): 0.85**
Temperature exponent in VSS viscosity relation μ ∝ T^ω. Paper above gives 0.85 for this value.

**Other Params:**
- Tref = 273.15 K (standard reference temperature)
- Alpha = 1.4 (standard VSS parameter for monatomic gases)

## Simulation Setup
- Domain: 3.0" × 1.13" × 0.25" (76.2 mm × 28.7 mm × 6.35 mm)
- Grid: 350 × 150 × 50 cells (2.625M total)
- Inlet: 100 Pa, 10 mg/s mass flow, 300K
- Gas: 100% Xenon
- Surface: Accommodation coefficient = 1.0