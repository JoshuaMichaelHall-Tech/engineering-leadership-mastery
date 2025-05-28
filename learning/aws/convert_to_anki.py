#!/usr/bin/env python3
"""
Convert semicolon-delimited flashcards to pipe-delimited format for Anki import.
Each line should be: Question; Answer
Output format: Question|Answer|Tag
"""

import sys
import re

def convert_flashcards(input_file, output_file, default_tag="AWS"):
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Split into sections
    sections = content.split('\n## ')
    
    cards = []
    
    for section in sections:
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        # Get section title (remove any '#' at the start)
        section_title = lines[0].replace('#', '').strip()
        if not section_title:
            continue
            
        # Process each line in the section
        for line in lines[1:]:
            if ';' in line:
                parts = line.split(';', 1)
                if len(parts) == 2:
                    question = parts[0].strip()
                    answer = parts[1].strip()
                    if question and answer:
                        # Clean up the tag
                        tag = section_title.replace(' ', '_').replace('(', '').replace(')', '')
                        cards.append(f"{question}|{answer}|{tag}")
    
    # Write to output file
    with open(output_file, 'w') as f:
        for card in cards:
            f.write(card + '\n')
    
    print(f"Converted {len(cards)} flashcards")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_to_anki.py input.md output.txt")
        sys.exit(1)
    
    convert_flashcards(sys.argv[1], sys.argv[2])