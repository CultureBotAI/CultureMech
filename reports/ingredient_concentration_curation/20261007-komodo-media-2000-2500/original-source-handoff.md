# Original Recipe Follow-up

This is a source-inspection handoff, not an applied quantity correction. Source
PDF text was inspected through the web tool during the cohort review. Screenshot
requests returned references without visible image content, so no visual page
inspection is claimed. No locally hashed PDF capture is recorded by this file.

## Medium 650

The official [DSMZ recipe, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf)
states: "Add 20 mM pyruvate after autoclaving."
It lists the basal salts, yeast extract, vitamin B12 and tap-water input
separately. This corroborates the API preparation context but does not validate
the imported 1.741 G_PER_L mass conversion or establish a stock strength/dose.

Next: capture and hash the original source, reconcile the exact pyruvate form,
represent the source's molar amount at the post-autoclave stage, and retain any
unknown stock inputs as unknown. Inspect the complete normalized record again
before a guarded change. The local pyruvate ingredient already exists.

## Medium 762

The official [DSMZ recipe, page 1](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium762.pdf)
states: "Prepare the medium without Na2CO3 and NaHCO3 in 900 ml distilled water"
and separately specifies preparing the two carbonate salts in 100 ml water,
sterilizing separately and adding to the cooled medium. This confirms a real
preparation boundary, not a single autoclaved flat recipe.

Next: preserve the two source input volumes and their preparation stages.
Neither the input-volume sum nor the nominal table denominator is evidence
that the final solution was made up to a measured litre. Keep stage-specific
input amounts separate from final-medium concentrations.

## Medium 752

The web tool could not open the [original PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium752.pdf)
on two attempts. That is a tool-specific access failure, not proof the PDF is
absent. The accessible API source and complete local context remain captured.
The actual [official mobile recipe page](https://www.bacmedia.dsmz.de/medium/752?mobile=1)
was then opened and inspected, not merely read as a search excerpt. Its table
also specifies 1 ml of the 0.36 g/l manganese stock and 1 ml of the 50 g/l iron
stock, with 1000 ml water; the liquid and agar preparation instructions are
distinct. This corroborates the API dose interpretation without establishing
an independently measured final litre. Retry an authorized direct PDF retrieval
before deciding original-source access.
The known issue is the two metal-stock volume doses encoded as mass
concentrations; the current local record is liquid, not the separate agar branch.

Bibliographic years remain unknown. A copyright footer is not treated as a
verified publication year.
