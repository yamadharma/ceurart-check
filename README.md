# CEURART document verification

# Table of Contents

1.  [Key issues](#orgd3523da)
2.  [Utilities](#org233c1ea)

<a id="orgd3523da"></a>

# Key issues

-   Frequent errors are:
    -   not using Libertinus fonts;
    -   using an old CEURART template;
    -   not using the correct copyright phrase;
    -   not having selectable text in the PDF file, preventing indexing by GoogleScholar and the like.


<a id="org233c1ea"></a>

# Utilities

-   The document verification utilities for CEUR-WS can be found in the repository: <https://github.com/yamadharma/ceurart-check>.
-   `check-pdf-errors`:
    -   Checks pdf files.
    -   Checks for the presence of the phrase 'Creative Commons' in pdf files.
        -   This is to check if the text can be highlighted (if the document is not an image).
    -   Checking for the use of Libertinus fonts.
    -   Checking for duplication of pdf files.
-   `check-index-errors`:
    -   Checks the `index.html` file.

