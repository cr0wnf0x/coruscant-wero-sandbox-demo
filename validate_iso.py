import sys
import xml.etree.ElementTree as ET

def validate_iso(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Remove namespace prefixes for easier checking
        # ISO 20022 uses different namespaces for different versions
        tag_name = root.tag.split('}')[-1] if '}' in root.tag else root.tag
        
        # Look for GrpHdr and CstmrCdtTrfInitn
        # We search with a wildcard for namespaces
        grphdr_found = False
        initn_found = False
        
        for elem in root.iter():
            local_name = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if local_name == 'GrpHdr':
                grphdr_found = True
            elif local_name == 'CstmrCdtTrfInitn':
                initn_found = True
        
        if grphdr_found and initn_found:
            print("VALIDATION_SUCCESS")
            sys.exit(0)
        else:
            missing = []
            if not grphdr_found: missing.append("<GrpHdr>")
            if not initn_found: missing.append("<CstmrCdtTrfInitn>")
            print(f"Error: Missing required blocks: {', '.join(missing)}")
            sys.exit(1)
            
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_iso.py <path_to_xml>")
        sys.exit(1)
    
    validate_iso(sys.argv[1])
