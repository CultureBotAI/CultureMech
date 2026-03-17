
# Class: TemperatureValue

Temperature with units

URI: [culturemech:TemperatureValue](https://w3id.org/culturemech/TemperatureValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PreparationStep]++-%20temperature%200..1>[TemperatureValue&#124;value:float;unit:TemperatureUnitEnum],[SterilizationDescriptor]++-%20temperature%200..1>[TemperatureValue],[StorageConditions]++-%20temperature%201..1>[TemperatureValue],[StorageConditions],[SterilizationDescriptor],[PreparationStep])](https://yuml.me/diagram/nofunky;dir:TB/class/[PreparationStep]++-%20temperature%200..1>[TemperatureValue&#124;value:float;unit:TemperatureUnitEnum],[SterilizationDescriptor]++-%20temperature%200..1>[TemperatureValue],[StorageConditions]++-%20temperature%201..1>[TemperatureValue],[StorageConditions],[SterilizationDescriptor],[PreparationStep])

## Referenced by Class

 *  **None** *[➞temperature](preparationStep__temperature.md)*  <sub>0..1</sub>  **[TemperatureValue](TemperatureValue.md)**
 *  **None** *[➞temperature](sterilizationDescriptor__temperature.md)*  <sub>0..1</sub>  **[TemperatureValue](TemperatureValue.md)**
 *  **None** *[➞temperature](storageConditions__temperature.md)*  <sub>1..1</sub>  **[TemperatureValue](TemperatureValue.md)**

## Attributes


### Own

 * [➞value](temperatureValue__value.md)  <sub>1..1</sub>
     * Description: Numeric temperature value
     * Range: [Float](types/Float.md)
 * [➞unit](temperatureValue__unit.md)  <sub>1..1</sub>
     * Description: Temperature unit
     * Range: [TemperatureUnitEnum](TemperatureUnitEnum.md)
