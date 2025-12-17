#
# File: check-libbyhead.py
# Version: 0.95
#
# Checks whether the PDF files in the current directory have issues in matching the CEURART style.
# (C) 2024-2025 by Manfred Jeusfeld. This script is made available under the
# Creative Commons Attribution-ShareAlike CC-BY-SA 4.0 license.
#
# Call by python3 $HOME/bin/check-libbyhead.py <pdffile> 
# Returns ecit code 0 if the headings on page 1 of the pdffile are in Libertinus font
# Otherwise returns exit code 1
#
# Created with the help of GenAI; requires python3 and pdfminer.six
#  pip install pdfminer.six
#

import sys
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTChar, LTAnno
import statistics
import logging

# Configure pdfminer.six to suppress its own logging output
logging.getLogger('pdfminer').setLevel(logging.WARNING)

# --- Hardcoded Parameters ---
TARGET_FONT = 'Libertinus'
SIZE_FACTOR = 1.3        # Check fonts 30% larger than the body text
SUCCESS_THRESHOLD = 0.80 # 80% usage of the target font in headings required
PAGES_TO_CHECK = [0]     # Only check the first page (index 0)
# ----------------------------

def get_all_chars(layout):
    """
    Helper function to recursively yield all LTChar objects from a layout element.
    """
    for item in layout:
        if isinstance(item, LTChar):
            # Skip LTAnno objects which are technical annotations, not rendered characters
            if not isinstance(item, LTAnno): 
                yield item
        elif isinstance(item, list) or hasattr(item, '__iter__'):
            yield from get_all_chars(item)

def check_font_usage_headings_p1(pdf_path: str):
    # 1. First Pass: Collect all font sizes for heuristic determination (Page 1 only)
    all_font_sizes = []
    
    try:
        # Check only the pages specified in PAGES_TO_CHECK (i.e., page 1)
        for page_layout in extract_pages(pdf_path, page_numbers=PAGES_TO_CHECK): 
            for item in get_all_chars(page_layout):
                all_font_sizes.append(round(item.size, 2))
    except Exception as e:
        print(f"Error during font size collection: {e}", file=sys.stderr)
        return False, 0.0, 0

    if not all_font_sizes:
        return False, 0.0, 0

    try:
        # Find the body font size mode/median from Page 1 data
        body_font_size = statistics.mode(all_font_sizes)
    except statistics.StatisticsError:
        body_font_size = statistics.median(all_font_sizes)

    heading_size_threshold = body_font_size * SIZE_FACTOR

    # 2. Second Pass: Check only characters above the heading size threshold (Page 1 only)
    heading_chars_total = 0
    heading_chars_target = 0
    
    for page_layout in extract_pages(pdf_path, page_numbers=PAGES_TO_CHECK): 
        for character in get_all_chars(page_layout):
            
            if character.size >= heading_size_threshold:
                
                heading_chars_total += 1
                font_name = character.fontname.upper()
                
                if TARGET_FONT.upper() in font_name:
                    heading_chars_target += 1

    if heading_chars_total == 0:
        return False, 0.0, 0

    # 3. Calculate and return success/failure
    usage_percentage = heading_chars_target / heading_chars_total
    
    if usage_percentage >= SUCCESS_THRESHOLD: 
        return True, usage_percentage, heading_chars_total
    else:
        return False, usage_percentage, heading_chars_total

# --- Execution Block (Minimal Output) ---
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <path_to_pdf>", file=sys.stderr)
        sys.exit(1)

    pdf_file = sys.argv[1]
    
    passed, _, _ = check_font_usage_headings_p1(pdf_file)

    # Use exit code only for communication (0 for success, 1 for failure)
    if passed:
#        print(f"RESULT: pass")
        sys.exit(0)
    else:
#        print(f"RESULT: fail")
        sys.exit(1)
