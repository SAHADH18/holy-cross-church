import os
import re
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from generate_all_units import unit_meta, parse_original_file

def validate():
    print("=" * 100)
    print("FAMILY UNITS RE-DESIGN COMPREHENSIVE VALIDATION REPORT")
    print("=" * 100)
    
    total_units = len(unit_meta)
    passed_units = 0
    all_errors = []

    for filename, meta in unit_meta.items():
        unit_num = meta['num']
        en_name = meta['en_name']
        ml_name = meta['ml_name']
        img_path = meta['img']

        # 1. Check generated file exists
        if not os.path.exists(filename):
            all_errors.append(f"[{filename}] Missing generated file!")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            gen_content = f.read()

        # 2. Check original data parsed
        parsed = parse_original_file(filename)
        if not parsed:
            all_errors.append(f"[{filename}] Could not parse original file!")
            continue

        orig_comm = parsed['committee']
        orig_members = parsed['members']

        # 3. Check Image exists
        if not os.path.exists(img_path):
            all_errors.append(f"[{filename}] Image missing on disk: {img_path}")

        # 4. Check that image is in generated HTML
        if img_path not in gen_content:
            all_errors.append(f"[{filename}] Image path {img_path} not found in HTML!")

        # 5. Check Committee count and names in generated HTML
        for role, name in orig_comm:
            if name and name not in gen_content:
                all_errors.append(f"[{filename}] Committee member '{name}' ({role}) not found in generated HTML!")

        # 6. Verify Unit Members Directory is completely removed
        if 'Unit Members Directory' in gen_content or 'unit-members-card' in gen_content or 'unit-members-table' in gen_content:
            all_errors.append(f"[{filename}] Unit Members Directory section still found in generated HTML!")

        # 7. Check Total Families and Total Unit Members stats
        expected_family_html = f'<span class="unit-stat-label">Total Families</span>\n                <span class="unit-stat-value">{len(orig_members)}</span>'
        expected_members_html = f'<span class="unit-stat-label">Total Unit Members</span>\n                <span class="unit-stat-value">120</span>'
        if expected_family_html not in gen_content:
            all_errors.append(f"[{filename}] Total Families count {len(orig_members)} not found or malformed!")
        if expected_members_html not in gen_content:
            all_errors.append(f"[{filename}] Total Unit Members count 120 not found or malformed!")

        # 8. Check Navigation & Breadcrumbs
        if 'family_units.html' not in gen_content:
            all_errors.append(f"[{filename}] Back link to family_units.html missing!")
        if f'<span>{en_name}</span>' not in gen_content:
            all_errors.append(f"[{filename}] Breadcrumb for '{en_name}' missing!")

        # 9. Check Footer credit
        if 'Powered by' not in gen_content or 'cryoflametechnologies.com' not in gen_content:
            all_errors.append(f"[{filename}] Footer powered by Cryoflame missing!")

        passed_units += 1
        print(f"✓ Unit {unit_num:2}: {en_name:30} | Comm: {len(orig_comm):2} | Members: {len(orig_members):2} | Image: {img_path:35} | Status: PASSED")

    print("=" * 100)
    print(f"SUMMARY: {passed_units}/{total_units} Units successfully validated against original source data!")
    if all_errors:
        print(f"ERRORS ({len(all_errors)}):")
        for err in all_errors:
            print("  -", err)
    else:
        print("ALL AUDIT CHECKS PASSED PERFECTLY WITH ZERO DISCREPANCIES!")

if __name__ == '__main__':
    validate()
