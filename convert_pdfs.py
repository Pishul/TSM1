import os
import time
import io
import fitz  # PyMuPDF
try:
    import pymupdf4llm
except ImportError:
    pymupdf4llm = None
import pyautogui
pyautogui.FAILSAFE = False
import pyperclip
import win32clipboard
from PIL import Image

SOURCE_DIRS = [
    r"a:\Downloads\TSM1-Final\Home_Works",
    r"a:\Downloads\TSM1-Final\Lecture_Notes",
    r"a:\Downloads\TSM1-Final\Source_Book"
]

TARGET_DIRS = {
    "Home_Works": r"a:\Downloads\TSM1-Final\TSM1\Home_Works",
    "Lecture_Notes": r"a:\Downloads\TSM1-Final\TSM1\lecture_notes",
    "Source_Book": r"a:\Downloads\TSM1-Final\TSM1\textbook"
}

def send_image_to_clipboard(image):
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:] # skip BMP header
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def extract_via_deepseek_rpa(img, page_num):
    print(f"  -> Page {page_num}: Using DeepSeek RPA for OCR...")
    send_image_to_clipboard(img)
    
    # Switch to Chrome/DeepSeek manually or assume user has it focused
    # We will assume Chrome is focused
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)
    
    prompt = "لطفا متن و فرمول‌های این تصویر را به صورت دقیق با فرمت Markdown و LaTeX استخراج کن. فقط متن خروجی را بنویس و هیچ توضیح اضافه‌ای نده."
    pyperclip.copy(prompt)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    
    print("  -> Waiting 45 seconds for DeepSeek generation...")
    time.sleep(45)
    
    print("  -> Copying response...")
    # Select all, copy
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    
    # Deselect
    pyautogui.click(10, 100) # click near top left to deselect
    
    page_text = pyperclip.paste()
    # Find the text after our prompt
    prompt_idx = page_text.rfind(prompt)
    if prompt_idx != -1:
        response = page_text[prompt_idx + len(prompt):]
        # Remove any leading DeepSeek labels
        response = response.strip()
        if response.startswith("DeepSeek"):
            response = response[8:].strip()
        return response
    else:
        print("  -> ERROR: Prompt not found in clipboard text. Taking the whole clipboard as fallback (might contain history).")
        return page_text[-2000:] # Just a chunk

def process_pdf(pdf_path, target_dir):
    filename = os.path.basename(pdf_path)
    md_filename = filename.replace('.pdf', '.md')
    output_md_path = os.path.join(target_dir, md_filename)
    
    if os.path.exists(output_md_path):
        print(f"Skipping {filename}, already processed.")
        return

    print(f"Processing {filename}...")
    doc = fitz.open(pdf_path)
    
    # Check if the PDF is text-based by sampling first 3 pages
    sample_text = ""
    for i in range(min(3, len(doc))):
        sample_text += doc[i].get_text()
        
    is_text_based = len(sample_text.strip()) > 500
    
    if is_text_based and pymupdf4llm is not None:
        print(f"  -> {filename} is text-based. Using pymupdf4llm...")
        md_text = pymupdf4llm.to_markdown(pdf_path)
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(md_text)
        print(f"  -> Saved {md_filename}")
    else:
        print(f"  -> {filename} is image-based (or pymupdf4llm missing). Starting DeepSeek RPA...")
        print("  !!! PLEASE BRING CHROME (DEEPSEEK) TO THE FOREGROUND IN 10 SECONDS !!!")
        for i in range(10, 0, -1):
            print(f"  Starting in {i}...")
            time.sleep(1)
            
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {filename}\n\n")
            
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=150)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            md_text = extract_via_deepseek_rpa(img, page_num + 1)
            with open(output_md_path, 'a', encoding='utf-8') as f:
                f.write(f"\n## Page {page_num + 1}\n\n")
                f.write(md_text)
                f.write("\n\n---\n")

def main():
    for source_dir in SOURCE_DIRS:
        dir_name = os.path.basename(source_dir)
        target = TARGET_DIRS.get(dir_name)
        if not target or not os.path.exists(source_dir):
            continue
            
        for filename in os.listdir(source_dir):
            if filename.lower().endswith('.pdf'):
                # FOR TESTING, JUST PROCESS ONE SMALL FILE
                if filename == "TSMI - HW1.pdf" or filename == "TSM I- n10.pdf":
                    pdf_path = os.path.join(source_dir, filename)
                    process_pdf(pdf_path, target)

if __name__ == "__main__":
    main()
