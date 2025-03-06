import re

def is_timecode(line):
    """Check if a line contains SMPTE timecode (format like 00:00:00:00)."""
    timecode_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}[:;]\d{2}')
    return bool(timecode_pattern.match(line.strip()))

def process_captions(input_file, output_file):
    """
    Process captions from input_file and write to output_file.
    
    - Remove timecode lines
    - Consolidate consecutive speech from same speaker
    - Format speaker names in bold
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    # Split into blocks (each block is separated by a blank line)
    blocks = content.split('\n\n')
    processed_blocks = []
    
    previous_speaker = None
    previous_block_index = -1
    
    for block in blocks:
        if not block.strip():
            continue
            
        lines = block.strip().split('\n')
        current_lines = []
        
        # Skip the first line if it's a timecode
        start_idx = 0
        if lines and is_timecode(lines[0]):
            start_idx = 1
            
        if start_idx >= len(lines):
            # Skip blocks that only have timecode
            continue
            
        speaker = lines[start_idx].strip()
        text = ' '.join(line for line in lines[start_idx+1:] if line.strip())
        
        if speaker == previous_speaker and processed_blocks:
            # Same speaker as previous block, append text to previous block
            processed_blocks[previous_block_index] += ' ' + text
        else:
            # New speaker, create a new block
            formatted_block = f"**{speaker}**: {text}"
            processed_blocks.append(formatted_block)
            previous_block_index = len(processed_blocks) - 1
            previous_speaker = speaker
    
    # Write processed blocks to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n\n'.join(processed_blocks))