
# Class: PreparationStep

A step in medium preparation

URI: [culturemech:PreparationStep](https://w3id.org/culturemech/PreparationStep)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%200..1-++[PreparationStep&#124;step_number:integer;action:PreparationActionEnum;description:string;duration:string%20%3F;equipment:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20preparation_steps%200..*>[PreparationStep],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%200..1-++[PreparationStep&#124;step_number:integer;action:PreparationActionEnum;description:string;duration:string%20%3F;equipment:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20preparation_steps%200..*>[PreparationStep],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞preparation_steps](mediaRecipe__preparation_steps.md)*  <sub>0..\*</sub>  **[PreparationStep](PreparationStep.md)**

## Attributes


### Own

 * [➞step_number](preparationStep__step_number.md)  <sub>1..1</sub>
     * Description: Sequential order
     * Range: [Integer](types/Integer.md)
 * [➞action](preparationStep__action.md)  <sub>1..1</sub>
     * Description: Action type
     * Range: [PreparationActionEnum](PreparationActionEnum.md)
 * [➞description](preparationStep__description.md)  <sub>1..1</sub>
     * Description: Detailed instruction
     * Range: [String](types/String.md)
 * [➞temperature](preparationStep__temperature.md)  <sub>0..1</sub>
     * Description: Temperature for this step
     * Range: [TemperatureValue](TemperatureValue.md)
 * [➞duration](preparationStep__duration.md)  <sub>0..1</sub>
     * Description: Time duration (e.g., "15 minutes", "overnight")
     * Range: [String](types/String.md)
 * [➞equipment](preparationStep__equipment.md)  <sub>0..1</sub>
     * Description: Required equipment (e.g., "autoclave", "magnetic stirrer")
     * Range: [String](types/String.md)
 * [➞notes](preparationStep__notes.md)  <sub>0..1</sub>
     * Description: Additional tips or warnings
     * Range: [String](types/String.md)
