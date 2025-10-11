# Table of Contents

1.  [Key issues](#org9192900)
2.  [Utilities](#org77cff69)
    1.  [`check-pdf-errors`](#org74f3826)
    2.  [`check-index-errors`](#orgfe91471)
    3.  [`ceur-add-pagenum`](#orgdbf37cf)

CEURART document verification.


<a id="org9192900"></a>

# Key issues

-   Frequent errors are:
    -   not using Libertinus fonts;
    -   using an old CEURART template;
    -   not using the correct copyright phrase;
    -   not having selectable text in the PDF file, preventing indexing by GoogleScholar and the like.


<a id="org77cff69"></a>

# Utilities

-   The document verification utilities for CEUR-WS can be found in the repository: <https://github.com/yamadharma/ceurart-check>


<a id="org74f3826"></a>

## `check-pdf-errors`

-   Source: <https://ceur-ws.org/check-pdf-errors>
-   Checks pdf files.
-   Checks for the presence of the phrase 'Creative Commons' in pdf files.
    -   This is to check if the text can be highlighted (if the document is not an image).
-   Checking for the use of Libertinus fonts.
-   Checking for duplication of pdf files.


<a id="orgfe91471"></a>

## `check-index-errors`

-   Source: <https://ceur-ws.org/check-index-errors>
-   Checks the `index.html` file.
-   Rules:
    -   paper PDFs that are in the directory but not listed in `index.html`;
    -   papers that are linked in `index.html` but not included in the directory.


<a id="orgdbf37cf"></a>

## `ceur-add-pagenum`

-   Repo: <https://github.com/amato-gianluca/ceur-add-pagenum>
-   A small Python script for counting the number of pages in the PDF files linked to an index.html document (prepared for submission to CEUR-WS), and updating the CEURPAGES fields.
-   The script does not alter the PDF files, just the `index.html`.
-   The script depends on the `lxml` and `PyPDF2` packages.
