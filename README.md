# Digitizing Well-test Pressure PDF Reports into Machine-readable Information
FA'23 Project with Bureau of Ocean Management (BOEM) through Discovery Research Program at UC Berkeley

## Project Objective
The project objective is to extract data from **diverse well test reports and convert this information into a machine-readable format**. Divergent styling, fonts, headers, and subsections are prevalent, resulting in the difficult standardization task.
The documents exhibit various forms of degradation, such as **smudging, blurring, and special characters**. Recognizing this, we focus on the development of a robust model capable of adapting to and functioning with the considerable diversity inherent in the well test reports. We hoped to create a model to address the challenges posed by variations in document presentation and accommodate the full spectrum of document quality. This involved leveraging **Optical Character Recognition (OCR)** and complementary methodologies to extract data reliably and enhance the interpretability of information from documents that deviated from standard templates.
The end product is an accurate database of subsurface pressure and temperature information, linked to a specific location and depth and collected at a specific time, which can be used to evaluate reservoir properties for oil and gas and carbon storage assessments. Such achievement and insight is especially valuable because these **well test reports are legacy data – it will likely never be collected in the same location again – and so if it was not made machine readable, it will not be available to future users.**

## Files
### Deliverables
- Final symposium poster _(BOEM Final Poster)_
- Final report detailing all our progress & methods _(Deliverable - BOEM Final Report)_
### 3 methods for this project
- Tabula _([Peiying] R_and_Tabula.ipynb)_
- “pdftools” library in R _([Peiying] Text_Extraction_Using_R.html)_
- Custom Box Trained Model _([Gio] program.py]_
- Archived initial attempt of above ^ _([Sandya] rectangulate then ocr.ipynb)_
### Miscellaneous achievements
- Function to score how many words detected _([Gio] function to get % of words detected.ipynb)_
- Notebook to choose pages from PDF _([Sandya] pdf_to_needed_table_image.ipynb)_

#### Collaborators: Sandya Wijaya, Giovanni Hernandez, Peiying Guan
