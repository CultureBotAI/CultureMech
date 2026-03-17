
# Class: StorageConditions

Storage requirements for prepared medium

URI: [culturemech:StorageConditions](https://w3id.org/culturemech/StorageConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%201..1-++[StorageConditions&#124;light_condition:LightConditionEnum%20%3F;shelf_life:string%20%3F;container_type:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20storage%200..1>[StorageConditions],[SolutionDescriptor]++-%20storage_conditions%200..1>[StorageConditions],[SolutionDescriptor],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%201..1-++[StorageConditions&#124;light_condition:LightConditionEnum%20%3F;shelf_life:string%20%3F;container_type:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20storage%200..1>[StorageConditions],[SolutionDescriptor]++-%20storage_conditions%200..1>[StorageConditions],[SolutionDescriptor],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞storage](mediaRecipe__storage.md)*  <sub>0..1</sub>  **[StorageConditions](StorageConditions.md)**
 *  **None** *[➞storage_conditions](solutionDescriptor__storage_conditions.md)*  <sub>0..1</sub>  **[StorageConditions](StorageConditions.md)**

## Attributes


### Own

 * [➞temperature](storageConditions__temperature.md)  <sub>1..1</sub>
     * Description: Storage temperature
     * Range: [TemperatureValue](TemperatureValue.md)
 * [➞light_condition](storageConditions__light_condition.md)  <sub>0..1</sub>
     * Description: Light exposure requirement
     * Range: [LightConditionEnum](LightConditionEnum.md)
 * [➞shelf_life](storageConditions__shelf_life.md)  <sub>0..1</sub>
     * Description: Duration of stability
     * Range: [String](types/String.md)
 * [➞container_type](storageConditions__container_type.md)  <sub>0..1</sub>
     * Description: Recommended container (e.g., "glass bottle", "polypropylene tube")
     * Range: [String](types/String.md)
 * [➞notes](storageConditions__notes.md)  <sub>0..1</sub>
     * Description: Additional storage tips
     * Range: [String](types/String.md)
