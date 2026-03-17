
# Class: SupplierInfo

Commercial supplier information

URI: [culturemech:SupplierInfo](https://w3id.org/culturemech/SupplierInfo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20supplier_catalog%200..1>[SupplierInfo&#124;supplier_name:string;catalog_number:string%20%3F;product_url:uri%20%3F;notes:string%20%3F],[MediaVariant]++-%20supplier_info%200..1>[SupplierInfo],[MediaVariant],[IngredientDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[IngredientDescriptor]++-%20supplier_catalog%200..1>[SupplierInfo&#124;supplier_name:string;catalog_number:string%20%3F;product_url:uri%20%3F;notes:string%20%3F],[MediaVariant]++-%20supplier_info%200..1>[SupplierInfo],[MediaVariant],[IngredientDescriptor])

## Referenced by Class

 *  **None** *[➞supplier_catalog](ingredientDescriptor__supplier_catalog.md)*  <sub>0..1</sub>  **[SupplierInfo](SupplierInfo.md)**
 *  **None** *[➞supplier_info](mediaVariant__supplier_info.md)*  <sub>0..1</sub>  **[SupplierInfo](SupplierInfo.md)**

## Attributes


### Own

 * [➞supplier_name](supplierInfo__supplier_name.md)  <sub>1..1</sub>
     * Description: Vendor name (e.g., "Sigma-Aldrich", "Thermo Fisher")
     * Range: [String](types/String.md)
 * [➞catalog_number](supplierInfo__catalog_number.md)  <sub>0..1</sub>
     * Description: Product catalog number
     * Range: [String](types/String.md)
 * [➞product_url](supplierInfo__product_url.md)  <sub>0..1</sub>
     * Description: Direct product link
     * Range: [Uri](types/Uri.md)
 * [➞notes](supplierInfo__notes.md)  <sub>0..1</sub>
     * Description: Additional sourcing notes
     * Range: [String](types/String.md)
