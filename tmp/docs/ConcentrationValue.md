
# Class: ConcentrationValue

Quantified concentration with units

URI: [culturemech:ConcentrationValue](https://w3id.org/culturemech/ConcentrationValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20concentration%201..1>[ConcentrationValue&#124;value:string;unit:ConcentrationUnitEnum;per_volume:string%20%3F],[SolutionDescriptor]++-%20concentration%200..1>[ConcentrationValue],[SolutionDescriptor],[IngredientDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20concentration%201..1>[ConcentrationValue&#124;value:string;unit:ConcentrationUnitEnum;per_volume:string%20%3F],[SolutionDescriptor]++-%20concentration%200..1>[ConcentrationValue],[SolutionDescriptor],[IngredientDescriptor])

## Referenced by Class

 *  **None** *[➞concentration](ingredientDescriptor__concentration.md)*  <sub>1..1</sub>  **[ConcentrationValue](ConcentrationValue.md)**
 *  **None** *[➞concentration](solutionDescriptor__concentration.md)*  <sub>0..1</sub>  **[ConcentrationValue](ConcentrationValue.md)**

## Attributes


### Own

 * [➞value](concentrationValue__value.md)  <sub>1..1</sub>
     * Description: Numeric value or range
     * Range: [String](types/String.md)
 * [➞unit](concentrationValue__unit.md)  <sub>1..1</sub>
     * Description: Concentration unit
     * Range: [ConcentrationUnitEnum](ConcentrationUnitEnum.md)
 * [➞per_volume](concentrationValue__per_volume.md)  <sub>0..1</sub>
     * Description: Volume basis (e.g., "per liter", "per 100 mL")
     * Range: [String](types/String.md)
