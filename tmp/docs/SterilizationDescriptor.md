
# Class: SterilizationDescriptor

Sterilization method and parameters

URI: [culturemech:SterilizationDescriptor](https://w3id.org/culturemech/SterilizationDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%200..1-++[SterilizationDescriptor&#124;method:SterilizationMethodEnum;pressure:float%20%3F;duration:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20sterilization%200..1>[SterilizationDescriptor],[MediaRecipe])](https://yuml.me/diagram/nofunky;dir:TB/class/[TemperatureValue],[TemperatureValue]<temperature%200..1-++[SterilizationDescriptor&#124;method:SterilizationMethodEnum;pressure:float%20%3F;duration:string%20%3F;notes:string%20%3F],[MediaRecipe]++-%20sterilization%200..1>[SterilizationDescriptor],[MediaRecipe])

## Referenced by Class

 *  **None** *[➞sterilization](mediaRecipe__sterilization.md)*  <sub>0..1</sub>  **[SterilizationDescriptor](SterilizationDescriptor.md)**

## Attributes


### Own

 * [➞method](sterilizationDescriptor__method.md)  <sub>1..1</sub>
     * Description: Sterilization technique
     * Range: [SterilizationMethodEnum](SterilizationMethodEnum.md)
 * [➞temperature](sterilizationDescriptor__temperature.md)  <sub>0..1</sub>
     * Description: Temperature setting
     * Range: [TemperatureValue](TemperatureValue.md)
 * [➞pressure](sterilizationDescriptor__pressure.md)  <sub>0..1</sub>
     * Description: Pressure in psi or kPa (for autoclaving)
     * Range: [Float](types/Float.md)
 * [➞duration](sterilizationDescriptor__duration.md)  <sub>0..1</sub>
     * Description: Sterilization duration
     * Range: [String](types/String.md)
 * [➞notes](sterilizationDescriptor__notes.md)  <sub>0..1</sub>
     * Description: Special instructions (e.g., "Filter-sterilize heat-labile components separately")
     * Range: [String](types/String.md)
