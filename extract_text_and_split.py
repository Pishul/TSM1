import os
import fitz
import pymupdf4llm
import shutil

SOURCE_DIRS = {
    "Home_Works": r"a:\Downloads\TSM1-Final\Home_Works",
    "Lecture_Notes": r"a:\Downloads\TSM1-Final\Lecture_Notes",
    "Source_Book": r"a:\Downloads\TSM1-Final\Source_Book"
}

TARGET_DIRS = {
    "Home_Works": r"a:\Downloads\TSM1-Final\TSM1\Home_Works",
    "Lecture_Notes": r"a:\Downloads\TSM1-Final\TSM1\lecture_notes",
    "Source_Book": r"a:\Downloads\TSM1-Final\TSM1\textbook"
}

TEMP_DIR = r"a:\Downloads\TSM1-Final\TSM1\temp_ocr"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Track what needs manual agent OCR
to_ocr = []

for category, src_dir in SOURCE_DIRS.items():
    if not os.path.exists(src_dir):
        continue
    tgt_dir = TARGET_DIRS[category]
    
    for filename in os.listdir(src_dir):
        if not filename.lower().endswith(".pdf"):
            continue
            
        # Optional: For testing, limit to a few files if needed, but we will process all
        
        pdf_path = os.path.join(src_dir, filename)
        md_filename = filename.replace('.pdf', '.md')
        out_md = os.path.join(tgt_dir, md_filename)
        
        if os.path.exists(out_md):
            print(f"Skipping {filename}, already exists.")
            continue
            
        print(f"\nAnalyzing {filename.encode('utf-8', 'replace').decode('utf-8')}...")
        try:
            doc = fitz.open(pdf_path)
            # Check text ratio on first 3 pages
            text_len = sum(len(doc[i].get_text().strip()) for i in range(min(3, len(doc))))
            
            is_text = text_len > 100
            
            if is_text:
                print(f"  -> Typed PDF detected. Extracting with pymupdf4llm...")
                md_text = pymupdf4llm.to_markdown(pdf_path)
                with open(out_md, 'w', encoding='utf-8') as f:
                    f.write(md_text)
                print(f"  -> Saved {md_filename}")
            else:
                print(f"  -> Scanned PDF detected. Splitting for Agent OCR...")
                # Write header to target file
                with open(out_md, 'w', encoding='utf-8') as f:
                    f.write(f"# {filename}\n\n")
                    
                for page_num in range(len(doc)):
                    page_pdf_name = f"{filename}_page_{page_num+1}.pdf"
                    page_pdf_path = os.path.join(TEMP_DIR, page_pdf_name)
                    
                    # Save single page pdf
                    single_doc = fitz.open()
                    single_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
                    single_doc.save(page_pdf_path)
                    single_doc.close()
                    
                    to_ocr.append({
                        "file": page_pdf_path,
                        "target": out_md,
                        "page": page_num + 1
                    })
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Save the list of pages to process so the orchestrator can read it
import json
with open(os.path.join(TEMP_DIR, "ocr_queue.json"), "w", encoding="utf-8") as f:
    json.dump(to_ocr, f, ensure_ascii=False, indent=2)

print(f"\nDone! Prepared {len(to_ocr)} pages for Agent OCR.")
